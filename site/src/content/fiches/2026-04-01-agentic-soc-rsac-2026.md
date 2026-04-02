---
title: "Everyone told you to deploy AI agents. No one told you what happens to your SOC when you do"
date: 2026-04-01
url: "https://venturebeat.com/security/rsac-2026-agentic-soc-agent-telemetry-security-gap"
authors: ["Louis Columbus", "VentureBeat"]
keywords: [RSAC 2026, SOC, agents IA, CrowdStrike, Cisco, sécurité entreprise]
theme: "IA"
tone: "news"
used_in: ["2026-04-01"]
---

## Résumé

À RSAC 2026, CrowdStrike, Cisco et Palo Alto Networks ont tous présenté des outils SOC agentiques, mais un écart fondamental persiste : les entreprises déploient massivement des agents IA sans disposer des bases comportementales nécessaires pour les sécuriser. 85 % des entreprises ont des pilotes d'agents en cours, mais seulement 5 % sont en production — l'écart étant dû à l'incapacité des équipes sécurité à répondre aux questions fondamentales de gouvernance.

## Points clés

- CrowdStrike détecte 1 800+ applications IA distinctes sur les endpoints entreprise, soit 160 millions d'instances uniques
- Le temps de breakout adversaire le plus rapide enregistré est tombé à 27 secondes (moyenne : 29 minutes, contre 48 en 2024)
- 85 % des entreprises ont des pilotes d'agents IA, mais seulement 5 % en production (Cisco)
- L'écart de 80 points vient de trois questions sans réponse : quels agents tournent, que sont-ils autorisés à faire, qui est responsable
- CrowdStrike, Cisco et Palo Alto Networks ont tous lancé des outils SOC agentiques à RSAC 2026

## Analyse approfondie

Le CEO de CrowdStrike, George Kurtz, a souligné dans son keynote à RSAC 2026 que le temps de breakout adversaire le plus rapide jamais enregistré est tombé à 27 secondes. La moyenne est désormais de 29 minutes, contre 48 minutes en 2024. C'est le temps dont disposent les défenseurs avant qu'une menace ne se propage. Parallèlement, les capteurs CrowdStrike détectent désormais plus de 1 800 applications IA distinctes fonctionnant sur les endpoints entreprise, représentant près de 160 millions d'instances applicatives uniques. Chacune génère des événements de détection, des événements d'identité et des journaux d'accès aux données qui affluent dans des systèmes SIEM architecturés pour des workflows à vitesse humaine.

Cisco a constaté que 85 % des entreprises clientes interrogées ont des pilotes d'agents IA en cours. Seulement 5 % ont fait passer les agents en production, selon Jeetu Patel, président et Chief Product Officer de Cisco. Cet écart de 80 points existe parce que les équipes de sécurité ne peuvent pas répondre aux questions de base que les agents imposent : quels agents fonctionnent, qu'est-ce qu'ils sont autorisés à faire, et qui est responsable quand l'un d'eux déraille.

« La menace numéro un est la complexité de la sécurité. Mais nous courons dans cette direction avec l'IA également », a déclaré Etay Maor, VP Threat Intelligence chez Cato Networks, à VentureBeat lors de RSAC 2026. Maor assiste à la conférence depuis des années et constate que le thème de 2026 est clairement l'IA agentique — mais pas dans le sens positif qu'espéraient les éditeurs. Le problème : les agents génèrent un volume de télémétrie que les SOC existants ne sont pas dimensionnés pour traiter.

Les trois géants de la cybersécurité — CrowdStrike, Cisco et Palo Alto Networks — ont tous présenté des outils SOC agentiques à RSAC 2026, reconnaissant que les approches traditionnelles ne suffisent plus face au volume et à la vitesse des menaces dans un environnement saturé d'agents IA. Cependant, un problème fondamental persiste : aucun de ces outils ne résout le déficit de base comportementale des agents. Sans savoir ce qu'un agent est censé faire normalement, il est impossible de détecter quand il fait quelque chose d'anormal.

## Pourquoi ça compte

RSAC 2026 marque le moment où l'industrie de la cybersécurité reconnaît officiellement que les agents IA créent un nouveau paradigme de menace. Le chiffre de 160 millions d'instances IA sur les endpoints devrait alerter tout engineering leader : la gouvernance des agents n'est plus un sujet futur, c'est un prérequis immédiat pour passer du pilote à la production.
