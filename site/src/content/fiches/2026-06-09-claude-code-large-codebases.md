---
title: "How Claude Code works in large codebases: Best practices and where to start"
date: 2026-06-09
url: https://link.mail.beehiiv.com/ss/c/u001.Ira8ofUIq_P_lCLURPEgQ4_vmR0U0HcWuynAcra7cQDl0FA5uE8y1OfRsCQEvVCTRVRCPhGGHesSA0-U2ZztSEAbNgw3-p5KnR6pl4MuWEy1ucGOjLbVDfBgV-2Lf50xDIKA5K_O1_hOk3d0TS7DCXN0jZnJyyA2VQKQWYinestqUAGeJvencIcZIDZeOTAewEEwsCWRHqsvYJjQ4-o7z8uK_SwhdNBkrplyj2yOL9s/4rc/T8LNCv72RLyBIyuO1pgQMA/h14/h001.lNdSsl_-gJbRzLsfeGs0LmzUpAtr6xEGWw1Xl7IM-Yo
authors: [Anthropic]
keywords: [Claude Code, large codebases, agentic search, RAG, monorepo, context]
theme: IA
tone: tutorial
used_in: ["2026-06-09"]
---

## Résumé

Cet article d'Anthropic décrit les patterns observés pour une adoption réussie de Claude Code dans de très grandes codebases : monorepos de plusieurs millions de lignes, systèmes legacy bâtis sur des décennies, dizaines de microservices répartis sur plusieurs dépôts, organisations à milliers de développeurs. Le point central : Claude Code navigue dans le code comme un ingénieur (parcours du système de fichiers, lecture, grep, suivi des références), sans index RAG à maintenir — une « recherche agentique » qui évite les écueils des pipelines d'embedding, à condition d'avoir assez de contexte de départ.

## Points clés

- Claude Code tourne en production sur des monorepos multi-millions de lignes, du legacy de plusieurs décennies, des architectures distribuées et des orgs à milliers de devs.
- Il navigue comme un ingénieur : parcourt le filesystem, lit les fichiers, utilise grep, suit les références.
- Pas d'index de codebase à construire, maintenir ou uploader sur un serveur ; tout est local.
- La recherche agentique évite les échecs du RAG, dont les pipelines d'embedding prennent du retard sur le code réel.
- Compromis : ça marche mieux quand l'agent a assez de contexte de départ pour savoir où chercher.
- Les patterns fonctionnent aussi sur des langages peu associés à l'IA (C, C++, C#, Java, PHP).

## Analyse approfondie

Claude Code tourne en production dans des monorepos de plusieurs millions de lignes, des systèmes legacy bâtis sur des décennies, des architectures distribuées couvrant des dizaines de dépôts, et au sein d'organisations comptant des milliers de développeurs. Ces environnements posent des défis que des codebases plus petites et plus simples ne posent pas : par exemple des commandes de build qui diffèrent dans chaque sous-répertoire, ou du code legacy éparpillé dans des dossiers sans racine commune.

L'article couvre les patterns observés qui ont mené à une adoption réussie de Claude Code à grande échelle. Le terme « large codebase » recouvre un large spectre de déploiements : monorepos de millions de lignes, systèmes legacy construits sur des décennies, dizaines de microservices répartis sur des dépôts séparés, ou n'importe quelle combinaison. Cela inclut aussi des langages que les équipes n'associent pas toujours aux outils de code IA, comme C, C++, C#, Java, PHP. (Claude Code y est plus performant que ce que la plupart des équipes anticipent, en particulier avec les sorties de modèles récentes.) Si chaque déploiement est façonné par son contrôle de version, sa structure d'équipe et ses conventions accumulées, les patterns présentés se généralisent et constituent un bon point de départ.

**Comment Claude Code navigue dans les grandes codebases.**

Claude Code navigue dans une codebase comme le ferait un ingénieur logiciel : il parcourt le système de fichiers, lit des fichiers, utilise grep pour trouver exactement ce dont il a besoin, et suit les références à travers le code. Il opère localement sur la machine du développeur et ne nécessite pas qu'un index de la codebase soit construit, maintenu ou uploadé sur un serveur.

Les outils de code IA basés sur le RAG fonctionnent en embeddant l'ensemble de la codebase et en récupérant les chunks pertinents au moment de la requête. À grande échelle, ces systèmes peuvent échouer parce que les pipelines d'embedding n'arrivent pas à suivre le rythme d'équipes d'ingénierie actives. Au moment où un développeur interroge l'index, celui-ci reflète la codebase telle qu'elle existait il y a des semaines, des jours, voire des heures. La récupération renvoie alors une fonction que l'équipe a renommée il y a deux semaines, ou référence un module supprimé au dernier sprint, sans aucune indication que l'un ou l'autre est obsolète.

La recherche agentique évite ces modes d'échec. Il n'y a pas de pipeline d'embedding ni d'index centralisé à maintenir tandis que des milliers d'ingénieurs commitent du nouveau code. L'instance de chaque développeur travaille à partir de la codebase vivante.

Mais l'approche a un compromis : elle fonctionne mieux quand Claude dispose d'assez de contexte de départ pour savoir où chercher. Cela signifie que la qualité de la navigation de Claude dépend du contexte initial qu'on lui fournit. (...)

## Pourquoi ça compte

L'article démontre que, à grande échelle, le facteur limitant n'est pas la capacité brute du modèle mais le contexte de départ et la stratégie de navigation. C'est la contrepartie concrète du modèle de maturité du contexte : la recherche agentique remplace le RAG, mais reste tributaire de la qualité du contexte qu'on lui donne.
