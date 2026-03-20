---
title: "Writing my first evals"
date: 2026-03-20
url: https://nicknisi.com/posts/writing-my-first-evals/
authors: ["Nick Nisi"]
keywords: [evals, LLM, Claude, agent SDK, qualité]
theme: IA
tone: tutorial
used_in: ["2026-03-20"]
---

## Résumé

Nick Nisi raconte comment il a construit ses premiers systèmes d'évaluation pour deux outils de développement alimentés par l'IA chez WorkOS. Face au caractère non-déterministe des sorties des LLM, il a abandonné les tests classiques au profit d'évaluations basées sur des fixtures et des juges LLM. L'article détaille les architectures d'éval pour un CLI d'installation automatique et un générateur de contexte agent, et tire une leçon transversale : définir ce que "bon" signifie avant de commencer à mesurer.

## Points clés

- Les tests classiques (`expect(output).toBe(expected)`) ne fonctionnent pas pour les sorties non-déterministes des LLM
- Le CLI `workos install` utilise le Claude Agent SDK pour installer AuthKit automatiquement dans 16 frameworks différents
- Le système d'éval repose sur des fixtures : des applications minimales dans différents états de départ (vierge, Auth0 existant, middleware conflictuel)
- Les évaluateurs LLM (Claude comme juge) permettent de noter la qualité sémantique sur une échelle standardisée de 0 à 4
- Les evals ne sont pas des tests : ce sont des instruments de mesure qui acceptent la variance pour capturer des tendances
- La leçon clé : définir ce que "bon" signifie avant de mesurer, pas après

## Analyse approfondie

### Le problème de départ

L'auteur a construit deux outils de développement alimentés par l'IA chez WorkOS et avait besoin de vérifier s'ils fonctionnaient réellement. Le premier outil est `workos install`, une commande CLI construite avec le Claude Agent SDK qui installe automatiquement WorkOS AuthKit dans des projets existants, et ce pour 16 frameworks différents. Le second est WorkOS Skills, un système qui génère automatiquement du contexte agent à partir de la documentation.

Le problème fondamental : la sortie d'une IA est non-déterministe. On ne peut pas écrire `expect(output).toBe(expected)` parce que la sortie change à chaque exécution. Il fallait donc repenser complètement l'approche de validation.

### Le système d'éval pour `workos install`

La solution a été de construire un système d'évaluation basé sur des fixtures. Pour chaque framework supporté, l'équipe a créé des applications de démarrage minimales représentant différents états de départ :

- **example** : une application vierge, état de départ le plus simple
- **example-auth0** : une application avec Auth0 déjà installé, pour tester la migration
- **partial-install** : une installation WorkOS partiellement complétée
- **conflicting-middleware** : une application avec un middleware qui entre en conflit avec AuthKit

L'agent CLI est exécuté sur chaque fixture, puis le résultat est évalué par des métriques composites plutôt que par une comparaison exacte. Ces métriques incluent les fichiers modifiés, le succès du build et un score de revue. Le score de revue est particulièrement intéressant : c'est un évaluateur LLM (Claude) qui juge si l'installation résultante est correcte et propre, comme le ferait un relecteur humain.

### Le système d'éval pour WorkOS Skills

Le second outil, WorkOS Skills, génère automatiquement du contexte agent à partir de la documentation WorkOS. Pour l'évaluer, l'équipe a construit un système où Claude sert de juge avec un barème standardisé sur une échelle de 0 à 4 :

- **0** : la réponse est complètement incorrecte ou hors sujet
- **1** : la réponse contient des éléments pertinents mais est largement insuffisante
- **2** : la réponse est partiellement correcte mais manque d'éléments importants
- **3** : la réponse est bonne avec des détails mineurs manquants
- **4** : la réponse est excellente et complète

Ce barème est appliqué de manière cohérente sur un ensemble de questions prédéfinies, ce qui permet de suivre l'évolution de la qualité au fil des itérations du système.

### Les evals ne sont pas des tests

C'est la leçon la plus importante de l'article. Les tests unitaires sont binaires : ça passe ou ça casse. Les evals sont des instruments de mesure qui acceptent la variance pour capturer des tendances. Un test échoué signifie que quelque chose est cassé. Un score d'eval qui baisse signifie que quelque chose a probablement régressé, mais il faut investiguer pour comprendre pourquoi.

Cette distinction change fondamentalement la façon dont on interprète les résultats. On ne cherche pas le vert ou le rouge, on cherche des courbes, des tendances, des régressions statistiquement significatives. C'est un changement de paradigme pour les développeurs habitués aux suites de tests classiques.

### Définir "bon" avant de mesurer

Les deux systèmes d'éval ont enseigné la même leçon : il faut définir ce que "bon" signifie avant de commencer à mesurer. Sans définition claire de la qualité attendue, on se retrouve à évaluer au feeling (ce que l'auteur appelle le "vibes-based assessment"). Les evals structurés forcent à expliciter les critères de qualité, ce qui bénéficie non seulement à l'évaluation mais aussi à la conception de l'outil lui-même.

## Pourquoi ça compte

Cet article fournit un guide pratique et accessible pour construire des systèmes d'évaluation d'outils alimentés par l'IA, un sujet encore peu documenté malgré son importance croissante. La distinction entre tests et evals, et l'approche de juges LLM avec barème standardisé, sont directement applicables par toute équipe qui intègre des LLM dans ses produits.
