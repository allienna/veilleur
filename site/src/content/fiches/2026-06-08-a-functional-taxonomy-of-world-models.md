---
title: "A Functional Taxonomy of World Models"
date: 2026-06-08
url: https://substack.com/redirect/a1cb9422-c590-4263-ad64-436719965fca?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [drfeifei.substack.com, World Labs]
keywords: [world models, intelligence spatiale, POMDP, simulateur, planificateur]
theme: IA
tone: opinion
used_in: ["2026-06-08"]
---

## Résumé

Fei-Fei Li et l'équipe de World Labs cherchent à mettre de l'ordre dans l'un des termes les plus surchargés de l'IA : le « world model ». Là où les modèles de langage apprennent la structure statistique du texte, les modèles du monde apprennent celle de l'espace et du temps. Les auteurs proposent une taxonomie fonctionnelle fondée sur la boucle agent-action-état-observation des POMDP, distinguant trois objets souvent confondus : le renderer (sortie : pixels), le simulateur (sortie : état) et le planificateur (sortie : actions).

## Points clés

- Le monde n'est pas fait de mots : le substrat physique (réel ou virtuel) diffère fondamentalement du texte.
- « World model » est revendiqué par la vision, la robotique, le RL et le génératif — chacun désignant une chose différente, d'où la confusion.
- La clarté vient d'un schéma ancien : la boucle POMDP (agent → action → état → observation), dont est issue la définition technique originelle du terme.
- Un **renderer** produit des observations (pixels) pour l'œil humain ; ce qui compte est la fidélité visuelle (ex. Google Genie 3, RTFM de World Labs).
- Un **simulateur** produit un état géométriquement, physiquement et dynamiquement fidèle, exploitable autant par des humains que par des programmes (agents RL, contrôleurs robotiques, véhicules autonomes).
- Un **planificateur** produit des actions : étant donné une observation et un but, il décide quoi faire ensuite (modèles Vision-Language-Action, World Action Models).

## Analyse approfondie

> « Le monde, c'est tout ce qui a lieu. » — Ludwig Wittgenstein, *Tractatus Logico-Philosophicus*, 1921

**Le monde n'est pas fait de mots.**

Dans un essai précédent, nous avancions que l'intelligence spatiale est la prochaine frontière de l'IA, et que les modèles du monde en sont le chemin. Ici, l'équipe de World Labs et moi voulons aller un cran plus loin : parmi les nombreuses choses aujourd'hui construites et appelées « modèles du monde », quelles pièces fonctionnelles composent réellement cette capacité — et à quoi sert chacune ?

Les modèles de langage ont donné aux machines une maîtrise extraordinaire des concepts, du vocabulaire et du raisonnement, mais le monde physique, virtuel ou réel, tourne sur un substrat différent. Là où les modèles de langage apprennent la structure statistique du texte, les modèles du monde apprennent la structure statistique de l'espace et du temps : comment la lumière tombe sur une surface, à quoi ressemble un jardin sous un angle qu'aucune caméra n'a capturé, comment les objets répondent à une force et obéissent aux lois de la physique.

Cela fait de « modèle du monde » l'un des termes les plus importants et les plus surchargés de l'IA d'aujourd'hui. Vision par ordinateur, robotique, apprentissage par renforcement et IA générative prétendent tous construire des modèles du monde, et chacun entend quelque chose de bien différent. Un **modèle vidéo** qui produit des flammes superbes mais physiquement impossibles, un **modèle de langage** improvisant un jeu jouable et un **moteur physique** simulant fidèlement une combustion portent tous le même nom.

Les Grecs anciens n'ont jamais pu s'accorder sur ce dont le monde était fait — feu, eau, ou atomes indivisibles — parce que le « monde » n'a jamais été une chose unique. C'était toujours un substitut pour la totalité qu'un penseur donné avait besoin de raisonner. L'IA a hérité du même problème, précisément au moment où le domaine a besoin de précision.

Trancher cette confusion commence par un diagramme plus ancien que toutes les technologies en question. Les manuels d'apprentissage par renforcement, dont le canonique Sutton et Barto, utilisent depuis des décennies une version de la même image pour décrire comment un agent interagit avec un monde. Le nom formel de cette image est le processus de décision markovien partiellement observable (POMDP), et la définition originelle du terme « modèle du monde » appartient à cette tradition.

