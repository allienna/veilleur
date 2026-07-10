---
title: "Ways to think about token pricing — Benedict Evans"
date: 2026-07-10
url: https://www.ben-evans.com/benedictevans/2026/7/9/ways-to-think-about-token-pricing
authors: [Benedict Evans]
keywords: [token pricing, supply crunch, gross margins, commodity, capex]
theme: Tech
tone: opinion
used_in: ["2026-07-10"]
---

## Résumé

Benedict Evans analyse l'économie du prix des tokens IA. Deux certitudes seulement : on est en pénurie d'offre, et cette situation est instable. La question de fond est de savoir si les labs de modèles conserveront un pouvoir de fixation des prix durable, ou s'ils finiront en fournisseurs d'infrastructure banalisée à faible marge. Evans penche pour la seconde hypothèse : tous les signaux observables y pointent.

## Points clés

- Deux certitudes : pénurie d'offre et instabilité ; toutes les variables (offre, demande, prix, capacité, capex) sont en jeu.
- Côté offre : plus de mille milliards de dollars de capex data center arrivent, l'efficacité d'inférence progresse vite.
- Côté demande : la pénurie de ce semestre est tirée par un seul cas d'usage à fort product-market fit, le développement logiciel, un marché finalement assez petit.
- L'inférence tourne à 40-50 % de marge brute, mais cela n'inclut pas le coût d'entraînement du modèle suivant, aujourd'hui bien supérieur au revenu.
- Trois questions structurantes : combien paieront pour être à la frontière ? la frontière continue-t-elle d'avancer significativement ? la compétition entre modèles frontière restera-t-elle féroce ?

## Analyse approfondie

### Comment penser le prix des tokens

L'IA est aujourd'hui en pénurie d'offre, mais que se passe-t-il quand on en sortira ? Comment et où l'offre, la demande, le prix, la capacité et le capex reviendront-ils à l'équilibre ? Aujourd'hui, les labs de modèles peuvent fixer leur prix, mais pourquoi ne finiraient-ils pas en infrastructure banalisée à faible marge ?

Il n'y a que deux choses que l'on puisse dire avec certitude sur le prix des tokens : nous sommes en pénurie d'offre, et c'est instable. Toutes les variables sont en jeu, et le marché va se décanter au cours des prochaines années pour atteindre un nouvel équilibre. On a beaucoup d'analyses frénétiques sur le "time to power", mais la question qui reste au bout est de savoir si les modèles de fondation ont un pouvoir de fixation des prix durable, un levier stratégique et une capture de valeur — ou s'ils deviennent des fournisseurs d'infrastructure banalisée à faible marge. Pour l'instant, je pense que chaque dynamique observable pointe vers la seconde option.

La situation actuelle est clairement transitoire. Côté offre, mille milliards de dollars ou plus de capex data center arrivent dans le pipe (et bien plus de capex semi-conducteurs derrière), l'efficacité d'inférence continue de s'améliorer très vite, et les nouveaux modèles sont bien plus (ou bien moins !) efficaces dans leur usage des tokens. Côté demande, bien que le marché soit contraint en capacité depuis 2022, la pénurie du premier semestre a été tirée par un product-market fit soudain sur en réalité un seul cas d'usage — le développement logiciel — un champ assez petit finalement (imaginez qu'on ait eu un product-market fit sur un cas d'usage grand public avec des centaines de millions de DAU : l'infrastructure d'aujourd'hui ne pourrait pas le supporter à aucun prix). Nous ne savons pas quels seront les prochains cas d'usage à passer à l'échelle, ni quand, ni quels seront leurs besoins en tokens.

Un cran au-dessus, il est assez largement rapporté que l'inférence a aujourd'hui 40-50 % de marge brute : cela inclut l'amortissement des coûts serveurs associés (ou le coût de leur location), mais on ne connaît pas vraiment la durée de vie des actifs (cinq ans ? sept ans ?), et cela n'inclut évidemment pas le coût d'entraînement du prochain modèle une ou deux fois par an, actuellement bien plus élevé que le revenu. En principe, l'inférence est un coût marginal et l'entraînement un coût fixe, donc avec un revenu suffisamment élevé on peut atteindre la rentabilité — mais on ne sait pas comment les coûts d'entraînement évolueront. De l'autre côté, on ne sait pas quelle part de la montée en usage des derniers mois a un ROI (ou du moins un ROI quantifiable pour un directeur financier), ni quels prix les gens seraient prêts à payer.

Toutes les variables vont donc bouger dans tous les sens sur les douze prochains mois, et rebouger sur trois à cinq ans. Comment suggérer où cela se stabilisera ? On peut tenter une modélisation bottom-up — poser des hypothèses sur chaque variable, estimer les puces disponibles, celles que TSMC et l'industrie peuvent livrer et quand, la vitesse de mise en service en data center et d'alimentation électrique — mais ce serait comme bâtir en 1998 une prévision à cinq ans du marché du haut débit : le tableur sera très joli, on tombera peut-être juste pour cette année, mais il y a trop de variables inconnues pour prédire utilement la structure du marché à long terme.

Autrement dit, on peut dire que le prix du token est une fonction de l'offre et de la demande, à un niveau situé entre le coût marginal des vendeurs et le ROI des acheteurs — mais on ne sait pas ce que seront l'offre, la demande, le coût marginal ou le ROI.

L'autre approche est top-down : comment ce genre de situation tend-il à se dérouler ? Trois questions structurent tout :

- **Premièrement, combien de gens paieront pour être en haut à droite de la courbe — à la frontière ?** Certains cas d'usage fonctionnent déjà très bien avec un petit modèle ancien, éventuellement open source, tournant "gratuitement" sur site ou sur votre téléphone ; à l'autre extrême, certains obtiennent de meilleurs résultats avec le modèle frontière le plus récent et le plus cher. Combien de cas d'usage tirent un meilleur résultat en montant dans la courbe de coût, et combien ont un ROI pour cela ?
- **Deuxièmement, la frontière continue-t-elle d'avancer significativement ?** C'est la question scientifique de base : combien de temps la frontière continue-t-elle de s'améliorer, en nécessitant toujours plus de compute, et à un rythme qui la maintient devant la pression baissière des gains d'efficacité et de capacité ?
- **Troisièmement, la compétition entre modèles frontière restera-t-elle féroce ?** Le champ se réduit-il à quelques modèles avec des effets de réseau ? Les modèles divergent-ils, chacun dominant clairement un domaine ? Ou reste-t-on avec une poignée d'entreprises produisant des modèles frontière globalement équivalents ?

## Pourquoi ça compte

L'essor des agents asynchrones et en flotte n'est économiquement viable que si le coût du token s'effondre. Cette analyse pose le cadre pour comprendre si cet effondrement aura lieu, et pourquoi les labs de modèles risquent de devenir des fournisseurs d'infrastructure banalisée plutôt qu'un oligopole rentable.
