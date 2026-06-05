---
title: "AI, Ashby Engineering, and the Future"
date: 2026-06-05
url: "https://www.ashbyhq.com/blog/engineering/ai-ashby-engineering-and-the-future"
authors: ["Colin (Head of EMEA Engineering, Ashby)"]
keywords: [code généré par IA, jugement, responsabilité, revue de code, culture d'ingénierie]
theme: "Leadership"
tone: "opinion"
used_in: ["2026-06-05"]
---

## Résumé

Retour d'expérience d'Ashby, éditeur SaaS de recrutement (100 000 utilisateurs hebdo) : depuis août 2025, plus de la moitié du code en production est généré par l'IA, sans hausse des incidents clients ni régression de qualité. La thèse : le coût de production du code tend vers zéro, et la valeur de l'ingénieur se déplace vers le jugement, le goût et la responsabilité.

## Points clés

- Depuis août 2025, plus de 50 % du code en production d'Ashby est généré par l'IA, avec des incidents clients stables.
- Pas de régression observée en qualité, vélocité ou temps d'onboarding — la compréhension du code aurait même augmenté.
- Thèse centrale : « the cost of producing code is heading towards zero ».
- L'IA prend la partie mécanique (syntaxe, glue code, frappe) ; le jugement et le goût gagnent en valeur.
- Deux règles de fond : « Empathy cannot be replaced by AI » et « You are responsible for what you ship ».

## Analyse approfondie

### Une preuve à l'échelle, hors labo IA

Colin, Head of EMEA Engineering chez Ashby, ouvre sur un constat chiffré : depuis août 2025, plus de la moitié du nouveau code arrivant en production est généré par l'IA, tandis que les incidents clients restent globalement stables. Plus de clients, plus de code écrit par l'IA, et le ciel n'est pas tombé. Ce n'est pas un projet jouet : Ashby sert plus de 100 000 utilisateurs hebdomadaires, des millions de candidatures par semaine, avec des fonctionnalités équivalentes à des produits entiers (comparables à Calendly ou Looker). L'auteur note même une absence de régression en qualité, vélocité ou onboarding — et anecdotiquement, une meilleure compréhension de la base de code.

### Le coût du code tend vers zéro

La thèse : « Our thesis is that the cost of producing code is heading towards zero. » L'IA ne vient pas pour le métier, mais pour ses parties mécaniques — syntaxe, glue code, les *tip-taps* du clavier, c'est-à-dire les portions les moins intéressantes. Ce qui compte pour l'ingénieur — son jugement, son goût, sa compréhension des clients — gagne en importance. La valeur de l'ingénieur a toujours résidé dans son jugement ; chaque gain d'efficacité sur la production de code a déplacé le rôle dans cette direction, et l'IA sera le plus grand de ces déplacements. Un ingénieur, Tom, témoigne : « Almost all my PRs are entirely AI-written now. I implemented an entire data ingestion via AI… It's ~40 PRs ».

### Les deux règles de fond

Face à ce basculement, Ashby pose deux garde-fous. D'abord, « Empathy cannot be replaced by AI » : construire des produits est une démarche humaine ; les LLM n'ont pas de goût, ne connaissent pas les clients, ne ressentent ni la frustration d'un mauvais produit ni le plaisir d'un excellent. Dans un monde où produire quelque chose de fonctionnel est devenu ultra-rapide, savoir produire quelque chose d'excellent compte davantage. Ensuite, « You are responsible for what you ship » : peu importe qui — ou quoi — a écrit le code, l'ingénieur reste responsable de ce qu'il met en production. L'enjeu collectif est de construire un modèle mental partagé : quand faire confiance à l'IA, quand la contredire, et que changer dans les systèmes pour que « move fast » ne devienne pas « move recklessly ».

## Pourquoi ça compte

Ashby fournit la preuve qu'un éditeur SaaS ordinaire — pas un labo frontière — opère déjà majoritairement en code généré par IA sans dégradation : la bascule décrite par Anthropic n'est pas réservée à ceux qui fabriquent les modèles, et le vrai débat devient celui du jugement et de la responsabilité.
