---
title: "Lessons from Building Claude Code: How We Use Skills"
date: 2026-03-18
url: https://links.tldrnewsletter.com/HZAKB9
authors: [Thariq, Anthropic]
keywords: [Claude Code, skills, agents IA, workflows, vérification]
theme: IA
tone: tutorial
used_in: ["2026-03-18"]
---

## Résumé

Thariq, d'Anthropic, partage les leçons tirées de l'utilisation intensive de skills dans Claude Code. Avec des centaines de skills en usage actif, l'article révèle que les skills ne sont pas de simples fichiers markdown — ce sont des dossiers contenant scripts, assets et hooks. Les meilleures skills incluent des scripts de vérification qui enregistrent la sortie vidéo. L'insight central : le système autour du modèle compte plus que le modèle lui-même.

## Points clés

- Des centaines de skills sont en usage actif dans Claude Code au sein d'Anthropic
- Les skills ne sont pas de simples fichiers markdown — ce sont des dossiers complets avec scripts, assets et hooks
- Catégories de skills : utilisation de bibliothèques, vérification, migration, workflow
- Les meilleures skills intègrent des scripts de vérification qui enregistrent la sortie vidéo pour valider le résultat
- Insight clé : le système autour du modèle importe plus que le modèle lui-même
- L'investissement dans l'outillage et les processus entourant l'agent multiplie son efficacité

## Analyse approfondie

Thariq, membre de l'équipe Anthropic, détaille comment l'équipe utilise les skills dans Claude Code — le CLI officiel d'Anthropic pour Claude. L'article va bien au-delà d'un simple tutoriel pour révéler une philosophie de l'ingénierie agentique.

### L'échelle d'utilisation

L'équipe a des centaines de skills en usage actif. Ce n'est pas un gadget ou une fonctionnalité marginale — les skills sont un élément central de la façon dont Anthropic elle-même utilise Claude Code au quotidien. Cette échelle d'adoption interne est en soi un signal fort sur l'importance du concept.

### Les skills ne sont pas du markdown

La conception courante d'une "skill" pour un agent IA est un fichier de prompt : un document markdown contenant des instructions. L'article révèle que les skills de Claude Code sont bien plus que cela. Ce sont des dossiers structurés qui peuvent contenir :

- **Des fichiers markdown** décrivant les instructions et le contexte
- **Des scripts exécutables** que l'agent peut lancer pour effectuer des actions
- **Des assets** (images, fichiers de configuration, templates) nécessaires à la skill
- **Des hooks** qui se déclenchent à des moments précis du workflow

Cette architecture transforme une skill d'une simple instruction en un véritable micro-environnement de travail pour l'agent.

### Catégories de skills

L'article identifie quatre grandes catégories de skills en usage chez Anthropic :

- **Utilisation de bibliothèques** : skills qui enseignent à l'agent comment utiliser correctement une bibliothèque spécifique, avec ses conventions, ses pièges et ses bonnes pratiques
- **Vérification** : skills dédiées à la validation du travail produit, avec des critères explicites de succès et des scripts de test
- **Migration** : skills qui guident l'agent à travers des transformations de code complexes, étape par étape, avec des points de contrôle
- **Workflow** : skills qui orchestrent des processus complets impliquant plusieurs outils et étapes

### Le pouvoir de la vérification

Le point le plus marquant de l'article concerne les skills de vérification. Les meilleures skills ne se contentent pas de dire à l'agent quoi faire — elles incluent des scripts qui vérifient automatiquement que le résultat est correct. Certaines vont jusqu'à enregistrer la sortie vidéo de l'exécution pour une validation visuelle.

Cette approche résout un problème fondamental des agents IA : sans vérification, l'agent ne sait pas si son travail est réellement correct. Il peut produire du code qui compile mais qui ne fait pas ce qu'on attend. Les scripts de vérification ferment cette boucle de feedback.

### Le système compte plus que le modèle

L'insight central de l'article est que les performances d'un agent IA dépendent davantage du système qui l'entoure que du modèle lui-même. Un modèle moyen avec d'excellentes skills, des scripts de vérification robustes et des workflows bien conçus surpassera un modèle supérieur utilisé "nu", sans structure autour de lui.

C'est un message important pour l'industrie : plutôt que d'attendre le prochain modèle plus puissant, investir dans l'outillage — les skills, les guardrails, les boucles de feedback — est le levier le plus immédiat et le plus rentable pour améliorer la productivité des agents.

### Implications pour les équipes

Pour les équipes qui adoptent des agents de codage, l'article suggère un changement de priorité : au lieu de se concentrer sur le choix du meilleur modèle, investir dans la création d'une bibliothèque de skills adaptée à leur contexte spécifique. Cela inclut documenter les conventions du projet, créer des scripts de vérification automatisés, et structurer des workflows reproductibles.

## Pourquoi ça compte

Cet article fournit un retour d'expérience de première main sur l'utilisation des agents IA à grande échelle chez Anthropic elle-même. L'insight que le système autour du modèle importe plus que le modèle est une leçon précieuse pour toute équipe qui construit avec des agents — et un contre-pied à la course aux benchmarks.
