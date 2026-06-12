---
title: "Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools"
date: 2026-06-12
url: "https://link.mail.beehiiv.com/ss/c/u001.u7AEjFG7xD7PeXgObD5uIw5ddFRsdrPwRAsyKfCK_wmOr6G9LgJRUJxSwZaF6t2lLGp3c5gO2nw9MIx3JC-vHJ-r5uED0_KUTyN82QOA-qwdTWZSjsnB-v72YmVTK0pAUw_RDSqEWi1PIN7tZ3yT-b5cKyLvJh73P9ML1BF9iOKvphu5AXEaNUUHA7uXyWsX-VrEZEnfhd7WFWUU-j6n9w/4rf/AKVyNDvFSUaVXTyhmC3i1Q/h10/h001.rzLv6EbjBwac7ZWYV5rQILY6CXYSUrfAeH85wIh1rNE"
authors: ["MIT Sloan / Wharton (Mert Demirer, Leon Musolff, Liyuan Yang)"]
keywords: ["productivité IA", "outils de codage IA", "monotonic decay", "Amdahl's Law", "agents asynchrones"]
theme: "IA"
tone: "research"
used_in: ["2026-06-12"]
---

## Résumé

Une étude conjointe MIT/Wharton croise la télémétrie confidentielle de Microsoft avec les données publiques de plus de 100 000 développeurs GitHub pour mesurer l'impact réel des outils d'IA sur la productivité logicielle. Elle classe les outils en trois générations (autocomplétion, agents synchrones, agents asynchrones) et observe que les gains de vélocité au niveau des tâches — spectaculaires — se dissolvent à mesure que le travail monte vers une livraison en production. Les auteurs nomment ce phénomène la « décroissance monotone ».

## Points clés

- L'autocomplétion, les agents synchrones (Claude Code, Cursor) et les agents asynchrones augmentent l'activité de commit de respectivement +40 %, +140 % et +180 %.
- Un gain de +228 % de lignes de code brutes avec l'autocomplétion se réduit à seulement +10 % de releases effectivement livrées.
- La cause : un **Upstream Output Elasticity** de 0,75 — chaque couche de la hiérarchie (lignes → fichiers → commits → PRs → releases) absorbe 25 % du gain précédent via le gatekeeping humain.
- L'élasticité de substitution entre code généré et relecture humaine est de 0,25 — ils sont des compléments forts, pas des substituts (comme un châssis et des pneus).
- Les agents asynchrones court-circuitent les premières couches, doublant l'impact final sur les livraisons par rapport à l'autocomplétion.

## Analyse approfondie

### La hiérarchie de production verticale

Les auteurs structurent la production logicielle comme une chaîne verticale : lignes de code → fichiers → commits → pull requests → repositories → releases. Chaque montée dans la hiérarchie représente un seuil de coordination humaine. L'IA excelle aux couches basses (génération de syntaxe) mais bute sur les couches hautes (revue, intégration, mise en prod).

### Le modèle mathématique

L'**Upstream Output Elasticity** (θ = 0,75) agit comme un multiplicateur compressant : un gain massif au bas de la pile se retrouve multiplié par 0,75 à chaque couche. Sur 5 couches, un gain initial de 741 % (agents sync) donne un gain final de ~20 % en releases. C'est de l'Amdahl's Law appliquée à l'ingénierie logicielle : accélérer la partie déjà rapide (l'écriture) n'accélère pas le goulot d'étranglement (le delivery humain).

### Pourquoi les agents font mieux

Les agents synchrones et asynchrones ne se contentent pas d'écrire des lignes dans un éditeur : ils gèrent directement des fichiers, des commits, des PRs. En injectant leur productivité plus haut dans la hiérarchie, ils évitent une partie du chemin de décroissance. L'impact final sur les releases est ainsi doublé par rapport à l'autocomplétion.

### La limite structurelle

L'**Elasticity of Substitution** (σ = 0,25) signifie que code IA et effort humain de revue sont des compléments forts : accélérer l'un sans accélérer l'autre ne produit pas de gain proportionnel. C'est le défi fondamental : tant que les processus de revue, d'intégration et de déploiement n'accélèrent pas, le goulot se déplace simplement d'un cran vers le haut.

## Pourquoi ça compte

Cette étude offre le premier modèle économique rigoureux de l'impact réel des outils IA sur la productivité logicielle — elle confirme que le goulot d'étranglement n'a jamais été l'écriture du code, et que l'impact mesurable sur la livraison reste bien en deçà des gains annoncés sur les réseaux sociaux.
