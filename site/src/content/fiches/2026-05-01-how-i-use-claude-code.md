---
title: "How I Use Claude Code"
date: 2026-05-01
url: https://docs.anthropic.com/en/docs/claude-code
authors: [Anonymous practitioner]
keywords: [Claude Code, plan mode, research artifacts, agentic workflow, code review]
theme: IA
tone: tutorial
used_in: ["2026-05-01"]
---

## Résumé

Retour d'expérience après neuf mois d'utilisation de Claude Code comme outil principal de développement. Le workflow décrit est radicalement différent de celui de la plupart des utilisateurs d'outils IA : il repose sur un principe central — ne jamais laisser Claude écrire du code avant d'avoir validé un plan écrit. Cette séparation planning / exécution évite les efforts gaspillés, garde le développeur en contrôle des décisions d'architecture, et produit de meilleurs résultats avec moins de tokens. Le workflow se déroule en trois phases : recherche, plan, implémentation — chacune produit un artefact markdown persistant, jamais juste un résumé verbal dans le chat.

## Points clés

- Principe central : pas de code avant validation d'un plan écrit
- Phase 1 — Recherche : étude approfondie, restitution dans un `research.md`
- Phase 2 — Plan : décomposition en étapes, validation humaine
- Phase 3 — Implémentation : seulement après validation du plan
- Le langage du prompt compte : "deeply", "in great details", "intricacies" évitent que Claude survole
- Les artefacts markdown sont la surface de revue — pas un exercice scolaire

## Analyse approfondie

J'utilise Claude Code comme outil de développement principal depuis environ 9 mois, et le workflow auquel je suis arrivé est radicalement différent de ce que la plupart des gens font avec les outils de coding IA. La majorité des développeurs tape un prompt, utilise parfois le mode plan, corrige les erreurs, recommence. Les plus *terminally online* enchaînent des ralph loops, des MCPs, des gas towns (vous vous souvenez ?), etc. Les résultats dans les deux cas sont un bordel qui s'effondre complètement pour tout ce qui n'est pas trivial.

Le workflow que je vais décrire a un principe central : **ne jamais laisser Claude écrire du code avant d'avoir relu et approuvé un plan écrit**. Cette séparation entre planning et exécution est la chose la plus importante que je fais. Elle empêche les efforts gaspillés, me garde en contrôle des décisions d'architecture, et produit des résultats significativement meilleurs avec un usage minimal de tokens par rapport au fait de sauter directement au code.

### Phase 1 : Recherche

Chaque tâche significative commence par une directive de lecture profonde. Je demande à Claude de comprendre en profondeur la partie pertinente de la base de code avant de faire quoi que ce soit d'autre. Et j'exige toujours que les conclusions soient écrites dans un fichier markdown persistant, jamais juste un résumé verbal dans le chat.

> read this folder in depth, understand how it works deeply, what it does and all its specificities. when that's done, write a detailed report of your learnings and findings in research.md

> study the notification system in great details, understand the intricacies of it and write a detailed research.md document with everything there is to know about how notifications work

> go through the task scheduling flow, understand it deeply and look for potential bugs. there definitely are bugs in the system as it sometimes runs tasks that should have been cancelled. keep researching the flow until you find all the bugs, don't stop until all the bugs are found. when you're done, write a detailed report of your findings in research.md

Notez la langue : **"deeply"**, **"in great details"**, **"intricacies"**, **"go through everything"**. Ce n'est pas du remplissage. Sans ces mots, Claude survole. Il lit un fichier, voit ce qu'une fonction fait au niveau de sa signature, et passe à autre chose. Tu dois signaler que la lecture en surface n'est pas acceptable.

L'artefact écrit (`research.md`) est critique. Ce n'est pas pour faire faire les devoirs à Claude. C'est ma surface de revue. Je peux la lire, vérifier que Claude a vraiment compris le système, et corriger les malentendus avant qu'aucun planning ne commence. Si la recherche est fausse, le plan sera faux, et l'implémentation sera fausse. Garbage in, garbage out.

### Phase 2 : Planning

Une fois la recherche validée, je demande à Claude de produire un plan détaillé d'implémentation, lui aussi sous forme de markdown. Ce plan doit lister :

- Les fichiers à modifier
- L'ordre des changements
- Les tests à écrire
- Les risques identifiés
- Les hypothèses sur lesquelles repose le plan

Je relis ce plan attentivement. Souvent, je le modifie. Parfois je le rejette et redemande une autre approche. C'est ici que le travail d'architecture se fait — pas dans le code.

### Phase 3 : Implémentation

Seulement après validation du plan, j'autorise Claude à écrire du code. Et même là, il suit le plan étape par étape, en faisant valider chaque morceau avant de passer au suivant. Les commits restent petits. Les tests sont écrits en même temps. Les déviations par rapport au plan sont signalées explicitement.

### Pourquoi ça marche

- Les erreurs sont attrapées tôt, où elles coûtent peu
- Le contexte reste petit (le plan tient en quelques pages)
- La revue se fait sur des documents lisibles, pas sur des diffs énormes
- L'intention reste claire et partagée

C'est plus lent au départ. C'est radicalement plus rapide à l'arrivée.

## Pourquoi ça compte

C'est probablement le workflow le plus reproductible publié sur Claude Code. La discipline en trois phases (research → plan → implement) avec artefacts markdown intermédiaires est applicable à n'importe quel agent — c'est un pattern, pas une recette.
