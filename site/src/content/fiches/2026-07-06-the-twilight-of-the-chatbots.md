---
title: "The twilight of the chatbots"
date: 2026-07-06
url: https://www.oneusefulthing.org/p/the-twilight-of-the-chatbots
authors: [Ethan Mollick]
keywords: [agents, exponentiel, capability, harness, management]
theme: IA
tone: opinion
used_in: ["2026-07-06"]
---

## Résumé

Ethan Mollick soutient que les modèles progressent à un rythme « plus qu'exponentiel », mesuré par METR, l'AI Security Institute britannique, GDPval et Epoch (Opus 4.7 : 14 h d'autonomie pour un logiciel valant 2 à 17 semaines de travail humain, 251 $ de tokens). Cette montée en capacité fait basculer l'usage : on quitte le chatbot-copilote pour l'agent qu'on pilote comme un manager. Le facteur décisif de réussite n'est plus le métier mais l'expertise du domaine. Et comme on est « à l'intérieur » d'une exponentielle, chaque saut est vécu comme un choc, ce qui explique la turbulence permanente autour de l'IA.

## Points clés

- Les capacités augmentent à un rythme meilleur qu'exponentiel, malgré une frontière « en dents de scie » où l'IA reste faible par endroits.
- Epoch : Opus 4.7 a construit en 14 h un logiciel équivalent à 2-17 semaines de dev pour 251 $ ; Mollick a vu Fable tourner 9 h en autonomie.
- Les modèles chinois open-weights suivent leur propre courbe exponentielle, 6-12 mois derrière les modèles fermés américains, mais bien moins chers.
- On passe du chatbot (co-intelligence, étape par étape) à l'agent autonome doté d'un harness (Claude Code, Codex) qui améliore encore la capacité du modèle.
- Une étude OpenAI montre que l'adoption des agents progresse vite hors de la tech (juridique, RH) ; un quart des employés OpenAI font tourner au moins 4 agents en parallèle chaque semaine.
- Ce qui compte n'est pas le métier de l'utilisateur mais son expertise : plus on est expert, plus on tire de valeur de chaque prompt. La bonne posture est celle du manager.

## Analyse approfondie

Si vous avez l'impression que les choses s'accélèrent dans l'IA, vous avez probablement raison. De meilleurs modèles des grands labs américains sortent plus vite que jamais (même si des interventions gouvernementales ont temporairement bloqué l'accès à deux des modèles les plus puissants, Claude Fable et GPT-5.6).

Mais il n'y a pas que le rythme de sortie. Les preuves pointent aussi vers des gains de capacité en accélération (même si la frontière reste en dents de scie et que les IA restent faibles à bien des endroits). C'est particulièrement visible quand on regarde la capacité des IA à faire du vrai travail. Quelques bonnes évaluations tentent de mesurer combien de travail humain les IA peuvent abattre. Deux des plus célèbres, de METR et de l'AI Security Institute officiel du gouvernement britannique, estiment le nombre d'heures de travail de programmeur humain que l'IA peut réaliser avec un seul prompt. GDPval compare des experts humains de nombreux domaines à la performance de l'IA à l'aide de juges professionnels. Tous augmentent à un rythme meilleur qu'exponentiel.

Une autre organisation menant des expériences similaires, Epoch, a récemment constaté qu'Opus 4.7, travaillant seul pendant 14 heures, a pu construire un paquet logiciel qui aurait pris 2 à 17 semaines de travail d'ingénierie humaine (coût : 251 $ en tokens). Là encore, les systèmes d'IA ne passent pas tous les tests et ne sont pas toujours bon marché à faire tourner, mais ils s'améliorent à un rythme très rapide. Dans mes propres expériences, j'ai trouvé que Fable pouvait travailler en autonomie pendant 9 heures pour exécuter des projets logiciels très complexes qui auraient pris à une équipe bien plus d'une semaine.

Jusqu'ici, je me suis concentré sur les modèles de frontière, ceux à la plus haute « intelligence ». Ils sont fabriqués par trois entreprises américaines — Anthropic, OpenAI et Google (même si ça fait un moment que Google n'a pas sorti de nouveau modèle). Mais il existe un second ensemble de modèles quasi-frontière, avec un retard typique de 6-12 mois, tous chinois. Ce sont des modèles à poids ouverts (open weights), que n'importe qui peut utiliser ou modifier après leur sortie (à l'inverse des modèles de frontière, propriétaires). Cela les rend assez bon marché à exploiter. Eux aussi grimpent une courbe d'amélioration exponentielle, bien qu'à la traîne des modèles fermés américains. On le voit dans mon graphe de performance sur un test appelé AA-Briefcase, qui simule une mission de conseil complexe sur plusieurs semaines : les modèles chinois open-weights sont sur leur propre courbe exponentielle, derrière les modèles fermés US.

