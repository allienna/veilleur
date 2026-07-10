---
title: "Software Design in the Agentic Age: Place Your Bets"
date: 2026-07-10
url: https://verraes.net/2026/07/software-design-in-the-agentic-age/
authors: [Mathias Verraes]
keywords: [software design, agentic development, specifications, dark factory, harness engineering]
theme: Tech
tone: opinion
used_in: ["2026-07-10"]
---

## Résumé

Mathias Verraes rapporte ses observations du retreat "Future of Software Engineering" de Thoughtworks, un événement sur invitation réunissant une soixantaine de leaders de l'industrie, hôté par Martin Fowler. Le débat central : que devient le design logiciel à l'ère du développement agentique ? Consensus émergent — la qualité de code bas niveau devient automatisable, mais le design haut niveau reste un territoire humain, avec un centre de gravité qui glisse du code vers les modèles de domaine et les spécifications.

## Points clés

- Les styles de travail vont du pair programming avec LLM jusqu'aux "dark factories" — pipelines entièrement automatisés où l'humain n'améliore que la qualité du pipeline.
- Beaucoup s'accordent sur la valeur de l'"harness engineering" comme moyen de garantir les résultats.
- Débat sur la qualité de code bas niveau : sert-elle encore, alors que les agents abaissent drastiquement le coût du changement ? Deux camps s'opposent.
- Le design haut niveau reste humain, avec assistance de l'IA ; les specs pourraient remplacer le code comme source unique de vérité.
- Recommandation de prudence : couvrir le risque de l'IA en gardant des systèmes capables de revenir à une ingénierie 100 % humaine.

## Analyse approfondie

**Résumé de l'auteur**
- La qualité de code reste probablement importante, mais elle est automatisable.
- Le design logiciel haut niveau demeure un territoire humain, avec des assists de l'IA.
- Le focus se déplace du code vers les modèles de domaine et les spécifications.
- Les spécifications pourraient remplacer le code comme source unique de vérité.
- La rigueur et les pratiques d'ingénierie restent cruciales.
- Il faut se couvrir contre les risques de l'IA en construisant des systèmes capables de revenir à une ingénierie humaine.

*Cette semaine, j'ai participé au retreat "Future of Software Engineering" de Thoughtworks à Engelberg, en Suisse. C'était un événement sur invitation réunissant une soixantaine de leaders de l'industrie, hôté par Martin Fowler. L'événement utilisait un format "open space", où toutes les sessions prenaient la forme de débats de groupe, essentiellement centrés sur le développement agentique. Voici quelques observations sur l'évolution du rôle du design logiciel.*

### Les participants du retreat

Les participants avaient des parcours très variés, et leur usage du développement agentique l'était tout autant. Certains l'utilisaient pour de petits projets et des preuves de concept, d'autres pour des parties de leur environnement de production, et quelques-uns sur des systèmes critiques et des environnements très régulés.

Les styles allaient de l'humain qui programme en déléguant de petits changements au LLM, en passant par le pair programming avec le LLM, la génération automatisée avec vérification humaine, la génération automatisée avec vérification automatisée, jusqu'aux pipelines de "dark factory" complets. (En industrie, une "dark factory" est une usine entièrement automatisée où les humains ne sont pas autorisés.) Dans ce style, la supervision humaine se limite presque exclusivement à améliorer la qualité des pipelines. Quel que soit le style, beaucoup s'accordaient sur la valeur de l'"harness engineering" comme moyen de garantir les résultats.

### La qualité de code bas niveau

Une question récurrente : à quel point devrait-on encore se soucier du design logiciel à la granularité du code ? Il s'agit de préoccupations comme le nommage, la duplication de code, le code mort, le mélange de responsabilités, la modularité, le couplage et la cohésion. On peut grossièrement regrouper les opinions des participants en deux arguments opposés :

1. Ces préoccupations existent pour la lisibilité et la compréhensibilité du code par les humains, et impactent le coût du changement. Les agents abaissent significativement ce coût, et n'ont pas besoin de tels principes de design.
2. Les agents bénéficient d'un code bien structuré et bien conçu.

Les tenants du second camp ont avancé des arguments convaincants :
- Les LLM ont été entraînés sur des langages humains, et ont des limitations similaires à celles des programmeurs humains. La clarté leur importe autant qu'à nous.
- Comme avec les humains, un code bien organisé réduit la surface que l'agent doit tenir en "tête" à un instant donné, et diminue donc les erreurs.

### Le design haut niveau

Là où l'accord se fait davantage, c'est sur l'idée que le design haut niveau — les frontières de domaine, les modèles, les contrats entre composants — reste un territoire humain, assisté par l'IA. Le focus se déplace du code lui-même vers ces modèles de domaine et vers les spécifications, qui pourraient devenir la source unique de vérité, le code n'étant plus qu'un artefact généré. La rigueur et les pratiques d'ingénierie ne disparaissent pas : elles changent d'objet.

### Placer ses paris

Face à l'incertitude, la recommandation est de se couvrir : construire des systèmes et conserver des compétences permettant de revenir à une ingénierie entièrement humaine si le pari agentique venait à déraper. On place ses paris, mais on garde une porte de sortie.

## Pourquoi ça compte

C'est l'une des rares synthèses de terrain, issue directement des architectes qui façonnent les pratiques de demain, sur ce qui reste humain quand les agents écrivent le code : le design, les modèles de domaine et les spécifications. Un repère précieux pour décider où investir ses compétences.
