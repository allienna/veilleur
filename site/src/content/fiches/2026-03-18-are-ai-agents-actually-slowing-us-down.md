---
title: "Are AI agents actually slowing us down?"
date: 2026-03-18
url: https://newsletter.pragmaticengineer.com/p/are-ai-agents-actually-slowing-us
authors: [Gergely Orosz]
keywords: [AI agents, productivité, qualité code, incidents, metrics]
theme: IA
tone: opinion
used_in: ["2026-03-18"]
---

## Résumé

Gergely Orosz compile plusieurs signaux inquiétants sur l'impact réel des agents IA en entreprise. Le site web dégradé d'Anthropic est passé inaperçu, Amazon impose désormais une validation senior pour les changements générés par agents après une série de SEV, et Meta comme Uber traquent la consommation de tokens IA dans les évaluations de performance — mais sans mesurer la qualité du code produit. Le constat : la qualité est en baisse.

## Points clés

- Le site web dégradé d'Anthropic est resté en ligne sans que personne ne le remarque — un symptôme de la confiance excessive dans les outputs IA
- Amazon a instauré une validation obligatoire par un ingénieur senior pour tout changement produit par un agent IA, après une série d'incidents de production (SEV)
- Meta et Uber intègrent la consommation de tokens IA dans leurs évaluations de performance des développeurs
- Ces entreprises mesurent l'usage des agents mais pas la qualité du code qui en résulte — un angle mort dangereux
- La vitesse de production augmente, mais la qualité globale diminue en parallèle

## Analyse approfondie

Le site web d'Anthropic — l'entreprise derrière Claude — a connu une dégradation visible de qualité qui est restée en ligne pendant une période prolongée, sans que personne en interne ne semble le remarquer ou agir. Ce fait, en apparence anodin, est symptomatique d'un problème plus large : quand les agents IA produisent du contenu ou du code à grande vitesse, qui vérifie la qualité de ce qui sort ?

### Les incidents Amazon

Amazon a connu une série de SEV (incidents de production de sévérité élevée) directement attribuables à des changements de code générés par des agents IA. La réponse de l'entreprise a été d'imposer une nouvelle règle : tout changement produit par un agent doit désormais être approuvé par un ingénieur senior avant d'être déployé.

Cette mesure représente un recul significatif par rapport à la promesse d'accélération des agents. Si chaque output nécessite une revue senior, le gain de vitesse est en grande partie annulé par le goulot d'étranglement de la validation. C'est un aveu implicite que les agents, dans leur état actuel, ne sont pas suffisamment fiables pour opérer de manière autonome en production.

### Meta et Uber : mesurer l'usage, pas la qualité

Meta et Uber ont commencé à intégrer des métriques de consommation de tokens IA dans leurs processus d'évaluation de performance (perf reviews) des développeurs. L'idée sous-jacente : les développeurs qui utilisent activement les agents IA sont considérés comme plus productifs.

Le problème fondamental est l'absence de métriques de qualité associées. On mesure combien de tokens un développeur consomme, mais pas si le code produit avec ces tokens est correct, maintenable ou sécurisé. C'est l'équivalent de mesurer la productivité d'un écrivain au nombre de mots produits sans lire ce qu'il écrit.

Cette approche crée des incitations perverses : les développeurs sont encouragés à utiliser les agents au maximum, indépendamment de la pertinence ou de la qualité du résultat. Ceux qui prennent le temps de coder manuellement quand c'est plus approprié risquent d'être pénalisés dans leurs évaluations.

### Un schéma récurrent

Le fil conducteur de ces trois exemples est le même : les organisations adoptent les agents IA avec empressement, mesurent la vitesse et le volume, mais négligent la qualité. C'est un schéma classique en ingénierie — optimiser une métrique proxy (la vitesse) au détriment de la métrique réelle (la valeur livrée et la fiabilité).

Gergely Orosz conclut que la qualité du code produit avec des agents IA est en baisse dans l'industrie. Non pas parce que les agents sont fondamentalement mauvais, mais parce que les processus, les incitations et les garde-fous autour d'eux n'ont pas suivi le rythme de leur adoption.

## Pourquoi ça compte

Cet article est un signal d'alarme concret, appuyé par des exemples de grandes entreprises tech, montrant que l'adoption des agents IA sans cadre de qualité adéquat produit exactement l'inverse de ce qu'on espère : plus de dette technique, plus d'incidents, et des métriques de productivité trompeuses.
