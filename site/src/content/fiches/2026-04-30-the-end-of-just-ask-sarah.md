---
title: "The end of \"Just ask Sarah\""
date: 2026-04-30
url: https://simme.dev/posts/the-end-of-just-ask-sarah/
authors: [Simon Aronsson]
keywords: [documentation, agents, organizational-memory, adr, leadership]
theme: Leadership
tone: opinion
used_in: ["2026-04-30"]
---

## Résumé

Toute organisation a sa Sarah — l'ingénieure qui sait pourquoi un service a été splitté ainsi, pourquoi telle abstraction existe, pourquoi le fix évident a été refusé il y a trois trimestres. Les humains peuvent demander à Sarah. Les agents IA, non. Simon Aronsson défend que la documentation, qui était jusqu'ici une politesse pour les futurs humains, devient le moyen principal de garantir un contexte historique durable et disponible — et que les organisations qui ne l'écrivent pas vont voir leurs agents amplifier leurs dettes décisionnelles à grande vitesse.

## Points clés

- Toute organisation a sa Sarah, dépositaire informelle de la mémoire des décisions techniques et produit.
- Les humains peuvent demander à Sarah. Les agents non, ils ne peuvent que lire ce qui est écrit.
- L'absence d'ADR ou de spec n'empêche pas la décision : elle l'empêche d'être propagée.
- Un agent qui ne trouve pas le contexte étend simplement le pattern dominant — c'est par design, pas par bug.
- Le coût de la non-documentation se concentrait sur l'onboarding humain ; il se distribue désormais sur chaque tâche agentique.

## Analyse approfondie

Toute organisation d'ingénierie a sa Sarah. Les humains peuvent lui demander — les agents, non.

Sarah, c'est la personne qui sait pourquoi un service a été splitté, pourquoi une abstraction existe, pourquoi une contrainte étrange a façonné le design actuel, et pourquoi le fix évident a été rejeté il y a trois trimestres.

Cela change radicalement l'importance de la documentation. La doc n'est plus une politesse pour les futurs humains. Elle devient notre moyen principal d'assurer un contexte historique durable et disponible. De la même manière que "le code ennuyeux est un signal organisationnel", l'absence de documentation révèle des priorités, et les agents les amplifieront plus vite que jamais.

Imagine un agent qui ouvre une nouvelle tâche. Il commence à parcourir la base de code pour trouver des patterns qui l'aideront à décider de ce qu'il doit faire. Il cherche dans la documentation un ADR expliquant pourquoi le service est structuré de cette façon. Mais il n'y en a aucun, et aucune spec ne décrit l'intention.

L'agent va faire ce pour quoi il a été conçu : trouver le pattern dominant et l'étendre. Ce n'est pas que l'agent soit buggé ou trop optimiste, c'est que le contexte non-persisté ne se propage pas.

Une décision **a bien été** prise — le code est là, après tout. Elle n'a juste pas été écrite. Donc l'agent hérite du résultat sans le raisonnement, et comble les blancs du mieux qu'il peut.

### Les humains portent l'état

La mémoire organisationnelle a toujours été une structure sociale autant que technique. Elle vit avec l'ingénieur qui est dans l'équipe depuis sept ans. Elle est ancrée dans la phrase "demande à Sarah", ou dans le contexte transmis lors des one-on-ones et accumulé au fil des standups. L'écrit est devenu un backup. Il était toujours censé être là, mais rarement maintenu jusqu'au point où on pouvait s'y fier.

Quand le système fonctionne, on n'en voit pas le coût. Quand quelqu'un part, on découvre quelles parties de la mémoire dépendaient d'elle. Sarah part en sabbatique trois mois et soudain, l'équipe redécouvre des sujets qu'elle pensait clos. C'est inconfortable, mais on s'adapte parce que les autres humains restent et finissent par reconstruire la connaissance par discussion, par lecture rétrospective, par cassage de quelques choses et réparation.

### Les agents n'ont pas de Sarah

Les agents ne peuvent pas reconstruire ce contexte ainsi. Ils ne peuvent pas tirer un café avec un staff engineer. Ils ne peuvent pas lire le ton d'une remarque dans un standup. Ils ne peuvent pas demander "tiens, c'est bizarre cette structure, pourquoi ?". Ils peuvent uniquement lire ce qui est écrit, et ce qu'ils lisent devient leur monde.

Quand on multiplie les agents qui contribuent au code, le coût des décisions non écrites se met à composer. Chaque agent qui ouvre une tâche refait le même chemin : il cherche, il devine, il étend. Et chaque extension qui n'aurait pas été prise par un humain qui connaît l'histoire devient une nouvelle dette.

### L'intention doit être durable

L'auteur défend que la solution n'est pas d'écrire plus de doc, mais d'écrire l'intention. Les ADR (Architecture Decision Records), les RFC internes, les specs courtes, les commentaires "pourquoi" — pas "comment" — dans le code, deviennent des artefacts de premier rang. Ils sont la version persistée de la conversation qui a eu lieu, et ils sont la seule façon pour un agent de prendre la même décision plus tard.

Concrètement, Aronsson recommande de :
- Écrire un ADR à chaque fois qu'on prend une décision dont on devra justifier la trace dans six mois.
- Garder ces ADR dans le repo, pas dans un Notion ou un Confluence séparé, pour qu'un agent qui clone le repo les lise au passage.
- Documenter les non-décisions aussi : "On a envisagé X, on ne l'a pas fait parce que Y" est presque plus précieux que la décision elle-même.

### La décision non-écrite reste une décision

Le titre de la section est l'argument central : qu'on l'écrive ou pas, la décision a été prise. La question n'est pas "est-ce qu'on documente ?" mais "est-ce qu'on accepte de payer le coût de la non-documentation à chaque future tâche, humaine ou agentique ?".

### Concentration du coût

Avant les agents, le coût se concentrait sur l'onboarding humain : un nouveau dev mettait six mois à comprendre l'histoire, et c'était un coût qu'on absorbait. Avec les agents, le coût se distribue sur chaque tâche. Chaque PR ouverte par un agent qui n'a pas trouvé le contexte ré-introduit potentiellement la dette qu'on pensait avoir réglée.

C'est ce qui rend la doc-as-context si critique : ce n'est plus un investissement long terme à amortir, c'est un input opérationnel quotidien.

## Pourquoi ça compte

Pour un leader tech, le message est clair : si tu déploies des agents dans ton org, ta documentation devient interface de production. Investir dans l'écriture des ADR, des specs et des "pourquoi" n'est plus un nice-to-have — c'est ce qui détermine la qualité des décisions que tes agents prendront pour toi demain.
