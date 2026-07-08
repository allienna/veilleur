---
title: "The slow death of the hands-on engineering manager"
date: 2026-07-07
url: https://elinkc09.newsletter.manager.dev/ss/c/u001.RTyWcqXASoNN_N7VZ16WVQ0bWW7G7dilLQBC1zpVXB_2BeXSAhs5hpBWZ_Lg7E9fhtmv_ce4Ob5epUdoe5b6Hof_RHN-p9sYEcYiUSV1fL5AfJD9I4zRqGFiUs7c0m6Bvvo3CA_NFm7GD46lifytKrtRVaTJa_lPnkxftzt9Oa-_xWWxUkXra3_Anj-r7u3HjXEUlCjLH5K_rtHHJ6TACY_v211XgXDVPsqWPvzfndKV89lA1FxBXmcKT80xeyQjJqpdd44mEZUeB6knapNCvjxBfG7cpuTkK8Z4u2sO2Ee_rC9m0dDtL-fCVCiG4hboGgzAK2u47oye8qPqRVmbJbV-X7ErgGB8s-yR6tHG-C2Edpl-uzw4P5auGRC2gMgi_Rv9axFuTS9u2gvsRvxdLbYGNXOlcoQUIO3QGYTKdukZTYkV32m3tGQndWBH0Id5T88c0SLXpLBG7fdNehzlADwiNbASet3AdL8NP_i2MmQoHINtE17QawvxCnKeIOe_WHj9YLxEHo_37Zty_XMgQHMMvtQ5YhCDqUge2ZQmvirEA8_vGWmt1VfpjcJEA6orATmgn7bKn2L1Ekpj3YpOWoe1voBTkcnGiyWIfHwSVaICHUZtrPzduqEQm2Jh9IGfqME4RIP2-k-YKZ4Lcs1l0lsgGbbV2RW0C7lBVcnp9GwFA9aIyTYph0xReBpWrOs_iOsjZv8D2xdpJOwctEZ-nCHmqvSk_Bl9hE9Oldg06IydCDCjtsXlVcpVVg-ZDoRU/4s4/SA6ztXqmSMSGunSEkAUVng/h1/h001.mpKNJst_4Y_ItRo0rb4DMx-GaHjYQM12ALN14MwvxZ1A
authors: [manager.dev]
keywords: [engineering manager, hands-on, dette de compétence, mentorat technique, outillage interne]
theme: Leadership
tone: opinion
used_in: ["2026-07-07"]
---

## Résumé

Ce billet de la newsletter manager.dev part d'un constat chiffré : 95 % des engineering managers voudraient coder davantage mais s'en sentent incapables. L'auteur décrit le glissement progressif du manager « hands-on » vers le manager 100 % réunions, puis propose une méthode concrète pour renouer avec le code sans empiéter sur le chemin critique de l'équipe : choisir de petites tâches à fort bénéfice pour les développeurs. Il illustre cette approche avec deux exemples internes — un chatbot documentaire RAG construit par un collègue manager, et un outil d'automatisation qu'il a lui-même développé pour simplifier un processus pénible de copie de données.

## Points clés

- 95 % des engineering managers voudraient coder plus mais ne s'en sentent plus capables.
- Deux profils de managers : les « super hands-on » qui prennent des tickets chaque sprint, et les managers à temps plein en réunion, sans temps de code — presque tout le monde glisse du premier vers le second.
- La régression est progressive : « un sprint sans code devient deux, puis dix, puis toute une année » — ce n'est plus un problème de temps disponible mais d'habitude perdue.
- Solution proposée : choisir des tâches hors chemin critique, dans l'une de ces trois catégories — aider directement les ingénieurs, apprendre quelque chose de nouveau, ou traiter un sujet dont personne d'autre ne s'occupera.
- Exemple 1 : un manager de l'équipe a construit, avec un dépôt open source existant, un chatbot interne branché sur Confluence, les README GitHub et Slack, pour répondre aux questions récurrentes sur le legacy.
- Exemple 2 : l'auteur a automatisé lui-même (UI simple + backend Python) un processus manuel et lent de copie de données de prod vers QA, remonté en rétrospective par son équipe.

## Analyse approfondie

Le texte s'ouvre sur le paradoxe vécu par beaucoup de managers techniques : on attend d'eux qu'ils aident leurs équipes à adopter l'IA efficacement, alors qu'ils peinent eux-mêmes à rester dans la pratique du code. L'auteur distingue deux trajectoires : le manager « super hands-on », qui prend des tâches à chaque sprint et connaît la base de code en profondeur, et le manager à plein temps en réunions, qui ne code plus du tout. Presque tout le monde commence dans la première catégorie et glisse vers la seconde — lui-même dit avoir vécu cette transition deux fois. Le mécanisme est insidieux : ce n'est pas un choix brutal mais une accumulation de sprints sans tâche de code, jusqu'à ce qu'une année entière passe sans qu'on ouvre son IDE. Le vrai obstacle au retour n'est alors plus le temps (il reste toujours deux ou trois heures disponibles par semaine) mais la perte de l'habitude et l'auto-persuasion qu'on ne pourra rien produire d'utile en si peu de temps.

Pour sortir de ce piège, l'auteur recommande de choisir des tâches précises, hors du chemin critique, qui répondent à l'un des trois critères suivants : aider concrètement les ingénieurs de l'équipe, apprendre quelque chose de nouveau, ou traiter un sujet utile à l'entreprise que personne d'autre ne prendra en charge. Il détaille un premier exemple vécu par un collègue manager avec huit ans d'ancienneté dans l'entreprise : interrompu en permanence par les mêmes questions sur des parties historiques du code, il a fini par documenter ses réponses — sans succès, car personne ne consultait cette documentation, non par paresse mais parce qu'elle restait invisible. Sa solution a été de construire, à partir d'un dépôt open source existant (sans compétence frontend requise), un chatbot interne interrogeant Confluence, les README GitHub et les canaux Slack publics de l'entreprise, avec à la clé un article détaillé publié sur Medium expliquant la démarche technique (RAG, Langchain, base vectorielle).

Le second exemple est personnel : lors d'une rétrospective, un membre de l'équipe se plaint d'un processus long et pénible de copie de données de production vers les environnements de QA, jusque-là géré par un job Jenkins limité à de petits volumes. L'auteur construit alors une interface simple (avec l'aide de ChatGPT, se disant « nul en CSS ») et un backend Python qui permet de lancer la copie selon des critères précis et de recevoir une notification par e-mail (via SendGrid) une fois l'opération terminée. Il souligne le double bénéfice de ce type de projet : améliorer concrètement le quotidien des ingénieurs, tout en permettant au manager d'apprendre quelque chose de nouveau au passage. Sa conclusion est un plaidoyer pour que tout manager technique, jusqu'au CTO, conserve une pratique minimale du code — rendue plus soutenable en choisissant des tâches modestes, à son propre rythme.

## Pourquoi ça compte

Ce billet donne une méthode concrète et peu coûteuse en temps pour qu'un manager technique reste crédible et connecté au code, un enjeu d'autant plus sensible à l'ère des agents où l'on demande justement à ces managers d'accompagner l'adoption de l'IA par leurs équipes.
