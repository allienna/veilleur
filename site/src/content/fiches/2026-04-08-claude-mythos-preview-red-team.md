---
title: "Claude Mythos Preview — Red Team Assessment"
date: 2026-04-08
url: "https://red.anthropic.com/2026/mythos-preview/"
authors: ["Nicholas Carlini", "Anthropic Red Team"]
keywords: [Claude Mythos, red team, zero-day, exploit, reverse engineering]
theme: "Sécurité"
tone: "research"
used_in: ["2026-04-08"]
---

## Résumé

Le rapport technique du red team d'Anthropic détaille les capacités de Claude Mythos Preview en cybersécurité. Le modèle découvre des vulnérabilités zero-day dans des codebases réels, génère des exploits fonctionnels, et démontre des capacités de reverse engineering sur du code fermé — transformant des vulnérabilités N-day en exploits exploitables.

## Points clés

- Mythos Preview découvre des zero-days et génère des exploits fonctionnels de bout en bout
- Le modèle est capable de reverse-engineering sur du code fermé (binaires compilés)
- Il transforme des vulnérabilités N-day (connues mais non exploitées) en exploits opérationnels
- Plus de 99 % des failles découvertes n'étaient pas encore patchées au moment du rapport
- Les évaluations couvrent à la fois les codebases open source et les logiciels propriétaires

## Analyse approfondie

### Méthodologie rigoureuse

Le rapport, signé par une équipe de plus de 20 chercheurs, détaille les protocoles d'évaluation utilisés. L'équipe a testé Mythos Preview sur des tâches de sécurité progressives : d'abord la détection de vulnérabilités connues, puis la découverte de failles inédites (zero-days), et enfin la génération d'exploits complets.

### Zero-days dans des logiciels critiques

Le résultat le plus frappant est la capacité du modèle à trouver des zero-days dans chaque OS et navigateur majeur. Le rapport indique que ces failles sont de haute sévérité et que la grande majorité n'a pas encore été corrigée — d'où la retenue d'Anthropic sur les détails spécifiques.

### Reverse engineering et N-day

Au-delà de la découverte de vulnérabilités dans du code source, Mythos Preview démontre une capacité inédite : le reverse engineering de binaires compilés. Le modèle peut analyser du code fermé, identifier des vulnérabilités, et produire des exploits fonctionnels. Il peut également prendre des vulnérabilités connues (N-day) pour lesquelles aucun exploit public n'existe et en créer un.

### Un moment charnière pour la recherche en sécurité

Les auteurs qualifient cette publication de "watershed moment" pour la sécurité informatique. La combinaison de la vitesse d'analyse, de la capacité à travailler sur du code source comme sur des binaires, et de la qualité des exploits générés place le modèle au-dessus des capacités de la plupart des chercheurs en sécurité humains.

## Pourquoi ça compte

Ce rapport technique fournit les preuves concrètes derrière les annonces de Project Glasswing. Il établit que l'IA frontier a franchi un seuil qualitatif en cybersécurité offensive, rendant urgente la mise en place de défenses à la hauteur.
