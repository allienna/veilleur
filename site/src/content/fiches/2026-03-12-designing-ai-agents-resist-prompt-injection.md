---
title: "Designing AI agents to resist prompt injection"
date: 2026-03-12
url: "https://links.tldrnewsletter.com/IifO3y"
authors: ["OpenAI"]
keywords: ["prompt injection", "social engineering", "sécurité agents", "défense en profondeur", "manipulation"]
theme: "Sécurité"
tone: "research"
used_in: ["2026-03-12"]
---

## Résumé

OpenAI publie son analyse de l'évolution de la prompt injection : les attaques les plus efficaces ressemblent désormais à du social engineering plutôt qu'à de simples injections de commandes. L'article défend une approche de défense en profondeur — concevoir les systèmes pour que l'impact d'une manipulation reste contenu, même si certaines attaques réussissent.

## Points clés

- Les attaques par prompt injection évoluent vers du social engineering sophistiqué, pas de simples overrides
- Le filtrage des entrées ("AI firewalling") ne suffit pas car détecter une attaque revient à détecter un mensonge
- La défense efficace repose sur le design du système : limiter l'impact même si la manipulation réussit
- OpenAI compare le modèle à un employé de service client : même manipulé, ses actions doivent rester bornées
- L'approche privilégiée est la défense en profondeur plutôt que la détection parfaite

## Pourquoi ça compte

À mesure que les agents IA gagnent en autonomie (navigation web, actions pour l'utilisateur), la surface d'attaque par prompt injection explose. Cet article d'OpenAI pose un cadre de réflexion essentiel pour quiconque déploie des agents en production.
