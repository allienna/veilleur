---
title: "Xiaomi's new open source, agentic AI coding harness MiMo Code beats Claude Code at ultra-long, 200+ step tasks"
date: 2026-06-12
url: "https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks"
authors: ["VentureBeat"]
keywords: ["MiMo Code", "mémoire persistante", "agents long-horizon", "SQLite FTS5", "open source"]
theme: "IA"
tone: "news"
used_in: ["2026-06-12"]
---

## Résumé

Xiaomi open-source MiMo Code V0.1.0, un agent de codage terminal-native qui surpasse Claude Code sur les tâches longues de plus de 200 étapes, selon les propres benchmarks de Xiaomi sur 576 développeurs. La clé : une architecture mémoire cross-session à quatre couches (mémoire projet, checkpoints de session, notes scratch, logs de progression) gérée par un sous-agent dédié à l'écriture de checkpoints. Disponible sous licence MIT.

## Points clés

- Fork d'OpenCode (projet open source), étendu avec une architecture mémoire propre à Xiaomi.
- La mémoire est structurée en 4 couches : fichier `MEMORY.md` persistant, checkpoints de session, notes scratch, logs de tâche.
- Un sous-agent indépendant ("checkpoint-writer") gère l'écriture des checkpoints pendant que l'agent principal code — sans interrompre son flux.
- Le moteur de recherche mémoire est SQLite FTS5 (full-text search) pour des rappels rapides.
- Accès gratuit limité au modèle MiMo-V2.5 (fenêtre de contexte 1M tokens), sans inscription requise.

## Analyse approfondie

### Le problème que MiMo Code résout

Les agents de codage IA dégradent sur les longues sessions : à mesure que la fenêtre de contexte se remplit, les décisions antérieures, les conventions et l'état des tâches se compriment ou disparaissent. Les développeurs sont contraints de ré-expliquer leur projet à l'agent. Xiaomi considère que la compression de contexte est une impasse : ce qu'il faut, c'est un mécanisme explicite de stockage et de rappel.

### L'architecture mémoire à 4 couches

**Couche 1 — MEMORY.md** : un fichier persistant qui contient les informations clés du projet (conventions, architecture, décisions importantes). Il survit entre les sessions.

**Couche 2 — Checkpoints de session** : des snapshots de l'état courant de la tâche, écrits à intervalles réguliers par le sous-agent dédié.

**Couche 3 — Notes scratch** : des notes temporaires que l'agent principal peut consulter rapidement pendant son travail.

**Couche 4 — Logs de progression par tâche** : un suivi de l'avancement qui permet à l'agent de savoir où il en est sans tout relire depuis le début.

### Le sous-agent checkpoint-writer

L'innovation architecturale clé est la séparation des responsabilités : l'agent principal code sans interruption, pendant qu'un sous-agent dédié observe et écrit les checkpoints. C'est l'équivalent d'un architecte qui prend des notes pendant qu'un entrepreneur construit — sans demander à l'entrepreneur d'arrêter. Cette séparation évite le coût cognitif de la prise de notes inline.

### Positionnement compétitif

MiMo Code se positionne directement contre Claude Code sur le segment des tâches longues. Les benchmarks internes montrent des gains significatifs sur les tâches dépassant 200 étapes. Cependant, les benchmarks sont auto-déclarés et réalisés sur un échantillon de 576 développeurs — à prendre avec les précautions habituelles.

## Pourquoi ça compte

MiMo Code incarne une thèse architecturale concrète : la mémoire persistante et structurée est la prochaine frontière des agents de codage, plus que la taille du contexte ou la qualité du modèle seuls. Si cette approche s'avère généralisable, elle pourrait redéfinir comment tous les agents de codage gèrent les tâches de longue durée.
