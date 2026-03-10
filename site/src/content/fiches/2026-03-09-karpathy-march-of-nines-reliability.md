---
title: "Karpathy's March of Nines shows why 90% AI reliability isn't even close to enough"
date: 2026-03-09
url: "https://venturebeat.com/technology/karpathys-march-of-nines-shows-why-90-ai-reliability-isnt-even-close-to"
authors: ["VentureBeat"]
keywords: [fiabilité, march of nines, Karpathy, workflows agentiques, production]
theme: "IA"
tone: "news"
used_in: ["2026-03-09"]
---

## Résumé

VentureBeat explore le concept de "March of Nines" d'Andrej Karpathy : chaque neuf supplémentaire de fiabilité (90% → 99% → 99,9%) demande autant d'effort d'ingénierie que le précédent. Un workflow agentique en 10 étapes à 90% par étape ne donne que 35% de succès bout-en-bout. L'article propose des stratégies concrètes (SLOs, retrieval hardening, structured outputs, circuit breakers) pour progresser vers la fiabilité enterprise.

## Points clés

- Atteindre 90% de fiabilité n'est que "le premier neuf" — chaque neuf supplémentaire exige un effort comparable
- Un workflow en 10 étapes à 90%/étape = 34,87% de succès end-to-end ; à 99%/étape = 90,4%
- La frontière entre "prototype impressionnant" et "outil de production" se joue sur ces pourcentages
- Stratégies proposées : SLOs par composant, hardening du retrieval, structured outputs, circuit breakers
- Les plateformes d'évaluation deviennent une infrastructure critique pour mesurer et améliorer ces métriques

## Analyse approfondie

« Quand vous obtenez une démo et que quelque chose fonctionne 90 % du temps, c'est juste le premier neuf », explique Andrej Karpathy. La « Marche des Neuf » cadre une réalité de production courante : on peut atteindre les premiers 90 % de fiabilité avec une bonne démo, et chaque neuf supplémentaire (90 % → 99 % → 99,9 %) exige un effort d'ingénierie comparable au précédent.

Les workflows agentiques composent les échecs de manière multiplicative. Un flux enterprise typique peut inclure : parsing d'intention, récupération de contexte, planification, un ou plusieurs appels d'outils, validation, formatage et journalisation d'audit. Si un workflow comporte n étapes avec une probabilité de succès p par étape, le succès bout-en-bout est approximativement p^n. Les pannes corrélées (auth, rate limits, connecteurs) domineront à moins de durcir les dépendances partagées.

Le tableau chiffré est parlant : avec 10 étapes à 90 % chacune, le succès end-to-end tombe à 34,87 % — soit environ 6,5 interruptions par jour pour 10 workflows quotidiens, territoire de prototype. À 99 % par étape, on atteint 90,44 % — acceptable pour une démo mais les interruptions restent fréquentes en usage réel. À 99,9 %, le taux de succès est 99 % mais ça reste ressenti comme peu fiable. Ce n'est qu'à 99,99 % par étape qu'on commence à ressentir la fiabilité d'un logiciel enterprise dépendable, avec environ une interruption tous les 3,3 mois.

L'article propose neuf leviers concrets pour ajouter des neuf. Premier levier : contraindre l'autonomie avec un graphe de workflow explicite — les appels modèle s'inscrivent dans une machine à états ou un DAG avec outils autorisés, tentatives maximales et prédicat de succès par nœud. Deuxième : imposer des contrats à chaque frontière via JSON Schema/protobuf, avec validation côté serveur avant toute exécution d'outil. Troisième : superposer les validateurs en trois couches — syntaxe, sémantique (intégrité référentielle, bornes numériques) et règles métier (approbations, résidence des données).

Quatrième levier : router par risque en utilisant des signaux d'incertitude (classifieurs, vérifications de cohérence, second modèle vérificateur) pour décider du routage. Cinquième : traiter les appels d'outils comme des systèmes distribués — timeouts par outil, backoff avec jitter, circuit breakers, limites de concurrence, versionnement des schémas d'outils. Sixième : rendre le retrieval prédictible et observable — suivre le taux de retrieval vide, la fraîcheur des documents, déployer les changements d'index avec des canaris.

Septième : construire un pipeline d'évaluation en production avec un golden set alimenté par les incidents, shadow mode et canaris A/B avec rollback automatique sur régression des SLI. Huitième : investir dans l'observabilité — émettre des traces/spans par étape, stocker les prompts et I/O des outils avec contrôles d'accès stricts, classifier chaque échec dans une taxonomie. Neuvième : fournir un curseur d'autonomie avec des fallbacks déterministes — par défaut en lecture seule ou actions réversibles, confirmation explicite pour les écritures irréversibles, modes safe par tenant.

L'article propose aussi un sketch d'implémentation : un wrapper `run_step` autour de chaque étape modèle/outil qui convertit l'imprévisibilité en contrôle piloté par politique — validation stricte, retries bornés, timeouts, télémétrie et fallbacks explicites.

Le rapport McKinsey 2025 confirme l'enjeu business : 51 % des organisations utilisant l'IA ont connu au moins une conséquence négative, et près d'un tiers des conséquences étaient liées à l'inexactitude de l'IA. Les neuf arrivent par l'ingénierie disciplinée : workflows bornés, interfaces strictes, dépendances résilientes et boucles d'apprentissage opérationnel rapides.

## Pourquoi ça compte

Ce cadre conceptuel offre un langage commun pour discuter de la fiabilité IA en entreprise. Il explique pourquoi tant de POC ne passent pas en production et donne une feuille de route d'ingénierie concrète.
