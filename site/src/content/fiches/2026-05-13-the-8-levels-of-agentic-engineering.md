---
title: "The 8 Levels of Agentic Engineering — Bassim Eledath"
date: 2026-05-13
url: https://www.bassimeledath.com/blog/the-8-levels-of-agentic-engineering
authors: [Bassim Eledath]
keywords: [agentic engineering, context engineering, compounding engineering, MCP, sub-agents]
theme: IA
tone: opinion
used_in: ["2026-05-13"]
---

## Résumé

Bassim Eledath propose un modèle de maturité en 8 niveaux pour décrire la pratique de l'ingénierie agentique. Tab complete, IDE agentique, context engineering, compounding engineering, MCP & skills, sub-agents, agents en arrière-plan, multi-agents. Chaque palier représente un saut net d'output, et chaque amélioration des modèles amplifie le gain. Surtout, Eledath insiste sur l'« effet multijoueur » : ton débit est strangulé par le niveau le plus bas de ton équipe.

## Points clés

- 8 niveaux, imparfaitement séquentiels, qui décrivent une progression de pratique observée sur le terrain
- Niveaux 1-2 : tab complete et IDE agentique (Cursor) — historiques, déjà dépassés
- Niveau 3 : context engineering — « chaque token doit se battre pour sa place »
- Niveau 4 : compounding engineering — plan/delegate/assess/codify, popularisé par Kieran Klaassen
- Niveau 5 : MCPs et skills — exemple d'une skill de PR review qui lance des sub-agents
- L'écart entre capacité du modèle et maturité de pratique explique pourquoi certaines équipes shippent et d'autres restent au POC
- « Effet multijoueur » : un teammate niveau 2 freine un teammate niveau 7

## Analyse approfondie

La capacité de l'IA à coder dépasse notre capacité à la manier efficacement. C'est pourquoi le maxxing des scores SWE-bench ne se synchronise pas avec les métriques de productivité que la direction engineering surveille vraiment. Quand l'équipe d'Anthropic livre un produit comme Cowork en 10 jours et qu'une autre équipe ne dépasse pas un POC cassé avec les mêmes modèles, la différence est que l'une a fermé l'écart entre capacité et pratique, et l'autre non.

Cet écart ne se ferme pas du jour au lendemain. Il se ferme en niveaux. 8 niveaux. La plupart d'entre vous sont sans doute déjà au-delà des premiers, et vous devriez avoir envie d'atteindre le suivant, car chaque niveau apporte un bond d'output, et chaque amélioration de modèle amplifie ces gains.

L'autre raison de s'en soucier, c'est l'effet multijoueur. Votre output dépend plus que vous ne le pensez du niveau de vos coéquipiers. Imaginez que vous soyez un wizard niveau 7, levant plusieurs PRs solides avec vos agents en arrière-plan pendant que vous dormez. Si votre repo exige l'approbation d'un collègue avant le merge, et que ce collègue est niveau 2, à relire encore manuellement les PRs, ça étrangle votre débit. Il est donc dans votre intérêt de tirer votre équipe vers le haut.

### Niveaux 1 & 2 : Tab Complete et IDE agentique

Ça a commencé avec Copilot et le tab complete. Click tab, autocompletion. Probablement oublié depuis par beaucoup et zappé par les nouveaux entrants. Ça favorisait les devs expérimentés capables de squeletter leur code pour laisser l'IA remplir les trous.

Les IDE orientés IA comme Cursor ont changé la donne en connectant le chat au codebase, rendant les éditions multi-fichiers beaucoup plus simples. Mais le plafond, c'était toujours le contexte. Le modèle ne pouvait aider que sur ce qu'il voyait, et trop souvent il ne voyait pas le bon contexte, ou en voyait trop.

### Niveau 3 : Context Engineering

Buzz phrase de l'année 2025, le context engineering est devenu un sujet quand les modèles sont devenus fiables pour suivre un nombre raisonnable d'instructions avec juste la bonne quantité de contexte. Le contexte bruité était aussi mauvais que le contexte sous-spécifié, donc l'effort consistait à améliorer la densité d'information de chaque token. « Chaque token doit se battre pour sa place dans le prompt » était le mantra.

En pratique, le context engineering touche plus de surface qu'on ne le réalise. C'est votre system prompt et vos fichiers de règles (`.cursorrules`, `CLAUDE.md`). C'est la manière dont vous décrivez vos outils, car le modèle lit ces descriptions pour décider lesquels appeler. C'est gérer l'historique de conversation pour qu'un agent long-running ne perde pas le fil au bout de dix tours. C'est décider quels outils exposer à chaque tour, parce que trop d'options noient le modèle comme elles noient un humain.

On en parle moins aujourd'hui. La balance a penché vers des modèles qui tolèrent du contexte plus bruité et qui raisonnent à travers des terrains plus chaotiques (les fenêtres plus larges aident aussi). Mais ça reste pertinent : les petits modèles sont plus sensibles au contexte ; les outils et modalités gourmands en tokens (Playwright, images) brûlent vite ; les agents avec dizaines d'outils passent plus de tokens à parser des schemas qu'à faire un travail utile.

### Niveau 4 : Compounding Engineering

Le context engineering améliore la session courante. Le compounding engineering, popularisé par Kieran Klaassen, améliore chaque session suivante. C'était un point d'inflexion pour beaucoup : ça a montré que le « vibe coding » pouvait faire plus que du prototype.

C'est une boucle plan, delegate, assess, codify. Vous planifiez la tâche avec assez de contexte pour que le LLM réussisse. Vous déléguez. Vous évaluez le résultat. Et surtout, vous codifiez ce que vous avez appris : ce qui a marché, ce qui a cassé, le pattern à suivre la prochaine fois.

Ce qui fait le compound, c'est l'étape de codification. Les LLMs sont stateless. S'ils réintroduisent une dépendance que vous aviez explicitement retirée hier, ils le referont demain — sauf si vous le leur dites. La manière la plus courante de fermer cette boucle est de mettre à jour votre `CLAUDE.md` (ou équivalent). Attention : l'instinct de tout codifier dans le fichier de règles peut se retourner contre vous (trop d'instructions = aucune). Le meilleur move est de créer un setting où le LLM peut découvrir le bon contexte par lui-même, par exemple via un dossier `docs/` à jour.

### Niveau 5 : MCP et Skills

Les niveaux 3 et 4 résolvent la question du contexte. Le niveau 5 résout la capacité. Les MCPs et skills custom donnent à votre LLM accès à votre base de données, vos APIs, votre pipeline CI, votre design system, Playwright pour le browser testing, Slack pour les notifications. Au lieu de juste penser à votre codebase, le modèle peut maintenant agir dessus.

Exemple : une skill de PR review partagée par l'équipe, qui lance conditionnellement des sub-agents selon la nature de la PR. L'un gère la sûreté d'intégration avec la base. Un autre fait de l'analyse de complexité pour flaguer les redondances ou l'overengineering. Un autre vérifie la santé des prompts. Il lance aussi les linters et Ruff.

Pourquoi investir autant dans une skill de review ? Parce qu'à mesure que les agents produisent des PRs en volume, la revue humaine devient le bottleneck, pas le quality gate. Block a un super write-up sur leur marketplace interne de skills (plus de 100 skills, des bundles par rôle, traitement comme du code : PRs, reviews, versionning).

## Pourquoi ça compte

Ce modèle de maturité donne un vocabulaire commun pour parler des pratiques d'IA en équipe. Il transforme une discussion floue (« on utilise l'IA ») en diagnostic actionnable (« on est niveau 3 mais bloqués au 4 parce qu'on ne codifie pas »).
