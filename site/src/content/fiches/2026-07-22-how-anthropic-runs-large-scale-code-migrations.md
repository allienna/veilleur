---
title: "How Anthropic runs large-scale code migrations with Claude Code"
date: 2026-07-22
url: https://claude.com/blog/ai-code-migration
authors: [claude.com]
keywords: [code migration, Claude Code, judge, test suite, refactoring]
theme: IA
tone: tutorial
used_in: ["2026-07-22"]
---

## Résumé

Anthropic documente sa méthode pour mener des migrations de code à grande échelle avec Claude Code, généralisée en un processus en six étapes. Le prérequis central n'est pas la génération de code mais la mise en place d'un « juge » solide, seule garantie d'une condition de sortie et d'une mesure de succès. Le juge doit pouvoir évaluer l'ancien et le nouveau code à égalité, ce qui suppose de réécrire les tests pour les rendre portables et de le valider sur du code volontairement cassé. La première étape produit un rulebook, une carte de dépendances et un inventaire des trous à combler avant toute traduction.

## Points clés

- Le prérequis absolu d'une migration est un « juge » fiable : sans lui, pas de condition de sortie ni de mesure de succès.
- Le juge doit évaluer l'ancien et le nouveau code sur un pied d'égalité, alors que les tests d'origine dépendent souvent de fonctions internes qui ne se portent pas.
- On valide le juge en le lançant sur du code délibérément cassé : s'il ne détecte pas la casse, ce n'est pas un juge.
- Des agents adverses vérifient que les tests réécrits n'affaiblissent pas les assertions.
- L'étape 1 crée le rulebook, la carte de dépendances et l'inventaire des trous — le rulebook doit précéder l'inventaire.
- Sur un port Python vers TypeScript, l'ingénieur a relancé la migration de bout en bout trois fois, jetant le résultat à chaque tour jusqu'à la troisième passe.

## Analyse approfondie

### Six étapes pour les grandes migrations de code

*Le processus ci-dessous a été généralisé pour rester pertinent sur plusieurs langages et scénarios. Pour plus de détails, on peut lire le blog de Jarred. Un « Migration starter kit » est également disponible. Note : le starter kit est un modèle généralisé du processus — ce n'est pas exactement ce sur quoi ces portages spécifiques ont tourné.*

### Prérequis

Un prérequis avant de démarrer un projet de migration est de disposer d'un juge solide, sans quoi vous n'aurez ni condition de sortie, ni mesure de succès.

Le juge doit pouvoir évaluer à la fois le code d'origine et le code cible sur un pied d'égalité. Les suites de tests écrites dans le langage d'origine dépendent souvent de fonctions internes qui n'existeront pas dans le code cible.

Pour construire ce juge :

- **Catégoriser les tests existants.** Utiliser Claude pour identifier quels tests sont exprimables sous forme d'appels externes et lesquels dépendent d'internes qui ne se porteront pas.
- **Réécrire pour la portabilité.** Convertir les tests orientés externe en assertions capables de tourner à la fois contre l'original et le portage. Utiliser des agents adverses pour vérifier que les tests réécrits n'affaiblissent pas les assertions.
- **Valider le juge.** Le lancer contre le code d'origine pour confirmer qu'il passe. Puis le lancer contre du code délibérément cassé pour confirmer qu'il échoue — un juge qui n'attrape pas la casse n'est pas un juge.

Jarred disposait d'une grande suite de tests écrite dans un troisième langage (TypeScript), mais ce ne sera pas le cas de la plupart des projets. Pour son portage Python vers TypeScript, Mike a créé un « parity harness » de sept scénarios réels et considérait tout changement de comportement comme un bug à corriger.

Avant de détailler chaque étape, un schéma peut aider à suivre. Cela suit essentiellement la méthodologie de Jarred, avec des revues et des gates à chaque étape. Mike a suivi une structure d'ensemble similaire avec des workflows en boucle proches, mais il a mené la migration entière de bout en bout, révisé les règles et le workflow selon les résultats, puis recommencé — jetant la sortie à chaque fois jusqu'à la troisième passe.

### Étape 1 — Créer le rulebook, la carte de dépendances et l'inventaire des trous

Dans cette étape on crée les fondations de la migration : un inventaire des endroits où le code devra être refactorisé plutôt que simplement traduit, un rulebook expliquant comment traduire le code, et une carte de dépendances pour ordonner les chantiers d'implémentation.

L'ordre compte : le rulebook doit venir avant l'inventaire des trous. L'inventaire des trous est défini par ce que le rulebook laisse par défaut [...].

## Pourquoi ça compte

C'est le passage de l'IA-copilote à l'IA-usine : quand un agent peut porter une base de code entière, le vrai savoir-faire d'ingénierie se déplace vers la définition d'un juge fiable et de conditions de sortie mesurables.
