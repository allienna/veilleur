---
title: "Entire Claude Code CLI source code leaks thanks to exposed map file"
date: 2026-04-01
url: "https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/"
authors: ["Ars Technica"]
keywords: [Claude Code, fuite de code, source map, Anthropic, sécurité]
theme: "IA"
tone: "news"
used_in: ["2026-04-01"]
---

## Résumé

Le code source complet de Claude Code, l'outil CLI d'Anthropic pour le développement assisté par IA, a fuité suite à l'exposition d'un fichier source map dans le package npm distribué publiquement. La fuite révèle l'architecture interne détaillée de l'outil, confirmant que sa force repose davantage sur l'ingénierie du "harnais" que sur le modèle lui-même.

## Points clés

- Un fichier source map exposé dans le package npm a permis de reconstruire l'intégralité du code TypeScript original
- Claude Code utilise des outils dédiés (Grep, Glob, LSP) plutôt que de simples appels shell pour optimiser les permissions et la collecte de résultats
- Le système inclut une déduplication des lectures de fichiers et une autocompaction des contextes trop longs
- La fuite confirme l'investissement massif d'Anthropic dans l'ingénierie d'orchestration autour du modèle
- Anthropic a réagi en retirant le source map des distributions ultérieures

## Analyse approfondie

Le code source complet de l'outil en ligne de commande Claude Code d'Anthropic a fuité publiquement après qu'un fichier source map a été découvert dans le package npm distribué. Les fichiers source map sont des fichiers de débogage qui permettent de reconstruire le code source original à partir du JavaScript minifié — ils n'auraient jamais dû être inclus dans la distribution de production.

La fuite a été rapidement repérée par la communauté de développeurs, et des copies du code TypeScript reconstitué ont commencé à circuler sur GitHub. Le code révèle l'architecture interne complète de Claude Code : comment l'outil gère le contexte des conversations, comment il interagit avec le système de fichiers local, comment il orchestre les appels au modèle, et quels garde-fous sont en place.

Parmi les détails techniques notables : Claude Code charge le contexte git (branche principale, branche courante, commits récents) et les fichiers CLAUDE.md au démarrage. Il utilise des marqueurs de frontière pour séparer le contenu statique du contenu dynamique, permettant un cache global des parties statiques pour éviter de les retraiter à chaque interaction. L'outil dispose de ses propres outils dédiés pour la recherche de fichiers (Glob), la recherche de contenu (Grep), et l'analyse de code (LSP — Language Server Protocol), plutôt que de passer par le shell.

La gestion du contexte limité est un aspect central de l'architecture. Le système effectue une déduplication des lectures de fichiers en vérifiant si un fichier a changé avant de le retraiter. Quand les résultats d'outils sont trop volumineux, ils sont écrits sur disque avec seulement un aperçu et une référence de fichier conservés dans le contexte. Un mécanisme d'autocompaction et de résumé intervient quand le contexte devient trop long.

Claude Code maintient également un fichier markdown structuré pour chaque conversation avec des sections dédiées : titre de session, état courant, spécification de tâche, fichiers et fonctions, workflow, erreurs et corrections. Cette structure permet au modèle de maintenir une cohérence sur de longues sessions de travail.

Anthropic n'a pas commenté publiquement la fuite au-delà du retrait du source map des distributions suivantes du package npm.

## Pourquoi ça compte

Cette fuite est paradoxalement une des meilleures démonstrations de la thèse "le harnais compte plus que le modèle" — le code révèle un investissement considérable dans l'ingénierie d'orchestration, la gestion de contexte et les outils spécialisés, confirmant que la différence entre un chatbot et un agent de code productif réside dans l'infrastructure qui entoure le modèle.
