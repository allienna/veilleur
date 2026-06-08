---
title: "Our billing pipeline was suddenly slow. The culprit was a hidden bottleneck in ClickHouse"
date: 2026-06-08
url: https://substack.com/redirect/cdaeb231-e7ca-49d7-bd4c-15e10bbc091c?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Cloudflare]
keywords: [ClickHouse, partitionnement, OLAP, performance, retention]
theme: Data
tone: news
used_in: ["2026-06-08"]
---

## Résumé

Chez Cloudflare, les jobs d'agrégation quotidiens dans ClickHouse — qui alimentent la facturation de centaines de millions de dollars de revenus — ont ralenti progressivement après une migration, sans qu'aucune métrique habituelle (I/O, mémoire, lignes scannées, parts lues) ne bouge. L'enquête révèle un goulot d'étranglement caché dans les internals de ClickHouse : la durée des requêtes corrélait avec le nombre *total* de parts du cluster, et non avec les parts effectivement lues. Le changement de clé de partitionnement de `(day)` à `(namespace, day)`, censé être neutre en performance, avait fait exploser le nombre total de parts. L'équipe a écrit trois patches pour corriger le problème.

## Points clés

- Le pipeline fait des millions d'appels ClickHouse par jour ; un retard a des implications majeures en aval (revenus, systèmes anti-fraude).
- Cloudflare stocke plus de 100 Po sur quelques douzaines de clusters, via un système « Ready-Analytics » : une seule table massive, datasets disambiguïsés par `namespace`, clé primaire `(namespace, indexID, timestamp)`.
- Ancienne rétention « taille unique » : 31 jours pour tout le monde, via suppression de partitions — trop rigide pour les besoins variés des équipes.
- Solution retenue : nouvelle clé de partitionnement `(namespace, day)` pour une rétention par namespace, plus une couche de gestion du stockage avec algorithme de max-min fairness (utilisation cible à 90 %).
- Hypothèse fausse : « comme chaque requête filtre sur un namespace, le nombre de parts lues par requête ne change pas, donc les perfs sont inchangées. »
- Réalité : la durée des requêtes corrélait linéairement avec le nombre total de parts du cluster, même pour des parts jamais lues.

## Analyse approfondie

Chez Cloudflare, nous sommes de gros utilisateurs de ClickHouse, une base de données analytique (OLAP) open source. Chaque jour, nous faisons des millions d'appels à ClickHouse pour déterminer combien facturer aux utilisateurs pour leur usage des produits Cloudflare. Si ces jobs ne se terminent pas à temps, les factures deviennent très difficiles à réconcilier.

Ce pipeline alimente des centaines de millions de dollars de revenus d'usage, des systèmes anti-fraude, et plus encore ; un retard a donc des implications majeures en aval.

C'est pourquoi ce fut un gros problème quand les jobs d'agrégation quotidiens dans ClickHouse — responsables de l'envoi des factures de Cloudflare — ont fortement ralenti, à la suite d'une migration. Tous les suspects habituels semblaient irréprochables : I/O, mémoire, lignes scannées, parts lues. Tout ce que l'on vérifie d'ordinaire quand une requête ClickHouse est lente paraissait normal.

Voici l'histoire de la découverte d'un goulot d'étranglement caché, enfoui profondément dans les internals de ClickHouse, et des trois patches que nous avons écrits pour le corriger.

### Le décor : une plateforme analytique à l'échelle du pétaoctet

Nous utilisons ClickHouse pour stocker plus d'une centaine de pétaoctets de données sur quelques douzaines de clusters. Pour simplifier l'embarquement de nos nombreuses équipes internes, nous avons construit un système appelé « Ready-Analytics » début 2022.

Le principe est simple : au lieu de concevoir de nouvelles tables, les équipes streament leurs données dans une seule table massive. Les datasets sont disambiguïsés par un `namespace`, et chaque enregistrement suit un schéma standard (par ex. 20 champs flottants, 20 champs chaîne, un timestamp et un `indexID`).

Dans ClickHouse, la façon dont les données sont triées est cruciale pour la performance des requêtes. C'est là qu'intervient l'`indexID`. C'est un champ chaîne, partie de la clé primaire, ce qui signifie que chaque namespace peut trier ses données de la manière optimale pour les requêtes attendues. Au total, la clé primaire ressemble à : (`namespace`, `indexID`, `timestamp`).

