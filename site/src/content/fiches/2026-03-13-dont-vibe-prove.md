---
title: "Don't Vibe — Prove"
date: 2026-03-13
url: "https://ngrislain.github.io/projects/2026-3-12-dont-vibe--prove/"
authors: ["NGrislain"]
keywords: [vérification formelle, types dépendants, Lean 4, Curry-Howard, vibe coding, spécification]
theme: IA
tone: opinion
used_in: ["2026-03-13"]
---

## Résumé

L'article propose de remplacer le vibe coding par la vérification formelle grâce aux types dépendants (Lean 4). Si les humains ne lisent plus la majorité du code généré, la lisibilité d'un langage n'est plus la priorité — c'est le pouvoir de spécification qui compte. Via la correspondance de Curry-Howard, les types deviennent des propositions et les programmes des preuves, permettant au compilateur de vérifier la correction du code et non simplement sa compilation. Un changement philosophique fondamental : passer de l'écriture de code à l'écriture de spécifications.

## Points clés

- Si les humains ne lisent plus le code généré, la lisibilité n'est plus la priorité — le pouvoir de spécification l'est
- Les types dépendants (Lean 4) permettent d'exprimer des propriétés arbitraires dans le système de types : pas juste "c'est une liste" mais "c'est une liste triée de longueur n"
- Correspondance de Curry-Howard : les types sont des propositions, les programmes sont des preuves — le compilateur vérifie les preuves, pas juste la compilation
- Le vibe coding a mûri (harnesses de vérification, règles, tests automatisés) mais le fossé entre spécification et implémentation reste
- Proposition radicale : et si le système de types *était* la spécification, éliminant le fossé entre intention et implémentation ?
- Changement philosophique : passer de l'écriture de code à l'écriture de spécifications formelles

## Analyse approfondie

L'IA peut écrire du code rapidement. Mais peut-elle écrire du code **correct** ?

Le vibe coding a grandi. Ce qui a commencé comme du « prompt and pray » a évolué en une discipline d'ingénierie sérieuse : les praticiens conçoivent des harnesses de vérification, écrivent des fichiers de règles, mettent en place des suites de tests automatisés, et laissent les agents IA tourner de manière autonome pendant des heures. Le rôle humain s'est déplacé de l'écriture de code vers la définition de contraintes et la review des résultats. Les résultats sont impressionnants — et s'améliorent rapidement.

Ce changement a un corollaire rarement explicité : si les humains ne lisent plus la majorité du code généré, alors optimiser un langage pour la lisibilité humaine n'est plus la priorité qu'il était. L'attrait de Python ou JavaScript — syntaxe claire, courbe d'apprentissage douce — importait quand les humains étaient les auteurs **et** les lecteurs principaux. Dans un monde où l'IA écrit l'implémentation et où les humains définissent surtout l'intention, la valeur d'un langage réside de plus en plus dans la précision avec laquelle il peut exprimer **ce que** le code devrait faire, et non dans la facilité avec laquelle un humain peut lire **comment** il le fait. Les langages vont probablement déplacer leur focus de l'ergonomie d'implémentation vers le pouvoir de spécification.

Pourtant, aujourd'hui, une tension fondamentale demeure. Aussi sophistiqué que soit le harness, la spécification et l'implémentation restent des artefacts séparés. Les contraintes vivent à un endroit, le code à un autre, et le lien entre eux doit être continuellement vérifié par de l'outillage externe. Il y a toujours un fossé entre l'intention et l'implémentation — un fossé qu'on peut réduire, mais jamais combler.

Et si le système de types **était** la spécification ?

### Les types comme spécifications

