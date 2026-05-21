---
title: "anshuman on X: \"On Building Agents From First Principles\""
date: 2026-05-21
url: https://links.tldrnewsletter.com/Gb5Zoo
authors: [Anshuman Mishra]
keywords: [agents, reinforcement learning, environment, reward, action space]
theme: IA
tone: tutorial
used_in: ["2026-05-21"]
---

## Résumé

Anshuman Mishra propose de construire un modèle mental des agents IA « depuis les fondations », plutôt qu'en partant d'un framework. Avant le trainer, il y a un environnement ; avant le reinforcement learning, un espace d'actions ; avant l'agent, une politique qui produit des actions modifiant l'état du monde. À travers un exemple volontairement minuscule — un agent texte-vers-diagramme qui émet du JSON structuré — il montre que la boucle de fond (prompt → action → environnement → reward → gradient) est universelle, et que la vraie bascule est que l'agent génère des instructions exécutables, pas du texte plausible.

## Points clés

- Les tutos sur le post-training démarrent trop haut dans la pile (le framework) ; mieux vaut partir plus bas.
- La boucle fondamentale : `prompt → action du modèle → environnement → reward → mise à jour du gradient`.
- Les libs (TRL, Unsloth, PRIME-RL, verl, OpenRLHF) ne sont pas magiques : ce sont des infrastructures autour de cette boucle.
- La première question n'est pas « quel trainer RL ? » mais « quel est l'environnement ? ».
- Un environnement n'a besoin que de trois choses : un prompt d'entrée, un format d'action, une fonction de reward.
- Le SFT est souvent nécessaire avant le RL : le modèle doit d'abord apprendre le « langage » de l'environnement (JSON valide, IDs stables, pas de doublons, coordonnées finies…).

## Analyse approfondie

*Note de l'auteur : les arguments sont les miens ; l'écriture et la structure ont été affinées avec GPT 5.5. C'est en partie une expérience d'usage de l'IA pour rédiger vite des billets de recherche technique à partir de notes brutes, tout en gardant le goût, la direction et les affirmations humains.*

Les tutoriels sur le post-training démarrent trop haut dans la pile. Ils commencent par un framework. Installe cette librairie, définis cette fonction de reward, lance ce trainer, regarde la courbe de reward monter. C'est utile une fois qu'on comprend déjà ce qui se passe. C'est moins utile quand on essaie de se construire un modèle mental de l'ensemble du système.

Je trouve plus utile de partir d'un cran plus bas. Avant qu'il y ait un trainer, il y a un environnement. Avant qu'il y ait du reinforcement learning, il y a un espace d'actions. Avant qu'il y ait un agent, il y a une politique produisant des actions qui changent un état du monde.

Ce billet est une tentative de construire cette image depuis les premiers principes.

L'exemple sera délibérément petit : un agent texte-vers-diagramme. L'utilisateur demande un diagramme simple, et le modèle produit des actions JSON structurées qui créent des formes sur un canevas. On peut voir ça comme une version minuscule d'un agent à la tldraw. Au lieu de cliquer dans un vrai éditeur, le modèle émet des actions comme « créer un rectangle », « ajouter un label », « connecter ces deux nœuds ».

Le but n'est pas de construire le meilleur agent de diagrammes au monde. Le but est de comprendre la forme de l'entraînement d'agents lui-même.

À haut niveau, la boucle est : `prompt → action du modèle → environnement → reward → mise à jour du gradient`.

Presque tout système d'entraînement d'agents est une version à grande échelle de cette boucle. Un agent navigateur, un agent de code, un agent tableur, un planificateur robotique, un solveur de maths et un agent de diagrammes ont tous la même structure de base. Ils diffèrent par l'environnement, l'espace d'actions et la fonction de reward.

