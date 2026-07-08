---
title: "Harness Engineering for Self-Improvement"
date: 2026-07-08
url: https://lilianweng.github.io/posts/2026-07-04-harness/
authors: [Lilian Weng, lilianweng.github.io]
keywords: [harness, recursive self-improvement, agents, orchestration, workflow]
theme: IA
tone: research
used_in: ["2026-07-08"]
---

## Résumé

Lilian Weng explore le concept de *harness engineering* : le système qui entoure le modèle de base et orchestre son exécution — comment il réfléchit et planifie, appelle les outils et agit, perçoit et gère son contexte, stocke des artefacts et évalue ses résultats. Elle défend l'idée que cette couche entre le modèle brut et le monde réel compte autant que l'intelligence brute du modèle, et qu'elle est un moteur clé de l'auto-amélioration récursive (RSI). Les agents de code à succès comme Claude Code et Codex sont, fondamentalement, des harnesses.

## Points clés

- Le concept d'auto-amélioration récursive (RSI) remonte à I. J. Good (1965) et à la formulation de Yudkowsky (2008) : une IA qui utilise son intelligence actuelle pour améliorer la machinerie cognitive qui la produit.
- En IA moderne, la boucle passe surtout par l'amélioration du *pipeline d'entraînement* et du *système de déploiement*, plus que par la réécriture directe des poids.
- Le **harness** = le système qui entoure le modèle : orchestration de l'exécution, réflexion/planification, appel d'outils, perception et gestion du contexte, stockage d'artefacts, évaluation des résultats.
- La couche « système de déploiement » entre le modèle brut et le contexte réel semble aussi importante que l'intelligence brute du modèle.
- Forte analogie avec les systèmes d'exploitation : le harness doit encapsuler la logique complexe tout en gardant une interface simple ; configs, interfaces d'outils et protocoles tendront à se standardiser.
- Pattern 1 — Automatisation de workflow : boucle orientée objectif (planifier, exécuter, observer/tester, améliorer) jusqu'à atteindre le but (ex. le repo autoresearch de Karpathy).

## Analyse approfondie

Le concept d'**auto-amélioration récursive (RSI)** remonte à I. J. Good (1965), qui définissait une « machine ultra-intelligente » comme un système capable de surpasser les humains dans toutes les activités intellectuelles et de concevoir de meilleures machines pour s'améliorer lui-même. Yudkowsky (2008) a utilisé l'expression « auto-amélioration récursive » pour désigner une boucle de rétroaction spécifique : une IA utilise son intelligence actuelle pour améliorer la machinerie cognitive qui produit son intelligence.

Cette boucle de rétroaction, en IA moderne, peut désigner un modèle réécrivant directement ses propres poids, mais plus largement un modèle qui améliore son *pipeline d'entraînement* et son *système de déploiement*, ce qui permet en retour un meilleur modèle successeur avec de meilleures performances sur des tâches à forte valeur économique. La vitesse de la R&D en IA s'est montrée drastiquement accélérée dans les labos frontier (Anthropic, OpenAI).

Je mentionne explicitement la couche « système de déploiement » entre le modèle brut et le contexte réel car elle semble aussi importante que l'intelligence brute du modèle (c'est-à-dire les évals, le bon pré-entraînement). Les harnesses sont des composants importants du déploiement de l'IA, comme le montrent des produits d'agents de code à succès comme Claude Code et Codex.

Un **harness** est le système qui entoure le modèle de base et orchestre son exécution : il décide comment le modèle réfléchit et planifie, appelle les outils et agit, perçoit et gère le contexte, stocke les artefacts, et évalue les résultats. Ce post se concentrera sur la recherche autour du harness engineering et sur la façon dont il contribue au RSI. Une grande partie des travaux récents sur l'auto-recherche, le self-play auto-améliorant et le RSI au test-time se rapproche du design de systèmes logiciels à l'exécution : comment le modèle observe, agit, mémorise, se vérifie et s'améliore.

Le design devrait être délibérément simple et générique pour permettre la généralisation, en s'appuyant vraisemblablement sur les pratiques existantes de génie logiciel pour tirer parti des connaissances de pré-entraînement. Il y a aussi une forte analogie entre systèmes d'exploitation et harnesses. Comme un OS, un harness devrait encapsuler une logique compliquée tout en gardant une interface simple. Entre-temps, les configs, interfaces d'outils et autres protocoles pourraient progressivement se standardiser à travers l'industrie.

**Pattern 1 : Automatisation de workflow.** Définir un workflow dans lequel le modèle peut opérer, tester et itérer est une clé de l'automatisation du design. Le repo autoresearch de Karpathy est un exemple propre de la façon dont un workflow peut être construit. Un workflow courant suit une boucle orientée objectif — planifier, exécuter, observer/tester, améliorer, exécuter de nouveau — *jusqu'à* ce que l'objectif soit atteint. Le processus peut déclencher des requêtes proactives vers les utilisateurs pour clarifier la spécification de la tâche ou les préférences d'exécution. (Illustration : la boucle d'agent simplifiée de Codex, où l'agent appelle des outils et où les réponses des outils affectent la génération suivante du modèle.)

## Pourquoi ça compte

Une grille de lecture précieuse pour tout GenAI Architect : la performance d'un produit d'IA ne se joue pas qu'au niveau du modèle, mais dans l'ingénierie du harness qui l'entoure — orchestration, mémoire, outils et évaluation.
