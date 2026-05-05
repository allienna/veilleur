---
title: "Nicolas Bustamante on X: \"Model-Harness-Fit\""
date: 2026-05-05
url: https://links.tldrnewsletter.com/qUoyVM
authors: [Nicolas Bustamante]
keywords: [agents, harness, Claude Code, Codex, model-agnostic]
theme: IA
tone: opinion
used_in: ["2026-05-05"]
---

## Résumé

Nicolas Bustamante a fait tourner Claude Code, Codex CLI et GitHub Copilot CLI sur la même machine, sur les mêmes fichiers, avec les mêmes prompts. Trois harnais qui semblent identiques en surface produisent des comportements visiblement différents. Sa thèse : les modèles sont post-entraînés contre un harnais spécifique, pas seulement contre une API. Conséquence stratégique : ceux qui tentent de construire des agents "model-agnostic" finissent toujours par dégrader leurs modèles, ou par maintenir une stack complète par fournisseur.

## Points clés

- Trois agents de coding (Claude Code, Codex CLI, Copilot CLI) sur même workstation, même git, même bash : comportements différents au-delà du style.
- Les modèles sont post-entraînés contre un harnais : noms d'outils, schémas, tags de citation, structure des skills, protocole de planification.
- Sortir un modèle de son harnais natif = perdre de la performance non récupérable.
- "Swapping orchestrators is not a cosmetic change. It is a model swap in disguise."
- Pour rester multi-provider sans dégrader : maintenir une stack complète par modèle, et exposer le choix comme "tu choisis un produit, pas juste un modèle".

## Analyse approfondie

Vaut-il mieux utiliser un LLM avec son harnais natif (Claude Code ou Codex), ou un harnais générique qui swap les modèles à la demande ?

Un ingénieur OpenAI a tweeté un mème hilarant sur le sujet ce matin, j'ai donc décidé de creuser en regardant les implémentations de harnais de Codex, Claude Code et du SDK GitHub. Le harnais compte-t-il vraiment autant que ça ?

Je garde trois agents de coding actifs sur la même workstation. Claude Code dans un terminal. Codex CLI dans un autre. GitHub Copilot CLI dans un troisième. Mêmes fichiers. Même arbre git. Même bash. Trois harnais différents qui semblent indistinguables.

J'ai passé le même prompt dans les trois et le comportement était visiblement différent, de manière qui dépassait largement les différences de surface — style et vitesse — auxquelles je m'attendais entre vendeurs.

La réponse facile, c'est que "les modèles se comportent différemment parce que ce sont des modèles différents". Mais ici j'ai testé les mêmes modèles dans des harnais différents.

Les modèles sont post-entraînés contre le harnais, pas seulement contre l'API. Les noms d'outils qu'ils attendent, les schémas d'entrée qu'ils émettent, les tags de citation qu'ils enroulent autour des faits mémorisés, la structure de fichiers des skills qu'ils invoquent, le protocole de planification qu'ils suivent quand le harnais leur dit "fais d'abord un plan" (rien de tout cela n'est une capacité générique du modèle).

Ce sont des conventions au niveau byte cuites dans le post-training d'un modèle spécifique contre un harnais spécifique. Sortez le modèle de son harnais et vous abandonnez de la performance que vous ne pouvez pas récupérer sans réécrire l'un ou l'autre.

Cela a une conséquence directe pour quiconque a tenté de livrer un agent "model-agnostic". On ne peut pas juste swap un modèle.

Supporter BYOK et multi-modèle (ce qui est la posture responsable, puisqu'il est risqué de dépendre d'un seul fournisseur !) ajoute de la complexité d'ingénierie réelle.

Pour swapper un modèle proprement, il faut swapper le harnais avec : la surface d'outils, les formes de schéma, les corps de skills qui nomment ces outils, le contrat de citation, le rituel de mémoire, la structure du system prompt, parfois le protocole de planification.

Tout ce qui est au-dessus du modèle doit bouger quand le modèle bouge. C'est pourquoi tout vendeur d'agent qui supporte plusieurs fournisseurs finit soit (a) par faire tourner une variante dégradée de chaque modèle qu'il supporte, soit (b) par maintenir une stack complète séparée par modèle et par exposer le choix à l'utilisateur comme "tu choisis un produit, pas juste un modèle". L'option (b) est le chemin qui gagne en qualité, et le coût d'ingénierie vaut la peine pour éviter d'être enfermé dans un seul lab.

Swapper un orchestrateur n'est pas un changement cosmétique. C'est un swap de modèle déguisé. Le lab frontier a passé l'année dernière à façonner les instincts du modèle pour une surface d'outils particulière.

## Pourquoi ça compte

Cette analyse remet en cause un dogme qu'on entend partout depuis 18 mois : "construis ton agent en model-agnostic pour ne pas être lock-in". Bustamante montre que ce n'est plus une option neutre — c'est un compromis quantifié sur la performance. Pour quiconque conçoit une plateforme d'agents en entreprise, la question "modèle + harnais" devient l'unité d'achat.
