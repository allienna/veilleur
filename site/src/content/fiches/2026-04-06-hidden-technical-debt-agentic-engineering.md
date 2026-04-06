---
title: "The hidden technical debt of agentic engineering"
date: 2026-04-06
url: https://thenewstack.io/hidden-agentic-technical-debt/?utm_source=tldrdata
authors: [The New Stack]
keywords: [agentic AI, technical debt, infrastructure, agents, production, MCP]
theme: IA
tone: opinion
used_in: ["2026-04-06"]
---

## Résumé
En s'inspirant du célèbre article de Google "Hidden Technical Debt in Machine Learning Systems" (2015), cet article dresse un panorama des 7 blocs d'infrastructure qui entourent les agents en production et constituent la dette technique cachée de l'ingénierie agentique. Construire un agent est facile ; le code de l'agent lui-même représente la plus petite partie d'un système en production. Le MCP fournit une interface standardisée pour les outils, mais ne résout pas les problèmes de gestion des credentials, de scope des données ou de propagation des changements d'API.

## Points clés
- La dette technique agentique est analogue à la dette technique des systèmes ML décrite par Google en 2015 : le code "utile" est entouré d'une infrastructure massive et souvent invisible
- 7 blocs d'infrastructure sont identifiés comme sources de dette cachée en production agentique
- Le code de l'agent proprement dit est la plus petite partie du système de production — l'essentiel du travail est dans l'infrastructure périphérique
- MCP standardise l'interface des outils mais ne résout pas la gestion des credentials, le scope des données ni la propagation des changements d'API
- L'observabilité des agents est un défi particulier car les systèmes sont non-déterministes et les traces d'exécution sont complexes à interpréter
- Les evals pour agents sont fondamentalement différents des evals pour modèles : l'environnement, le timing et les effets de bord importent autant que la qualité de la sortie

## Analyse approfondie

### La parallèle avec le papier Google de 2015

En 2015, des ingénieurs de Google ont publié un article fondateur intitulé "Hidden Technical Debt in Machine Learning Systems". Leur constat était provocateur : dans un système ML en production, le code qui implémente le modèle lui-même ne représente qu'une infime fraction du code total. La vaste majorité du code concerne l'infrastructure périphérique — ingestion de données, validation, feature engineering, serving, monitoring, pipeline orchestration. Et c'est cette infrastructure, souvent construite rapidement et sans la même rigueur que le code modèle, qui accumule la dette technique la plus dangereuse.

Dix ans plus tard, l'ingénierie agentique reproduit exactement le même pattern. Les développeurs se concentrent sur le comportement de l'agent — ses prompts, son raisonnement, ses capacités — pendant que l'infrastructure qui permet à l'agent de fonctionner en production s'accumule de manière ad hoc. L'article de The New Stack propose une cartographie de cette dette cachée, structurée en 7 blocs d'infrastructure.

### Bloc 1 : les Integrations

Le premier bloc concerne les intégrations avec les systèmes externes que l'agent utilise. Un agent capable d'appeler des APIs, d'accéder à des bases de données, d'interagir avec des services SaaS doit gérer une complexité d'intégration considérable.

Les deux problèmes principaux sont la **gestion des credentials** et la **propagation des changements d'API**. Pour les credentials : qui détient les secrets ? Comment sont-ils rotés ? Que se passe-t-il quand un token expire en milieu d'exécution ? Pour les changements d'API : quand un service externe met à jour son API, comment l'agent le sait-il ? Comment les outils qu'il utilise sont-ils mis à jour ? La plupart des implémentations actuelles gèrent ce problème de manière artisanale, avec des secrets stockés dans des variables d'environnement et des changements d'API découverts à la première erreur en production.

MCP (Model Context Protocol) standardise l'interface entre l'agent et ses outils, ce qui simplifie certains aspects de l'intégration. Mais MCP ne gère pas les credentials — c'est à l'infrastructure hôte de le faire. Et MCP ne notifie pas l'agent quand une API sous-jacente change — c'est à l'auteur du serveur MCP de maintenir la compatibilité. L'interface est standardisée, mais la complexité de fond reste entière.

### Bloc 2 : le Context Lake

Le deuxième bloc est ce que l'article appelle le "Context Lake" — le stockage et la gestion du contexte d'exécution de l'agent. Un agent en production doit non seulement se souvenir du contexte de la conversation ou de la tâche en cours, mais aussi conserver des traces de ses décisions passées, des états intermédiaires, des résultats d'actions précédentes.

Ce besoin crée une infrastructure de persistence complexe. Combien de contexte faut-il conserver ? Pendant combien de temps ? Comment indexer les traces de décisions pour qu'elles soient retrouvables ? Comment gérer la confidentialité des contextes quand plusieurs utilisateurs partagent le même agent ? Ces questions sont fondamentales pour les agents à longue durée de vie ou ceux qui opèrent sur des workflows multi-steps étendus dans le temps.

