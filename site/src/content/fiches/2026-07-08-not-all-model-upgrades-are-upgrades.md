---
title: "Not all model upgrades are upgrades"
date: 2026-07-08
url: https://developer.microsoft.com/blog/not-all-model-upgrades-are-upgrades
authors: [Waldek Mastykarz, developer.microsoft.com]
keywords: [coût par token, consommation de tokens, évaluation, Sonnet 5, benchmark]
theme: IA
tone: research
used_in: ["2026-07-08"]
---

## Résumé

Un nouveau modèle sort avec un prix par token plus bas et de meilleurs benchmarks, on bascule dessus — et une semaine plus tard, l'agent brûle 12 fois plus de tokens pour un résultat parfois pire. Waldek Mastykarz (Microsoft) montre, benchmarks à l'appui, que la grille tarifaire ne détermine pas la facture : c'est la consommation de tokens qui le fait. Sur des tâches d'architecture, Sonnet 5 a consommé jusqu'à 12x plus de tokens que Sonnet 4.6 en médiane, et produit une qualité moindre. La conclusion : on ne connaît la direction que prend un « upgrade » qu'après l'avoir mesuré sur ses propres charges.

## Points clés

- Sonnet 5 est moins cher par token que Sonnet 4.6 sur toute la grille (input 2 $ vs 3 $, output 10 $ vs 15 $ par million).
- Mais sur 12 scénarios d'architecture (60 runs/modèle), Sonnet 5 a consommé 12x plus de tokens en médiane, avec un run à 47x.
- Sur les tâches d'upgrade de code, Sonnet 5 coûte 2,01 $/run contre 0,55 $ — soit 3,7x plus cher malgré une remise de 33 % par token.
- Qualité en baisse : sur le critère « idiomatique », 90 % pour Sonnet 4.6 contre 78 % pour Sonnet 5 ; l'ancien modèle égale ou dépasse le nouveau sur 8 scénarios sur 9.
- Contre-exemple : sur les migrations SPFx, Sonnet 5 passe le Select gate à 100 % contre 60 % pour 4.6 — donc tout dépend de la tâche, d'où l'impératif de mesurer.

## Analyse approfondie

Un nouveau modèle sort avec un prix par token plus bas et de meilleurs benchmarks. Vous basculez. Une semaine plus tard, quelqu'un demande pourquoi l'agent brûle 12 fois plus de tokens sur la même tâche tout en produisant un résultat de moins bonne qualité.

**Des tokens moins chers, des factures plus élevées.** Sonnet 5 est moins cher par token sur toute la ligne. Voici la comparaison des grilles tarifaires :

| | Sonnet 4.6 | Sonnet 5 |
| --- | --- | --- |
| Input (par 1M de tokens) | 3,00 $ | 2,00 $ |
| Input en cache | 0,30 $ | 0,20 $ |
| Output | 15,00 $ | 10,00 $ |

Dans une telle comparaison, Sonnet 5 gagne à chaque ligne. Mais les grilles tarifaires ne déterminent pas votre facture : la consommation de tokens le fait, et Sonnet 5 consomme sensiblement plus de tokens.

Sur des tâches d'architecture (12 scénarios, 60 runs par modèle), Sonnet 5 a utilisé 12x plus de tokens en médiane. Un scénario a vu un seul run consommer 47x le volume habituel. Sur les upgrades de code (3 scénarios, 15 runs par modèle), l'écart atteint 10x. Une remise de 33 % par token ne survit pas à ce type d'augmentation.

Ce que ça vous coûte en dollars dépend de la tâche. Sur les upgrades de code, Sonnet 5 revient à 2,01 $ par run contre 0,55 $ pour Sonnet 4.6, ce qui rend le modèle « moins cher » 3,7x plus coûteux. Sur les tâches d'architecture, l'histoire s'inverse : Sonnet 5 a coûté en moyenne 0,47 $ par run contre 0,54 $, ce qui le rend 12 % moins cher là où l'augmentation de tokens est assez modérée pour que la remise l'emporte. **Vous ne saurez pas dans quelle direction va votre charge de travail tant que vous ne l'aurez pas mesurée.**

**La qualité ne s'est pas améliorée non plus.** Le modèle plus récent peut coûter plus cher ou moins cher, selon la tâche. Produit-il au moins un meilleur résultat ? Sur le travail d'architecture, d'après nos évaluations, non. Les deux modèles ont accompli la tâche au même taux, 75 % sur notre porte « Select » (l'agent a-t-il seulement tenté la bonne tâche ?). C'est sur la qualité du résultat qu'ils diffèrent. Sur les 9 scénarios où les deux produisaient un résultat utilisable, Sonnet 4.6 a obtenu 90 % sur notre dimension « Idiomatique » (le résultat suit-il les patterns et conventions établis ?) contre 78 % pour Sonnet 5. L'ancien modèle a surpassé ou égalé la qualité sur 8 scénarios sur 9. Sur un scénario, la conception d'une architecture d'analytics IoT, Sonnet 4.6 a réussi sur 4 runs sur 5. Sonnet 5 en a réussi 1. Même prompt, résultat mesurablement pire. Plus de tokens et une qualité moindre sur la majorité des scénarios. L'« upgrade » est parti dans le mauvais sens.

**Quand un upgrade compte vraiment.** Les tâches d'upgrade de code renversent le tableau. Nous avons testé trois scénarios de mise à jour de projets SharePoint Framework (SPFx), dont une migration gulp-vers-Heft et une migration de config ESLint legacy-vers-flat. Sonnet 4.6 a passé la porte Select sur 60 % des runs. Sonnet 5 a passé 100 %. L'exemple le plus net est la mise à jour de SPFx v1.21.1 vers v1.22.0, que Sonnet 4.6 échouait.

## Pourquoi ça compte

C'est un rappel salutaire pour toute équipe qui pilote ses coûts IA : le prix affiché par token est un leurre, seule l'évaluation sur ses propres charges dit la vérité. Un réflexe FinOps indispensable à l'ère des agents.