Un agent — qui peut être une personne, un robot ou un système logiciel — entreprend des actions. Ces actions affectent l'état du monde. L'agent ne voit jamais cet état directement. Ce qui lui parvient, ce sont des observations : les photons qui tombent sur une rétine, les relevés d'un capteur, les pixels d'une image vidéo. De nouvelles observations informent de nouvelles actions, et la boucle continue.

Le mot « état » mérite d'être déplié, car son sens change d'un domaine à l'autre. Il ne s'agit pas de l'état du chimiste (solide, liquide, gaz), mais de l'état du physicien et du roboticien : une description complète de ce qui se passe dans le monde à un instant donné, incluant chaque objet, chaque position, chaque vitesse, chaque propriété. L'état est la réalité sous-jacente du monde ; complet en principe, mais jamais directement visible par un agent qui s'y trouve. Les observations sont la vue partielle qu'un agent en a. Les actions sont ce que l'agent fait en réponse.

Cette boucle — agent vers action vers état vers observation et retour — est la structure qui a donné son sens technique au terme moderne « modèle du monde ». L'expression elle-même est plus ancienne, remontant à la proposition de Kenneth Craik (1943) selon laquelle les esprits raisonnent en faisant tourner des « modèles à petite échelle » de la réalité, idée portée dans les réseaux de neurones à la fin des années 1980 et au début des années 1990. Les différentes choses aujourd'hui appelées modèles du monde sont en réalité différentes projections de cette même boucle. Chacune en restitue une pièce différente.

**Le premier type de modèle du monde est un renderer.** Un renderer produit des observations sous forme de pixels destinés à l'œil humain, et la qualité qui compte le plus est la fidélité visuelle. Un modèle vidéo qui transforme un prompt textuel en un plan de drone cinématographique est un renderer. Il en va de même pour un système interactif comme Genie 3 de Google, ou RTFM de World Labs, où le modèle génère des images en temps réel conditionnées par l'entrée de l'utilisateur. Le modèle ne porte aucune compréhension explicite de la structure tridimensionnelle. Il produit ce qu'un spectateur verrait, non ce qui est. Les bâtiments du plan de drone peuvent sembler parfaits vus d'en haut, mais essayez de rouler dans la ville en dessous et ils s'effondrent.

**Le deuxième type est un simulateur.** Un simulateur produit un état : une représentation géométriquement, physiquement ou dynamiquement fidèle du monde, sur laquelle humains et programmes peuvent calculer et interagir. Là où le contrat du renderer est purement visuel, celui du simulateur est structurel : une géométrie qui tient sous inspection, une physique qui respecte les lois de Newton, des dynamiques qui se comportent comme le monde l'exige. Un simulateur sert deux consommateurs à la fois. Des professionnels humains — architectes, designers, réalisateurs, développeurs de jeux — ont besoin d'une exactitude au-delà de la plausibilité visuelle. Des programmes informatiques — agents RL, contrôleurs de robots, véhicules autonomes — utilisent les simulateurs comme terrains d'entraînement où ils peuvent interagir avec le monde à grande échelle, testant des scénarios dangereux, coûteux ou impossibles à exécuter dans la réalité.

**Le troisième type est un planificateur.** Un planificateur produit des actions. Étant donné une observation et un but, il répond à la question de ce que l'agent devrait faire ensuite. C'est, à bien des égards, l'inverse du renderer. Là où un renderer prend des actions en entrée et produit des observations, un planificateur prend des observations en entrée et produit des actions, refermant la boucle perception-action. Les modèles Vision-Language-Action, les systèmes model-based et la nouvelle vague de World Action Models sont tous des tentatives de planificateurs : des systèmes capables de décider ce qu'un robot devrait faire dans un monde non structuré.

Ces trois catégories décrivent l'essentiel de ce qui est aujourd'hui livré, et la distinction est utile en pratique. Elles ne sont cependant pas fondamentalement séparées. La même connaissance sous-jacente du fonctionnement du monde — géométrie, physique, dynamiques — se trouve sous chacune d'elles. Un modèle capable de rendre une tasse sous n'importe quel angle devrait, en principe, en porter une représentation structurelle.

## Pourquoi ça compte

Avant de débattre des capacités d'un « modèle du monde », il faut savoir lequel des trois objets on construit : la confusion sur le substrat (pixels vs état vs actions) est une source majeure d'attentes mal calibrées dans toute l'industrie IA.
