---
title: "The Future Of Software Engineering with Anthropic"
date: 2026-03-17
url: https://www.akashbajwa.co/p/the-future-of-software-engineering
authors: [Akash Bajwa, Sivesh]
keywords: [software engineering, Claude Code, test-first, closed-loop, evals]
theme: IA
tone: opinion
used_in: ["2026-03-17"]
---

## Résumé

Un roundtable organisé par Akash Bajwa et Sivesh avec Anthropic et des engineering leaders de Stripe, NVIDIA, Google DeepMind, Microsoft, Apple, xAI et Scale AI a produit une synthèse rare sur l'évolution concrète des pratiques d'ingénierie logicielle. Les participants ont convergé sur trois mutations majeures : le test-first comme nouveau paradigme par défaut, deux niveaux d'évaluations (régression + nouvelles capacités), et le "closed-loop development" comme source des gains composés.

## Points clés

- Test-first devient le standard : définir les cas de test d'abord, laisser l'agent construire en face
- Deux niveaux d'evals : régression (100% obligatoire sur chaque PR) + frontier (nouvelles capacités)
- Le closed-loop development — bug → triage agent → PR de correction — est la source des gains composés
- Consensus fort : ne pas mandater l'adoption, passer par hackathons et compétitions internes
- Claude Code est né comme une UI terminal simple en fin 2024, conçu pour les modèles de dans 6-12 mois

## Analyse approfondie

### L'origine de Claude Code

La session a débuté par une retelling de l'histoire de Claude Code. Début fin 2024 comme une simple interface terminal, le projet a été construit contre un principe directeur : concevoir pour les capacités des modèles dans 6 à 12 mois, pas pour là où ils en sont aujourd'hui. L'adoption a été organique — un projet piloté par des ICs (individual contributors) qui a scalé par la valeur démontrée, pas par décision hiérarchique.

### Le closed-loop development

Un des fils directeurs de la discussion était le "closed-loop development". Un participant a décrit un setup dans son entreprise où les rapports de bugs sont automatiquement triés par un agent, classifiés par sévérité, vérifiés contre un ensemble d'evals, et une PR de correction est ouverte — le tout avec un minimum de touche humaine. La salle a largement reconnu ce pattern.

L'argument de fond : les gains composés viennent de boucles, pas d'étapes isolées. De meilleurs outils de code améliorent les modèles. De meilleurs modèles améliorent les outils. Les équipes qui construisent ces boucles maintenant accumulent un avantage difficile à rattraper.

### Test-first et deux niveaux d'évals

Plusieurs participants ont décrit un changement de paradigme : on définit les cas de test d'abord et on laisse l'agent construire en face. Cette approche a été décrite comme "la seule façon sensée de gérer le volume de PRs générées."

Pour gérer ce volume de façon fiable, une architecture d'évaluations en deux niveaux s'est imposée naturellement :
- **Evals de régression** : doivent rester à 100% et tournent sur chaque PR
- **Evals de nouvelles capacités** : pour les fonctionnalités inédites, permettent d'avancer sans régresser

### Sur l'adoption et le management

Consensus fort dans la salle : ne jamais mandater l'adoption. Un participant a décrit l'utilisation de compétitions et hackathons comme mécanisme d'adoption. La différence entre les équipes qui progressent et celles qui stagnent n'est pas la qualité du modèle IA — c'est la culture d'expérimentation et le feedback loop.

## Pourquoi ça compte

Ce compte-rendu de roundtable est rare : des engineering leaders de tier 1 qui partagent leurs pratiques concrètes, pas leurs intentions. La convergence sur test-first, closed-loop et double-tier evals dessine un standard émergent pour les équipes qui veulent vraiment bénéficier des agents autonomes.
