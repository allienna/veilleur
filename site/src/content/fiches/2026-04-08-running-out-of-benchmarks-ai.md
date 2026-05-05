---
title: "We're actually running out of benchmarks to upper bound AI capabilities"
date: 2026-04-08
url: "https://www.lesswrong.com/posts/gfkJp8Mr9sBm83Rcz/we-re-actually-running-out-of-benchmarks-to-upper-bound-ai"
authors: ["LessWrong"]
keywords: [benchmarks IA, saturation, évaluation, METR, capacités IA]
theme: "IA"
tone: "research"
used_in: ["2026-04-08"]
---

## Résumé

Un chercheur associé à METR constate que l'IA progresse plus vite que notre capacité à la mesurer. Les benchmarks traditionnels sont saturés à un rythme accéléré, et les nouvelles approches (évaluations agentiques, études d'uplift) peinent à suivre le rythme des capacités des modèles.

## Points clés

- Les benchmarks qui semblaient infranchissables en 2024 (comme GPQA) ont été saturés en un an
- Les approches alternatives (Time Horizon de METR, BrowseComp d'OpenAI, GDPval) émergent mais ne suffisent pas
- La saturation des benchmarks rend difficile l'évaluation des risques des modèles frontier
- Le problème n'est pas seulement technique : sans mesure fiable, les politiques de sécurité des labs sont aveugles
- Les benchmarks agentiques (τ2-Bench, Terminal-Bench) sont plus résistants mais aussi saturés plus vite que prévu

## Analyse approfondie

### Le paradoxe de la mesure

L'article met en lumière un paradoxe fondamental : plus les modèles progressent vite, plus nous avons besoin de benchmarks fiables pour évaluer leurs capacités et risques — mais c'est précisément cette progression qui rend les benchmarks existants obsolètes. La communauté de recherche court après un train qui accélère.

### De GPQA à l'ère agentique

L'auteur retrace l'évolution rapide : en début 2025, GPQA était considéré comme un défi majeur. Moins d'un an plus tard, il était saturé. Les labs ont répondu avec de nouvelles approches — la méthodologie Time Horizon de METR, les évaluations de type BrowseComp d'OpenAI — mais le cycle de saturation se raccourcit à chaque itération.

### Implications pour la sécurité IA

Le point le plus préoccupant est le lien avec la sécurité. Les frontier AI safety policies d'Anthropic et OpenAI reposent sur des seuils de capacité mesurés par des benchmarks. Si ces benchmarks ne mesurent plus rien (car saturés), les mécanismes de sécurité perdent leur fondement empirique. C'est un problème de gouvernance autant que technique.

## Pourquoi ça compte

Cette réflexion touche à un enjeu fondamental de la gouvernance IA : si nous ne pouvons plus mesurer les capacités des modèles, nous ne pouvons plus prendre de décisions éclairées sur leur déploiement. Le rythme de saturation des benchmarks est un indicateur avancé de la progression de l'IA.
