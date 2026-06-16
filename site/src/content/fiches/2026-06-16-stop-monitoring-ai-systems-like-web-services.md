---
title: "Stop Monitoring AI Systems Like Web Services"
date: 2026-06-16
url: https://www.newsletter.swirlai.com/p/stop-monitoring-ai-systems-like-web?utm_source=tldrit
authors: [Aurimas Griciunas, SwirlAI]
keywords: [observability, LLM monitoring, latency, token cost, silent failures]
theme: IA
tone: tutorial
used_in: ["2026-06-16"]
---

## Résumé

Aurimas Griciunas (SwirlAI) explique pourquoi la plupart des systèmes d'IA sont encore monitorés comme les services web qu'ils côtoient — uptime, taux d'erreur, percentiles de latence — alors que ces métriques ne capturent pas ce qui casse vraiment dans un système LLM. Un LLM brise les hypothèses du monitoring web : la réponse est générée token par token (la « latence » est au moins trois chiffres différents), le coût croît avec les tokens et non les requêtes, et les pannes les plus dommageables sont silencieuses (un texte confiant renvoyé avec un statut 200). L'auteur propose de regrouper les métriques par la question à laquelle elles répondent : est-ce rapide, ça passe à l'échelle, est-ce correct, est-ce que ça tient, et — quand un agent est dans la boucle — comment se comporte-t-il.

## Points clés

- Beaucoup de systèmes IA sont monitorés comme des services web ; les dashboards d'infra ne disent pas que l'utilisateur fixe un écran blanc 4 secondes avant le premier token.
- Un LLM brise les hypothèses du monitoring web : réponse token par token, coût lié aux tokens, pannes silencieuses.
- La « latence » est au moins trois chiffres selon l'endroit de la timeline (notamment phases de prefill et de génération).
- Les régressions de qualité ne renvoient pas un 500 : elles renvoient un texte confiant avec un statut 200.
- Cinq questions couvrent l'essentiel : rapidité, scalabilité, correction, robustesse, comportement de l'agent.
- Beaucoup de ces métriques doivent être construites soi-même car rien ne les émet par défaut.

## Analyse approfondie

Beaucoup de systèmes d'IA sont encore monitorés comme les services web à côté desquels ils tournent. La passerelle d'API émet uptime, taux d'erreur et percentiles de latence, et les dashboards viennent gratuitement avec l'infrastructure. Malheureusement, aucun de ces chiffres ne peut vous dire que des utilisateurs fixent un écran blanc pendant quatre secondes avant que le premier token s'affiche, ni que la dépense en tokens par tâche a doublé depuis la dernière mise à jour du prompt, ni que le modèle a commencé à inventer des réponses autour du contexte récupéré au lieu de s'appuyer dessus.

L'écart existe parce qu'un système LLM brise les hypothèses sur lesquelles le monitoring web a été bâti. Les réponses sont générées token par token, donc la « latence » est au moins trois chiffres différents selon l'endroit de la timeline où l'on se place. Le coût croît avec les tokens plutôt qu'avec les requêtes. De plus, les pannes les plus dommageables sont silencieuses : une régression de qualité ne lève pas un 500, elle renvoie un texte confiant avec un statut 200.

Pour l'auteur, il est utile de regrouper les métriques par la question à laquelle elles répondent. Cinq questions couvrent l'essentiel de ce qui dérape en production : est-ce rapide, est-ce que ça passe à l'échelle, est-ce correct, est-ce que ça tient dans le temps, et — quand il y a un agent dans la boucle — comment se comporte-t-il ? L'article parcourt chaque groupe, ce que les métriques signifient mécaniquement, et lesquelles il faut construire soi-même car rien ne les émet par défaut.

Une requête LLM comporte deux phases qui produisent des chiffres de latence différents. Pendant le *prefill*, le modèle ingère l'intégralité du prompt et construit son état interne ; puis vient la phase de génération, token par token. Cette distinction explique pourquoi un seul nombre de « latence » est trompeur et pourquoi le temps jusqu'au premier token est une métrique d'expérience à part entière.

## Pourquoi ça compte

C'est le pendant opérationnel de la thèse du jour : si la trace dit la vérité que la source cache, encore faut-il instrumenter une observabilité conçue pour les LLM — sinon on pilote des systèmes critiques avec des cadrans aveugles.
