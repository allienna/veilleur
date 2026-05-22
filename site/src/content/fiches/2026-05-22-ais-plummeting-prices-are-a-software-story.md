---
title: "AI's Plummeting Prices Are a Software Story, Not a Hardware One"
date: 2026-05-22
url: https://weightythoughts.com/p/ais-plummeting-prices-are-a-software
authors: [weightythoughts.com]
keywords: [LLMflation, inference cost, open-weight models, software optimization, economics]
theme: IA
tone: opinion
used_in: ["2026-05-22"]
---

## Résumé

L'article explique pourquoi le coût d'inférence des modèles s'effondre et pourquoi des modèles locaux sur du matériel grand public deviennent « assez bons » pour la plupart des usages. Deux macro-tendances se nourrissent l'une l'autre : les coûts d'inférence baissent de 70 à 90 % par an (la « LLMflation », un facteur 1 000 en trois ans), et cette baisse rend les modèles open-weight de plus en plus compétitifs avec la frontière. Le point clé, contre-intuitif : ce n'est pas (principalement) le matériel qui fait chuter les prix — c'est le logiciel.

## Points clés

- Les coûts d'inférence baissent de 70 à 90 % par an ; Guido Appenzeller parle de « LLMflation » — un facteur 1 000 en trois ans.
- L'IA *semble* coûter plus cher parce qu'on monte en gamme (modèles plus gros, requêtes plus chères), alors que le coût à capacité constante s'effondre — comme les ordinateurs malgré la loi de Moore.
- Le moteur principal de cette baisse n'est pas le hardware, mais le software (optimisations d'inférence).
- Conséquence : les modèles open-weight sur du matériel commodité « un peu vieux » deviennent de plus en plus compétitifs avec la frontière.
- Cela menace ce que les labs frontières pourront facturer pour leurs plus gros modèles ; l'auteur a vu sa facture d'agents IA passer d'un futur 2 000 $/mois à presque rien.

## Analyse approfondie

Pourquoi l'inférence des modèles devient-elle moins chère ? Comment l'auteur a-t-il fait passer une facture d'agents IA bientôt supérieure à 2 000 $/mois à presque rien ? Et pourquoi des modèles locaux sur du matériel commodité sont-ils potentiellement « assez bons » pour la plupart des gens ? Deux macro-tendances se nourrissent l'une l'autre.

Premièrement, **les coûts d'inférence IA chutent de 70 à 90 % par an.** Guido Appenzeller a forgé le terme « LLMflation » à partir de son observation initiale : les coûts ont « chuté d'un facteur 1 000 en trois ans ». Peu importe combien de fois on le répète — et combien d'observateurs avisés le soulignent — cela continue de choquer la plupart des gens, parce que l'IA *donne l'impression* de devenir plus chère.

C'est parce que les coûts baissent pour la *même capacité* (même modèle, même requête), alors qu'on augmente constamment ce qu'on utilise (modèle plus gros, requête plus coûteuse). C'est la même raison pour laquelle, malgré la loi de Moore (plus lente que la LLMflation), les ordinateurs ne coûtent pas 0,00001 $ : on les a rendus plus gros à mesure, même quand leur coût s'effondrait exponentiellement.

Ça, c'est l'histoire ancienne. La partie intéressante, c'est ce qui *pilote* cette chute des coûts. **Ce n'est pas (principalement) le matériel. C'est le logiciel.** (L'auteur s'appuie sur un graphique a16z montrant la division par 10 du coût par an.)

La deuxième tendance en est une conséquence : **les modèles locaux, open-weight, sur du matériel commodité un peu daté, deviennent de plus en plus compétitifs avec les modèles de la frontière.** Cela a évidemment de grandes implications — et de potentielles conséquences — sur ce que les labs frontières pourront finalement facturer pour leurs plus gros modèles.

L'auteur explique avoir écrit cet article presque par accident : il a toujours expérimenté avec des modèles open-weight, même quand ça n'avait aucun sens de les faire tourner, et son historique public de bidouille avec les modèles de langage remonte à 2014.

## Pourquoi ça compte

Comprendre que la baisse des prix est une histoire de logiciel, pas de matériel, change la planification : l'intelligence devient quasi-gratuite et jetable, ce qui justifie économiquement les flottes d'agents et fragilise le pricing des labs frontières.
