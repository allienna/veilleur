---
title: "Addy Osmani on X: \"Loop Engineering.\""
date: 2026-06-09
url: https://links.tldrnewsletter.com/hw6fq7
authors: [Addy Osmani]
keywords: [loop engineering, coding agents, automation, worktrees, Claude Code, Codex]
theme: IA
tone: opinion
used_in: ["2026-06-09"]
---

## Résumé

Addy Osmani formalise un changement de paradigme dans le travail avec les agents de code : le « Loop Engineering ». L'idée est qu'on cesse d'être la personne qui prompte l'agent pour devenir celle qui conçoit le système qui le prompte. Une boucle est un objectif récursif — on définit un but, l'IA itère jusqu'à complétion. Osmani identifie cinq briques de base désormais présentes nativement dans Claude Code comme dans Codex, tout en restant prudent sur les coûts en tokens et le risque de « slop ».

## Points clés

- Le Loop Engineering, c'est se remplacer soi-même comme prompteur : on conçoit le système qui prompte l'agent à sa place.
- Une « boucle » = un objectif récursif où l'IA itère jusqu'à ce que la tâche soit finie.
- Cinq briques de base + un endroit pour mémoriser l'état ; Claude Code et Codex les ont désormais tous les deux.
- Le responsable de Claude Code chez Anthropic : « Je ne prompte plus Claude. J'ai des boucles qui tournent (...). Mon job, c'est d'écrire des boucles. »
- Ce n'est plus une affaire d'outil : il y a un an il fallait écrire et maintenir des scripts bash ; aujourd'hui les briques sont livrées dans les produits.
- Osmani reste sceptique : c'est tôt, les coûts en tokens peuvent varier énormément, et la question de la qualité (slop) reste valide.

## Analyse approfondie

**Loop Engineering.**

Le Loop Engineering consiste à se remplacer soi-même comme personne qui prompte l'agent. On conçoit le système qui le fait à la place. Une boucle peut être vue comme un objectif récursif : on définit un but, et l'IA itère jusqu'à la complétion. Cela tient en gros à cinq briques de base, et Claude Code comme Codex les possèdent désormais toutes les cinq.

Osmani croit que cela pourrait être l'avenir de la manière dont on travaille avec les agents de code. Il reste cependant prudent : c'est encore tôt, il est sceptique, et il faut absolument faire attention aux coûts en tokens (les usages peuvent varier énormément selon qu'on est « token rich » ou « token poor »). Il faut aussi un moyen de garantir que la qualité ne baisse pas — les inquiétudes autour du « slop » sont légitimes.

Il cite deux voix. La première : « Vous ne devriez plus prompter les agents de code. Vous devriez concevoir des boucles qui promptent vos agents. » La seconde, le responsable de Claude Code chez Anthropic : « Je ne prompte plus Claude. J'ai des boucles qui tournent, qui promptent Claude et décident quoi faire. Mon job, c'est d'écrire des boucles. »

Qu'est-ce que ça veut dire ? Pendant environ deux ans, la façon d'obtenir quelque chose d'un agent de code était d'écrire un bon prompt et de partager assez de contexte. On tape une chose, on lit ce qui revient, on tape la suivante. L'agent est un outil et on le tient en main en permanence, tour après tour. Cette époque est en train de se terminer — du moins certains le pensent.

Désormais, on construit un petit système qui trouve le travail, le distribue, le vérifie, note ce qui est fait, puis décide de la prochaine chose, et on laisse ce système solliciter les agents à notre place. Osmani évoque un cousin de cette approche : le « harness », l'environnement dans lequel un agent unique tourne — le système qui construit le logiciel. Le Loop Engineering se situe un étage au-dessus du harness : il tourne sur un timer, il fait apparaître de petits helpers, et il se nourrit lui-même.

Ce qui surprend, c'est que ce n'est plus vraiment une affaire d'outil. Il y a un an, pour avoir une boucle, il fallait écrire un tas de bash et le maintenir indéfiniment — c'était le vôtre et celui de personne d'autre. Maintenant les pièces sont livrées à l'intérieur des produits. La liste de briques de Steinberger correspond presque exactement à l'app Codex, puis presque à l'identique à Claude Code. Et une fois qu'on remarque que la forme est la même, on arrête de se disputer sur l'outil : on conçoit une boucle qui fonctionne quel que soit celui dans lequel on se trouve.

Une boucle a besoin de cinq choses, plus un endroit pour mémoriser l'état :
1. Des automatisations qui se déclenchent sur un planning et font la découverte et le tri toutes seules.
2. Des worktrees pour que deux agents travaillant en parallèle ne se marchent pas dessus.
(et les briques suivantes, qui complètent l'orchestration et la mémoire partagée.)

## Pourquoi ça compte

Le Loop Engineering nomme et structure une transition de fond du métier : passer du « prompteur » à l'« architecte de boucles ». C'est le cadre conceptuel qui explique pourquoi tout l'outillage agentique (sandboxes, review, orchestration) se met en place en même temps.
