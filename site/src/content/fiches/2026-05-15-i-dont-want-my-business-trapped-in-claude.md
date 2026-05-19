---
title: "I don't want my business trapped in Claude"
date: 2026-05-15
url: https://aiwithremy.beehiiv.com/
authors: [aiwithremy.beehiiv.com, Remy Gaskell]
keywords: [vendor lock-in, AI agents, portability, Claude, business workflow]
theme: IA
tone: opinion
used_in: ["2026-05-15"]
---

## Résumé

Rémy Gaskell, builder et auteur de la newsletter AI with Remy, explique pourquoi il refait l'architecture de son setup IA pour ne pas se retrouver "piégé dans Claude". Sa thèse : séparer son OS personnel (qui peut rester fortement intégré à Claude Code) de ses agents business, qui doivent rester portables et capables de migrer d'une plateforme à l'autre. Il documente aussi des annonces clés de la semaine côté Notion, Claude Small Business et Codex.

## Points clés

- Le lock-in plateforme est un risque concret quand les agents tournent en production
- Rémy sépare son setup en deux : OS personnel (intimement lié à un fournisseur) et agents business (portables)
- Notion a lancé sa Developer Platform pour faire du workspace un canvas partagé humains/agents
- Anthropic a lancé Claude for Small Business pour packager Claude comme un employé IA
- OpenAI a battu Anthropic sur le primitive `/goal` (agent long-running), Hermes l'a copié rapidement

## Analyse approfondie

### Le constat de départ

Rémy ouvre sa newsletter en racontant que son réflexe a longtemps été de tout brancher sur Claude — Claude Code pour le dev, Claude pour le chat, Claude Agent SDK pour les déploiements business. Une intégration fluide, des résultats spectaculaires. Mais en regardant la quantité de logique métier qu'il avait fini par cabler en dur dans l'écosystème Anthropic, il a réalisé que migrer ailleurs coûterait des semaines de travail.

D'où le pivot : tracer une frontière claire entre ce qui peut rester "trapped" et ce qui ne doit jamais l'être.

### La séparation OS personnel / agents business

Pour son OS personnel — la façon dont lui-même bosse au quotidien — Rémy garde Claude Code comme socle. Il assume la dépendance, parce que la productivité personnelle dépend de l'intégration fine. Si Claude change ses prix demain, il s'adaptera ou paiera. C'est son outil, pas son produit.

Pour les agents business — ceux qui tournent dans des entreprises clientes, gèrent des intégrations Gmail/Xero/Salesforce et créent de la valeur facturable — il refuse cette logique. Ces agents doivent rester portables. Concrètement, ça veut dire :
- Une couche d'abstraction sur les LLM (n'importe quel provider, swappable)
- Un état métier qui vit dans la base de l'entreprise, pas dans une mémoire Anthropic
- Des outils définis dans des standards ouverts (MCP, OpenAPI) plutôt que dans des SDK propriétaires
- Des tests d'évaluation qui tournent contre plusieurs modèles, pas un seul

L'argument économique est direct : si Claude met ses agents au compteur (ce qui vient justement d'arriver), un business qui dépend à 100 % de Claude voit sa marge brute bouger sans avoir bougé son code.

### Les annonces de la semaine

Au passage, Rémy commente plusieurs annonces du jour :
- **Notion Developer Platform** : le workspace devient un canvas partagé où humains, agents, données live et contexte cohabitent. Pour Rémy, c'est la première vraie réponse au problème du contexte partagé entre coéquipiers humains et agentic.
- **Claude for Small Business** : Anthropic packagise Claude comme un "employé IA" pour les fonctions finance, sales, marketing, support, HR, ops. Un produit consommable, pas une API.
- **Claude Agent View** : gérer 3, 5 ou 10 sessions Claude Code en parallèle ressemble de plus en plus à une salle de contrôle d'agents.
- **Codex `/goal`** : OpenAI a battu Claude Code sur une primitive d'agent long-running vraiment utile, et Hermes (NousResearch) l'a copiée rapidement.

### La conclusion implicite

Le message global de l'édition : les outils convergent (tous se mettent à l'orchestration multi-agents, tous packagent l'IA comme un employé), et l'arbitrage qui compte n'est plus "quel outil je choisis" mais "quelle dépendance je me crée".

## Pourquoi ça compte

C'est une voix de praticien (pas d'analyste) qui formalise une discipline d'architecture devenue urgente : distinguer la dépendance qu'on assume (productivité personnelle) de celle qu'on refuse (continuité business). Un cadre simple, exportable, et qu'on devrait tous appliquer cette semaine.
