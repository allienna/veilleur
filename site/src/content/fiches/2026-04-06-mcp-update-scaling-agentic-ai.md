---
title: "Next Major MCP Update Focuses on Scaling Agentic AI"
date: 2026-04-06
url: https://techstrong.ai/articles/next-major-mcp-update-focuses-on-scaling-agentic-ai/?utm_source=tldrdata
authors: [Techstrong AI]
keywords: [MCP, Model Context Protocol, Anthropic, agentic AI, scaling, protocol]
theme: IA
tone: news
used_in: ["2026-04-06"]
---

## Résumé
Lors du MCP Dev Summit à New York, David Soria Parra (Anthropic, co-créateur de MCP) a annoncé la prochaine itération majeure du protocole, prévue pour juin 2026 et co-développée avec Google et Microsoft. Les nouvelles fonctionnalités se concentrent sur le passage à l'échelle des workflows agentiques autonomes : serveurs stateless, gestion native des tâches longue durée, triggers initiés par le serveur, streaming natif et skills réutilisables. Les SDKs MCP sont désormais téléchargés 110 millions de fois par mois, confirmant l'adoption massive du protocole comme standard de facto pour la communication agent-outil.

## Points clés
- La prochaine version majeure de MCP est prévue pour juin 2026, co-développée par Anthropic, Google et Microsoft
- L'annonce a été faite au MCP Dev Summit à New York par David Soria Parra, co-créateur du protocole chez Anthropic
- Les SDKs MCP atteignent 110 millions de téléchargements par mois, signe d'une adoption massive
- Nouvelles fonctionnalités majeures : serveurs stateless pour déploiement on-demand, gestion native des tâches longue durée (long-running tasks), triggers initiés par le serveur
- Ajout de sémantiques de retry, de politiques d'expiration et de streaming natif pour les workflows autonomes
- Introduction de skills réutilisables basés sur la connaissance de domaine
- Focus sur la "progressive discovery" : chargement des outils au runtime pour optimiser l'efficacité des agents
- Exploration de mécanismes de sécurité spécifiques aux interactions agent/serveur MCP

## Analyse approfondie

### Le MCP Dev Summit et le contexte de l'annonce

Le MCP (Model Context Protocol) a été lancé par Anthropic fin 2024 comme protocole ouvert pour standardiser la communication entre les agents IA et leurs outils ou sources de données. En moins d'un an et demi, il s'est imposé comme le standard de facto de l'écosystème : des centaines de serveurs MCP ont été développés par la communauté, des frameworks comme LangChain, CrewAI ou AutoGen l'ont adopté, et les principaux acteurs cloud — AWS, Google, Microsoft Azure — ont intégré le support MCP dans leurs offres.

Le MCP Dev Summit à New York a réuni les principaux contributeurs et utilisateurs du protocole. C'est dans ce contexte que David Soria Parra, l'un des co-créateurs de MCP chez Anthropic, a présenté la roadmap de la prochaine version majeure. La nature collaborative du développement — Anthropic, Google et Microsoft codesignent cette version — est un signal fort : MCP n'est plus un protocole propriétaire Anthropic, mais un effort d'industrie visant à établir un standard interopérable.

### Les limites de MCP actuel que la v2 cherche à résoudre

La version actuelle de MCP a été conçue principalement pour des interactions synchrones et stateful : un agent se connecte à un serveur MCP, appelle des outils, reçoit des résultats. Ce modèle fonctionne bien pour les cas d'usage simples — interroger une base de données, appeler une API REST, lire un fichier — mais montre ses limites pour les workflows agentiques avancés.

Trois catégories de limitations ont motivé la v2 :

1. **Le modèle stateful est coûteux à opérer** : maintenir une connexion persistante entre l'agent et chaque serveur MCP consomme des ressources et complique le déploiement à l'échelle.
2. **Les tâches longue durée ne sont pas bien supportées** : une tâche qui prend plusieurs minutes (ex : générer un rapport complexe, effectuer une migration de données) ne s'intègre pas bien dans le modèle request-response synchrone actuel.
3. **Les agents passifs ne peuvent pas initier des actions** : dans la version actuelle, c'est toujours l'agent qui interroge le serveur MCP. Il n'y a pas de mécanisme pour que le serveur notifie proactivement l'agent d'un événement (ex : "une nouvelle donnée est disponible", "ta tâche de fond est terminée").

### Serveurs stateless : déploiement on-demand

L'une des évolutions les plus attendues est le support des serveurs MCP stateless. Dans ce modèle, le serveur MCP n'a pas besoin de maintenir une connexion persistante avec l'agent. Il peut être instancié à la demande, traiter une requête, et être détruit — comme une fonction serverless.

Ce changement a des implications opérationnelles considérables. Il devient possible de déployer des serveurs MCP comme des fonctions Lambda ou des Cloud Functions, sans maintenir de fleet de serveurs toujours actifs. Le coût d'opération diminue drastiquement pour les serveurs MCP peu sollicités. La scalabilité est simplifiée : pas besoin de dimensionner à l'avance, chaque requête spin up sa propre instance.

