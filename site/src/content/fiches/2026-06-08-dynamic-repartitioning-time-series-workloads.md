---
title: "Dynamic Repartitioning for Time Series Workloads"
date: 2026-06-08
url: https://substack.com/redirect/99f59bbe-d256-4545-86a2-1889578e9a8c?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Netflix Technology Blog]
keywords: [Cassandra, wide partitions, time series, repartitionnement, latence]
theme: Data
tone: news
used_in: ["2026-06-08"]
---

## Résumé

L'équipe data de Netflix décrit comment elle a réduit l'impact des *wide partitions* dans son abstraction TimeSeries, bâtie sur Apache Cassandra 4.x pour ingérer et interroger des pétaoctets de données temporelles à latence milliseconde. Quand les partitions deviennent trop larges, les latences de lecture grimpent à plusieurs secondes, provoquant pauses GC, forte utilisation CPU, mises en file des threads et timeouts. Plutôt que de simplement ajouter du matériel, ils ont conçu un système de repartitionnement dynamique qui réajuste la stratégie de partition en fonction de la charge réelle.

## Points clés

- L'abstraction TimeSeries de Netflix sert des pétaoctets d'événements temporels avec une latence en millisecondes, sur Cassandra 4.x (débit, latence, coût, maturité opérationnelle).
- Le défi clé à cette échelle : les wide partitions, qui grossissent à mesure que les événements s'accumulent dans le temps.
- Latence normale : quelques millisecondes ; mais sur certains datasets, les partitions trop larges provoquent des latences en secondes, surtout en queue de distribution.
- Conséquences extrêmes : pauses de garbage collection, forte utilisation CPU, mise en file des threads, timeouts de lecture.
- La stratégie d'origine découpe les données en tranches de temps (time slices, time buckets, event buckets), évitant aussi les tombstones lors des suppressions.
- Le provisioning initial repose sur des inputs utilisateur + simulations Monte Carlo, mais ce dimensionnement statique atteint ses limites quand la charge réelle diverge des prévisions.

## Analyse approfondie

*Par Rajiv Shringi, Kaidan Fullerton, Oleksii Tkachuk et Kartik Sathyanarayanan.*

### Introduction

L'abstraction TimeSeries de Netflix est un système scalable pour ingérer et interroger des pétaoctets de données d'événements temporels avec une latence à la milliseconde. Nous utilisons Apache Cassandra 4.x comme stockage sous-jacent, pour deux raisons principales :

- **Débit, latence et coût** : Cassandra gère des millions de lectures et d'écritures à faible latence de manière économique.
- **Maturité opérationnelle** : notre équipe data possède une expertise opérationnelle profonde dans l'exploitation de grands clusters Cassandra en production.

Cependant, utiliser Cassandra à cette échelle introduit des compromis pour les charges TimeSeries. Un défi clé est celui des *wide partitions* (partitions larges), car les partitions des datasets TimeSeries peuvent devenir très grandes à mesure que les événements s'accumulent. Le problème est aggravé par le fait que les serveurs TimeSeries traitent régulièrement un très fort débit de lecture.

Ce billet retrace notre parcours pour réduire l'impact des wide partitions dans nos datasets TimeSeries, les solutions construites et les leçons apprises.

> Note : bien que ce billet parle de re-partitionnement dans Cassandra, les mêmes techniques s'appliquent plus largement à d'autres systèmes de stockage.

### Impact des wide partitions

Pour la plupart de nos datasets, nous observons une latence de lecture moyenne de l'ordre de quelques millisecondes. Cependant, sur certains datasets, à mesure que les partitions deviennent trop larges, nous observons de hautes latences de lecture de l'ordre de la seconde, surtout en queue de distribution. Cela peut entraîner des timeouts.

Dans les cas extrêmes, si la plupart des lectures ciblent des wide partitions, nous pouvons voir des pauses de garbage collection, une forte utilisation CPU et de la mise en file des threads. Augmenter la taille du cluster Cassandra sous-jacent est toujours une option, mais il nous faut des alternatives plus intelligentes que simplement « jeter plus d'argent au problème ».

### Stratégie de partitionnement TimeSeries

L'abstraction TimeSeries a été conçue pour résoudre le problème des wide partitions en divisant les données en blocs de temps discrets. En résumé, la stratégie découpe un dataset en tranches de temps (time slices), buckets de temps (time buckets) et buckets d'événements (event buckets), brisant les wide partitions en morceaux gérables. Cette stratégie permet aussi d'interroger et de supprimer efficacement les données par le temps, sans avoir à gérer les tombstones.

### Choisir la stratégie de partitionnement

Quand un namespace (c'est-à-dire un dataset) est créé, les utilisateurs doivent spécifier les caractéristiques anticipées de leur charge. Cette spécification alimente notre pipeline de provisioning, qui traite ces inputs, exécute des simulations Monte Carlo et produit une infrastructure et une configuration de partition optimales.

### Le problème de l'approche actuelle

Bien que cette méthode de provisioning soit performante au départ, elle repose sur des prévisions faites au moment de la création. Quand la charge réelle diverge de ces prévisions — volumes plus élevés, motifs d'accès différents, croissance non anticipée —, la configuration statique de partition n'est plus optimale, et les wide partitions réapparaissent. D'où le besoin d'un repartitionnement *dynamique*, capable de réajuster la stratégie au fil du temps plutôt que de figer une décision prise à l'instant zéro.

## Pourquoi ça compte

Illustration parfaite que les décisions de structure (taille et stratégie de partition) ne sont pas des acquis : un dimensionnement optimal à la création se dégrade avec la croissance, et la bonne réponse n'est pas d'ajouter du matériel mais de rendre la structure adaptative.
