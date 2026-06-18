---
title: "You Got Faster. Your Company Didn’t."
date: 2026-06-18
url: https://terriblesoftware.org/2026/06/17/you-got-faster-your-company-didnt/
authors: [terriblesoftware.org]
keywords: [productivity, AI, code review, technical debt, organization]
theme: Leadership
tone: opinion
used_in: ["2026-06-18"]
---

## Résumé

Grâce à l'IA, chaque individu d'une équipe se sent plus productif, et pourtant l'entreprise dans son ensemble n'avance pas plus vite. L'auteur explique ce paradoxe : la productivité individuelle de l'IA ne fait que transférer le travail (la lecture, la vérification, la compréhension) aux relecteurs, car un document a un seul auteur mais de multiples lecteurs. Aller plus vite en refilant la partie lente à celui qui vient après ressemble à une « chaîne de Ponzi ». Il rappelle la citation de Pascal : « J'aurais écrit une lettre plus courte, mais je n'ai pas eu le temps. »

## Points clés

- L'IA rend chaque personne individuellement plus rapide, mais l'organisation entière ne s'accélère pas pour autant.
- Le temps économisé par l'auteur est en réalité transféré aux relecteurs : un raccourci pour l'un devient un problème pour tous.
- Un document généré par IA oblige les relecteurs à tout vérifier (fact-checking) faute de pouvoir distinguer ce que l'auteur assume de ce que le modèle a inventé.
- Un document est un service : le deal implicite est que l'auteur dépense son temps pour que les lecteurs n'aient pas à le faire.
- Le même schéma se retrouve dans les pull requests, les tests automatisés et même les décisions.
- La compression, l'édition et la vérification *sont* le travail ; il faut consacrer une partie des heures gagnées grâce à l'IA à éditer.

## Analyse approfondie

> *« J'aurais écrit une lettre plus courte, mais je n'ai pas eu le temps. »* — Blaise Pascal

À cause de l'IA, tout le monde dans votre équipe est plus productif qu'il ne l'était il y a un an, il suffit de leur demander. Alors pourquoi *l'entreprise* elle-même n'est-elle pas plus rapide ?

Je crois savoir pourquoi.

Disons qu'un ingénieur doit rédiger un brief technique pour une migration de base de données. Il y a deux ans, cela lui aurait coûté un après-midi entier : lire le code et quelques articles en ligne, peser les options, écrire, supprimer, réécrire. Le résultat était court, et chaque mot avait survécu au contact de son cerveau.

Avançons jusqu'à aujourd'hui : il colle le contexte dans un modèle et appuie sur envoyer. Quelques minutes plus tard, l'agent lui rend un plan plusieurs fois plus long que tout ce qu'il aurait écrit à la main.

Eh bien, il est plus productif maintenant, non ? Une fraction du temps, plusieurs fois plus de production. Mais qu'en est-il de tous les autres ? Une poignée de relecteurs ouvrent un document plusieurs fois plus long qu'il ne devrait l'être, avec cette odeur d'IA caractéristique dessus.

Et la longueur n'est pas le plus gros problème ! Étant donné que le document a clairement été généré par IA, chaque relecteur est désormais aussi en train de le vérifier point par point. Le brief dit que le job actuel traite les événements de manière séquentielle. Vraiment ? Il dit que la migration touche neuf tables. Est-ce bien neuf ? Quand un collègue écrit une phrase comme ça à la main, vous lui faites confiance, parce que quelqu'un a compté et a mis son nom sur ce décompte. Quand c'est un modèle qui l'écrit, et que l'auteur n'a pas vérifié, la phrase a exactement la même apparence. Vous ne pouvez pas distinguer les affirmations qu'il assume de celles que le modèle a rêvées, donc vous devez traiter chaque ligne comme non vérifiée. Les relecteurs finissent par faire la réflexion que l'auteur a esquivée (sauf que cette fois elle arrive joliment formatée, et avec assurance ![Image 1: 🥲](https://s.w.org/images/core/emoji/17.0.2/svg/1f972.svg)).

Donc chacune de ces relectures prend maintenant plus de temps qu'avant. Il s'est épargné *à lui-même* l'après-midi et a tranquillement dépensé celui de tous les autres. Le temps a simplement été transféré, et parce qu'un document a un seul rédacteur et de nombreux lecteurs, le raccourci d'une personne devient le problème de tous.

Voyez-vous, un document est censé être un service. Le deal (implicite) est que le rédacteur dépense son temps pour que les lecteurs n'aient pas à le faire. C'est pourquoi Pascal, dans la citation en haut, s'excusait : la longue lettre est bon marché pour moi et coûteuse pour vous, la courte lettre est coûteuse pour moi et bon marché pour vous. Au travail, je vous dois généralement la courte parce qu'il y a un seul moi et de nombreux vous. La compression, l'édition et la vérification *sont* le travail.

Au passage, ce n'est pas seulement les documents… Je vois aussi le même schéma dans les pull requests, les tests automatisés, et même les décisions. **Nous allons plus vite en refilant la partie lente (la lecture, la compréhension réelle) à celui qui vient après**. Une chaîne de Ponzi ?

Comprenez-moi bien : utilisez l'IA, par tous les moyens. Je l'utilise aussi, et je ne reviendrai (probablement) pas en arrière. Le truc, c'est que le modèle vous rend de nombreuses heures, alors s'il vous plaît, dépensez-en un peu à éditer !

J'ai déjà une règle pour le code écrit par l'IA : [si je ne peux pas expliquer le changement, je ne peux pas l'expédier](https://terriblesoftware.org/2026/05/27/using-my-fucking-brain/). La même règle s'applique ici : si vous ne pouvez pas défendre une phrase une fois le document terminé, c'est qu'il n'est pas vraiment terminé, n'est-ce pas ?

Et si vous êtes du côté de ceux qui reçoivent ces documents, vous avez le droit de pousser en retour et de dire : *« Ça se lit comme un brouillon non édité. Peux-tu le réduire à la décision, aux compromis, et à ce dont tu as besoin de ma part ? Je serai content de le relire ensuite. »*

* * *

Voilà donc pourquoi l'entreprise n'accélère jamais, même quand tout le monde en son sein accélère. Le temps que l'ingénieur a économisé n'est pas allé quelque part de bon : il a atterri sur tous ceux qui ont dû lire son document.

Et encore une fois, il ne ment pas quand il dit qu'il est plus rapide. Il l'est. Moi aussi, la plupart du temps. La vitesse est bien réelle pour chacun de nous *individuellement*. C'est juste que lorsque vous l'additionnez à l'échelle de l'équipe, elle pointe dans la mauvaise direction ; tout le monde est plus rapide, et l'ensemble avance pourtant plus lentement.

Ce qui me fait penser que nous devons à ceux qui nous lisent un peu plus que ce que nous leur avons donné ces derniers temps.

## Pourquoi ça compte

Ce paradoxe rappelle aux leaders techniques que la productivité de l'IA ne se mesure pas à l'échelle individuelle mais à l'échelle du système : optimiser le débit de chacun sans discipline d'édition peut paradoxalement ralentir l'organisation entière.
