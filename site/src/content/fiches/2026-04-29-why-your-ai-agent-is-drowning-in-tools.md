---
title: "Why Your AI Agent Is Drowning in Tools (And How Code Mode Saves It)"
date: 2026-04-29
url: https://engineering.leanix.net/blog/code-mode/
authors: [LeanIX Engineering]
keywords: [MCP, Code Mode, tool design, contexte, hallucination]
theme: IA
tone: tutorial
used_in: ["2026-04-29"]
---

## Résumé

L'article décrit deux problèmes critiques quand on branche trop d'outils MCP à un agent : le bloat de la fenêtre de contexte (5 à 7 % consommé avant le premier message utilisateur) et l'hallucination d'outils (le LLM invente des noms ou mélange les paramètres). Trois solutions sont explorées : la réduction (côté agent ou côté MCP), et surtout "Code Mode" — où l'agent écrit du code pour orchestrer les appels au lieu d'invoquer chaque outil individuellement.

## Points clés

- À 50+ tools branchés, 5 à 7 % du contexte est mangé avant même le premier message utilisateur.
- Trop d'outils sémantiquement similaires => hallucinations : noms inventés, paramètres mélangés entre outils.
- Solution 1 : agent-side filtering — curer manuellement les outils avant de les passer au LLM.
- Solution 2 : MCP-side reduction — éviter de wrapper chaque endpoint REST en outil, raisonner par cas d'usage.
- Solution 3 : Code Mode — laisser l'agent écrire du code qui appelle les APIs, plus expressif et moins bavard.

## Analyse approfondie

Imagine que tu utilises plusieurs serveurs MCP au travail. En tant que développeur, tu peux brancher un MCP Figma, un MCP Context7 ou un MCP Jira sur ton agent, ce qui te permet d'exploiter des outils via le langage naturel. Ça paraît parfait, non ?

Mais tu as probablement déjà heurté le mur : trop d'outils inondent la fenêtre de contexte de ton LLM.

Cela crée deux problèmes critiques. Premièrement, **le bloat de la fenêtre de contexte**. Chaque nom d'outil, chaque description, chaque schéma de paramètres consomme des tokens à chaque requête. À 50+ outils, cela peut manger 5 à 7 % du contexte du modèle avant même qu'un message utilisateur n'arrive, repoussant l'historique de conversation, le contenu des documents, et l'espace de raisonnement.

Deuxièmement, **l'hallucination d'outils**. Quand tu as trop d'outils sémantiquement similaires, le LLM se met à inventer des noms d'outils qui n'existent pas, à confondre des paramètres entre outils, ou à appeler le bon outil avec des arguments tirés du schéma d'un autre outil.

Alors, comment résoudre ça ?

### Solution 1 : la réduction d'outils

L'approche la plus directe est de réduire le nombre d'outils. Tu peux le faire de deux façons : limiter ce que voit l'agent IA, ou réduire le nombre d'outils côté MCP.

**Filtrage côté agent.** Avec cette approche, tu définis un set curé d'outils qui résolvent le problème spécifique auquel ton agent IA est confronté. Tu demandes la liste complète des outils au MCP, puis tu la filtres avant de la passer au LLM. Moins d'outils, c'est moins de contexte consommé.

Avantages : très transparent (chaque appel et argument est visible et facile à debugger), simple à implémenter (suis la spec MCP et c'est fait).

Inconvénients : bloat persiste pour les grosses APIs (centaines/milliers d'endpoints), aller-retours nombreux pour les workflows multi-étapes, contrôle de flux complexe maladroit (boucles, retries, branches s'expriment mal en invocations individuelles), évaluation continue nécessaire pour les nouveaux outils.

**Réduction côté MCP.** Si tu possèdes le serveur MCP, tu peux réduire les outils à la source. Ne wrappe pas chaque appel d'API REST en outil. Réfléchis aux cas d'usage que tu cherches à résoudre. Un cas d'usage peut combiner deux APIs, ou wrapper un seul appel API avec une logique métier dédiée.

## Pourquoi ça compte

Cet article met le doigt sur une faille opérationnelle majeure de l'écosystème agents : à force d'empiler les MCP, on dégrade le comportement même qu'on cherche à améliorer. Le pattern "Code Mode" est un signal architectural clé pour 2026.
