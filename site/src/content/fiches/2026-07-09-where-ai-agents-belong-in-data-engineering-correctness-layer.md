---
title: "Where AI Agents Belong in Data Engineering: The Correctness Layer"
date: 2026-07-09
url: https://www.ssp.sh/blog/where-agents-belong-in-de/
authors: [Simon Späth, ssp.sh]
keywords: [data engineering, agents, correctness layer, tokens, discipline]
theme: Data
tone: opinion
used_in: ["2026-07-09"]
---

## Résumé

Simon Späth propose une grille de lecture pour savoir où les agents IA sont réellement utiles en data engineering, à travers trois niveaux (chat, autonome, tooling dédié). Sa thèse centrale tient en une formule : **correctness over confidence**. Comme les LLM produiront toujours des réponses avec assurance, y compris fausses, la discipline d'ingénierie consiste à bâtir une « couche de correction » autour d'eux plutôt qu'à leur faire confiance. Il détaille où chaque niveau d'agent aide dans le cycle de vie DE, et illustre la notion de « blast radius » (rayon d'impact) d'une action d'agent.

## Points clés

- Trois niveaux d'agents en data engineering : phase de chat, autonome, et tooling dédié — chacun aide à des étapes différentes du cycle de vie.
- Principe directeur : **correctness over confidence** — un agent sûr de lui mais faux est plus dangereux qu'un agent qui doute.
- La discipline d'ingénierie avec l'IA consiste à construire une couche de correction, pas à supprimer la vérification.
- Notion de « blast radius » : évaluer l'ampleur des dégâts qu'une action d'agent peut causer avant de la lui déléguer.
- Optimisation de l'usage des tokens et cas d'usage typiques (renommage/évolution de colonnes et de logique) traités comme des exemples concrets.

## Analyse approfondie

Pourquoi utiliser des agents en data engineering, et à quels niveaux nous aident-ils réellement à être productifs ? Le point de départ de Späth est que les LLM produiront toujours des sorties formulées avec assurance — y compris quand elles sont fausses. C'est de là que découle tout le reste.

**Les trois niveaux d'agents en data engineering.** L'auteur distingue trois modes d'usage : la phase de chat (l'agent assiste, l'humain garde la main), l'autonome (l'agent exécute des tâches de bout en bout), et le tooling dédié (des outils spécialisés construits autour du modèle). Chaque niveau correspond à un degré d'autonomie différent et à un rayon d'impact différent.

**Où, dans le cycle de vie DE, chaque niveau aide vraiment.** Tous les agents ne servent pas partout. Certaines étapes du cycle de vie (exploration, prototypage) tolèrent une autonomie élevée ; d'autres (production, transformations critiques) exigent une couche de vérification stricte. Faire correspondre le bon niveau d'agent à la bonne étape est le cœur de la décision d'architecture.

**Quelle discipline d'ingénierie pour travailler avec l'IA ?** La réponse tient dans l'idée de couche de correction. Puisqu'on ne peut pas rendre le modèle fiable par construction, on rend le système fiable : tests, garde-fous, vérifications déterministes autour de la sortie de l'agent. La formule de l'auteur, **correctness over confidence**, résume l'inversion : on ne demande plus au modèle d'être sûr, on construit ce qui garantit qu'il a raison.

**La couche de correction pour les data engineers.** Concrètement, c'est l'ensemble des mécanismes qui interceptent et valident ce que l'agent produit avant que ça touche la production : contrats de données, tests, revue. L'auteur illustre avec un exemple de « blast radius » — mesurer l'ampleur des dégâts possibles d'une action (par ex. renommer des colonnes et changer la logique associée) avant de la déléguer à un agent.

**Améliorer l'usage des tokens.** L'auteur aborde enfin l'optimisation de la consommation de tokens, en traitant les cas d'usage typiques comme des occasions de discipline plutôt que de dépense aveugle.

## Pourquoi ça compte

« Correctness over confidence » est peut-être la formule la plus juste pour cadrer le travail avec des agents en 2026 : la valeur n'est pas dans l'autonomie brute de l'agent, mais dans la qualité de la couche de vérification qu'on construit autour. Une boussole utile pour toute équipe qui industrialise des agents.
