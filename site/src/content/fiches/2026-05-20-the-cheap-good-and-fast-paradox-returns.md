---
title: "The Cheap, Good, And Fast Paradox Returns"
date: 2026-05-20
url: https://engineering.prezi.com/the-cheap-good-and-fast-paradox-returns-2c7f0d8672e4?utm_source=tldrdev
authors: [Attila Vágó, engineering.prezi.com]
keywords: [AI-assisted development, productivity, engineering, paradox, Prezi]
theme: IA
tone: opinion
used_in: ["2026-05-20"]
---

## Résumé

Attila Vágó, staff software engineer chez Prezi, raconte son travail d'aider les équipes growth à adopter l'IA. Son constat : le vieux paradoxe "cheap, good and fast — pick two" qu'on pensait dépassé grâce à l'IA est en réalité de retour. Déployer Cursor à tout le monde ne suffit pas à transformer la vélocité des équipes. Les contraintes du métier (dépendances, régulations, revues, utilisateurs réels) ne disparaissent pas avec l'IA — elles redeviennent visibles dès qu'on essaie d'industrialiser.

## Points clés

- Le paradoxe "cheap, good, fast" semblait obsolète à l'arrivée de l'IA — il revient en force
- Donner Cursor à tout le monde n'est pas une stratégie : c'est une condition nécessaire mais largement insuffisante
- Les contraintes externes (régulations, dépendances, revues) freinent autant que les contraintes internes
- L'IA accélère certaines phases mais ne supprime pas la complexité globale du métier
- Analogie avec la rénovation d'appartement : le contractor a les meilleurs outils, mais reste contraint par l'électricien et le plombier
- Le rôle staff engineer évolue : ce n'est plus "code plus vite", c'est "lever les blocages systémiques à la diffusion de l'IA"

## Analyse approfondie

Combien de fois avez-vous dû dire à un manager, un client, un coéquipier que "cheap, good and fast" ne peut pas être vrai en même temps ? On finit par choisir entre basse qualité, livraison lente, ou solutions chères. Et l'IA ? Elle nous fait reconsidérer la faisabilité de ce trio. Au fond, c'est le rêve. Mais ça ne marche pas. Du moins, ça ne marchait pas avant l'IA. Est-ce que l'IA change suffisamment la donne pour effacer ce paradoxe vieux de plusieurs siècles ?

Actuellement, l'appartement de l'auteur est en rénovation majeure. Il a essentiellement déménagé chez la sœur de son contractor pendant une semaine parce qu'il n'a pas de salle de bain fonctionnelle. Ce n'était pas prévu. C'est arrivé parce que l'électricien et le plombier — dont on a besoin tous les deux pour refaire une salle de bain — n'ont pas réussi à venir aussi rapidement que le contractor l'espérait. Les deux souhaitaient que ce soit fait dans les 10 jours où il était en vadrouille en Transylvanie — beau coin, soit dit en passant — mais la réalité ne correspond pas toujours à ce qu'on espère.

Le logiciel n'est pas différent. Son contractor a tous les outils modernes qu'on peut imaginer. Il utilise même des lasers pour mesurer et aligner. Il n'est pas ralenti par ses outils. Ni par ses compétences. Il a même rénové le château d'Enya. Oui, *cette* Enya. L'auteur ne prend pas n'importe quel contractor. Mais rien de tout cela ne compte quand on a des dépendances et des régulations à respecter. Et ça s'applique aux développeurs logiciels autant qu'à un contractor.

**Tout ce qui vous ralentit.** Au cours des dernières semaines, le cœur de son job en tant que staff software engineer a été de trouver des moyens d'accélérer les équipes growth, d'essayer de les habiliter avec du développement et des outils pilotés par IA. Si ça vous semble être un objectif simple, détrompez-vous. Ce n'est pas une question de dire à tout le monde "utilisez Cursor" et de regarder ensuite les équipes pousser du code comme jamais. Il aimerait que ce soit son job. Il pourrait juste sourire toute la journée et approuver aléatoirement des PRs que Coderabbit a déjà approuvées. Mais il y a bien plus à faire que ça.

D'abord et avant tout, il faut comprendre ce qui ralentit réellement les équipes — et ce n'est presque jamais la vitesse à laquelle on tape du code. La suite du billet détaille les vrais points de friction qu'il a identifiés (dépendances, processus de revue, contraintes de conformité, alignement produit) et comment l'IA s'insère — ou pas — dans chacun d'eux.

## Pourquoi ça compte

C'est l'antidote au discours "tout le monde sera 10x avec Cursor". Pour un Engineering Director qui doit défendre des arbitrages de productivité avec son COMEX, c'est le rappel utile : la productivité d'une équipe est un système, pas une fonction du seul outillage individuel.
