---
title: "OpenClaw has 500,000 instances and no enterprise kill switch"
date: 2026-04-01
url: "https://venturebeat.com/security/openclaw-500000-instances-no-enterprise-kill-switch"
authors: ["Louis Columbus", "VentureBeat"]
keywords: [OpenClaw, agents IA, sécurité, gouvernance, zero trust, RSAC 2026]
theme: "IA"
tone: "news"
used_in: ["2026-04-01"]
---

## Résumé

L'assistant IA personnel OpenClaw, avec 500 000 instances déployées et aucun mécanisme de contrôle entreprise, illustre les risques de la prolifération d'agents IA non gouvernés. Un cas documenté montre un CEO dont l'instance OpenClaw — contenant conversations, base de données de production et clés API — a été mise en vente sur BreachForums pour 25 000 dollars en crypto.

## Points clés

- OpenClaw compte 500 000 instances déployées sans aucun kill switch entreprise natif
- Un CEO britannique a vu son instance OpenClaw mise en vente sur BreachForums comme flux d'intelligence en temps réel
- Les données stockées en clair dans des fichiers Markdown sous ~/.openclaw/workspace/ sans chiffrement
- Le listing incluait : conversations IA, base de production, tokens Telegram, clés API Trading 212, informations personnelles
- L'industrie a accordé aux agents IA un niveau d'autonomie qu'elle n'accorderait jamais à un employé humain

## Analyse approfondie

« Your AI? It's my AI now. » Cette phrase d'Etay Maor, VP Threat Intelligence chez Cato Networks, prononcée lors de RSAC 2026, résume parfaitement la situation d'OpenClaw. L'assistant IA personnel, qui compte désormais 500 000 instances déployées, ne dispose d'aucun mécanisme natif permettant aux entreprises de contrôler, auditer ou révoquer les accès de leurs employés.

La preuve concrète de ce risque est arrivée sur BreachForums trois semaines avant l'interview de Maor. Le 22 février, un acteur malveillant utilisant le pseudonyme "fluffyduck" a publié une annonce proposant un accès root à l'ordinateur d'un CEO britannique pour 25 000 dollars en Monero ou Litecoin. Mais le shell n'était pas le point de vente principal — c'était l'assistant IA OpenClaw du CEO.

L'acheteur potentiel obtenait : chaque conversation que le CEO avait eue avec l'IA, la base de données de production complète de l'entreprise, des tokens de bot Telegram, des clés API Trading 212, et des informations personnelles que le CEO avait partagées avec l'assistant concernant sa famille et ses finances. L'acteur malveillant notait que le CEO interagissait activement avec OpenClaw en temps réel, faisant de cette annonce un flux d'intelligence en direct plutôt qu'un dump de données statique.

Vitaly Simonovich, chercheur senior en sécurité chez Cato CTRL, a documenté l'annonce le 25 février. L'instance OpenClaw du CEO stockait tout en fichiers Markdown en clair sous ~/.openclaw/workspace/ sans aucun chiffrement.

L'argument de Maor est que l'industrie a accordé aux agents IA le type d'autonomie qu'elle n'étendrait jamais à un employé humain, abandonnant au passage les principes fondamentaux de sécurité : zero trust, moindre privilège, et assume-breach. Les agents accèdent à des données sensibles, exécutent des actions, et accumulent du contexte au fil du temps — le tout sans les contrôles qu'on imposerait à n'importe quel autre système ayant ce niveau d'accès.

Le problème structurel est que OpenClaw, comme beaucoup d'outils IA personnels, a été conçu pour l'utilisateur individuel sans considération pour la gouvernance d'entreprise. Il n'y a pas de journal d'audit centralisé, pas de politique de rétention des données, pas de mécanisme de révocation à distance, et pas de chiffrement des données au repos.

## Pourquoi ça compte

Le cas OpenClaw est un signal d'alarme pour toutes les entreprises où des employés utilisent des assistants IA personnels avec des données professionnelles. Sans gouvernance, chaque instance devient un point de collecte de données sensibles non chiffrées — et donc une cible de choix pour les attaquants. La question n'est plus théorique.
