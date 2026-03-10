---
title: "Your LLM Doesn't Write Correct Code. It Writes Plausible Code."
date: 2026-03-09
url: "https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code"
authors: ["Katana Quant"]
keywords: [LLM, Rust, SQLite, performance, plausibilité]
theme: "IA"
tone: "opinion"
used_in: ["2026-03-09"]
---

## Résumé

Un développeur analyse une réécriture Rust de SQLite générée par LLM : le code compile, passe tous les tests et implémente correctement le format de fichier. Pourtant, un lookup sur 100 lignes prend 1 815 ms au lieu de 0,09 ms — soit 20 000 fois plus lent. L'article argumente que les LLMs optimisent pour la plausibilité, pas pour la correction, et que ce problème est systémique.

## Points clés

- Le code LLM compile, passe les tests, lit et écrit le bon format de fichier — mais est 20 171x plus lent sur les lookups par clé primaire
- Les LLMs sont entraînés à produire du code qui ressemble à du code correct, ce qui n'est pas la même chose que du code correct
- Un second cas d'étude confirme le pattern : le code généré fonctionne en surface mais échoue sur les propriétés non-fonctionnelles
- Les données de METR et GitClear confirment que le phénomène est systémique, pas anecdotique
- La citation clé : "LLMs optimize for plausibility over correctness"

## Analyse approfondie

Un des tests les plus simples qu'on puisse faire sur une base de données : un lookup par clé primaire sur 100 lignes. SQLite prend 0,09 ms. Une réécriture Rust générée par LLM prend 1 815 ms — soit 20 171 fois plus lent.

Le code compile, passe tous les tests, lit et écrit le bon format de fichier SQLite. Le README revendique le MVCC, la compatibilité fichier et une API C drop-in. À première vue, on dirait un moteur de base de données fonctionnel. Mais il ne l'est pas.

L'auteur a analysé le code source : 576 000 lignes de Rust réparties sur 625 fichiers — 3,7 fois plus que SQLite. L'architecture a les bons noms de modules, la bonne structure. Mais deux bugs majeurs se composent avec une série de choix individuellement défendables qui s'additionnent.

Premier bug : la fonction `is_rowid_ref()` ne reconnaît que trois noms magiques (rowid, _rowid_, oid) et ignore les colonnes déclarées comme INTEGER PRIMARY KEY. Dans SQLite, une seule ligne dans `where.c` convertit une référence de colonne nommée en XN_ROWID quand elle correspond à la colonne INTEGER PRIMARY KEY de la table — déclenchant une opération SeekRowid au lieu d'un scan complet. La réécriture a un B-tree fonctionnel avec une recherche binaire correcte en O(log n), mais le query planner ne l'appelle jamais pour les colonnes nommées. Chaque requête WHERE fait un scan linéaire : 10 000 comparaisons au lieu de ~700 étapes B-tree pour 100 lignes. O(n²) au lieu de O(n log n).

Second bug : chaque INSERT hors transaction déclenche un cycle complet d'autocommit avec `sync_all()` (équivalent fsync), là où SQLite utilise `fdatasync` — 1,6 à 2,7 fois moins coûteux sur SSD NVMe. 100 INSERT signifient 100 fsync, contre un seul en mode batch.

À ces deux bugs s'ajoutent plusieurs anti-patterns qui composent : un clone de l'AST à chaque hit de cache (SQLite réutilise un handle compilé via `sqlite3_prepare_v2()`), une allocation heap Vec<u8> de 4 Ko à chaque lecture de page (SQLite retourne un pointeur direct dans la mémoire épinglée du cache), un rechargement complet du schéma après chaque autocommit (SQLite vérifie un simple cookie entier), et un formatage eager dans le hot path. Chacun de ces choix semblait sûr individuellement : « on clone parce que l'ownership Rust rend les références partagées complexes », « on utilise sync_all parce que c'est le défaut sûr ». Mais le résultat est ~2 900 fois plus lent.

L'article cite un second projet du même auteur : un démon de nettoyage de disque de 82 000 lignes de Rust, avec 192 dépendances, un tableau de bord terminal à sept écrans avec palette de recherche fuzzy, un moteur de scoring bayésien, un prévisionniste EWMA avec contrôleur PID, et un pipeline de téléchargement d'assets avec URLs miroir — pour résoudre un problème qu'une seule ligne de cron résout. Le LLM a généré ce qui était décrit, pas ce qui était nécessaire.

La recherche académique confirme le caractère systémique. L'étude METR (juillet 2025, mise à jour février 2026) avec 16 développeurs open-source expérimentés a montré que les participants utilisant l'IA étaient 19 % plus lents, pas plus rapides — tout en croyant avoir été accélérés de 20 %. L'analyse GitClear de 211 millions de lignes modifiées (2020-2024) rapporte que le code copié-collé a augmenté tandis que le refactoring a décliné — pour la première fois, les lignes copiées-collées dépassent les lignes refactorisées. Le benchmark Mercury (NeurIPS 2024) confirme empiriquement que les LLMs de code atteignent ~65 % en correction mais moins de 50 % quand l'efficacité est aussi requise. Le benchmark BrokenMath (NeurIPS 2025) montre que même GPT-5 produit des « preuves » sycophantiques de théorèmes faux 29 % du temps quand l'utilisateur implique que l'énoncé est vrai. Le rapport DORA 2024 de Google rapporte que chaque augmentation de 25 % de l'adoption IA au niveau équipe est associée à une baisse estimée de 7,2 % de la stabilité des livraisons.

La conclusion de l'auteur : les LLMs optimisent pour la plausibilité, pas pour la correction. Le code n'est pas le vôtre tant que vous ne le comprenez pas assez bien pour le casser. Les vibes ne suffisent pas — définissez ce que « correct » signifie, puis mesurez.

## Pourquoi ça compte

Cet article met le doigt sur l'angle mort principal de l'IA générative pour le code : les tests unitaires ne suffisent pas à garantir la qualité. Les propriétés non-fonctionnelles (performance, scalabilité) échappent structurellement aux LLMs.
