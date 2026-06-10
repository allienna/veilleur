---
title: "8 levels of context maturity in AI-native engineering"
date: 2026-06-09
url: https://link.mail.beehiiv.com/ss/c/u001.3a5P_SwQzY5x8USD2q4p0ifl3M68qmkH56j-n_NuhhP4hNYBzzelAmkV9t-_1NZMyF6-R9ZsET6TyrGQzp4nA3pLFoBCNR_5BWagr9uqIXQA-r0EyIQq_ZsECjhPnaWZwdoIQZVW8S9Y1qk3-OfueGWZbFi_Uwn9gsuRjlaBathREHXSniwBB4oKT_CnLv0ke3PZ4zxMgBYUKrACaVtIJlQ0HGGQ_rwH9ZIGpwlcZU0GKjTwkP6Lq6yHf2ARXoBY/4rc/T8LNCv72RLyBIyuO1pgQMA/h9/h001.SClh1lERZ4TwUYoAo56wSKEhfXpk-nEdytVA3IOJNZQ
authors: [Unblocked, Brandon Walsenuk]
keywords: [context engineering, AI-native, maturity model, CLAUDE.md, MCP, autonomy]
theme: IA
tone: opinion
used_in: ["2026-06-09"]
---

## Résumé

Cet article (support d'un webinaire animé par Brandon Walsenuk, Developer Relations chez Unblocked) propose un modèle en 8 niveaux de maturité du contexte dans l'ingénierie AI-native. Le constat de départ : l'IA intervient dans environ 60 % du travail d'ingénierie, mais seul un cinquième peut être délégué sans surveillance. Ce gap n'est pas un problème de modèle, mais de contexte. Le modèle décrit trois zones — « tu es le contexte », « contexte curé », « la couche de contexte » — et explique les trois murs où les équipes calent.

## Points clés

- L'IA est présente dans ~60 % du travail d'ingénierie, mais seul ~1/5 est délégable sans surveillance.
- Le goulot d'étranglement n'est pas le modèle, c'est le contexte.
- Zone 1 « Tu es le contexte » (niveaux 1-2) : tab-complete et IDE agents ; la sortie vaut ce que vaut le pilote.
- Zone 2 « Contexte curé » (niveaux 3-4) : context engineering + boucle « plan, delegate, assess, codify », mais plafonnée par ce qu'on a su écrire.
- Zone 3 « La couche de contexte » (niveaux 5-8) : MCP, skills, harness engineering, background agents, équipes d'agents.
- Un mauvais contexte coûte de plus en plus cher à mesure qu'on pousse vers l'autonomie.

## Analyse approfondie

L'IA apparaît aujourd'hui dans environ 60 % du travail d'ingénierie. Mais seule une cinquième partie environ peut réellement être déléguée sans que quelqu'un surveille la sortie. C'est le gap qui mérite qu'on en parle, et ce n'est pas un problème de modèle.

C'est un problème de **contexte**.

Il n'y a pas si longtemps, c'était vous le moteur de contexte. Chaque bonne session d'agent reposait sur votre mémoire de ce qu'il fallait coller dans le prompt. Les équipes sont alors passées aux fichiers de règles et aux CLAUDE.md, et la plupart ont discrètement calé là : les règles pourrissent plus vite que quiconque ne peut les tenir à jour.

Le modèle présenté décrit les **8 niveaux de maturité du contexte** — le cadre utilisé pour expliquer où les équipes se bloquent sur le chemin vers des agents auxquels on peut vraiment faire confiance. Il se découpe en trois zones :

- **Tu es le contexte (niveaux 1-2).** Tab-complete et IDE agents. La sortie ne vaut que ce que vaut la personne qui pilote.
- **Contexte curé (niveaux 3-4).** Context engineering, plus la boucle « plan, delegate, assess, codify » (planifier, déléguer, évaluer, codifier). Mieux que de s'appuyer sur la mémoire, mais avec un plafond : les règles ne capturent que ce qu'on savait déjà devoir écrire.
- **La couche de contexte (niveaux 5-8).** MCP et skills, harness engineering, background agents, équipes d'agents. Ici, un contexte synthétisé et conscient des permissions devient « load-bearing » (porteur). Il doit exister avant qu'un humain puisse sortir de la boucle.

Ce que l'on en retire :

- À quel niveau se trouve réellement votre équipe, et contre quel mur elle bute probablement. La plupart des équipes calent sur l'un des trois murs principaux.
- Pourquoi ajouter toujours plus d'outils, de connecteurs et de fenêtre de contexte finit par ne plus aider — et ce qu'il faut faire à la place.
- Ce qu'il faut vraiment pour atteindre une couche de contexte. Un mauvais contexte devient d'autant plus coûteux qu'on pousse vers l'autonomie : c'est donc la partie qu'il vaut mieux bien traiter tôt.

Public visé : leaders d'ingénierie, ingénieurs senior et staff, et équipes plateforme ayant déjà adopté des outils de code IA et voulant une réponse claire sur la suite. Le webinaire est animé par Brandon Walsenuk, Developer Relations chez Unblocked, et s'accompagne d'une auto-évaluation gratuite pour situer son équipe.

## Pourquoi ça compte

Ce modèle nomme le vrai plafond de l'IA-native engineering : ce n'est plus la puissance du modèle, mais la qualité et la structure du contexte. Il explique pourquoi les fichiers de règles ne suffisent pas et pourquoi la prochaine étape (MCP, skills, couches de contexte) est une condition préalable à l'autonomie.