Pour les développeurs d'outils, cela réduit également la barrière à l'entrée : construire un serveur MCP stateless est plus simple qu'un serveur stateful, et peut être déployé sur n'importe quelle plateforme serverless standard.

### Task capability : support natif des workflows longue durée

La "task capability" est probablement la fonctionnalité la plus transformatrice de la v2. Elle introduit dans le protocole lui-même un mécanisme pour gérer des tâches asynchrones de longue durée.

Concrètement, au lieu qu'un appel d'outil retourne immédiatement un résultat, il peut retourner un identifiant de tâche. L'agent peut ensuite polling ou s'abonner à des notifications pour savoir quand la tâche est terminée. Des sémantiques de **retry** sont définies au niveau du protocole : si une tâche échoue, dans quelles conditions doit-elle être relancée automatiquement ? Des **politiques d'expiration** permettent de définir une durée maximale après laquelle une tâche est considérée comme ayant échoué.

Ces primitives sont essentielles pour les workflows agentiques autonomes qui orchestrent des tâches complexes. Un agent qui doit analyser un large dataset, faire tourner un job de machine learning ou orchestrer un pipeline de déploiement ne peut pas se permettre d'attendre synchronement le résultat — il doit pouvoir déléguer, passer à autre chose, et revenir quand la tâche est terminée.

### Server-initiated triggers : inversion du flux de contrôle

Les server-initiated triggers représentent une inversion fondamentale du modèle de communication MCP. Jusqu'ici, le flux de contrôle était toujours agent → serveur. Les triggers permettent au serveur d'initier une communication vers l'agent.

Les cas d'usage sont nombreux :
- Un serveur MCP connecté à un système de ticketing peut notifier l'agent quand un nouveau ticket urgent arrive
- Un serveur de monitoring peut alerter l'agent quand un seuil d'alerte est dépassé
- Un serveur de données peut signaler à l'agent qu'un nouveau dataset est disponible pour analyse
- Un serveur d'exécution de tâches peut notifier l'agent de la completion d'un job lancé précédemment

Ces triggers sont nécessaires pour construire des agents véritablement réactifs aux événements, plutôt que des agents qui ne fonctionnent qu'en mode pull.

### Streaming natif

La v2 intègre le streaming natif comme primitive de premier niveau. Actuellement, les résultats d'appels d'outils MCP sont retournés en une seule fois. Le streaming permet de retourner des résultats partiels au fur et à mesure de leur disponibilité.

Pour les agents, cela améliore significativement la réactivité perçue : l'agent peut commencer à traiter les premiers résultats d'une requête pendant que les suivants arrivent encore. Pour les outils qui génèrent du contenu progressivement — génération de texte, lecture de fichiers volumineux, résultats de requêtes larges — c'est un gain de performance et d'expérience utilisateur substantiel.

### Skills réutilisables basés sur la connaissance de domaine

Un autre ajout notable est le concept de **skills réutilisables**. Plutôt que de définir des outils atomiques (appeler une API, lire un fichier), les skills encapsulent une connaissance de domaine plus riche : "comment analyser les métriques de rétention", "comment diagnostiquer un problème de performance SQL", "comment générer un rapport de conformité".

Ces skills peuvent être partagés entre agents et entre organisations, créant un écosystème de savoir-faire agentique réutilisable. C'est une évolution vers quelque chose de plus proche d'une "librairie de comportements" que d'une simple "boîte à outils".

### Progressive discovery : chargement des outils au runtime

Face au problème de la limite du context window des LLMs, la progressive discovery propose une solution élégante : plutôt que de charger tous les outils disponibles dans le contexte de l'agent au démarrage, les outils sont découverts et chargés dynamiquement au runtime, selon les besoins.

Un agent confronté à une tâche commence avec un ensemble minimal d'outils génériques. S'il a besoin d'un outil spécifique, il le demande et le protocole lui fournit sa définition. Cette approche préserve le context window pour le raisonnement et le contenu, et évite la "pollution" du contexte par des centaines de définitions d'outils inutilisés.

### Sécurité des interactions agent/MCP

L'agenda de la v2 inclut aussi une réflexion sur la sécurité spécifique aux interactions agent/serveur MCP — un sujet qui n'était pas adressé dans la v1. Les prompt injections via des serveurs MCP malveillants, l'escalade de privilèges via des chaînes d'agents, et la validation de l'intégrité des résultats des outils sont des vecteurs d'attaque qui deviennent critiques à mesure que MCP est déployé en production dans des contextes sensibles.

## Pourquoi ça compte
La v2 de MCP marque la transition d'un protocole de prototypage vers une infrastructure de production pour les agents autonomes — le support des workflows longue durée, des triggers événementiels et du stateless sont exactement les primitives qui manquaient pour déployer des agents dans des systèmes d'entreprise réels.
