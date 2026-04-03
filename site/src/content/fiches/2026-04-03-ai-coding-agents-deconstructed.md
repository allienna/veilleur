---
title: "AI Coding Agents, Deconstructed"
date: 2026-04-03
url: "https://blog.apiad.net/p/the-anatomy-of-ai-coding-agents"
authors: ["Alejandro Piad-Morffis"]
keywords: [agents de codage, architecture agentique, fenêtre de contexte, ReAct loop, harness engineering]
theme: "IA"
tone: opinion
used_in: ["2026-04-03"]
---

## Résumé

Alejandro Piad-Morffis soutient que les échecs des agents de codage IA sont des défaillances systémiques, pas des défaillances de modèle. Tout se passe à l'intérieur d'une fenêtre de contexte qui grandit à chaque cycle de la boucle ReAct, créant une tension fondamentale entre puissance et finitude. L'article propose un cadre à quatre éléments — Constitution, Spécifications, Plans, Tâches — et plaide pour une discipline du "harness engineering" : concevoir les systèmes qui guident les agents plutôt que de simplement rédiger des prompts.

## Points clés

- Les échecs des agents ne viennent pas du modèle sous-jacent mais du système qui l'entoure
- La fenêtre de contexte est à la fois la source de puissance de l'agent et sa principale contrainte
- La boucle ReAct (penser, agir, observer, répéter) gonfle le contexte à chaque itération
- Le cadre en quatre éléments — Constitution, Spécifications, Plans, Tâches — permet de contraindre l'agent différemment à chaque niveau
- Le "harness engineering" est une discipline émergente : concevoir les systèmes de guidage des agents
- Trois domaines d'application sont identifiés, chacun avec des exigences différentes en matière de contexte et d'autonomie

## Analyse approfondie

### Le diagnostic central : ce ne sont pas des problèmes de modèle

Alejandro Piad-Morffis ouvre avec une affirmation provocatrice : la plupart des gens qui se plaignent de leurs agents de codage IA se trompent de cible. Ils blâment le modèle — "GPT-4 n'est pas assez bon", "Claude ne comprend pas mon codebase" — alors que le problème est systémique. Améliorer le modèle sous-jacent ne résoudra pas le problème si le système qui l'entoure est mal conçu.

Cette distinction est capitale parce qu'elle déplace la responsabilité et l'effort. Si le problème est le modèle, on attend la prochaine version. Si le problème est le système, on peut agir maintenant, avec les modèles existants.

### Tout se passe dans la fenêtre de contexte

Pour comprendre pourquoi les systèmes échouent, il faut comprendre la contrainte fondamentale : tout ce qu'un agent fait, il le fait à l'intérieur de sa fenêtre de contexte. Instructions, historique de conversation, contenu des fichiers lus, résultats des outils exécutés, erreurs rencontrées — tout cela s'accumule dans une fenêtre de taille finie.

La fenêtre de contexte est simultanément la source de puissance de l'agent et sa principale limite. Plus il y a d'information dans le contexte, plus l'agent peut prendre de décisions éclairées. Mais plus le contexte grossit, plus les inférences deviennent coûteuses, lentes, et éventuellement dégradées — les modèles ont du mal à maintenir une cohérence parfaite sur de très longs contextes.

### La boucle ReAct et l'inflation du contexte

Les agents de codage fonctionnent typiquement selon la boucle ReAct (Reasoning + Acting) : penser à l'étape suivante, exécuter une action (lire un fichier, lancer un test, écrire du code), observer le résultat, puis recommencer. À chaque cycle de cette boucle, le contexte grossit : les observations s'ajoutent, les résultats intermédiaires s'accumulent, les erreurs et leurs corrections s'empilent.

Pour une tâche simple avec peu d'itérations, ce n'est pas un problème. Mais pour une tâche complexe — refactorer un module entier, ajouter une fonctionnalité qui touche à plusieurs parties du système, déboguer un problème intermittent — le nombre de cycles peut devenir très élevé, et le contexte peut atteindre ses limites avant que la tâche soit terminée.

C'est là que les agents échouent de façon caractéristique : ils "oublient" des instructions données au début, répètent des erreurs déjà corrigées, ou perdent le fil de l'objectif global en se concentrant trop sur les détails immédiats.

