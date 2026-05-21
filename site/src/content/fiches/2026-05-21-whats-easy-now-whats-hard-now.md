---
title: "What's Easy Now? What's Hard Now?"
date: 2026-05-21
url: https://brooker.co.za/blog/2026/05/18/whats-easy-whats-hard.html
authors: [Marc Brooker, brooker.co.za]
keywords: [coding agents, feedback loops, specification, formal methods, software engineering]
theme: IA
tone: opinion
used_in: ["2026-05-21"]
---

## Résumé

Marc Brooker propose une grille de lecture contre-intuitive pour comprendre les capacités à long terme des agents de code : les agents ne sont que des boucles de feedback. Son hypothèse — la « feedback loop hypothesis » — affirme que les agents trouveront faciles les tâches dotées d'un feedback efficace et difficiles celles qui en sont privées. Conséquence dérangeante : le SaaS et les UIs, qui semblent « faciles », deviendront « difficiles » (feedback humain lent et inconsistant), tandis que le logiciel système, réputé « difficile », deviendra « facile » (spécifications claires, vérifiables sans humain). Cela élève la valeur de la spécification et des outils qui l'appliquent au code.

## Points clés

- Les agents de code deviennent excellents et très peu coûteux ; super-humains sur certaines tâches, en retrait sur d'autres.
- « Feedback is uniquely powerful » : un composant imparfait dans une boucle de feedback peut produire d'excellents résultats.
- Les agents IA sont des boucles de feedback : la bascule autocomplétion → agent, c'est déplacer le feedback du dev vers l'agent.
- Feedback loop hypothesis : feedback efficace = tâche « facile » à long terme ; absence de feedback = tâche « difficile ».
- Contre-intuition : le SaaS/UI devient « difficile » (humain dans la boucle), le logiciel système « facile » (spec claire, propriétés testables).
- Ce qui monte en valeur : la spécification et les outils qui l'appliquent (Rust, TLA+, P, property-based testing, Verus, Hydro, simulateurs).

## Analyse approfondie

*Quatrième billet d'une série sur la façon dont l'IA change le développement logiciel.*

J'ai passé beaucoup de temps à réfléchir à la forme des capacités des agents de code. Ce qu'ils savent bien faire, ce qu'ils sauront faire ; ce qu'ils font mal, et dans quelle mesure c'est inhérent ou transitoire. C'est important, parce que c'est la question la plus déterminante pour l'avenir du logiciel et de l'ingénierie logicielle. Je ne prétends pas avoir la réponse, mais j'arrive à une conclusion qui peut être profondément contre-intuitive.

Les agents de code deviennent vraiment très bons, et peuvent construire des logiciels significatifs et corrects très vite, à un coût transformativement bas. Ils ont des capacités super-humaines sur certaines tâches de code. Bien sûr, les systèmes informatiques ont des capacités super-humaines depuis au moins 85 ans. Je pense qu'on va découvrir, comme au cours de ces neuf décennies, que cette nouvelle technologie est largement super-humaine dans certains domaines, et bien moins capable que les humains dans d'autres. La question importante est : comment, et pourquoi ?

**Le feedback est puissant.** Au début de mes études d'ingénieur électricien, un professeur a dessiné au tableau un circuit simple resté gravé dans ma mémoire : on applique une tension à gauche, et à droite on obtient sa racine carrée. Les deux composants sont un ampli opérationnel et un multiplicateur analogique. Ce circuit encapsule peut-être l'idée la plus importante de l'électronique : *le feedback est uniquement puissant.* Peut-être déraisonnablement puissant. C'est l'idée qui fait fonctionner presque tout appareil électronique, qui maintient les avions en l'air et empêche votre four de brûler le dîner. Des composants placés à l'intérieur de boucles de feedback peuvent se comporter très différemment de leur comportement « open loop ». D'excellentes sorties peuvent être extraites de composants médiocres. Un multiplieur peut devenir un extracteur de racine carrée. Le feedback change tout.

Les agents IA ne sont rien d'autre que des boucles de feedback. Ils sont construits autour d'un composant au comportement open loop utile mais imparfait (un LLM), et utilisent le feedback pour rendre ce composant capable de choses qu'il ne sait pas faire sans. C'est l'idée de fond de la transformation de l'outillage de dev des deux dernières années : le passage de l'IA open loop (l'autocomplétion intelligente dans les IDEs) aux agents — déplacer le feedback du développeur humain (build, test, retour à l'IDE) dans l'agent lui-même (build, test, itère).

Une grande partie de la discussion sur les capacités à long terme porte sur le comportement open loop des modèles. Mais ce n'est que la moitié du tableau. Je dirais même que c'est la moitié la moins importante. Le feedback est ce qui va piloter les capacités à long terme.

**L'hypothèse de la boucle de feedback.** *À long terme, les agents de code trouveront « faciles » les tâches dotées d'un feedback efficace, et « difficiles » celles dépourvues de feedback efficace. La disponibilité d'un feedback précis déterminera les limites de leurs capacités.*

D'un côté, ce devrait être non-controversé. Quiconque a construit du code avec des agents sait que de bons messages d'erreur les gardent débloqués. On voit des outils comme Rust guider les agents vers du code correct en fournissant un feedback explicite et immédiat. On voit les agents excellents sur le travail de performance, là où existent de bons benchmarks. On voit le property-based testing être uniquement précieux. On voit aussi que les agents ne sont pas très bons en *architecture* (où le feedback est du type « je le reconnais quand je le vois ») ni en programmes concurrents (où le feedback est du type « ça a silencieusement corrompu les données à l'exécution »).

Mais regardons un peu plus loin, et comparons deux problèmes : construire un site web d'édition de photos ergonomique et délicieux ; construire un moteur de stockage de base de données correct et performant. Pour des modèles open loop, le premier est plus facile que le second. La feedback loop hypothesis, elle, me fait penser que le second est en réalité le problème le plus facile à long terme. Pourquoi ? Considérez leurs boucles de feedback. Celle du site web, au-delà de quelques tests automatisés, requiert un humain dans la boucle : il doit être agréable à utiliser pour des humains — notoirement lents, mous et inconsistants comme fournisseurs de feedback. Le moteur de base de données, lui, a une spécification plutôt simple : API, propriétés de sûreté, propriétés de vivacité. Avec les bons outils dans la boucle, l'itération vers le succès ne requiert aucun humain.

**Qu'est-ce que ça veut dire ?** C'est différent de l'intuition de beaucoup de gens. Ils voient les sites et UIs comme « faciles » (cf. la SaaSpocalypse) et le logiciel système comme « difficile ». La feedback loop hypothesis dit que c'est l'inverse : on va découvrir que le SaaS est « difficile » et le logiciel système « facile ». Cela va élever l'importance de la spécification (l'écriture de ce à quoi « bien » ressemble pour piloter la boucle) et des outils qui appliquent cette spécification au code : outils au compile-time comme Rust, Hydro, Verus ; outils de modélisation comme TLA+ et P ; outils de spécification comme l'analyseur de specs de Kiro ; outils de test, simulateurs, mocks. Le futur du développement logiciel, c'est construire ces boucles de feedback. Beaucoup de problèmes difficiles demeurent.

## Pourquoi ça compte

Une grille mentale puissante pour anticiper où les agents seront forts ou faibles : ce n'est pas la difficulté apparente d'une tâche qui compte, mais la qualité du feedback disponible. De quoi réorienter l'investissement vers la spécification et l'outillage de vérification.
