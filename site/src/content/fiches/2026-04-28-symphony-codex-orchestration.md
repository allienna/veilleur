---
title: "An open-source spec for Codex orchestration: Symphony"
date: 2026-04-28
url: "https://links.tldrnewsletter.com/fp0tkz"
authors: ["OpenAI", "Alex Kotliarskyi", "Victor Zhu", "Zach Brock"]
keywords: [Symphony, Codex, agent orchestration, Linear, autonomous agents]
theme: "IA"
tone: "news"
used_in: ["2026-04-28"]
---

## Résumé

OpenAI a publié Symphony, un orchestrateur open-source qui transforme un board de gestion de projet comme Linear en plan de contrôle pour agents Codex. Plutôt que de gérer manuellement 3 à 5 sessions Codex en parallèle, l'humain ne fait plus que reviewer les PR sortantes. Sur certaines équipes OpenAI, cela a multiplié par 5 le nombre de PR mergées en trois semaines, et change fondamentalement comment les équipes pensent leur travail.

## Points clés

- Le bottleneck n'est plus l'agent mais l'attention humaine : 3 à 5 sessions Codex en parallèle est le plafond avant que le context-switching ne fasse chuter la productivité
- Symphony décale la primitive de "session de coding" vers "ticket / unité de travail livrable"
- Chaque issue Linear ouverte se voit assigner un agent qui tourne en continu jusqu'à complétion
- +500 % de PR mergées dans certaines équipes en trois semaines
- Les agents peuvent eux-mêmes créer des issues quand ils repèrent des opportunités d'amélioration en cours de route
- Symphony brille particulièrement dans les gros monorepos où le dernier mile (CI, rebases, conflits) est lent et fragile
- Toutes les tâches ne s'y prêtent pas : les problèmes ambigus restent du ressort des sessions interactives

## Analyse approfondie

### Le plafond des agents de coding interactifs

Même s'ils sont devenus plus faciles à utiliser, les agents de coding — qu'ils soient accessibles via web ou CLI — restent des outils interactifs. À mesure que l'échelle du travail agentique augmentait chez OpenAI, l'équipe a découvert un nouveau type de fardeau. Chaque ingénieur ouvrait quelques sessions Codex, assignait des tâches, reviewait les outputs, dirigeait l'agent, et recommençait. En pratique, la plupart des gens géraient confortablement 3 à 5 sessions à la fois avant que le context-switching ne devienne douloureux. Au-delà, la productivité chutait. On oubliait quelle session faisait quoi, on jonglait entre terminaux pour remettre les agents sur les rails, et on debuggait des tâches longues qui s'étaient bloquées à mi-parcours.

Les agents étaient rapides, mais le système avait un bottleneck : l'attention humaine. L'équipe avait construit une équipe d'ingénieurs juniors extrêmement capables, puis assigné les ingénieurs humains à les micromanager. Ça n'allait pas scaler.

### Un changement de perspective

L'équipe a réalisé qu'elle optimisait la mauvaise chose. Elle organisait son système autour des sessions de coding et des PR mergées, alors que les PR et les sessions sont des moyens, pas une fin. Les workflows software sont largement organisés autour de livrables : issues, tâches, tickets, milestones.

Alors elle s'est demandé : et si on arrêtait de superviser les agents directement et qu'on les laissait pull leur travail depuis le task tracker ?

Cette idée est devenue Symphony, une spec écrite qui fonctionne comme superviseur pour orchestrer le travail agentique.

### Transformer l'issue tracker en orchestrateur d'agents

Symphony part d'un concept simple : toute tâche ouverte doit être prise en charge et complétée par un agent. Au lieu de gérer des sessions Codex dans plusieurs onglets, l'issue tracker devient le plan de contrôle.

Dans cette configuration, chaque issue Linear ouverte est mappée à un workspace agent dédié. Symphony surveille en continu le board de tâches et s'assure que chaque tâche active a un agent en boucle jusqu'à complétion. Si un agent crashe ou stalle, Symphony le redémarre. Si du nouveau travail apparaît, Symphony le récupère et commence à organiser le travail.

L'équipe a construit son workflow basé sur des statuts de tickets, en utilisant Linear comme une state machine.

> Une fois le travail abstrait de cette façon, les tickets peuvent représenter des unités de travail beaucoup plus larges.

L'équipe utilise régulièrement Symphony pour orchestrer des features complexes et des migrations d'infrastructure. Par exemple, elle peut filer une tâche demandant à l'agent d'analyser le codebase, Slack, ou Notion et de produire un plan d'implémentation. Une fois le plan validé, l'agent génère un arbre de tâches, découpant le travail en étapes et définissant les dépendances entre tâches.

