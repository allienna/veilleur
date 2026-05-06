---
title: "claude code is not making your product better"
date: 2026-05-06
url: https://ethanding.substack.com/p/claude-code-is-not-making-your-product
authors: [Ethan Ding]
keywords: [productivité IA, K-shape, agentic coding, mesure, ingénieurs seniors]
theme: IA
tone: opinion
used_in: ["2026-05-06"]
---

## Résumé

Ethan Ding constate ce que les économistes du travail ont déjà mesuré : les gains de productivité de l'agentic coding ne sont pas distribués uniformément — ils dessinent un K. Les seniors décollent, les juniors stagnent ou régressent. Mais surtout, même quand les ingénieurs produisent plus de code, le rythme d'amélioration du produit ne suit pas. Dax (opencode.ai), Karri Saarinen (CEO Linear), David Cramer (Sentry) — aucun n'est critique de l'IA, tous voient le même pattern. La question n'est plus "est-ce qu'on code plus vite ?" mais "est-ce qu'on mesure la bonne chose ?"

## Points clés

- Les gains de productivité du coding agentic suivent une courbe en K : seniors en hausse, juniors stagnants ou en baisse depuis 2023
- La narrative dominante (« on a vidé six ans de backlog en un trimestre ») cache cette inégalité
- Trois témoignages convergents (Dax, Saarinen, Cramer) : plus de code, pas plus de produit
- Lines of code per hour est probablement la mauvaise métrique
- L'écart entre output ingénieur et amélioration produit s'élargit, alors qu'il devrait se réduire
- Le marketing IA capture le haut du K et invisibilise le bas

## Analyse approfondie

Quelque chose d'intéressant se passe. Les voix les plus bruyantes disent que les agents IA de coding ont tout changé. Les ingénieurs qui construisent réellement les produits qu'on utilise tous les jours racontent quelque chose de plus compliqué.

Avant le discours Twitter, il y a la donnée. Les économistes du travail sont arrivés en premier. Les gains de productivité des coding agents ne sont pas répartis de façon égale. Ils suivent une courbe en K : les seniors deviennent significativement plus productifs ; les juniors, au mieux, font du surplace ; au pire, régressent.

Sur le graphique de l'output ingénieur par séniorité depuis 2015, les courbes seniors (en bleu) montrent une croissance mesurable depuis l'inflection LLM de 2023. Les juniors (en rouge) sont essentiellement plats ou en déclin. Le K est réel. La question est ce qu'il signifie.

La narrative populaire colle au haut du K. Twitter VC produit sa propre version de ce graphique depuis deux ans. Les citations sont prévisibles :

> *"Notre équipe a vidé six ans de backlog en un trimestre. Toutes les PR sont générées par IA. On n'a jamais shippé aussi vite."* — n'importe quel fondateur YC, n'importe quel mois 2025

> *"J'ai utilisé Cursor pour construire tout notre backend en trois jours. Deux ingénieurs faisant le travail de vingt."* — le tweet qui récolte 40k likes à chaque variation

> *"Le code de Claude Code est entièrement claude-codé. L'IA qui écrit l'IA. La récursion est réelle."* — Dario Amodei / Anthropic, à répétition

Pour être juste : il y a quelque chose de réel dans le haut du K. Le coding agentic réduit le temps pour produire une PR pour certaines catégories de travail. Personne de sérieux ne le conteste. La vraie question est de savoir si lines of code per hour est ce qu'il faut mesurer.

### Si les ingénieurs sont plus productifs, le rythme d'amélioration produit par ingénieur devrait monter

Il y a quelques semaines, trois choses se sont produites en quelques jours. Dax (qui construit opencode.ai) a envoyé quelque chose à son équipe. Karri Saarinen (CEO de Linear) a répondu. David Cramer (qui a construit Sentry de zéro à 10M$/mois) a posté ses graphiques GitHub. Aucun n'est critique de l'IA. Tous voient le même pattern.

Le pattern : plus de PRs, plus de commits, plus de ce que les outils mesurent. Mais le produit ne s'améliore pas plus vite. Les bugs ne diminuent pas plus vite. Les nouvelles fonctionnalités qui sortent ne sont pas significativement plus impactantes. La courbe d'output engineer monte, la courbe d'amélioration produit reste plate.

C'est un signal qui mérite d'être pris au sérieux. Il dit qu'on est en train de mesurer la mauvaise chose, ou que ce qui était un bottleneck (la production de code) ne l'était plus, et que le vrai bottleneck est ailleurs : dans la décision, dans le design, dans le contact avec l'utilisateur, dans les arbitrages entre features.

### Ce que ça implique pour les juniors

La courbe du bas du K est plus inquiétante. Les juniors n'ont pas seulement moins de gains — ils peuvent en avoir des négatifs. Pourquoi ?

L'hypothèse de Ding : pour bénéficier de l'agentic coding, il faut savoir le diriger. Savoir quand l'agent a tort. Savoir quoi vérifier. Ce sont des compétences seniors. Sans elles, l'agent amplifie les erreurs au lieu de les corriger. Le junior produit du code qui marche localement mais qui se fissure à l'échelle ; le senior, lui, sait demander à l'agent de revoir, sait casser le problème, sait quand sortir et faire à la main.

À long terme, cela pose un problème de pipeline. Comment former les seniors de demain si les juniors d'aujourd'hui n'apprennent plus en construisant lentement ?

### Les bonnes métriques

Si lines of code per hour ne marche pas, qu'est-ce qui marche ? Ding ne donne pas de réponse définitive, mais propose des pistes :

- Améliorations mesurables du produit (NPS, retention, conversion)
- Réduction du time to value pour les utilisateurs
- Stabilité (réduction des incidents, des rollbacks)
- Capacité de l'organisation à apprendre (documenté plus haut)

Le point central : il faut mesurer ce qui compte pour l'utilisateur, pas ce qui compte pour le rapport au board.

## Pourquoi ça compte

Cet article fournit une donnée empirique précieuse à toute conversation sur le ROI de l'IA en engineering : les gains existent, mais la métrique courante (lines of code, PRs shippées) cache une dispersion réelle (K-shape) et un découplage productivité/produit. Lecture obligatoire pour les CTOs, VPs et engineering managers qui doivent justifier leurs investissements IA en 2026.
