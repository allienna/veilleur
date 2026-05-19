---
title: "The Workflow Collision"
date: 2026-05-19
url: https://webframp.com/posts/the-workflow-collision/?utm_source=tldrnewsletter
authors: [webframp]
keywords: [Kanban, agentic, workflow, trust, planning]
theme: IA
tone: opinion
used_in: ["2026-05-19"]
---

## Résumé

L'auteur décrit une tension structurelle que la plupart des équipes n'ont pas encore vue : le workflow humain (Kanban, pull-based, WIP, design sessions) et le lifecycle des agents IA (state machine, planification upfront, gates adversariales) reposent sur des théories de la confiance opposées. Le pull-based dit "trust the worker to choose well", l'agent dit "constrain the worker". Quand on plugue un agent dans une équipe sans nommer cette différence, on impose silencieusement un modèle qui s'oppose à celui qu'elle a construit.

## Points clés

- Le workflow humain (Kanban pull-based) repose sur la confiance dans les personnes pour s'auto-organiser
- Le lifecycle d'agent repose sur la contrainte via state machine et transitions vérifiées
- Le human-in-the-loop pour démarrer une tâche n'est pas une commodité — c'est une frontière de sécurité (l'issue body devient une attack surface sinon)
- Planning : juste-in-time côté humain, upfront et adversariel côté agent
- Les deux approches sont valides — mais incompatibles sur le même travail
- Le nombre d'états dans le workflow grandit dès qu'on injecte un agent

## Analyse approfondie

> Une collision arrive que la plupart des équipes n'ont pas encore remarquée.

D'un côté, le workflow que votre équipe utilise réellement. Si vous gérez une équipe plateforme ou opérationnelle, ça ressemble probablement à du Kanban : flux pull-based, WIP limits, design sessions avant implémentation, un petit nombre d'états que tout le monde comprend. Le workflow existe pour servir les personnes. Vous avez passé des années à l'affûter. Ça marche.

De l'autre côté, le lifecycle dont votre agent IA a besoin. Si vous utilisez un framework agentique — comme Swamp ou équivalent — l'agent opère à travers une state machine avec transitions imposées, planification upfront, gates de revue adversariale et checks qui empêchent physiquement de sauter des étapes. Le lifecycle existe pour contraindre l'agent. Ça marche.

Le problème, c'est qu'ils sont en désaccord sur presque tout ce qui compte.

### Là où ça collisionne

**Qui pilote le travail ?**

Un workflow Kanban mature est pull-based. Les membres de l'équipe terminent ce sur quoi ils travaillent, vérifient leur WIP limit, et pullent l'item le plus prioritaire de la ready queue. Personne n'assigne le travail. Le système fait confiance aux personnes pour s'auto-organiser.

Un agent lifecycle est operator-initiated. Un humain dit à l'agent de commencer à travailler sur une issue spécifique. L'agent ne peut pas prendre du travail tout seul — et pour de bonnes raisons. Si n'importe quel agent pouvait attraper n'importe quelle issue à l'instant où elle est filée, le corps de l'issue devient une *attack surface*. Imposer un opérateur dans la boucle est une frontière de sécurité.

Ce ne sont pas juste des mécaniques différentes. Elles reflètent des théories de la confiance différentes. Le pull-based dit : *faites confiance au worker pour bien choisir*. L'agent lifecycle dit : *contraignez le worker parce qu'il ne peut pas se faire confiance pour choisir du tout*.

**Comment fonctionne la planification ?**

Dans un workflow d'équipe, les design sessions sont des explorations collaboratives de l'espace du problème. Toute l'équipe pose des questions : Quels sont les risques ? Qu'est-ce qu'on ne sait pas ? Quelle est l'expérience la plus simple ? La valeur est dans l'enquête elle-même, pas dans la production d'un document. La planification se fait just-in-time, au bon niveau de détail, parce que les exigences changent et que les détails précoces sont du gaspillage.

Dans un agent lifecycle, l'agent génère un plan d'implémentation complet contre les conventions du repository, puis une revue adversariale le déchire selon des dimensions définies. L'humain relit le plan et donne soit du feedback, soit son approbation. La planification est une activité de production — l'agent écrit un plan, le système le valide, l'humain signe. L'implémentation est bloquée tant que le plan ne passe pas.

L'une dit : ne planifiez pas les détails trop tôt parce que le contexte va changer. L'autre dit : planifiez tout en amont parce que l'agent a besoin d'une spécification vérifiée pour exécuter. Les deux sont correctes pour leur contexte. **Elles sont incompatibles si on les applique au même travail.**

**Combien d'états il faut ?**

Un workflow Kanban bien conçu utilise un nombre minimal d'états — typiquement trois ou quatre — pour que le tableau reste compréhensible. L'agent lifecycle, lui, multiplie les états pour rendre les transitions explicites : draft, plan, plan-reviewed, implementing, awaiting-review, etc. Plus on injecte d'agents dans le système, plus le workflow se complexifie pour leurs besoins, pas pour ceux des humains.

### Implication pour le management

L'article ne propose pas une solution toute faite mais nomme la tension : un Engineering Director ne peut pas plugger un agent dans son équipe en pensant que c'est juste un nouvel outil. C'est un modèle de gouvernance opposé qui s'invite. Soit on adapte l'humain au pattern de l'agent (on perd l'auto-organisation), soit on adapte l'agent au pattern humain (on perd les garanties de sécurité), soit on bâtit explicitement deux mondes parallèles qui se rencontrent en quelques points clairs.

## Pourquoi ça compte

C'est l'article qui met enfin un mot précis sur le grincement qu'on ressent en intégrant des agents dans des équipes déjà matures. Au-delà de la productivité, ce qui se joue, c'est un changement de modèle de confiance organisationnelle. Indispensable pour quiconque rédige les guidelines d'usage des agents en équipe.
