---
title: "Microsoft Agent 365, now generally available, expands capabilities and integrations"
date: 2026-05-07
url: https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
authors: [microsoft.com]
keywords: [agents, gouvernance, observabilité, shadow-ai, defender]
theme: IA
tone: news
used_in: ["2026-05-07"]
---

## Résumé

Microsoft annonce la disponibilité générale d'Agent 365, son "control plane" pour observer, gouverner et sécuriser les agents IA — qu'ils soient bâtis avec ses propres outils ou par des partenaires de l'écosystème. L'enjeu : freiner la prolifération des agents qui s'installent dans les SI sans visibilité IT, en s'appuyant sur Defender, Intune et un environnement Windows 365 dédié aux agents. La sortie de GA s'accompagne d'une série de previews qui élargissent la couverture aux agents autonomes, aux SaaS partenaires et aux agents locaux comme OpenClaw, Claude Code ou GitHub Copilot CLI.

## Points clés

- Agent 365 passe en GA et couvre désormais à la fois les agents agissant pour le compte d'utilisateurs et les agents avec leurs propres credentials
- Microsoft Defender et Intune permettent de découvrir et bloquer les agents locaux non managés (shadow AI), à commencer par OpenClaw
- Une cartographie d'exposition (asset context mapping) arrivera en juin 2026, reliant agents, MCP servers, identités et ressources cloud
- Windows 365 for Agents fournit un environnement managé dédié à l'exécution sécurisée des agents
- L'écosystème SaaS est intégré (agents construits via Foundry, Bedrock, Gemini Enterprise) pour offrir une vue unifiée

## Analyse approfondie

Microsoft ouvre son billet par un constat : les agents IA ne sont pas une promesse à venir, ils tournent déjà dans les environnements. Ils apparaissent là où on les attend — Copilot, Teams, Microsoft 365 — mais aussi dans des recoins moins visibles : assistants locaux autonomes, agents SaaS connectés à des données sensibles, scripts qui s'enchaînent et invoquent d'autres outils.

Le problème n'est pas l'existence des agents, mais leur multiplication rapide à travers applications, endpoints et clouds, souvent en dehors du périmètre des équipes responsables du risque. Un agent qui peut invoquer des outils, accéder à des données et interagir avec d'autres agents transforme un workflow utile en oversharing de données, en mésusage d'outils ou en actions à privilèges excessifs en quelques secondes. Et plus les agents deviennent faciles à créer, plus la surface d'attaque grandit.

D'où la promesse : on ne peut pas gouverner ce qu'on ne voit pas, ni sécuriser ce qu'on ne comprend pas. Agent 365 se positionne comme le control plane pour observer, gouverner et sécuriser les agents et leurs interactions, en s'appuyant sur les workflows admin et sécurité que les équipes utilisent déjà.

### Une plateforme unique, quel que soit le mode d'exécution

Microsoft distingue trois cas d'usage : agents délégués (agissant pour un utilisateur, GA), agents avec leurs propres accès opérant en arrière-plan (GA), et agents avec leurs propres accès participant à des workflows d'équipe (preview publique). Cette taxonomie est importante : elle reflète la maturité grandissante des déploiements, où certains agents triant des tickets de support tournent désormais avec leurs propres identités plutôt que sous celle d'un utilisateur.

### Découverte du shadow AI

Le morceau le plus significatif concerne la détection du shadow AI. Defender et Intune vont permettre de découvrir et gérer les agents locaux installés sur des appareils Windows, en commençant par OpenClaw, puis en élargissant à GitHub Copilot CLI et Claude Code. Pour les clients du programme Frontier, la console Microsoft 365 fait apparaître une page Shadow AI listant les agents OpenClaw détectés, leurs appareils, et permet d'appliquer des stratégies Intune pour bloquer leurs méthodes d'exécution courantes.

À partir de juin 2026, Defender fournira une cartographie d'exposition pour chaque agent, incluant les appareils sur lesquels ils tournent, les MCP servers configurés, les identités associées, et les ressources cloud que ces identités peuvent atteindre. Les équipes sécurité pourront évaluer la surface d'exposition et le rayon d'impact potentiel, et investiguer l'activité des agents (accès fichiers, comportement réseau) avec les données endpoint habituelles.

### Contrôles policy-based et runtime blocking

Au-delà du monitoring, Agent 365 permettra d'appliquer des contrôles basés sur des politiques pour définir ce que les agents ont le droit de faire, avec un support initial pour OpenClaw via Intune. Si un agent managé adopte des comportements malveillants — tentative d'accès ou d'exfiltration de données sensibles — Defender pourra bloquer les coding agents en runtime et générer des alertes contextualisées.

### Couverture multi-cloud

Comme les développeurs construisent des agents avec Microsoft Foundry, AWS Bedrock et Google Gemini Enterprise, Agent 365 ambitionne d'offrir une visibilité cross-cloud, étendue à un large écosystème SaaS où des partenaires (Software Development Companies) embarquent leurs propres agents.

## Pourquoi ça compte

Cette annonce marque le passage des agents IA d'un sujet d'innovation à un sujet de gouvernance d'entreprise. Pour les DSI et RSSI, la question n'est plus "faut-il adopter les agents" mais "qui tient l'inventaire et le control plane", et Microsoft se positionne comme un acteur incontournable du périmètre — y compris pour des agents non-Microsoft.
