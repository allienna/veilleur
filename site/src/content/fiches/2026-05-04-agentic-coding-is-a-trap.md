---
title: "Agentic Coding is a Trap"
date: 2026-05-04
url: https://larsfaye.com/articles/agentic-coding-is-a-trap?utm_source=tldrdev
authors: [Lars Faye]
keywords: [agentic coding, abstraction, skill atrophy, paradox of supervision, vendor lock-in]
theme: IA
tone: opinion
used_in: ["2026-05-04"]
---

## Résumé

Lars Faye conteste frontalement le récit dominant selon lequel l'agentic coding est l'avenir et que le développeur devient simplement un orchestrateur. Il pose quatre trade-offs quantifiables (complexité accrue, atrophie des compétences, vendor lock-in, coûts variables des tokens) et un paradoxe central : seuls les développeurs critiques et compétents peuvent piloter ces agents efficacement, mais c'est précisément cette capacité critique que l'usage des agents érode. Il s'appuie sur des études de Anthropic, Microsoft et le MIT, et sur des témoignages de Simon Willison et de directeurs ingénierie chez LinkedIn. Sa thèse : un niveau d'ambiguïté plus élevé n'est pas un niveau d'abstraction plus élevé.

## Points clés

- L'agentic coding crée un éloignement croissant entre l'orchestrateur et le code généré et committé
- Quatre trade-offs : complexité système accrue (non-déterminisme), atrophie des compétences, vendor lock-in (les outages Claude Code ont déjà bloqué des équipes entières), coûts de tokens fluctuants vs coût fixe d'un employé
- "A higher level of ambiguity is not a higher level of abstraction"
- "Paradox of supervision" (Anthropic) : utiliser efficacement Claude requiert de la supervision, et superviser Claude requiert les compétences mêmes qui s'atrophient avec la sur-utilisation de l'IA
- Sandor Nyako (Director of Software Engineering, LinkedIn) demande à ses 50 ingénieurs de ne pas utiliser ces outils pour les tâches de critical thinking ou de problem solving
- Simon Willison (30 ans d'expérience) rapporte ne plus avoir de "modèle mental ferme" de ses applications, ce qui rend chaque feature additionnelle plus dure à raisonner
- L'atrophie des compétences peut survenir en quelques mois selon les études citées
- Les juniors sont les plus exposés : reviewer du code représente au mieux 50% du processus d'apprentissage

## Analyse approfondie

> *"L'IA fait le code, et l'humain dans la boucle est l'orchestrateur"*

C'est le sentiment qui est hypé dans l'industrie en ce moment : le coding traditionnel est mort ou presque, et le Spec Driven Development (SDD) est l'avenir. Tu génères un plan, tu te déconnectes de l'écriture du code. Les agents savent mieux faire, et gèrent toute l'implémentation. Tu es là en tant qu'*expert*, pour fournir le "bon goût", reviewer les outputs, et constamment piloter le ou les agents pour exécuter le plan que tu as méticuleusement assemblé.

Le workflow prend de nombreuses formes, mais en gros, c'est un processus où quelqu'un définit les requirements du projet (simultanément à un niveau micro et macro), génère un plan, et ensuite tire sur le levier de la machine à sous encore et encore, itérant et réitérant avec souvent *plusieurs* instances d'agent jusqu'à ce que ce soit fini. Tout en mettant une distance croissante entre l'"orchestrateur" et le code qui est généré et committé.

Les coding agents sont utiles et puissants, mais il y a déjà des trade-offs quantifiables qui méritent d'être discutés :

- Une complexité accrue des systèmes environnants pour atténuer l'ambiguïté accrue du non-déterminisme de l'IA
- L'atrophie des compétences pour une large frange de la population
- Le vendor lock-in pour les individus et les équipes entières (les outages Claude Code ont déjà mis des équipes entières à l'arrêt)
- Des coûts d'accès aux outils fluctuants et croissants. Le coût d'un employé est fixe ; les tokens sont une cible mouvante constante

Le succès avec cette approche des coding agents repose sur un élément crucial : seul un développeur compétent qui pense de manière critique, et à l'aise avec le niveau architectural, peut repérer les problèmes dans des milliers de lignes de code généré, *avant* qu'ils ne deviennent un problème.

Pourtant, dans une ironie du sort, c'est précisément la pensée critique et la clarté cognitive de l'individu que les outils IA ont maintenant été prouvés impacter négativement.

### Pas juste une "abstraction" de plus

Un refrain commun dans la communauté, c'est que les programmeurs "montent juste dans la stack" vers un autre type d'abstraction. Que ces outils soient vraiment une couche d'abstraction est en soi un débat ouvert ; un niveau d'ambiguïté plus élevé n'est pas un niveau d'abstraction plus élevé.

Les programmeurs ont historiquement été méfiants des nouveaux langages : à la sortie de FORTRAN, on disait qu'il introduisait plus de bugs et plus d'instabilité, et que l'assembleur direct était plus efficace. Plus tard, on dénoncerait la "magie" introduite par les compilateurs. Mais ces craintes étaient spéculatives et théoriques. Avec l'IA, les impacts se mesurent déjà — y compris sur des devs avec une décennie ou plus d'expérience.

Les juniors sont face à une montée encore plus raide, parce qu'on tronque leur capacité à travailler avec le code et qu'on la remplace par du review de code généré. Reviewer du code, c'est important, mais c'est au mieux 50% du processus d'apprentissage. Sans la friction et les défis qui viennent du travail direct sur le code, leur capacité à apprendre est sérieusement diminuée.

### Le "paradoxe de la supervision"

Enterré dans une étude récente de Anthropic, un moment d'honnêteté surprenant sur les risques d'utiliser les coding agents au quotidien :

> Une raison pour laquelle l'atrophie des compétences de coding est inquiétante, c'est le "paradoxe de la supervision"... utiliser efficacement Claude requiert de la supervision, et superviser Claude requiert les compétences mêmes de coding qui peuvent s'atrophier avec la sur-utilisation de l'IA.

Sandor Nyako, Director of Software Engineering chez LinkedIn, qui supervise 50 ingénieurs, l'a constaté se propager dans son organisation et a demandé à son équipe de ne pas utiliser ces outils pour des "tâches qui requièrent de la pensée critique ou de la résolution de problèmes".

> "Pour développer ses compétences, il faut passer par la difficulté. Les gens doivent développer le muscle pour penser à travers les problèmes. Comment quelqu'un peut-il questionner si l'IA est juste s'il n'a pas de pensée critique ?"

Il y a aussi la question de ce qui constitue de la "sur-utilisation". On a déjà des preuves, à la fois data-driven et anecdotiques, que ces compétences peuvent s'atrophier et disparaître relativement rapidement (en quelques mois dans certains cas).

C'est la contradiction qui fait que beaucoup de boosters IA parlent des deux côtés de la bouche : l'usage des coding agents est en train de diminuer activement les compétences même dont on a besoin pour piloter efficacement les coding agents.

### Les LLM accélèrent les mauvaises parties

Contrairement au discours actuel, on n'avait pas nécessairement besoin d'écrire du code plus vite. Surtout pas du code qu'on ne comprend pas pleinement, et particulièrement pas par énormes blocs qu'on n'a pas le temps de reviewer.

## Pourquoi ça compte

C'est l'un des articles "contre-récit" les plus structurés de 2026 sur l'agentic coding. À garder sous la main quand quelqu'un dans une réunion répète "les devs vont juste devenir orchestrateurs" : la réponse n'est pas "non" mais "oui, et voilà les coûts qu'on n'a pas encore facturés".
