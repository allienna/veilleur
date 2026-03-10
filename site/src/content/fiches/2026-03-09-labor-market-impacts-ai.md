---
title: "Labor market impacts of AI: A new measure and early evidence"
date: 2026-03-09
url: "https://www.anthropic.com/research/labor-market-impacts"
authors: ["Anthropic"]
keywords: [marché du travail, exposition IA, emploi, embauches, observed exposure]
theme: "IA"
tone: "research"
used_in: ["2026-03-09"]
---

## Résumé

Anthropic publie une recherche introduisant la métrique "observed exposure" qui combine la capacité théorique des LLMs avec les données d'usage réel. Résultat principal : la couverture réelle de l'IA reste une fraction de sa capacité théorique. Pas d'augmentation systématique du chômage chez les travailleurs les plus exposés, mais des signaux précoces de ralentissement des embauches de jeunes travailleurs dans les métiers exposés.

## Points clés

- La métrique "observed exposure" combine capacité théorique du LLM et données d'usage réel — plus fiable que les estimations purement théoriques
- Les travailleurs les plus exposés tendent à être plus âgés, plus éduqués, mieux payés et majoritairement féminins
- Pas de hausse systématique du chômage depuis fin 2022 pour les métiers les plus exposés
- Signal précoce : les embauches de jeunes travailleurs ralentissent dans les métiers exposés
- L'écart entre exposition théorique et usage réel reste très large

## Analyse approfondie

Anthropic introduit une nouvelle mesure du risque de déplacement par l'IA : l'« observed exposure » (exposition observée), qui combine la capacité théorique des LLMs avec les données d'usage réel, en pondérant plus fortement les usages automatisés (plutôt qu'augmentatifs) et professionnels.

L'approche croise trois sources de données : la base O*NET qui énumère les tâches associées à environ 800 métiers américains, les données d'usage propres à Anthropic (mesurées dans l'Anthropic Economic Index), et les estimations d'exposition théorique de Eloundou et al. (2023) qui scorent chaque tâche : 1 si un LLM seul peut doubler la vitesse d'exécution, 0,5 si des outils supplémentaires sont nécessaires, 0 sinon. 97 % des tâches observées dans les quatre rapports précédents de l'Economic Index tombent dans les catégories théoriquement réalisables.

L'écart entre capacité théorique et usage réel reste très large. Par exemple, Claude ne couvre actuellement que 33 % des tâches dans la catégorie Informatique et Mathématiques, alors que 94 % sont théoriquement réalisables. Beaucoup de tâches théoriquement possibles n'apparaissent pas dans l'usage réel en raison de limitations des modèles, contraintes légales, exigences logicielles spécifiques ou étapes de vérification humaine.

Les métiers les plus exposés selon cette mesure sont les programmeurs informatiques (75 % de couverture), suivis des représentants du service client dont les tâches principales apparaissent de plus en plus dans le trafic API, et des opérateurs de saisie de données (67 % de couverture). À l'autre extrémité, 30 % des travailleurs ont une couverture nulle — cuisiniers, mécaniciens moto, maîtres-nageurs, barmans.

Le profil démographique des travailleurs les plus exposés est notable. Ils tendent à être 16 points de pourcentage plus féminins, 11 points plus blancs, et presque deux fois plus susceptibles d'être asiatiques que le groupe non exposé. Ils gagnent 47 % de plus en moyenne et ont des niveaux d'éducation plus élevés : les titulaires d'un diplôme de troisième cycle représentent 17,4 % du groupe le plus exposé contre 4,5 % du groupe non exposé.

Les projections du Bureau of Labor Statistics valident partiellement la mesure : pour chaque augmentation de 10 points de pourcentage de la couverture, la projection de croissance de l'emploi diminue de 0,6 point. Cette corrélation n'existe pas avec la mesure purement théorique d'Eloundou et al.

L'analyse des tendances du chômage via le Current Population Survey ne montre pas d'augmentation systématique pour les métiers les plus exposés depuis fin 2022. Le changement moyen dans l'écart depuis la sortie de ChatGPT est faible et non significatif. Le cadre analytique pourrait détecter des augmentations différentielles de l'ordre de 1 point de pourcentage.

Cependant, un signal précoce émerge pour les jeunes travailleurs. En utilisant la dimension panel du CPS, l'étude mesure le taux d'entrée en emploi des 22-25 ans dans les métiers exposés vs non exposés. Les séries divergent visuellement en 2024 : le taux d'entrée dans les métiers exposés diminue d'environ un demi-point de pourcentage, soit une baisse de 14 % par rapport à 2022. Cette baisse est juste à la limite de la significativité statistique, et il n'y a pas de diminution équivalente pour les travailleurs de plus de 25 ans. Ce résultat fait écho aux conclusions de Brynjolfsson et al. qui rapportent une baisse de 6 à 16 % de l'emploi dans les métiers exposés parmi les 22-25 ans.

## Pourquoi ça compte

C'est l'une des premières études à mesurer l'impact réel (pas théorique) de l'IA sur l'emploi avec des données concrètes. Le signal sur les jeunes travailleurs est discret mais sa trajectoire est claire — un indicateur avancé pour les décideurs RH et tech.
