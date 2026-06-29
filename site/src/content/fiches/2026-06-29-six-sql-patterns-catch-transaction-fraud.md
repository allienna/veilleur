---
title: "Six SQL patterns I use to catch transaction fraud"
date: 2026-06-29
url: https://substack.com/redirect/61c86253-1c08-4df6-bce5-11f0dbdcc577?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Anonyme - program-integrity team]
keywords: [SQL, détection de fraude, window functions, data engineering, anti-hype]
theme: Data
tone: tutorial
used_in: ["2026-06-29"]
---

## Résumé

Un praticien de l'intégrité des programmes explique que la détection de fraude dans les données transactionnelles est avant tout une affaire de SQL — pas de machine learning, pas de bases de graphes, pas du dernier hype Gartner. Il détaille six patterns qu'il déploierait sur un nouveau dataset, dans l'ordre, des plus simples (vélocité, voyage impossible) aux plus subtils (anomalies de montant, marchands suspects). Chaque pattern tient en une requête SQL ciblée, avec ses seuils à ajuster et ses faux positifs connus.

## Points clés

- La fraude transactionnelle se détecte surtout en SQL : les bonnes tables, les bonnes jointures, les bonnes « formes » à chercher.
- Vélocité : compter les transactions par fenêtre glissante pour repérer une carte volée qu'on vide vite (window function `count() OVER` + `QUALIFY`).
- Voyage impossible : via `LAG()` et la distance haversine, détecter une carte présente dans deux villes éloignées en quelques minutes (seuil ~600 mph).
- Anomalies de montant : les petits montants ronds ($1, $5, $10) trahissent des tests de carte ; les montants juste sous un seuil ($99,99, $499,99) trahissent quelqu'un qui connaît les règles.
- Marchands suspects : un skimmer se voit comme un nombre inhabituel de cartes non liées dépensant plus que d'habitude sur une courte fenêtre.

## Analyse approfondie

**Avertissement de l'auteur :** je fais du data sur une équipe d'intégrité de programme. Les exemples ci-dessous utilisent des tables de transactions génériques et des scénarios inventés. Rien ne provient de ce sur quoi j'ai réellement travaillé. Les opinions sont les miennes, pas celles de mon employeur.

La détection de fraude dans les données transactionnelles, c'est surtout du SQL. Pas du machine learning, pas des bases de graphes, ni le hype Gartner de l'année. Du SQL, exécuté contre les bonnes tables, avec les bonnes jointures, à la recherche des bonnes formes. Je travaille surtout sur des programmes d'aides publiques, mais les patterns ci-dessous se transposent à tout ce qui a une table de transactions : cartes de crédit, demandes de remboursement santé, e-commerce, points de vente. Si de l'argent bouge et est loggué, ces requêtes trouveront des choses bizarres dans le log. Six patterns, à peu près dans l'ordre où je les construirais sur un nouveau dataset.

### 1. Vélocité

Le plus simple. Quelqu'un avec une carte volée veut la vider avant que le porteur ne s'en aperçoive. Donc il frappe la carte vite.

```
SELECT
  cardholder_id,
  date_trunc('hour', timestamp) AS hour_bucket,
  count(*) AS tx_count,
  min(timestamp) AS first_tx,
  max(timestamp) AS last_tx
FROM transactions
WHERE timestamp >= current_date - INTERVAL '30 days'
GROUP BY 1, 2
HAVING count(*) > 10;
```

On règle deux boutons : la taille de la fenêtre et le seuil de comptage. Je fais généralement tourner en parallèle une version 1 minute, 5 minutes et 1 heure, et je compare — différentes fraudes se manifestent à différentes échelles. Quelques porteurs dépasseront le seuil légitimement (opérateurs de distributeurs, recharges de cartes prépayées en gros) : ce sont vos faux positifs, à mettre en whitelist après le premier passage. Pour la vélocité en fenêtre glissante, j'utilise cette forme :

```
SELECT
  cardholder_id,
  timestamp,
  count(*) OVER (
    PARTITION BY cardholder_id
    ORDER BY timestamp
    RANGE BETWEEN INTERVAL '5 minutes' PRECEDING AND CURRENT ROW
  ) AS tx_in_last_5min
FROM transactions
QUALIFY tx_in_last_5min >= 5
ORDER BY cardholder_id, timestamp;
```