Les agents ne commencent à travailler que sur les tâches non bloquées, donc l'exécution se déroule naturellement et optimalement en parallèle pour ce DAG. Par exemple, l'équipe a marqué l'upgrade de React comme bloqué sur la migration vers Vite. Comme prévu, les agents ont commencé à upgrader React seulement après que la migration vers Vite soit terminée.

### Les agents créent eux-mêmes du travail

Les agents peuvent aussi créer du travail eux-mêmes. Pendant l'implémentation ou la review, ils remarquent souvent des améliorations qui sortent du scope de la tâche actuelle : un problème de performance, une opportunité de refactoring, une meilleure architecture. Quand cela arrive, ils filent simplement une nouvelle issue qu'on peut évaluer et planifier plus tard — beaucoup de ces tâches de suivi sont aussi reprises par des agents.

Cette façon de travailler réduit drastiquement le coût cognitif de lancer du travail ambigu. Si l'agent se trompe, c'est encore une information utile, et le coût pour nous est proche de zéro. On peut très bon marché filer des tickets pour que l'agent prototype et explore, et jeter les explorations qu'on n'aime pas.

### Une augmentation massive de l'output et de l'exploration

En observant les effets de travailler avec Symphony, le changement le plus évident a été l'output. Parmi certaines équipes chez OpenAI, le nombre de PR mergées a augmenté de 500 % dans les trois premières semaines. Hors d'OpenAI, le fondateur de Linear Karri Saarinen a mis en lumière un pic de workspaces créés à mesure que Symphony était libéré.

Mais le shift plus profond est dans la façon dont les équipes pensent le travail. Quand les ingénieurs ne passent plus de temps à superviser des sessions Codex, l'économie du changement de code change complètement. Le coût perçu de chaque changement chute parce qu'on n'investit plus d'effort humain dans la conduite de l'implémentation elle-même.

Ça a changé les comportements. Il est devenu trivial de créer des tâches spéculatives dans Symphony. Tester une idée, explorer un refactor, tester une hypothèse, et ne garder que les résultats prometteurs.

Ça élargit aussi qui peut initier du travail. Le product manager et le designer peuvent désormais déposer des feature requests directement dans Symphony. Ils n'ont pas besoin de checkout le repo ou de gérer une session Codex. Ils décrivent la feature et reçoivent un review packet qui inclut un walkthrough vidéo de la feature qui marche dans le vrai produit.

Symphony brille aussi dans les gros monorepos (comme celui qu'a OpenAI) où le dernier mile pour lander une PR est lent et fragile. Le système surveille la CI, rebase au besoin, résout les conflits, retry les checks flaky, et globalement chaperonne les changements à travers la pipeline. Au moment où un ticket atteint le statut **Merging**, on a haute confiance que le changement va finir dans la branche main sans babysitting humain.

### Les nouveaux problèmes

Opérer à ce niveau vient avec des tradeoffs. Quand on est passés de diriger les agents de manière interactive à leur assigner du travail au niveau ticket, on a perdu la capacité de constamment les nudger en plein vol et de les corriger en route. Parfois l'agent produit quelque chose qui rate complètement la cible. C'était utile — ces échecs ont révélé des trous dans le système et nous ont aidés à le rendre plus robuste.

Au lieu de patcher le résultat manuellement, on a ajouté des garde-fous et des skills pour que les agents puissent réussir la fois suivante. Avec le temps, cela nous a poussés à ajouter de nouvelles capacités à notre harness, comme lancer des tests end-to-end, piloter l'app via Chrome DevTools, et gérer des smoke tests QA. On a significativement amélioré notre documentation et clarifié à quoi ressemble le bon.

Toutes les tâches ne se prêtent pas au style Symphony. Certains problèmes nécessitent encore des ingénieurs travaillant directement avec des sessions Codex interactives, surtout les problèmes ambigus ou le travail qui requiert un fort jugement et de l'expertise. En pratique, ce sont généralement les tâches les plus intéressantes et les plus agréables sur lesquelles passer du temps.

La différence est que Symphony peut absorber le gros du travail d'implémentation routinier. Cela permet aux ingénieurs de se concentrer sur un seul problème difficile à la fois.

## Pourquoi ça compte

Symphony marque une étape importante : la primitive de l'agentique cesse d'être la "session de coding" et devient le "ticket". C'est exactement le saut qu'attendait l'industrie pour passer de l'IA assistante à l'IA autonome encadrée. Les équipes qui comprendront vite ce changement de perspective vont creuser un écart de productivité massif.
