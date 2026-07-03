---
title: "A coding agent is six functions in a trenchcoat"
date: 2026-07-03
url: https://elink56e.dataelixir.com/ss/c/u001.MwQ9-DqNm-0ctGFRWAEvcbeJ5lreZsNER36P-UBzynN5fx2bnRSnZjvgfM9GduSJkvYP4EyXXz3c2P5vM3wu6X8daRliJYZ1wBl7W8NPUIBIo4BRQM1UL93TawEXtDuejPtoaxnBq7tPngZ9GaJx9au_SZEirMC96X64boQTNOHvAGiCKY9B870vRiJzPg6WA7Q30PjxGL6YcdBBxjNCNXXH-XWVi9HQZnG1U6HXGVY/4rx/v8zq24JpQCSh4Zh1V2CdNw/h16/h001.ebGEYYaeNgQDs8HTU-aQxf0LaAM13Lr9HqKq672OxRk
authors: [Data Elixir]
keywords: [agent de code, tools, harness, LLM, sécurité, ellmer]
theme: Tech
tone: tutorial
used_in: ["2026-07-03"]
---

## Résumé

Cet article démystifie ce qu'est réellement un agent de code. Derrière des outils comme Claude Code, Cursor ou Codex se cache une mécanique simple : un LLM auquel on fournit quelques fonctions pour lire, écrire, éditer, lister, chercher et exécuter des commandes. L'auteur prouve que trois outils suffisent à construire un agent minimal fonctionnel, en le codant de zéro en R avec ellmer. Il montre ensuite comment ajouter la recherche, l'édition ciblée, et surtout des garde-fous de sécurité pour empêcher le modèle de sortir du répertoire projet.

## Points clés

- Un agent de code est simplement un « harness » (système d'exécution d'outils pour le LLM) équipé d'outils de lecture et d'écriture spécifiques à une base de code.
- Les six outils classiques : lire un fichier, écrire un fichier, éditer un fichier, lister les fichiers, chercher un motif, exécuter une commande shell.
- Trois outils suffisent (lire, écrire, exécuter) pour un agent minimal viable.
- Un bon agent embarque aussi un gros prompt système de bonnes pratiques (souvent extractible même s'il n'est pas open source).
- La sécurité est centrale : sans garde-fou, le modèle peut lire ou écrire hors du projet ; l'auteur ajoute une fonction `safe_path()` qui vérifie que tout chemin reste sous le répertoire de travail.

## Analyse approfondie

Les agents de code comme Claude Code, Cursor et Codex ont pris d'assaut le domaine de l'ingénierie logicielle. Depuis novembre 2025, ils ont radicalement transformé la pratique du développement pour de nombreux programmeurs (moi y compris), et dans le billet de cette semaine je veux plonger dans ce qui les fait fonctionner.

Nous avons déjà parlé des outils (fonctions) et des harnesses (un système pour exécuter des outils pour le compte du LLM). Et vous savez qu'un agent est un harness doté d'outils de lecture et d'écriture. Alors qu'est-ce qui fait d'un agent un agent **de code** ? La réponse tient aux outils spécifiques qu'il fournit : ceux qui permettent à un LLM d'explorer et d'éditer une base de code de la même façon qu'un humain le ferait.

La plupart des agents de code fournissent une variation des outils suivants :

- **Read file** : lire le contenu d'un fichier, ou une partie de celui-ci.
- **Write file** : créer un nouveau fichier avec un contenu neuf.
- **Edit file** : effectuer une modification ciblée sur un fichier existant, généralement en remplaçant un bloc de texte par un autre.
- **List files** : afficher les fichiers et répertoires d'un chemin donné pour que l'agent puisse s'orienter dans la structure du projet.
- **Search** : trouver les lignes correspondant à un motif dans la base de code pour localiser rapidement le code pertinent.
- **Run command** : exécuter une commande shell arbitraire, ce qui permet à l'agent de faire tout ce dont il pourrait avoir besoin d'autre.

Un bon agent de code contient aussi généralement un gros prompt avec des conseils sur les bonnes pratiques. Bien que ces prompts ne soient pas open source, ils sont assez faciles à débusquer, si bien que diverses personnes les ont extraits. Il est instructif d'y jeter un œil, ne serait-ce que pour prendre la mesure de leur complexité.

Des six outils ci-dessus, seuls trois sont vraiment essentiels pour un agent de code basique. Pour le prouver, l'auteur construit un tout petit agent de code en R avec ellmer. On part d'un minimalisme radical — juste read file, write file et run command — puis on monte en puissance. On perd quelques commodités, mais en échange on obtient quelque chose qui se lit d'une traite.

Les trois fonctions d'outils sont écrites dans un R volontairement ennuyeux : `read_file` lit les lignes d'un fichier et les renvoie concaténées ; `write_file` écrit le contenu et confirme l'action ; `run_command` exécute une commande système et retourne sa sortie. Chaque fonction renvoie une chaîne qui est réinjectée au LLM comme résultat de l'appel d'outil.

On crée ensuite un chat et on enregistre les trois fonctions comme outils (ici avec `chat_anthropic` sur claude-sonnet-4-5). Les descriptions comptent : elles indiquent au LLM quand et comment mobiliser chaque outil. Un prompt système basique précise que l'assistant travaille dans le répertoire courant, doit lire un fichier avant de l'éditer, lancer les tests pertinents après modification, et continuer jusqu'à ce que la tâche soit accomplie. Et voilà tout l'agent ! On peut alors lui confier une tâche simple comme « Trouve la fonction qui parse les dates et ajoute-lui un test unitaire ».

Pour aller plus loin, l'auteur implémente les outils `list_files` et `search_files`, puis s'attaque à leur sécurité. Sans précaution, le modèle peut atteindre des fichiers hors du projet. La parade : une fonction `safe_path()` qui résout le chemin (en écrasant les `..` et en suivant les liens symboliques) et vérifie qu'il reste sous le répertoire de travail, sinon elle lève une erreur. Ce wrapper doit être appliqué à `read_file`, `write_file`, `list_files` — et pas seulement à la recherche.

Enfin, l'auteur ajoute un outil `edit_file` qui remplace une portion exacte de texte (le texte « old » devant apparaître une seule fois dans le fichier), à préférer à `write_file` pour ne modifier qu'une partie d'un fichier existant. Il annonce revenir plus tard en détail sur la sécurité, notamment sur les approches pour rendre les outils généraux (comme l'exécution d'un shell) aussi sûrs que possible.

## Pourquoi ça compte

Comprendre qu'un agent de code n'est ni magique ni opaque — juste une poignée de fonctions autour d'un LLM — permet de le cadrer, de le sécuriser et de garder un regard critique sur ce qu'il fait, au lieu de le traiter comme une boîte noire.
