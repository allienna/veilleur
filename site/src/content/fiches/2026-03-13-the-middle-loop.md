---
title: "The Middle Loop"
date: 2026-03-13
url: "https://annievella.com/posts/the-middle-loop/"
authors: ["Annie Vella"]
keywords: [étude longitudinale, développeurs, allocation du temps, boucle intermédiaire, vérification, code review]
theme: IA
tone: research
used_in: ["2026-03-13"]
---

## Résumé

Annie Vella présente les résultats d'une étude longitudinale menée sur 6 mois avec 158 ingénieurs logiciels dans 28 pays. 82 % rapportent passer moins de temps à écrire du code, mais le temps libéré ne remonte pas vers la conception et l'architecture comme on le suppose habituellement. Il se compresse sur toutes les tâches et migre vers une nouvelle « boucle intermédiaire » : orchestrer, vérifier et itérer avec l'IA. La seule tâche en augmentation est la code review. Le rôle de développeur est en train d'être redéfini en temps réel.

## Points clés

- 82 % des ingénieurs rapportent passer moins de temps à écrire du code au second questionnaire
- Le temps libéré ne remonte PAS vers la conception/architecture — il se compresse sur les 6 tâches mesurées
- Une nouvelle "boucle intermédiaire" (middle loop) émerge : orchestrer l'IA, vérifier ses outputs, itérer
- La code review est la seule tâche où les ingénieurs rapportent passer plus de temps
- Basculement de la création vers la vérification (creation-to-verification shift) mesuré sur 6 mois
- L'étude est longitudinale (2 points de mesure) avec 95 participants appariés, ce qui donne un signal robuste

## Analyse approfondie

Au début de sa carrière, Annie Vella a pris un poste de développeuse logiciel dans un grand cabinet de conseil. Il s'est avéré que le travail consistait principalement à réparer les bases de données Access d'autres personnes en faisant un clic droit et en appuyant sur « réparer ». Elle a tenu environ un mois avant de remercier pour l'opportunité, de remettre sa démission et de passer à autre chose.

Le point important : ce sur quoi vous passez votre temps définit ce à quoi vous pensez. Ce à quoi vous pensez est ce que vous pratiquez. Et ce que vous pratiquez est ce sur quoi vous développez des compétences. L'intitulé du poste disait « développeuse logiciel » mais le travail quotidien disait tout autre chose.

C'est pourquoi la première question de recherche qu'elle a voulu explorer dans le cadre de son Master d'Ingénierie à l'Université d'Auckland, supervisé par Kelly Blincoe, portait sur la concentration des tâches. Les outils IA sont-ils en train de modifier où les ingénieurs passent réellement leur temps et leurs efforts ? Parce que si c'est le cas, ils modifient implicitement les compétences que nous pratiquons et, in fine, la définition même du rôle.

Sur six mois, d'octobre 2024 à avril 2025, elle a mené une étude longitudinale à méthodes mixtes avec des ingénieurs logiciels professionnels répartis dans 28 pays — 158 participants éligibles au premier round, 101 au second, avec 95 appariés sur les deux rounds. C'est le premier d'une série d'articles partageant ses découvertes.

### Le temps manquant

Elle a demandé aux participants comment leur allocation de temps avait évolué sur six tâches de développement fondamentales : concevoir, écrire du code, refactorer, tester, déboguer et reviewer.

Cinq des six tâches présentaient des moyennes inférieures au neutre — les participants rapportaient passer moins de temps sur presque tout. L'écriture de code montrait la réduction la plus forte, avec 82 % rapportant passer moins de temps au second questionnaire. La review de code était la seule tâche où les ingénieurs rapportaient passer *plus* de temps, et encore, seulement légèrement au-dessus du neutre.

Ce sont des perceptions, pas des mesures chronométriques, et les gens ne sont généralement pas doués pour estimer le temps. Mais des variations aussi cohérentes, mesurées deux fois sur six mois, constituent quand même un signal significatif.

