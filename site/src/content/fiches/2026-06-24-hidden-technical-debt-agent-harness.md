---
title: "Hidden Technical Debt of AI Systems: Agent Harness"
date: 2026-06-24
url: https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/?utm_source=tldrdev
authors: [Lee Han Chung, leehanchung.github.io]
keywords: [agent harness, technical debt, orchestration, MCP, production agents]
theme: IA
tone: opinion
used_in: ["2026-06-24"]
---

## Résumé

Lee Han Chung analyse le *harness* d'agent — la couche d'orchestration entre le modèle et son environnement (system prompts, outils, boucles, retry, compaction de contexte, juges, allowlists) — comme une dette technique cachée que peu d'équipes budgètent. Sa thèse : une grande partie de ce code va se dissoudre dans la prochaine génération de modèles, et les équipes qui traitent leur harness comme une surface produit permanente passeront un an à l'arracher. Il distingue harness interne (livré par le constructeur du modèle) et harness externe (assemblé par l'utilisateur), et oppose le harness de production (surface de contrainte) au harness d'entraînement.

## Points clés

- Le harness est le « système d'exploitation » de l'agent : le modèle est le CPU, le harness orchestre instructions, outils, mémoire et donne l'illusion de ressources infinies.
- Composants du harness : system prompt, surface d'outils, protocole de rollout, gestionnaire de contexte, mémoire, topologie de sous-agents, guardrails, vérificateurs/juges, observabilité.
- Distinction de Birgitta Böckeler : harness *interne* (Claude Agent SDK, Cursor Auto, Codex app server) vs harness *externe* (AGENTS.md, serveurs MCP, skills, agents de revue). Ils évoluent à des rythmes différents et accumulent des dettes différentes.
- OpenAI rapporte que ses défis les plus durs sont devenus « concevoir des environnements, des boucles de feedback et des systèmes de contrôle » plutôt qu'écrire du code applicatif.
- En production, le harness est une surface de contrainte : moindre privilège, deny par défaut, credentials scopés, paliers d'approbation, filtres anti prompt injection, retry idempotent, runtime max, log d'audit, kill switch.
- La vraie question : quelles parties du harness sont *porteuses*, et lesquelles ne sont que l'échafaudage nécessaire au niveau actuel de capacité des modèles ?

## Analyse approfondie

Si vous construisez des produits agentiques depuis douze mois, vous écrivez du code de harness : system prompts, wrappers d'outils, boucles planificateur-exécuteur, politiques de retry, stratégies de compaction de contexte, allowlists précisant quels outils un agent peut appeler depuis quelle surface, juges pour décider quand s'arrêter, et fallbacks pour quand le modèle dérive. Même dessiner des workflows dans des outils no-code/low-code comme n8n est du travail de harness. Toutes les équipes en ont construit. Les bonnes équipes en ont construit beaucoup. La partie amère : presque tout cela va se dissoudre dans la prochaine génération de modèles, et les équipes qui traitent leur harness comme une surface produit permanente passeront un an à l'arracher.

Cet article zoome sur l'agent IA lui-même et pose la question restée sans réponse à travers tous les billets sur l'ingénierie de harness des six derniers mois : quelles parties sont porteuses, et lesquelles ne sont que la structure dont nous avions besoin à ce niveau précis de capacité des modèles ?

On définit le harness d'agent comme la couche d'orchestration entre le modèle et les environnements dans lesquels il opère. Cela inclut les system prompts, des ensembles d'outils de base — accès terminal (bash), accès au système de fichiers (lecture, écriture) — et potentiellement un client MCP pour accéder à des serveurs MCP contenant des outils. Un agent est alors un harness + un modèle de fondation.

Une analogie utile : traiter l'IA comme la prochaine génération d'informatique. L'intelligence centrale est dans le modèle, ou le CPU d'un ordinateur. Et le modèle seul n'est pas utile sans système d'exploitation pour orchestrer instructions et outils. Le harness est le système d'exploitation : il fournit les interruptions et les interfaces vers le monde extérieur, gère processus et threads, et gère la mémoire (le contexte du modèle) pour donner à l'utilisateur l'illusion d'une mémoire et de ressources infinies.

### Décomposition d'un harness

Un harness peut être l'union de :

- **System prompt et persona** — les instructions permanentes qui biaisent le comportement du modèle à chaque tour.
- **Surface d'outils** — l'ensemble des fonctions appelables exposées au modèle, et les schémas, descriptions et exemples qui lui apprennent à les utiliser.
- **Protocole de rollout** — single-turn, multi-turn, ReAct, plan-and-execute, deep-research, multi-agent. La forme de la boucle dans laquelle le modèle s'exécute.
- **Gestionnaire de contexte** — ce qui est transporté entre les tours, ce qui est compacté, résumé, abandonné.
- **Mémoire** — brouillons court terme, fichiers de progrès moyen terme, stores récupérables long terme.
- **Topologie de sous-agents** — orchestrateur, workers, juges, sous-skills, protocoles de hand-off.
- **Guardrails et gates** — filtres d'entrée et de sortie, gates d'action, allowlists, paliers d'approbation, KL caps à l'entraînement, lignes rouges comportementales en production.
- **Vérificateurs et juges** — ce qui décide si une étape a réussi, si un plan doit continuer, si le modèle doit s'arrêter.
- **Observabilité** — traces, replay, hooks d'éval, les coutures que l'humain peut saisir pour comprendre ce qui s'est passé.

Tous les harnais ne se valent pas : certains sont minimalistes (pi), d'autres complets (Claude Code). Certains visent les agents personnels locaux (OpenClaw), d'autres la mémoire (Letta code), d'autres l'inférence récursive à long contexte (Recursive Language Models), d'autres la collaboration massive multi-agent (Gas Town). En tant que couche système d'exploitation de l'IA, c'est exactement comme les multiples distributions Linux pour tous les cas d'usage imaginables.

### Autres définitions du harness d'agent

Nommer les choses est le problème le plus dur de l'informatique, et la définition du harness ne fait pas exception. Prenons l'analogie d'une équipe de F1 : les labos IA construisent le moteur (le modèle agentique) ; il faut une équipe de mécaniciens pour construire le harness et la coque ; et il faut évaluer et optimiser la voiture pour avoir une chance de gagner. La star du spectacle, c'est le pilote — l'utilisateur du modèle. Il personnalise la voiture, sa combinaison, son casque, ses porte-bonheur : c'est le second type de harness.

L'article de Birgitta Böckeler établit une distinction nette. Il y a un harness *interne* livré par le constructeur du modèle — Claude Agent SDK d'Anthropic, Auto de Cursor, app server de Codex. Et un harness *externe* que l'utilisateur assemble par-dessus — `AGENTS.md`, serveurs MCP, skills personnalisés, agents de revue de code spécifiques à l'organisation. Les deux sont du harness. Ils évoluent à des horloges différentes et accumulent des dettes différentes.

L'équipe d'OpenAI a décrit son travail interne de harness en disant que ses défis les plus durs étaient devenus « concevoir des environnements, des boucles de feedback et des systèmes de contrôle » plutôt qu'écrire du code applicatif. Le billet d'Anthropic sur les harnais efficaces pour agents longue durée en est un exemple concret : un harness à deux prompts avec un agent initialiseur qui construit un `init.sh`, un `claude-progress.txt`, une liste de features structurée en JSON, et un agent de code qui prend la prochaine feature en échec, commit, met à jour le fichier de progrès et s'arrête. Le harness n'est pas le modèle. Le harness n'est pas non plus de la simple plomberie. C'est une boucle de feedback délibérément conçue qui transforme un appel de modèle en travail utile sur un horizon plus long que n'importe quelle fenêtre de contexte.

### De la recherche à la production

La propriété la plus sous-discutée du harness : le harness de production et le harness d'entraînement ne sont pas le même artefact, et de plus en plus ne devraient pas l'être.

En production, le harness est une surface de contrainte. L'agent agit pour le compte d'un utilisateur, contre des systèmes réels, avec des conséquences réelles. On veut une allowlist d'outils serrée, des credentials scopés, des paliers d'approbation pour les actions d'écriture, des filtres d'entrée et de sortie contre le prompt injection, une politique de retry idempotente, un runtime maximum, un log d'audit, un kill switch. Comme le note Ashpreet Bedi, l'accès en lecture seule est une configuration d'outil, pas une instruction de system prompt. Les bons défauts ressemblent au déploiement prudent d'un processus puissant mais fondamentalement non fiable : principe de moindre privilège, deny par défaut, tout observer.

## Pourquoi ça compte

Ce texte met un nom — et un budget — sur une dette technique que la plupart des équipes IA ignorent. Il donne un cadre concret pour distinguer ce qui est porteur de ce qui est jetable dans une architecture agentique, ce qui est vital pour piloter des investissements d'ingénierie en 2026.
