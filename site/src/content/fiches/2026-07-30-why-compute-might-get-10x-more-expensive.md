---
title: "Why compute might get 10x more expensive in coming years"
date: 2026-07-30
url: https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive?utm_source=tldrai
authors: [Dwarkesh Patel]
keywords: [compute, GPU pricing, lab margins, inference, Alchian-Allen]
theme: IA
tone: opinion
used_in: ["2026-07-30"]
---

## Résumé

Dwarkesh Patel time-boxe deux heures pour poser une arithmétique dérangeante : les revenus des labos font x10 par an alors que la capacité de compute ne fait que x3. Pour tenir cette trajectoire, il faut que les marges augmentent, que le prix du compute augmente, ou que les labos consacrent une part croissante de leur compute à l'inférence. Les trois se produisent déjà, mais la conclusion qu'il retient est la deuxième : plus les modèles sont intelligents, mieux ils monétisent le même compute, donc plus le compute devient cher — potentiellement 10 à 15x les prix actuels.

## Points clés

- Les revenus d'Anthropic font x10 en glissement annuel ; le compute des labos ne fait que x3 par an.
- Les prix spot du compute sont en hausse de plus de 40 % depuis le creux de février, et cela sous-estime ce que les labos paient réellement.
- Google paierait 900 M$ par mois pour 110 000 GPU (mix GB200/GB300) louées à SpaceX, environ 2x le prix spot.
- Un ingénieur logiciel humain tournant sur l'équivalent d'une H100 justifierait un loyer de plus de 250 k$/an pour cette H100 — 15x les prix spot actuels.
- Effet Alchian-Allen : à 20 $ l'heure de H100, utiliser un modèle plus faible devient absurde car il brûle plus de tokens pour le même résultat. Les labos les plus efficaces pourront facturer une prime énorme.
- Le x3 de capacité annuelle se décompose en 1,4x loi de Moore, 1,2x nouvelles fabs (bridées par l'offre d'outils EUV jusqu'en 2030 au moins), 1,8x réallocation des wafers de pointe vers l'IA — ce dernier facteur saturant d'ici fin 2027.

## Analyse approfondie

*Note de l'auteur : j'expérimente un format de billet très rapide, en me limitant à deux heures d'écriture. Je ne pourrai pas clouer beaucoup de sous-questions importantes, mais l'alternative est de ne progresser sur aucun des sujets qui m'intéressent.*

### L'arithmétique de départ

Les revenus d'Anthropic ont fait x10 en glissement annuel. Anthropic devrait finir l'année autour de 100 à 150 milliards de dollars de revenus. Pour que cette tendance continue, Anthropic devrait faire 1 000 milliards de dollars de revenus d'ici la fin de l'année prochaine. Il n'y a aucune raison profonde pour que la tendance continue, et elle pourrait très bien s'arrêter — c'est au fond une question de capacités de l'IA. Mais supposons qu'elle continue. Que devrait-il être vrai de ce monde-là ?

Le compute des labos fait x3 par an. Pour qu'un labo fasse x10 de revenus en ne faisant que x3 de compute, il faut une combinaison de trois choses :

1. Les marges des labos augmentent.
2. Le prix du compute augmente.
3. Les labos dépensent une fraction plus grande de leur compute en inférence.

Ces trois choses se produisent déjà, pour l'essentiel :

1. Anthropic est passé de 40 % de marge en 2025 à probablement plus de 80 % cette année pour l'inférence Fable (peut-être pas sur le compute marginal, voir plus bas).
2. Les prix spot du compute sont en hausse de plus de 40 % depuis le creux de février, et cela sous-estime probablement ce que les labos doivent réellement payer.
3. Environ un quart de la dépense compute d'OpenAI en 2024 allait à l'inférence selon Epoch ; on est certainement plus près de 50 % maintenant, si ce n'est plus.

### Pourquoi les labos ne veulent pas de l'option 3

Les labos préféreraient *ne pas* faire le 3 (dépenser une part croissante de leur compute en inférence). Comme on l'a dit en plaisantant, l'intérêt des revenus d'inférence est de convaincre les investisseurs de vous donner plus d'argent pour acheter plus de compute pour entraîner de plus gros modèles. Si vous dépensez l'essentiel de votre compute en inférence, vous déclarez en quelque sorte que le progrès de l'IA a stagné, parce que ça ne vaut plus le coup d'investir davantage en entraînement, et votre business devient celui d'un fournisseur cloud. Les labos ne pensent pas que ce soit vrai : ils pensent servir des modèles qui paraîtront extrêmement mauvais dans un an, afin de construire le business case permettant de continuer à entraîner des modèles plus intelligents.

Il reste donc le 1 (les marges augmentent) ou le 2 (le compute devient plus cher). Ce sera davantage le premier si les 1 ou 2 labos leaders sont significativement devant la concurrence. Dans un marché, vos marges sont fixées par votre avance sur la meilleure alternative. Pour que l'effet 1 domine, les marges devraient atteindre le milieu des 90 % d'ici la fin de l'année prochaine. Cela me paraît assez fou. Mais il me semble plausible que les revenus des labos continuent de croître à une vitesse stupéfiante.

### Le compute devient beaucoup plus cher

Il reste donc un dernier effet pour expliquer comment ce monde à 1 000 milliards de revenus pourrait advenir : le compute devient beaucoup plus cher. Comme mentionné, cela commence déjà. La hausse de prix est encore plus forte sur la tranche de compute dont les labos ont besoin : ils ne peuvent évidemment pas s'appuyer sur des instances spot — il leur faut de la sécurité pour leurs poids et les données clients, et suffisamment d'échelle pour obtenir une bonne utilisation et de la flexibilité.

Pour mesurer la folie du marché sur cette tranche, considérez le prix auquel Google et Anthropic louent du compute à SpaceX. Google paierait 900 millions de dollars par mois pour 110 000 GPU — un mélange de GB200 et GB300. C'est environ 2x le prix spot horaire de ces GPU. Et le prix spot actuel est lui-même 40 % supérieur à celui de février.

**La conclusion clé que je veux souligner : à mesure que les modèles d'IA deviennent plus intelligents, ils monétiseront mieux la même quantité de compute.** Si un véritable ingénieur logiciel de niveau humain pouvait tourner sur l'équivalent d'une H100, aux tarifs de marché actuels des ingénieurs logiciels, cette H100 devrait se louer plus de 250 000 dollars par an. C'est 15x les prix spot d'aujourd'hui.

Bien sûr, on pourrait s'attendre à ce que si nous avons 10 millions d'ingénieurs logiciels supplémentaires, la valeur marginale d'un ingénieur logiciel diminue, et que cette H100 ne produise donc pas nécessairement 15x plus de revenus qu'aujourd'hui. Mais je ne sais pas si c'est vrai. Si nous appliquions cet argument à des humains plutôt qu'à de l'IA, ce serait le classique sophisme du volume de travail fixe (*lump of labour fallacy*). Les économistes considèrent généralement que l'immigration hautement qualifiée ne fait pas baisser les salaires à long terme, en raison de la manière dont la spécialisation et l'innovation augmentent la valeur du travail. Peut-être que ce choc d'offre de travail est si grand et si rapide que cette heuristique générale ne s'applique plus. Mais si l'on croit ce que dit l'économie standard du travail, alors la valeur marginale du compute — et donc son prix marginal — devrait devenir stupéfiante.

### Que se passerait-il dans un tel monde ?

- **Rattraper devient de plus en plus dur.** À mesure que les meilleurs modèles monétisent mieux le compute, il devient de plus en plus difficile de rattraper. Si d'ici 2028 nous avons automatisé l'ingénierie logicielle et que le prix du compute est 15x plus élevé qu'aujourd'hui, il sera bien plus difficile pour vous, sans revenus, de concurrencer les labos de pointe pour l'accès au compute.

- **Les marges de l'efficacité explosent.** Si vous pouvez entraîner le modèle le meilleur et le plus efficace, vous pourrez facturer des marges BEAUCOUP plus élevées qu'aujourd'hui. C'est l'effet Alchian-Allen : quand un coût fixe est ajouté à deux biens de qualité différente, le bien premium devient relativement moins cher, donc la demande se déplace vers lui. À 20 dollars l'heure de H100, il sera extrêmement coûteux et stupide d'utiliser un modèle plus faible et moins efficace, parce qu'il brûlera plus de tokens sur votre compute cher pour obtenir le même résultat. Les labos pourront donc facturer une très grosse prime s'ils entraînent un modèle qui économise mieux cette ressource rare. Si vous devez payer si cher le compute sous-jacent, autant payer un supplément pour utiliser le meilleur modèle, le plus efficace, qui tourne sur cette même quantité de compute.

- **Beaucoup d'applications actuelles de l'IA sont évincées par le prix.** La raison pour laquelle l'IA est relativement bon marché aujourd'hui, au moins comparée au travail humain, est en partie qu'elle ne sait pas faire beaucoup de choses que les meilleurs humains savent faire. À un moment, ce ne sera plus le cas. Utiliser des GPU pour fabriquer de la bouillie vidéo courte sera alors évincé par le prix.
  - Cela dit, ce type de prédiction ressemble aux erreurs passées sur la rareté. Je pense au pari Simon-Ehrlich, où Paul Ehrlich avait parié que le coût d'un panier de matières premières augmenterait plutôt que de diminuer sur la décennie précédant 1990. Ce pari est célèbre parce qu'il est censé illustrer comment la vision malthusienne d'Ehrlich a été falsifiée : il sous-estimait la manière dont les signaux de marché et l'ingéniosité humaine trouvent des moyens de mieux économiser les intrants rares. (Bien que d'autres analyses montrent que si le pari avait été fait sur une autre décennie, Ehrlich aurait gagné.)
  - Je suppose que le panier Simon-Ehrlich n'est pas la bonne classe de référence pour le compute, parce que l'offre de compute est beaucoup moins élastique, et beaucoup moins capable d'absorber de grands chocs de demande, que l'extraction de différents métaux.

### La décomposition du x3

Ce x3 de capacité compute par an provient du produit des facteurs suivants : 1,4x de la loi de Moore, 1,2x de la construction de nouvelles fabs (bridée au moins jusqu'en 2030 par l'offre d'outils EUV), 1,8x du fait que l'IA capte l'allocation de wafers en technologie de pointe au détriment d'autres appareils (ce qui commencera à buter contre un mur d'ici fin 2027, quand l'IA passera de 60 % à 86 % du N3). Il semble difficile de faire beaucoup mieux sur trois de ces intrants, et le dernier butera contre un mur d'ici un ou deux ans, à mesure que l'allocation de wafers sature.

### Nuances finales

Je veux préciser qu'à un certain point dans le futur, le compute redevient bon marché. À un moment, des robots pourront transformer des rivages de silice et des mines de cuivre en ordinateurs. Le prix du compute devrait alors retomber plus près du coût des intrants bruts et des outils. Je ne parle ici que du régime actuel, où le compute IA ne fait que x3 par an, ce qui n'est pas assez rapide pour compenser l'effet prix de l'utilité croissante de l'IA année après année.

Au passage, le fait que les revenus fassent x10 par an alors que le compute ne fait que x3 suggère de très fortes économies d'échelle dans le business des modèles. Logiquement, cela fait sens : quand vous entraînez un modèle, vous payez un coût unique pour apprendre toutes ces compétences, que vous pouvez ensuite amortir sur tous vos utilisateurs. (Contrairement au travail humain, où chaque instance doit être formée depuis zéro.)

J'aimerais que nous ne vivions pas dans un monde avec de si fortes économies d'échelle de l'intelligence, parce que je m'inquiète de la concentration du pouvoir. Mais il semble que ce soit le cas.

*Note : les marges d'inférence mixtes sont supérieures à 70 %, donc je suppose que les marges de l'API Fable sont au-dessus de 80 % — affirmation purement au feeling.*

## Pourquoi ça compte

C'est le cadre économique qui justifie tout le travail d'optimisation côté harness et d'efficacité par tâche : si le compute renchérit d'un ordre de grandeur, le coût par tâche réussie devient la métrique de pilotage, et le choix du modèle se joue sur l'efficacité en tokens plus que sur le score brut.
