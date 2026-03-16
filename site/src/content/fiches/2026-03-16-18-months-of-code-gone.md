---
title: "18 Months of Code, Gone. Here's What We Learned."
date: 2026-03-16
url: https://tompiagg.io/posts/we-threw-away-1-5-years-of-code
authors: [Tom Piagg, Autonoma]
keywords: [startup, rewrite, testing, technical debt, TypeScript]
theme: Tech
tone: opinion
used_in: ["2026-03-16"]
---

## Résumé

Le fondateur d'Autonoma raconte pourquoi sa startup a décidé de jeter 18 mois de développement et de tout réécrire. Après quatre pivots, l'équipe avait construit un produit QA sans tests, sans TypeScript strict, en mode "just ship". Ça a fonctionné à deux développeurs, mais l'arrivée de recrues a fait exploser les bugs. Le fondateur a même interdit l'écriture de tests avant de réaliser que cette culture détruisait la qualité du produit.

## Points clés

- Choix initial : TypeScript monorepo, pas de strict, zéro test — "just ship"
- Fonctionnel à 2 développeurs qui connaissaient tout le code
- Catastrophe après les premières recrues : bugs partout, un client perdu
- Le fondateur a interdit les tests par conviction culturelle, puis changé d'avis trop tard
- Les modèles IA de l'époque (GPT-4) nécessitaient d'énormes guardrails et wrappers Playwright/Appium
- La réécriture a démarré avec tests from the ground up et TypeScript strict

## Analyse approfondie

L'équipe d'Autonoma n'est pas étrangère aux pivots. Ils ont pivoté environ quatre fois déjà (recherche d'entreprise, génération de documentation, agent de coding, plateforme de test QA). Les raisons dépassent le cadre de l'article. Dans tous les cas, ils savaient que les bugs étaient douloureux, ils ne savaient juste pas quelle était la meilleure façon de résoudre le problème.

### L'ère sans tests

Dans son passé, le fondateur a été coupable d'overengineering. Il était "Uncle Bob-Pilled" mais s'est tellement brûlé avec ça que dans cette startup, il est parti à 180 degrés dans la direction opposée : monorepo TypeScript, pas de strict, pas de tests. Juste shipper et c'est tout ce qui compte.

Ça a très bien fonctionné pour leurs premiers clients quand ils n'étaient que deux à écrire du code et que chacun possédait une énorme partie du codebase et connaissait tout. Après qu'ils aient commencé à recruter, c'est devenu un désastre. Les bugs apparaissaient de partout. Le codebase était un énorme bazar de nulls, de comportements indéfinis, de mauvaise gestion d'erreurs. C'était si grave qu'ils ont perdu un client à cause de ça.

Pendant très longtemps, le fondateur n'a PAS autorisé les gens à écrire des tests parce qu'il pensait que culturellement, ils avaient besoin d'une culture de shipping rapide et qu'ils devaient dogfooder leur propre produit, et que ça devait suffire. À un moment, il a réalisé qu'il affectait la qualité de leur produit et la productivité, et il a changé d'avis. D'une certaine façon, c'était trop tard.

### Pourquoi une réécriture et pas un refactoring

Quand ils ont initialement entrepris de construire le produit, ils voulaient une solution entièrement agentique. À l'époque, la technologie n'était pas là. C'était l'ère GPT-4 (pas 4o, juste 4). Les modèles étaient si mauvais qu'ils ont dû construire d'énormes guardrails et leur donner des informations très précises pour qu'ils fonctionnent à peu près. Ils ont construit d'énormes wrappers Playwright et Appium qui faisaient des inspections très complexes sur le code et extrayaient un tas d'informations.

Maintenant que les modèles sont beaucoup plus capables, toute cette infrastructure de guardrails est devenue du poids mort. La réécriture permet de repartir avec une architecture adaptée aux capacités actuelles des modèles, avec des tests dès le départ et TypeScript en mode strict.

### La leçon

C'est que maintenant qu'ils réécrivent tout, ils ont commencé avec des tests dès le début et le mode TypeScript le plus strict. L'expérience a prouvé que la "culture du shipping" sans filet de sécurité ne scale pas au-delà de l'équipe fondatrice.

## Pourquoi ça compte

C'est un cas d'étude rare où un fondateur admet ouvertement ses erreurs de jugement sur les tests et la qualité. L'article illustre concrètement la comprehension debt : quand le code n'est compris que par ses auteurs originaux, chaque nouvelle recrue augmente la dette de manière exponentielle.
