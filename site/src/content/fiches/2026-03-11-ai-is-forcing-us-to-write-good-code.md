---
title: "AI Is Forcing Us To Write Good Code"
date: 2026-03-11
url: https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code
authors: [Logic Inc]
keywords: [code quality, coverage 100%, guardrails, agents IA, tests]
theme: IA
tone: opinion
used_in: ["2026-03-11"]
---

## Résumé

Une équipe de six personnes partage ses choix controversés pour accommoder les coding agents, dont l'exigence de 100 % de code coverage. L'argument central : les agents n'optimisent pas pour la qualité par défaut — ils sont comme un Roomba qui roule sur les accidents et les étale partout. Les seuls garde-fous sont ceux qu'on impose et qu'on fait respecter. À 100 % de coverage, on élimine la décision humaine de ce qui est "assez important" pour être testé, et l'agent est contraint de trouver le seul chemin correct.

## Points clés

- 100 % de code coverage n'est pas une métrique de qualité — c'est une contrainte pour l'agent, qui garantit qu'il a vérifié chaque ligne qu'il a écrite
- À 95 %, on fait encore des choix sur ce qui mérite un test. À 100 %, cette décision disparaît
- Les agents ont besoin de guardrails solides : tests, linters, documentation, small modules, static typing
- Ces "bonnes pratiques" étaient optionnelles depuis des décennies — les agents les rendent obligatoires
- L'équipe traite la coverage comme un "secret weapon" : scepticisme initial, puis adoption enthousiaste après un jour de pratique
- Sans guardrails suffisants et avec un contexte agentique lacunaire, le résultat est catastrophique

## Analyse approfondie

Pendant des décennies, tout le monde savait à quoi ressemblait le "bon code" : tests complets, documentation claire, petits modules bien scopés, typage statique, environnements de développement reproductibles. Ces choses étaient toujours optionnelles, et la pression temporelle signifiait que l'optionnel était coupé en premier.

Les agents ont besoin de ces éléments optionnels. Ils ne sont pas doués pour créer un désordre et le nettoyer ensuite. Les agents seront joyeusement le Roomba qui roule sur la crotte du chien et l'étale dans toute la maison.

Les seuls garde-fous sont ceux qu'on définit et qu'on fait respecter. Si le contexte agentique est insuffisant et que les garde-fous ne sont pas adéquats, on se retrouve dans un monde de douleur. Mais si les garde-fous sont solides, le LLM peut rebondir inlassablement jusqu'à ce que le seul chemin de sortie soit le bon.

### 100 % de code coverage

Le choix le plus controversé est le plus précieux : exiger 100 % de code coverage. Tout le monde est sceptique quand on l'entend, jusqu'à ce qu'on vive avec pendant un jour. C'est parfois comme une arme secrète.

La coverage, telle qu'utilisée ici, n'est pas strictement une question de prévention des bugs — c'est la garantie que l'agent a vérifié le comportement de chaque ligne de code qu'il a écrite.

L'interprétation erronée habituelle est de penser que 100 % de coverage signifie "zéro bug" ou qu'on poursuit une métrique qui sera gamifiée. Ce n'est ni l'un ni l'autre.

Pourquoi 100 % ? À 95 % de coverage, on prend encore des décisions sur ce qui est "assez important" pour être testé. À 99,99 %, on ne sait pas si cette ligne non couverte dans `./src/foo.ts` était là avant que l'agent ne touche au fichier. À 100 %, il n'y a pas d'ambiguïté.

### Impact sur le workflow

L'équipe décrit plusieurs autres investissements spécifiques et parfois controversés pour accommoder leurs coding agents. Le principe directeur est que les agents amplifient à la fois les bonnes et les mauvaises pratiques — si les fondamentaux ne sont pas solides, les agents créeront du chaos plus rapidement qu'un humain ne pourrait le faire.

## Pourquoi ça compte

Cet article renverse un argument courant ("l'IA dégrade la qualité du code") en montrant que les agents, correctement contraints, forcent le retour à des pratiques que l'industrie repoussait depuis des années — et que le vrai problème n'est pas l'IA, mais l'absence de guardrails.
