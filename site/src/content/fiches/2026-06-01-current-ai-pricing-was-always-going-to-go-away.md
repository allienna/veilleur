---
title: "The current AI pricing was always going to go away"
date: 2026-06-01
url: https://leadershipintech.com/links/22430/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [leadershipintech.com]
keywords: [pricing, inférence, demande induite, HBM, GPU]
theme: IA
tone: opinion
used_in: ["2026-06-01"]
---

## Résumé

Le forfait IA bon marché est une parenthèse subventionnée qui se referme. Microsoft a annulé des licences Claude Code internes, Uber a épuisé son budget IA 2026 en quatre mois et GitHub supprime ses offres à tarif fixe. Deux forces convergent : la demande induite (l'inférence moins chère fait exploser les usages, pas la facture) et une offre de mémoire/GPU qui se renchérit brutalement. La conséquence : seules les architectures de prix indexées sur le coût réel (per-action, crédits, hybride) survivront.

## Points clés

- L'« ère de la subvention IA » se termine : les labs n'ont plus le choix que de répercuter leurs coûts.
- Demande induite : baisser le coût par token ne réduit pas la dépense, il décuple ce qu'on demande au modèle (analogie de l'autoroute et des trajets).
- Côté offre, la HBM a quadruplé en 18 mois et le BOM des NVIDIA VR200 grimpe de 95 % (Morgan Stanley), la mémoire pesant pour +435 %.
- Le CFO d'Anthropic a témoigné sous serment : 10 Md$ de compute pour 5 Md$ de revenus.
- Trois modèles de tarification tiennent face à un coût mobile : per-action, crédits, hybride. Le per-seat est le seul qui fait semblant que les coûts sont fixes.

## Analyse approfondie

La tarification IA actuelle allait forcément disparaître. Elle n'a tout simplement aucun sens.

