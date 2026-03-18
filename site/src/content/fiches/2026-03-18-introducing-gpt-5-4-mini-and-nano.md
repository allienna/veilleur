---
title: "Introducing GPT-5.4 mini and nano"
date: 2026-03-18
url: https://links.tldrnewsletter.com/kHfx4k
authors: [OpenAI]
keywords: [GPT-5.4, mini, nano, inférence, benchmarks]
theme: IA
tone: news
used_in: ["2026-03-18"]
---

## Résumé

OpenAI lance GPT-5.4 mini et nano, deux nouveaux modèles optimisés pour la vitesse et le coût. GPT-5.4 mini est deux fois plus rapide que GPT-5 mini tout en approchant les performances de GPT-5.4 sur plusieurs benchmarks, avec 54,4 % sur SWE-Bench Pro. GPT-5.4 nano est le plus petit et le moins cher de la gamme, conçu pour les tâches de classification, extraction et ranking dans les workloads sensibles à la latence.

## Points clés

- GPT-5.4 mini est 2x plus rapide que GPT-5 mini et approche GPT-5.4 sur plusieurs évaluations
- Score de 54,4 % sur SWE-Bench Pro, un benchmark exigeant de résolution de problèmes logiciels réels
- GPT-5.4 nano est le modèle le plus petit et le moins cher de la gamme OpenAI
- Nano est conçu pour les tâches de classification, extraction et ranking — pas pour la génération longue
- Les deux modèles ciblent les workloads sensibles à la latence où chaque milliseconde compte

## Analyse approfondie

OpenAI présente deux nouveaux ajouts à la famille GPT-5.4 : mini et nano, conçus pour offrir les capacités de la génération GPT-5.4 dans des formats plus rapides et plus économiques.

### GPT-5.4 mini

GPT-5.4 mini est le successeur de GPT-5 mini. Il est deux fois plus rapide que son prédécesseur tout en offrant des performances significativement améliorées sur l'ensemble des benchmarks. Sur plusieurs évaluations, mini approche les résultats de GPT-5.4 complet, ce qui en fait un choix attractif pour les cas d'usage où le rapport performance/coût est déterminant.

Le modèle atteint 54,4 % sur SWE-Bench Pro, un benchmark qui mesure la capacité d'un modèle à résoudre des problèmes logiciels réels issus de dépôts open source. Ce score démontre que mini n'est pas un simple modèle "léger" — il est capable de raisonnement technique substantiel.

Mini est conçu pour les applications en production qui nécessitent des réponses rapides sans sacrifier la qualité : chatbots, assistants de codage, pipelines d'analyse en temps réel.

### GPT-5.4 nano

Nano est le plus petit modèle jamais proposé par OpenAI. Il occupe un créneau spécifique : les tâches où la latence et le coût sont les contraintes dominantes, et où la génération longue n'est pas nécessaire.

Les cas d'usage cibles incluent :

- **Classification** : catégorisation de textes, détection de sentiment, routage de requêtes
- **Extraction** : parsing structuré de données depuis du texte libre
- **Ranking** : tri et priorisation d'éléments selon des critères définis

Nano n'est pas destiné à remplacer les modèles plus grands pour des tâches complexes de raisonnement ou de génération. Il est conçu comme une brique d'infrastructure, optimisée pour être appelée des millions de fois par jour dans des pipelines automatisés.

### Positionnement dans la gamme

La famille GPT-5.4 se décline désormais en trois tailles : le modèle complet pour les tâches les plus exigeantes, mini pour le meilleur rapport qualité/vitesse, et nano pour le volume et la latence minimale. Cette stratification permet aux développeurs de choisir le bon modèle pour chaque étape de leur pipeline, plutôt que d'utiliser un modèle surdimensionné partout.

## Pourquoi ça compte

L'arrivée de mini et nano confirme la tendance de fond : la compétition se joue désormais autant sur l'efficience que sur la performance brute. Pour les équipes en production, pouvoir choisir le bon modèle pour chaque tâche change l'économie des applications IA.
