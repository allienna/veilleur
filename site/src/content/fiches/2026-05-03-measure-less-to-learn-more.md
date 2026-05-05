---
title: "Measure Less to Learn More: Using Fewer, Higher-quality Metrics to Capture What Matters"
date: 2026-05-03
url: https://leadershipintech.com/links/22198/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Discord Engineering, Jake Mainwaring]
keywords: [experimentation, AB testing, metrics, statistics, data science]
theme: Data
tone: research
used_in: ["2026-05-03"]
---

## Résumé

L'équipe Data Science de Discord raconte comment elle a réduit le nombre de métriques par défaut de ses expérimentations d'environ 50 à 15. En multipliant les métriques observées, on multiplie aussi les faux positifs et le bruit statistique : il devient plus dur de détecter un effet réel modéré sans déclencher de fausses alertes. En s'appuyant sur une analyse de corrélation et une PCA pour identifier les redondances, Discord a amélioré sa capacité à détecter des effets réels d'environ 45 %. La leçon : la valeur d'un système d'expérimentation ne vient pas du nombre de métriques mesurées mais de la qualité du signal qu'elles produisent.

## Points clés

- Trop de métriques crée un problème statistique : plus on mesure, plus on génère de faux positifs.
- Discord est passé d'environ 50 métriques par défaut à 15, sélectionnées pour leur signal propre.
- L'analyse de corrélation et la PCA ont permis d'identifier les métriques redondantes.
- Le gain : ~45 % de capacité supplémentaire à détecter des effets réels modérés.
- Couverture et signal sont deux choses différentes ; empiler par sécurité dégrade la prise de décision.

## Analyse approfondie

Suivre trop de métriques dans une expérimentation crée un vrai problème statistique : plus on mesure, plus il devient difficile de détecter un effet réel sans aussi générer de fausses alertes. Discord a réduit ses métriques d'expérimentation par défaut d'environ 50 à 15 en identifiant les mesures redondantes via une analyse de corrélation et une analyse en composantes principales (PCA). Cette réduction a amélioré leur capacité à détecter des effets réels modérés d'environ 45 %.

Le mécanisme est connu en statistiques sous le nom de problème des comparaisons multiples : à chaque fois qu'on ajoute un test, on augmente la probabilité qu'au moins un d'entre eux fasse apparaître un faux positif. Pour compenser, on durcit les seuils de significativité, ce qui a pour effet pervers de masquer aussi les vrais effets modérés — exactement ceux qui font le quotidien d'un produit en itération.

L'approche de Discord consiste à reconnaître que beaucoup de métriques mesurent peu ou prou la même chose. La PCA identifie les axes principaux de variance ; la corrélation montre quelles métriques se déplacent ensemble. Un panel resserré, conçu pour couvrir l'espace décisionnel sans redondance, donne au final une lecture plus claire des effets — et permet d'utiliser des seuils statistiques moins punitifs.

## Pourquoi ça compte

Cette logique dépasse largement l'A/B testing. Toute organisation tech accumule des dashboards, KPI et métriques produits par réflexe de couverture, et finit par confondre activité de mesure et qualité de pilotage. Le contre-exemple Discord rappelle que mesurer moins peut littéralement faire voir plus.
