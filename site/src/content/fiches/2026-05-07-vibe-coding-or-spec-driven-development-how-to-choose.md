---
title: "Vibe coding or spec-driven development? How to choose"
date: 2026-05-07
url: https://www.infoworld.com/article/4166817/vibe-coding-or-spec-driven-development-how-to-choose.html
authors: [InfoWorld, Isaac Sacolick]
keywords: [vibe-coding, spec-driven, devops, ai-coding, productivité]
theme: IA
tone: tutorial
used_in: ["2026-05-07"]
---

## Résumé

InfoWorld compare deux approches émergentes du développement assisté par IA : le vibe coding (on prompte, l'IA génère, on itère par feeling) et le spec-driven development (on écrit la spec, l'IA exécute). L'article positionne les deux non comme rivaux mais comme outils différents pour des cas d'usage différents : vibe coding pour les protos, l'expérimentation et le citizen development ; SDD pour les systèmes durables, scalables, et les contextes régulés. Au milieu, les classiques code-generation tools (Copilot, Cursor) restent l'option par défaut pour la plupart des tâches.

## Points clés

- Trois catégories d'outils IA pour le code : code generators, vibe coding, spec-driven development
- Le vibe coding excelle pour les POCs, MVP et l'expérimentation rapide, mais peine en production
- Le SDD ajoute une étape de spécification itérative, qui sert ensuite de contrat pour la génération
- Le débat n'est pas "lequel choisir" mais "lequel pour quel cas d'usage"
- Citation marquante : "Software has long been treated like infrastructure: built to last, hard to change, expensive to replace. That model is giving way" (Chris Willis, Domo)

## Analyse approfondie

L'article part d'un constat structurel : la demande d'applications, intégrations et analytics dépasse l'offre d'équipes agiles et d'ingénieurs DevOps. À cela s'ajoutent les priorités business — sécurité applicative, modernisation cloud, dette technique — qui forcent à arbitrer en permanence. Avant l'IA, les pistes étaient le 4GL, le low-code/no-code, la SaaS configurable. L'IA générative est le prochain accélérateur.

### Trois familles d'outils, à ne pas confondre

L'auteur distingue clairement trois catégories :

1. **Code-generating tools** (Copilot, Cursor, Cline, Codex, Claude Code, Gemini Code Assist, Q Developer) : ils écrivent du code à la demande, intégrés dans l'IDE. Le travail du dev passe de l'écriture à l'expression — exigences, plateforme, critères non-fonctionnels.

2. **Vibe coding** (Bolt, Lovable, Replit) : génère prototypes, fonctionnalités et applis prêtes-à-l'emploi via une expérience itérative basée sur les prompts. Le dev observe l'IA générer le code en direct.

3. **Spec-driven development (SDD)** : ajoute une étape intermédiaire où l'équipe construit, par prompts itératifs, des documents de spécification et de design qui servent ensuite de base à la génération.

### Ce que le vibe coding fait bien

L'expérience vibe coding permet à un dev de prompter ce qu'il veut construire et de regarder l'IA produire le code en direct. Les plateformes comme Bolt, Lovable et Replit peuvent démarrer depuis un prompt unique, mais elles brillent surtout en mode planification : la plateforme reformule les exigences, pose des questions, propose des options quand les exigences sont floues.

Le "vibe" qu'on en retire, c'est l'envie d'aller vite de l'idée à l'application fonctionnelle. Et ce n'est pas réservé aux devs : business owners, fondateurs non-techniques, citizen developers s'y mettent — à condition d'apprendre les bonnes pratiques de sécurité.

> "Vibe coding enables groups within the organization to create minimal viable products or small-scale tools that greatly increase their productivity" (Duncan Ng, Vultr)

Cas d'usage typiques : POCs à mettre devant des prospects pour valider un product-market fit, automatisations de processus laborieux pour gagner en efficacité.

### Les vibes peuvent-ils aller en prod ?

C'est là que ça se corse. Plusieurs experts cités sont sceptiques :

> "Vibe coding accelerates POCs, rapid experimentation, and idea exploration, but it lacks deterministic behavior, making it fundamentally unsuitable for systems that need to be maintained, scaled, or supported long-term" (Rajesh Padmakumaran, Genpact)

> "Vibe coding accelerates experimentation, but without clear architectural constraints, observability, and performance guardrails, it introduces variability that breaks downstream systems in devops and IT operations" (Piyush Patel, Algolia)

L'auteur trace le parallèle avec le low-code/no-code : il y a dix ans, les mêmes inquiétudes (sécurité, architecture, performance, résilience opérationnelle) accompagnaient ces plateformes. Les vendeurs qui ont gagné ont construit la confiance par la transparence, et les DSI ont appris quel scaffolding, quels processus et quelle documentation étaient nécessaires pour passer à l'échelle. Le vibe coding suivra probablement la même trajectoire.

### Quand le SDD prend le relais

Pour des systèmes qui doivent durer — applications métier critiques, intégrations B2B, services soumis à des contraintes de conformité — la spec redevient le contrat. Le SDD permet de formaliser ce contrat de manière itérative et lisible avant de lancer la génération. C'est plus lent au démarrage, mais cela donne à toutes les parties prenantes (PM, architecte, sécurité, ops) un point d'ancrage commun.

### Le verdict de l'auteur

Pas de réponse binaire. La règle de décision se construit autour de :
- Maturité de la base de code (greenfield vs legacy)
- Tolérance au risque (interne vs critique)
- Qui sera responsable de la maintenance (équipe permanente vs jetable)
- Régulations applicables

Pour la majorité des organisations, l'usage à court terme sera mixte : vibe coding pour les protos et les outils internes, SDD pour ce qui touche à la prod, code generators classiques pour l'amélioration continue.

## Pourquoi ça compte

Ce comparatif est une référence utile pour les CIO et architectes qui doivent cadrer l'usage de l'IA dans leurs équipes dev. Il évite le piège du "tout vibe" comme celui du "tout spec", et propose une grille de décision pragmatique alignée sur les contraintes réelles.
