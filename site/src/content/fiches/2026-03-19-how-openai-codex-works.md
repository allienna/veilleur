---
title: "How OpenAI Codex Works"
date: 2026-03-19
url: https://blog.bytebytego.com/p/how-openai-codex-works
authors: [ByteByteGo]
keywords: [OpenAI, Codex, agent, architecture, orchestration, MCP]
theme: IA
tone: tutorial
used_in: ["2026-03-19"]
---

## Résumé

ByteByteGo détaille l'architecture technique de Codex, l'agent de code cloud d'OpenAI. Le système repose sur trois couches : une boucle agentique (agent loop), un système de gestion du prompt et du contexte assemblé depuis cinq sources différentes, et une architecture multi-surface qui permet à un même agent de fonctionner dans VS Code, le terminal et le navigateur. L'équipe a abandonné MCP au profit d'un protocole propriétaire pour gérer les interactions complexes.

## Points clés

- Codex utilise codex-1, une version d'o3 fine-tunée pour l'ingénierie logicielle
- Le prompt est assemblé dynamiquement depuis 5 sources : instructions système, mémoire de conversation, contexte du repo, résultats d'outils, et instructions utilisateur
- Quand la conversation dépasse la fenêtre de contexte, un mécanisme de résumé compresse l'historique
- MCP a été abandonné car il ne supportait pas le streaming, l'approbation mid-task et les diffs de code
- Un protocole propriétaire a été construit from scratch pour piloter l'agent sur plusieurs surfaces
- Chaque tâche tourne dans une sandbox cloud isolée préchargée avec le repo

## Analyse approfondie

### Le modèle n'est qu'un composant

Quand OpenAI a livré Codex, les problèmes d'ingénierie les plus difficiles n'avaient presque rien à voir avec le modèle d'IA lui-même. Le modèle codex-1 est une version d'o3 (le modèle de raisonnement d'OpenAI) fine-tunée pour l'ingénierie logicielle. Il est important, mais ce n'est qu'un composant dans un système beaucoup plus large. Le vrai travail d'ingénierie a porté sur tout ce qui l'entoure.

Comment assemble-t-on le bon prompt à partir de cinq sources différentes ? Que se passe-t-il quand l'historique de conversation devient si volumineux qu'il menace de dépasser la mémoire du modèle ? Comment faire fonctionner le même agent dans un terminal, un navigateur web et trois IDEs différents sans le réécrire à chaque fois ?

### La boucle agentique

Le cœur de Codex est une boucle d'exécution où le modèle pense, agit, observe, puis recommence. À chaque itération, le modèle reçoit un prompt, décide d'utiliser un outil (exécuter une commande, lire un fichier, écrire du code) ou de répondre à l'utilisateur. S'il utilise un outil, le résultat est ajouté à la conversation et la boucle continue.

Cette boucle est supervisée. Certaines actions (comme l'exécution de commandes shell ou la modification de fichiers en dehors du dépôt) déclenchent des points d'approbation où l'utilisateur doit valider avant que l'agent ne continue.

### La gestion du contexte

Le prompt envoyé au modèle à chaque tour de boucle est assemblé dynamiquement à partir de cinq sources :

1. **Instructions système** : les règles de base sur le comportement de l'agent
2. **Mémoire de conversation** : l'historique des échanges précédents
3. **Contexte du dépôt** : les fichiers pertinents du codebase, sélectionnés par recherche sémantique ou par parcours de l'arbre de fichiers
4. **Résultats d'outils** : les sorties des commandes exécutées précédemment
5. **Instructions utilisateur** : la demande courante et les préférences

Quand la conversation grandit au point de menacer de dépasser la fenêtre de contexte du modèle, un mécanisme de résumé entre en jeu. Plutôt que de simplement tronquer l'historique (ce qui ferait perdre des informations critiques), le système compresse les échanges précédents en un résumé qui préserve les décisions clés et l'état courant du travail.

### L'échec de MCP et le protocole propriétaire

Quand l'équipe Codex a voulu intégrer l'agent dans VS Code, elle a d'abord essayé l'approche évidente : l'exposer via MCP (Model Context Protocol), le standard émergent pour connecter les modèles d'IA aux outils. Ça n'a pas fonctionné.

Les patterns d'interaction riches dont un vrai agent a besoin — streaming de la progression en temps réel, pause en milieu de tâche pour obtenir l'approbation de l'utilisateur, émission de diffs de code — ne correspondaient pas à ce que MCP offrait. Le protocole MCP est conçu pour des interactions requête-réponse relativement simples, pas pour le type de communication bidirectionnelle et continue qu'un agent de code nécessite.

L'équipe a donc construit un nouveau protocole from scratch, spécifiquement conçu pour les besoins des agents de code. Ce protocole supporte :

- Le streaming natif de la progression
- Les points d'arrêt pour approbation humaine
- L'émission de diffs de code structurés
- La synchronisation d'état entre l'agent et l'IDE

### L'architecture multi-surface

Ce protocole a permis de résoudre le problème de la multi-surface : un même agent, une même logique, accessible depuis VS Code, le terminal web, le navigateur et potentiellement d'autres IDEs. Chaque surface implémente le même protocole, ce qui évite de devoir réécrire la logique de l'agent pour chaque environnement.

Chaque tâche soumise à Codex tourne dans sa propre sandbox cloud isolée, préchargée avec une copie du dépôt de l'utilisateur. Plusieurs tâches peuvent être exécutées en parallèle, et l'utilisateur peut suivre la progression en temps réel.

## Pourquoi ça compte

Cet article révèle que les défis majeurs des agents de code ne sont pas dans le modèle d'IA mais dans l'orchestration qui l'entoure. L'abandon de MCP au profit d'un protocole propriétaire est un signal fort : les standards actuels ne sont pas encore à la hauteur des besoins réels des agents de code en production. C'est un aperçu de la couche d'infrastructure qui va définir la prochaine génération d'outils de développement.
