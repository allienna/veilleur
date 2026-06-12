---
title: "Software Is Made Between Commits - Zed Blog"
date: 2026-06-12
url: "https://zed.dev/blog/introducing-deltadb"
authors: ["Zed Industries"]
keywords: ["DeltaDB", "version control", "agents IA", "collaboration", "worktree"]
theme: "Tech"
tone: "opinion"
used_in: ["2026-06-12"]
---

## Résumé

L'équipe de Zed annonce DeltaDB, un nouveau système de contrôle de version conçu pour capturer non plus des snapshots (commits) mais le flux continu de deltas — chaque opération entre les commits. Le constat central : quand humains et agents éditent le même worktree en continu, c'est la conversation qui génère le code qui devient la vraie source du logiciel, et Git n'a jamais été conçu pour ça.

## Points clés

- Git capture des snapshots discrets ; DeltaDB capture chaque opération avec une identité stable, permettant de référencer n'importe quel moment de l'évolution du code.
- Les messages et les édits qu'ils produisent sont enregistrés côte à côte — ni l'un ni l'autre ne dérive de l'autre.
- DeltaDB utilise des CRDT (Conflict-free Replicated Data Types) pour permettre à plusieurs humains et agents d'éditer simultanément les mêmes fichiers sur différentes machines.
- Les références aux lignes de code survivent aux modifications parce qu'elles sont ancrées à un delta, pas à un numéro de ligne.
- Beta disponible dans quelques semaines.

## Analyse approfondie

### Le problème que Git ne résout pas

Git a été conçu autour d'un modèle de collaboration asynchrone : je travaille de mon côté, tu travailles du tien, on se synchronise via des commits puis des merges. Ce modèle supposait que l'unité de travail était le commit — un moment intentionnel de capture. Dans ce modèle, tout ce qui se passe *entre* les commits est invisible et éphémère.

Avec les agents IA, cette invisibilité devient un problème. Un agent peut effectuer des centaines d'opérations entre deux commits. La conversation qui a guidé ces opérations — les prompts, les décisions, les corrections — est perdue. Si un bug est introduit, il est difficile de reconstituer le raisonnement qui y a conduit.

### L'abstraction centrale : le delta

DeltaDB remplace le commit comme unité atomique par le delta — chaque opération élémentaire sur le code. Chaque delta a une identité stable. On peut référencer l'état du code à n'importe quel point dans son évolution, pas seulement aux commits. Cela permet de lier une ligne de code spécifique à la conversation qui l'a produite, même si cette ligne a bougé depuis.

### CRDT pour la collaboration multi-agents

Les worktrees DeltaDB reposent sur des CRDT, ce qui permet à plusieurs agents et humains d'éditer simultanément les mêmes fichiers sans conflits destructeurs. Les fichiers restent des fichiers réels sur disque — les outils existants (terminal, IDE, compilateurs) fonctionnent sans modification. On peut monter le worktree à n'importe quel moment.

### La thèse philosophique

> Increasingly, the conversation that generates the code is becoming the true source of our software.

Zed pousse une idée forte : si la conversation est le vrai code source, alors nos outils de versioning doivent capturer la conversation, pas seulement ses artefacts. DeltaDB est une tentative de répondre à cette réalité plutôt que de l'ignorer.

## Pourquoi ça compte

DeltaDB représente l'une des premières tentatives sérieuses de repenser le contrôle de version à l'ère des agents — une infrastructure qui pourrait devenir aussi fondamentale que Git l'est aujourd'hui si l'édition multi-agents en temps réel devient la norme.
