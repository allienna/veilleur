---
title: "RDEL #137: What kinds of new debt are teams accumulating with AI?"
date: 2026-04-03
url: "https://link.mail.beehiiv.com/ss/c/u001.71LCQkoHczeoiEaexlZjtjNH4ATSZBzBEVr3dqi6a5i3h23INcLJkXo0_uWUYOYoQFYm6DiTSalPiLwDoZBV38W1EJQyKDKyvnx-oljK2WyJKA5lpX-bYhIt-ejLBBAMgck3emFJnqhroInk8dsLFdzYG7Knqzv0020UNkw1b8g_YGtxI25Zm48XZy2yIwNs/4ph/Gsov6Q6FSgKOvnO9xaXguA/h8/h001.83WoYC25RVHG1FqHZFqyL4LX2Mz7obh5YH-C7Vhx5Ts"
authors: ["Research-Driven Engineering Leadership"]
keywords: [dette technique, dette cognitive, dette sociale, IA, santé logicielle]
theme: "Leadership"
tone: research
used_in: ["2026-04-03"]
---

## Résumé

La Dr. Margaret-Anne Storey propose un "modèle de triple dette" pour caractériser ce que les équipes accumulent lorsqu'elles adoptent l'IA dans leur développement : une dette technique (dans le code), une dette cognitive (dans les personnes — érosion de la compréhension partagée) et une dette sociale (dans les relations — perte de confiance et de coordination). L'IA accélère l'accumulation des trois simultanément. Les outils traditionnels de suivi de la dette technique sont insuffisants pour capturer ces nouvelles dimensions, et les équipes ont besoin d'indicateurs spécifiques pour mesurer la santé de la compréhension et de la coordination.

## Points clés

- L'IA génère du code propre que personne dans l'équipe ne peut expliquer : c'est la dette cognitive
- La dette sociale se manifeste par la perte de vocabulaire partagé, des revues de code superficielles et un onboarding plus long
- Les trois types de dette se renforcent mutuellement et s'accumulent plus vite avec l'IA qu'avec le développement traditionnel
- Les outils classiques de mesure de la dette technique (SonarQube, etc.) ne capturent ni la dette cognitive ni la dette sociale
- Des indicateurs pratiques existent : fraîcheur de la documentation, profondeur des revues de PR, ratio de commentaires "pourquoi", facteur bus, points de contact de mentorat
- La synthèse couvre plusieurs études empiriques, pas seulement des observations anecdotiques

## Analyse approfondie

### Le constat de départ : la dette ne s'arrête pas au code

La newsletter RDEL (Research-Driven Engineering Leadership) consacre son numéro 137 à une question que peu d'équipes se posent encore : quelle dette accumule-t-on réellement en adoptant l'IA dans le développement logiciel ? La réponse habituelle se cantonne à la dette technique — du code généré rapidement, potentiellement mal structuré, difficile à maintenir. Mais les recherches de la Dr. Margaret-Anne Storey, chercheuse réputée en génie logiciel, suggèrent que c'est bien plus complexe.

Son modèle de triple dette identifie trois dimensions distinctes qui s'accumulent simultanément lorsqu'une équipe adopte des outils d'IA pour le codage.

### La dette technique : ce que l'on connaît déjà

La première dimension est la plus familière. La dette technique désigne le code qui fonctionne mais qui sera coûteux à modifier, tester ou comprendre dans le futur. Avec l'IA, cette dette prend une forme particulière : le code généré est souvent syntaxiquement propre, respecte les conventions, mais peut manquer de cohérence architecturale à grande échelle, dupliquer de la logique sans le savoir, ou adopter des patterns inadaptés au contexte spécifique du projet.

Le paradoxe est que la dette technique générée par l'IA est moins visible que celle produite par un développeur pressé. Un code humain bâclé se repère à ses noms de variables cryptiques, ses commentaires absents, ses fonctions trop longues. Le code IA peut être impeccablement formaté tout en étant profondément inadapté aux besoins réels.

### La dette cognitive : l'érosion de la compréhension partagée

La deuxième dimension est moins connue mais potentiellement plus dangereuse sur le long terme. La dette cognitive se loge dans les personnes, pas dans le code. Elle représente l'érosion progressive de la compréhension partagée au sein de l'équipe : qui sait pourquoi telle décision architecturale a été prise ? Qui comprend réellement le fonctionnement du module de paiement que l'agent a généré il y a trois mois ?

