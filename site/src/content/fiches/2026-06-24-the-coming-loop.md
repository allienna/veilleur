---
title: "The Coming Loop"
date: 2026-06-24
url: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/?utm_source=tldrnewsletter
authors: [lucumr.pocoo.org]
keywords: [agentic engineering, loop, harness, coding agents, automation]
theme: IA
tone: opinion
used_in: ["2026-06-24"]
---

## Résumé

Armin Ronacher observe l'émergence d'une nouvelle manière de travailler avec les agents de code : on ne les prompte plus directement, on écrit des *boucles* (loops) qui les pilotent. Une boucle extérieure à l'agent prend une tâche, la confie au modèle, décide si le résultat est satisfaisant, puis relance, change le contexte ou délègue à une autre machine. L'auteur reconnaît que ce pattern fonctionne magnifiquement pour certains cas (portage de code, exploration de performances, recherche) mais reste sceptique pour le code durable qu'il veut comprendre et maîtriser.

## Points clés

- Citation de Boris Cherny : « Je ne prompte plus Claude. J'ai des boucles qui le promptent et qui décident quoi faire. Mon job, c'est d'écrire des boucles. »
- Il existe deux boucles : la boucle interne de l'agent (appel d'outil, lecture/écriture de fichier, tests) et la boucle externe au niveau du harness, qui maintient la tâche vivante au-delà du « j'ai fini » du modèle.
- Les modèles actuels produisent un code trop défensif, trop complexe, trop local : ils ajoutent des fallbacks au lieu de rendre les mauvais états impossibles. Mis dans une boucle, ce comportement s'amplifie.
- Les boucles fonctionnent très bien quand elles produisent des artefacts sans longévité (proof of concept, traductions mécaniques vérifiables, benchmarks) — un signal « assez utile » suffit pour relancer une itération.
- Métaphore : on passe d'un logiciel vu comme une machine déterministe à un logiciel vu comme un organisme qu'on diagnostique plutôt qu'on comprend.

## Analyse approfondie

> Je ne prompte plus Claude. J'ai des boucles qui le promptent et qui décident quoi faire. Mon job, c'est d'écrire des boucles.
> — Boris Cherny

Au cours des derniers mois, j'ai vu de plus en plus de gens construire, par-dessus les agents de code, quelque chose qui ressemble nettement à autre chose que « simplement utiliser un agent de code ». Une partie de cela se passe au-dessus de Pi, ce qui est sympa à voir. Le pattern est cependant le même partout : le travail est mis dans une sorte de file, une machine le prend, tente quelque chose, s'arrête, puis un *harness* décide si c'était vraiment la fin.

Si ce n'est pas le cas, le harness poursuit la même session, injecte un autre message, démarre une session fraîche avec un contexte modifié, ou envoie la tâche à une autre machine. La tâche reste vivante au-delà du point où le modèle, seul, aurait normalement dit : « J'ai fini. »

Je pense à ce type de boucle plus que je ne voudrais l'admettre.

Il y a déjà une boucle d'agent à l'intérieur de chaque agent de code. Le modèle appelle un outil, intègre le résultat, appelle un autre outil, lit un fichier, édite un fichier, lance des tests, et finit par produire une réponse. Cette boucle nous est familière depuis longtemps. L'autre boucle est celle du harness : la boucle à l'extérieur de la boucle de l'agent. Elle n'est pas nouvelle non plus — on en fait des variantes depuis les débuts de Claude Code — mais elle devient de plus en plus présente dans l'ingénierie agentique, et ces dernières semaines elle a commencé à dominer les discussions sur Twitter.

### Je ne suis pas encore bon à ça

Mon statut actuel : je n'ai pas eu beaucoup de succès avec cette façon de travailler pour le code qui me tient à cœur — et ça représente beaucoup de code.

C'est en partie une question de goût, en partie une question de contrôle. Je vise un standard élevé pour ce à quoi le code doit ressembler, et je veux comprendre le code que je livre. Sous pression, ou dans une discussion avec un humain, je veux pouvoir expliquer ce que fait le système sans devoir d'abord demander à une machine de me l'expliquer. Il y a évidemment une question : ce désir de comprendre le code, l'aurai-je encore dans quelques années ? Pour l'instant, la compréhension reste importante pour moi.

Vu ce désir, il me manque quelque chose dans mon expérience du code écrit sans que j'y prête attention, particulièrement issu de boucles. Les modèles actuels tendent à produire du code trop défensif, trop complexe, dont le raisonnement est trop local. Ils évitent les invariants forts. Ils ajoutent des fallbacks au lieu de rendre les mauvais états impossibles. Ils dupliquent du code, inventent de mauvaises abstractions et masquent un design flou avec plus de machinerie. Pire : je vois pour l'instant très peu de progrès sur ce point. À mon goût, des harnais « mains-libres » comme Claude Code avec ultracode produisent un code pire que ce qu'on produisait l'automne dernier — parce que Claude Code avec Fable travaillera sans interruption sur un problème pendant trente minutes ou plus, là où le processus aurait été bien plus « human in the loop » auparavant.