Tout système de types exprime **certaines** propriétés — même `int` vs `string` élimine une classe d'erreurs. Des systèmes de types plus riches expriment des propriétés plus riches : les génériques contraignent les relations entre types, les types linéaires tracent la propriété des ressources, les types à raffinement attachent des prédicats aux types de base. Mais les **types dépendants** vont plus loin : les types peuvent dépendre de **valeurs**, ce qui rend le langage de types suffisamment expressif pour énoncer des propositions logiques arbitraires. Pas seulement « c'est une liste » mais « c'est une liste **de longueur n** ». Pas seulement « cette fonction retourne une liste » mais « cette fonction retourne une liste **et voici une preuve vérifiée par machine qu'elle est triée** ».

Ce n'est pas spéculatif. C'est Lean 4 aujourd'hui.

Le fondement théorique est la **correspondance de Curry-Howard** : les types **sont** des propositions, et les programmes **sont** des preuves. Une fonction de type `A → B` n'est pas simplement un morceau de code qui transforme `A` en `B` — c'est une preuve constructive que « si `A`, alors `B` ». Quand on écrit `List α → SortedList α`, on définit simultanément une fonction et on énonce un théorème : « pour toute liste, il existe une version triée, et voici la preuve ». Le compilateur ne se contente pas de vérifier que le code s'exécute — il vérifie que la **preuve** est valide.

### La thèse : l'IA devrait écrire des preuves, pas du code

La thèse de l'article est directe : dans un monde où l'IA génère l'implémentation, nous devrions exprimer nos intentions dans un langage où la correction est vérifiable par machine. Les types dépendants offrent exactement cela. Au lieu de :

1. Écrire une spécification en langage naturel
2. Demander à l'IA de générer du code
3. Espérer que le code corresponde à la spécification
4. Écrire des tests pour vérifier (partiellement) la correspondance

On pourrait :

1. Écrire une spécification en types dépendants
2. Demander à l'IA de générer une preuve (un programme qui satisfait le type)
3. Laisser le compilateur vérifier que la preuve est valide

Le fossé entre intention et implémentation disparaît, non pas parce que l'IA est devenue parfaite, mais parce que le système de types rend toute implémentation incorrecte *impossible à compiler*.

### Lean 4 en pratique

L'article illustre avec des exemples concrets en Lean 4 comment les types dépendants fonctionnent. Un type comme `Vector α n` encode non seulement le contenu (des éléments de type `α`) mais aussi la longueur (`n`). Une fonction de concaténation `Vector α m → Vector α n → Vector α (m + n)` garantit *au niveau du type* que le résultat a la bonne longueur. Pas besoin de test — le compilateur le vérifie.

### Les obstacles et le réalisme

L'article ne prétend pas que cette approche est prête pour le mainstream. Les types dépendants ont une courbe d'apprentissage abrupte. Lean 4, bien que plus ergonomique que ses prédécesseurs (Coq, Agda), reste un outil de niche. La productivité immédiate est inférieure à celle d'un langage comme Python.

Mais l'argument est que ces calculs changent quand l'IA est dans la boucle. Si c'est l'IA qui écrit le code (les preuves), la courbe d'apprentissage du langage d'implémentation importe moins. Ce qui importe est la capacité du langage de spécification — le système de types — à exprimer précisément l'intention humaine.

### Du code au contrat

L'article conclut sur un changement de paradigme philosophique. Le développement logiciel est traditionnellement centré sur le **comment** : comment implémenter, comment optimiser, comment structurer le code. Les types dépendants déplacent le centre de gravité vers le **quoi** : quelles propriétés le programme doit satisfaire, quelles garanties il doit fournir, quels invariants doivent tenir.

Dans un monde où l'IA gère le « comment », la valeur humaine réside dans le « quoi ». Et les types dépendants sont le langage le plus précis que nous ayons pour exprimer le « quoi ».

## Pourquoi ça compte

Cet article pousse la réflexion sur le vibe coding à son terme logique : si l'IA écrit le code et que les humains ne le lisent plus, alors les langages doivent évoluer de la lisibilité vers la vérifiabilité — un changement de paradigme qui remet en question les fondements mêmes du génie logiciel.
