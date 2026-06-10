---
title: "Initial impressions of Claude Fable 5"
date: 2026-06-10
url: https://simonwillison.net/2026/Jun/9/claude-fable-5/
authors: [Simon Willison]
keywords: [Claude Fable 5, benchmarks, context window, guardrails, fallback]
theme: IA
tone: opinion
used_in: ["2026-06-10"]
---

## Résumé

Simon Willison, sans accès anticipé, a passé environ 5,5 heures à tester Claude Fable 5. Son impression : un modèle « bête de course » — lent, cher, mais qui vient à bout de presque tout ce qu'on lui jette, au point que le défi devient de trouver des tâches qu'il ne sait pas faire. Il détaille les caractéristiques techniques (1M de contexte, 128k tokens de sortie max, knowledge cut-off janvier 2026, prix double d'Opus 4.x) et constate la « big model smell » : un modèle qui paraît énorme, autant par la vitesse et le coût que par l'étendue de ses connaissances.

## Points clés

- ~5,5 heures de tests sans accès anticipé : « something of a beast », lent et cher.
- Le vrai défi devient de trouver des tâches que le modèle échoue à accomplir.
- Fenêtre de contexte de 1 million de tokens, 128 000 tokens de sortie max, cut-off de connaissances en janvier 2026.
- Prix : le double d'Opus 4.5/4.6/4.7/4.8, soit $10 / $50 le million de tokens, sans surcoût pour le contexte long.
- Les garde-fous se déclenchent assez souvent pour justifier de nouveaux mécanismes API et une option de fallback automatique vers un autre modèle.
- « Big model smell » : Fable répond là où Opus 4.8 préfère avouer son incertitude, témoignant de l'étendue de ses connaissances.

## Analyse approfondie

9 juin 2026.

Je n'ai pas eu d'accès anticipé à la sortie d'aujourd'hui de Claude Fable 5, mais j'ai passé les ~5,5 dernières heures à le mettre à l'épreuve. Mes premières impressions, c'est que c'est quelque chose comme une **bête**. C'est lent, c'est cher, et ça a avalé avec entrain tout ce que je lui ai lancé jusqu'ici. Comme c'est souvent le cas avec les modèles de pointe actuels, le défi est de trouver des tâches qu'il ne sait pas faire.

D'abord, passons en revue les caractéristiques clés.

Anthropic affirme que Claude Fable 5 offre les mêmes performances que Claude Mythos 5, mais avec des garde-fous bien plus stricts en place pour empêcher son usage à des fins nuisibles. Ces garde-fous se déclenchent assez souvent pour que l'API Claude dispose de nouveaux mécanismes pour vous prévenir quand vous les heurtez, et même d'une nouvelle option pour demander un repli automatique vers un autre modèle si quelque chose est rejeté.

Claude Mythos 5 sort aussi aujourd'hui ; Anthropic dit qu'il « partage les capacités de Claude Fable 5 sans les classificateurs de sécurité ».

Les modèles ont une fenêtre de contexte d'un million de tokens, 128 000 tokens de sortie maximum et une date de coupure des connaissances fixée à janvier 2026.

Ils sont facturés au double du prix de Claude Opus 4.5/4.6/4.7/4.8 : $10/million de tokens en entrée et $50/million en sortie. Pas d'augmentation de prix pour l'usage du contexte long.

À part ça, le guide de migration est nettement plus mince que le guide équivalent pour Opus 4.8.

**The big model smell.** La meilleure façon de décrire Fable, c'est qu'il donne une impression d'**énormité**. Pas seulement en vitesse et en coût, mais aussi dans l'étendue de ce qu'il sait.

Voici un exemple de prompt que j'ai utilisé pour comparer les connaissances de Fable à celles d'Opus 4.8 (faute de frappe incluse) : « Liste tous les projets open source de Simon Willion, du plus récent au plus ancien, chacun avec une date approximative de première sortie ».

La réponse d'Opus 4.8 commençait par avouer qu'il n'avait pas de liste fiable, exhaustive et datée, préférant être honnête plutôt que de risquer des dates inexactes ou des entrées fabriquées, avant de donner une poignée de projets bien connus avec prudence. (Le billet poursuit en montrant que Fable, lui, répond de façon nettement plus étendue — illustration de la « big model smell ».)

## Pourquoi ça compte

C'est le contrepoint « terrain » indispensable à l'annonce officielle : un praticien reconnu confirme le saut de capacité, mais rappelle aussi les coûts réels (lenteur, prix) et la fréquence concrète des garde-fous — un éclairage honnête pour qui doit décider d'adopter ou non le modèle.
