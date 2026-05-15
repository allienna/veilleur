---
title: "The 8 Levels of Agentic Engineering"
date: 2026-05-15
url: https://www.bassimeledath.com/blog/agentic-engineering-levels
authors: [bassimeledath.com, Bassim Eledath]
keywords: [agentic engineering, context engineering, AI productivity, orchestration, multiplayer]
theme: IA
tone: opinion
used_in: ["2026-05-15"]
---

## Résumé

Bassim Eledath propose un cadre de progression en 8 niveaux pour décrire la maîtrise du coding agentic, du tab-complete jusqu'à l'orchestration de subagents en parallèle pendant qu'on dort. Sa thèse : la capacité des modèles dépasse aujourd'hui notre capacité à les utiliser, et l'écart entre une équipe qui shippe en 10 jours et une autre bloquée sur un POC vient de cette pratique, pas du modèle. Important : la progression d'un individu est plafonnée par le niveau le plus bas de son équipe.

## Points clés

- Le coding agentic se progresse par paliers discrets — chacun multiplie le throughput
- Niveau 3 = Context Engineering, où chaque token doit se battre pour sa place dans le prompt
- Niveaux supérieurs = orchestration multi-agents, background agents, pipelines async
- L'effet "multiplayer" : votre output dépend du niveau de vos coéquipiers (et de vos reviewers)
- L'amélioration des modèles amplifie le gain à chaque niveau franchi

## Analyse approfondie

### Le constat de départ

La capacité de l'IA en coding dépasse aujourd'hui notre capacité à l'exploiter. C'est pour ça que les scores SWE-bench progressent sans que les métriques de productivité des leaders d'ingénierie suivent. Quand l'équipe d'Anthropic shippe un produit comme Cowork en 10 jours, et qu'une autre équipe n'arrive pas à dépasser un POC cassé avec les mêmes modèles, la différence vient de ce qui sépare la capacité de la pratique. Et cet écart se ferme par paliers.

Il y a aussi un effet multiplayer : votre throughput dépend du niveau de vos coéquipiers. Un wizard niveau 7 qui fait tourner plusieurs PR en background pendant qu'il dort, si son repo exige l'approbation d'un collègue resté au niveau 2 (review manuelle), voit sa cadence cassée. D'où l'intérêt d'élever toute l'équipe.

### Niveaux 1 & 2 : Tab Complete et Agent IDE

Tout a commencé avec Copilot et le tab complete. Click tab, autocomplete code. Probablement oublié de beaucoup et sauté par les nouveaux entrants. Ça favorisait les devs expérimentés capables de squelettiser leur code avant que l'IA remplisse les blancs.

Les IDE comme Cursor ont changé la donne en connectant le chat au codebase, rendant les edits multi-fichiers nettement plus simples. Mais le plafond, c'était toujours le contexte. Le modèle ne pouvait aider que sur ce qu'il voyait — et trop souvent il voyait soit le mauvais contexte, soit trop du mauvais contexte.

À ce niveau, on expérimente aussi le plan mode : traduire une idée vague en plan structuré pour le LLM, itérer sur le plan, puis déclencher l'implémentation. Ça marche bien à ce stade. Aux niveaux supérieurs, on en dépend moins.

### Niveau 3 : Context Engineering

Phrase à la mode de 2025, le context engineering est devenu central quand les modèles sont devenus fiables à suivre un nombre raisonnable d'instructions avec juste la bonne quantité de contexte. Un contexte bruyant est aussi nocif qu'un contexte sous-spécifié, donc l'effort porte sur la densité d'information par token. Le mantra : "chaque token doit se battre pour sa place dans le prompt".

À ce niveau, on commence à structurer ses repos pour faciliter l'auto-navigation de l'agent : conventions de nommage, fichiers `CLAUDE.md` annotés, INDEX.md commentés, glossaires de codes projet. Le contexte n'est plus collé à la volée, il est mis en place comme une infra.

### Niveaux 4-6 : Subagents et orchestration

Au-delà du contexte, on entre dans la délégation. On apprend à découper une tâche en subagents : un qui plannifie, un qui implémente, un qui review, un qui valide. Chacun a son contexte minimal et son objectif clair. C'est aussi là qu'on commence à industrialiser ses evals — tests automatisés qui vérifient que la chaîne d'agents fait bien ce qu'on attend, sur un jeu de cas figés.

À ces niveaux, les outils comme Claude Code, Codex, Cowork ne sont plus utilisés comme un copilote, mais comme une plateforme d'orchestration.

### Niveaux 7-8 : Background agents et pipelines async

Les niveaux les plus élevés correspondent au coding asynchrone à large échelle : plusieurs PR ouvertes en parallèle pendant qu'on dort, chacune produite par un agent en background, reviewée par un autre agent, mergée après passage des CI. Le dev humain devient un orchestrateur qui revoit les diffs, arbitre les conflits, recadre les agents qui dérivent.

À ce stade, le throughput est multiplié par un facteur qui n'a plus rien à voir avec le tab-complete d'origine.

### L'effet multiplayer

Le point qui revient en boucle dans l'article : votre niveau effectif est celui du goulot d'étranglement de votre équipe. Si vos reviewers humains sont au niveau 2, vos PR niveau 7 attendent. Si votre CI est au niveau 1, vos agents niveau 6 se bloquent. D'où la nécessité, pour qui veut vraiment monter, de tirer son équipe avec soi — et accessoirement, d'investir dans l'outillage commun (linters, tests, conventions) plus que dans son propre setup.

## Pourquoi ça compte

C'est un cadre de progression structurant qu'on peut utiliser pour situer son équipe, identifier le prochain palier réaliste, et prioriser les investissements (context vs orchestration vs eval). C'est aussi un rappel utile que le coding agentic n'est pas une question d'outil mais de pratique systémique.
