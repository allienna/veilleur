---
title: "The Trust Problem With AI Agents"
date: 2026-04-29
url: https://tldr.tech/blog/trust-problem-ai-agents
authors: [TLDR]
keywords: [confiance, agents, transparence, fiabilité, developer experience]
theme: IA
tone: opinion
used_in: ["2026-04-29"]
---

## Résumé

L'article pose une thèse simple : les outils IA deviennent plus capables, mais les développeurs leur font moins confiance. La raison ne tient pas à la puissance des modèles, mais à la prévisibilité et à la transparence des outils qui les exposent. Tant que le développeur récupère un changelog opaque sans comprendre pourquoi l'agent a fait ce qu'il a fait, la défiance s'installe — et elle se mérite.

## Points clés

- La capacité brute attire vers un outil. La fiabilité et la prévisibilité sont ce qui te fait y rester.
- La métaphore de l'air fryer : un appareil qui ne marche qu'une fois sur deux n'est pas un bon appareil, peu importe ses fonctionnalités.
- Premier coupable : la transparence. Si on ne voit pas le raisonnement de l'agent, on hérite d'un changelog du quoi sans le pourquoi.
- Sans visibilité sur le raisonnement, on découvre les mauvaises décisions tard — dans une diff, ou pire, en production.
- Quand on orchestre plusieurs agents en parallèle, le problème de transparence est multiplié par le nombre d'acteurs.

## Analyse approfondie

Si tu es développeur, il y a de fortes chances que tu aies utilisé un outil IA. Et si tu en as utilisé un, tu as probablement déjà vécu ce moment où la sortie n'était pas celle que tu attendais. Moi, oui. Cette sortie peut être un diff qui touche un fichier que tu ne voulais pas modifier, un commit dans ton historique git qui n'était pas censé être poussé, ou une instruction qui n'aurait pas dû être écrite. J'ai même suivi un tutoriel généré qui m'a mené dans le mur.

Quand je me suis retrouvé dans cette situation, je me suis complètement gaslighté en pensant que c'était moi qui avais fait fausse route. Je crois que ce type d'interaction se produit moins avec les modèles et le tooling actuels. Mais ces outils, par design malheureusement, ne sont pas très bons pour communiquer quand ils se trompent — sauf si on le leur pointe explicitement. Du coup, tu te retrouves avec des problèmes que tu ne voyais pas venir, et il faut anticiper leur existence sans pour autant faire totalement confiance à tes outils.

La communication et la sortie de ces outils, ça n'a pas encore "abouti".

### Pourquoi les développeurs ne peuvent pas s'appuyer entièrement sur les agents

La confiance dans nos outils vient d'une sortie fiable et prévisible. C'est valable pour tout. Si tu avais l'air fryer le plus chic du monde avec toutes les options, mais qu'il ne cuisait ton plat qu'une fois sur deux, tu t'occuperais moins de ses capacités parce qu'elles ne seraient pas utilisées de façon fiable. Si tu achetais une batterie super puissante qui prétend recharger ton téléphone en 10 minutes, mais 30 % du temps... est-elle vraiment puissante ?

La capacité, c'est excitant — c'est souvent ce qu'on regarde quand on envisage de changer d'outil ou d'acheter quelque chose de neuf. Mais la prévisibilité et la fiabilité, c'est ce qui fait qu'on continue d'utiliser un outil dans la durée.

En tant qu'industrie, on a donné aux agents de coding et aux outils IA une tonne de capacités... et on leur fait moins confiance qu'avant. Les développeurs ne font pas vraiment confiance aux agents, pour quelques raisons.

### Coupable n°1 : la transparence

Si tu ne regardes pas chaque étape du raisonnement de ton agent (à supposer que ton outil l'expose), tu te retrouves souvent avec un changelog qui te dit ce que l'agent a fait, mais pas nécessairement pourquoi. Tu finis par défendre des décisions que tu n'as pas prises, à partir d'une boîte noire.

Quand tu vois le raisonnement, tu peux arrêter une mauvaise hypothèse tôt et corriger la trajectoire. Quand tu ne le vois pas — ou si tu orchestres plusieurs agents en parallèle — tu risques de capter ces décisions tardivement dans un diff, ou pire, en production.

## Pourquoi ça compte

L'article pose l'enjeu humain de l'industrialisation des agents : sans transparence et sans fiabilité, aucune valeur produite ne se transforme en confiance durable. C'est la dimension que les annonces produit oublient.
