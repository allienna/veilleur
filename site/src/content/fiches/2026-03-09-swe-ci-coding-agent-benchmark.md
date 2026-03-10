---
title: "Most Coding Agents Break 75%+ of Their Own Fixes Over Time"
date: 2026-03-09
url: "https://www.engineerscodex.com/swe-ci-coding-agent-benchmark"
authors: ["Engineer's Codex"]
keywords: [SWE-CI, benchmark, régression, coding agents, maintenance]
theme: "IA"
tone: "research"
used_in: ["2026-03-09"]
---

## Résumé

SWE-CI est un nouveau benchmark qui évalue les coding agents non pas sur un fix isolé, mais sur leur capacité à maintenir du code sur la durée — 233 jours en moyenne et 71 commits consécutifs. Résultat : la plupart des modèles introduisent des régressions dans plus de 75% des tâches. Seule la série Claude Opus dépasse un taux de zéro-régression de 50%.

## Points clés

- Contrairement à SWE-bench qui teste un fix sur un snapshot, SWE-CI évalue la maintenance sur 100 tâches couvrant en moyenne 233 jours et 71 commits
- Le protocole utilise un duo Architect + Programmer pour simuler un workflow réaliste
- La plupart des modèles ont un zero-regression rate inférieur à 0,25 — ils cassent quelque chose dans 75%+ des cas
- Seule la série Claude Opus dépasse 50% de tâches sans régression
- La différence entre "corriger un bug" et "maintenir un codebase" est qualitative, pas quantitative

## Analyse approfondie

La plupart des benchmarks de coding agents demandent à un modèle de corriger un bug, dans un snapshot d'un dépôt, une seule fois. SWE-CI pose une question plus difficile : peut-on maintenir un vrai codebase sur des mois d'évolution sans casser ce qu'on vient de corriger ? Pour la plupart des modèles, la réponse est non.

Le benchmark comprend 100 tâches issues de 68 dépôts Python réels, couvrant en moyenne 233 jours et 71 commits consécutifs. 18 modèles de 8 fournisseurs ont été testés, consommant plus de 10 milliards de tokens. La plupart des modèles ont un taux de zéro-régression inférieur à 0,25 — ils introduisent des régressions dans plus de 75 % des tâches.

Le problème de SWE-bench, le benchmark canonique, est qu'il évalue des corrections isolées. Les vrais codebases évoluent : une fonctionnalité ajoutée en janvier affecte les tests en mars. SWE-CI introduit un paradigme « basé sur l'évolution » : chaque tâche se déroule sur jusqu'à 20 itérations CI, où l'agent doit faire des changements qui passent les tests d'aujourd'hui sans défaire ce qui fonctionnait déjà.

Le protocole d'évaluation utilise un duo d'agents : l'Architecte analyse les tests en échec et rédige un document de spécifications, le Programmeur implémente les modifications. Ce découpage mime un workflow d'ingénierie réaliste. Le scoring se fait via EvoScore, une métrique pondérée par le futur qui récompense la stabilité à long terme.

Claude Opus est l'exception notable : c'est la seule famille de modèles à dépasser un taux de zéro-régression de 50 %. Au sein de chaque famille de fournisseurs, les modèles plus récents surpassent systématiquement les plus anciens — mais aucun n'a « résolu » la maintenabilité.

## Pourquoi ça compte

Ce benchmark change la conversation sur les coding agents : la question n'est plus "peut-il résoudre ce ticket ?" mais "peut-il travailler sur ce repo pendant 8 mois sans tout casser ?". C'est le critère qui compte pour une adoption en production.
