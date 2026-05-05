---
title: "The Compounding Software Factory"
date: 2026-05-01
url: https://refactoring.fm/p/the-compounding-software-factory?utm_source=tldrdev
authors: [Luca Rossi, Rob Zuber]
keywords: [software factory, DX, AI productivity, engineering management, CircleCI]
theme: Leadership
tone: opinion
used_in: ["2026-05-01"]
---

## Résumé

Troisième volet de la série "Software Factory" de Luca Rossi, co-écrit avec Rob Zuber (CTO de CircleCI). Données à l'appui : les équipes qui étaient au 90e percentile en DX il y a trois ans livrent aujourd'hui plus de deux fois plus vite qu'avant l'IA. La maturité d'avant l'IA prédit qui gagne avec l'IA. L'article s'attaque ensuite à la "trajectoire par défaut" des équipes — la dégradation — et explique comment l'inverser à l'âge de l'IA. Le rôle du manager n'est pas réduit, il est rehaussé : c'est lui qui doit créer les conditions pour que l'IA produise du *bon* code, pas juste du code "good enough".

## Points clés

- Données CircleCI : les équipes au top 90e percentile DX en 2023 livrent maintenant >2x plus vite qu'avant l'IA — les autres ne décollent pas
- Trois étapes pour créer du levier avec l'IA : Specs détaillées → Rules réutilisables → Modules de code partagés
- La trajectoire par défaut des équipes est la dégradation (hygiène, capture de connaissance, mauvaises priorités)
- Inverser cette trajectoire est désormais le vrai job du manager
- Tout le monde a accès aux mêmes modèles ; ce qui te différencie, c'est l'environnement autour

## Analyse approfondie

Hé, Luca à l'écriture. Voici le troisième et dernier article de notre série Software Factory, écrit avec mon ami Rob Zuber, CTO chez CircleCI.

Avant celui-ci, nous avons publié :
1. *The Era of the Software Factory*
2. *How to Grow your Software Factory*

Pourquoi trois articles ? Parce qu'on aime travailler à partir des premiers principes.

Dans le premier article, on a établi (avec des données réelles) que les équipes qui vont loin avec l'IA le font grâce à un bon DX. Les mêmes équipes qui avaient un bon DX il y a trois ans gagnent maintenant la course de l'IA : celles au 90e percentile shippent désormais plus de 2x plus vite qu'avant.

Dans le second, on a dit : ok, mais une fois que tu as un bon DX, comment tu crées du levier avec l'IA ? Et on a posé un plan en trois étapes :

1. **Specs** — commencer par écrire de bonnes instructions détaillées sur ce qui doit être fait. Ex : "crée un bouton qui a les caractéristiques suivantes [...]"
2. **Rules** — transformer les specs en règles réutilisables que l'IA peut suivre. C'est quand tu peux dire à l'IA : "crée un bouton en utilisant nos règles de création de boutons"
3. **Modules** — l'étape finale, quand l'IA peut réutiliser du code directement, pas des règles, et tu dis simplement : "crée un primary button"

Ça semble *good enough*, alors pourquoi un troisième article ?

Parce que si tu fais tout ça correctement, ton résultat sera : un process solide où l'IA produit du travail *good enough* pour être livré. Et même si c'est déjà ambitieux, je pense qu'il faut viser plus haut.

### La trajectoire par défaut, c'est la dégradation

La réalité inconfortable des équipes d'ingénierie jusqu'ici : la plupart des bases de code se dégradent avec le temps. Plus on avance, plus c'est dur d'y faire des changements. C'est l'entropie.

### Ce qui cause la dégradation

- **Hygiène de code** qui se relâche : tests sautés, refactos repoussés, code mort qui s'accumule
- **Capture de connaissance** absente : les onboardings prennent six mois parce qu'aucune doc à jour
- **Mauvaises priorités** : on construit ce qui se voit, pas ce qui compte

### Comment aller dans l'autre sens

Sur chaque dimension, il existe une pratique pour inverser la pente. Et l'IA, bien utilisée, est un accélérateur de ces pratiques :

- L'IA peut écrire des tests rétroactivement
- L'IA peut produire de la documentation
- L'IA peut signaler les patterns dégradants

Mais elle ne le fait que si on le lui demande. Et c'est ça, le travail du manager.

### Empowering managers

C'est le territoire ultime du manager. Dans l'âge de l'IA, le manager n'est pas remplacé : il devient celui qui :

- Définit ce qui est *bon*, pas juste fonctionnel
- Refuse de livrer ce que personne ne comprend
- Investit dans les routes (l'environnement de dev) plutôt que dans les Ferraris (les outils)
- Empêche la dégradation de gagner

Tout le monde a accès aux mêmes modèles. Ce qui différencie une équipe, c'est ce qu'elle construit autour.

## Pourquoi ça compte

C'est l'article qui réconcilie la promesse de l'IA et la réalité du management. Les chiffres CircleCI sont précieux pour les conversations en comex : non, l'IA ne nivelle pas le terrain — elle amplifie l'écart entre équipes matures et équipes immatures.
