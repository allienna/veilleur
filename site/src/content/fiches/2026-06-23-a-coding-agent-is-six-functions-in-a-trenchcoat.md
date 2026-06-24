---
title: "A coding agent is six functions in a trenchcoat"
date: 2026-06-23
url: https://elink56e.dataelixir.com/ss/c/u001.MwQ9-DqNm-0ctGFRWAEvcbeJ5lreZsNER36P-UBzynN5fx2bnRSnZjvgfM9GduSJkvYP4EyXXz3c2P5vM3wu6X8daRliJYZ1wBl7W8NPUIBIo4BRQM1UL93TawEXtDuejPtoaxnBq7tPngZ9GaJx9au_SZEirMC96X64boQTNOHvAGiCKY9B870vRiJzPg6WA7Q30PjxGL6YcdBBxjNCNXXH-XWVi9HQZnG1U6HXGVY/4rq/r319z6YKTm2UnMhONNYNxA/h4/h001.0xX8a7SP7gLf1nKcn-EvXtAnsD9PC-Ejesh28G6sD8A
authors: [Data Elixir]
keywords: [coding agent, tools, harness, Claude Code, ellmer, LLM]
theme: IA
tone: tutorial
used_in: ["2026-06-23"]
---

## Résumé

Cet article démystifie ce qu'est réellement un agent de code (Claude Code, Cursor, Codex). Un agent, c'est un *harness* qui exécute des outils pour le compte d'un LLM. Un agent de **code** se distingue par six outils spécifiques qui lui permettent d'explorer et d'éditer un codebase comme un humain : lire, écrire, éditer un fichier, lister, chercher, lancer une commande. L'auteur démontre que seuls trois de ces six outils sont vraiment essentiels en construisant un mini-agent de code en R avec ellmer.

## Points clés

- Un agent est un harness avec des outils de lecture et d'écriture ; un agent de code ajoute les outils pour explorer et éditer un codebase.
- Six outils typiques : Read file, Write file, Edit file, List files, Search, Run command.
- Seuls trois (lire, écrire, lancer une commande) sont réellement essentiels pour un agent basique.
- Un bon agent de code embarque aussi un gros prompt système de bonnes pratiques, complexe (et facilement « reniflable »).
- L'auteur construit un agent minimal en R avec ellmer pour le prouver — lisible d'une traite.

## Analyse approfondie

Les agents de code comme Claude Code, Cursor et Codex ont pris d'assaut le domaine du génie logiciel. Depuis novembre 2025, ils ont radicalement changé la pratique du développement logiciel pour beaucoup de programmeurs (y compris moi), et dans le post de cette semaine je veux plonger dans ce qui les fait fonctionner.

Nous avons déjà parlé des outils (functions) et des harnesses (un système pour exécuter des outils pour le compte du LLM). Et vous savez qu'un agent est un harness avec des outils pour lire et écrire. Alors qu'est-ce qui fait d'un agent un agent de **code** ? La réponse, ce sont les outils spécifiques qu'il fournit : ceux qui permettent à un LLM d'explorer et d'éditer un codebase de la même façon qu'un humain le ferait.

La plupart des agents de code fournissent une variation des outils suivants :

- **Read file** : lire le contenu d'un fichier, ou d'une partie.
- **Write file** : créer un nouveau fichier avec du contenu frais.
- **Edit file** : faire une modification ciblée sur un fichier existant, en remplaçant généralement un morceau de texte par un autre.
- **List files** : montrer les fichiers et répertoires à un chemin donné pour que l'agent puisse s'orienter dans la structure du projet.
- **Search** : trouver les lignes correspondant à un motif à travers le codebase pour localiser rapidement le code pertinent.
- **Run command** : exécuter une commande shell arbitraire, ce qui permet à l'agent de faire tout le reste dont il pourrait avoir besoin.

Un bon agent de code contient aussi généralement un gros prompt avec des conseils de bonnes pratiques. Bien que ces prompts ne soient pas open source, ils sont assez faciles à renifler, donc divers contributeurs les ont extraits. C'est instructif d'y jeter un œil rien que pour sentir à quel point ils sont complexes.

Des six outils ci-dessus, seuls trois sont vraiment essentiels pour un agent de code basique. Pour le prouver, je vais construire un tout petit agent de code en R avec ellmer. On commencera de façon impitoyablement minimale — avec seulement read file, write file et run command — puis on montera en gamme. On perdra quelques agréments, mais en échange on obtient quelque chose qu'on peut lire en une seule fois.

(Suit l'implémentation des trois fonctions outils, puis l'ajout progressif des trois autres.)

## Pourquoi ça compte

Comprendre qu'un agent de code n'est « que » six fonctions dans un imperméable déplace l'attention du modèle vers le harness et les outils — exactement là où se joue la fiabilité, et là où l'ingénieur reprend la main.
