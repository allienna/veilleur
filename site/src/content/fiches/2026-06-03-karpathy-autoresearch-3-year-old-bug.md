---
title: "Karpathy's Autoresearch found a 3-year-old bug in our query engine (and improved performance by 11%)"
date: 2026-06-03
url: https://posthog.com/blog/karpathy-autoresearch-query-engine-bug
authors: [PostHog]
keywords: [autoresearch, Karpathy, ClickHouse, query optimization, AI agent]
theme: IA
tone: tutorial
used_in: ["2026-06-03"]
---

## Résumé

PostHog a appliqué l'idée d'"autoresearch" de Karpathy lors d'un hackathon : pointer un agent IA sur le moteur de requêtes, lui fournir des requêtes lentes de production, un benchmark et un budget, puis le laisser boucler la nuit. L'agent a découvert qu'un wrap `toTimeZone()` ajouté en 2023 empêchait le planificateur ClickHouse d'utiliser correctement la clé primaire et le partition pruning — un bug latent depuis presque trois ans. Le correctif a réduit de 62 % les granules scannés et accéléré la requête de ~37 % en moyenne. L'article détaille le stack, la structure d'investigation (campagnes, lanes, hypothèses, expériences) et le pipeline automatisé en construction.

## Points clés

- L'idée d'autoresearch (Karpathy, mars 2026) : donner à un agent un système réel, un benchmark et un budget, puis boucler — proposer un changement, mesurer, garder ou jeter.
- Effet de second ordre clé : l'agent n'a pas le biais de quelqu'un qui vit dans la base de code ; il traite une expression de 3 ans avec la même suspicion qu'une ligne d'hier.
- Le bug : `toTimeZone(timestamp, tz)` empêchait le planificateur de dériver les bornes pour le partition pruning et la clé primaire.
- Le correctif (mettre le timestamp nu côté champ, le fuseau côté constante) : -62 % de granules, -37 % de temps moyen, sémantique identique.
- Stack : agent `pi` de Mario Zechner, extension `pi-autoresearch` de la communauté, un contrat d'orchestration de campagne maison, un cluster ClickHouse de test jetable.
- Recette généralisable : toute métrique tolérée en silence (vitesse, mémoire, coût, taux d'erreur) peut être ciblée par un harnais bon marché et un agent.

## Analyse approfondie

Il y a quelques semaines, lors d'un offsite d'équipe à Lisbonne, nous avons pointé un agent IA sur notre moteur de requêtes, lui avons fourni des requêtes lentes de production, et l'avons laissé tourner la nuit. Au matin, il avait trouvé quelque chose d'embarrassant : pendant presque trois ans, chaque requête avec un filtre temporel n'utilisait pas correctement la clé primaire de ClickHouse. Le correctif a réduit de 62 % le nombre de granules que ClickHouse devait scanner sur la requête de benchmark, et a rendu la requête elle-même nettement plus rapide.

L'idée générale n'est pas la nôtre. Andrej Karpathy l'a packagée et nommée en mars 2026 : donner à un agent IA un petit système réel, un benchmark et un budget, et le laisser boucler ; proposer un changement, lancer le benchmark, garder ce qui aide, jeter le reste. Karpathy l'a fait tourner deux jours sur un entraînement nanochat de profondeur 12 et a trouvé environ 20 changements améliorant la validation loss, dont certains transféraient à un plus gros modèle. La forme n'est pas nouvelle (FunSearch de DeepMind en 2023, AI Scientist de Sakana en 2024), mais le repo de Karpathy est assez petit et concret pour inspirer sa propre version en une après-midi.

La partie intéressante pour nous est l'effet de second ordre : l'agent ne porte pas le biais qui vient du fait de vivre dans une base de code. Pour nous, le wrap `toTimeZone()` avait juste toujours été là. Le genre de code qu'on cesse de voir. L'agent n'a aucun a priori. Il lance chaque diagnostic, lit le code ClickHouse et PostHog environnant pour le contexte, et traite une expression de trois ans avec la même suspicion que la ligne écrite hier.

Chaque année, nous organisons des hackathons lors des offsites. Une grande partie de ce qu'est aujourd'hui PostHog (session replay, data warehouse, logs, etc.) a démarré ainsi. Lors d'un offsite conjoint des équipes Analytics Platform et Query Performance à Lisbonne, notre projet de hackathon était de faire le truc de Karpathy, mais pour la performance des requêtes ClickHouse.

**Le stack utilisé :**

- **pi** : un petit agent de coding en terminal construit par Mario Zechner. Il parle à n'importe quel LLM qu'on lui pointe, expose un petit SDK, et est assez petit pour qu'on lise tout le code.
- **pi-autoresearch** : une extension communautaire de `davebcn87` qui câble la boucle de Karpathy dans pi. On lui donne un objectif, une baseline, une commande de benchmark et une métrique cible. Il itère, commite chaque candidat, lance le benchmark, et tient un journal pour que le run survive aux resets de contexte.
- **Un contrat d'orchestration de campagne** écrit par-dessus `pi-autoresearch`. La boucle de base "essaie, mesure, garde ou jette" est trop lâche quand une seule requête ClickHouse a des centaines de réécritures plausibles. Structure en quatre parties : une **campagne** (une requête lente, une branche git), découpée en **lanes** (directions d'optimisation liées à un goulot suspecté : ordre des prédicats, parsing JSON, gestion des fuseaux, usage de la clé primaire…), avec une **hypothèse** concrète et testable dans chaque lane, et une **expérience** dans chaque hypothèse (un run, un benchmark, un verdict, avec une passe de réflexion explicite).
- **Un cluster ClickHouse de test jetable** : même forme de données que la production mais anonymisée, sur du matériel moins cher dédié à l'agent.

