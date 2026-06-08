---
title: "Why we shrank our TimescaleDB chunks from 30 days to 7"
date: 2026-06-08
url: https://substack.com/redirect/88771809-a952-43c3-abe6-83a9470fbe76?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Yask Srivastava, WMG Lab]
keywords: [TimescaleDB, chunks, hypertable, compression, time series]
theme: Data
tone: opinion
used_in: ["2026-06-08"]
---

## Résumé

Yask Srivastava (WMG Lab) raconte comment Sodatone, plateforme d'intelligence A&R de Warner Music, a réduit l'intervalle de chunk de ses hypertables TimescaleDB de 30 à 7 jours. Un chunk de 30 jours, parfait quand la table était petite, avait fini par faire échouer le job de compression devenu trop gros pour finir en une passe. L'article détaille les cinq dimensions impactées par la taille de chunk, pourquoi le bon réglage d'hier devient le piège de demain à débit d'ingestion croissant, et pourquoi `set_chunk_time_interval` est l'un des leviers les plus sûrs à actionner.

## Points clés

- Une hypertable TimescaleDB ressemble à une table Postgres unique mais est en réalité une collection de chunks, chacun couvrant une plage de temps — ce qui permet au planner de sauter les chunks hors prédicat.
- La taille de chunk impacte cinq choses qui se cumulent : working set en mémoire, pruning des chunks, taille de batch de compression, coût de backfill, granularité de rétention.
- Recommandation officielle : le chunk actif devrait tenir dans ~25 % de la mémoire disponible — une cible mobile, car le même intervalle de temps représente plus d'octets quand l'ingestion croît.
- `set_chunk_time_interval` n'affecte que les chunks futurs : pas de réécriture, pas de verrou exclusif, pas de backfill — donc un levier sûr et réversible.
- Déclencheur concret : en septembre, le job de compression d'une table lourde (millions de lignes/semaine, plusieurs To) a commencé à échouer car le chunk était devenu trop gros.
- Résultat : compression rattrapant l'ingestion plus vite, écart « live / compressé » réduit (gains de compression ~90 %).

## Analyse approfondie

*Par Yask Srivastava.*

Chaque jour, Sodatone (la plateforme d'intelligence A&R de WMG) collecte des signaux d'engagement depuis les plateformes de streaming et sociales et les transforme en séries temporelles que nos scouts et équipes de label utilisent pour repérer les artistes émergents. La plupart de ces données vivent dans des hypertables TimescaleDB, une par paire plateforme-et-métrique. Donc quand l'une d'elles se met à mal se comporter, c'est souvent un indicateur avancé pour les autres.

Si vous n'avez jamais vécu dans TimescaleDB, voici la version courte. Une hypertable ressemble à une table Postgres unique, mais sous le capot c'est une collection de tables plus petites — des *chunks* — chacune contenant les lignes d'une plage de temps. Par exemple, une hypertable avec un chunk de 30 jours contenant un an de données est en réalité 12 tables cousues ensemble. Cela signifie que pour interroger les données du dernier mois, notre requête ne touche que le chunk le plus récent ; tous les autres sont sautés sans être lus, ce qui améliore drastiquement les temps de requête.

### Pourquoi la taille de chunk compte

La taille de chunk affecte cinq choses qui se cumulent :

- **Working set en mémoire.** Le chunk actif (non compressé) est ce que touchent vos écritures chaudes et vos lectures de données récentes. S'il ne tient pas confortablement dans les shared buffers et le page cache, chaque requête récente commence à payer de l'I/O.
- **Pruning des chunks.** Le planner saute les chunks dont la plage de temps ne recoupe pas votre prédicat WHERE. C'est la raison principale pour laquelle les hypertables sont rapides sur les scans par plage de temps — et des chunks plus petits rendent le pruning plus sélectif sur les requêtes de données récentes.
- **Taille de batch de compression.** La politique de compression de TimescaleDB compresse les chunks une fois passé un certain âge. Les gros chunks sont plus longs à compresser et décompresser que les petits.
- **Coût de backfill.** Ré-ingérer des données dans un chunk compressé signifie le décompresser, appliquer le changement, et le recompresser. Le chunk est l'unité de ce travail.
- **Granularité de rétention.** Si vous appliquez un jour `add_retention_policy`, le chunk est aussi l'unité d'éviction.

La recommandation de TimescaleDB est que le chunk actif tienne dans environ 25 % de la mémoire disponible. C'est une cible mobile. À mesure que les taux d'ingestion croissent, le même intervalle de temps représente plus d'octets, et un chunk de 30 jours qui allait bien il y a un an peut devenir un problème aujourd'hui.

Ce qu'il faut savoir sur `set_chunk_time_interval`, c'est qu'il n'affecte que les chunks futurs. Les chunks existants conservent leur taille d'origine et continuent d'être interrogés sans souci. Pas de réécriture, pas de verrou exclusif, pas de backfill. L'hypertable transitionne naturellement à l'arrivée de la prochaine frontière de chunk. Cela en fait l'un des leviers les plus sûrs à tourner dans TimescaleDB. Si le résultat ne vous plaît pas, vous l'inversez de la même façon.

### Ce que nous avons remarqué

Fin de l'année dernière, nous avons remarqué qu'une de nos hypertables les plus lourdes — des millions de lignes par semaine, plusieurs To sur disque avant compression — vieillissait mal. La compression prenait du retard sur l'ingestion, les lectures de données récentes devenaient progressivement plus lourdes au fil de l'automne, et chaque fois qu'un flux amont republiait quelques jours d'historique (ce qui arrive plus souvent qu'on ne le voudrait), nous finissions par décompresser des mois entiers de données pour absorber le changement. L'intervalle de chunk — fixé à 30 jours quand la table était petite — avait cessé de nous rendre service.

### Ce que nous avons changé

En septembre, le job de compression de cette table a commencé à échouer — le chunk était devenu trop gros pour finir en une seule passe. C'est pourquoi ce fut la première table que nous avons touchée. Nous avons fait passer l'intervalle de chunk de 1 mois à 7 jours, et regardé le job tourner dans le dashboard de monitoring Timescale Cloud jusqu'à ce qu'il s'exécute proprement à nouveau.

Deux mois plus tard, nous avons vu la même panne sur une autre table — un de nos flux de données de classements musicaux. Le même correctif a marché. À ce stade, l'ayant vu deux fois en deux mois, nous avons mis à jour le reste de nos tables d'engagement chaudes dans une seule PR début décembre. Toutes sont passées à des chunks de 7 jours. Chaque migration ressemblait à un simple `set_chunk_time_interval(..., interval: "7 days")` encadré par un `safety_assured`.

### Ce que nous y avons gagné

- **La compression a rattrapé son retard plus vite.** Des chunks plus petits terminent une passe de politique de compression plus rapidement, donc l'écart entre données « live » et compressées a diminué pour chaque table touchée (gains de compression de l'ordre de 90 %).

## Pourquoi ça compte

Rappel concret qu'un paramètre par défaut « raisonnable » est une dette qui mûrit avec la croissance : ce qui tenait dans la mémoire il y a un an la déborde aujourd'hui, et savoir quels leviers sont sûrs à actionner (ici, n'affecter que les chunks futurs) est une compétence d'ingénierie data à part entière.
