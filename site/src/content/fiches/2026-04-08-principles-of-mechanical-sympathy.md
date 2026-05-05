---
title: "Principles of Mechanical Sympathy"
date: 2026-04-08
url: "https://martinfowler.com/articles/mechanical-sympathy-principles.html"
authors: ["Martin Fowler"]
keywords: [mechanical sympathy, performance, hardware, abstraction, optimisation]
theme: "Tech"
tone: "tutorial"
used_in: ["2026-04-08"]
---

## Résumé

Martin Fowler revient sur le concept de "mechanical sympathy" — comprendre le fonctionnement du hardware sous-jacent pour écrire du logiciel performant. L'article pose des principes fondamentaux pour naviguer entre abstraction et performance, un rappel pertinent à l'ère où l'IA pousse vers toujours plus d'abstraction.

## Points clés

- La "mechanical sympathy" vient de la course automobile : piloter en comprenant la mécanique du véhicule
- Appliquée au logiciel : écrire du code qui travaille *avec* le hardware, pas contre lui (cache lines, mémoire, I/O)
- Les abstractions sont nécessaires mais ont un coût — le développeur doit savoir quand les traverser
- Fowler identifie des principes pratiques : localité des données, prédictibilité des accès mémoire, compréhension du modèle de coûts
- Le concept est d'autant plus pertinent que l'IA génère du code sans conscience du hardware

## Analyse approfondie

### Un concept plus pertinent que jamais

Le terme "mechanical sympathy" a été popularisé dans le monde du développement par Martin Thompson (créateur du LMAX Disruptor). Fowler le reprend et le systématise en principes applicables. Dans un contexte où l'IA génère de plus en plus de code, la compréhension du hardware devient un différenciateur — l'IA produit du code fonctionnel, mais rarement du code qui exploite les caractéristiques du hardware.

### Principes fondamentaux

Fowler structure sa réflexion autour de plusieurs axes : la localité des données (structurer les données pour que les accès séquentiels soient contigus en mémoire), la prédictibilité (permettre au CPU de pré-charger les données via le branch prediction), et le modèle de coûts (savoir que lire en L1 cache prend 1 ns, en RAM 100 ns, sur SSD 100 μs, sur réseau 1 ms change fondamentalement la façon de concevoir un système).

### L'ironie de l'abstraction IA

Il y a une ironie dans le fait que cet article paraisse au moment où l'IA pousse l'industrie vers plus d'abstraction. Les agents de code assemblent des composants sans se soucier de la mémoire ou du cache. Fowler rappelle que les abstractions fuient toujours ("leaky abstractions") et que la connaissance du niveau en dessous reste indispensable pour diagnostiquer les problèmes de performance.

## Pourquoi ça compte

À l'ère de l'IA et de l'abstraction maximale, ce rappel aux fondamentaux de la performance hardware est un contrepoint bienvenu. Les développeurs qui comprennent le hardware sous leurs abstractions seront ceux qui résoudront les problèmes que les agents de code ne sauront pas diagnostiquer.
