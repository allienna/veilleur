---
title: "Writing my first evals"
date: 2026-05-04
url: https://workos.com/blog/writing-my-first-evals?utm_source=tldrai&utm_medium=newsletter&utm_campaign=q22026
authors: [Nick Nisi, WorkOS]
keywords: [evals, claude agent sdk, fixtures, ai testing, workos]
theme: IA
tone: tutorial
used_in: ["2026-05-04"]
---

## Résumé

Nick Nisi raconte comment il a construit deux systèmes d'évaluation pour deux outils dev IA chez WorkOS — `workos install` (un CLI propulsé par le Claude Agent SDK qui installe AuthKit dans 16 frameworks) et WorkOS Skills (contexte agent auto-généré depuis la doc). Le déclic : les outils tournaient mais il n'avait aucune idée s'ils faisaient *bien* leur boulot. Comme un agent ne produit jamais deux fois la même sortie, `expect(output).toBe(expected)` ne tient pas. Sa solution : des fixtures — projets minimaux par framework — copiées dans un répertoire temporaire, auxquels on applique l'agent, puis on mesure le diff git. Le diff devient la source de vérité de ce qui a changé.

## Points clés

- Un agent ne fait pas la même chose deux fois : noms de fichiers, styles d'import, gestion d'erreur diffèrent à chaque run
- Les fixtures sont des starter apps minimales (React SPA, Next.js, Flask, etc.) — 16 frameworks chez WorkOS, avec plusieurs états de départ par framework (`example`, `example-auth0`, `partial-install`, `conflicting-middleware`)
- Le `git init` après `pnpm install` matters : le diff post-agent devient la source de vérité
- "Magic is untestable by default"
- Une vraie eval ne peut pas être un test unitaire classique : c'est une grille de scoring sur des axes qui comptent (fonctionnalité, lisibilité du diff, respect des conventions)
- L'inquiétude initiale ("24 fixtures, c'est à la fois pas assez et trop à maintenir") est universelle ; il faut juste commencer

## Analyse approfondie

J'ai passé les dernières semaines à construire deux outils dev propulsés par l'IA chez WorkOS. À un moment, j'ai réalisé que je n'avais aucune idée s'ils marchaient vraiment.

Pas "marchaient" au sens de "est-ce que ça tourne". Ça tournait très bien. Je veux dire "marchaient" au sens de "est-ce que faire tourner cet outil rend vraiment les choses meilleures pour le développeur qui l'utilise ?" C'est une question plus dure qu'elle n'en a l'air quand l'output de ton outil est différent à chaque run.

J'avais besoin d'evals. Et je n'avais aucun background pour en écrire.

C'est l'histoire de la construction de deux systèmes d'évaluation très différents pour deux problèmes très différents, et de la découverte qu'ils m'enseignaient la même chose.

**Les projets** : WorkOS CLI (la commande `workos install`, propulsée par le Claude Agent SDK) | WorkOS Skills (contexte agent auto-généré depuis notre doc).

### L'agent fait-il la bonne chose ?

Le premier outil est `workos install`, une commande CLI qui utilise le Claude Agent SDK pour installer automatiquement WorkOS AuthKit dans ton projet. Tu le pointes sur une app Next.js, une SPA React, un serveur Python Flask, ou n'importe lequel des 16 frameworks supportés, et il découvre quoi faire. Il lit ton code, comprend la structure de ton projet, crée les bons fichiers, modifie les bonnes configs, et installe les bonnes dépendances.

C'est de la magie. Et la magie est intestable par défaut.

Le problème pour tester un agent IA, c'est qu'il ne fait pas la même chose deux fois. Même projet d'input, même prompt, output différent. Noms de fichiers différents, styles d'import différents, approches de gestion d'erreur différentes. `expect(output).toBe(expected)` se casse instantanément.

Donc j'ai construit un système d'eval.

### Les fixtures comme états de départ

L'eval démarre avec des fixtures : des starter apps minimales pour chaque framework supporté. Une SPA React avec trois pages. Une app Next.js avec un layout basique. Un serveur Python Flask avec un endpoint health. 16 frameworks au total, chacun avec plusieurs états de départ comme `example`, `example-auth0` (migration depuis Auth0), `partial-install`, et `conflicting-middleware`.

Le fixture manager copie chacun dans un répertoire temporaire, lance `pnpm install` (ou `pip install`, `bundle install`, `go mod download`, selon ce qu'il détecte), et initialise un repo git. Ce `git init` matters. Le diff après le passage de l'agent devient la source de vérité de ce qui a changé.

Je serai honnête : quand j'ai eu environ 24 fixtures, ma réaction a été : "ça donne à la fois l'impression de ne pas être assez et d'être déjà trop à maintenir. Est-ce vraiment la bonne route ?" Je m'inquiétais aussi des coûts en tokens, de la flakiness, du temps de tourner ces evals à chaque PR.

Mais à mesure que je faisais tourner les evals et que je voyais les régressions remonter, j'ai compris : ce que je construisais, c'était la première vraie boucle de feedback que j'avais sur cet outil. Sans ça, je pilotais à vue.

## Pourquoi ça compte

C'est un retour terrain pragmatique sur ce que ça veut dire vraiment écrire des evals quand on construit avec les Claude Agent SDK ou équivalents. Beaucoup d'équipes vont passer par cette même prise de conscience en 2026 : l'outil "magique" qu'on a construit est intestable tant qu'on n'a pas investi dans une infra d'eval — fixtures + scoring sur des axes qui comptent + diff git comme source de vérité.
