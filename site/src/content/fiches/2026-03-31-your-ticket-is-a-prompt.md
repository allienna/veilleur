---
title: "Your ticket is a prompt"
date: 2026-03-31
url: https://dheer.co/tickets-are-prompts/
authors: [Dheer Gupta]
keywords: [AI agents, tickets, fragmentation, product management, outcome-driven]
theme: IA
tone: opinion
used_in: ["2026-03-31"]
---

## Résumé

Dheer Gupta observe que les tickets de développement, conçus pour des humains, deviennent de facto des prompts lorsque des agents IA les exécutent — et que leur périmètre étroit produit un travail tout aussi étroit. En expérimentant avec des équipes d'agents, il constate que ceux-ci reproduisent fidèlement les biais de fragmentation qui minent les équipes produit depuis des décennies : création de sous-tickets, correctifs atomiques et perte de vue de l'objectif initial. Sa recommandation : confier aux agents des initiatives orientées résultat plutôt que des issues techniques découpées à l'avance.

## Points clés

- Les mots inscrits sur un ticket définissent le périmètre de raisonnement d'un agent IA — un fragment de ticket produit un fragment de travail
- Sans supervision stricte, les agents créent spontanément de nouveaux tickets à périmètre étroit, reproduisant le cycle de fragmentation des équipes humaines
- Les bugs introduits par un agent suivant un ticket trop restreint génèrent leurs propres tickets, créant une cascade de correctifs atomiques qui ne résolvent rien globalement
- La fragmentation existait déjà dans les équipes humaines, mais était compensée par les conversations informelles et la connaissance tacite — les agents n'ont pas ces mécanismes
- La recommandation clé : assigner aux agents la plus grande unité de travail justifiable, orientée résultat, et les laisser décomposer eux-mêmes les sous-tâches au moment de la revue

## Analyse approfondie

Beaucoup de gens à qui l'auteur parle ne réalisent pas que leurs tickets sont désormais des prompts, et que si l'on continue à les utiliser comme avant l'IA, ils vont empoisonner le contexte. Les mots inscrits sur le ticket déterminent ce qu'un agent considère comme relevant de son périmètre et contraignent son raisonnement. Un fragment produit un travail en forme de fragment.

La semaine précédente, l'auteur a volontairement renoncé à imposer des workflows stricts à son équipe d'agents pour une tâche relativement simple. Ils ont immédiatement cédé à leur instinct naturel : repousser le travail vers d'autres tickets. Un agent a rédigé une issue : une description du symptôme, une liste des fichiers concernés, un correctif proposé limité au changement le plus étroit possible. Propre, professionnel, le genre de ticket que l'auteur a lu des milliers de fois dans JIRA. L'équipe d'agents suivante a pris le relais, a suivi le chemin biaisé que le ticket avait tracé, et a introduit deux nouveaux bugs parce que le périmètre étroit excluait du contexte important. Ces bugs ont engendré leurs propres tickets. Trois itérations plus tard, le résultat initial était enterré sous des correctifs atomiques qui, collectivement, ne résolvaient rien. L'auteur a répété l'expérience. Même comportement à chaque fois.

Les agents se comportent comme les tickets dont ils se sont nourris. Le rétrécissement du périmètre, la déférence envers les petites pièces plutôt que les résultats globaux, l'instinct de fragmenter avant de réfléchir. Ce ne sont pas des problèmes d'agents. Ce sont les mêmes schémas comportementaux qui minent les équipes produit depuis des décennies, le même problème de personnalité humaine reproduit fidèlement par chaque modèle entraîné sur ces données. Chaque pattern de ticket dans le backlog a formé une génération d'ingénieurs. Désormais, il forme une génération d'agents. Leur travail enfle de la même manière que les délais produit enflent dans les équipes humaines, sauf que maintenant le cycle se boucle en minutes plutôt qu'en sprints.

La recommandation de l'auteur : assigner aux agents la plus grande unité de travail justifiable. Un résultat produit ou une fonctionnalité peut se résumer en deux lignes. C'est ce qui doit figurer sur le ticket. Il faut laisser les agents déterminer les sous-tâches au moment où le travail est prêt pour la revue, pas avant. Dès qu'on découpe une initiative en issues techniques en amont, le résultat se perd et l'attention se déplace vers les détails. Si une initiative est véritablement trop volumineuse, il faut la découper en initiatives plus petites, pas en issues plus petites. Elles doivent rester orientées résultat : quelque chose qui donne à l'agent de l'espace pour raisonner, pas une issue technique qu'il suit aveuglément.

La maladie de la fragmentation a toujours été là. On ne pouvait pas la voir clairement quand les humains captaient le contexte dans les conversations de couloir et comblaient les lacunes grâce à leur connaissance tacite. Les agents n'ont pas de couloirs. Ils ont les mots inscrits sur le ticket, et rien d'autre.

## Pourquoi ça compte

Cet article met en lumière un angle mort critique de l'adoption des agents IA dans les workflows d'ingénierie : les pratiques de découpage du travail héritées de l'ère humaine deviennent activement nuisibles quand elles servent de prompts à des agents sans contexte implicite. C'est un signal d'alarme pour les engineering managers qui déploient des agents sans repenser fondamentalement la granularité et la nature de leurs tickets.