D'accord, les ingénieurs passent moins de temps à écrire du code, pas de surprise. Mais l'hypothèse standard — selon laquelle le temps libéré remonte vers la conception et l'architecture — ne tient pas. Le temps s'est compressé sur la quasi-totalité des six tâches, y compris la conception. Plutôt que d'échanger du temps d'écriture contre du temps de conception, les ingénieurs rapportent passer moins de temps sur presque tout.

Alors où va réellement ce temps ?

### Nommer le nouveau travail

Les données quantitatives ont révélé un **basculement de la création vers la vérification** au cours des six mois d'étude — l'équilibre entre la production de code et la vérification de code s'est déplacé en faveur de la vérification. Les entretiens ont aidé à expliquer pourquoi.

Les ingénieurs ont décrit un nouveau rythme de travail. Ils ne partent plus d'un fichier vide pour construire progressivement. Au lieu de cela, ils commencent par orchestrer — configurer le contexte, formuler l'intention, choisir l'outil. Puis ils génèrent — demandant à l'IA de produire du code, des tests, de la documentation. Ensuite vient le travail que beaucoup ont décrit comme la partie la plus longue : évaluer et itérer. L'output est-il correct ? Est-il complet ? Correspond-il à l'architecture ? S'intègre-t-il au reste du système ?

Ce cycle — orchestrer, générer, évaluer — est ce qu'elle appelle la **boucle intermédiaire** (middle loop).

Elle l'appelle « intermédiaire » parce qu'elle se situe entre deux boucles existantes bien connues :

- La **boucle interne** (inner loop) : le cycle classique écrire-compiler-exécuter-déboguer que les développeurs connaissent intimement
- La **boucle externe** (outer loop) : le cycle plus large de planification, review, déploiement, feedback

La boucle intermédiaire n'est ni écrire du code ni planifier du travail. C'est le travail continu d'orchestration d'une intelligence non-humaine, de vérification de ses outputs et d'itération vers quelque chose qui fonctionne. Et elle absorbe le temps que les gens pensaient récupérer.

### Ce que la boucle intermédiaire contient

Dans les entretiens, les ingénieurs ont décrit des activités spécifiques qui peuplent cette boucle :

- **Cadrage du contexte** : configurer le bon contexte pour l'IA, choisir quels fichiers inclure, quelle documentation référencer
- **Formulation d'intentions** : apprendre à exprimer ce qu'on veut de manière que l'IA puisse comprendre et exécuter
- **Évaluation des outputs** : reviewer le code généré non pas comme on reviewe le code d'un collègue, mais avec un scepticisme accru envers les hallucinations et les erreurs subtiles
- **Itération corrective** : guider l'IA à travers des corrections, reformuler les demandes, contraindre les résultats

### Implications pour la profession

Si ce sur quoi nous passons notre temps définit ce que nous pratiquons, et si ce que nous pratiquons définit nos compétences, alors la boucle intermédiaire est en train de redéfinir ce qu'est un développeur logiciel. Le rôle se déplace : moins de production de code, plus d'orchestration et de vérification. Moins d'artisan, plus de superviseur d'une intelligence non-humaine.

La question ouverte est de savoir si c'est une transition temporaire — une phase d'apprentissage où nous apprenons à travailler avec l'IA — ou un changement permanent dans la nature du travail de développement logiciel.

Les données de cette étude suggèrent que c'est un changement structurel, pas transitoire. Les mesures au second point temporel montrent un approfondissement des tendances, pas une normalisation.

## Pourquoi ça compte

C'est l'une des rares études longitudinales avec des données solides sur l'impact réel de l'IA sur le travail des développeurs — elle invalide l'hypothèse confortable selon laquelle le temps économisé sur le code serait réinvesti dans la conception, et nomme la nouvelle réalité : la boucle intermédiaire.
