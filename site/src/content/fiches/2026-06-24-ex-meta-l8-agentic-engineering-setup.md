---
title: "An Ex-Meta L8's Agentic Engineering Setup"
date: 2026-06-24
url: https://blog.bytebytego.com/p/an-ex-meta-l8s-agentic-engineering?utm_source=tldrdev
authors: [Kun Chen, blog.bytebytego.com]
keywords: [agentic engineering, workflow, productivity, terminal, engineering manager]
theme: IA
tone: tutorial
used_in: ["2026-06-24"]
---

## Résumé

Kun Chen, ancien principal engineer L8 chez Meta, Microsoft et Atlassian (où il a dirigé Rovo Dev), partage son setup complet d'ingénierie agentique après avoir quitté la big tech pour construire en solo. Il a cessé d'écrire la majorité du code lui-même et se comporte désormais comme un engineering manager dirigeant une équipe d'agents : il décide quoi construire et juge si c'est bon, l'outillage gérant presque tout entre les deux. Résultat : livrer plus de 30 PR de qualité par jour est devenu « une journée tranquille ».

## Points clés

- Le changement de posture : passer de « écrire du code » à « diriger une équipe d'agents » comme un engineering manager — rester au niveau du quoi-construire et du est-ce-bon.
- Gain de productivité revendiqué : 30+ PR de haute qualité par jour, un « flow state » constant où la qualité et la vitesse de sa pensée sont le seul goulot d'étranglement restant.
- Le résultat ne vient pas d'un outil hypé unique mais d'un long processus, souvent désordonné, pour distinguer ce qui marche en vrai de ce qui sonne bien en démo.
- Préférence assumée pour le terminal sur la GUI : garder le flow et le focus quand les mains ne quittent pas le clavier.
- Démarche concrète illustrée sur un vrai projet (« Hi Bit », un tuteur IA pour son fils), suivie de l'idée jusqu'à la PR mergée.

## Analyse approfondie

*Ceci est un billet invité de Kun Chen, ancien principal engineer L8 chez Meta, Microsoft et Atlassian, où il a dirigé le développement de Rovo Dev, le produit AI SDLC d'Atlassian. Il a quitté la big tech pour construire en solo et s'est lancé pleinement dans l'ingénierie agentique. Il déroule ci-dessous son setup complet, étape par étape.*

Bonjour à tous, Kun ici. Pour le contexte : j'ai passé des années à piloter l'adoption des agents auprès de dizaines de milliers d'ingénieurs de tous niveaux, au sein de mon entreprise et chez de nombreux clients. Passer en solo m'a en fait permis de m'appuyer encore plus sur les agents.

Voici la différence que l'usage des agents a faite sur ma productivité : livrer 30 PR de haute qualité qui atteignent mon propre standard était auparavant difficile à imaginer — c'est aujourd'hui une journée tranquille. J'ai atteint ce qui ressemble à un état de flow constant, où la qualité et la vitesse de mes pensées sont le seul goulot d'étranglement restant.

Tout cela n'est pas venu d'une astuce unique ou d'un outil hypé. C'est venu d'un processus long et souvent désordonné pour comprendre ce qui marche vraiment dans le monde réel, par opposition à ce qui sonne bien en démo. La version courte : j'ai maintenant arrêté d'écrire la plupart du code moi-même et j'ai commencé à agir comme un engineering manager dirigeant une équipe d'agents. Je reste au niveau de la décision sur quoi construire et sur la qualité, et j'ai construit l'outillage pour gérer presque tout ce qu'il y a entre les deux.

La partie intéressante de ce parcours, c'est toute la friction que j'ai dû retirer pour en arriver là. Dans ce billet, j'essaie donc de partager tout ce que je fais, étape par étape, pour mes projets professionnels et personnels.

Si vous êtes dans le même parcours pour rendre votre travail avec les agents plus productif et agréable, j'espère que cela vous donnera une longueur d'avance.

Premièrement, ce que je partage ici est mon setup personnel. Ce qui marche bien pour moi n'est peut-être pas le meilleur choix pour tout le monde. Je le partage tel quel, surtout dans l'espoir qu'il soit une référence utile ou une source d'inspiration sur quoi explorer.

Deuxièmement, je n'ai aucune affiliation avec les produits tiers que je mentionne, et les outils que j'ai construits sont tous gratuits et open source. Je cite ces produits parce que ce sont sincèrement ceux que j'utilise. Ce ne sont souvent pas les seuls choix possibles, donc je vous encourage à étudier différentes options selon vos intérêts et vos besoins.

Pour rendre ce billet concret et pratique, je vais vous guider à travers mon workflow en utilisant un vrai projet que je construis activement. Il s'appelle « Hi Bit » : un tuteur IA que je fabrique pour mon fils afin de lui enseigner l'ingénierie agentique. Dans la suite, je suivrai l'implémentation d'une fonctionnalité précise d'entrée d'image dans le projet Hi Bit, de l'idée jusqu'à la PR mergée, pour que vous ayez une vue de première main de mon workflow agentique.

### Terminal vs GUI

Il y a un débat constant dans la communauté des développeurs : terminal contre interface graphique. Je suis évidemment biaisé : j'ai commencé à coder il y a près de 30 ans et j'ai construit des décennies de mémoire musculaire sur un workflow centré terminal depuis. Mais j'ai essayé des GUIs de temps en temps, de Visual Basic, Visual Studio, à Atom, et maintenant la dernière app Codex.

La raison pour laquelle je m'en tiens aux terminaux est très simple : je garde mon flow et mon focus au mieux quand mes mains ne quittent jamais le clavier.

## Pourquoi ça compte

C'est le contrepoint « terrain » des billets théoriques sur la boucle et le harness : un staff+ engineer crédible montre que la productivité de l'ingénierie agentique est réelle et chiffrable, et que le métier glisse vers un rôle de management d'agents plutôt que d'écriture de code.
