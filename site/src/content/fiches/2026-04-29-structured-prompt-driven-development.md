---
title: "Structured-Prompt-Driven Development (SPDD)"
date: 2026-04-29
url: https://martinfowler.com/articles/structured-prompt-driven/
authors: [Martin Fowler, Thoughtworks]
keywords: [SPDD, prompts, gouvernance, REASONS, ingénierie logicielle]
theme: IA
tone: opinion
used_in: ["2026-04-29"]
---

## Résumé

Thoughtworks propose une méthode d'ingénierie baptisée SPDD (Structured Prompt-Driven Development) qui traite les prompts comme des artefacts de livraison de premier rang : versionnés, revus, réutilisés, améliorés. La méthode part d'un constat : la vélocité individuelle apportée par les assistants IA ne se traduit pas automatiquement en throughput au niveau système. Au cœur de SPDD, le canvas REASONS — sept dimensions structurant le passage de l'intention au code.

## Points clés

- L'IA accélère le typage individuel, mais le delivery est rarement limité par le typage.
- Les frictions remontent au niveau des requirements ambigus, des reviews surchargées, et du risque en production.
- SPDD traite les prompts comme des assets versionnables, reviewables, réutilisables.
- Le canvas REASONS structure un prompt en sept parties : Requirements, Entities, Approach, Structure, tâches, Normes, Safeguards.
- Objectif : rendre les changements générés par IA gouvernables et fiables au niveau organisationnel.

## Analyse approfondie

Une fois qu'une équipe adopte les assistants de coding IA, les premiers gains apparaissent au niveau individuel : un développeur peut rédiger, modifier et refactorer du code beaucoup plus vite qu'avant. Mais la vitesse de delivery est rarement limitée par le typage. Quand on regarde l'ensemble du cycle de delivery, des requirements à la release, de nouvelles frictions apparaissent :

- Les requirements ambigus deviennent du code rapidement, et les malentendus passent à l'échelle avec.
- Les reviews doivent traiter plus de changements, et l'incohérence devient plus facile à introduire.
- Plus de problèmes d'intégration et de test surfacent parce que "généré" ne veut pas dire "aligné".
- Le risque en production est plus dur à raisonner quand le volume de changement augmente.

Donc oui, la vitesse locale s'améliore. Mais cela ne se traduit pas automatiquement en throughput au niveau système. C'est comme acheter une Ferrari et la conduire sur des chemins boueux : le moteur est puissant, mais ton heure d'arrivée est déterminée par l'état des routes et le trafic. Selon notre expérience, la vraie question n'est pas "comment générer plus de code". C'est : comment rendre les changements générés par IA gouvernables, reviewables et réutilisables, pour que les équipes deviennent plus rapides et plus sûres ?

C'est ce qui a mené nos équipes IT internes Thoughtworks (Global IT Services) vers une méthode et un workflow qu'on appelle maintenant Structured Prompt-Driven Development (SPDD). SPDD vise à transformer l'assistance IA d'une efficacité personnelle en une capacité organisationnelle qui passe à l'échelle, sans sacrifier la qualité.

### Qu'est-ce que SPDD ?

SPDD est une méthode d'ingénierie qui traite les prompts comme des artefacts de livraison de premier rang.

Au lieu de s'appuyer sur des chats ad hoc, SPDD transforme les prompts en assets qui peuvent être : versionnés, reviewés, réutilisés, améliorés dans le temps. Les équipes utilisent des prompts structurés pour capturer requirements, langage du domaine, intention de design, contraintes, et un découpage de tâches. Ensuite le LLM génère du code à l'intérieur d'une frontière définie, donc la sortie devient plus prévisible et plus facile à valider.

Elle a deux composants centraux.

### Le canvas REASONS

Le canvas REASONS est une structure pour générer des prompts. Il force la clarté autour des requirements, du modèle du domaine, de l'approche solution, de la structure système, du découpage de tâches, des normes réutilisables, et des garde-fous. Le LLM est ainsi guidé par l'intention, pas par la devinette.

Le canvas REASONS est une structure en sept parties qui guide un prompt de l'intention au design, de l'exécution à la gouvernance.

**Parties abstraites (intention & design)**

- R — Requirements : quel problème résout-on, et quelle est la définition de "done" ?
- E — Entities : entités du domaine et relations.
- A — Approach : la stratégie pour répondre aux requirements.
- S — Structure : où placer les changements dans l'architecture.

## Pourquoi ça compte

SPDD est l'un des premiers cadres méthodologiques sérieux pour industrialiser le coding assisté par IA dans une organisation. Pour tout Engineering Manager qui se demande comment passer du "tout le monde fait du Cursor" à une discipline d'équipe, c'est une lecture de référence.
