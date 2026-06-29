---
title: "Palana (Part 1): Why Grab built a secure platform for autonomous AI Agents"
date: 2026-06-29
url: https://substack.com/redirect/a21cb930-a684-4991-8905-f6a3a96ca110?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Grab Engineering]
keywords: [AI agents, sécurité, Kubernetes, isolation, plateforme]
theme: IA
tone: news
used_in: ["2026-06-29"]
---

## Résumé

Grab a construit Palana, une plateforme Kubernetes-native pour faire tourner des agents IA autonomes en toute sécurité. Le constat de départ : dès qu'un agent a un accès réseau, des credentials, des outils et une mémoire, ce n'est plus une interface de chat mais un workload capable d'agir — et le modèle de risque bascule. Palana donne à chaque agent un environnement contenu, observé et maintenu, sans transformer chaque nouvel agent en projet d'infrastructure sur-mesure. La plateforme fait déjà tourner des centaines d'agents en production chez Grab.

## Points clés

- Un agent doté d'accès réseau, de credentials, d'outils et de mémoire est un workload qui agit, pas un simple chatbot.
- « Faire tourner des agents dans des conteneurs » ne répond pas aux vraies questions de plateforme : identité, credentials, isolation entre utilisateurs, accès Internet, auditabilité, arrêt d'urgence.
- Palana fournit un namespace Kubernetes par agent, du stockage persistant `/data`, un ingress contrôlé, une egress médiatisée par proxy, des credentials injectés depuis Vault et un routage LLM.
- Sécurité et productivité se renforcent : si le chemin sûr est aussi le plus ergonomique, les équipes l'adoptent spontanément et les contrôles n'ont pas à être rajoutés après coup.

## Analyse approfondie

### Résumé

Les agents d'intelligence artificielle (IA) passent de l'expérimentation aux workflows d'ingénierie quotidiens. Ils peuvent lire du code, appeler des API, lancer des tests, créer des merge requests, répondre à des messages Slack et conserver un état sur la durée. Cela les rend utiles, mais change aussi le modèle de risque — surtout à mesure que les agents gagnent en autonomie dans leur usage des outils. Un agent doté d'un accès réseau, de credentials, d'outils et de mémoire n'est plus une simple interface de chat. C'est un workload capable d'agir. Plus on donne de capacités aux agents, plus ils prennent de valeur — mais plus ils deviennent risqués, et plus le maintien des contrôles et de la supervision devient difficile. On a besoin d'environnements isolés, où les capacités sont ajoutées de façon claire et intentionnelle, au lieu d'hériter de « tout ce qui est sur votre laptop ».

Palana est la plateforme Kubernetes-native de Grab pour faire tourner ces workloads en sécurité. Elle donne à chaque agent un namespace isolé, du stockage persistant, un ingress contrôlé, une egress médiatisée par proxy, l'injection de credentials adossée à Vault, un routage LLM, des contrôles d'accès Git, des logs d'audit structurés et des kill switches d'urgence. Elle est aujourd'hui utilisée pour faire tourner des centaines d'agents, incluant des environnements de développement distants, de l'automatisation Slack, des workers OpenClaw, des agents Hermes et d'autres systèmes internes à longue durée de vie.

### Introduction

La première vague d'outils de coding IA vivait au plus près de l'utilisateur : un plugin dans l'IDE, une fenêtre de chat, ou un assistant en ligne de commande tournant sur le laptop du développeur. Modèle familier, facile à adopter. Mais la même question revenait sous différentes formes : comment laisser les agents faire un travail utile dans l'entreprise sans traiter chaque nouvel agent comme un projet d'infrastructure sur-mesure ?

La réponse n'est pas simplement « faire tourner des agents dans des conteneurs ». Les conteneurs aident à packager le runtime, mais ne répondent pas aux questions de plateforme plus difficiles :

- Pour quel utilisateur cet agent agit-il ?
- Quels credentials peut-il utiliser ?
- Peut-il voir l'état d'un autre utilisateur ?
- Peut-il se connecter directement à Internet ?
- Comment inspecter l'activité LLM, Git et HTTP après un incident ?
- Comment arrêter rapidement un agent sans avoir à compter sur sa coopération ?
- Comment donner aux équipes une expérience self-service sans leur livrer un accès cluster-admin ?

### Ce qu'est Palana

Palana, système propriétaire développé en interne par l'équipe CyberSecurity de Grab, est un substrat d'exécution sécurisé pour agents autonomes et semi-autonomes. Le nom vient d'une racine sanskrite associée à la protection, l'entretien, le soin. Palana ne cherche pas à être le cerveau de l'agent : c'est l'environnement qui contient, observe et soutient l'agent pendant qu'il travaille. À haut niveau, Palana fournit :

- Un namespace Kubernetes par agent, avec RBAC, quotas de ressources, network policy et stockage scopé à l'agent.
- Une expérience en ligne de commande et un portail pour créer, lancer, arrêter, configurer et inspecter les agents.
- Un stockage `/data` persistant pour que les agents à longue durée de vie préservent mémoire, caches, dépôts et état de session entre les redémarrages.
- Un accès shell via navigateur pour les workloads interactifs (Claude Code UI, OpenCode, IDE, ttyd, flux de dev adossés à SSH).
- Un accès LLM via un wrapper LiteLLM qui injecte les credentials GrabGPT par agent depuis Vault.
- Une egress HTTP/HTTPS via un proxy Envoy ext-authz, avec vérifications de politiques Open Policy Agent (OPA) et logs de requêtes structurés.
- Des secrets « proxy-only », où les agents référencent des tokens placeholder mais ne peuvent pas lire directement les credentials sous-jacents.

### Pourquoi Grab l'a construit

Le besoin immédiat venait de la recherche en sécurité : disposer d'un endroit pour exécuter et investiguer OpenClaw et des frameworks d'agents associés sans exposer le réseau interne ni placer de credentials bruts dans le runtime de l'agent. Ce cas d'usage a imposé une conception orientée containment dès le départ. Le besoin plus large est vite devenu la productivité des développeurs : une fois les primitives en place, Palana s'est avéré utile pour le coding distant, l'automatisation Slack, les assistants internes, les expériences à longue durée et les workflows opérationnels agentiques.

Les objectifs de sécurité et de productivité se renforcent mutuellement. **Si le chemin sûr est en self-service et ergonomique, les équipes l'utiliseront davantage.** Et si le chemin productif est observable et contrôlé par politique par défaut, la sécurité appropriée est intégrée automatiquement, sans que les équipes plateforme aient à rajouter des contrôles après l'adoption.

## Pourquoi ça compte

C'est le signal le plus net que l'IA agentique quitte le laboratoire pour la production : la vraie difficulté n'est pas le modèle, c'est la plateforme — identité, isolation, audit. Un retour aux fondamentaux du platform engineering, appliqués à une nouvelle classe de workload.
