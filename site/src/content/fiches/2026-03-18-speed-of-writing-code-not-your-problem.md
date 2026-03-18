---
title: "If you thought the speed of writing code was your problem - you have bigger problems"
date: 2026-03-18
url: https://andrewmurphy.io/blog/if-you-thought-the-speed-of-writing-code-was-your-problem-you-have-bigger-problems
authors: [Andrew Murphy]
keywords: [theory of constraints, bottleneck, productivité, livraison logicielle, Goldratt]
theme: Leadership
tone: opinion
used_in: ["2026-03-18"]
---

## Résumé

Andrew Murphy applique la Théorie des Contraintes d'Eliyahu Goldratt au développement logiciel à l'ère de l'IA. Son argument : si écrire du code n'était pas le goulot d'étranglement de votre système de livraison, l'accélérer avec l'IA ne rend pas le système plus rapide — il le rend plus cassé. Les vrais bottlenecks sont la revue de code, les tests, le déploiement et la découverte produit.

## Points clés

- La Théorie des Contraintes (Goldratt, "The Goal") stipule que le débit d'un système est limité par son goulot d'étranglement
- Optimiser une étape qui n'est pas le bottleneck ne produit pas un système plus rapide — cela produit un système plus cassé
- Écrire du code n'a jamais été le goulot d'étranglement dans la plupart des organisations
- Les vrais bottlenecks : la revue de code, les tests, le déploiement, la découverte produit, les décisions d'architecture
- Citation clé : "When you optimise a step that is not the bottleneck, you don't get a faster system. You get a more broken one."
- Accélérer la production de code crée un embouteillage en aval : plus de PRs en attente de revue, plus de bugs à tester, plus de dette technique

## Analyse approfondie

L'article s'ouvre sur un constat simple : l'industrie tech est en ébullition autour de l'IA qui accélère l'écriture de code. Mais Andrew Murphy pose une question fondamentale — est-ce que la vitesse d'écriture du code était réellement votre problème ?

### La Théorie des Contraintes appliquée au logiciel

Eliyahu Goldratt, dans son livre "The Goal" (1984), a formulé la Théorie des Contraintes : tout système de production a un goulot d'étranglement, et le débit total du système est déterminé par ce goulot. Améliorer n'importe quelle autre étape que le goulot d'étranglement est au mieux inutile, au pire contre-productif.

Appliquée au développement logiciel, cette théorie révèle un problème fondamental avec la promesse des agents IA de codage. Le pipeline de livraison logicielle comporte de nombreuses étapes : découverte produit, spécification, architecture, écriture de code, revue de code, tests, déploiement, monitoring. L'écriture de code n'est qu'une de ces étapes.

### Quand on accélère ce qui n'est pas le bottleneck

Si l'écriture de code n'est pas le goulot d'étranglement — et dans la plupart des organisations, elle ne l'est pas —, alors l'accélérer avec des agents IA ne réduit pas le temps de livraison total. Au contraire, cela crée un engorgement en aval.

Plus de code est produit plus vite, ce qui signifie :

- Plus de pull requests en attente de revue, submergant les reviewers
- Plus de changements à tester, débordant les pipelines de QA
- Plus de déploiements à gérer, augmentant le risque opérationnel
- Plus de décisions d'architecture à prendre, ralentissant les arbitrages

> "When you optimise a step that is not the bottleneck, you don't get a faster system. You get a more broken one."

C'est exactement ce que la Théorie des Contraintes prédit : quand on augmente le débit d'une étape non-contrainte, on accumule du travail en cours (WIP) qui encombre le système sans accélérer la sortie.

### Identifier le vrai bottleneck

Murphy invite les équipes à se poser la question honnêtement : quel est le vrai goulot d'étranglement dans votre processus de livraison ? Pour beaucoup d'organisations, c'est la revue de code (pas assez de reviewers qualifiés), les tests (couverture insuffisante, tests manuels), le déploiement (processus lourds, approbations multiples) ou la découverte produit (on ne sait pas quoi construire).

L'ironie est que les agents IA pourraient potentiellement aider sur ces vrais bottlenecks — agents de revue de code, génération automatique de tests, automatisation du déploiement — mais l'industrie se focalise sur l'étape la plus visible et la plus gratifiante : écrire du code neuf.

### Le piège de la métrique visible

Il est plus facile de mesurer "lignes de code produites" que "valeur livrée aux utilisateurs". Les agents IA de codage offrent des métriques impressionnantes sur la première dimension, ce qui crée l'illusion de productivité. Mais la productivité réelle d'une équipe logicielle se mesure en fonctionnalités livrées, en stabilité du système et en satisfaction utilisateur — pas en volume de code produit.

## Pourquoi ça compte

Cet article fournit un cadre théorique solide (Goldratt) pour expliquer pourquoi l'accélération du codage par l'IA ne se traduit pas automatiquement en gains de productivité. C'est une lecture essentielle pour tout engineering manager qui doit justifier (ou questionner) l'investissement dans les outils de codage IA.
