---
title: "8 levels of context maturity in AI-native engineering"
date: 2026-06-23
url: https://link.mail.beehiiv.com/ss/c/u001.3a5P_SwQzY5x8USD2q4p0ifl3M68qmkH56j-n_NuhhP4hNYBzzelAmkV9t-_1NZMyF6-R9ZsET6TyrGQzp4nA3pLFoBCNR_5BWagr9uqIXQA-r0EyIQq_ZsECjhPnaWZwdoIQZVW8S9Y1qk3-OfueC4UCozOQdr-SzeYwVlw2yyRb7vi1lAGEYN5njqz8xOsVev4szt29O1N_uKrzEoWqEs7GrjGCUeAGTm9CGiHT_YyiOteCt3AJj3FUQXLJDq8/4rq/q4gwrYlsQTuTmP68g5wleA/h9/h001.b5borLR2vmSjXvmfhQ3kQahkB95UbnT803wtE6rBDzw
authors: [Unblocked, Brandon Walsenuk]
keywords: [context engineering, AI-native, MCP, harness, maturité, agents]
theme: IA
tone: opinion
used_in: ["2026-06-23"]
---

## Résumé

L'IA intervient désormais dans environ 60 % du travail d'ingénierie, mais à peine un cinquième peut être délégué sans supervision humaine. Cette session/présentation d'Unblocked défend une thèse claire : ce trou n'est pas un problème de modèle, c'est un problème de contexte. Elle propose un modèle de maturité en huit niveaux, répartis en trois zones, pour situer où une équipe est bloquée sur le chemin vers des agents réellement dignes de confiance.

## Points clés

- L'IA touche ~60 % du travail d'ingénierie, mais seulement ~20 % peut être délégué sans surveillance — l'écart vient du contexte, pas du modèle.
- Trois zones de maturité : « Tu es le contexte » (niveaux 1-2), « Contexte curé » (niveaux 3-4), « La couche de contexte » (niveaux 5-8).
- Les fichiers de règles et `CLAUDE.md` constituent un piège : la plupart des équipes s'y arrêtent, et les règles pourrissent plus vite qu'on ne les maintient.
- Empiler plus d'outils, de connecteurs et de fenêtre de contexte finit par ne plus aider — il faut une vraie couche de contexte synthétisé et conscient des permissions.
- Plus on pousse vers l'autonomie, plus le mauvais contexte coûte cher : c'est la partie à bien faire tôt.

## Analyse approfondie

L'IA apparaît désormais dans environ 60 % du travail d'ingénierie. Mais seulement un cinquième environ peut réellement être délégué sans que quelqu'un surveille la sortie. C'est cet écart qui mérite qu'on en parle, et ce n'est pas un problème de modèle.

C'est un problème de contexte.

Il n'y a pas si longtemps, c'était toi le moteur de contexte. Chaque bonne session d'agent tournait sur ta mémoire de ce qu'il fallait coller dedans. Les équipes sont donc passées aux fichiers de règles et aux `CLAUDE.md`, et la plupart d'entre elles ont silencieusement calé là. Les règles pourrissent plus vite que personne ne peut les maintenir à jour.

Cette session parcourt les 8 niveaux de maturité du contexte, le modèle utilisé pour expliquer où les équipes se bloquent sur le chemin vers des agents auxquels on peut réellement faire confiance. Il se décompose en trois zones :

- **Tu es le contexte** (niveaux 1-2). Tab complete et IDE agentiques. La sortie ne vaut que ce que vaut celui qui pilote.
- **Contexte curé** (niveaux 3-4). Le context engineering, plus la boucle « planifier, déléguer, évaluer, codifier ». Mieux que de se reposer sur la mémoire, mais avec un plafond : les règles ne capturent que ce que tu savais déjà devoir écrire.
- **La couche de contexte** (niveaux 5-8). MCP et skills, harness engineering, agents d'arrière-plan, équipes d'agents. Ici, un contexte synthétisé et conscient des permissions devient porteur. Il doit exister avant qu'un humain puisse sortir de la boucle.

Tu repartiras en sachant :

- À quel niveau ton équipe se situe réellement, et contre quel mur tu te cognes probablement. La plupart des équipes sont bloquées sur l'un des trois principaux murs.
- Pourquoi ajouter plus d'outils, de connecteurs et de fenêtre de contexte finit par ne plus aider. Et ce qu'il faut faire à la place.
- Ce qu'il faut vraiment pour atteindre une couche de contexte. Le mauvais contexte coûte de plus en plus cher à mesure qu'on pousse vers l'autonomie, donc c'est la partie qui vaut le coup d'être bien faite tôt.

Pour qui : leaders d'ingénierie, ingénieurs senior et staff, et équipes plateforme qui ont déjà adopté les outils de code IA et veulent une réponse claire sur la suite.

(Présentation animée par Brandon Walsenuk, Developer Relations chez Unblocked, avec une auto-évaluation gratuite pour situer son équipe.)

## Pourquoi ça compte

Ce modèle de maturité donne un vocabulaire commun pour diagnostiquer pourquoi les agents calent en production — et déplace le débat du choix du modèle vers la construction d'une vraie couche de contexte, le vrai chantier de 2026.
