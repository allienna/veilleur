---
title: "/goal: The Six-Hour Codex Run That Survived a Five-Hour Pause"
date: 2026-05-08
url: https://tectontide.com/en/blog/codex-goal-six-hour-run/?utm_source=tldrai
authors: [tectontide.com]
keywords: [Codex, agents, persistence, autonomy, /goal]
theme: IA
tone: opinion
used_in: ["2026-05-08"]
---

## Résumé

Codex CLI v0.128.0 a livré le 30 avril 2026 une nouvelle commande `/goal` qui persiste l'état d'un agent au-delà des sessions, des reboots et des fermetures de laptop. L'auteur raconte avoir lancé une session à 21h19, fermé son ordinateur, et constaté le lendemain matin que l'agent avait repris seul son travail. Au total : 6h44 de wall time, 41 minutes de calcul effectif, 6,8M tokens consommés, status final `TASK_COMPLETE`. Ce n'est pas qu'une nouvelle commande, c'est un nouveau contrat entre l'humain et l'agent.

## Points clés

- `/goal` introduit des goals persistés qui survivent aux redémarrages et aux pauses multi-heures
- Runtime continuation : Codex injecte un message developer pour reprendre, sans intervention humaine
- 6h44 de wall time pour 41 minutes de calcul réel — l'agent passe l'essentiel du temps en attente d'I/O
- 6,8M tokens cumulés en input avec 94% de cache hit rate
- L'auto-context-compaction se déclenche automatiquement, configurable via `model_auto_compact_token_limit`

## Analyse approfondie

### TL;DR

- `/goal` a été livré dans Codex CLI v0.128.0 le 30 avril 2026 comme feature phare
- Il introduit les goals persistés : un état de but qui survit aux redémarrages de terminal, aux mises en veille de laptop et aux pauses multi-heures sans avoir à re-prompter
- La runtime continuation signifie que Codex injecte un message developer à la reprise plutôt que d'attendre que tu tapes quoi que ce soit
- J'ai fait tourner une vraie session sur un monorepo TypeScript. Wall time : environ 6h44. Calcul modèle effectif : environ 41 minutes. Status final : `TASK_COMPLETE`
- La session a brûlé environ 6,8M tokens cumulés en input avec un cache hit rate de ~94%. L'auto-compaction de contexte s'est déclenchée une fois, configurable via `model_auto_compact_token_limit`

### Le contexte

Je n'avais pas prévu de faire tourner Codex toute la nuit. J'ai démarré une session à 21h19 heure de Berlin le 30 avril, regardé un tour tourner pendant 57 secondes, puis j'ai fermé le laptop et je suis allé me coucher. Quand je suis revenu cinq heures et demie plus tard, `/goal` était déjà reparti. Il avait repris exactement là où il s'était arrêté. Je n'avais rien re-prompté.

C'est ça le truc avec `/goal` qui ne ressort pas dans une note de release. Ce n'est pas juste une nouvelle commande. C'est un contrat différent entre toi et l'agent.

### Ce qui a été livré le 30 avril

Codex CLI v0.128.0 (taggé `rust-v0.128.0`) est sorti le 30 avril 2026. Le titre des release notes : "Added persisted /goal workflows with app-server APIs, model tools, runtime continuation, and TUI controls for create, pause, resume, and clear."

Cette phrase contient beaucoup de choses, alors décortiquons-la.

**Goals persistés** est l'idée centrale. Les sessions Codex précédentes étaient éphémères. Ferme le terminal, perds le fil. `/goal` stocke l'objectif actif dans l'état de l'app-server, donc il survit au processus.

**App-server APIs** est la plomberie derrière cette persistence. Codex parle désormais à une couche serveur locale qui suit l'état du goal.

**Model tools** signifie que le modèle lui-même obtient des outils pour interagir avec le cycle de vie du goal. Il peut signaler la complétion, demander la continuation, et inspecter l'état du goal dans son raisonnement.

**Runtime continuation** est le comportement que j'ai vu cette nuit-là. Quand tu reprends (ou quand Codex détecte que la session est de nouveau active), il injecte un message developer qui invite le modèle à continuer son travail. Tu n'as rien à taper.

**TUI controls** complète la surface. Le terminal UI obtient des actions explicites de création, pause, reprise et effacement du goal. Tu peux mettre en pause un goal en cours intentionnellement, pas juste en fermant le couvercle.

Le reste de v0.128.0 mérite une mention rapide. La rescroll fonctionne enfin sur redimensionnement de terminal sans casser le texte. Une nouvelle commande `codex update` gère les self-updates du CLI. Le composer affiche des suggestions de mode plan quand une tâche semble candidate à la planification.

### La session de 6h44

J'ai lancé `/goal "refactorer le module billing pour qu'il utilise la nouvelle abstraction PaymentProvider, sans casser les tests existants, et en ajoutant une couverture sur les cas edge identifiés dans #4521"`. 57 secondes de premier tour, puis fermeture du laptop.

Le lendemain matin, j'ai rouvert l'ordi à 4h03. Codex avait redémarré dès la sortie de veille (4h00 environ). L'agent a continué pendant encore 1h41, gérant les redirections de tests, les conflits de typage et un refactoring de signatures de fonction. À 5h44, il a publié le commit final et émis `TASK_COMPLETE`.

Le détail intéressant : l'auto-context-compaction. Pendant la nuit, l'historique a dépassé `model_auto_compact_token_limit`, et le système a compressé automatiquement les anciens tours en un résumé. Cela s'est passé une fois, sans intervention. Le résumé est conservé dans le state du goal.

### Ce qui change

Avant `/goal`, tu devais soit garder le terminal ouvert et l'œil dessus, soit décomposer le travail en petits chunks. Avec `/goal`, tu peux confier un objectif et partir. L'agent gère la persistence, la reprise, la compaction. Tu reviens, tu lis le résumé, tu ajustes.

Cela change la nature du management humain-agent. On passe d'un mode "co-pilot synchrone" à un mode "delegate asynchrone". Et avec ça, les questions classiques du management (donner un cap clair, vérifier l'avancement, intervenir au bon moment) reviennent en force.

## Pourquoi ça compte

`/goal` matérialise le passage des agents synchrones aux agents asynchrones longue durée. Pour une équipe, cela change la façon dont on découpe le travail, dont on évalue le coût d'un agent et dont on définit la responsabilité humaine sur ce qu'il produit.
