---
title: "OpenAI has the smarter model. Anthropic is winning anyway."
date: 2026-05-20
url: https://blog.ravi-mehta.com/p/openai-vs-anthropic?utm_source=tldrnewsletter
authors: [Ravi Mehta]
keywords: [Anthropic, OpenAI, MCP, Claude Code, plateforme]
theme: IA
tone: opinion
used_in: ["2026-05-20"]
---

## Résumé

Ravi Mehta analyse un paradoxe : sur les benchmarks d'intelligence (Artificial Analysis), OpenAI reste devant Anthropic, mais sur l'AI Index de Ramp en mai 2026, Anthropic vient de dépasser OpenAI sur la dépense entreprise. Sa thèse : la course ne se joue plus au niveau du modèle mais au niveau de la plateforme. Anthropic a parié sur les "mains" (MCP, Claude Code, intégration au terminal et aux outils existants) plutôt que sur la "tête". Le pattern se répète avec Claude (skills), Claude Cowork (file access), Claude Design (HTML rendering) — pas plus malin, mais mieux outillé.

## Points clés

- Deux courbes contradictoires : OpenAI gagne en benchmarks, Anthropic gagne en revenus entreprise
- OpenAI joue au niveau du modèle ; Anthropic joue au niveau de la plateforme
- MCP (Model Context Protocol) : standard ouvert pour brancher n'importe quel modèle à n'importe quel outil
- Claude Code a gagné non parce que le modèle était meilleur, mais parce qu'il vit dans le terminal au milieu de git, docker, ffmpeg, jq, etc.
- Métaphore *mens et manus* (MIT) : l'intelligence sans capacité d'agir ne sert à rien
- Les "Claude X" récents (skills, Cowork, Design) sont tous des variations de la même idée : donner des mains différentes à Claude

## Analyse approfondie

Deux graphiques racontent l'histoire.

Sur le classement d'intelligence d'Artificial Analysis, les modèles frontière d'OpenAI battent toujours Claude. Ils sont en tête sur les benchmarks qui ont défini cette industrie depuis trois ans.

Le modèle GPT le plus capable d'OpenAI surpasse Claude Opus sur les benchmarks clés.

Sur l'AI Index de Ramp pour mai 2026, Anthropic vient de dépasser OpenAI en dépense entreprise. L'usage d'Anthropic explose, dépassant OpenAI pour la première fois ce mois-ci.

Si l'intelligence était ce qui compte, cela ne devrait pas arriver.

Alors qu'est-ce qu'Anthropic fait qu'OpenAI ne fait pas ?

**OpenAI se bat au niveau du modèle. Anthropic se bat au niveau de la plateforme — et c'est là que l'IA appliquée se gagne.**

Deux paris ont mené Anthropic là. Aucun n'apparaît sur un benchmark.

La devise du MIT est *mens et manus*. L'esprit et les mains. L'idée : l'intelligence n'a aucun sens sans la capacité d'agir sur le monde. Vous pouvez être un savant en ingénierie structurelle, mais sans une scie vous ne construisez pas de maison.

Pendant trois ans, l'industrie de l'IA a été obsédée par l'esprit. Modèles plus gros. Benchmarks plus malins. Plus de paramètres.

Anthropic a parié sur les mains.

Cela a commencé avec **MCP** — le Model Context Protocol. Un standard qui permet à n'importe quel modèle d'IA d'accéder à n'importe quel outil, n'importe quelle source de données, n'importe quel système. Pas glamour. Pas une release qui domine les benchmarks. Juste de la "plomberie".

Puis est venu **Claude Code**. Le secret de polichinelle du succès de Claude Code : il n'a pas gagné parce que le modèle de codage sous-jacent était meilleur. Les mêmes modèles Claude étaient disponibles dans Cursor, dans tous les plugins IDE, dans chaque wrapper du marché. Claude Code a gagné parce qu'il vit dans le terminal — où des milliers d'outils existent déjà. Git. Docker. ffmpeg. jq. Chaque script CI jamais écrit.

Mettre Claude dans la CLI ne l'a pas rendu plus intelligent. Cela lui a donné des mains.

Le pattern se répète avec Claude (skills), Claude Cowork (file access), et Claude Design (HTML rendering). Aucun de ces produits n'est un "Claude plus intelligent". Ce sont des Claude avec des mains différentes — outils différents, surfaces différentes, façons différentes d'agir dans le monde.

OpenAI a passé les dernières années à pousser les frontières du modèle. Anthropic a passé les mêmes années à pousser les frontières de ce que le modèle peut faire concrètement.

## Pourquoi ça compte

Pour un architecte ou un directeur engineering, c'est la grille de lecture clé du moment : arrêter d'arbitrer sur "qui a le meilleur modèle" et commencer à arbitrer sur "qui a la meilleure intégration à mon écosystème d'outils". C'est aussi un message stratégique pour qui construit des produits IA en interne : la valeur est dans la plomberie, pas dans le modèle.
