---
title: "Don't trust large context windows"
date: 2026-06-15
url: https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows
authors: [garrit.xyz]
keywords: [context window, context rot, coding agents, smart zone, artefacts]
theme: IA
tone: opinion
used_in: ["2026-06-15"]
---

## Résumé

L'auteur met un nom sur une intuition : la fenêtre de contexte d'un LLM se divise en une « zone intelligente » (modèle affûté) et une « zone bête » (l'attention décroche), avec une bascule autour de 100k tokens — peu importe la taille annoncée. Les agents de code y entrent vite. La parade : traiter le contexte comme un budget et sortir l'information dans des artefacts écrits (specs, breadcrumbs) qu'une nouvelle session peut reprendre proprement.

## Points clés

- Le contexte utile est une fraction du nombre annoncé ; la bascule « zone bête » se situe vers 100k tokens, indépendamment des 200k/1M/2M vantés.
- Les études RULER et le rapport « context rot » de Chroma montrent une dégradation progressive à mesure qu'on remplit la fenêtre.
- Un agent de code atteint 100k tokens « avant le déjeuner » (lectures de fichiers, debug, tests).
- L'auto-compaction (ex. Claude Code) aide mais se déclenche trop tard et résume avec un modèle déjà dégradé.
- Meilleure pratique : ouvrir une nouvelle session avec une spec écrite soi-même — un handoff à plus fort signal que tout résumé automatique (approche « breadcrumb »).

## Analyse approfondie

L'auteur raconte avoir regardé une vidéo qui a nommé une chose qu'il ressentait. L'auteur de la vidéo découpe la fenêtre de contexte d'un LLM en deux zones : la **zone intelligente**, où le modèle est affûté, et la **zone bête**, où l'attention décroche et où le modèle commence à oublier ce qu'on lui a dit cinq minutes plus tôt. La bascule se situe quelque part autour de 100k tokens. Peu importe la taille de la fenêtre annoncée.

Cela compte parce que les agents de code vous emmènent allègrement droit dans la zone bête. Un agent moderne brûle les tokens vite : quelques lectures de fichiers, une longue session de debug, une batterie de tests tentaculaire, et vous voilà à 100k avant le déjeuner. Pendant ce temps, les vendeurs annoncent des fenêtres de 200k, 1M, voire 2M, comme si ces nombres représentaient un working set utilisable. Ce n'est pas le cas. Des études comme RULER et le rapport de Chroma sur le « context rot » montrent que le contexte effectif n'est qu'une fraction du nombre annoncé, et que la performance se dégrade graduellement à mesure qu'on remplit la fenêtre.

Les grandes fenêtres de contexte sont surtout un nombre marketing. Les architectures qui les sous-tendent fonctionnent, mais elles maquillent un problème que le mécanisme d'attention ne résout pas vraiment. Le nombre sur la boîte grossit à chaque version ; la partie utilisable ne suit pas.

Les agents modernes deviennent malins là-dessus. Des outils comme Claude Code « auto-compactent » : quand la session devient longue, l'agent résume l'historique et repart à neuf. Ça aide. Mais l'auto-compaction se déclenche après qu'on a déjà passé du temps dans la zone bête, et le résumé est lui-même produit par un modèle déjà dégradé. Mieux que rien, mais l'auteur préfère éviter la situation tout court.

Ce qu'il fait : ouvrir une nouvelle session et lui passer une spec qu'il a écrite lui-même. C'est un handoff à bien plus fort signal que tout résumé automatique, parce qu'il décide ce qui compte pour la suite. C'est l'approche « breadcrumb » appliquée aux agents : laisser un artefact que la session suivante — ou la personne suivante — peut reprendre proprement. On peut aller plus loin : des projets comme obra/superpowers et mattpocock/skills structurent des workflows d'agents entiers autour de petits artefacts nommés (PRD, plans, skills, handoffs de sous-agents). Chacun est une façon de garder la session de travail dans la zone intelligente en déplaçant délibérément l'information hors de la session, vers quelque chose que la session suivante peut lire.

L'auteur traite donc sa fenêtre de contexte comme un budget : il suppose que seul le premier morceau travaille réellement pour lui, et tout ce qu'il peut sortir de la session vivante vers un artefact écrit est une chose de moins contre laquelle l'attention doit se battre.

## Pourquoi ça compte

C'est le contrepoint technique aux promesses marketing : ça explique concrètement pourquoi la facture de tokens explose (agents qui remplissent la zone bête) et pourquoi l'humain qui rédige specs et artefacts reste le garant de la qualité du travail agentique.
