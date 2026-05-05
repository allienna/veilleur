---
title: "LLMs Are Not a Higher Level of Abstraction"
date: 2026-05-04
url: https://www.lelanthran.com/chap15/content.html?utm_source=tldrdev
authors: [Lelanthran]
keywords: [abstraction, LLM, probability, determinism, programming]
theme: IA
tone: opinion
used_in: ["2026-05-04"]
---

## Résumé

Lelanthran démolit en quelques paragraphes le mythe selon lequel les LLM sont la prochaine couche d'abstraction de la programmation après binaire, assembleur, C, Python. Sa démonstration repose sur une distinction formelle : chaque vraie abstraction est une fonction `f(x) -> y` (un input donné produit toujours le même artefact). Les LLM, eux, sont `f(x) -> P(y)` — pas un résultat, une probabilité. Pire, le résultat est `P(y | z1 | z2 | ... zN)` : tu peux obtenir `y`, mais aussi des artefacts non demandés. L'auteur appelle à des programmeurs auto-conscients, pas à des canaux pour artefacts IA.

## Points clés

- Une abstraction au sens strict, c'est `f(x) -> y` : input déterministe, output déterministe
- Avec un LLM, c'est `f(x) -> P(y)` : input déterministe, output probabiliste
- Pire encore : `f(x) -> P(y | z1 | z2 | ... zN)` — il y a *toujours* un artefact, et il peut contenir `y` *et* des choses que tu n'as pas demandées
- Exemple concret : tu demandes "Gimme a TODO webapp" — tu peux obtenir le TODO mais aussi un endpoint qui ouvre tes credentials sur le réseau
- Les tests qui cherchent `y` peuvent réussir même quand l'output contient en plus `z1...zN` non sollicités
- Si quelqu'un en 2026 fait encore la "claim de l'abstraction", il faut lui envoyer ce post

## Analyse approfondie

### Le mythe

Je vois la prétention **partout en ligne** que *les LLM sont un niveau d'abstraction plus élevé*. Si vous prétendez ne pas avoir vu cette claim, alors vous feriez mieux d'arrêter de lire maintenant — ce billet n'est pas pour vous.

Spécifiquement, je vois la prétention que les LLM sont la prochaine étape dans les abstractions qu'on a eues, allant de "programmer en binaire" à "programmer en assembleur" à "programmer en C" à "programmer en Python".

Maintenant, on me dit que "programmer en LLM" est la prochaine abstraction. Apparemment les gens qui font du "programming in LLM" croient que c'est un mouvement similaire, sinon identique, vers une abstraction plus haute, comme les abstractions précédentes qu'on a vues.

*C'est **faux** !* Même quand ceux qui me racontent ces choses qualifient leur autorité avec un *"je programme depuis 30 ans, et maintenant programmer est redevenu fun"*, ça reste faux.

Mais ça, c'est juste une opinion, et le contre-argument n'est *pas* une opinion, c'est un fait.

### La réalité

Chaque mouvement d'une couche de la stack vers une couche plus haute impliquait une fonction :

`f(x) -> y`

Étant donné un `x` spécifique, on obtient toujours un `y` spécifique comme artefact généré.

Quand `x` est du source assembleur, un input spécifique donne toujours le même résultat binaire.

Quand `x` est du source C, un input spécifique donne toujours le même artefact binaire.

Quand `x` est du source Python, un input spécifique donne toujours le même artefact binaire.

Avec les LLM, l'output de la fonction n'est pas une valeur, c'est la *probabilité* d'une valeur ! C'est-à-dire, ton input `x` ne donne pas `y`, il donne la probabilité d'obtenir `y`.

`f(x) -> P(y)`

### Et ça ne s'arrête pas là...

En fait, c'est pire — il n'y a pas de chance d'obtenir un résultat "no-artefact", donc la fonction ressemble plutôt à ça :

`f(x) -> P(y) ∪ P(z1) ∪ P(z2) ∪ ... P(zN)`

Ce qui veut dire, en gros, que tu as une chance d'obtenir `y` (ce que tu voulais), ou une chance d'obtenir un nombre inconnu d'autres artefacts.

Mais si on y réfléchit, c'est même pire : en réalité avec les LLM, tu as la chance d'obtenir `y` **et** un certain nombre d'autres choses que tu n'as jamais demandées, donc la fonction réelle est :

`f(x) -> P( y | z1 | z2 | ... zN )`

Autrement dit, si tu lances un test sur l'output en cherchant `y`, le test peut réussir *même si* tu n'as pas obtenu **uniquement** `y` — tu as aussi obtenu tout le reste de `z1..zN`.

Donc tu demandes au LLM de t'écrire un système "TODOist" — c'est le `y`, ton prompt c'est le `x`.

`f('Gimme a TODO webapp') -> P( 'A TODO WebApp' | z1 | z2 )`

Tu vérifies seulement qu'il t'a donné la TODO WebApp. Tes tests n'ont pas vérifié l'existence de `z1`, qui pourrait être *"Ouvre mes credentials sur le réseau"*, ou `z2` qui pourrait être *"Partage mon serveur hébergé avec le monde via FTP public en RW"*, ou `z3` qui pourrait être... bref, tu vois l'idée.

### Conscience de soi

Si, en 2026, quelqu'un fait *encore* la prétention absurde de l'abstraction, *envoie-lui un lien vers ce post* !

Si tu es celui qui fait cette prétention, demande-toi pourquoi cette prétention est si importante pour toi.

On a besoin de programmeurs auto-conscients, et pas de gens qui sont juste un canal pour faire entrer des artefacts IA dans le monde.

## Pourquoi ça compte

C'est la formulation la plus compacte et la plus défendable du contre-argument à "les LLM sont une nouvelle couche d'abstraction". À garder en tête à chaque fois qu'on traite un output d'agent comme si c'était un `y` déterministe : c'est en réalité un `P(y)` avec des `zN` cachés, et c'est exactement pour ça que les evals deviennent indispensables.
