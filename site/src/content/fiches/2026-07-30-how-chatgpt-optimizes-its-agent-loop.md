---
title: "How ChatGPT Optimizes its Agent Loop: Harness, API, and Inference"
date: 2026-07-30
url: https://blog.bytebytego.com/p/how-chatgpt-optimizes-its-agent-loop?utm_source=tldrnewsletter
authors: [ByteByteGo]
keywords: [harness, agent loop, inference, KV cache, cost per task]
theme: IA
tone: research
used_in: ["2026-07-30"]
---

## Résumé

ByteByteGo a interviewé les ingénieurs OpenAI qui ont conçu et déployé les techniques d'efficacité derrière Codex et ChatGPT Work. La thèse : la capacité brute des modèles n'est que la moitié du sujet, l'autre moitié est le **coût par tâche réussie**. Une application agentique comme Codex n'est pas un LLM mais un système à trois couches — harness, API, inférence — et chaque itération de la boucle agentique refait énormément de travail déjà fait. L'article détaille les optimisations appliquées à chaque couche, aucune ne touchant au modèle lui-même.

## Points clés

- La capacité seule ne suffit pas : GPT-5.6 Sol en reasoning max dépasse Fable 5 sur l'Artificial Analysis Coding Agent Index pour moins de la moitié du coût.
- Un LLM ne sait que prédire des tokens : il ne peut ni exécuter une commande, ni éditer un fichier, ni se souvenir entre deux appels. Le harness fournit tout le reste.
- Une requête traverse trois couches : harness (contexte, exécution d'outils en sandbox, boucle), API (auth, rate limits, tokenisation, safety), inférence (fleets de GPU).
- Une tâche lourde peut boucler plus de 100 fois ; une seconde de latence en trop par appel modèle ajoute environ une demi-minute à la tâche.
- Côté harness, quatre techniques : WebSockets persistants, préfixes de prompt stables, découverte d'outils différée, Code Mode.
- Côté API : tokeniser uniquement le delta, et lancer les classifieurs de sécurité en parallèle de l'inférence plutôt qu'avant.
- Côté inférence : routage conscient du cache, gestion du KV cache, decoding spéculatif, séparation prefill/decode.

## Analyse approfondie

### Le contexte

Les labos d'IA avancent plus vite que jamais et publient les modèles les plus capables que nous ayons connus. Récemment, Anthropic a sorti Fable 5, puis OpenAI la famille GPT-5.6 incluant GPT-5.6 Sol, son modèle le plus capable, Kimi a sorti Kimi K3, et Opus 5 est arrivé il y a quelques jours.

**Mais la capacité n'est que la moitié du tableau.** L'autre moitié, c'est combien il coûte à ces modèles d'accomplir une tâche : le *coût par tâche réussie*. Un coût plus bas rend le modèle plus abordable pour les utilisateurs et moins onéreux pour le fournisseur. Un effort énorme, à l'intérieur des labos, est consacré à rendre chaque composant et chaque couche de leurs applications d'IA plus optimisé et plus efficace, pour réduire le coût global. Par exemple, GPT-5.6 Sol en reasoning maximal score plus haut que Fable 5 sur l'Artificial Analysis Coding Agent Index tout en coûtant moins de la moitié.

Pour comprendre quelles techniques sont adoptées dans les labos de pointe, ByteByteGo a rencontré les ingénieurs OpenAI qui ont développé et livré ces techniques dans les systèmes derrière Codex et ChatGPT Work.

### Pourquoi la requête ne va pas directement au LLM

Quand vous confiez une tâche à Codex ou ChatGPT Work — corriger un bug, par exemple — la requête ne part pas directement vers le LLM. C'est plus complexe que ça. Une application d'IA comme Codex n'est pas juste un LLM. C'est un système, avec de nombreux composants. Les requêtes utilisateur traversent plusieurs couches avant que le LLM ne voie le moindre token.

Pour comprendre pourquoi, il faut voir ce qu'est réellement un LLM. Un LLM est un réseau de neurones entraîné à prédire le prochain token. Il prend une séquence de tokens en entrée et produit une séquence de tokens en sortie. **Il ne peut pas exécuter une commande shell, éditer un fichier, ni se souvenir de quoi que ce soit entre deux appels.** Or une tâche agentique comme « corrige ce bug et fais tourner les tests » est essentiellement constituée d'actions. Quelque chose doit transformer les tokens prédits par le modèle en commandes réelles, réinjecter les résultats, et continuer jusqu'à ce que la tâche soit terminée.

### La couche harness

C'est le rôle de la **couche harness**, un système construit au-dessus du LLM pour prendre en charge ces responsabilités. Elle prend la tâche de l'utilisateur en entrée, décide quelles instructions, quelles définitions d'outils et quelle quantité d'historique inclure dans le contexte, et maintient l'historique de conversation. Quand le modèle répond par un appel d'outil, le harness l'exécute selon des politiques d'approbation dans un environnement sandbox, ajoute le résultat, et renvoie la conversation au LLM.

Le harness a deux responsabilités principales. D'abord, il est la **source de vérité** de la conversation : il détient l'enregistrement autoritaire de chaque instruction, message, appel d'outil et résultat d'outil. Ensuite, il exécute la **boucle agentique** : il décide ce qui entre dans le contexte envoyé au LLM, envoie la requête, reçoit la réponse en streaming, la parse, et surveille les appels d'outils. Quand un appel apparaît, il l'exécute sous politique d'approbation dans un sandbox, ajoute le résultat à la conversation, et renvoie le tout au LLM. Il répète cette boucle jusqu'à ce que la tâche soit terminée. Des tâches lourdes peuvent en théorie répéter plus de 100 fois. Chaque itération porte un surcoût : **une seconde supplémentaire par appel modèle ajoute environ une demi-minute à une tâche longue.**

### La couche API

Mais même la requête du harness ne va pas directement au LLM. Dans les applications prêtes pour la production, il y a une couche API (une couche applicative) entre le harness et l'endpoint d'inférence. Cette couche existe parce qu'un vrai produit doit gérer des choses que ni le harness ni le LLM ne couvrent : authentifier l'appelant, appliquer les rate limits, et surtout convertir le texte en identifiants de tokens attendus par le LLM, puis reconvertir les tokens générés en texte.

### La couche inférence

Une fois que la couche API a préparé le contexte et l'a tokenisé en une séquence d'identifiants, c'est au LLM de traiter l'entrée. C'est la **couche inférence** : un endpoint distant adossé à des flottes de GPU hébergeant le modèle. Son travail est d'exécuter le calcul du modèle sur les tokens préparés et de produire la réponse — un nouvel appel d'outil ou la réponse finale — aussi efficacement que possible. Puis de rendre les tokens générés à la couche API.

### Le trajet complet d'une requête

Supposons que vous demandiez à Codex de « tracer la régression du checkout, la patcher, et lancer les tests ». Voici ce qui se passe :

1. Le harness assemble les instructions, les définitions d'outils et votre tâche dans une requête, et l'envoie à l'API.
2. L'API met la requête en mémoire tampon, parse le JSON, et le valide : la requête est bien formée, et le modèle choisi supporte toutes les fonctionnalités demandées. Elle vérifie qui appelle, applique les rate limits, et exécute les preflight checks.
3. L'API rend la conversation dans le format d'entrée du modèle et la tokenise.
4. L'API envoie les tokens à la couche inférence, et démarre **en même temps** ses vérifications de sécurité : des classifieurs qui cherchent par exemple du contenu de cyberattaque ou d'armes biologiques. Ces vérifications font la course pour finir avant que le premier token généré ne revienne.
5. La couche inférence traite le prompt et commence à générer. Sa sortie ici n'est pas la réponse finale : c'est un appel d'outil — chercher « checkout timeout » dans le code.
6. Les tokens générés remontent vers l'API.
7. L'API convertit les tokens en texte et les emballe dans des événements API.
8. L'API les streame vers le harness.
9. Le harness reconnaît l'appel d'outil, exécute la recherche dans son sandbox, ajoute la sortie à la conversation, et renvoie la conversation mise à jour à l'API.

Ce n'est là **qu'une seule itération**. En pratique, une tâche répète cette boucle de nombreuses fois jusqu'à ce que le modèle produise son résumé final et que le harness rende le contrôle à l'utilisateur. Chaque itération refait une grande partie du même travail : l'historique est renvoyé, le texte retokenisé, le prompt reprocessé. **Supprimer ce travail répété est la principale opportunité d'optimisation.**

### Optimiser le harness : le réseau

Du point de vue du harness, la latence vient de quatre sources : le réseau, le traitement du prompt, le contenu du contexte, et les allers-retours de la boucle.

Le harness tourne sur la machine de l'utilisateur, mais le modèle tourne dans les datacenters d'OpenAI : chaque appel modèle est donc un échange réseau. La manière standard de faire cet échange est HTTPS. Le harness ouvre une connexion, envoie une requête contenant tout ce dont le serveur (la couche API) a besoin, et reçoit une réponse. Comme les réponses d'un modèle de langage arrivent progressivement, un token à la fois, les applications de chat utilisent typiquement les Server-Sent Events (SSE) au-dessus d'HTTPS : le client envoie une requête, et le serveur streame la réponse par petits morceaux sur la réponse ouverte.

SSE est une voie à sens unique. C'est parfaitement adapté à l'ère du chat, où un message utilisateur produit un appel modèle et une réponse streamée. **Mais les agents ne fonctionnent pas en une passe.** Un seul tour de Codex peut contenir de nombreux appels modèle. Avec HTTPS, chacun de ces appels est une nouvelle requête portant deux coûts distincts.

Le **premier coût** est l'établissement de connexion. Ouvrir une nouvelle connexion HTTPS implique un handshake TCP suivi d'un handshake TLS : plusieurs allers-retours réseau avant qu'un seul octet utile ne soit transmis. Payer ça une fois par message utilisateur est acceptable ; le payer plusieurs fois à l'intérieur d'un même tour de conversation est cher.

Le **second coût** est la répétition du payload lui-même. HTTP est sans état : chaque requête doit porter tout ce dont le serveur a besoin — les instructions, les définitions d'outils, et toute la conversation jusqu'ici. Au vingtième appel d'outil, le harness renvoie le prompt initial, dix-neuf appels d'outils et dix-neuf résultats, **juste pour ajouter un nouveau résultat à la fin**. Le payload grossit à chaque itération, et le harness passe de plus en plus de temps à uploader des données que le serveur a déjà vues.

Le correctif pour le coût de connexion est d'ouvrir une connexion et de la maintenir vivante, au lieu d'en créer une nouvelle à chaque appel. C'est exactement ce pour quoi les WebSockets sont conçus : un seul handshake initial, puis les deux côtés peuvent envoyer des messages quand ils veulent, sans surcoût par message.

### Les autres techniques

L'article détaille ensuite les autres leviers :

- **Préfixes de prompt stables** au niveau du harness, pour maximiser les taux de hit du cache de prompt côté serveur.
- **Découverte d'outils différée (deferred tool discovery)**, pour ne pas payer le coût de tokens de définitions d'outils dont la tâche n'a pas besoin.
- **Code Mode**, pour laisser le modèle exprimer des séquences d'actions comme du code plutôt que comme une série d'appels d'outils séparés, ce qui réduit le nombre d'allers-retours dans la boucle.
- Au niveau API : **tokenisation du delta uniquement**, et exécution des safety checks **en parallèle** de l'inférence.
- Au niveau inférence : **routage conscient du cache** (envoyer une requête vers la machine qui détient déjà le KV cache correspondant), **gestion du KV cache**, **decoding spéculatif**, et **séparation du prefill et du decode** sur des ressources distinctes.

## Pourquoi ça compte

C'est la meilleure cartographie publique de ce qu'est réellement une application agentique en production : un système à trois couches où l'essentiel des gains ne vient pas du modèle. Pour toute équipe qui construit des agents, c'est directement une liste de leviers d'optimisation applicables — et un rappel que la métrique de référence est le coût par tâche réussie, pas le score au benchmark.
