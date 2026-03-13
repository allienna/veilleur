---
title: "Nobody Gets Promoted for Simplicity"
date: 2026-03-12
url: "https://leadershipintech.com/links/21716/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email"
authors: ["Leadership in Tech"]
keywords: ["simplicité", "promotion", "over-engineering", "culture engineering", "incentives"]
theme: "Leadership"
tone: "opinion"
used_in: ["2026-03-12"]
---

## Résumé

L'article expose un biais systémique dans les organisations tech : la complexité est récompensée (promotions, entretiens) tandis que la simplicité reste invisible. L'ingénieur qui livre en 50 lignes de code n'a rien à écrire dans son dossier de promotion, alors que celui qui introduit une architecture événementielle inutile "screams Staff+".

## Points clés

- La complexité est visuellement impressionnante et facile à documenter ; la simplicité est invisible par nature
- Les entretiens system design récompensent l'ajout de composants, pas la retenue
- Le biais commence aux entretiens et se perpétue dans les cycles de promotion
- Citation de Dijkstra : "Simplicity is a great virtue, but it requires hard work to achieve and education to appreciate"
- La solution passe par un changement culturel : valoriser explicitement ce qui n'a PAS été construit
- Les managers doivent reconnaître que "personne n'est promu pour la complexité qu'il a évitée"

## Analyse approfondie

### L'ingénieur A contre l'ingénieur B

L'article pose le problème avec un scénario parlant. L'ingénieur A livre une feature en 50 lignes de code, lisibles, testables, en deux jours. L'ingénieur B prend trois semaines pour la même feature : couche d'abstraction, système pub/sub, framework de configuration extensible. Au moment des promotions, le dossier de B « s'écrit tout seul » : *« Designed and implemented a scalable event-driven architecture, introduced a reusable abstraction layer adopted by multiple teams. »* Celui de A se résume à trois mots : *« Implemented feature X. »* Le travail de A était meilleur, mais invisible — parce qu'on ne peut pas écrire un récit convaincant sur ce qu'on n'a *pas* construit.

### Le biais commence avant même l'embauche

En entretien system design, proposer une solution simple — une base de données, une API directe, un cache — provoque systématiquement un « What about scalability? What if you have ten million users? ». Le candidat ajoute des services, des queues, du sharding. L'interviewer est satisfait. La leçon intériorisée : la complexité impressionne, la simplicité ne suffit pas.

Le même biais se retrouve en design review : « Shouldn't we future-proof this? » L'ingénieur repart ajouter des couches d'abstraction pour des problèmes qui ne se matérialiseront peut-être jamais — non parce que le problème l'exige, mais parce que la salle l'attend.

### Le vrai marqueur de séniorité

L'auteur distingue complexité justifiée et complexité non méritée (*unearned complexity*). Il y a une différence entre « we're hitting database limits and need to shard » et « we might hit database limits in three years, so let's shard now ». Le chemin vers la séniorité n'est pas d'apprendre plus d'outils et de patterns, mais de savoir quand ne *pas* les utiliser : « Anyone can add complexity. It takes experience and confidence to leave it out. »

### Conseils actionables

Pour les ingénieurs : rendre la simplicité visible. Au lieu de « Implemented feature X », écrire : *« Evaluated three approaches including an event-driven architecture, determined that a straightforward implementation met all requirements, and shipped in two days with zero incidents over six months. »* En design review, ne pas céder mais démontrer : « Here's what it would take to add that later, and here's what it costs us now. I think we wait. »

Pour les engineering leaders : changer les questions posées. Au lieu de « Have we thought about scale? », demander : « What's the simplest version we could ship, and what signals would tell us we need something more complex? » En comité de promotion, challenger les dossiers impressionnants : « Was all of that necessary? » Et publiquement, célébrer l'ingénieur qui a supprimé du code.

## Pourquoi ça compte

Dans un monde où l'IA génère du code complexe à volonté, la capacité à choisir la solution la plus simple devient le vrai marqueur de séniorité. Cet article est un rappel salutaire pour les engineering managers qui construisent leurs grilles de promotion.
