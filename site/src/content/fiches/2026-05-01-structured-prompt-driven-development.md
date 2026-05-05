---
title: "Structured-Prompt-Driven Development (SPDD)"
date: 2026-05-01
url: https://martinfowler.com/articles/structured-prompt-driven.html
authors: [Thoughtworks Global IT Services]
keywords: [SPDD, prompt engineering, REASONS canvas, governance, AI workflow]
theme: IA
tone: research
used_in: ["2026-05-01"]
---

## Résumé

Thoughtworks formalise une méthode de delivery autour de l'IA : Structured Prompt-Driven Development (SPDD). L'idée centrale : traiter les prompts comme des artefacts de livraison de premier ordre — versionnés, revus, réutilisés, améliorés au fil du temps. Plutôt que des chats jetables, les équipes utilisent des prompts structurés pour capturer les exigences, le langage métier, l'intention de design, les contraintes et la décomposition des tâches. Le LLM génère alors du code dans une frontière définie, ce qui rend l'output plus prévisible et plus facile à valider. SPDD vise à transformer l'assistance IA d'un gain individuel en capacité organisationnelle qui scale.

## Points clés

- Les prompts deviennent des artefacts de livraison versionnés, pas des chats éphémères
- Le REASONS Canvas structure le prompt en sept parties : Require, Express, Approach, Structure, Operate, Norms, Safeguards
- L'intention bascule de "comment générer plus de code" vers "comment rendre les changements IA gouvernables, revisables, réutilisables"
- Les gains individuels en vitesse ne se traduisent pas automatiquement en throughput système
- L'analogie : avoir une Ferrari ne sert à rien sur des routes boueuses

## Analyse approfondie

Une fois qu'une équipe adopte les assistants de code IA, les premiers gains apparaissent au niveau individuel : un développeur peut rédiger, modifier et refactorer du code beaucoup plus vite qu'avant. Mais la vitesse de delivery est rarement limitée par la frappe. Quand on regarde l'ensemble du cycle de livraison — des exigences à la mise en production — de nouvelles frictions apparaissent :

- Les exigences ambiguës deviennent du code rapidement, et les malentendus scalent avec elles.
- Les revues doivent traiter plus de changement, et l'incohérence devient plus facile à introduire.
- Plus de problèmes d'intégration et de test font surface parce que "généré" ne veut pas dire "aligné".
- Le risque en production est plus difficile à raisonner quand le volume de changement augmente.

Donc oui, la vitesse locale s'améliore. Mais ça ne se traduit pas automatiquement en throughput système. C'est comme acheter une Ferrari et la conduire sur des routes boueuses : le moteur est puissant, mais le temps d'arrivée est déterminé par les conditions de route et le trafic. D'après notre expérience, la vraie question n'est pas "comment générer plus de code". C'est : comment rendre les changements générés par IA gouvernables, revisables et réutilisables, pour que les équipes deviennent plus rapides et plus sûres ?

C'est ce qui a conduit nos équipes IT internes (Global IT Services) à une méthode et un workflow que nous appelons désormais Structured Prompt-Driven Development (SPDD). SPDD vise à transformer l'assistance IA d'efficacité personnelle en capacité organisationnelle qui scale, sans sacrifier la qualité.

### Qu'est-ce que SPDD ?

Le Structured Prompt-Driven Development est une méthode d'ingénierie qui traite les prompts comme des artefacts de livraison de premier ordre. Plutôt que de se reposer sur des chats ad hoc, SPDD transforme les prompts en assets qui peuvent être : versionnés, revus, réutilisés et améliorés dans le temps. Les équipes utilisent des prompts structurés pour capturer les exigences, le langage métier, l'intention de design, les contraintes et la décomposition des tâches. Le LLM génère ensuite du code dans une frontière définie, l'output devient donc plus prévisible et plus facile à valider.

### Le REASONS Canvas

Le REASONS Canvas est une structure pour générer des prompts. Il force la clarté autour des exigences, du modèle métier, de l'approche solution, de la structure système, de la décomposition des tâches, des normes réutilisables et des garde-fous. Le LLM est ainsi guidé par l'intention, pas par la devinette.

Le REASONS Canvas est une structure en sept parties qui guide un prompt depuis l'intention → le design → l'exécution → la gouvernance.

**Parties abstraites (intention & design)**
- **R — Require** : exigences fonctionnelles et non-fonctionnelles
- **E — Express** : langage métier, vocabulaire, ubiquitous language
- **A — Approach** : approche de design haut-niveau
- **S — Structure** : structure technique, modules, frontières

**Parties concrètes (exécution & gouvernance)**
- **O — Operate** : décomposition des tâches, ordre d'exécution
- **N — Norms** : conventions, règles d'équipe, standards
- **S — Safeguards** : garde-fous, validation, critères d'acceptation

### Au-delà du canvas

SPDD inclut aussi un workflow : comment les prompts sont stockés (typiquement dans le repo aux côtés du code), comment ils sont revus (PR sur les prompts), comment ils sont composés (un prompt master qui hérite de prompts modulaires), et comment ils évoluent (un prompt qui ne marche plus est traité comme un bug).

### Pourquoi ça change le rapport au LLM

Quand le prompt est versionné, l'output devient reproductible (à la stochasticité près). Quand le prompt est revu, l'intention est partagée. Quand le prompt est réutilisable, on capitalise sur les bons patterns au lieu de les redécouvrir.

## Pourquoi ça compte

SPDD nomme ce que beaucoup d'équipes commencent à faire intuitivement. Avoir un vocabulaire et un canvas formel facilite l'adoption au-delà des praticiens individuels — c'est exactement ce qui manque pour passer du "ça marche pour moi" au "ça marche pour notre organisation".
