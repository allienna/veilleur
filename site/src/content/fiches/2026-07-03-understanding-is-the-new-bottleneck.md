---
title: "Understanding is the new bottleneck"
date: 2026-07-03
url: https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html
authors: [Geoffrey Litt]
keywords: [compréhension, dette cognitive, revue de code, agents IA, augmentation]
theme: IA
tone: opinion
used_in: ["2026-07-03", "2026-07-07"]
---

## Résumé

Geoffrey Litt, design engineer chez Notion, défend une thèse à contre-courant : il reste crucial de comprendre le code que nos agents écrivent. Non pas seulement pour le *vérifier* (les agents deviennent bons à ça), mais pour *participer* — car un projet est fait de dizaines de boucles d'itération, et c'est notre compréhension qui nourrit la prochaine idée. Il présente trois techniques inspirées de la pédagogie : les explications (literate diffs, quiz), les micro-mondes interactifs, et les espaces partagés en équipe. Son fil conducteur : l'objectif de l'informatique a toujours été d'augmenter l'humain, pas seulement de l'automatiser.

## Points clés

- On comprend le code non pas uniquement pour vérifier, mais pour *participer* au processus créatif sur la durée.
- Ne pas comprendre crée une « dette cognitive » (concept de Margaret Storey et Simon Willison), analogue à la dette technique.
- Technique 1 — les explications : « literate diffs » structurés en prose, docs d'explication qui enseignent le contexte avant le détail, et quiz qu'on s'impose de réussir avant d'envoyer son code.
- Technique 2 — les micro-mondes : faire écrire par l'agent de petits outils interactifs qui aident l'humain à comprendre un système (inspiré de Seymour Papert).
- Technique 3 — les espaces partagés : construire une compréhension collective en équipe (agents et plans collaboratifs dans Notion).
- Le quiz agit comme un « régulateur de vitesse » : il empêche la boucle IA d'aller plus vite que la compréhension humaine.

## Analyse approfondie

**Avis tranché : je pense qu'il est toujours important de comprendre le code que nos agents écrivent !**

Dans cette conférence, j'explique pourquoi, et je montre quelques idées pour comprendre le code efficacement.

Les agents écrivent de plus en plus de code pour nous, et on sait tous qu'il devient plus difficile de suivre. Mais la bonne nouvelle, c'est qu'il existe de nombreuses façons de comprendre le code ! Lire les diffs ligne par ligne n'est pas la seule.

L'essentiel de cette conférence porte sur des techniques que j'ai trouvées utiles pour comprendre les systèmes que mes agents construisent : les docs d'explication de code, les quiz pour vérifier ma compréhension, les micro-mondes avec lesquels je peux jouer. Mais il faut d'abord poser une question plus fondamentale…

### Pourquoi comprendre ?

Ne sommes-nous pas censés nous retirer de la boucle et laisser les agents boucler tout seuls ? À mesure qu'ils deviennent plus intelligents, n'est-il pas moins important pour nous d'être dans le détail ?

Je pense que beaucoup de gens — même ceux qui sont pro-compréhension — ont une réponse légèrement erronée à cette question.

Une réponse possible : on comprend *pour vérifier*. On contrôle le travail de l'agent, on regarde s'il est correct. « Correct » peut vouloir dire beaucoup de choses : est-ce conforme au spec, est-ce bien architecturé… mais c'est fondamentalement une question de pouce levé / pouce baissé.

Or voici le problème : les agents deviennent de plus en plus doués pour vérifier leur propre travail. Et c'est une bonne chose ! J'aime quand mon agent ne fait pas d'erreurs. Mais alors, où cela nous laisse-t-il, nous les humains ?

C'est là qu'intervient une autre réponse : **on peut comprendre pour participer.** On apprend ce que fait l'agent pour pouvoir être un participant actif du processus créatif.

Ce n'est jamais une seule boucle ! Un projet, c'est de très nombreuses boucles avec l'agent. Et la compréhension que vous avez du système fait partie de votre capacité à trouver la prochaine idée pour le faire évoluer. Il faut un riche ensemble de concepts en tête pour penser de façon créative et fluide à la manière de faire avancer les choses. Sans cette aisance, votre capacité à participer au projet est sérieusement limitée.

Cela rejoint de près l'idée de « dette cognitive », popularisée par Margaret Storey et Simon Willison. C'est comme la dette technique : on peut s'en tirer à court terme sans comprendre ce qui se passe, mais ça finit par nous mordre.

Comment construire cette compréhension humaine quand on travaille avec l'IA et qu'on avance vite ? Ce n'est pas la première fois qu'on réfléchit à la façon de transmettre la compréhension : on peut s'inspirer de l'éducation et voler ses meilleures idées.

### Technique 1 : les explications

