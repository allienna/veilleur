---
title: "GitHub - superradcompany/microsandbox: 🧱 local-first and microVM-backed sandboxes for AI agents"
date: 2026-06-09
url: https://github.com/superradcompany/microsandbox
authors: [superradcompany]
keywords: [sandbox, microVM, AI agents, local-first, isolation, SDK]
theme: IA
tone: news
used_in: ["2026-06-09"]
---

## Résumé

Microsandbox est un projet open source (licence Apache 2.0) qui permet de lancer des micro-VM légères en quelques millisecondes directement depuis des SDK. Tout tourne en local sur la machine du développeur : pas de serveur à configurer, pas de démon résident, tout est embarqué et rootless. Son ambition affichée : « le moyen le plus simple de donner à un agent son propre ordinateur ». Des SDK sont fournis pour Rust, Python, TypeScript et Go.

## Points clés

- Lance des micro-VM légères en quelques millisecondes depuis un SDK.
- Tourne en local : pas de serveur, pas de démon résident, embarqué et rootless.
- SDK disponibles en Rust, Python, TypeScript et Go.
- Positionnement : « donner à ton agent son propre ordinateur » de la façon la plus simple.
- Licence Apache 2.0, communauté Discord active, releases publiques.
- Brique d'isolation d'exécution pour le code généré par les agents IA.

## Analyse approfondie

**Microsandbox — le moyen le plus simple de donner à ton agent son propre ordinateur.**

Microsandbox fait apparaître des **VM légères en quelques millisecondes** à partir de ses SDK. Le tout tourne **localement** sur la machine de l'utilisateur. Il n'y a aucun serveur à mettre en place, aucun démon qui traîne en arrière-plan : tout est embarqué et **rootless** (sans privilèges root).

Installation du SDK selon le langage :

- `cargo add microsandbox` — 🦀 Rust
- `uv add microsandbox` — 🐍 Python
- `npm i microsandbox` — 🟦 TypeScript
- `go get github.com/superradcompany/microsandbox/sdk/go` — 🐹 Go

Le projet est distribué sous **licence Apache 2.0**, avec des releases publiques (y compris des préversions) et une communauté sur Discord.

Le positionnement est clair : à l'heure où les agents IA génèrent et exécutent du code de façon autonome, il faut un environnement d'exécution **isolé**, rapide et sûr. Les micro-VM apportent une isolation forte (frontière matérielle, contrairement à un simple conteneur), tout en restant assez légères pour démarrer en millisecondes — un compromis crucial pour des agents qui peuvent lancer de nombreuses exécutions éphémères. Le caractère local-first et rootless réduit la surface d'attaque et évite la dépendance à une infrastructure cloud, ce qui en fait une brique adaptée aux postes de développeurs comme aux pipelines agentiques.

## Pourquoi ça compte

Faire tourner du code généré par une IA sans risque exige une isolation forte et instantanée. Microsandbox incarne la couche « exécution sûre » de l'infrastructure agentique qui se construit actuellement en open source, en parallèle des outils de review et d'orchestration.
