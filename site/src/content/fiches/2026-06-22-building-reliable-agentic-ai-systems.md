---
title: "Building Reliable Agentic AI Systems"
date: 2026-06-22
url: https://martinfowler.com/articles/reliable-llm-bayer.html
authors: [martinfowler.com, Bayer]
keywords: [agentic, RAG, context engineering, harness engineering, fiabilité]
theme: IA
tone: research
used_in: ["2026-06-22"]
---

## Résumé

Étude de cas de Bayer sur PRINCE, un système agentique construit sur de l'Agentic RAG pour la recherche préclinique. L'article détaille l'architecture technique et les décisions d'ingénierie, et montre que la fiabilité d'un système agentique ne vient pas du modèle, mais de l'échafaudage qui l'entoure. Les auteurs relisent leurs choix à travers deux notions : le *context engineering* (quelle information chaque modèle reçoit) et le *harness engineering* (orchestration, frontières des outils, persistance d'état, retries, fallbacks, validation, boucles de réflexion, observabilité, revue humaine).

## Points clés

- La recherche préclinique est complexe et riche en données ; les recherches par mots-clés (logique booléenne rigide) échouent face à des questions nuancées.
- Le RAG combine la puissance générative des LLM et la précision de la recherche d'information.
- PRINCE transforme l'accès aux données précliniques en une expérience conversationnelle intuitive.
- *Context engineering* : ce que chaque modèle reçoit ou non, et comment le contexte circule entre étapes spécialisées (recherche, réflexion, écriture).
- *Harness engineering* : l'échafaudage autour des modèles — orchestration, frontières des outils, persistance d'état, retries, fallbacks, validation, boucles de réflexion, observabilité, revue humaine.

## Analyse approfondie

La découverte de médicaments en phase préclinique est intrinsèquement complexe et intensive en données. Les chercheurs font face au défi majeur d'accéder efficacement à de vastes volumes d'informations générées durant cette phase critique et de les analyser. Les méthodes traditionnelles de recherche par mots-clés, souvent dépendantes d'une logique booléenne rigide, sont fréquemment insuffisantes face à la nature nuancée et complexe des questions de recherche préclinique.

L'avènement des grands modèles de langage (LLM) a présenté une opportunité de transformation. En combinant la puissance générative des LLM avec la précision des systèmes de recherche d'information, le Retrieval-Augmented Generation (RAG) a émergé comme une technique prometteuse. Cette approche a le potentiel de révolutionner l'accès aux données précliniques, en permettant aux chercheurs de poser des questions complexes en langage naturel et de recevoir des réponses précises, riches en contexte, ancrées dans des données propriétaires.

Reconnaissant ce potentiel tôt, Bayer s'est engagé à explorer comment ces technologies pourraient répondre à des défis de longue date dans la recherche préclinique.

Dans ce billet, nous partageons ce parcours — comment l'investissement précoce de Bayer dans l'IA générative a abouti à PRINCE, un système d'IA agentique construit sur l'Agentic RAG. Cette étude de cas explore l'architecture technique, les décisions d'ingénierie et les leçons apprises en transformant la recherche de données précliniques d'un labyrinthe ardu en une expérience conversationnelle intuitive.

Beaucoup des décisions d'ingénierie derrière PRINCE peuvent désormais être comprises à travers le prisme du *context engineering* et du *harness engineering*, même si lorsque le système a été conçu, nous n'utilisions pas ces termes. Le context engineering a façonné quelle information chaque modèle recevait, ce qu'il ne recevait pas, et comment le contexte circulait entre des étapes spécialisées telles que la recherche, la réflexion et l'écriture. Le harness engineering a façonné l'échafaudage autour des modèles : orchestration, frontières des outils, persistance d'état, retries, fallbacks, validation, boucles de réflexion, observabilité et revue humaine.

Si ce billet se concentre sur l'architecture technique et les défis d'ingénierie, notre article publié dans *Frontiers in Artificial Intelligence* couvre l'évolution produit et l'impact business plus en détail.

### Le défi : naviguer dans le labyrinthe des données précliniques

Le paysage de la recherche préclinique chez Bayer, comme dans beaucoup de grandes organisations pharmaceutiques, se caractérise par un éventail diversifié et étendu de données. Cela inclut des jeux de données hautement structurés issus de diverses études, aux côtés de vastes quantités d'informations non structurées intégrées dans des documents textuels tels que des rapports d'étude, des publications et des soumissions réglementaires. Les chercheurs rencontraient fréquemment des obstacles significatifs pour accéder à cette information et l'analyser efficacement.

## Pourquoi ça compte

PRINCE illustre, par un cas industriel réel, le principe central de la veille du jour : la fiabilité d'un système agentique ne vient pas du modèle mais du harnais (validation, fallbacks, revue humaine, observabilité). C'est la preuve concrète que « superviser l'agent » est une discipline d'ingénierie à part entière.
