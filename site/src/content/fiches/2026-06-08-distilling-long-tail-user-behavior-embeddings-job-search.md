---
title: "Distilling Long-Tail User Behavior into Scalable Embeddings for Job Search"
date: 2026-06-08
url: https://substack.com/redirect/1e63959d-c323-4d37-aeac-57436d7161fe?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Marsan Ma, Nikhil Lopes, Raj Amrit, Hong Lu, Dipankar Biswas, Trent Kyono]
keywords: [embeddings, recommandation, modeles de sequence, distillation, feature store]
theme: IA
tone: research
used_in: ["2026-06-08"]
---

## Résumé

L'article décrit un système de modélisation du comportement utilisateur (UBM) pour la recherche d'emploi, conçu pour résoudre la tension entre des historiques comportementaux riches et la contrainte de latence à la milliseconde en production. L'idée centrale : faire la modélisation séquentielle coûteuse une seule fois, hors ligne, avec de gros modèles, puis distiller l'historique de chaque utilisateur en un embedding compact réutilisable de nombreuses fois en ligne. Servi via un feature store, cet embedding s'intègre aux modèles de production existants avec un minimum de changements et produit des gains constants de plusieurs pourcents sur plusieurs surfaces à fort trafic.

## Points clés

- Les modèles en production sont rarement les plus gros qu'on sache entraîner : ils sont compacts, sensibles à la latence, et doivent scorer d'énormes ensembles de candidats sous contrainte de coût.
- La modélisation tabulaire classique force des compromis qui déforment l'intention : fenêtres de taille fixe, agrégations agressives, features one-hot qui perdent la similarité sémantique.
- On modélise le comportement comme des séquences, à la manière de phrases en NLP (jobs vus, cliqués, sauvegardés, candidatés, avec métadonnées).
- Un gros modèle hors ligne lit les longs historiques et émet un embedding ; de nombreux petits modèles en ligne le consomment comme une feature dense ordinaire.
- L'encodeur de jobs (Deep & Cross Network) est réutilisé sur tous les flux pour garder un espace d'embedding cohérent.
- L'auto-attention sert à débruiter les longs historiques et à séparer l'intention durable des comportements ponctuels.

## Analyse approfondie

*Auteurs : Marsan Ma, Nikhil Lopes, Raj Amrit, Hong Lu, Dipankar Biswas, Trent Kyono — Direction : Iris Wang, Madhu Kurup.*

Les systèmes de recommandation et de ranking alimentent bon nombre des expériences les plus importantes des grandes plateformes internet. Pourtant, les modèles qui tournent en production sont rarement les plus gros que l'on puisse entraîner. Ce sont généralement des modèles supervisés compacts, sensibles à la latence, qui doivent scorer d'énormes ensembles de candidats pour des millions d'utilisateurs sous de fortes contraintes de coût.

Cela crée une tension pratique :

- On veut utiliser des historiques comportementaux riches et de long terme, et du deep learning moderne.
- On a quand même besoin d'une latence à la milliseconde pour des systèmes de ranking, de recommandation et d'enchères à fort trafic.

Cet article décrit comment nous avons traité cette tension dans la recherche d'emploi en construisant un système de modélisation du comportement utilisateur (UBM) qui apprend des historiques de longue traîne hors ligne et les distille en embeddings utilisateur compacts, consommables par de nombreux modèles en ligne.

À haut niveau, UBM :

- Exploite le comportement utilisateur de long terme avec des modèles de séquence profonds.
- Distille l'historique de chaque utilisateur en un embedding de longueur fixe.
- Rend cet embedding disponible via un feature store.
- Permet aux modèles de production existants d'utiliser l'embedding avec des changements de serving minimes.
- Produit des gains constants de plusieurs pourcents sur plusieurs surfaces à fort trafic.

L'idée centrale est simple : faire la modélisation séquentielle coûteuse une fois, hors ligne, et réutiliser la représentation utilisateur obtenue de nombreuses fois en ligne.

### Pourquoi le comportement de longue traîne est difficile à utiliser directement en production

Pour une plateforme d'emploi, comprendre les chercheurs d'emploi est central pour faire correspondre les bonnes personnes aux bons postes. L'historique d'un utilisateur peut inclure de nombreux signaux tout au long du parcours de recrutement : requêtes de recherche (titres, mots-clés, entreprises, lieux), impressions et clics sur des offres, sauvegardes et favoris, débuts et finalisations de candidatures, réponses des employeurs et résultats en aval.