### La tension fondamentale : puissance vs finitude

L'article nomme explicitement la tension centrale de l'architecture agentique : le contexte est puissance, mais le contexte est fini. Il n'y a pas de solution miracle à cette tension — les fenêtres de contexte grandissent avec chaque nouvelle génération de modèles, mais les tâches que les développeurs veulent confier aux agents grandissent en proportion.

La conséquence pratique est que le design du système doit activement gérer ce que l'agent voit dans son contexte. Donner trop d'information dès le départ est aussi problématique que d'en donner trop peu. Le timing de l'information — quand la fournir, dans quel format, avec quelle priorité — devient une variable de conception à part entière.

### Le cadre à quatre éléments

Pour structurer ces choix de conception, l'article propose un cadre à quatre niveaux, chacun contraignant l'agent différemment :

**Constitution** — Les valeurs et principes fondamentaux qui guident l'agent en toutes circonstances. C'est le niveau le plus stable : il ne change pas d'une tâche à l'autre. On y définit ce que l'agent doit toujours faire (écrire des tests, documenter les décisions) et ne jamais faire (modifier les fichiers de configuration de production, supprimer des données sans confirmation).

**Spécifications** — Ce que l'on veut construire. Ce niveau décrit le domaine métier, les exigences fonctionnelles, les contraintes non-fonctionnelles. Une bonne spécification donne à l'agent suffisamment de contexte pour comprendre l'intention derrière chaque décision technique, pas seulement la mécanique.

**Plans** — Comment le construire. Ce niveau traduit les spécifications en séquence d'étapes techniques. Un bon plan découpe la tâche en unités assez petites pour tenir confortablement dans le contexte d'une session, tout en restant assez cohérentes pour que l'agent puisse les exécuter sans perdre le fil.

**Tâches** — Les unités atomiques de travail. Ce sont les actions individuelles que l'agent exécute à chaque cycle de la boucle ReAct : lire un fichier, écrire une fonction, lancer les tests. Une bonne décomposition en tâches minimise les risques de dépendances circulaires et d'accumulation de contexte inutile.

### Les trois domaines d'application

L'article identifie trois domaines dans lesquels les agents de codage s'appliquent, avec des exigences très différentes :

Le premier domaine est la **génération de code à partir de zéro** — créer un nouveau module, une nouvelle API, un nouveau composant. C'est là que les agents brillent le plus, parce que le contexte de départ est minimal et que l'espace de décision est relativement bien contraint par les spécifications.

Le deuxième domaine est la **modification de code existant** — refactoring, ajout de fonctionnalités, correction de bugs. C'est plus difficile parce que l'agent doit comprendre un contexte existant avant d'agir, ce qui consomme du contexte disponible et augmente le risque d'erreurs.

Le troisième domaine est la **navigation et la compréhension de codebase** — répondre à des questions sur le code, identifier des dépendances, tracer des flux d'exécution. C'est un domaine souvent négligé, mais potentiellement très utile pour les développeurs qui rejoignent un projet complexe.

### Le harness engineering : une discipline émergente

La conclusion de l'article est un appel à reconnaître le "harness engineering" comme une discipline à part entière. Le "harness" (harnais) désigne l'ensemble du système qui entoure l'agent : les prompts système, les outils disponibles, la façon dont les informations sont injectées dans le contexte, les mécanismes de validation des résultats, les boucles de feedback.

Jusqu'à présent, la plupart des équipes traitent ce harnais comme secondaire — on passe du temps à choisir le bon modèle, à optimiser les prompts individuels, mais peu à concevoir l'architecture globale du système agentique. L'article argumente que c'est précisément là que se joue la différence entre un agent qui déçoit et un agent qui transforme la productivité d'une équipe.

Le harness engineering, c'est l'ingénierie des systèmes qui guident les agents. Ce n'est pas du prompt engineering — c'est de l'architecture logicielle appliquée aux systèmes d'IA.

## Pourquoi ça compte

Cet article fournit un vocabulaire et un cadre conceptuel pour diagnostiquer et améliorer les déploiements d'agents de codage, à un moment où beaucoup d'équipes expérimentent sans méthode et attribuent leurs échecs aux mauvaises causes.
