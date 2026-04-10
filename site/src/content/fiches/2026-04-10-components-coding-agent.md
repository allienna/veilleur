---
title: "Components of A Coding Agent"
date: 2026-04-10
url: "https://link.mail.beehiiv.com/ss/c/u001.u7AEjFG7xD7PeXgObD5uI4TGUjHe7DXGFFmqNkCynUURnQgnu1U1lXxslVh48dbZZ9XpCCpHs1y0J0zv6GXcdNDbmnDS9LV_SgwPUqmDSTirsejyMqu8NrpfUStP_U67MBst4_5mTgd4ptpCx-YTzsH9uxUY11Suh0hLqwepsYRDSRhk4iQpJ-C_lHnzalCZLJ5Yse_6DnJcQ8gk6J8dJQ/4po/-Dh9L7oNQ_unt2XC4Tm6Wg/h14/h001.LL4yk1vPP9cll1A2N896LwCIdgn7WGhZkZSGYZ0llEU"
authors: ["Sebastian Raschka"]
keywords: [coding agent, LLM, agent harness, context management, agentic loop]
theme: "IA"
tone: "tutorial"
used_in: ["2026-04-10"]
---

## Résumé

Sebastian Raschka décortique les six composants fondamentaux d'un agent de code, en établissant une distinction claire entre le modèle LLM, le comportement de raisonnement et le produit agent. Il explique pourquoi des systèmes comme Claude Code ou Codex semblent bien plus capables que le même modèle utilisé en chat classique, grâce à l'ensemble du système qui les entoure. L'article propose une analogie mécanique éclairante et une décomposition méthodique qui permet de comprendre ce qui fait réellement la différence dans un agent de code.

## Points clés

- Un LLM est un modèle de prédiction du prochain token ; un modèle de raisonnement est un LLM entraîné à consacrer plus de calcul au moment de l'inférence ; un agent est une boucle de contrôle autour du modèle
- Le harness (harnais) de l'agent décide quoi inspecter, quels outils appeler, comment mettre à jour l'état et quand s'arrêter
- Analogie : le LLM est le moteur, le modèle de raisonnement est un moteur gonflé, le harness de l'agent est le véhicule complet
- Les gens confondent souvent modèle, comportement de raisonnement et produit agent — mais ce sont des couches distinctes
- Les six building blocks sont : le modèle, la gestion du contexte, l'utilisation d'outils, la mémoire, le prompt engineering et la boucle agentique
- Claude Code ou Codex paraissent plus capables que le même modèle en chat car tout le système environnant fait la différence

## Analyse approfondie

### Distinguer modèle, raisonnement et agent

Sebastian Raschka commence par poser une distinction fondamentale que beaucoup de praticiens négligent. Le **LLM** (Large Language Model) est le modèle de base — un prédicteur de prochain token entraîné sur de vastes corpus. Le **modèle de raisonnement** (reasoning model) est un LLM qui a été spécifiquement entraîné pour consommer davantage de calcul au moment de l'inférence (inference-time compute), lui permettant de décomposer des problèmes complexes étape par étape. L'**agent**, quant à lui, n'est pas un modèle : c'est une boucle de contrôle construite autour du modèle.

Cette distinction est cruciale car les gens ont tendance à tout fusionner — le modèle, le comportement de raisonnement et le produit agent — en une seule entité. Or ce sont des couches séparées, chacune avec ses responsabilités et ses leviers d'amélioration propres.

### Le harness : le vrai cerveau opérationnel

Le harness (harnais ou châssis) de l'agent est le composant qui orchestre tout. C'est lui qui décide :
- **Quoi inspecter** : quels fichiers lire, quelles parties du code examiner
- **Quels outils appeler** : éditeur de fichiers, terminal, recherche web, etc.
- **Comment mettre à jour l'état** : maintenir le contexte de la conversation, enregistrer les résultats intermédiaires
- **Quand s'arrêter** : déterminer que la tâche est terminée ou qu'il faut demander une clarification

### L'analogie mécanique

Raschka propose une analogie particulièrement parlante avec l'automobile :
- Le **LLM** est le **moteur** — il fournit la puissance brute de génération de texte
- Le **modèle de raisonnement** est un **moteur gonflé** (beefed-up engine) — plus de puissance de calcul, meilleure capacité à résoudre des problèmes complexes
- Le **harness de l'agent** est le **véhicule complet** — châssis, direction, transmission, freins, tout ce qui permet de transformer la puissance brute en déplacement utile

