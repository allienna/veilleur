---
title: "Cisco grabs Astrix to secure AI agents"
date: 2026-05-05
url: https://www.networkworld.com/article/4166695/cisco-grabs-astrix-to-secure-ai-agents.html?utm_source=tldrit
authors: [networkworld.com]
keywords: [Cisco, Astrix, agent security, identity management, NHI]
theme: IA
tone: news
used_in: ["2026-05-05"]
---

## Résumé

Cisco a annoncé l'acquisition d'Astrix Security, spécialiste de la sécurité des identités machines et d'agents (Non-Human Identities, NHI). L'opération vise à doter Cisco d'une couche de gestion du cycle de vie des credentials d'agents, de détection d'anomalies et de contrôle d'accès — une brique manquante dans la stack pour sécuriser les déploiements d'agents en entreprise. Le rachat s'inscrit dans une vague plus large où les grands fournisseurs d'infra construisent un control plane dédié aux agents IA.

## Points clés

- Cisco rachète Astrix Security pour adresser la sécurité des identités machines et d'agents.
- Astrix gère le cycle de vie des credentials, la détection d'anomalies et le contrôle d'accès pour des entités non humaines.
- L'enjeu : les agents IA accumulent des permissions étendues sans gouvernance claire.
- La transaction renforce la stratégie sécurité de Cisco autour des charges agentiques.
- S'inscrit dans une vague de consolidation : sécuriser les agents devient un marché à part entière.

## Analyse approfondie

Cisco a annoncé l'acquisition d'Astrix Security, une société spécialisée dans la sécurité des identités non humaines (Non-Human Identities, ou NHI). Cette opération vise à renforcer le portefeuille de Cisco autour des charges agentiques, et plus largement autour de la sécurité d'une nouvelle classe d'identités qui prolifèrent dans les SI : agents IA, services-to-services, comptes de service, tokens d'API, et autres entités automatisées qui consomment des ressources et prennent des décisions.

La proposition de valeur d'Astrix repose sur trois piliers :

- **Gestion du cycle de vie des credentials** : émission, rotation, révocation des secrets utilisés par les agents et les services. Le problème classique : un agent reçoit des permissions élargies "le temps d'un POC", puis vit indéfiniment avec ces droits, et personne ne sait plus qui l'a créé ni à quoi il sert.
- **Détection d'anomalies** : observer les comportements normaux d'une identité machine, et lever une alerte quand un agent commence à toucher des ressources qui sortent de son périmètre habituel.
- **Contrôle d'accès** : appliquer des politiques fines sur ce qu'un agent peut ou ne peut pas faire, à quel moment, depuis quelle origine.

Pour Cisco, l'enjeu est de proposer aux RSSI une couche cohérente entre la sécurité réseau historique et la sécurité d'un parc d'agents qui explose. Les déploiements actuels sont caractérisés par une absence de gouvernance des NHI : selon plusieurs études récentes, les organisations comptent désormais entre 20 et 50 identités machines pour chaque identité humaine, et la majorité de ces NHI ne sont pas gérées dans un IAM unifié.

L'opération s'inscrit dans une dynamique plus large : sécuriser les agents IA est en train de devenir un marché autonome, avec une vague de rachats et de levées chez les pure players (Astrix, Pipelock côté open source, des dizaines d'autres start-up encore confidentielles). On retrouve ici la logique éprouvée de la sécurité d'entreprise : commencer par les outils de niche (firewall, IAM, SIEM), puis voir les grands acteurs absorber ces briques pour construire des plateformes intégrées.

## Pourquoi ça compte

C'est un signal très concret de la maturation de l'IA d'entreprise : on ne parle plus seulement d'expérimentation, mais de gouvernance de production. Quand Cisco commence à racheter des spécialistes des NHI, c'est que la couche de contrôle des agents devient une exigence d'architecture, pas un nice-to-have.
