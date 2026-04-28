---
title: "Databases Were Not Designed For This"
date: 2026-04-28
url: "https://link.mail.beehiiv.com/ss/c/u001.K3FzaWG5vnes9asChrWWUKSsj6-JWblzpUjCH-67DDBotp1lxvvn63nCa--q6zLHY5SGpfiuDkZjlfbrBJf-nguzwfXvYNr_PvMuuFbZq3UL5LDaKuTTBA32869COBAfGf64xJUDvx7gg1vcWrw78N7mBqQCqWn2jqncFFqBcdaTvX9lgUwxDThyjbZiQr4B/4q6/SUa9yOjzT-K0oF3iTvxpNg/h13/h001.ddqr3XYzd0OdRwjaEoYP9ne4GSxZ00s7gXszW6PN3HU"
authors: ["Hussein Nasser"]
keywords: [databases, agentic AI, postgres, statement timeout, connection pool]
theme: "Tech"
tone: "tutorial"
used_in: ["2026-04-28"]
---

## Résumé

Le contrat implicite qui régissait depuis 40 ans la conception des bases de données — "le caller est une application déterministe écrite et reviewée par un humain" — vole en éclats avec l'arrivée des agents. Hussein Nasser détaille comment chaque hypothèse historique (caller déterministe, requêtes prévisibles, écritures intentionnelles, connexions brèves) est violée par les systèmes agentiques, et propose des patterns concrets pour s'adapter : statement timeouts agressifs au niveau du rôle, idle transaction limits, et un repenser global des permissions et du pool de connexions.

## Points clés

- Le contrat implicite des DB depuis 40 ans suppose un caller humain et déterministe — les agents le violent à toutes les couches
- Les agents *raisonnent* leurs requêtes ; chaque chemin de raisonnement produit une requête différente sur les mêmes tables
- Les indexes optimisés pour le happy path et les pools de connexions calibrés sur le pic observé ne tiennent plus
- Première ligne de défense : poser des `statement_timeout` au niveau du rôle, pas de l'application (ex : 5s)
- Deuxième ligne : `idle_in_transaction_session_timeout` pour éviter qu'un agent n'oublie une transaction ouverte pendant qu'il "réfléchit"
- Les agents génèrent des charges imprévisibles — il faut accepter que la DB devienne un endroit défensif

## Analyse approfondie

### Le contrat implicite

Il y a un contrat implicite à la base de chaque décision d'architecture de base de données qu'on a jamais prise. Probablement personne ne l'a jamais écrit. Il existait juste.

Le contrat dit à peu près ceci : le caller est une application écrite par un humain, qui exécute du code déterministe, qui émet des requêtes prévisibles, reviewé par un développeur avant déploiement. Les écritures sont intentionnelles. Les connexions sont brèves. Quand quelque chose va de travers, un humain le remarque. La base peut être bête et rapide parce que la couche application est intelligente et prudente.

Pendant 40 ans, ce contrat a tenu. Il a façonné comment on a designé les schémas, dimensionné les pools de connexions, accordé les permissions, et pensé les modes d'échec. Ça marchait parce que l'hypothèse était correcte.

Elle ne l'est plus. Les systèmes d'IA agentiques violent ce contrat à chaque couche simultanément.

### Hypothèse n°1 — Le caller déterministe

Dans toutes les applications déployées avant les agents, les requêtes qui frappaient la base étaient écrites par un humain :

- le développeur a écrit le SQL
- le développeur l'a code-reviewé
- le développeur l'a testé et déployé

Cette hypothèse est si profonde que le tooling la reflète automatiquement : le query planner Postgres construit ses statistiques autour des patterns de requêtes observés, les couches de cache se chauffent sur les requêtes répétées, et les pools de connexions sont tunés pour le nombre attendu de requêtes concurrentes d'une complexité connue.

Les agents fonctionnent différemment ; ils *raisonnent* leur chemin vers les requêtes. Différents chemins de raisonnement produisent des requêtes différentes sur les mêmes tables.

Un agent travaillant sur une tâche d'analyse client peut émettre un join sur cinq tables qui n'a jamais été émis auparavant, garder la connexion pendant qu'il réfléchit au résultat, puis émettre une requête de suivi complètement différente. Vos indexes couvrent le happy path. Votre pool de connexions est dimensionné pour votre pic observé. Aucun des deux ne tient quand l'agent peut construire n'importe quelle requête en fonction des données qu'il a besoin.

### Statement timeouts

Les statement timeouts sont votre première ligne de défense. Une requête écrite par un humain qui prend 30 secondes est un bug que quelqu'un va remarquer. Une requête agent qui prend 30 secondes peut être une boucle de raisonnement que personne ne surveille.

Donc, posez les timeouts au niveau du rôle, pas seulement au niveau de l'application :

```sql
CREATE ROLE agent_worker;
ALTER ROLE agent_worker SET statement_timeout = '5s';
ALTER ROLE agent_worker SET idle_in_transaction_session_timeout = '10s';
```

Le `idle_in_transaction_session_timeout` est crucial — il empêche un agent qui ouvre une transaction puis se "perd" dans son raisonnement de garder cette transaction ouverte indéfiniment, bloquant des locks sur des lignes sans personne pour les libérer.

### Les autres hypothèses qui craquent

L'article continue en démontant méthodiquement chaque autre hypothèse historique : les écritures intentionnelles (un agent peut décider d'écrire pour "tester"), les connexions brèves (un agent peut tenir une connexion pendant des minutes), la prévisibilité du volume (un agent peut tomber dans une boucle et émettre des milliers de requêtes en quelques secondes).

À chaque fois, la même logique : il faut déplacer la défense du code applicatif (qui n'existe plus en tant que tel) vers la base elle-même, via des permissions par rôle, des quotas, des limites de concurrence par utilisateur, et de la réservation de capacité.

## Pourquoi ça compte

C'est la première fois qu'on voit articulé aussi clairement *pourquoi* les agents cassent les infrastructures qu'on a construites pendant 40 ans. Pour les architectes data et les SRE, c'est une checklist de rétro-ingénierie de leurs DBs avant que le premier agent en production ne saturent leurs connexions ou ne provoquent un deadlock à 3h du matin.
