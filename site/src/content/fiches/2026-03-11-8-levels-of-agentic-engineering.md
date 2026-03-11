---
title: "The 8 Levels of Agentic Engineering"
date: 2026-03-11
url: https://www.bassimeledath.com/blog/levels-of-agentic-engineering
authors: [Bassim Eledath]
keywords: [agentic engineering, niveaux de maturité, coding agents, productivité, équipes]
theme: IA
tone: opinion
used_in: ["2026-03-11"]
---

## Résumé

Bassim Eledath propose un framework en 8 niveaux pour mesurer la maturité des équipes en ingénierie agentique, de l'autocomplétion basique aux agents background autonomes qui soumettent des PR pendant que le développeur dort. L'article insiste sur l'effet multiplicateur d'équipe : la productivité individuelle est contrainte par le niveau du maillon le plus faible. Chaque niveau supplémentaire représente un saut majeur en output, et chaque amélioration de modèle amplifie ces gains.

## Points clés

- 8 niveaux de maturité : de Tab Complete (niveau 1) aux agents background autonomes (niveau 7-8)
- L'effet "multiplayer" : votre throughput dépend du niveau de vos collègues, pas seulement du vôtre
- Niveaux 1-2 : autocomplétion et IDE avec agent (Copilot, Cursor) — le plafond est le contexte
- Niveaux 3-4 : plan mode et agentic coding — le développeur orchestre, l'agent exécute
- Niveaux 5-6 : multi-agents, worktrees parallèles, review automatisée
- Niveaux 7-8 : agents background 24/7 qui soumettent des PR de manière autonome
- L'équipe d'Anthropic a livré Cowork en 10 jours — la même technologie utilisée différemment donne des résultats radicalement différents

## Analyse approfondie

La capacité de codage de l'IA dépasse notre capacité à l'utiliser efficacement. C'est pourquoi les scores SWE-bench ne se traduisent pas en métriques de productivité réelles. Quand l'équipe d'Anthropic livre un produit comme Cowork en 10 jours et qu'une autre équipe n'arrive pas à dépasser un POC cassé avec les mêmes modèles, la différence est que l'une a comblé l'écart entre capacité et pratique, et l'autre non.

Cet écart se comble par niveaux. Huit niveaux. La plupart des lecteurs ont dépassé les premiers, et chaque niveau suivant représente un saut énorme en output. Chaque amélioration de la capacité du modèle amplifie encore ces gains.

L'autre raison de s'en préoccuper est l'effet multiplayer. Votre output dépend plus qu'on ne le pense du niveau de vos coéquipiers. Si vous êtes un wizard niveau 7, levant plusieurs PR solides avec vos agents background pendant que vous dormez, mais que votre repo nécessite l'approbation d'un collègue niveau 2 qui review encore manuellement les PR, votre throughput s'effondre. Il est donc dans votre intérêt de tirer votre équipe vers le haut.

### Niveaux 1 et 2 : Tab Complete et Agent IDE

L'autocomplétion est le point de départ. GitHub Copilot a lancé le mouvement. Cliquer Tab, autocompléter le code. Les IDE orientés IA comme Cursor ont changé la donne en connectant le chat à la codebase, rendant les éditions multi-fichiers drastiquement plus faciles. Mais le plafond était toujours le contexte — le modèle ne pouvait aider qu'avec ce qu'il pouvait voir.

La plupart des gens à ce niveau expérimentent aussi le plan mode : traduire une idée brute en un plan structuré étape par étape pour le LLM, itérer sur ce plan, puis déclencher l'implémentation.

### Niveaux suivants : orchestration et autonomie

À partir du niveau 3, on entre dans le codage agentique proprement dit : le développeur orchestre, l'agent exécute des tâches complètes. Les niveaux supérieurs introduisent le multi-agent, les worktrees parallèles, la review automatisée, jusqu'aux agents background qui fonctionnent en permanence et soumettent des PR de manière autonome.

L'article souligne que chaque niveau n'est pas seulement un gain incrémental — c'est un changement qualitatif dans la façon dont le travail se fait. Et l'écart entre les équipes qui adoptent ces niveaux et celles qui restent aux niveaux inférieurs ne cesse de se creuser.

## Pourquoi ça compte

Ce framework offre une grille de lecture concrète pour les engineering managers qui veulent mesurer et accélérer l'adoption des agents de code dans leurs équipes — et comprendre pourquoi certaines équipes tirent un bénéfice 10x de la même technologie que d'autres.
