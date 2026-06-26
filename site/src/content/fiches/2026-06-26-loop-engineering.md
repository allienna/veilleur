---
title: "Loop Engineering"
date: 2026-06-26
url: https://link.mail.beehiiv.com/ss/c/u001.K3FzaWG5vnes9asChrWWUH4s5J6LGhy1MGtNBf8LtprSVZbXt-cw1Q62dDP5FQkEQyneRXNuw8WpDqdfKf8UGkEoIDp1FU-f-99Z_Cv0EtrOA59zhhIHjDAmD_NP33ndrpBn5iOqCJdrnsBBUVHxhJgIHioSbJVulk9o7Kcdacc/4rt/GprCMSxARbOYQXWwa4OaOQ/h15/h001.5w2o7lqWwYeuvh4VYVZ-HiKDSpDRNMwY_CN01lh9Xag
authors: [Addy Osmani]
keywords: [loop engineering, agents, harness, automation, orchestration]
theme: IA
tone: opinion
used_in: ["2026-06-26"]
---

## Résumé

L'article décrit l'émergence du "loop engineering" : un changement de paradigme où l'on ne prompte plus directement les agents de coding, mais où l'on conçoit des boucles qui les pilotent. Peter Steinberger comme Boris Cherny (head of Claude Code chez Anthropic) le formulent crûment : leur métier n'est plus de prompter, mais d'écrire des boucles. Là où, pendant deux ans, on tenait l'outil en main tour après tour, on construit désormais un système qui trouve le travail, le distribue, le vérifie, note ce qui a été fait, puis décide de la suite.

## Points clés

- Peter Steinberger : "Vous ne devriez plus prompter des agents de coding. Vous devriez concevoir des boucles qui promptent des agents."
- Boris Cherny (head of Claude Code, Anthropic) : "Je ne prompte plus Claude. J'écris des boucles qui lancent des prompts, qui décident quoi faire. Mon job, c'est d'écrire les boucles."
- Pendant deux ans, le mode d'usage était : taper, lire la réponse, re-taper — un tour après l'autre, l'humain tenant l'outil.
- Le loop engineering : construire un petit système qui trouve le travail, le distribue, le vérifie, journalise, puis décide de la suite.
- Il s'articule avec d'autres concepts : "agent harness engineering" (l'environnement d'un agent unique) et "factory model" (un système qui construit du logiciel).
- Le loop engineering se situe un étage au-dessus du harness : c'est un harness qui tourne sur un timer, génère des helpers, et se nourrit lui-même.
- Ce n'est plus vraiment une affaire d'outil : il y a un an, écrire une boucle demandait du code ; ce n'est plus le cas.

## Analyse approfondie

L'auteur prévient que la portée du loop engineering varie énormément selon que l'on est "token rich" ou "token poor", et veut déballer ce que cela signifie.

Peter Steinberger a récemment dit : "Vous ne devriez plus prompter des agents de coding. Vous devriez concevoir des boucles qui promptent des agents." De même, Boris Cherny, head of Claude Code chez Anthropic, a dit : "Je ne prompte plus Claude. J'écris des boucles qui lancent des prompts, qui poussent Claude à comprendre quoi faire. Mon job, c'est d'écrire les boucles."

Alors, qu'est-ce que tout cela veut dire ? Pendant à peu près deux ans, la façon dont on obtenait quelque chose d'un agent de coding était d'écrire un bon prompt et de partager assez de contexte. Vous tapez une chose, vous lisez ce qui revient, vous tapez la suivante. L'agent est un outil et vous le tenez en main tout du long, un tour après l'autre. Cette partie-là est en quelque sorte terminée, ou du moins certains pensent qu'elle est en train de l'être.

Maintenant, vous construisez un petit système qui trouve le travail, le distribue, le vérifie, note ce qui a été fait, puis décide de la chose suivante ; vous laissez ce système titiller les agents à votre place.

J'ai écrit auparavant sur un cousin de ceci, l'*agent harness engineering*, qui consiste à fabriquer l'environnement dans lequel un agent unique s'exécute — le *factory model*, un système qui construit du logiciel. Le loop engineering se situe un étage au-dessus du harness. C'est un harness, mais qui tourne sur un timer, génère de petits helpers, et se nourrit lui-même.

La chose qui m'a surpris, c'est que ce n'est plus vraiment une affaire d'outil. Il y a un an, si vous vouliez une boucle, vous deviez l'écrire en code. Aujourd'hui, ce n'est plus le cas : la boucle peut être décrite et orchestrée à un niveau plus haut, et c'est cette capacité d'orchestration qui devient la compétence centrale.

## Pourquoi ça compte

Le loop engineering nomme la compétence qui prend de la valeur quand le débit de code devient une commodité : orchestrer des systèmes d'agents plutôt qu'exécuter. C'est un repère concret pour comprendre vers quoi évolue le métier d'ingénieur.
