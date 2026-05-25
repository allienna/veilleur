---
title: "--dangerously-skip-reading-code"
date: 2026-05-25
url: https://olano.dev/blog/dangerously-skip/
authors: [olano.dev]
keywords: [LLM, revue de code, loi d'Amdahl, organisation, responsabilité]
theme: IA
tone: opinion
used_in: ["2026-05-25"]
---

## Résumé

Et si on cessait de lire le code généré par les LLM, comme on a cessé de lire l'assembleur ou le JavaScript transpilé ? L'auteur explore cette hypothèse provocante : puisque les LLM produisent du code non déterministe plus vite qu'on ne peut le relire, on ne peut plus sérieusement prétendre revoir et approuver chaque diff. Mais arrêter de lire ne veut pas dire arrêter d'être rigoureux — cela signifie déplacer la rigueur ailleurs. Et surtout, c'est une décision organisationnelle, pas individuelle.

## Points clés

- Les LLM génèrent du code plus vite et de façon non déterministe ; relire chaque diff devient illusoire.
- Cesser de lire le code source pourrait être assumé comme on a cessé de lire l'assembleur — le langage haut niveau devenant une nouvelle forme de « code machine ».
- Ce n'est pas un choix individuel : c'est une décision d'organisation, pour des raisons de responsabilité *et* à cause de la loi d'Amdahl.
- Sans réorganiser les processus, maximiser la seule vitesse de génération ne produit aucun gain de productivité réel.
- Il faut réduire les humains-dans-la-boucle, la coordination, la friction et le gatekeeping, et confier aux ingénieurs des pans entiers de travail avec autonomie de décision.

## Analyse approfondie

L'auteur prolonge un précédent billet où il affirmait qu'il serait irresponsable de supposer qu'on n'aura plus jamais à lire ni à déboguer notre code — de croire que tout problème surgissant pourra être corrigé par les LLM. Jusqu'ici, c'était le travail du programmeur de comprendre et maintenir le code source, comme proxy de la compréhension et de la maintenance du système logiciel. Nous sommes tenus pour responsables de ce que produisent les LLM.

Mais, demande-t-il, et si ce n'était plus le cas ? Et si, après avoir dûment communiqué les risques et les arbitrages à la direction, celle-ci décidait quand même de prendre ces risques ? Rien d'inédit : les entreprises, surtout les startups tech, font régulièrement des compromis de court terme pour gagner en productivité, devancer la concurrence, séduire des investisseurs.

S'il existe un mandat organisationnel pour minimiser le temps passé à coder grâce aux LLM, c'est une nouvelle contrainte avec laquelle composer. On peut alors définir ce qu'est un bon travail d'ingénierie dans ce contexte. On peut cesser de lire le code généré par les LLM, exactement comme on ne lit pas l'assembleur, le bytecode ou le JavaScript transpilé : notre code source en langage haut niveau devient une autre forme de code machine.

Ce déclic est venu à l'auteur après la lecture du rapport de retraite de Thoughtworks. Les LLM produisent une sortie non déterministe et génèrent du code bien plus vite qu'on ne peut le lire ; on ne peut donc plus sérieusement espérer revoir, comprendre et approuver chaque diff. Mais cela ne signifie pas qu'on cesse d'être rigoureux : cela peut vouloir dire qu'il faut déplacer la rigueur ailleurs.

Point fondamental : ce n'est ni le choix d'un individu ni celui d'une équipe. Ce doit être une décision organisationnelle — non seulement pour des questions de gestion du risque et de responsabilité, mais aussi à cause de la loi d'Amdahl. Si l'on ne maximise que la vitesse de génération de code sans réorganiser les structures et les processus dans lesquels s'inscrit le travail, il n'y aura aucun gain de productivité tangible.

On ne peut pas avoir des devs qui pondent 20 000 lignes de « slop » par jour et attendre des autres qu'ils les lisent, les comprennent, et encore moins les approuvent. On ne peut pas tirer parti des agents si notre unité de travail reste « ajouter un endpoint à l'API REST ». On ne peut pas attendre d'un Product Owner qu'il alimente assez de travail pour occuper une équipe « two-pizza » si chaque ingénieur peut prendre quatre tâches à la fois et faire tourner des agents en dehors des heures.

La conclusion est structurelle : il faut retirer les humains-dans-la-boucle, réduire la coordination, la friction, la bureaucratie et le gatekeeping. Il faut un approvisionnement quasi infini d'exigences, des ingénieurs agissant comme des pseudo-designers produit, propriétaires de flux entiers de travail, avec le pouvoir de prendre des décisions autonomes.

## Pourquoi ça compte

Ce billet recadre le débat : la vraie question n'est pas technique (« faut-il lire le code de l'IA ? ») mais organisationnelle — où placer la rigueur et comment réarchitecturer les processus quand le code devient quasi gratuit.