Lorsqu'un développeur écrit du code manuellement, il en assimile la logique par le fait même de l'écrire. Il peut expliquer ses choix, les défendre, les adapter. Lorsqu'un agent génère ce même code en quelques secondes, cette assimilation n'a pas lieu — sauf si le développeur prend le temps de lire et comprendre chaque ligne, ce qui annule une grande partie du gain de productivité.

L'onboarding de nouveaux membres devient plus difficile. Il n'y a plus de "l'auteur de ce code peut t'expliquer pourquoi il a fait ça" — l'auteur est un modèle de langage qui n'est plus disponible pour répondre aux questions. La documentation se retrouve en décalage avec le code réel. Les commentaires "pourquoi" — ceux qui expliquent la raison d'être d'un choix plutôt que sa mécanique — disparaissent.

### La dette sociale : la dégradation des relations et de la coordination

La troisième dimension est la plus subtile. La dette sociale touche aux relations entre les membres de l'équipe et aux mécanismes de coordination. Elle se manifeste par une perte de confiance mutuelle, un vocabulaire partagé qui s'érode, et une coordination qui devient plus difficile.

Les revues de code (pull requests) sont un exemple frappant. Quand un agent génère 500 lignes de code fonctionnel, combien de reviewers prennent le temps de les lire ligne à ligne ? La tendance naturelle est de faire confiance au résultat — après tout, les tests passent. Mais c'est précisément dans cette revue superficielle que la dette sociale s'accumule : les reviewers perdent leur habitude d'engagement profond avec le code, leur capacité à repérer des problèmes subtils, et leur sentiment de responsabilité collective sur la base de code.

Le vocabulaire partagé s'érode également. Dans une équipe qui développe manuellement, les discussions autour du code forgent un langage commun : "notre façon de gérer les erreurs", "notre convention pour les services", "notre pattern d'authentification". Quand l'agent génère tout ça, ce langage commun n'émerge pas de la même façon. Des termes différents peuvent être utilisés pour des concepts identiques, créant des malentendus invisibles.

### L'accélération par l'IA

Ce qui rend ce modèle particulièrement pertinent aujourd'hui, c'est que l'IA n'introduit pas ces types de dette — elle les accélère tous les trois simultanément. Un développeur qui prend des raccourcis accumule de la dette technique. Une équipe qui grandit trop vite accumule de la dette cognitive et sociale. Mais ces processus prennent du temps. Avec l'IA, la vitesse de génération de code est telle que les trois dettes peuvent s'accumuler en quelques semaines à un rythme qui prendrait normalement des années.

La synthèse présentée dans RDEL #137 s'appuie sur plusieurs études empiriques — pas seulement des observations anecdotiques — ce qui lui confère une solidité particulière. Les auteurs ont analysé des équipes en transition vers l'IA et mesuré l'évolution de ces trois dimensions dans le temps.

### Des indicateurs pratiques pour mesurer la santé des équipes

Face à ce constat, le modèle propose des indicateurs concrets pour suivre la santé de l'équipe au-delà de la dette technique classique :

- **Fraîcheur de la documentation** : quel est l'écart moyen entre la date de modification du code et celle de la documentation associée ?
- **Profondeur des revues de PR** : nombre moyen de commentaires par PR, et surtout ratio de commentaires substantiels vs approbations silencieuses
- **Ratio de commentaires "pourquoi"** : quelle proportion des commentaires de code expliquent la raison d'être d'un choix plutôt que sa mécanique ?
- **Facteur bus** : combien de personnes comprennent suffisamment chaque partie critique du système pour le maintenir si quelqu'un quitte l'équipe ?
- **Points de contact de mentorat** : combien d'interactions formelles ou informelles de transmission de connaissance ont lieu chaque semaine ?

Ces indicateurs ne remplacent pas les métriques techniques classiques — couverture de tests, complexité cyclomatique, dette SonarQube — mais les complètent pour donner une image plus complète de la santé du système sociotechnique qu'est une équipe de développement.

## Pourquoi ça compte

Le modèle de triple dette offre aux Engineering Managers un cadre conceptuel pour anticiper des risques que les métriques techniques traditionnelles ne voient pas venir, et pour justifier des pratiques — revues approfondies, documentation, mentorat — qui semblent moins urgentes face à la pression de productivité que crée l'IA.