C'est la partie facile à manquer quand on utilise des frameworks. Des librairies comme TRL, Unsloth, PRIME-RL, verl, OpenRLHF, ou des trainers internes maison, ne sont pas magiques. Ce sont surtout de l'infrastructure autour de cette boucle : batching, génération de rollouts, inférence distribuée, calcul de reward, logging, modèles de référence, clipping, checkpointing et scaling. Le cœur conceptuel est bien plus petit.

Un modèle de langage est une distribution sur des séquences. Quand on l'utilise comme agent, on demande à cette distribution de produire des actions au lieu de prose ordinaire. Étant donné une observation, le modèle émet une action. Dans un modèle de chat, l'observation est la conversation et l'action est le message de l'assistant. Dans un agent navigateur, l'observation peut être le DOM et l'action un clic ou une frappe. Dans un agent de code, l'observation peut être l'état du dépôt et l'action un patch. Dans un agent de diagramme, l'observation est la requête utilisateur et l'action un objet JSON décrivant formes et connexions.

La première question n'est donc pas « quel trainer RL dois-je utiliser ? ». La première question est : quel est l'environnement ?

L'environnement définit quelles actions sont valides, ce qui arrive quand ces actions sont exécutées, et comment le succès est mesuré. Dans le fine-tuning supervisé ordinaire, cet environnement est souvent implicite. On montre au modèle des exemples de bon comportement et on lui demande de les imiter. En reinforcement learning, l'environnement devient explicite. Le modèle essaie quelque chose, l'environnement répond, et la fonction de reward décide si la tentative était bonne.

Pour un agent de diagramme, une complétion n'est pas bonne simplement parce qu'elle « sonne » plausible. Elle est bonne si le JSON parse, si le schéma est valide, si le canevas accepte les actions, si les objets demandés apparaissent, si les flèches connectent les bons nœuds, et si la disposition finale est compréhensible. C'est la différence centrale entre le fine-tuning de chat ordinaire et l'entraînement d'agents : l'entraînement d'agents ancre la sortie du modèle dans un monde exécutable.

Partons du plus petit espace d'actions possible. Le modèle doit retourner du JSON avec un tableau `actions`. Chaque action crée une forme ou connecte deux formes. Une complétion valide ressemble à un objet contenant des `create_shape` (type, id, forme, coordonnées x/y, largeur/hauteur, texte) et des `connect` (from, to, texte).

Cela paraît simple, mais contient déjà la structure essentielle de l'usage d'outils (tool use). Le modèle ne génère plus seulement du texte. Il génère des instructions qu'un autre système va exécuter. Cela change le problème d'entraînement : le modèle doit apprendre non seulement quoi dire, mais ce que l'environnement acceptera. Il doit créer les formes avant de les connecter. Il doit utiliser des IDs stables. Éviter les IDs en double. Garder des coordonnées finies. Éviter les types de formes invalides. Émettre du JSON parseable. Ce ne sont pas des détails philosophiques : ils déterminent si la politique peut seulement entrer dans la région valide de l'espace d'actions.

C'est pourquoi le SFT est souvent nécessaire avant le RL. Avant que le modèle puisse optimiser le reward, il doit apprendre le langage de l'environnement.

Un environnement n'a besoin que de trois choses : un prompt d'entrée, un format d'action et une fonction de reward. L'auteur en donne une implémentation minimale en pur Python : un canevas déterministe supportant rectangles, ellipses, losanges, blocs de texte et flèches, avec validation (types autorisés, IDs uniques, dimensions positives et bornées, nombres finis, interdiction de connecter une forme à elle-même). Le point n'est pas que ce canevas soit sophistiqué, mais qu'il fournisse un monde déterministe dans lequel les sorties du modèle peuvent réussir ou échouer.

## Pourquoi ça compte

Au moment où l'on empile des frameworks d'agents, ce billet remet l'essentiel au centre : un agent, c'est un environnement, un espace d'actions et une reward. Le bon modèle mental pour quiconque construit ou évalue des agents en production.