Un moteur seul, aussi puissant soit-il, ne mène nulle part. C'est l'ensemble du véhicule qui détermine l'expérience de conduite.

### Pourquoi Claude Code et Codex semblent plus capables

Un point central de l'article est l'explication de pourquoi des systèmes comme Claude Code ou Codex donnent l'impression d'être fondamentalement plus performants que le même modèle sous-jacent utilisé dans une interface de chat classique. La réponse ne tient pas au modèle lui-même, mais à tout le système qui l'entoure :

- **Le contexte du dépôt** (repo context) : l'agent a accès à l'ensemble du code source, comprend la structure du projet, peut naviguer entre les fichiers
- **La conception des outils** (tool design) : les outils mis à disposition sont pensés pour le développement — édition de fichiers, exécution de commandes, recherche dans le code
- **La stabilité du prompt cache** : les prompts système et le contexte sont mis en cache pour maintenir une cohérence tout au long de la session
- **La mémoire** : l'agent conserve le fil de la conversation et peut référencer des informations antérieures
- **La continuité des sessions longues** (long-session continuity) : contrairement au chat stateless, l'agent maintient un état riche sur la durée

### Les six building blocks

Raschka identifie et détaille les six composants essentiels d'un agent de code :

1. **Le modèle lui-même** — La fondation. Le choix du LLM (sa taille, ses capacités de raisonnement, sa fenêtre de contexte) définit le plancher de performance de l'agent. Un meilleur moteur permet un meilleur véhicule, mais ne suffit pas.

2. **La gestion du contexte** (context management) — Comment l'agent accède et organise l'information. Cela inclut la lecture du contexte du dépôt (repo context), la lecture de fichiers, la compréhension de la structure du projet. Un agent qui sait quels fichiers lire et quand les lire sera vastement plus efficace qu'un agent qui travaille à l'aveugle.

3. **L'utilisation d'outils** (tool use) — Les capacités d'action de l'agent dans le monde réel. Cela comprend l'édition de fichiers, l'exécution de commandes dans le terminal, la recherche web, et tout autre outil mis à sa disposition. La qualité de la conception des outils (ergonomie, fiabilité, documentation) influence directement la performance de l'agent.

4. **La mémoire** (memory) — Deux types coexistent. La mémoire **à court terme** (short-term, in-session) correspond au contexte de la conversation en cours — ce qui a été dit, fait et décidé durant la session. La mémoire **à long terme** (long-term, cross-session) persiste entre les sessions et permet à l'agent de se souvenir des préférences, des décisions architecturales et des conventions du projet.

5. **Le prompt engineering et les prompts système** — L'art de formuler les instructions qui guident le comportement de l'agent. Les prompts système définissent le rôle, les contraintes et le style de l'agent. Un même modèle peut se comporter de façon radicalement différente selon la qualité de ses prompts.

6. **La boucle agentique** (agentic loop) — Le cycle planification-exécution-vérification qui structure le travail de l'agent. L'agent planifie une approche, exécute des actions via ses outils, vérifie les résultats, puis ajuste son plan. C'est cette boucle itérative qui permet à l'agent de gérer des tâches complexes que le modèle seul ne pourrait pas accomplir en une seule passe.

### Implications pour la conception d'agents

L'analyse de Raschka a des implications pratiques directes. Améliorer un agent de code ne se réduit pas à changer le modèle sous-jacent pour un modèle plus puissant. Chacun des six building blocks est un levier d'amélioration indépendant. Une meilleure gestion du contexte, des outils mieux conçus, une mémoire plus riche ou une boucle agentique plus sophistiquée peuvent avoir un impact aussi significatif — voire plus — qu'un upgrade du modèle.

## Pourquoi ça compte

Cette décomposition méthodique des agents de code tombe à point nommé alors que les coding agents deviennent des outils quotidiens pour les développeurs. Comprendre que la valeur réside dans le système complet — et pas seulement dans le modèle — permet de mieux évaluer, comparer et construire ces outils, et rappelle que l'ingénierie logicielle autour du modèle reste un différenciateur majeur.