### Bloc 3 : l'Observabilité

L'observabilité des agents est radicalement plus difficile que l'observabilité des systèmes logiciels classiques. Dans un service web traditionnel, une trace de requête est déterministe : requête → traitement → réponse. La latence, les erreurs et les performances sont mesurables et reproductibles.

Pour un agent, la trace d'exécution est un graphe complexe de décisions, d'appels d'outils, de résultats intermédiaires et de raisonnements. Deux exécutions du même agent avec le même input peuvent produire des traces complètement différentes — l'une explorant une piste, l'autre une piste totalement différente. Comment définir "l'agent a correctement fonctionné" dans ce contexte ? Quelles métriques suivre ? Comment alerter quand l'agent "se perd" dans une investigation sans fin ?

Des outils émergent pour répondre à ces besoins — LangSmith, Langfuse, Arize Phoenix — mais ils imposent une instrumentation spécifique et ne s'intègrent pas toujours bien avec les frameworks agentiques existants.

### Bloc 4 : la Gouvernance

La gouvernance agentique couvre plusieurs dimensions : qui peut déployer des agents ? Avec quels droits d'accès ? Sur quelles données ? Avec quels outils ? Comment s'assurer qu'un agent ne dépasse pas le périmètre qui lui est assigné ?

Ces questions deviennent critiques à mesure que les agents gagnent en autonomie et en accès aux systèmes internes. Un agent capable d'écrire dans une base de données, d'envoyer des emails, de modifier des fichiers de configuration, représente un risque considérable si ses permissions ne sont pas correctement contrôlées. La surface d'attaque est nouvelle : un prompt injection dans une source de données externe peut amener l'agent à exécuter des actions non souhaitées avec ses droits propres.

### Bloc 5 : Human-in-the-loop

Le cinquième bloc concerne les mécanismes de supervision humaine. Tous les agents ne doivent pas opérer en full autonomy. Pour les tâches à fort impact — modification de données critiques, envoi de communications externes, déclenchement d'actions irréversibles — un point d'approbation humaine est nécessaire.

Concevoir ce mécanisme correctement est plus difficile qu'il n'y paraît. Comment présenter à l'humain les actions que l'agent souhaite exécuter de manière compréhensible ? Comment gérer les timeouts si l'humain ne répond pas ? Comment éviter la "fatigue d'approbation" qui pousse les utilisateurs à approuver sans lire ? Ces questions de UX et d'ergonomie sont souvent négligées dans les implémentations agentiques actuelles.

### Bloc 6 : les Evals pour systèmes non-déterministes

L'évaluation des agents est fondamentalement différente de l'évaluation des modèles de langage classiques. Pour un LLM, on peut construire des benchmarks : pour un input donné, la sortie correcte est X. Pour un agent, la notion de "bonne réponse" est beaucoup plus floue.

Un agent qui atteint le bon résultat final en prenant un chemin inefficace est-il "bon" ? Un agent qui échoue sur un cas particulier mais réussit 95 % des tâches similaires est-il acceptable ? Comment évaluer le comportement de l'agent face à des inputs adversariaux ou des environnements partiellement défaillants ? Les evals agentiques doivent mesurer non seulement la qualité de la sortie finale, mais aussi la qualité du raisonnement intermédiaire, l'efficacité de l'utilisation des outils et la robustesse face aux perturbations.

### Bloc 7 : l'Agent Registry

Le septième bloc concerne la découverte et la gestion des agents eux-mêmes dans une organisation. À mesure que le nombre d'agents déployés augmente — agent analytics, agent support client, agent de code review, agent de génération de contenu — il devient nécessaire de maintenir un registre centralisé.

Ce registre doit documenter les capacités de chaque agent, ses dépendances (outils, modèles, services), ses droits d'accès, ses métriques de performance et son historique de déploiement. Sans ce registre, les organisations se retrouvent avec des proliférations d'agents mal documentés, des duplications de fonctionnalités et des dépendances cachées entre agents.

### La leçon fondamentale

La conclusion de l'article est sans ambiguïté : construire un agent est facile. Le faire fonctionner en production de manière fiable, sécurisée, observable et maintenable est une entreprise d'ingénierie sérieuse. Les équipes qui déploient des agents sans anticiper cette infrastructure accumulent une dette technique qui les rattrapera — tout comme les équipes ML qui ont ignoré la leçon du papier Google de 2015.

## Pourquoi ça compte
Pour toute organisation en train de déployer ou d'évaluer des systèmes agentiques, cet article fournit une grille de lecture pragmatique pour anticiper les investissements d'infrastructure nécessaires — bien au-delà du code de l'agent lui-même — et éviter de reproduire les erreurs de la première vague ML.
