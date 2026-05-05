---
title: "Long-running Agents"
date: 2026-04-29
url: https://addyosmani.com/blog/long-running-agents/
authors: [Addy Osmani]
keywords: [agents, long-running, persistance, orchestration, sandbox]
theme: IA
tone: opinion
used_in: ["2026-04-29"]
---

## Résumé

Addy Osmani propose une définition précise de la prochaine génération d'agents IA : des systèmes capables de progresser sur un objectif à travers de multiples sessions, sandboxes et fenêtres de contexte, sur des heures, jours ou semaines. La principale rupture avec le paradigme "chat-window + boucle" tient moins à la qualité du modèle qu'à l'ingénierie autour : persistance, reprise après échec, vérification, état externalisé. L'article cartographie ce qui change, qui pousse sur le sujet, et comment un ingénieur peut commencer à utiliser ces agents sans tout réécrire.

## Points clés

- L'image dominante d'un "agent IA" — un chat avec une boucle astucieuse — a un plafond clair : oubli, fausses fins de tâche, réintroduction de bugs.
- Un agent long-running progresse à travers de multiples sessions, sandboxes, et possiblement plusieurs jours, en laissant le workspace propre pour la session suivante.
- "Long-running" recouvre trois choses différentes qu'il faut distinguer : raisonnement à long horizon, exécution étalée dans le temps, et persistance d'état.
- Le métrique "time horizon" de METR (la durée de tâche qu'un modèle frontier complète à 50 % de fiabilité) double environ tous les sept mois depuis 2019.
- L'enjeu d'ingénierie majeur : construire une couche d'état qui vit en dehors de la fenêtre de contexte, et un handoff entre sessions qui ne fasse pas perdre la tête à l'agent.

## Analyse approfondie

**Un agent IA long-running peut continuer à progresser sur des heures, des jours ou des semaines. Il peut le faire à travers de multiples fenêtres de contexte et sandboxes, se relever d'un échec, laisser derrière lui des artefacts structurés, et reprendre là où il s'était arrêté.**

Pendant deux ans, l'image dominante d'un "agent IA" a été celle d'une fenêtre de chat avec une boucle astucieuse à l'intérieur. Tu tapes un objectif, l'agent appelle quelques outils, tu regardes les tokens défiler, tu cesses de regarder quand le travail dépasse ta patience ou quand la fenêtre de contexte se remplit. Ce paradigme nous a menés loin, mais il a un plafond. Le modèle oublie. Il déclare la tâche "terminée" alors qu'elle ne l'est pas. Il réintroduit un bug qu'il avait corrigé neuf tours plus tôt. Tout l'édifice est structuré autour d'une seule séance de travail.

Les agents long-running, c'est ce qui vient après. L'idée est facile à énoncer : un agent qui continue à faire des progrès sur un objectif à travers de multiples sessions et de multiples sandboxes, possiblement plusieurs jours ou semaines, tout en laissant le workspace assez propre pour que la session suivante puisse reprendre là où la précédente s'est arrêtée. L'ingénierie est plus difficile. Il faut résoudre les problèmes de persistance, de reprise et de vérification d'une manière qui ne se contente pas de masquer les fissures. Il faut construire une couche d'état qui vit en dehors de la fenêtre de contexte du modèle, et concevoir le handoff entre sessions pour que l'agent ne perde pas la tête en se réveillant dans un sandbox différent avec une fenêtre de contexte différente.

Cet article tente d'exposer ce qui a changé, qui pousse sur le sujet, et comment un ingénieur peut utiliser dès aujourd'hui des agents long-running sans tout réécrire de zéro.

### Ce que "long-running" veut vraiment dire

"Long-running" est utilisé pour dire au moins trois choses différentes en pratique, et il est utile de les garder distinctes.

**Raisonnement à long horizon.** L'agent doit planifier et exécuter sur de nombreuses étapes dépendantes. C'est essentiellement une histoire de qualité de modèle : cohérence, planification, capacité à se rattraper d'un mauvais virage pris dix étapes plus tôt. METR suit ce sujet avec leur métrique de _time horizon_, qui estime la durée d'une tâche qu'un modèle frontier peut compléter avec une fiabilité de 50 %. Le résultat saillant : la métrique double environ tous les sept mois depuis 2019, et leur mise à jour TH1.1 plus tôt cette année a doublé le compte de tâches de 8 heures et plus dans le set d'évaluation. Si cette courbe tient, les modèles frontier seront bientôt capables d'aborder de façon crédible des tâches de plusieurs jours.

## Pourquoi ça compte

Cet article pose le vocabulaire et les contraintes d'ingénierie qui définissent la prochaine étape pour les agents IA. Pour toute équipe qui veut sortir d'une démo et tenir en production, c'est la grille de lecture indispensable.
