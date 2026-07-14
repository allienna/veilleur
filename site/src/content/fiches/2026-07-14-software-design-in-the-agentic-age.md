---
title: "Software Design in the Agentic Age: Place Your Bets"
date: 2026-07-14
url: https://link.mail.beehiiv.com/ss/c/u001.sGoRjeV3QKXxxm_cll-jKWdsoPloiCvDY_hdYQQOhj_lUxqsDO0sTAKBd4zLBYg_Pyg91PK9T_wPsASfGTpvvQlXUlm8E0FjdZd8sKo2XxfYtMPez9jBCmHC-uyERhZ3MFe8uzkIquVeYnNGxhPV7WM3_oTb5I1Ar5JegfFnz6V_Zk_qDjW6Me5Q0u23RuBE/4sb/L5ZMi-hyQSeHr_sJ4UpZoQ/h16/h001.cBrd2INnsmX1Pk3yp_e7MPtjgzD7kp5SqEoEgGgCmOE
authors: [Thoughtworks, Martin Fowler]
keywords: [design logiciel, agents, spécifications, qualité de code, harness engineering]
theme: IA
tone: opinion
used_in: ["2026-07-14"]
---

## Résumé

Compte rendu du retreat « Future of Software Engineering » de Thoughtworks (Engelberg, Suisse), un événement sur invitation réunissant une soixantaine de leaders et hébergé par Martin Fowler. Les débats portaient principalement sur le développement agentique. Thèse : la qualité du code bas niveau est probablement encore importante mais automatisable ; le design de haut niveau reste du territoire humain avec des assistances IA ; le focus se déplace du code vers les modèles de domaine et les spécifications, qui pourraient remplacer le code comme unique source de vérité. La rigueur et les pratiques d'ingénierie restent cruciales, et il faut se couvrir contre les risques de l'IA en gardant des systèmes qui peuvent revenir à une ingénierie humaine.

## Points clés

- La qualité de code est probablement encore importante, mais automatisable.
- Le design logiciel de haut niveau reste territoire humain, avec assistance IA.
- Le focus se déplace du code vers les modèles de domaine et les spécifications.
- Les spécifications pourraient remplacer le code comme unique source de vérité.
- Rigueur et pratiques d'ingénierie restent cruciales ; « harness engineering » vu comme moyen de garantir les résultats.
- Se couvrir contre les risques de l'IA en construisant des systèmes réversibles vers l'ingénierie humaine.

## Analyse approfondie

**Résumé**

- La qualité du code est probablement encore importante, mais automatisable.
- Le design logiciel de haut niveau reste du territoire humain avec des assistances IA.
- Le focus se déplace du code vers les modèles de domaine et les spécifications.
- Les spécifications pourraient remplacer le code comme unique source de vérité.
- La rigueur et les pratiques d'ingénierie restent cruciales.
- Se couvrir contre les risques de l'IA en construisant des systèmes qui peuvent revenir à l'ingénierie humaine.

_Cette semaine, j'ai participé au retreat « Future of Software Engineering » de Thoughtworks à Engelberg, en Suisse. C'était un événement sur invitation réunissant environ 60 leaders de l'industrie, hébergé par Martin Fowler. L'événement utilisait un format « open space », où toutes les sessions prenaient la forme de débats de groupe, majoritairement centrés sur le développement agentique. Voici quelques-unes de mes observations sur le rôle changeant du design logiciel._

### Les participants du retreat

Les participants avaient des profils très variés, et leur usage du développement agentique l'était tout autant. Certains l'utilisaient pour de petits projets et des preuves de concept, d'autres pour des parties de leur environnement de production, et quelques-uns sur des systèmes critiques et des environnements hautement régulés.

Les styles des participants allaient d'humains programmant avec de petits changements délégués au LLM, en passant par le pair programming avec LLM, la génération automatisée avec vérification humaine, la génération automatisée avec vérification automatisée, jusqu'aux pipelines « dark factory » complets. (En manufacture, une dark factory est une usine entièrement automatisée où les humains ne sont pas admis.) Dans ce style, la supervision humaine se limite presque exclusivement à améliorer la qualité des pipelines. Quel que soit le style, beaucoup s'accordaient sur la valeur du « harness engineering » comme moyen de garantir les résultats.

### Qualité du code bas niveau

Une question récurrente : à quel point devrions-nous encore nous soucier du design logiciel à la granularité du code ? Ce sont des préoccupations comme le nommage, la duplication de code, le code mort, le mélange de responsabilités, la modularité, le couplage et la cohésion. Je peux grossièrement regrouper les opinions des participants en deux arguments opposés :

1. Ces préoccupations existent pour la lisibilité et la compréhensibilité humaines du code, et impactent le coût du changement. Les agents abaissent significativement le coût du changement, et n'ont pas besoin de tels principes de design.
2. Les agents bénéficient d'un code bien structuré et bien conçu.

Les personnes du second camp ont offert des arguments convaincants :

- Les LLM ont été entraînés sur des langages humains, et ont certaines limitations similaires à celles des programmeurs humains. La clarté compte autant pour les LLM que pour nous.
- Comme [pour les humains, un code bien structuré facilite la navigation, réduit la charge contextuelle et limite les erreurs].

## Pourquoi ça compte

C'est la vision d'un panel de leaders (dont Martin Fowler) sur là où va concrètement le design logiciel : le pari que la spécification devient la source de vérité et que le rôle humain remonte vers le domaine et l'architecture. Un signal fort pour repenser les pratiques d'équipe.
