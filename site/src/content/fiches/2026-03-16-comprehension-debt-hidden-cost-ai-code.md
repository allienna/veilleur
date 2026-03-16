---
title: "Comprehension Debt — the hidden cost of AI generated code."
date: 2026-03-16
url: https://addyosmani.com/blog/comprehension-debt/
authors: [Addy Osmani]
keywords: [comprehension debt, AI coding, agentic engineering, cognitive debt, code understanding]
theme: IA
tone: opinion
used_in: ["2026-03-16"]
---

## Résumé

Addy Osmani identifie la "comprehension debt" comme le coût caché de l'ingénierie agentique : l'écart croissant entre le volume de code dans un système et la part que les humains comprennent réellement. Contrairement à la dette technique classique, elle génère une fausse confiance — le code semble propre, les tests passent, mais la théorie du système s'évapore.

## Points clés

- La comprehension debt est l'écart entre le code existant et le code compris par les humains
- Une étude Anthropic montre que les développeurs utilisant l'IA pour générer du code scorent plus bas en compréhension
- Margaret-Anne Storey décrit une équipe incapable de faire des changements simples en semaine 7 — pas du code sale, mais une théorie du système disparue
- Contrairement à la dette technique, la comprehension debt génère une fausse confiance
- Le vrai goulot d'étranglement a bougé : ce n'est plus la production de code, c'est la compréhension

## Analyse approfondie

Il y a un coût qui n'apparaît pas dans vos métriques de vélocité quand les équipes plongent dans les outils de coding IA. Surtout quand il est fastidieux de relire tout le code que l'IA génère. Ce coût s'accumule régulièrement, et un jour il faut le payer — avec intérêts. On l'appelle la comprehension debt ou dette cognitive.

La comprehension debt est **l'écart croissant** entre la quantité de code qui existe dans votre système et **la quantité qu'un être humain comprend véritablement**.

Contrairement à la dette technique, qui s'annonce par une friction croissante — builds lents, dépendances emmêlées, cette appréhension rampante chaque fois qu'on touche à ce module — la comprehension debt génère une fausse confiance. Le codebase a l'air propre. Les tests sont verts. Le réveil arrive discrètement, généralement au pire moment possible.

Margaret-Anne Storey décrit une équipe d'étudiants qui a heurté ce mur en semaine sept : ils ne pouvaient plus faire de changements simples **sans casser quelque chose d'inattendu**. Le vrai problème n'était pas du code sale. C'était que personne dans l'équipe ne pouvait expliquer pourquoi les décisions de design avaient été prises ni comment les différentes parties du système étaient censées fonctionner ensemble. La théorie du système s'était évaporée.

C'est la comprehension debt qui se compose en temps réel.

### L'étude Anthropic

Une étude récente d'Anthropic intitulée "How AI Impacts Skill Formation" a mis en lumière les inconvénients potentiels d'une dépendance excessive aux assistants de coding IA. Dans une étude randomisée, les développeurs qui utilisaient l'IA pour la génération de code obtenaient des scores significativement plus bas en compréhension du code par rapport à ceux qui l'utilisaient pour l'exploration conceptuelle.

### Le vrai goulot d'étranglement

L'auteur observe sur les forums de développeurs des ingénieurs qui luttent véritablement avec la version structurelle de ce problème — pas le binaire familier optimisme contre scepticisme, mais un domaine qui essaie de comprendre à quoi ressemble la rigueur quand le goulot d'étranglement a bougé.

La production de code n'est plus le facteur limitant. La compréhension l'est. Et quand les équipes accumulent de la comprehension debt, elles ne le savent pas jusqu'à ce qu'elles essaient de changer quelque chose de fondamental — et découvrent que personne ne peut expliquer comment le système fonctionne réellement.

### Les signaux d'alerte

Les signes de comprehension debt incluent :
- Des développeurs qui ne peuvent expliquer le "pourquoi" derrière les décisions de design
- Des modifications simples qui cassent des parties inattendues du système
- Une dépendance croissante aux outils IA pour comprendre le code existant
- Des revues de code qui deviennent une formalité plutôt qu'une vérification réelle

## Pourquoi ça compte

Cet article nomme un problème que l'industrie commence à peine à reconnaître. À mesure que l'ingénierie agentique se généralise, la comprehension debt pourrait devenir la principale forme de dette dans les organisations tech — plus dangereuse que la dette technique classique parce qu'invisible jusqu'au point de rupture.
