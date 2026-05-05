---
title: "Introducing Ads CLI: A Command-Line Interface for Meta Ads and Commerce"
date: 2026-04-30
url: https://developers.facebook.com/blog/post/2026/04/29/introducing-ads-cli/
authors: [Meta, John Holstein, Matt Mayberry, Andrew Kutsy, Sanjay Patel]
keywords: [meta-ads-cli, agents, marketing-api, commerce, automation]
theme: IA
tone: news
used_in: ["2026-04-30"]
---

## Résumé

Meta lance le 29 avril 2026 son `ads-cli`, un outil en ligne de commande officiel pour piloter les campagnes Meta Ads, conçu autant pour les développeurs que pour les agents IA. L'outil packagé l'API Marketing en commandes prévisibles, gère l'authentification, la pagination, l'output et les erreurs, et supporte plusieurs formats de sortie (JSON, texte). C'est la première façon officielle, first-party, de plugger un agent IA dans un compte publicitaire Meta — et c'est gratuit, en open beta.

## Points clés

- Premier CLI officiel et first-party de Meta pour piloter les Meta Ads en ligne de commande.
- Conçu pour être consommé par des agents IA aussi bien que par des développeurs humains.
- Packagé l'API Marketing avec auth, pagination, formatage et gestion d'erreurs out-of-the-box.
- Supporte plusieurs formats de sortie (JSON, texte) pour s'intégrer à des pipelines automatisés.
- Remplace les wrappers tiers payants (~49 $/mois) qui faisaient courir un risque de bannissement de compte.

## Analyse approfondie

Meta introduit le Meta ads CLI, un outil en ligne de commande pour les développeurs qui veulent piloter leurs campagnes Meta Ads. Les développeurs et les agents IA qui travaillent avec l'API Meta Marketing peuvent désormais créer, éditer et analyser des campagnes directement depuis la ligne de commande, sans écrire de code custom.

### Pourquoi Meta a construit le ads CLI

Les développeurs racontent à Meta que l'API Meta Marketing est puissante, mais que l'utiliser de façon programmatique signifie réécrire le même code de nombreuses fois : authentification, pagination, formatage de la sortie, gestion des erreurs. Ces tâches répétitives ralentissent le développement et compliquent l'intégration de la gestion de campagnes dans des workflows automatisés.

Le ads CLI résout ce problème en packageant l'API Meta Marketing dans un seul outil avec des commandes prévisibles que développeurs et agents IA peuvent utiliser de façon fiable :

```
meta ads campaign list
meta ads insights get --campaign_id CAMPAIGN_ID --date-preset last_7d --fields conversions,impressions
```

Le CLI supporte plusieurs formats de sortie — JSON, texte plat — ce qui permet de l'intégrer à des pipelines existants et à des outils d'orchestration agentiques.

### Conçu pour les agents

Le point qui change tout, c'est la posture de Meta vis-à-vis des agents. Le CLI est explicitement positionné comme un outil dont les agents peuvent se servir directement. La sémantique des commandes est stable, les erreurs sont structurées, et l'output est prévisible. C'est exactement ce qui manquait à l'API Marketing pour être utilisable par un LLM sans que celui-ci hallucine des paramètres ou se perde dans la pagination.

Avant cette annonce, les agents qui voulaient piloter Meta Ads passaient par des wrappers tiers facturés autour de 49 $/mois — avec, en bonus, un risque non négligeable de se faire bannir le compte parce que ces wrappers contournaient les patterns d'API officiels. Désormais, c'est gratuit, officiel, et two-minutes-to-setup, comme le formule le post de Remy Gaskell qui a relayé la nouvelle dans sa newsletter "AI with Remy".

### Cas d'usage

Les premiers cas d'usage poussés par Meta tournent autour de l'analyse de campagnes (un agent qui pull les insights tous les jours et alerte si une campagne sous-performe), de l'optimisation de budget (l'agent qui réalloue automatiquement entre adsets selon le ROAS) et de la création de campagnes itératives (l'agent qui génère 5 variantes créatives, les push, et lit les conversions à 24h pour itérer).

Plus globalement, le ads CLI s'inscrit dans le mouvement de la semaine : Stripe Link CLI pour les paiements agentiques, Cloudflare pour le provisioning agentique, Meta Ads pour la pub agentique. Trois grandes plateformes, en moins d'une semaine, qui publient un CLI taillé pour les agents. Le pattern devient un standard de fait : packager une API en CLI prévisible, déterministe, et auditable, c'est l'interface que les agents préfèrent — bien plus que les MCP servers à grain fin ou les SDKs verbeux.

### Implications

Pour les marketers et les boîtes qui font de l'acquisition payante, c'est une invitation à construire des agents pilotes de campagnes avec un sérieux gain de productivité. Mais c'est aussi un sujet de gouvernance important : un agent qui peut créer et budgéter des campagnes Meta peut aussi cramer un budget en quelques heures s'il dérape. Comme pour Stripe Link CLI, la question des plafonds, des audits et des approbations devient centrale.

Pour les développeurs, le pattern à retenir est plus large : si tu maintiens une API publique, sortir un CLI officiel destiné aux agents est probablement la prochaine étape de ton produit.

## Pourquoi ça compte

L'`ads-cli` de Meta confirme le pattern de la semaine : les grandes plateformes packagent leurs APIs en CLI prévisibles, taillés pour les agents IA. C'est une nouvelle interface de consommation des services cloud et SaaS qui se met en place sous nos yeux, et elle redéfinit qui pilote les budgets marketing en bout de chaîne.
