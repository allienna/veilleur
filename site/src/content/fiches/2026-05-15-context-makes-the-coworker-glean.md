---
title: "Context makes the Coworker: Glean preferred ~2.5x as often as off-the-shelf MCP tools, which consumed 30% more tokens in Claude Cowork"
date: 2026-05-15
url: https://www.glean.com/blog/context-makes-the-coworker
authors: [glean.com]
keywords: [MCP, context layer, knowledge graph, token cost, federated search]
theme: IA
tone: research
used_in: ["2026-05-15"]
---

## Résumé

Glean a benchmarké sa couche de contexte (index centralisé + knowledge graph) contre les serveurs MCP standards, en gardant Claude Cowork comme harness constant sur environ 175 requêtes. Résultat : Glean est préféré 2,5 fois plus souvent et consomme 30 % de tokens en moins. Sur les requêtes complexes multi-étapes, le win rate monte à 73 %. La thèse : le MCP standardise la connexion, pas la qualité — et indexer en amont reste plus efficace qu'un federated search qui doit brute-forcer la recherche.

## Points clés

- Glean préféré 2,5x plus souvent qu'un MCP off-the-shelf sur Claude Cowork
- 30 % de tokens en moins en moyenne (43k contre 83k pour Glean vs MCP standard)
- Win rate de 66 % sur tâches simples, 73 % sur tâches complexes multi-étapes
- Le federated search paie un "token tax" : boucles de raisonnement et over-fetching
- La qualité du contexte devient le moat, pas le modèle

## Analyse approfondie

### La promesse, la réalité

La promesse des AI coworkers, c'est qu'un employé peut produire plus quand l'IA est connectée à ses sources de données externes : Google Docs, Gmail, Calendar, Salesforce, Atlassian. Mais réaliser cette promesse demande une IA dont la sortie soit directement utilisable, à un coût en tokens proportionné à la tâche.

Glean a voulu mesurer dans quelle mesure la couche de contexte façonne l'efficacité et le coût d'un AI coworker. Le constat sectoriel est connu : la qualité du contexte (index, knowledge graph) pilote la précision des réponses. Ce qui est moins compris, c'est l'arbitrage économique : un index coûte un peu de stockage en amont, mais réduit la dépendance au compute, qui explose en entreprise à mesure que la consommation de tokens des modèles frontière grimpe.

### Le protocole de benchmark

Pour isoler l'effet de la couche de contexte, Glean a standardisé le harness sur Claude Cowork — donc le même modèle, le même environnement d'exécution. Sur ~175 requêtes, ils ont comparé :
- Le serveur MCP distant de Glean (avec accès à des outils de recherche et d'écriture sur son index unifié)
- Les serveurs MCP off-the-shelf disponibles dans Cowork (federated search par connecteur)

Les deux principaux résultats agrégés :
- Glean préféré ~2,5x plus souvent
- Off-the-shelf consomme ~30 % de tokens en plus

### Le "federated search token tax"

Le MCP standardise la manière dont un modèle se connecte à des outils externes. Mais il ne standardise pas la qualité des outils eux-mêmes. La façon dont un outil est conçu façonne la qualité de la réponse qu'il permet, et le nombre d'appels et de boucles de raisonnement nécessaires pour y arriver.

Deux approches historiques s'opposent pour gérer le contexte en entreprise :
- **Federation** : interroger chaque système indépendamment, avec la recherche fournie out-of-the-box par chaque connecteur. Inconvénient : qualité hétérogène d'un connecteur à l'autre, pas de signaux cross-application, ranking incohérent.
- **Centralized indexing** : ingérer et normaliser les données dans une couche unique, ce qui permet des signaux cross-application et un ranking homogène.

Quand le federated search ne perd pas sur la justesse, il y parvient en brute-forçant le processus : multiples boucles de raisonnement, over-fetching, ce qui fait quasiment doubler la consommation de tokens (83k contre 43k pour Glean) et fait grimper les coûts d'entreprise.

### Plus la requête est complexe, plus l'écart se creuse

Le win rate de Glean est de 66 % sur les requêtes simples, 73 % sur les requêtes complexes en plusieurs étapes qui dépendent de combiner des signaux provenant de différentes apps. Plus la tâche se rapproche de ce qu'on attend vraiment d'un AI coworker (synthétiser des décisions, joindre Slack + Drive + CRM), plus l'avantage de l'index centralisé augmente.

### L'implication économique

Au-delà du benchmark, Glean tire un cadre : à mesure que la consommation de tokens devient un poste de coût significatif en entreprise, investir dans la couche de contexte (et donc dans un peu de stockage en amont) devient un arbitrage de plus en plus rentable. Le modèle est commodity, le contexte ne l'est pas.

## Pourquoi ça compte

C'est l'un des rares benchmarks publics qui isole l'effet de la couche de contexte sur la performance et le coût d'un agent. Pour les équipes qui industrialisent leurs usages IA, le message est limpide : la qualité du contexte est le différenciateur, et elle se chiffre en tokens économisés autant qu'en pertinence gagnée.
