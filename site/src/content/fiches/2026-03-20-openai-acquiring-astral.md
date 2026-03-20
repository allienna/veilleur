---
title: "Thoughts on OpenAI acquiring Astral and uv/ruff/ty"
date: 2026-03-20
url: https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/
authors: [Simon Willison]
keywords: [OpenAI, Astral, uv, open source, acquisition]
theme: IA
tone: opinion
used_in: ["2026-03-20"]
---

## Résumé

Simon Willison analyse l'acquisition d'Astral par OpenAI, l'entreprise derrière les outils Python uv, Ruff et ty. Il s'interroge sur la nature réelle de cette acquisition — talent ou produit — et sur l'avenir des projets open source qui sont devenus des infrastructures critiques pour l'écosystème Python. Willison souligne que les promesses de maintien de l'open source par les acquéreurs ont historiquement tendance à s'estomper après un à deux ans. L'article met en lumière une tension plus large : la dépendance croissante de l'infrastructure open source à la bonne volonté des grandes entreprises.

## Points clés

- OpenAI acquiert Astral pour intégrer leurs outils dans l'écosystème Codex, qui compte plus de 2 millions d'utilisateurs actifs hebdomadaires avec une croissance 3x des utilisateurs et 5x de l'utilisation
- Astral a développé des outils Python devenus incontournables : uv (gestion des dépendances et environnements), Ruff (linting et formatage rapide) et ty (sécurité des types)
- Le CLI Codex est écrit en Rust, et Astral emploie des ingénieurs Rust de premier plan, dont BurntSushi (auteur de regex, ripgrep, jiff)
- Willison questionne la dualité talent/produit de l'acquisition : il s'attend aux deux, mais avertit que les acquisitions "produit + talent" finissent souvent par n'être que du talent
- uv est l'outil le plus impactant — il a résolu les problèmes historiques de gestion d'environnement de Python et constitue désormais une infrastructure critique
- Les promesses de maintien de l'open source après acquisition ont historiquement tendance à s'effacer au bout d'un à deux ans

## Analyse approfondie

### L'annonce et le contexte

OpenAI a annoncé l'acquisition d'Astral, la startup derrière uv, Ruff et ty — trois outils qui ont transformé l'écosystème de développement Python. Cette acquisition intervient dans un contexte où Codex, l'agent de code d'OpenAI, connaît une croissance spectaculaire : plus de 2 millions d'utilisateurs actifs par semaine, une multiplication par 3 du nombre d'utilisateurs et par 5 de l'utilisation.

### Acquisition de talent ou de produit ?

Willison pose la question centrale : s'agit-il d'une acquisition de talents ou d'une acquisition de produit ? Il s'attend à ce que la réponse soit "les deux", mais prévient que l'histoire montre un schéma récurrent. Les acquisitions annoncées comme "produit + talent" ont souvent tendance à dériver vers du talent uniquement. L'entreprise acquéreuse intègre les ingénieurs dans ses propres projets, et les produits acquis finissent par être progressivement abandonnés ou mis en maintenance minimale.

### Le facteur Rust

Un angle important de cette acquisition est la dimension Rust. Le CLI de Codex est écrit en Rust, et Astral emploie certains des meilleurs ingénieurs Rust au monde. Parmi eux, BurntSushi — Andrew Gallant — l'auteur de la bibliothèque regex de Rust, de ripgrep et de jiff (une bibliothèque de gestion du temps). Willison note que cela brouille le message : cette acquisition concerne-t-elle le talent Rust pour le CLI Codex, ou l'intégration des outils Python dans l'écosystème OpenAI ? La communication d'OpenAI ne clarifie pas cette ambiguïté.

### uv : l'outil le plus impactant

Willison consacre une attention particulière à uv. De tous les outils d'Astral, c'est celui qui a eu l'impact le plus profond sur l'écosystème Python. Python a souffert pendant des années de problèmes chroniques de gestion d'environnement et de dépendances — un sujet de frustration constant pour les développeurs. uv a résolu ces problèmes de manière élégante et performante, devenant rapidement une infrastructure critique sur laquelle reposent d'innombrables projets et workflows.

Le fait qu'un outil aussi fondamental dépende désormais des décisions stratégiques d'OpenAI est une source d'inquiétude légitime pour Willison.

### Les promesses open source et leur durée de vie

Willison aborde frontalement la question de la pérennité des projets open source après une acquisition. OpenAI promet de maintenir uv, Ruff et ty en open source. Mais l'histoire du secteur montre que ces promesses ont une durée de vie limitée. Typiquement, après un à deux ans, les priorités changent, les ressources sont réallouées, et les projets open source acquis perdent progressivement leur dynamique.

Ce n'est pas nécessairement de la mauvaise foi : les réalités économiques et stratégiques de l'entreprise acquéreuse finissent par primer sur les engagements pris au moment de l'annonce.

### Une préoccupation plus large

Au-delà du cas spécifique d'Astral, Willison pointe une tendance structurelle préoccupante : l'infrastructure open source devient de plus en plus dépendante de la bonne volonté des grandes entreprises. Quand des outils fondamentaux comme uv passent sous le contrôle d'une entreprise dont le coeur de métier est ailleurs, la communauté se retrouve dans une position de vulnérabilité.

La question n'est pas de savoir si OpenAI a de bonnes intentions aujourd'hui — c'est de savoir ce qui se passe quand les priorités évoluent, quand les ingénieurs clés sont absorbés par d'autres projets, ou quand la stratégie de l'entreprise change de direction.

## Pourquoi ça compte

Cette acquisition illustre une tension fondamentale de l'écosystème tech actuel : les outils open source les plus critiques sont souvent développés par de petites équipes qui finissent par être absorbées par les géants. Pour quiconque utilise uv ou Ruff au quotidien — et c'est le cas de beaucoup de développeurs Python — la question de la pérennité de ces outils est désormais directement liée aux décisions stratégiques d'OpenAI.
