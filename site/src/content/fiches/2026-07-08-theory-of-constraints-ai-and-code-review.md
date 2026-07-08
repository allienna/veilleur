---
title: "Theory of constraints, AI, and code review"
date: 2026-07-08
url: https://swizec.com/blog/theory-of-constraints-ai-and-code-review/
authors: [Swizec Teller, swizec.com]
keywords: [théorie des contraintes, code review, productivité IA, goulot d'étranglement, vélocité]
theme: IA
tone: opinion
used_in: ["2026-07-08"]
---

## Résumé

Swizec Teller part d'un constat qui dérange : l'IA permet de produire du code plus vite que jamais, mais les entreprises shippent toujours à la même vitesse. Les études montrent des gains de productivité macro marginaux (0,4 à 4 %) malgré des gains individuels spectaculaires (code 50 % plus rapide). L'explication tient dans la théorie des contraintes de Goldratt : une usine ne va pas plus vite que son maillon le plus lent. Accélérer la génération de code quand le vrai goulot est la revue de code ne change rien au débit global.

## Points clés

- Le code n'a aucune valeur tant qu'il n'est pas livré ; produire du code est une vanity metric.
- Les gains de productivité IA au niveau macro sont marginaux : +4 % sur 1 300 entreprises européennes, +0,8 % sur 6 000 dirigeants, +0,4 à 1,3 % à l'échelle des pays riches.
- Pourtant, individuellement : code 50 % plus rapide, +26 % de tâches de code terminées, +15 % de tickets de support fermés, conseil business 25 % plus rapide.
- Théorie des contraintes (Goldratt, version « management » de la loi d'Amdahl) : le système ne va pas plus vite que son maillon le plus lent.
- Le goulot n'est pas la génération de code, c'est la revue : les PR s'accumulent, les relectures traînent des heures ou des jours pendant qu'on produit encore plus de code.

## Analyse approfondie

Peu importe la quantité de code que vous créez, il vaut zéro tant que vous ne le livrez pas. Écrire du code, construire des features, déplacer des tickets, ce sont toutes des vanity metrics. Rien de tout cela ne compte tant que les utilisateurs ne peuvent pas faire quelque chose qu'ils ne pouvaient pas faire avant.

Avec l'IA, vous pouvez produire plus de code, plus vite que jamais. Et ça ne change rien. Je parie que vous shippez encore à peu près à la même vitesse qu'avant, non ?

On le voit dans les données ! On le sent en regardant autour de soi. Tout le monde parle d'utiliser l'IA, de brûler des tokens, de faire du travail, mais on entend rarement les gens dire qu'ils accomplissent plus à l'échelle de l'entreprise.

> La vélocité dépend de la vitesse de review, pas de la vitesse de codage.

**Les preuves sur la productivité de l'IA.** Les gains de productivité liés à l'IA sont marginaux au mieux. Les études montrent une hausse moyenne de 4 % sur 1 300 entreprises en Europe, 0,8 % de production en plus sur 6 000 dirigeants sondés dans le monde, 0,4 % à 1,3 % de production économique en plus dans les pays riches, et ainsi de suite.

Même si la productivité *individuelle* est en hausse — des gens passant 3 h de moins par semaine sur leurs emails, écrivant du code 50 % plus vite, finissant 26 % de tâches de code en plus, fermant 15 % de demandes de support en plus, et faisant du conseil business 25 % plus vite. Tout ce battage, cette agitation, et pas grand-chose à montrer au final. Qu'est-ce qui cloche ?

Je pense que c'est la théorie des contraintes. Ce n'est pas parce que des pièces individuelles bougent plus vite que le système entier peut accomplir davantage.

**La théorie des contraintes.** La théorie des contraintes est la version « management » de la loi d'Amdahl. Dans une série de livres à travers les années 80 et 90, Goldratt a posé que « votre usine ne peut pas aller plus vite que sa pièce la plus lente ». Ça paraît évident, non ? Et je parie que votre entreprise n'est pas du tout optimisée en fonction de cette idée. Dites-moi si ça vous parle : vous produisez plus de code que jamais, vous croulez sous les pull requests et les revues de code, vos yeux se ferment devant de longs documents et des commentaires de code, des descriptions de PR pleines de mots qui ne disent rien, vous attendez des heures ou des jours que des gens regardent votre code, vous menez de longues conversations asynchrones dans les commentaires étalées sur plusieurs jours, et le temps que votre code soit enfin mergé, vous avez produit 10 PR de plus.

**La revue est le goulot.** [L'article poursuit en identifiant la revue de code comme le maillon lent du système : accélérer la génération, en amont de la contrainte, ne fait que gonfler la file d'attente sans augmenter le débit livré. Le levier est de fluidifier la revue — descriptions de PR concises, feedback rapide, réduction des allers-retours asynchrones.]

## Pourquoi ça compte

Un cadre de pensée directement actionnable pour tout Engineering Director : mesurer où se trouve la vraie contrainte avant d'investir dans l'accélération de la génération de code, sous peine de ne récolter aucun gain de débit réel.
