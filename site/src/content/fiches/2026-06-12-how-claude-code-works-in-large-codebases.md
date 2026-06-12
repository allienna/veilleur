---
title: "How Claude Code works in large codebases: Best practices and where to start"
date: 2026-06-12
url: "https://link.mail.beehiiv.com/ss/c/u001.Ira8ofUIq_P_lCLURPEgQ4_vmR0U0HcWuynAcra7cQDl0FA5uE8y1OfRsCQEvVCTRVRCPhGGHesSA0-U2ZztSEAbNgw3-p5KnR6pl4MuWEy1ucGOjLbVDfBgV-2Lf50xDIKA5K_O1_hOk3d0TS7DCVeIc6D540I8u8890kkLI3lKzER2fhZ0Sq8spNIZamAoQE89AOSiOq6Cd7mAhQ0JiufPtB-nYiWq2nATKwUVSng/4rf/AKVyNDvFSUaVXTyhmC3i1Q/h18/h001.BhzFsx7w363INPB-_FME9Mh0rfnXq-QZ2-U5ummJjDg"
authors: ["Anthropic"]
keywords: ["Claude Code", "monorepo", "recherche agentique", "RAG", "grands codebases"]
theme: "IA"
tone: "tutorial"
used_in: ["2026-06-12"]
---

## Résumé

Anthropic documente les patterns qui permettent à Claude Code de fonctionner efficacement dans des codebases de plusieurs millions de lignes — monorepos, systèmes legacy, microservices distribués, langages comme C, C++ ou Java. L'article explique pourquoi la recherche agentique (traverser le système de fichiers comme un ingénieur) surpasse le RAG pour les grands codebases, et quelles pratiques maximisent la qualité des résultats.

## Points clés

- Claude Code fonctionne en production dans des monorepos de millions de lignes, chez des organisations avec des milliers de développeurs.
- Contrairement au RAG, Claude Code ne nécessite pas d'index de codebase — il travaille directement sur le codebase live en local.
- Le RAG échoue à l'échelle car l'index reflète toujours un état passé : fonctions renommées, modules supprimés, conventions obsolètes.
- La recherche agentique a un prérequis : Claude doit avoir suffisamment de contexte de départ pour savoir où chercher.
- La qualité du contexte initial (CLAUDE.md, instructions de projet) conditionne directement la qualité des résultats.

## Analyse approfondie

### Pourquoi le RAG échoue dans les grands codebases

Les outils d'IA basés sur le RAG embarquent le codebase entier et en récupèrent des chunks pertinents à chaque requête. À grande échelle, les pipelines d'embedding ne suivent pas le rythme d'une équipe d'ingénieurs active. Au moment où un développeur interroge l'index, celui-ci peut refléter un codebase vieux de semaines, voire de jours. Le RAG peut alors retourner une fonction renommée il y a deux semaines, ou référencer un module supprimé lors du dernier sprint — sans aucun avertissement.

### Comment la recherche agentique fonctionne

Claude Code navigue le codebase comme le ferait un ingénieur : il traverse le système de fichiers, lit les fichiers, utilise grep pour trouver exactement ce dont il a besoin, et suit les références à travers le codebase. Il opère localement sur la machine du développeur, sans index centralisé à maintenir. Quand des milliers d'ingénieurs committent du code, chaque instance de Claude travaille sur le codebase live, jamais sur une version périmée.

### Le rôle critique du contexte de départ

L'approche agentique a un prérequis essentiel : elle fonctionne mieux quand Claude dispose d'un contexte de départ suffisant pour savoir où chercher. Dans les grands codebases, ce contexte doit être fourni explicitement — via des fichiers CLAUDE.md bien structurés, des instructions de projet claires, des points d'entrée identifiés. Sans ce contexte, l'agent doit explorer à l'aveugle, ce qui est coûteux en tokens et moins précis.

### Patterns observés pour une adoption réussie

Anthropic identifie plusieurs pratiques clés : documenter la structure du monorepo dans CLAUDE.md, fournir des exemples de commandes spécifiques aux sous-répertoires, identifier les fichiers d'entrée pour chaque domaine fonctionnel, et maintenir des conventions de nommage cohérentes qui aident l'agent à naviguer. Plus le point de départ est structuré, moins l'agent a besoin d'explorer — et meilleurs sont les résultats.

## Pourquoi ça compte

Cet article d'Anthropic est une documentation rare et concrète sur ce qui fonctionne réellement en production dans des environnements à grande échelle — il valide la thèse que la qualité du contexte fourni à l'agent est le principal levier d'amélioration des résultats, plus que le modèle lui-même.