Le range-narrowing a aussi aidé : quand une requête cible time out, l'agent réduit de moitié la plage (30 jours, 14, 7, 3, 1) jusqu'à ce qu'elle se termine en une à dix secondes, puis optimise sur cette version réduite.

**Le bug.** ClickHouse est rapide parce qu'il peut sauter du travail. Notre table `events` est partitionnée par `toYYYYMM(timestamp)` et la clé primaire est `(team_id, toDate(timestamp), event, …)`. Une requête bien formée avec une borne temporelle devrait faire ignorer à ClickHouse des mois entiers de données. Ce n'était pas le cas. Quand nous avons ajouté le support des fuseaux par équipe à HogQL en avril 2023, nous avons fait la chose sensée et avons wrappé chaque référence à `timestamp` dans `toTimeZone(timestamp, team_tz)` pour des dates d'affichage correctes. Ce que nous n'avions pas réalisé, c'est que le planificateur de requêtes de ClickHouse ne peut pas voir à travers `toTimeZone()`. Il ne pouvait donc pas dériver les bornes sur `toYYYYMM(timestamp)` (partition pruning désactivé) ni sur `toDate(timestamp)` (clé primaire utilisée seulement jusqu'à `team_id` et `event`).

La raison pour laquelle cela ne nous avait pas alertés : ClickHouse a aussi un MinMax skip index sur `timestamp`. Un index MinMax stocke la plus petite et la plus grande valeur par "granule" (8 192 lignes par défaut). C'est bien plus faible que le partition pruning, mais ça marche : les requêtes n'étaient pas catastrophiquement lentes, juste mesurablement plus lentes qu'elles n'auraient dû. C'est le genre de bug qui se cache pour toujours : lent mais pas "réveiller quelqu'un" lent, affectant toutes les requêtes (donc impossible d'A/B comparer), et la preuve vit dans la sortie d'`EXPLAIN PLAN indexes=1, json=1`, que personne ne lance sans déjà suspecter quelque chose.

Dans une des lanes, la boucle d'autoresearch a lancé l'`EXPLAIN`. Elle a remarqué `Partition: Condition='true'` (pas de pruning) et a essayé deux choses : ajouter `indexHint()` avec des bornes timestamp nues, et réécrire la comparaison pour que le côté champ soit nu et la constante porte le fuseau. La seconde approche a gagné, largement, et c'est ce qui a été livré. La sémantique est identique car `toTimeZone()` ne change que les métadonnées d'affichage : l'epoch sous-jacent est inchangé.

**Résultats** sur un funnel de 7 jours contre une vraie équipe en production : meilleur run -22 % (2 824 → 2 192 ms), moyenne tronquée -37 % (4 694 → 2 954 ms), granules du skip-index -62 % (60 683 → 23 291). Le speedup est le plus grand sur les requêtes à plages courtes, là où le partition pruning compte le plus. Le bug était présent depuis le changement de fuseau : environ trois ans.

**La suite.** Le hand-feeding ne scale pas. Le pipeline en construction : récupérer les requêtes lentes depuis `system.query_log`, monter une sandbox par requête candidate, lancer `pi-autoresearch` dans chaque sandbox, faire dédupliquer les suggestions par un LLM et lancer une session PostHog Code pour chaque idée survivante (qui écrit le vrai changement, avec tests et benchmarks), puis poster les PR résultantes dans Slack pour revue humaine. La recette n'est pas spécifique aux requêtes lentes : s'il y a une métrique que vous tolérez en silence (vitesse, mémoire, coût, précision, taux d'erreur), construisez un harnais bon marché que ça ne vous dérange pas de maltraiter, pointez un agent dessus, et regardez ce qui revient.

## Pourquoi ça compte

C'est une démonstration concrète et reproductible de l'orchestration d'agents au service de la performance : un agent sans a priori trouve en une nuit un bug que l'équipe tolérait depuis trois ans. La recette autoresearch est généralisable à toute métrique mesurable.
