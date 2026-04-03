---
title: "The 2nd Phase of Agentic Development"
date: 2026-04-03
url: "https://www.dbreunig.com/2026/04/01/the-2nd-phase-of-agentic-development.html"
authors: ["Drew Breunig"]
keywords: [développement agentique, spec-driven development, open source, réimagination, clones]
theme: "IA"
tone: opinion
used_in: ["2026-04-03"]
---

## Résumé

Drew Breunig observe que le développement agentique est en train de passer à une deuxième phase. La première vague a produit des clones et des portages — recréer des logiciels existants dans un autre langage en s'appuyant sur des suites de tests existantes comme spécifications. La deuxième vague produit des "réimaginations" — des projets qui repensent des concepts fondamentaux plutôt que de simplement copier. Ce glissement est rendu possible par l'émergence du "spec-driven development", où tests et spécifications guident l'agent plutôt que le codage humain étape par étape.

## Points clés

- La première phase agentique s'est concentrée sur les clones et les portages de logiciels existants
- Les suites de tests existantes fonctionnaient comme des spécifications naturelles pour guider les agents
- La deuxième phase produit des réimaginations : des projets qui rethinkent les fondamentaux plutôt que de copier
- Le "spec-driven development" devient le mode de travail naturel avec les agents
- Les "tokenmaxxers" reconstruisent activement des dépendances en Rust ou Go pour réduire les tokens consommés
- Ce changement de phase révèle ce que les agents font réellement bien : exécuter des spécifications précises, pas improviser

## Analyse approfondie

### La première vague : l'ère des clones et des portages

Drew Breunig commence par caractériser la première phase du développement agentique, celle qui a dominé 2025 et le début de 2026. Cette phase était marquée par des projets de clonage et de portage : prendre un logiciel existant et le recréer, soit dans le même langage avec une architecture différente, soit dans un autre langage avec les mêmes fonctionnalités.

Les exemples sont frappants par leur ambition. Anthropic a écrit un compilateur C en Rust en utilisant les suites de tests du compilateur original comme spécification. Vercel a recréé bash en TypeScript. Pydantic a construit un émulateur Python en Python. Dans chaque cas, la logique est la même : le logiciel source est assez bien documenté par ses tests pour qu'un agent puisse en produire une implémentation fonctionnelle sans qu'un humain n'écrive une seule ligne de logique métier.

Ces projets ont démontré quelque chose d'important : les agents de codage ne sont pas seulement capables de générer du code trivial ou boilerplate. Ils peuvent, dans les bonnes conditions, produire des systèmes complexes et corrects. Mais la condition clé est "dans les bonnes conditions" — et ces conditions, c'est précisément l'existence d'une spécification riche et vérifiable.

### Le rôle des suites de tests comme spécifications naturelles

Ce qui rend possible cette première vague, c'est une insight simple mais puissante : une suite de tests complète est une spécification. Elle décrit, de façon précise et vérifiable, ce que le logiciel doit faire dans des centaines voire des milliers de situations. Un agent peut utiliser cette suite comme une boussole : générer du code, lancer les tests, observer les échecs, corriger, recommencer, jusqu'à ce que tous les tests passent.

Cette boucle — générer, tester, corriger — est exactement la boucle ReAct dans son application la plus naturelle. Et les tests lui donnent quelque chose que les prompts seuls ne peuvent pas donner : une vérité objective. Soit le test passe, soit il échoue. Il n'y a pas d'ambiguïté, pas besoin d'interprétation humaine à chaque étape.

La conséquence est que les projets les mieux dotés en tests sont devenus les premiers candidats au portage agentique. Les langages et frameworks avec des écosystèmes de test matures — C, Python, les outils Unix classiques — ont été les premiers à être recréés.

### La deuxième vague : l'ère des réimaginations

Mais quelque chose a changé récemment. Drew Breunig observe cette semaine deux projets qui illustrent un glissement qualitatif : au lieu de cloner ce qui existe, ils réimaginent des concepts fondamentaux. Ils ne posent pas la question "comment refaire X dans un autre langage ?" mais "si on recommençait X de zéro aujourd'hui, avec toutes les connaissances accumulées depuis sa création initiale, comment le ferait-on ?"

