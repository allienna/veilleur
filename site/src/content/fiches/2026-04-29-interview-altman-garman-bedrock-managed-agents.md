---
title: "An Interview with OpenAI CEO Sam Altman and AWS CEO Matt Garman About Bedrock Managed Agents"
date: 2026-04-29
url: https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/
authors: [Ben Thompson, Stratechery]
keywords: [OpenAI, AWS, Bedrock, Managed Agents, partenariat]
theme: IA
tone: news
used_in: ["2026-04-29"]
---

## Résumé

Ben Thompson interviewe Sam Altman (OpenAI) et Matt Garman (AWS) à l'occasion de l'annonce de Bedrock Managed Agents. Le partenariat marque la fin de l'exclusivité OpenAI/Microsoft et place AWS comme un fournisseur d'infrastructure de premier plan pour les agents OpenAI. Le sujet central de l'interview n'est pas la qualité des modèles, mais la couche d'industrialisation : fiabilité, persistance, gestion d'état, retry — autrement dit tout ce qui sépare une démo d'un système en production.

## Points clés

- AWS et OpenAI annoncent Bedrock Managed Agents, un service géré pour faire tourner des agents OpenAI à l'échelle entreprise.
- Le partenariat met fin à l'exclusivité historique OpenAI/Microsoft sur l'infrastructure cloud.
- L'enjeu central n'est pas le modèle mais l'orchestration et la fiabilité opérationnelle.
- Le marché s'aligne sur une thèse commune : la valeur se déplace vers la couche infrastructure d'agents.
- Pour les ESN et les équipes plateforme, c'est un signal fort sur la consolidation à venir.

## Analyse approfondie

Cette interview de Stratechery, conduite par Ben Thompson, réunit Sam Altman (OpenAI) et Matt Garman (AWS) pour discuter du lancement de Bedrock Managed Agents. L'annonce s'inscrit dans une dynamique plus large : la fin de l'exclusivité OpenAI/Microsoft sur le cloud et la consolidation d'AWS comme acteur incontournable de l'infrastructure d'agents.

L'élément central qui émerge de la discussion : ni Altman ni Garman ne défendent ce produit en parlant de la qualité des modèles. Le sujet, c'est la production. Comment fait-on tourner des agents qui doivent gérer des process business sur la durée, avec persistance d'état, retries, et garanties opérationnelles ? Comment passe-t-on du POC avec un dev seul devant son IDE à un système qui sert des milliers de requêtes par jour avec des SLAs ?

Le positionnement d'AWS est stratégique : il ne s'agit pas de proposer un nouveau framework agentic, mais d'apporter à l'écosystème OpenAI ce qu'AWS sait faire mieux que personne — l'opération à grande échelle de systèmes distribués durables. Bedrock devient l'outil par lequel les entreprises peuvent consommer les modèles OpenAI sans avoir à gérer elles-mêmes les couches de fiabilité.

Pour OpenAI, c'est un repositionnement subtil : on cesse de vendre seulement le modèle pour vendre une promesse opérationnelle. Et c'est aussi, implicitement, l'aveu que la couche d'agents managés ne se construit pas en interne sans s'appuyer sur un opérateur cloud.

L'interview revient également sur la question business sous-jacente : quelle valeur se capture où ? Si la couche d'orchestration devient la pièce maîtresse, les hyperscalers (AWS, Azure, GCP) sont positionnés idéalement. Les éditeurs de modèles doivent se demander où ils tracent leur frontière de produit.

## Pourquoi ça compte

Cette interview est un marqueur de l'année 2026 : le marché se réorganise autour de l'industrialisation, plus autour de la course aux benchmarks. Pour décrypter le mouvement stratégique de fond, c'est une lecture clé.