Microsoft a annulé ses licences Claude Code internes cette semaine (peu importe la raison, même si c'est parce qu'ils l'ont intégré), Uber a cramé tout son budget IA 2026 en quatre mois, et GitHub supprime les offres à tarif forfaitaire sur l'ensemble de ses produits.

Vous verrez la formule « la fin de l'ère des subventions IA », façon polie de décrire ce que tout le monde a fait : coller des fonctionnalités IA dans chaque palier de leur produit, en pariant que les coûts d'inférence continueraient de baisser.

Ils n'ont pas baissé, la courbe des coûts plie dans le mauvais sens, et les labs n'ont d'autre choix que de répercuter.

### A-t-on collectivement oublié la pensée du second ordre ?

À chaque génération de modèle, le coût par token a bien baissé, parfois 10x, mais c'était à qualité comparable… Beaucoup de gens ont extrapolé et bâti des modèles économiques sur cette extrapolation, ce qui… n'est pas la bonne façon de raisonner.

La pensée du second ordre, quelqu'un ?

Tous ceux qui font de la planification routière connaissent la demande induite. Chaque nouvelle capacité invente une nouvelle demande. Les autoroutes en sont l'exemple type. Ajoutez une voie, vous récupérez de nouveaux trajets. Ces trajets n'existaient pas avant la voie. L'IA suit la même forme. Une inférence moins chère ne réduit pas la facture, elle élargit ce qu'on demande au modèle.

Mes requêtes de raisonnement prennent maintenant plus de 4 minutes, là où les anciennes en prenaient 2… Les workflows agentiques font 50 appels là où l'ancien en faisait un seul. Le coût unitaire baisse, les unités explosent, mais la dépense totale grimpe quand même.

Quiconque vend un « assistant IA » à tarif forfaitaire supposait que le comportement des utilisateurs ne changerait pas. Il a changé. Il change toujours.

La seconde force, c'est que l'offre a cessé de coopérer : l'économie de la mémoire et des GPU se retourne contre vous.

### La mémoire est devenue 4x plus chère. Les GPU plus de 95 % plus chers.

L'entraînement et l'inférence de pointe tournent sur des accélérateurs Nvidia couplés à de la mémoire à haute bande passante (HBM). Le plafond n'est plus le transistor, c'est la HBM et le packaging avancé qui la lie à la puce de calcul.

Morgan Stanley estime que le bill of material (BOM) des nouveaux NVIDIA VR200 sera 95 % plus élevé, la mémoire comptant à elle seule pour +435 %.

Ce plafond ne tient qu'à une seule usine de profondeur. La ligne de packaging CoWoS de TSMC était et reste le goulot d'étranglement de l'approvisionnement en accélérateurs. SK Hynix domine la HBM (et est devenue une entreprise très en vue, avec Samsung à la traîne et Micron derrière). Aucun ne peut ajouter de capacité du jour au lendemain. Ce sont des engagements de 18 à 36 mois minimum, planifiés pour un monde qui sous-estimait la demande d'un ordre de grandeur.

Le prix des GPU, c'est donc à quoi ressemble une tarification de pénurie. Le nec plus ultra des GPU, TPU et autres accélérateurs est ~2x plus cher que la génération précédente à échelle de cluster comparable. Les prix de la HBM ont quadruplé en 18 mois. L'énergie et le refroidissement sont désormais de vraies contraintes là où personne ne modélisait la puissance, d'où le fait que chaque hyperscaler ait son histoire de « campus d'un gigawatt » et son communiqué de presse sur un contrat nucléaire (PPA) — que ça se réalise ou non.

Le CFO d'Anthropic a témoigné sous serment en mars que l'entreprise avait dépensé 10 milliards de dollars en compute pour 5 milliards de revenus (Ed Zitron en fait le calcul, qui me semble juste). Les labs sont complètement sous l'eau côté compute et inférence, alors ils augmentent les prix pour garder la lumière allumée.

Les entreprises qui ont vendu des produits « IA partout » à tarif forfaitaire se retrouvent avec un problème de marge qu'elles se sont elles-mêmes architecturé. Le pari était qu'une de ces courbes plierait en leur faveur. Aucune ne l'a fait, aucune ne le fera probablement, certainement pas sur le calendrier que supposait leur tarification.

### Ce qui change à partir de maintenant

La question produit se déplace. On ne demande plus « où peut-on ajouter de l'IA ? » mais « quels cas d'usage méritent le coût d'inférence qu'ils brûlent ? ». C'est une roadmap plus difficile à écrire. Cela change aussi la surface de tarification, la partie que la plupart des équipes produit n'ont pas intégrée.

Trois architectures encaissent un coût mobile. Aucune n'est nouvelle. Toutes sont inconfortables pour des équipes commerciales habituées à vendre des sièges.

**Per-action.** Chaque appel API, chaque génération, chaque étape d'agent a un prix. Le revenu suit le coût car ils sont indexés sur le même événement sous-jacent. Twilio fait ça depuis 2008, AWS depuis 2006. L'inconvénient : la transparence coupe dans les deux sens, le client voit le compteur et négocie. L'avantage : votre marge brute ne dépend pas d'une devinette sur l'intensité d'usage de vos power users.

**Crédits.** Des seaux prépayés. Le client achète 100 000 crédits, les consomme sur ce qu'il veut, recharge. Les crédits lissent la trésorerie et permettent de mélanger les coûts de modèles derrière une seule unité, seule façon saine de gérer un produit qui route entre cinq fournisseurs d'inférence. Le piège : le breakage. Les crédits Snowflake sont de l'infrastructure, les clients comprennent ce qu'ils achètent. Beaucoup de crédits finissent en actifs échoués (comme une carte cadeau oubliée) et les clients savent reconnaître lequel ils ont acheté. On ne fait le second qu'une fois.

**Hybride !** Le nouveau favori de tout le monde (donc pas vraiment nouveau) : un siège de base avec des crédits inclus et un dépassement facturé à la consommation. La plupart des cycles de vente entreprise l'acceptent sans trop de résistance, parce qu'un nombre de sièges (ou un « forfait plateforme fixe ») ancre encore le contrat et que le compteur sert de soupape de sécurité. C'est le design vers lequel convergent la plupart des produits AI-native dès leur premier cycle de retarification.

Le point n'est pas la forme elle-même mais de savoir si la ligne bouge quand la ligne de coût bouge. Le per-seat est la seule architecture qui prétend que les coûts sont fixes. Tout le reste indexe le revenu sur l'événement sous-jacent.

### Le choix impossible

Si votre tarification peut bouger avec le coût, vous continuez à construire. Vous pouvez livrer le workflow agentique, le modèle de raisonnement plus lourd, la fonctionnalité lente et coûteuse pour power users — et vous avez un moyen d'être payé pour ça.

Si vous êtes verrouillé sur du per-seat (ou du forfait), vous choisissez entre deux options perdantes : encaisser la marge et la regarder se comprimer chaque trimestre où l'usage de vos clients grimpe, ou retirer l'IA de vos paliers les moins chers et regarder votre taux d'activation chuter sur les cohortes à bas prix.

## Pourquoi ça compte

C'est le cadre conceptuel le plus clair pour comprendre la bascule économique de l'IA en 2026 : la demande induite et le mur mémoire expliquent pourquoi les factures explosent malgré des tokens moins chers. Indispensable pour quiconque décide d'une stratégie produit ou pricing autour de l'IA.
