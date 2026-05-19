---
title: "bliki: Interrogatory LLM"
date: 2026-05-19
url: https://martinfowler.com/bliki/InterrogatoryLLM.html
authors: [Martin Fowler]
keywords: [LLM, context, interview, prompt pattern, Harper Reed]
theme: IA
tone: opinion
used_in: ["2026-05-19"]
---

## Résumé

Martin Fowler décrit un pattern simple mais puissant pour utiliser un LLM : au lieu de lui fournir des pages de contexte écrites à la main, on le prompte pour qu'il *nous interroge*. Une question à la fois, jusqu'à ce qu'il ait de quoi générer le document de contexte. Le pattern s'applique aussi à la revue d'un document existant par un expert humain : plutôt que de lui demander de lire, on lui fait passer une interview menée par un LLM. Et au-delà du contexte LLM, c'est aussi un moyen d'extraire de l'information de la tête de personnes qui n'aiment pas écrire.

## Points clés

- Inversion du flux habituel : c'est le LLM qui interroge l'humain, pas l'inverse
- Une question à la fois (sinon le LLM en pose plusieurs en parallèle et perd en qualité)
- Cas d'usage 1 : générer un document de contexte pour une session ultérieure
- Cas d'usage 2 : faire reviewer un document existant via une conversation
- Inspiré par le post de blog de Harper Reed
- Particulièrement utile pour les personnes qui trouvent l'écriture difficile

## Analyse approfondie

Quand on a besoin qu'un LLM réalise une tâche complexe, il faut souvent lui fournir beaucoup de contexte. Concevoir une nouvelle feature requiert des descriptions de la façon dont la feature doit apparaître à l'utilisateur, des guidelines sur la manière de l'implémenter, des informations sur les systèmes externes à consulter, etc. Tout cela peut représenter plusieurs pages de markdown. La façon évidente de procéder est qu'un humain écrive ce contexte, mais une alternative est d'utiliser un LLM pour écrire ce contexte après avoir *interviewé* un humain.

La manière de procéder : prompter le LLM pour qu'il m'interroge. Il doit poser toutes les questions dont il a besoin pour créer le contexte approprié. Je peux lui fournir une bonne partie de l'information dont il a besoin, et lui indiquer d'autres sources à consulter s'il ne peut pas trouver par lui-même. Une fois terminé, il peut générer le rapport de contexte pour une autre session (peut-être avec un autre modèle) qui mènera l'étape suivante.

Fowler attribue la description initiale de cette approche au [blog de Harper Reed](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/). Un élément frappant de cette approche est d'insister sur le fait que le LLM ne doit poser **qu'une question à la fois**. (Quand j'ai essayé, j'ai trouvé qu'il fallait fréquemment lui rappeler.)

Un autre usage de l'interrogatory LLM est de lui donner un document — par exemple une spécification logicielle — qui capture la connaissance d'un domaine, et de lui demander d'interviewer un expert humain pour déterminer si le document est exact. C'est une alternative à demander à l'expert humain de lire le document pour le reviewer. Beaucoup de gens trouvent la review difficile, donc une conversation avec un LLM peut être plus fructueuse — particulièrement si le document n'est pas bien écrit.

On peut naturellement combiner les deux : utiliser un interrogatory LLM pour construire un document, puis d'autres interrogatory LLMs pour le faire reviewer avec d'autres experts.

### Une portée plus large

Ce qui précède concerne l'utilisation d'un LLM pour créer ou évaluer du contexte destiné à un autre usage de LLM. Mais la technique a une portée plus large. Fowler explique qu'il est devenu un "natural writer", quelqu'un qui trouve dans le processus d'écriture une partie essentielle de la pensée. Pour vraiment comprendre quelque chose, il a besoin d'écrire à son sujet. Mais les gens sont différents. Beaucoup trouvent l'écriture difficile, parfois *très* difficile.

Cela peut devenir un vrai problème quand on a besoin de faire sortir de l'information de la tête de quelqu'un sous une forme que d'autres humains pourront consommer. Peut-être que ces personnes trouveront plus facile de demander à un LLM de les interviewer plutôt que d'écrire un document elles-mêmes. Le résultat aura certainement ce *tang* d'écriture IA que les gens comme Fowler trouvent agaçant — mais c'est mieux que ne pas avoir l'information du tout, soit parce qu'elle aurait été rédigée trop vite, soit parce qu'elle n'aurait jamais été rédigée.

## Pourquoi ça compte

Un pattern simple à intégrer immédiatement dans une organisation, et qui répond à un vrai pain point : sortir la connaissance des têtes des experts qui détestent écrire. Et il offre un pont entre la culture "humain qui pense en parlant" et la culture "agent qui veut une spec complète" — exactement la couture que tout le monde cherche à coudre en ce moment.
