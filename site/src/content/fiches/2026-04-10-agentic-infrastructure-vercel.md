---
title: "Agentic Infrastructure"
date: 2026-04-10
url: "https://vercel.com/blog/agentic-infrastructure?utm_source=tldrai"
authors: ["Vercel"]
keywords: [agentic infrastructure, Vercel, coding agents, AI SDK, serverless]
theme: "IA"
tone: "opinion"
used_in: ["2026-04-10"]
---

## Résumé

Guillermo Rauch (CEO de Vercel) affirme que chaque génération de logiciels exige une nouvelle infrastructure, et que nous entrons dans l'ère de l'infrastructure agentique. Les déploiements Vercel ont doublé en trois mois, portés par les coding agents qui représentent désormais plus de 30 % des déploiements. Vercel se positionne comme plateforme "agentic-first", conçue pour un monde où l'acteur final qui déploie est de plus en plus souvent une machine.

## Points clés

- Les déploiements hebdomadaires sur Vercel ont doublé en 3 mois ; plus de 30 % proviennent de coding agents (croissance de 1000 % en 6 mois)
- Claude Code représente 75 % des déploiements par agents, suivi de Lovable/v0 (6 %) et Cursor (1,5 %)
- Les projets déployés par des agents sont 20x plus susceptibles d'appeler des fournisseurs d'inférence IA
- "Les agents écrivent du logiciel qui utilise l'IA, et les agents construisent des agents"
- Le goulot d'étranglement pour les agents n'est plus l'intelligence mais l'environnement : cibles de déploiement propres, feedback rapide, systèmes observables
- Vercel identifie trois évolutions de l'infrastructure agentique : infrastructure pour les agents, infrastructure pour construire des agents, infrastructure elle-même agentique

## Analyse approfondie

### Chaque génération de logiciel exige une nouvelle infrastructure

L'article de Guillermo Rauch ouvre sur une perspective historique : les premières générations de logiciels nécessitaient des serveurs configurés manuellement, puis sont venus les cloud APIs, puis l'infrastructure définie par les frameworks (framework-defined infrastructure). Aujourd'hui, nous entrons dans une nouvelle ère — celle de l'infrastructure agentique (agentic infrastructure).

### Les chiffres qui témoignent du basculement

En l'espace de trois mois, les déploiements hebdomadaires sur Vercel ont doublé. Cette croissance est principalement portée par les agents. Plus de 30 % des déploiements proviennent désormais de coding agents, un chiffre en hausse de 1000 % sur six mois. Parmi ces agents, Claude Code domine avec 75 % des déploiements, suivi de Lovable et v0 à 6 %, et de Cursor à 1,5 %.

Un autre indicateur révélateur : les projets Vercel déployés par des agents sont 20 fois plus susceptibles d'appeler des fournisseurs d'inférence IA. Rauch résume cette dynamique par une formule frappante : "Agents are writing software that uses AI, and agents are building agents." Les agents écrivent du logiciel qui utilise l'IA, et les agents construisent des agents — une boucle récursive qui accélère l'adoption.

### Trois évolutions de l'infrastructure agentique

Rauch structure sa vision autour de trois niveaux d'évolution :

**1. Infrastructure sur laquelle les coding agents déploient.** Les preview URLs deviennent des boucles de feedback canoniques, et non plus de simples outils de QA humaine. L'agent déploie, observe le résultat via la preview URL, et itère — le tout sans intervention humaine. L'infrastructure doit donc offrir des cibles de déploiement propres et un retour rapide.

**2. Infrastructure pour construire et exécuter des agents.** Vercel met en avant son AI SDK et le concept de "fluid compute" — des fonctions serverless et des agents long-running cohabitant sur la même plateforme. L'idée est de permettre aux développeurs de construire des agents sans avoir à gérer l'orchestration de l'infrastructure sous-jacente.

**3. Infrastructure qui est elle-même agentique.** À ce stade, l'infrastructure ne se contente plus d'héberger des agents — elle devient agentique. Cela implique de l'observabilité avancée, de l'auto-diagnostic et de l'optimisation autonome. L'infrastructure anticipe les problèmes, se corrige et s'optimise sans attendre l'intervention d'un opérateur humain.

### Le vrai goulot d'étranglement : l'environnement, pas l'intelligence

L'une des thèses centrales de l'article est que le facteur limitant pour les agents n'est plus leur intelligence, mais leur environnement. Les agents ont besoin de cibles de déploiement propres (clean deploy targets), de feedback rapide et de systèmes observables. Sans ces éléments, même les agents les plus capables restent bloqués.

### Le positionnement de Vercel

Vercel se positionne explicitement comme une infrastructure "agentic-first" — construite pour un monde où l'acteur final qui déploie est de plus en plus souvent une machine. Ce n'est plus uniquement l'expérience développeur (DX) qui compte, mais aussi l'expérience agent (AX), la capacité de la plateforme à servir des agents autonomes comme citoyens de première classe.

## Pourquoi ça compte

Cet article de Vercel, appuyé par des données de production concrètes, illustre un basculement majeur : les coding agents ne sont plus une curiosité mais un vecteur de croissance dominant. Il pose les bases d'une nouvelle catégorie d'infrastructure où la plateforme doit être pensée autant pour les machines que pour les humains.
