---
title: "OpenClaw Architecture - Part 1: Control Plane, Sessions, and the Event Loop"
date: 2026-03-09
url: "https://substack.com/redirect/a18c560e-ac92-42f6-a4b4-fc0dc8e915d1?j=eyJ1IjoibDdhcWkifQ.IAGPfPzQmxTjksjIcek6XncOmC78KnDUC_6ZThXjjTE"
authors: ["OpenClaw"]
keywords: [architecture agent, event-driven, session isolation, control plane, state machine]
theme: "Tech"
tone: "tutorial"
used_in: ["2026-03-09"]
---

## Résumé

Deep-dive technique dans l'architecture event-driven d'OpenClaw. Un daemon Gateway sert de control plane et routeur de trafic, tandis que le runtime agent gère la réflexion et l'exécution. L'isolation par sessions via des clés de session empêche les fuites de contexte. Le comportement proactif vient de timers, schedules et webhooks qui créent des événements — pas d'un raisonnement continu.

## Points clés

- Architecture décrite comme "an event-driven, session-isolated, single-writer state machine"
- Le Gateway daemon agit comme control plane et traffic controller
- Le runtime agent sépare le thinking (réflexion) du doing (exécution)
- L'isolation par sessions via des clés dédiées empêche les fuites de contexte entre agents
- Le comportement proactif repose sur des événements (timers, schedules, webhooks), pas sur un raisonnement permanent

## Analyse approfondie

La plupart des démos d'agents IA semblent magiques. OpenClaw semble autonome. Mais sous le capot, ce n'est pas de la magie — c'est un système event-driven discipliné.

OpenClaw est un assistant IA personnel, auto-hébergé et open-source, qui vit plus près du système d'exploitation qu'une application de chat classique. Au lieu de discuter dans un onglet de navigateur, il se connecte aux canaux de messagerie existants (WhatsApp, Telegram, Slack, Discord, iMessage) et peut exécuter des actions réelles via des outils.

L'architecture repose sur deux composants principaux : un Gateway (plan de contrôle) qui reçoit les événements de multiples sources et les route, et un runtime agent qui effectue un « tour » — appeler un LLM, utiliser des outils, écrire l'état et répondre. Le Gateway est le contrôleur de trafic et la source de vérité ; le runtime agent est le travailleur qui fait la « réflexion + exécution ».

L'isolation par sessions via des clés de session empêche les fuites de contexte. Quand on parle à OpenClaw depuis différents endroits (DM vs chat de groupe, Telegram vs Slack), chaque contexte reste séparé. Une file FIFO avec conscience des « lanes » garantit qu'un seul run actif par session, tout en permettant le parallélisme entre sessions différentes.

Le comportement proactif ne vient pas d'un raisonnement continu. Si l'assistant « a une idée à 3h du matin », c'est parce qu'un timer, un schedule ou un webhook a créé un événement à 3h, et l'agent a exécuté un tour normal. Les cinq vecteurs d'entrée sont : les messages utilisateur, les heartbeats (par défaut toutes les 30 minutes), les webhooks, les hooks d'automatisation et les schedules/cron.

En résumé, l'architecture d'OpenClaw se réduit à quatre pièces : le temps (heartbeats + cron), les événements (messages + hooks + webhooks), l'état (sessions + mémoire workspace sur disque) et la boucle (tours de l'agent : lire → décider → agir → écrire).

## Pourquoi ça compte

Un modèle d'architecture concret pour construire des agents "toujours allumés" qui semblent proactifs sans être magiques. Utile pour quiconque veut passer d'un prototype d'agent à un système de production.