Par ailleurs, on sait que les modèles observent un échec local et ajoutent une défense locale. Karpathy a mentionné qu'ils sont « mortellement terrifiés par les exceptions ». Dans les systèmes à invariants importants — formats de données persistés, infrastructure critique — le bon correctif n'est pas « gérer chaque cas malformé ». C'est rendre le cas malformé non représentable ou impossible à écrire. Pourtant, même avec beaucoup de pilotage manuel, ce type de code ne sort pas naturellement des LLM.

Quand on met ce comportement derrière des boucles, on l'amplifie. Si chaque itération ajoute une petite défense, le système devient lentement moins compréhensible tout en paraissant plus robuste. Plus on est en retrait, plus cela arrive. Cela enseigne aussi de très mauvaises pratiques aux juniors à qui on donne ces outils sans guidage clair.

### Là où les boucles fonctionnent

En même temps, il serait malhonnête de prétendre que le pattern de la boucle ne fonctionne pas, car il fonctionne déjà étonnamment bien dans certains domaines.

Le portage de code en est un. Il existe déjà des exemples impressionnants de gros efforts de portage automatique, dont le travail rapporté autour du passage de Bun de Zig à Rust. Je l'ai moi-même utilisé avec succès pour porter MiniJinja en Go. Les explorations de performance sont un autre cas où cela fonctionne magnifiquement : une machine peut tenter des expériences, les benchmarker, jeter les échecs, et continuer à chercher. Le scanning de sécurité s'y prête naturellement, tout comme presque tout type de recherche : demander à un système d'explorer un espace de problème complexe et de rapporter sans nécessairement produire du code durable.

Un point commun à beaucoup de ces cas : soit ils ne génèrent pas de nouveau code mais transforment du code existant, soit ils produisent du code qui n'a délibérément pas une longue durée de vie. Je crois que les boucles produisant des artefacts sans besoin de longévité, ou créant une traduction mécanique clairement vérifiable, comptent davantage que la capacité générale d'un harness à mesurer mécaniquement un objectif. Beaucoup d'applications réussies de boucles utilisent un autre LLM comme juge ou comme orchestrateur. Le harness a juste besoin d'un signal qui lui permet de continuer ; il n'a pas à être objectif ou binaire, juste assez utile pour piloter une autre itération.

J'adore déjà les boucles qui retirent les parties ennuyeuses de ma journée — expérimenter, mesurer, me donner des idées.

### Le logiciel comme organisme

En revanche, utiliser cette même méthodologie de boucle pour écrire du code durable ne me convient pas encore. La métaphore que j'aime : on passe du logiciel comme machine déterministe au logiciel comme organisme.

Je suis devenu ingénieur dans un environnement qui m'encourageait à comprendre la machine. Il y avait toujours une couche qu'on pouvait éplucher pour approfondir sa compréhension. Côté architecture, je voyais comme désirable de pousser vers plus de déterminisme, pas moins. La capacité à comprendre le code a toujours été un objectif indéniable. Sur les systèmes bien conçus, il y avait toujours des ingénieurs qui savaient où vivaient les invariants, quelles parties étaient porteuses et quels changements étaient sûrs.

Cet idéal a toujours été mis à mal : de nombreux systèmes, surtout les plus gros, sont trop grands, trop dynamiques, trop dépendants de services externes pour tenir dans une seule tête. Même sans LLM, on diagnostique déjà les systèmes distribués un peu comme des médecins : on observe les symptômes, on forme des hypothèses, on « demande plus d'analyses », on essaie des remèdes, et on observe à nouveau.

Avec les LLM, on pousse bien plus loin dans cette direction et bien plus vite. On les utilise pour écrire le code, mais aussi pour le diagnostic et le remède. Beaucoup d'ingénieurs vivent déjà dans un monde où la première étape après un incident en production consiste à faire lire les logs par une machine, lui faire proposer des causes racines et poser proactivement un patch — patch souvent repris par une autre machine qui le relit, et parfois le merge sur main sans aucune supervision humaine.

C'est évidemment puissant, et je ne peux nier que cela paraît séduisant. Mais céder à cette idée, surtout avec moins de compréhension, a un coût qui ne se voit pas tout de suite.

## Pourquoi ça compte

C'est le texte qui nomme et théorise le basculement de 2026 : du prompt vers la boucle. Il pose la bonne tension — productivité réelle des loops vs. perte de compréhension et de contrôle du code durable — qui structure tout le débat de l'ingénierie agentique actuelle.
