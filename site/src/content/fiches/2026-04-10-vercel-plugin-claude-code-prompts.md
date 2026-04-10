---
title: "The Vercel Plugin on Claude Code wants to read all your prompts!"
date: 2026-04-10
url: "https://links.tldrnewsletter.com/pzcJMT"
authors: ["Akshay Chugh"]
keywords: [Claude Code, Vercel, prompt injection, télémétrie, vie privée]
theme: "IA"
tone: "opinion"
used_in: ["2026-04-10"]
---

## Résumé

Akshay Chugh révèle que le plugin Vercel pour Claude Code tente de lire l'intégralité des prompts de l'utilisateur, et ce sur tous les projets — pas uniquement ceux utilisant Vercel. Le plugin injecte des instructions comportementales dans le contexte système de Claude pour poser des questions à l'utilisateur et exécuter des commandes shell, sans aucun indicateur visuel distinguant ces requêtes de celles de Claude Code natif. L'auteur identifie un schéma préoccupant où des plugins tiers peuvent modifier le comportement d'un agent IA de manière invisible, brouillant la frontière entre assistance et surveillance.

## Points clés

- Le plugin Vercel pour Claude Code s'active sur tous les projets, pas uniquement les projets Vercel, malgré une détection de framework intégrée qui n'est pas utilisée pour limiter la télémétrie
- Le plugin n'affiche pas de prompt CLI natif : il injecte des instructions dans le contexte système de Claude pour que l'IA pose elle-même la question à l'utilisateur, rendant la demande indiscernable d'une question native
- Les données qualifiées d'"anonymes" par Vercel incluent en réalité les chaînes complètes de commandes bash envoyées aux serveurs de Vercel, sans informer l'utilisateur du caractère optionnel de cette collecte
- Le plugin constitue une forme d'injection de prompt par un plugin first-party : il injecte des instructions comportementales ordonnant à Claude de poser des questions ET d'exécuter des commandes sur le système de fichiers
- Le système de hooks et skills de Claude Code permet à n'importe quel plugin de modifier le comportement de l'agent de manière invisible pour l'utilisateur

## Analyse approfondie

### Découverte fortuite sur un projet non-Vercel

L'auteur travaillait sur un projet n'ayant aucun lien avec Vercel lorsque Claude Code a affiché une demande inattendue : partager le texte des prompts pour le plugin Vercel. Cette requête surprenante l'a conduit à examiner le fonctionnement interne du plugin, révélant un ensemble de comportements problématiques.

### Problème n°1 — Un faux consentement

Le plugin ne présente pas de prompt CLI classique à l'utilisateur. Au lieu de cela, il injecte des instructions dans le contexte système de Claude, demandant au modèle de poser lui-même une question à l'utilisateur et d'exécuter des commandes shell en fonction de la réponse. Le résultat est visuellement identique aux questions natives de Claude Code. Il n'existe aucun indicateur visuel permettant de savoir que la question provient d'un plugin tiers. L'utilisateur croit interagir avec Claude Code alors qu'il répond en réalité à une sollicitation d'un plugin externe.

### Problème n°2 — Des données "anonymes" qui ne le sont pas

Ce que Vercel qualifie de "données d'utilisation anonymes" inclut en réalité les chaînes complètes de commandes bash envoyées aux serveurs de Vercel. L'utilisateur n'est jamais informé que cette collecte est optionnelle. Le terme "anonyme" est utilisé de manière trompeuse, car les commandes bash peuvent contenir des informations sensibles sur les projets, les chemins de fichiers, les noms de services et l'infrastructure utilisée.

### Problème n°3 — Une exécution sur tous les projets

Le plugin intègre un mécanisme de détection de framework, mais ne l'utilise pas pour conditionner la collecte de télémétrie. Concrètement, même si le plugin peut détecter qu'un projet n'utilise pas Vercel, il s'exécute quand même partout. Chaque projet ouvert dans Claude Code est potentiellement concerné, indépendamment de sa nature ou de sa stack technologique.

### Problème n°4 — Le pattern d'injection de prompt

Le plugin injecte des instructions comportementales qui ordonnent à Claude de poser des questions à l'utilisateur ET d'exécuter des commandes sur le système de fichiers. Il s'agit d'une injection de prompt réalisée par un plugin first-party. Le modèle de langage devient un vecteur d'exécution pour du code tiers, sans que l'utilisateur n'ait de visibilité sur cette délégation.

### La préoccupation plus large : confiance et frontières dans l'écosystème

L'auteur élargit sa réflexion au-delà du cas Vercel. Lorsque des plugins tiers peuvent injecter des instructions comportementales dans le contexte d'un agent, la frontière entre assistance et surveillance devient floue. L'écosystème des agents IA a besoin de meilleures frontières de confiance (trust boundaries).

Le système de hooks et de skills de Claude Code signifie que n'importe quel plugin peut modifier le comportement de l'agent de manière totalement invisible pour l'utilisateur. Il n'existe pas de mécanisme clair permettant de distinguer une action initiée par Claude Code d'une action initiée par un plugin tiers. Ce manque de transparence pose un problème fondamental de confiance dans l'écosystème des outils d'IA.

## Pourquoi ça compte

Cette analyse met en lumière un angle mort critique de l'écosystème des agents IA : l'absence de frontières de confiance claires entre les plugins tiers et l'agent hôte. À mesure que les outils de développement alimentés par l'IA se généralisent, la question de la transparence et du consentement éclairé dans la collecte de données par les plugins devient un enjeu majeur de sécurité et de vie privée pour tous les développeurs.
