---
title: "The 8 Levels of Agentic Engineering"
date: 2026-03-13
url: "https://www.bassimeledath.com/blog/8-levels-of-agentic-engineering"
authors: ["Bassim Eledath"]
keywords: [agentic engineering, niveaux de maturité, coding agents, productivité, effet multiplayer]
theme: IA
tone: opinion
used_in: ["2026-03-13"]
---

## Résumé

Bassim Eledath propose une taxonomie en 8 niveaux de maturité pour l'ingénierie agentique, de la simple autocomplétion aux workflows entièrement autonomes. L'article met en lumière l'effet multiplayer : la productivité d'un développeur niveau 7 est bridée si son reviewer est niveau 2. Les scores SWE-bench ne se traduisent pas en métriques de productivité réelles, et la différence entre les équipes qui livrent et celles qui stagnent réside dans l'écart entre capacité disponible et pratique effective.

## Points clés

- 8 niveaux progressifs : de l'autocomplétion (niveau 1) aux workflows agentiques complets (niveau 8)
- L'effet multiplayer : votre output dépend du niveau de vos coéquipiers — un wizard niveau 7 est bridé par un reviewer niveau 2
- Les scores SWE-bench ne se traduisent pas en productivité réelle — l'écart est dans la pratique, pas dans la capacité du modèle
- L'équipe d'Anthropic a livré Cowork en 10 jours avec les mêmes modèles qu'une autre équipe incapable de dépasser un POC
- Chaque niveau supérieur représente un saut qualitatif, pas juste incrémental
- Niveaux 1-2 (Tab Complete, Agent IDE) : le plafond est le contexte disponible pour le modèle

## Analyse approfondie

La capacité de codage de l'IA dépasse notre capacité à l'utiliser efficacement. C'est pourquoi toute l'optimisation des scores SWE-bench ne se traduit pas dans les métriques de productivité dont les leaders en ingénierie se soucient réellement. Quand l'équipe d'Anthropic livre un produit comme Cowork en 10 jours et qu'une autre équipe n'arrive pas à dépasser un POC cassé en utilisant les mêmes modèles, la différence est que l'une a comblé l'écart entre capacité et pratique, et l'autre non.

Cet écart ne se comble pas du jour au lendemain. Il se comble par niveaux. Huit niveaux. La plupart des lecteurs ont probablement dépassé les premiers, et ils devraient être impatients d'atteindre le suivant, car chaque niveau supplémentaire représente un bond énorme en production, et chaque amélioration de la capacité des modèles amplifie encore ces gains.

L'autre raison de s'en préoccuper est l'effet multiplayer. Votre output dépend plus qu'on ne le pense du niveau de vos coéquipiers. Imaginons que vous soyez un wizard de niveau 7, soumettant plusieurs PR solides avec vos agents background pendant que vous dormez. Si votre dépôt exige l'approbation d'un collègue, et que ce collègue est au niveau 2, encore en train de reviewer manuellement les PR, cela étouffe votre débit. Il est donc dans votre intérêt de tirer votre équipe vers le haut.

Voici la progression des niveaux observée, de manière imparfaitement séquentielle, en échangeant avec plusieurs équipes et individus pratiquant le codage assisté par IA :

### Niveaux 1 et 2 : Tab Complete et Agent IDE

Ces deux niveaux sont traités rapidement, surtout pour mémoire.

Tout a commencé avec Copilot et l'autocomplétion. Appuyer sur Tab, autocompléter du code. Probablement oublié par beaucoup et complètement sauté par les nouveaux entrants dans l'ingénierie agentique. Cela favorisait ceux qui pouvaient anticiper le prochain bloc de code et avait un plafond bas.

Les IDE avec agent sont venus ensuite. Un chat dans votre IDE était connecté à votre codebase, rendant les éditions multi-fichiers bien plus faciles. C'est à ce moment que les IDE orientés IA comme Cursor ont décollé. Mais le plafond restait toujours le contexte — le modèle ne pouvait aider qu'avec ce qu'il pouvait voir.

La plupart des gens à ce niveau expérimentent aussi le mode plan : traduire une idée brute en un plan structuré étape par étape pour le LLM, itérer dessus, puis déclencher l'implémentation.

### Niveau 3 : Codage agentique

Au niveau 3, le développeur orchestre et l'agent exécute des tâches complètes. Le développeur ne dicte plus chaque ligne — il définit l'objectif et laisse l'agent trouver le chemin. C'est un changement qualitatif fondamental dans la façon dont le travail se fait.

### Niveaux 4 et 5 : Multi-agents et worktrees parallèles

Les niveaux supérieurs introduisent l'utilisation simultanée de plusieurs agents, les worktrees parallèles, et la capacité de travailler sur plusieurs branches en même temps. Le développeur devient un chef d'orchestre qui coordonne des agents spécialisés plutôt qu'un artisan qui produit du code.

### Niveau 6 : Review automatisée

La review automatisée par des agents transforme le goulot d'étranglement traditionnel de la code review. Au lieu d'attendre qu'un collègue humain soit disponible, un agent effectue un premier passage de review, identifiant les problèmes courants et validant la conformité aux standards.

### Niveaux 7 et 8 : Agents background et workflows autonomes

Au sommet de l'échelle, les agents fonctionnent en arrière-plan 24h/24, soumettant des PR de manière autonome. Le développeur se réveille le matin avec des PR prêtes à merger. Le niveau 8 représente des workflows entièrement autonomes où les agents gèrent des cycles complets de développement avec une supervision humaine minimale.

### L'écart qui se creuse

L'article souligne que chaque niveau n'est pas seulement un gain incrémental — c'est un changement qualitatif dans la façon dont le travail se fait. Et l'écart entre les équipes qui adoptent ces niveaux supérieurs et celles qui restent aux niveaux inférieurs ne cesse de se creuser. L'effet multiplayer signifie que même un individu au niveau 7 ne peut pas atteindre son plein potentiel si son équipe est au niveau 2.

C'est pourquoi la montée en compétence n'est pas seulement un choix individuel — c'est un impératif d'équipe. Les organisations qui comprennent cela et investissent dans l'élévation collective du niveau de maturité agentique de leurs équipes créeront un avantage compétitif de plus en plus difficile à rattraper.

## Pourquoi ça compte

Ce framework offre une grille de lecture concrète pour les engineering managers qui veulent mesurer et accélérer l'adoption des agents de code — et comprendre pourquoi l'effet multiplayer fait de la montée en compétence collective un impératif stratégique, pas juste individuel.