Cette distinction est plus profonde qu'elle n'y paraît. Cloner requiert de comprendre l'existant. Réimaginer requiert de comprendre pourquoi l'existant a les limites qu'il a, ce qu'on voulait vraiment accomplir, et comment on pourrait s'en approcher mieux. C'est un niveau d'abstraction supérieur.

Les réimaginations ne peuvent pas s'appuyer sur des suites de tests existantes — puisque le logiciel qu'elles ciblent n'existe pas encore. Elles nécessitent des spécifications construites explicitement, réfléchies à l'avance, et souvent itérées avec l'agent lui-même. C'est là qu'intervient le "spec-driven development" comme pratique délibérée.

### Le spec-driven development comme pratique émergente

Le "spec-driven development" n'est pas un concept nouveau — l'idée que les spécifications devraient précéder l'implémentation est aussi vieille que le génie logiciel. Mais dans la pratique, elle a toujours été difficile à maintenir parce que les spécifications ont tendance à devenir obsolètes dès que le code commence à évoluer.

Avec les agents, cette pratique devient non seulement viable mais nécessaire. Un agent sans spécification claire est un agent qui improvise — et l'improvisation agentique, c'est précisément ce qui produit du code plausible mais incorrectement aligné sur les besoins réels. Inversement, un agent avec une spécification précise, complète et vérifiable peut produire des résultats remarquables.

Le changement de phase que décrit Breunig, c'est donc aussi l'émergence d'une nouvelle compétence humaine : savoir écrire des spécifications suffisamment précises pour guider un agent. Cette compétence ressemble à la fois au design logiciel traditionnel et à quelque chose de nouveau — une façon de penser en termes de contraintes, de cas limites, de critères de validation, plutôt qu'en termes d'implémentation.

### Les tokenmaxxers : une communauté de pratique émergente

Breunig mentionne un phénomène parallèle et révélateur : les "tokenmaxxers". Ce terme désigne des développeurs qui reconstruisent activement leurs dépendances dans des langages plus économes en tokens — principalement Rust et Go — pour réduire la quantité de contexte que leurs agents consomment à chaque session.

C'est un comportement d'optimisation qui n'aurait aucun sens dans un paradigme de développement traditionnel. Personne ne réécriture ses dépendances en Rust juste pour économiser quelques kilooctets de code source. Mais dans un paradigme agentique, où la fenêtre de contexte est une ressource rare et précieuse, cette optimisation devient rationnelle.

Ce phénomène illustre à quel point le développement agentique crée de nouvelles contraintes et de nouveaux comportements d'optimisation qui n'existaient pas auparavant. Les tokenmaxxers sont les pionniers d'une ingénierie de la contrainte contextuelle qui deviendra probablement une compétence courante dans les équipes qui adoptent massivement les agents.

### Ce que la deuxième phase révèle sur les agents

En conclusion, Breunig note que la transition vers la deuxième phase révèle quelque chose d'important sur la nature des agents de codage : ils sont fondamentalement des exécuteurs de spécifications, pas des improvisateurs créatifs. Là où la première phase a exploité des spécifications déjà existantes (les tests), la deuxième phase nécessite de les construire délibérément.

Cela ne diminue pas la valeur des agents — être un excellent exécuteur de spécifications est extraordinairement précieux. Mais cela définit clairement où la valeur humaine reste irremplaçable : dans la capacité à imaginer ce que l'on veut construire, à le spécifier avec assez de précision pour qu'un agent puisse l'exécuter, et à évaluer si le résultat correspond à l'intention initiale.

## Pourquoi ça compte

Cette analyse offre une grille de lecture pour comprendre où en est le développement agentique et où il va, en distinguant ce qui est derrière nous (les clones) de ce qui émerge (les réimaginations), et en posant le spec-driven development comme la compétence clé de la prochaine phase.
