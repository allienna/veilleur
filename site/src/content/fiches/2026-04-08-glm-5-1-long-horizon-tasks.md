---
title: "GLM-5.1: Towards Long-Horizon Tasks"
date: 2026-04-08
url: "https://z.ai/blog/glm-5.1"
authors: ["Zhipu AI"]
keywords: [GLM-5.1, agents IA, SWE-Bench, tâches longues, coding]
theme: "IA"
tone: "research"
used_in: ["2026-04-08"]
---

## Résumé

Zhipu AI lance GLM-5.1, un modèle flagship conçu pour les tâches agentiques à horizon long. Il atteint l'état de l'art sur SWE-Bench Pro (58.4) et démontre une capacité unique à rester productif sur des centaines d'itérations, là où les modèles précédents plafonnent rapidement.

## Points clés

- GLM-5.1 atteint 58.4 sur SWE-Bench Pro, devant GPT-5.4 (57.7), Opus 4.6 (57.3) et Gemini 3.1 Pro (54.2)
- Le différenciateur clé : la capacité à maintenir sa productivité sur des sessions longues (600+ itérations)
- Les modèles précédents "épuisent leur répertoire" rapidement ; GLM-5.1 continue d'optimiser
- Démonstration sur trois scénarios : optimisation de base vectorielle, benchmark GPU, application web open-ended
- Le modèle révise sa stratégie en continu, ce qui le rend efficace sur les tâches ambiguës

## Analyse approfondie

### Le vrai différenciateur : l'endurance

La plupart des modèles de code appliquent leurs techniques les plus efficaces dès le départ, puis stagnent. Donner plus de temps à GPT-5.4 ou Opus 4.6 n'améliore pas significativement leurs résultats après un certain seuil. GLM-5.1 rompt avec ce pattern : sa performance continue de croître avec le temps de calcul, ce qui en fait un candidat naturel pour les workflows agentiques longs.

### Scénarios d'évaluation progressifs

L'évaluation est particulièrement bien conçue. Les trois scénarios représentent un gradient de structure : (1) optimisation de base vectorielle avec une métrique numérique claire, (2) benchmark GPU avec des mesures par problème, (3) construction d'application web sans métrique — uniquement le jugement du modèle. Ce gradient teste à la fois la capacité technique et le jugement autonome.

### Implications pour l'écosystème

L'arrivée de GLM-5.1 confirme que la course aux agents IA est mondiale. Zhipu AI, basé en Chine, propose un modèle qui rivalise avec les leaders occidentaux sur les benchmarks les plus exigeants. La compétition pousse l'ensemble de l'industrie vers des agents plus endurants et plus autonomes.

## Pourquoi ça compte

GLM-5.1 ajoute un concurrent sérieux dans la course aux agents de code, et son approche "long-horizon" pourrait redéfinir ce qu'on attend d'un modèle agentique. La capacité à rester productif sur la durée est potentiellement plus importante que la performance en one-shot.