Mais les graphes abstraits n'emmènent pas très loin et peuvent masquer à quel point la frontière est en dents de scie (et le fait que les modèles open-weights, bien qu'impressionnants, ne performent pas toujours aussi bien que leurs benchmarks le suggèrent). Pour un vrai éclairage, il faut essayer d'utiliser l'IA sur différents cas d'usage et évaluer rigoureusement leur qualité dans les domaines qui vous importent. Comme exemple ludique, j'ai créé un test où les IA doivent construire une simulation interactive d'un port évoluant dans le temps. Cela donne une perspective intéressante sur à quel point les modèles peuvent différer dans des domaines comme le design, l'approche stylistique et même le jugement. À mesure que les systèmes accomplissent des tâches plus longues, ces facteurs difficiles à benchmarker deviennent plus importants.

À mesure que les IA peuvent réaliser des tâches de plus en plus longues, la manière dont les gens utilisent l'IA change. Jusqu'à récemment, la façon dominante d'utiliser l'IA était comme co-intelligence : on demande quelque chose à l'IA, on vérifie les résultats, puis on demande l'étape suivante. Par un prompting soigneux et de l'attention humaine, on pouvait guider les IA sur des tâches complexes et de long terme.

Cette approche reste courante et utile, mais de plus en plus, ce n'est pas ainsi que l'IA est utilisée pour un travail à forte valeur. Les systèmes d'IA longs, intelligents et auto-correcteurs n'ont pas besoin d'intervention humaine constante et exigent une autre façon de travailler (c'est aussi le sujet de mon prochain livre, Co-Existence). Contrairement aux chatbots, les agents viennent avec une machinerie supplémentaire : des harnesses qui donnent à l'IA accès à des outils et à un environnement pour agir, et des applications conçues pour les agents comme Claude Code ou Codex d'OpenAI. Résultat, la capacité déjà croissante des modèles peut être encore améliorée par un bon harness ou une bonne app.

Le travail consiste donc de plus en plus à assigner du travail à des agents, plutôt qu'à travailler avec des chatbots. Une étude conjointe d'OpenAI et d'économistes académiques montre à quelle vitesse cela se produit dans leur propre organisation. Point crucial : il n'y a pas que les développeurs qui utilisent des agents. Le juridique, les RH et d'autres fonctions non-tech les ont adoptés à un rythme presque identique. OpenAI est peut-être une sorte de canari dans la mine pour ce qui arrivera ailleurs.

De plus en plus, le travail chez OpenAI ressemble à du management d'IA. Un quart des employés d'OpenAI ont au moins quatre agents en fonctionnement simultané chaque semaine. Et comme le code est écrit par des IA dans des harnesses et apps spécialisés, d'autres rôles deviennent des sortes de développeurs. Et ils sont bons. Une étude distincte des utilisateurs de Claude Code a trouvé que les ingénieurs logiciels avaient un taux de succès similaire à celui d'autres professions quand ils utilisaient réellement Claude Code sur des tâches de code.

Ce qui comptait vraiment n'était pas la profession de l'utilisateur, mais son expertise. Plus quelqu'un avait d'expérience dans un domaine, plus il réussissait à utiliser Claude Code dans ce domaine. Et, plus intéressant encore, plus il obtenait de sortie utile de Claude à chaque prompt. Nous passons d'un monde où des non-experts utilisent des chatbots pour combler des lacunes à un monde où des experts utilisent des agents pour accomplir du travail. Et la meilleure façon d'utiliser des agents est de se penser soi-même comme un manager.

Être sur une exponentielle signifie que chaque changement sur une fenêtre fixe est plus grand que le précédent. Si votre organisation a écrit un plan IA avant l'hiver 2025, il décrivait un système capable de quelques heures de travail avec un taux d'erreur assez élevé. Quelques mois plus tard, on obtient seize heures de travail ou plus à partir d'un seul prompt. C'est pourquoi l'IA continue de donner l'impression de faire des bonds, même s'il s'agit d'une courbe sur un graphe : nous vivons un doublement régulier de la capacité comme une série de chocs. Nous sommes très mauvais pour ressentir les exponentielles de l'intérieur, et nous sommes actuellement à l'intérieur d'une.

Je pense que cela explique aussi la turbulence autour de l'IA mieux que les histoires habituelles de hype. L'IA n'est pas une vraie menace de cybersécurité jusqu'à ce que soudain elle le soit, provoquant des changements de politique soudains et improvisés au plus haut niveau du gouvernement. Les marchés ignorent qu'une IA pourrait menacer un modèle d'affaires jusqu'à ce que soudain elle le puisse, entraînant d'énormes variations boursières. Ces à-coups sont lus comme les signes d'un champ immature qui finira par se stabiliser. Je ne pense pas qu'il va se stabiliser de sitôt. L'instabilité est ce qui arrive quand des institutions qui avancent à la vitesse des humains (ou pire, des comités) tentent de suivre une courbe de capacité qui n'a rien d'humain. Et tant qu'on est sur une forme d'exponentielle, l'écart ne fait que se creuser.

## Pourquoi ça compte

C'est la meilleure synthèse chiffrée du basculement chatbot → agent, et elle recadre le rôle de l'ingénieur comme celui d'un manager d'agents où l'expertise, pas le prompting, fait la différence.