Chaque fois qu'un agent finit un travail, c'est une occasion d'explication — un artefact. Le plus naïvement, on peut lire un diff de code : la matière brute qui a changé. Mais que serait la *meilleure* explication possible ? Si une équipe — humaine ou IA — avait vraiment sué sur l'art de bien vous expliquer quelque chose, à quoi cela ressemblerait-il ?

J'ai créé une skill appelée `/explain-diff`, que j'utilise tous les jours et que beaucoup de collègues ont trouvée précieuse. Elle produit des explications de code bien structurées, en HTML, markdown ou docs Notion (Notion est un bon endroit pour collaborer et discuter de ces explications en équipe — divulgation : j'y travaille, donc je suis biaisé).

Premier principe : **enseigne-moi le contexte de fond !** Avant même d'arriver à ce qui a changé, aide-moi à comprendre ce qui existait déjà.

Deuxième principe : **l'intuition avant le détail.** Avant tout code, on énonce l'objectif et on explique les concepts liés. Tout cela construit mon intuition de l'essence du changement. On peut aussi bâtir cette intuition avec des figures interactives.

On arrive enfin au code. Mais un diff typique est un tas de fichiers édités par ordre alphabétique, sans explication. Un « literate diff », comme je l'appelle, est structuré comme de la prose — il parcourt les changements dans un ordre sensé, avec des explications et des extraits de code intégrés. Plus rapide à relire qu'un diff brut. Le résultat final est un joli dossier d'explication ; je lis toujours ça avant le diff, parfois même imprimé, emporté au café. Ironie savoureuse : l'IA transforme une activité interactive en un rapport papier statique sur lequel je peux me concentrer profondément.

Au bas d'une explication, il y a un quiz interactif — cinq questions sur le changement — auquel j'essaie de répondre. Ma règle : je n'envoie pas de code aux autres tant que je ne peux pas réussir le quiz, et je fais pareil quand je relis le code d'autrui. **Un quiz est un régulateur de vitesse.** En travaillant avec l'IA, il est facile que la boucle tourne plus vite que la vitesse de compréhension humaine. Le quiz est une force de rappel : je me demande mécaniquement « est-ce que je comprends vraiment ? » pour rester un participant créatif à part entière.

### Technique 2 : les micro-mondes

Idée suivante, inspirée du visionnaire de l'éducation Seymour Papert. Comment l'appliquer au code ? **Peut-on créer des mondes qu'on habite et où l'on intuite naturellement le fonctionnement du système et son évolution ?**

L'an dernier, en codant un interpréteur Prolog, je peinais à intuiter ce qui se passait à l'intérieur. Il y a une grande différence entre fabriquer un outil *pour moi* afin de déboguer, et laisser l'agent déboguer — le faire moi-même est la façon dont je développe ma compréhension chemin faisant. Dans un « centre de commande », j'ai regardé le nouveau site prendre vie de façon incrémentale, ce qui m'a laissé une compréhension similaire à un travail manuel, mais beaucoup plus rapide. Le point clé : **les agents peuvent écrire du code pour nous aider à comprendre du code.** C'est énorme !

### Technique 3 : les espaces partagés

Dernière technique. Jusqu'ici tout tournait autour de la compréhension en solo… mais **en équipe, il faut comprendre ensemble.** Je suis très enthousiaste à l'idée de créer des environnements partagés où les équipes bâtissent cette compréhension collective. On peut désormais faire tourner des agents Claude et Cursor dans Notion ; je code beaucoup ainsi. Et quand ces agents rédigent un plan technique dans Notion, c'est dans une page collaborative par défaut, donc je peux commenter avec mon équipe et en discuter immédiatement. Penser ensemble, pas seul !

### Le but a toujours été d'augmenter

Il reste important pour les humains de comprendre comment les choses fonctionnent *en général* ! **Pas seulement pour vérifier, mais pour participer.** Et ce n'est pas une idée nouvelle : elle remonte aux origines mêmes de l'informatique. Il y a 50 ans, Alan Kay imaginait que les ordinateurs pouvaient être un nouveau médium, meilleur que le livre, pour apprendre aux gens — surtout aux enfants — à penser le monde : jouer à un jeu interactif et éditer son code en jouant, pour mieux comprendre la physique.

**Le but a toujours été d'*augmenter*, pas seulement d'automatiser.** Il est beau que l'IA rende la création de simulations si accessible… Avoir l'IA pour nous enseigner est l'une des plus grandes possibilités jamais ouvertes par l'informatique. **Si nous construisons les bons outils, nous pouvons désormais comprendre le monde mieux que jamais.** Nous n'avons pas à simplement nous retirer de la boucle : nous pouvons aussi entrer *plus profondément* dedans. Ça ne tient qu'à nous.

## Pourquoi ça compte

À l'heure où l'on nous pousse à « sortir de la boucle », Litt renverse la perspective : la compréhension devient le vrai goulet d'étranglement, et outiller cette compréhension est la compétence stratégique de l'ingénieur augmenté.
