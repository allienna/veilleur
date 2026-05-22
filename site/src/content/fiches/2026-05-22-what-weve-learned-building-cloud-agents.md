---
title: "What we've learned building cloud agents"
date: 2026-05-22
url: https://cursor.com/blog/cloud-agent-lessons
authors: [Cursor]
keywords: [cloud agents, development environment, orchestration, reliability, infrastructure]
theme: IA
tone: opinion
used_in: ["2026-05-22"]
---

## Résumé

Un an après le lancement de ses agents cloud, Cursor partage ses plus grandes leçons. Les agents cloud tournent désormais sur leurs propres VM dédiées, avec environnements, dépendances et accès réseau propres ; ils travaillent en parallèle, sans surveillance, sur des tâches plus longues qu'un agent local. La leçon centrale et contre-intuitive : l'environnement de développement est le produit. Reconstruire un environnement complet dans le cloud est étonnamment difficile, et un environnement incomplet dégrade silencieusement la qualité de sortie — un symptôme qu'on attribue souvent à tort au modèle.

## Points clés

- Les agents cloud sont passés d'une simple extension des agents locaux à une véritable couche d'exploitation autour d'eux.
- Le facteur n°1 de qualité de sortie : donner à l'agent un environnement de développement complet, comme en a un développeur.
- En local, l'agent hérite gratuitement de l'environnement du poste ; dans le cloud, il faut tout reconstruire de zéro.
- Un environnement incomplet ne produit ni crash ni erreur — juste une dégradation subtile de la qualité, souvent imputée au modèle.
- Atteindre le « full environment » exige de reconstruire de l'infra : outils de build d'environnement, hibernation/reprise des VM, checkpoint/restore durables.

## Analyse approfondie

Quand Cursor a lancé ses agents cloud il y a un an, ils semblaient être une extension directe des agents locaux. Depuis, leurs capacités se sont considérablement étendues.

Les agents cloud tournent désormais sur leurs propres machines virtuelles dédiées, avec leurs propres environnements, dépendances et accès réseau. Ils peuvent travailler en parallèle, tourner sans surveillance, et prendre en charge des tâches plus longues qu'un agent local posé sur un laptop. Ces capacités introduisent des défis d'installation d'environnement, de fiabilité et d'orchestration, bien moins prononcés quand l'agent tourne en local.

Cursor partage les plus grandes leçons apprises en construisant des agents cloud, et explique pourquoi ce travail ressemble de moins en moins à porter un agent local sur un serveur, et de plus en plus à construire une couche d'exploitation (operating layer) autour de lui.

**L'environnement de développement est le produit.** Au cours de la dernière année, le plus grand facteur de qualité de sortie d'un agent cloud s'est révélé être l'assurance qu'il dispose d'un environnement de développement complet, comme en a un développeur. Ce n'est pas un sujet auquel on pense autant en local, parce que les agents locaux héritent gratuitement de l'environnement de travail du laptop. Dans le cloud, il faut tout reconstruire de zéro — et il est étonnamment difficile de savoir quand on ne l'a pas fait parfaitement.

Au lieu d'un crash ou d'un message d'erreur, le seul indice est souvent une dégradation subtile de la qualité de sortie. On peut ne pas le remarquer au début, ou, si on le remarque, l'attribuer au modèle. Mais encore et encore, Cursor a retracé le problème jusqu'au même diagnostic : l'agent cloud n'avait pas l'environnement nécessaire pour exécuter ou vérifier son travail. Un an plus tôt, cela comptait moins, parce que les modèles ne pouvaient de toute façon pas tirer grand-chose de leur environnement. Mais à mesure qu'ils sont devenus plus intelligents, la configuration de l'environnement est devenue le facteur déterminant de leur plein potentiel.

Aujourd'hui, atteindre le « full environment » exige de reconstruire une quantité surprenante d'infrastructure : de meilleurs outils utilisateur pour construire l'environnement de l'agent ; des méthodes pour hiberner et reprendre efficacement les VM des agents entre les messages ; des pipelines pour checkpointer, restaurer et forker rapidement et durablement.

## Pourquoi ça compte

C'est le rappel que l'agentique en production n'est pas un problème de prompt mais d'infrastructure : « l'environnement est le produit » est une leçon directement transposable à toute équipe qui industrialise des agents internes.
