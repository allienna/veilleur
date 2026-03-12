---
title: "Le data warehouse, c'est 20 ans de bricolage collectif institutionnalisé"
date: 2026-03-12
description: "Pourquoi les agents IA exposent brutalement la dette sémantique que les humains compensaient depuis des années dans nos architectures data."
themes: [Data, IA, Architecture]
image: data-warehouse-bricolage-collectif.png
---

Je suis arrivé chez un grand retailer du Nord avec une mission claire : migrer la stack data d'AWS vers Google Cloud. Propre. Délimitée. On savait faire.

Sauf qu'on a ouvert le capot, et on n'a pas été déçu !

Des pipelines en prod depuis des années dont l'auteur avait quitté l'entreprise. Aucune documentation. Personne ne touche parce que personne ne comprend vraiment ce que ça produit ni avec quelle donnée — et ça tourne, alors pourquoi risquer. Des tables avec des noms qui semblent explicites jusqu'au moment où tu réalises que deux équipes les utilisent différemment et obtiennent des résultats incompatibles. On n'a pas migré. On a fait des préconisations pour les nouveaux use cases et on est repartis avec une liste de dettes qu'on n'avait pas commandée.

**Ce n'était pas un problème technique. C'était un problème sémantique.**

Et ce n'est pas une histoire ancienne. Cette semaine encore, des surfaces de magasins aberrantes — voire physiquement impossibles — qui varient selon que tu regardes le système source, le BI ou le Google Sheet de quelqu'un. Un dictionnaire de données existe, mais mal utilisé, donc il devient inutile. Des données répliquées dans BigQuery sans que personne ne sache exactement quelles transformations ont été appliquées au passage.

On appelait ça de la gouvernance mais dans la réalité, **c'est du bricolage collectif institutionnalisé.**

Et ça fonctionne — parce que des humains comblent les trous. On invoque un Data Engineer en réunion pour arbitrer entre deux dashboards qui donnent des chiffres différents. Le *"Combien on a fait cette année ?"* qui génère trois réponses, toutes défendables, et où la direction tranche en faveur de l'équipe avec le plus grand capital sympathie. Les gens qui savent que `rev_adj` veut dire *"le CA mais retraité selon les règles de la promo du Q3 version finance"* — pas parce que c'est écrit quelque part, mais parce qu'ils étaient dans la salle quand ça a été décidé.

Ce savoir-là ne vit pas dans le data warehouse. Il vit dans les têtes. Dans les Slack. Dans les réunions. Dans les anciens qui forment les nouveaux.

C'est fragile, opaque, et ça ne passe pas à l'échelle.

Mais ça passe quand même — parce que le consommateur final est humain.

**Le problème, c'est que les agents ne savent pas bricoler.**

Un LLM branché sur ces données ne va pas *Slacker* un collègue pour vérifier. Il ne va pas *sentir* que quelque chose cloche dans un chiffre. Il va lire `rev_adj`, faire une inférence, et agir. À l'échelle. Sans hésiter une seconde. Et se tromper. Silencieusement. Sur tout ce qui vient après.

**Ce n'est pas un problème d'IA. C'est un problème de contexte.**

Pendant vingt ans, le Data Warehouse a été conçu pour les humains — capables de navigation, d'interprétation, de compensation sociale. Le *star schema*, c'est de la signalétique pour des humains qui cherchent leur chemin dans des tables. La *medallion architecture*, c'est une chaîne d'inspection conçue pour qu'un humain valide à chaque étape. Les catalogues de données, c'est de l'affichage — utile si quelqu'un les lit, inutile sinon.

**Changer l'opérateur change tout (ou presque)**

Ce qui remplace l'ETL comme travail central, ce n'est pas un nouveau framework ou un nouvel outil. C'est une question différente. L'ETL demandait : *est-ce que la donnée est arrivée ?* Ce qui vient demande : *est-ce que la donnée peut être comprise — sans moi dans la salle ?*

C'est un métier différent. Pas plus simple. Peut-être plus intéressant.

---

*Cet article a été en partie inspiré par "ETL is Dead" d'Ananth Packkildurai ([Data Engineering Weekly, mars 2026](https://open.substack.com/pub/dataengineeringweekly/p/etl-is-dead)) — qui a mis des mots précis sur quelque chose que je vis sur le terrain depuis des années.*