Ce système est populaire, avec des centaines d'applications l'utilisant. Il avait déjà dépassé 2 Pio de données en décembre 2024, avec un taux d'ingestion de millions de lignes par seconde. Mais il avait un défaut critique : sa politique de rétention.

### Le problème : une rétention unique pour tout le monde

Cloudflare utilise ClickHouse depuis de nombreuses années, avant même qu'il ne dispose de fonctionnalités natives de Time-to-Live (TTL). En conséquence, nous avions bâti notre propre système de rétention basé sur le partitionnement. La table Ready-Analytics était partitionnée par `day`, et notre job de rétention supprimait simplement les partitions de plus de 31 jours.

Cette rétention « taille unique » de 31 jours était une limitation majeure. Certaines équipes devaient conserver des données pendant des années pour des raisons légales ou contractuelles, tandis que d'autres n'en avaient besoin que quelques jours. Cette restriction empêchait ces cas d'usage d'utiliser Ready-Analytics et les forçait vers une configuration conventionnelle, à l'embarquement bien plus complexe. Il nous fallait une **rétention par namespace**.

### La solution : un nouveau schéma de partitionnement

Nous avons envisagé deux approches principales : (1) une table par namespace — qui résoudrait naturellement le problème de rétention mais exigerait une automatisation conséquente pour gérer des milliers de tables à la demande ; (2) une nouvelle clé de partitionnement — passer de `(day)` à `(namespace, day)`.

Nous avons choisi la seconde option. Cela permettait à notre système de rétention existant de continuer à gérer les partitions, mais désormais avec une granularité par namespace.

Nous savions que cela augmenterait le nombre total de parts de données dans la table, mais nous avons fait une hypothèse clé : **puisque chaque requête est filtrée sur un namespace spécifique, le nombre de parts lues par une requête donnée ne devrait pas changer.** Nous pensions donc que la performance serait inchangée.

Ce nouveau système permettait aussi de construire une couche de gestion du stockage sophistiquée. Avec l'algorithme de max-min fairness, nous pouvions fixer une utilisation disque cible (par ex. 90 %) et « partager » automatiquement l'espace disponible. Les namespaces utilisant moins que leur juste part cédaient leur capacité inutilisée à ceux qui en avaient besoin. Cela nous permettait de faire tourner nos clusters à 90 % d'utilisation en confiance.

Nous avons commencé la migration en janvier 2025. Grâce à la fonctionnalité de table `Merge` de ClickHouse, nous avons combiné l'ancienne et la nouvelle table, écrivant toutes les nouvelles données dans la nouvelle table partitionnée pendant que les anciennes vieillissaient.

### Le mystère : quand la facturation se met à casser

Deux mois plus tard, fin mars 2025, l'équipe facturation a signalé que ses jobs d'agrégation quotidiens ralentissaient. Ces jobs sont critiques en temps ; s'ils ne finissent pas, les factures ne partent pas. Les jobs devenaient progressivement plus lents, et nous approchions d'une échéance.

Nous avons enquêté, mais aucun des suspects habituels n'était en cause. L'I/O allait bien. La mémoire allait bien. Les métriques des requêtes individuelles montraient qu'elles ne lisaient *pas* plus de données ni plus de parts qu'avant. Notre hypothèse initiale semblait correcte, et pourtant le système s'enrayait.

Il a fallu plusieurs jours avant même d'avoir une théorie. Finalement, nous avons tracé la durée des requêtes contre le **nombre total de parts** dans le cluster. La corrélation était indéniable. Le nombre total de parts par réplique de table croissait linéairement, suivant le nouveau schéma de partitionnement `(namespace, day)`.

Mais *pourquoi* ? Si nous ne *lisions* pas les parts supplémentaires, pourquoi leur simple existence finissait-elle par tout ralentir ?

## Pourquoi ça compte

Cas d'école sur les hypothèses de performance à l'échelle : une décision de partitionnement jugée neutre (« on ne lit pas plus de parts ») cachait un coût global, invisible des métriques par requête. À grande échelle, ce que vous ne mesurez pas peut être exactement ce qui vous coûte cher.
