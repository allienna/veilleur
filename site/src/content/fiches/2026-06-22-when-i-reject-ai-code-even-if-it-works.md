---
title: "When I reject AI code even if it works"
date: 2026-06-22
url: https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/
authors: [Vinícius Brasil]
keywords: [revue de code, agents, relecture, jugement, qualité]
theme: IA
tone: opinion
used_in: ["2026-06-22"]
---

## Résumé

À mesure que l'implémentation s'accélère, le vrai goulot d'étranglement se déplace vers la relecture du volume de code généré par l'IA — y compris son propre `git diff`. Vinícius Brasil explique pourquoi il rejette régulièrement du code IA *même quand il fonctionne*, et liste ses critères précis. Sa thèse : du code qui passe la CI peut quand même être une mauvaise solution, et les agents ont toujours besoin d'un bon ingénieur pour les guider.

## Points clés

- Le goulot d'étranglement passe de l'écriture à la relecture du code généré.
- La différence entre une première session ratée et une seconde réussie n'est pas le modèle, mais la personne derrière l'écran.
- Critères de rejet : approche inexplicable avec ses propres mots, diff plus gros que le problème, abstractions prématurées, perte de capacité à raisonner sur le système, confiance excessive dans l'output.
- Du code qui tourne et qui fait passer la CI au vert peut rester une mauvaise solution.
- Il plaide pour une revue humaine obligatoire en complément des revues IA.

## Analyse approfondie

Avec une implémentation de plus en plus rapide, le vrai goulot d'étranglement se déplace vers la relecture du volume de code généré par l'IA. Je ne parle même pas des PR de vos collègues (et de leurs agents), mais de votre propre `git diff` une fois que votre agent de code a terminé son travail.

Même en suivant les bonnes pratiques — commencer en mode plan, découper les grandes tâches en phases, livrer de petits changements — je ressens encore une surcharge cognitive en relisant quelque chose que je n'ai pas réellement réfléchi moi-même.

Avant les agents de code, face à une tâche, j'explorais la base de code, je pensais à différentes solutions, j'expérimentais, et seulement ensuite j'implémentais. Cela pouvait prendre des jours à consolider tout ce contexte. Quand je soumettais enfin cette PR, la confiance était plus élevée, et expliquer chacun de mes changements à mes collègues était plus facile.

Je dois admettre qu'avec l'IA, terminer de grandes tâches me prend toujours des jours. Le plus souvent, je rejette tous les changements faits par l'IA et je recommence. La différence entre la première session et la seconde n'est pas le modèle de LLM, mais la personne derrière l'écran. Avec plus de temps pour consolider le problème que j'essaie de résoudre, je peux conduire l'agent vers une meilleure solution au lieu d'être conduit par lui.

De plus en plus, je rejette le code IA pour les mêmes raisons :

- Je rejette le code IA quand je ne peux pas expliquer l'approche avec mes propres mots.
- Je rejette le code IA quand le diff est plus gros que le problème.
- Je rejette le code IA quand il introduit des abstractions avant d'avoir prouvé qu'elles sont nécessaires.
- Je rejette le code IA quand il fonctionne en local mais rend le système plus difficile à raisonner.
- Je rejette le code IA quand je fais davantage confiance à l'output qu'à ma propre compréhension.

Il n'est pas rare de voir des ingénieurs accepter trop vite les changements générés par l'IA, et c'est pourquoi je plaide pour une revue humaine obligatoire en complément des revues IA. La réalité est que du code qui tourne et qui fait passer la CI au vert peut quand même être une mauvaise solution, et l'ingénierie a toujours consisté à implémenter des solutions adéquates, scalables et extensibles.

J'utilise les agents de code depuis un certain temps et, malgré leur côté impressionnant, ils ont toujours besoin d'un grand ingénieur pour les guider vers de grandes solutions. Oui, les agents de code peuvent vous aider sur cette tâche avec plus que de la simple écriture de code, mais cela ne signifie pas qu'ils peuvent le faire de manière autonome et durable — *pas encore*.

## Pourquoi ça compte

Cette fiche donne des critères concrets et actionnables pour la revue de code à l'ère des agents — exactement le type de garde-fou humain que toute équipe AI-native devrait formaliser.