`QUALIFY` fonctionne sous Snowflake, BigQuery, Databricks, Teradata. Sous Postgres, on enveloppe le tout dans une CTE et on filtre à l'extérieur. Léger inconvénient, même résultat.

### 2. Voyage impossible

Si une carte est utilisée à Chicago et, sept minutes plus tard, à Los Angeles, l'un des deux passages est faux : la carte est clonée. C'est le signal de fraude le plus incontestable qui soit — il n'y a quasiment aucune raison légitime qu'une seule carte soit dans deux endroits distants en sept minutes.

```
WITH ordered_tx AS (
  SELECT
    cardholder_id, timestamp, location,
    LAG(timestamp) OVER (PARTITION BY cardholder_id ORDER BY timestamp) AS prev_ts,
    LAG(location)  OVER (PARTITION BY cardholder_id ORDER BY timestamp) AS prev_loc
  FROM transactions
)
SELECT
  cardholder_id, prev_ts AS first_tx, timestamp AS second_tx,
  prev_loc AS first_location, location AS second_location,
  EXTRACT(EPOCH FROM (timestamp - prev_ts)) / 60 AS minutes_apart,
  haversine(prev_loc, location) AS miles_apart
FROM ordered_tx
WHERE prev_ts IS NOT NULL AND prev_loc <> location
  AND haversine(prev_loc, location)
      / nullif(EXTRACT(EPOCH FROM (timestamp - prev_ts)), 0) * 3600 > 600;
```

`haversine` est la fonction de distance orthodromique ; la plupart des entrepôts en fournissent une. Le seuil de 600 mph est grossier — la vitesse de croisière d'un jet commercial est d'environ 575, donc c'est « plus vite qu'un avion ne pourrait le faire ». On peut le resserrer à 100 mph pour attraper aussi des déplacements terrestres suspicieusement rapides, mais on commence alors à ramasser de vrais voyageurs aériens. D'autres formes de la même famille valent le coup : deux villes distantes du même État en moins de 5 minutes (réseaux de clonage locaux), plusieurs codes postaux en une heure (réseaux de skimmers régionaux), franchissements de frontière en moins de 10 minutes (réseaux internationaux).

### 3. Anomalies de montant

Quelques montants apparaissent de façon disproportionnée dans la fraude et presque jamais dans l'usage normal.

```
SELECT cardholder_id, timestamp, amount, merchant_id
FROM transactions
WHERE (amount >= 99.50 AND amount < 100.00)
   OR (amount >= 499.50 AND amount < 500.00)
   OR amount IN (1.00, 5.00, 10.00)
ORDER BY cardholder_id, timestamp;
```

Les petits montants ronds — 1,00 $, 5,00 $, 10,00 $ — sont presque toujours des tests de carte : quelqu'un a récupéré un numéro dans un dump et vérifie qu'il marche avant de le revendre. Un vrai porteur n'achète quasiment jamais quelque chose à exactement 1,00 $ ; le café est à 4,73 $, l'essence à 52,81 $. La rondeur est le signal. Les montants juste sous un seuil sont différents : 99,99 $ est intéressant car 100 $ est souvent la ligne où le caissier doit vérifier l'identité ; 499,99 $ car 500 $ est souvent le plafond quotidien d'un distributeur. Celui qui fait la transaction connaît les règles et reste en dessous.

### 4. Marchands suspects

Quand un skimmer compromet un lecteur de carte (à une pompe à essence, par exemple), on n'a pas un cas de fraude mais des dizaines : chaque carte passée à cette pompe les semaines suivantes finit dans une base. Le symptôme côté marchand : un nombre inhabituel de cartes non liées dépensant plus que d'habitude, sur une courte fenêtre.

```
SELECT
  merchant_id,
  date_trunc('hour', timestamp) AS hour_bucket,
  count(DISTINCT cardholder_id) AS unique_cards,
  count(*) AS total_tx,
  sum(amount) AS total_amount
FROM transactions
WHERE timestamp >= current_date - INTERVAL '30 days'
GROUP BY 1, 2;
```

## Pourquoi ça compte

Un contrepoint salutaire au réflexe « colle un LLM/du ML sur le problème » : pour beaucoup de cas réels, du SQL bien pensé sur les bonnes tables bat le modèle sophistiqué. La discipline, c'est de savoir quand *ne pas* sortir l'artillerie ML.
