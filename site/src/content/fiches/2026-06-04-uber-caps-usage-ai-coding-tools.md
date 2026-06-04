---
title: "Uber Caps Usage of AI Tools Like Claude Code to Manage Costs"
date: 2026-06-04
url: https://simonwillison.net/2026/Jun/3/uber-caps-usage/
authors: [Simon Willison]
keywords: [coût IA, plafond budget, Claude Code, Cursor, tokenmaxxing]
theme: Leadership
tone: opinion
used_in: ["2026-06-04"]
---

## Résumé

Simon Willison commente une information rapportée par Natalie Lung pour Bloomberg : Uber plafonne désormais la consommation de ses ingénieurs à 1 500 $ de tokens par mois et par outil de code agentique (Cursor, Claude Code). La mesure fait suite au constat qu'Uber avait brûlé son budget IA annuel 2026 en quatre mois. Willison juge la politique rationnelle et bien plus saine que les leaderboards de « tokenmaxxing » qui poussaient les employés à consommer toujours plus. Il en tire surtout un signal sur la valeur réelle que ces outils représentent pour l'entreprise.

## Points clés

- Plafond de 1 500 $/mois **par outil** : la dépense sur un outil n'affecte pas le budget d'un autre.
- Les limites ne s'appliquent qu'au code agentique (Cursor, Claude Code), pas aux autres usages IA.
- En supposant deux outils actifs par ingénieur : 3 000 $ × 12 = 36 000 $/an de plafond par dev.
- Levels.fyi situe le package médian d'un ingénieur Uber aux US à 330 000 $ — le plafond IA représente donc ~11 % de la rémunération médiane.
- Uber avait épuisé son budget IA 2026 en quatre mois, budget probablement fixé en 2025 avant l'explosion des agents de code.
- Les plans individuels subventionnés (≈100 $/mois pour ~1 000 $ de tokens) ne sont plus accessibles aux grandes entreprises comme Uber.

## Analyse approfondie

Willison renvoie d'abord à un billet précédent où il notait qu'Uber avait cramé son budget IA 2026 en quatre mois — un résultat peu surprenant à ses yeux, puisque ce budget aurait été défini en 2025, avant que quiconque puisse prédire à quel point les agents de code dévoreurs de tokens allaient devenir populaires.

Il cite ensuite Natalie Lung pour Bloomberg : « Le géant du VTC limite tous ses employés à 1 500 $ de dépense mensuelle en tokens par outil de code IA, a déclaré un porte-parole d'Uber en réponse à une demande de Bloomberg News. Cela signifie que la dépense sur un outil n'a pas d'incidence sur le budget d'un autre. Les limites, instituées ces derniers mois, ne s'appliquent qu'aux logiciels de code agentique tels que Cursor ou Claude Code d'Anthropic PBC. »

Pour Willison, un plafond mensuel de 1 500 $ par outil constitue une réponse politique rationnelle à une sur-dépense, et bien plus sensée que ces leaderboards de *tokenmaxxing* qui encouragent les employés à se concurrencer pour consommer le plus d'IA possible.

Il y voit surtout un indice intéressant : un ordre de grandeur de la valeur réelle qu'Uber retire de ces outils. En supposant deux outils activement utilisés par ingénieur, on obtient 3 000 $ × 12 = 36 000 $ de plafond par ingénieur et par an. Or Levels.fyi liste le package de rémunération annuel médian des ingénieurs logiciels d'Uber aux États-Unis à 330 000 $. Le plafond de dépense IA de chaque employé équivaut donc à environ 11 % de cette rémunération médiane.

Willison ajoute une note personnelle : sa propre consommation de tokens tourne autour de 1 000 $/mois chez Anthropic comme chez OpenAI — mais ne lui coûte aujourd'hui que 100 $ par fournisseur grâce aux plans individuels généreusement subventionnés. Ces plans ne sont plus disponibles pour des entreprises de la taille d'Uber. Conséquence : s'il travaillait chez Uber, avec ses habitudes actuelles, il lui resterait encore ~500 $/mois de tokens à dépenser pour chacun de ces outils.

## Pourquoi ça compte

Premier chiffre public concret mettant un prix sur l'IA de code en entreprise : il transforme un débat abstrait sur les coûts en une ligne budgétaire arbitrée, à hauteur de ~11 % du package d'un ingénieur. Le signal que la phase de subvention illimitée se referme.
