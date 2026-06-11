---
title: "The evolution of agentic surfaces: building with Claude Managed Agents"
date: 2026-06-11
url: https://claude.com/blog/building-with-claude-managed-agents?utm_source=tldrai
authors: [anthropic.com]
keywords: [agents, production, infrastructure, API, Claude]
theme: IA
tone: news
used_in: ["2026-06-11"]
---

## Résumé

Anthropic présente Claude Managed Agents, une suite d'APIs composables pour construire et déployer des agents en production. L'article retrace l'évolution de l'architecture agentique d'Anthropic — du simple tokens in/tokens out à des systèmes multi-agents avec infrastructure gérée. La thèse : l'infrastructure (sécurité, state management, permissioning, observabilité) est ce qui sépare un prototype d'un agent en production, et les équipes brûlent trop de cycles sur ce harnais avant d'adresser leur cas d'usage.

## Points clés

- L'infrastructure est le principal goulot d'étranglement entre prototype et agent en production
- Claude Managed Agents fournit un harnais pré-optimisé pour la performance + infrastructure de production
- Passage possible du prototype au lancement en jours plutôt qu'en mois
- L'évolution part du simple API (tokens in/tokens out) vers des systèmes avec boucles d'exécution, sous-agents, gestion du contexte
- Claude Code a servi de terrain d'expérimentation interne pour cette architecture avant sa mise à disposition externe

## Analyse approfondie

### Le problème à résoudre

Faire fonctionner un agent en production exige plus qu'un bon prompt. L'agent a besoin d'un endroit pour exécuter le code qu'il écrit, des credentials pour accéder aux données, des sessions observables, et une infrastructure qui s'adapte à l'usage. L'équipe Applied AI d'Anthropic observe le même pattern en permanence : l'infrastructure est ce qui sépare un prototype d'un agent en production. Trop souvent, les équipes brûlent des cycles de développement sur la sécurité, la gestion du state, les permissions et le tuning du harnais.

Claude Managed Agents, leur suite d'APIs composables pour construire et déployer des agents de niveau production, couple un harnais d'agent optimisé pour la performance avec une infrastructure de production — permettant aux équipes de passer du prototype au lancement en jours plutôt qu'en mois.

### L'évolution de l'architecture

Quand Anthropic a ouvert Claude aux développeurs en 2023, l'API était délibérément simple : tokens en entrée, tokens en sortie. On envoyait un prompt, Claude retournait une complétion, et on construisait le harnais et l'infrastructure sous-jacente.

L'API s'est régulièrement enrichie au fil des années, mais le contrat en dessous n'a jamais changé : une requête, un tour de modèle, et l'application décide de la suite. Pendant longtemps, c'était suffisant pour résumer un document, classifier un ticket de support, réécrire un bloc de texte — le type de travail qui tient dans un seul tour.

Progressivement, cependant, les tâches que les gens voulaient déléguer ont cessé de tenir dans ce cadre. Ils voulaient que Claude porte une tâche jusqu'au bout, cherche quelque chose, agisse dessus, observe ce qui avait changé, et décide quoi faire ensuite. Et ils voulaient que Claude opère *dans* les systèmes sur lesquels leur travail tournait déjà — une codebase, un wiki interne, un système de tickets.

Avec l'API seule, transformer Claude en agent signifiait construire sa propre boucle : demander au modèle quoi faire, exécuter l'outil, réinjecter le résultat, et recommencer. On était responsable de construire et déployer l'échafaudage de l'agent, qui pouvait nécessiter un tuning au fur et à mesure de l'évolution des modèles.

### Claude Code comme laboratoire

Claude Code, l'outil de codage agentique qu'Anthropic a lancé en 2025 et qui permet à Claude d'interagir directement avec une codebase, contenait leur propre version de ce harnais : la boucle, l'exécution des outils, les sous-agents, la gestion du contexte. En travaillant avec Claude Code comme produit, l'équipe a appris ce qui compte réellement pour les workflows agentiques en production, et a commencé à distiller ces apprentissages en primitives réutilisables.

### L'architecture Claude Managed Agents

Claude Managed Agents est aujourd'hui une suite composable :

- **Files API** : stockage persistant de fichiers entre les sessions de l'agent
- **Shell tool** : exécution de code et de commandes dans un environnement sécurisé
- **Code execution** : sandbox isolé pour l'exécution de code avec gestion des dépendances
- **Managed sessions** : état persistant, observabilité et reprise des sessions longues
- **Permissions framework** : contrôle fin de ce à quoi l'agent peut accéder

Les équipes peuvent adopter ces composants individuellement ou en combinaison selon leurs besoins.

### Cas d'usage en production

Des équipes utilisent déjà Claude Managed Agents pour des workflows comme la migration de code à grande échelle, l'analyse de sécurité automatisée, ou le traitement de données complexes qui nécessitent plusieurs étapes et des décisions basées sur les résultats intermédiaires.

## Pourquoi ça compte

Cette annonce représente la maturité de l'offre agentique d'Anthropic : plutôt que de laisser chaque équipe réinventer le même harnais d'infrastructure, ils proposent une couche standard qui permet de se concentrer sur la logique métier. C'est un signal fort que l'ère des agents en production est arrivée, avec l'infrastructure qui va avec.
