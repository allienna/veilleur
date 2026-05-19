---
title: "Let's talk about AI slop"
date: 2026-05-19
url: https://archestra.ai/blog/only-responsible-ai?utm_source=tldrdev
authors: [Archestra]
keywords: [AI slop, open source, GitHub, bots, contribution quality]
theme: IA
tone: opinion
used_in: ["2026-05-19"]
---

## Résumé

L'équipe d'Archestra raconte son combat contre le flot de contributions IA non testées et de commentaires automatiques qui ont envahi leur repo open-source. Un bounty à 900 $ s'est retrouvé pollué par 253 commentaires de bots, une simple issue d'ajout de provider a généré 27 PRs non testées, et un membre de l'équipe consacre une demi-journée par semaine à nettoyer "l'AI slop". L'article documente les solutions essayées (bot de réputation, "AI sheriff") et leurs limites — et pose une question dérangeante : que devient l'open source si les mainteneurs croulent sous le bruit ?

## Points clés

- Une issue avec 900 $ de bounty noyée par 253 commentaires de bots
- 27 PRs pour ajouter un seul provider, la plupart non testées par leurs auteurs
- Une demi-journée par semaine perdue à nettoyer l'AI slop du repo
- Les notifications GitHub des watchers deviennent un mur de bruit
- Les vraies contributions sont noyées dans le flux automatique
- Tentatives de défense : bot de réputation (London-Cat) et "AI sheriff" (qui a fermé par erreur des PRs légitimes)
- Le coût de l'IA migre vers les mainteneurs et les reviewers, pas seulement vers les contributeurs

## Analyse approfondie

### La fin de l'open source tel qu'on le connaît ?

Quand GitHub a partagé il y a quelques mois ses statistiques [célébrant l'énorme contribution de l'IA dans ses métriques produit](https://github.blog/news-insights/octoverse/), passant complètement à côté du point de la dégradation de la qualité des contributions, l'équipe d'Archestra sentait déjà que ça partait en vrille.

Le premier moment inquiétant a été [une issue postée avec un bounty de 900 $](https://github.com/archestra-ai/archestra/issues/1301). L'équipe espérait motiver quelqu'un à contribuer et apporter le support des "MCP Apps" à leur plateforme. Ils ont rapidement attiré l'attention de contributeurs légitimes proposant des plans, posant des questions, soumettant des tentatives — mais très vite...

Les bots IA sont arrivés et ont fait exploser l'issue, la portant à **253 commentaires au total**, empoisonnant la conversation avec des "plans d'implémentation" sans intérêt et même de la pure agressivité envers les mainteneurs !

Les comptes IA ont commencé à inonder non seulement cette issue — mais le repo entier. Chaque commentaire bâclé déclenchait une notification pour chaque membre de l'équipe qui watchait le repo. Leurs notifications GitHub sont devenues un mur de bruit. Les vraies conversations avec des contributeurs comme @ethanwater, @developerfred et @Geetk172 — des gens activement engagés sur des bounties — étaient noyées.

Plus tard, le problème a pris la forme d'une épidémie. Par exemple, juste pour l'issue d'ajout du support du provider x.ai à Archestra, ils ont reçu **27 pull requests**, dont la plupart **les contributeurs n'avaient même pas essayé de tester**.

Un membre de l'équipe a dû passer **une demi-journée par semaine à nettoyer la garbage IA du repo**, supprimant les PRs non testées et fermant les issues hallucinées. Quand ils oubliaient de le faire, leur repo devenait rapidement un endroit complètement hostile aux contributeurs légitimes.

### Riposter

D'abord, ils ont essayé de calculer la "réputation" des contributeurs et ont bâti ["London-Cat"](https://github.com/archestra-ai/reputation-bot), un petit bot calculant une réputation de contributeur basée sur les PRs mergées et quelques autres signaux. Évidemment, ça n'a pas stoppé le spam, mais ça a aidé à savoir "qui est qui".

Étape suivante : un "AI sheriff", qui — évidemment — a fermé par erreur quelques PRs légitimes 🤦.

Le flot constant de commentaires et propositions IA inutiles ne faisait qu'empirer. L'article décrit ensuite les approches plus radicales testées par l'équipe (filtrages plus stricts, gating des contributions, restrictions sur les profils anonymes), avec leurs trade-offs.

### Le constat de fond

L'open source moderne reposait sur une économie implicite : les contributeurs investissent du temps de qualité, les mainteneurs en investissent un peu en review, et la collaboration crée de la valeur pour les deux. L'IA a cassé cette économie. Le coût marginal d'une PR a chuté à zéro côté contributeur — mais reste élevé côté mainteneur. Conséquence : les mainteneurs croulent.

## Pourquoi ça compte

C'est le contre-récit nécessaire face à l'enthousiasme sur "AI everywhere". L'IA déplace le coût du travail vers ceux qui revoient, vérifient et maintiennent. Si on parle de stratégie IA en équipe, il faut absolument intégrer cette dimension : qui paie le coût caché ?