En principe, cet historique est très précieux. En pratique, la modélisation tabulaire traditionnelle force plusieurs compromis. D'abord, on garde des fenêtres de taille fixe (les K actions les plus récentes) et on jette le reste. Ensuite, on agrège agressivement les séquences en statistiques telles que « top des mots de titre » ou « fraction de clics dans l'industrie X ». Enfin, on s'appuie sur des features one-hot ou éparses qui perdent la similarité sémantique entre titres, compétences, entreprises et industries.

Ces simplifications peuvent déformer l'intention de l'utilisateur. Prenons un chercheur d'emploi qui a candidaté à des postes d'ingénieur civil, exploré ensuite des rôles de formateur en logiciels médicaux, puis s'est finalement stabilisé dans la gestion de comptes senior. Une agrégation naïve sur les tokens de titre pourrait sur-pondérer le mot « software » et pousser le système vers des recommandations d'ingénierie logicielle, alors même que le comportement récent et constant de l'utilisateur pointe ailleurs.

En parallèle, servir directement des modèles de séquences empilés sur l'historique brut par impression ne tenait pas dans notre infrastructure de production existante, où les systèmes à fort trafic doivent scorer de grands ensembles de candidats dans des budgets stricts de latence et de coût. Il nous fallait un système où de grands modèles puissent apprendre des séquences brutes hors ligne, puis alimenter une représentation distillée dans les modèles en ligne compacts qui portent déjà le trafic de production.

### Modéliser le comportement comme de la modélisation de séquences

Nous modélisons le comportement utilisateur comme des séquences, à la manière de phrases en traitement du langage naturel : séquences de jobs vus, cliqués, sauvegardés ou candidatés (avec métadonnées : titre, lieu, salaire, entreprise, catégorie), séquences de requêtes de recherche et leurs attributs, et autres événements contextuels ordonnés dans le temps.

Les modèles de séquence sont utiles ici parce qu'ils savent débruiter les longs historiques, capturer la structure temporelle et apprendre les relations sémantiques entre jobs, requêtes et utilisateurs. La contrainte de serving façonne l'architecture : un grand modèle hors ligne lit les longs historiques et émet un embedding utilisateur, tandis que de nombreux petits modèles en ligne consomment cet embedding comme une feature dense ordinaire. Conceptuellement : la modélisation lourde des séquences se fait hors ligne ; le scoring léger se fait en ligne, de nombreuses fois.

### Architecture : des événements bruts aux embeddings utilisateur

**1. Encoder jobs et événements.** La première étape encode les jobs et événements individuels en vecteurs denses. Chaque job comporte plusieurs types de features : numériques (salaire, signaux de séniorité), catégorielles (lieu, catégorie, entreprise), multi-hot (titres normalisés, compétences, industries). Chaque type est mappé en embeddings, concaténés puis passés dans un Deep & Cross Network, produisant un embedding de job compact qui capture les interactions linéaires et non linéaires. Le même encodeur de jobs est réutilisé sur tous les flux comportementaux afin que toutes les séquences vivent dans un espace d'embedding cohérent.

**2. Construire les séquences de comportement.** Nous sommes passés par deux générations d'encodeurs : un premier design multi-séquences, puis le design unifié mono-séquence actuel. Dans la première version de production, l'historique était traité comme multi-canal : chaque type d'action était une séquence temporelle distincte d'embeddings de jobs (Apply, Click, Impression…). Chaque séquence inclut des encodages positionnels pour que le modèle raisonne sur la récence, l'ordre et les motifs temporels, au lieu de traiter l'historique comme un ensemble non ordonné.

**3. Débruiter les longs historiques avec l'auto-attention.** Les longs historiques sont bruités : les gens explorent, changent de direction, comparent des rôles de façon désinvolte ou cliquent sur des offres faiblement pertinentes. Le modèle de séquence doit séparer l'intention durable du comportement ponctuel.

## Pourquoi ça compte

C'est un patron d'architecture réutilisable bien au-delà de la recherche d'emploi : déporter le calcul lourd hors ligne et distiller en une représentation compacte est souvent la meilleure réponse à la tension entre richesse des modèles et contraintes de latence/coût en production.
