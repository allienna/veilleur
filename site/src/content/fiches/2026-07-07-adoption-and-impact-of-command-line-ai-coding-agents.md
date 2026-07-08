---
title: "Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI"
date: 2026-07-07
url: https://arxiv.org/abs/2607.01418
authors: [Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva]
keywords: [agents en ligne de commande, adoption, rétention, productivité, pull requests]
theme: IA
tone: research
used_in: ["2026-07-07"]
---

## Résumé

Cette étude académique analyse le déploiement à grande échelle des agents de code en ligne de commande (Claude Code et GitHub Copilot CLI) chez Microsoft début 2026, sur un échantillon de dizaines de milliers d'ingénieurs. Les auteurs s'intéressent à trois questions : qui adopte ces outils, qui continue à les utiliser dans la durée, et si leur usage se traduit par un gain de production mesurable. Leur résultat central : la première utilisation se propage surtout via les réseaux sociaux internes, la rétention est davantage liée à l'activité de code des ingénieurs qu'à des facteurs démographiques, et les adopteurs mergent environ 24 % de pull requests en plus que ce qu'ils auraient fait sans ces outils — un effet qui se maintient sur quatre mois.

## Points clés

- Étude menée sur des dizaines de milliers d'ingénieurs chez Microsoft pendant le déploiement anticipé de Claude Code et GitHub Copilot CLI début 2026.
- La première adoption se diffuse principalement par les réseaux sociaux internes (l'usage visible des pairs), plus que par une politique descendante.
- La rétention dans l'usage de l'outil est corrélée à l'activité de code des ingénieurs, pas à des variables démographiques.
- Les adopteurs mergent environ 24 % de pull requests en plus que leur contrefactuel estimé, un proxy imparfait pour la valeur produite mais un signal robuste.
- Cet effet de productivité persiste sur toute la fenêtre d'observation de quatre mois, ce qui exclut un simple effet de nouveauté.
- Conclusion des auteurs : les organisations qui déploient ces outils devraient traiter l'usage visible entre pairs comme un levier central de leur stratégie de rollout.

## Analyse approfondie

L'article part d'un enjeu de coût pour les grandes organisations : les dépenses en tokens liées aux agents de code en ligne de commande peuvent atteindre plusieurs millions de dollars par an, ce qui rend coûteuse une mauvaise lecture de l'adoption, de la rétention ou de l'impact réel de ces outils. Pour y répondre avec des données de terrain plutôt que des déclarations d'intention, les auteurs — chercheurs chez Microsoft — étudient le déploiement précoce de Claude Code et de GitHub Copilot CLI en 2026, sur une population de dizaines de milliers d'ingénieurs.

Le papier articule ses résultats autour de trois axes. D'abord l'adoption initiale : elle ne suit pas d'abord une logique hiérarchique ou de formation officielle, mais se propage surtout par les réseaux sociaux internes — voir des collègues proches utiliser l'outil augmente fortement la probabilité de l'essayer soi-même. Ensuite la rétention : contrairement à l'intuition selon laquelle l'ancienneté, le niveau ou d'autres facteurs démographiques expliqueraient qui continue d'utiliser l'outil dans la durée, c'est l'activité de code des ingénieurs (le volume et la régularité de leur travail de développement) qui est le meilleur prédicteur d'un usage soutenu.

Enfin, l'impact sur la production : les auteurs utilisent le nombre de pull requests mergées comme indicateur de production, tout en reconnaissant explicitement ses limites (une PR mergée n'équivaut pas à la valeur qu'elle délivre). Sur cette base, ils mesurent un gain d'environ 24 % de pull requests mergées chez les adopteurs par rapport à une estimation de ce qu'ils auraient produit sans l'outil. Point important méthodologiquement : ce gain se maintient sur toute la fenêtre d'observation de quatre mois, ce qui suggère un effet réel et durable plutôt qu'un simple pic de nouveauté ou de curiosité initiale.

Les auteurs concluent que les agents de code en ligne de commande ne sont ni adoptés de façon uniforme dans l'organisation, ni un simple effet de mode passager, et recommandent aux entreprises qui envisagent un déploiement similaire de considérer l'usage visible entre pairs comme un facteur stratégique central de leur plan de rollout — plus que la seule communication descendante ou la formation formelle.

## Pourquoi ça compte

C'est l'une des premières études d'ampleur à mesurer, avec des données de production réelles et sur plusieurs mois, l'impact des agents de code en ligne de commande en entreprise — un contrepoint chiffré utile face aux discours à la fois trop optimistes et trop alarmistes sur l'IA en ingénierie logicielle.
