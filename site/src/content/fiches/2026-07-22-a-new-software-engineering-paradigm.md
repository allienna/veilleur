---
title: "A new software engineering paradigm – Blog"
date: 2026-07-22
url: https://georgwiese.github.io/posts/formal-verification-ai/
authors: [georgwiese.github.io]
keywords: [formal verification, Lean, AI, review bottleneck, machine-checkable proof]
theme: IA
tone: opinion
used_in: ["2026-07-22"]
---

## Résumé

L'auteur défend un nouveau paradigme d'ingénierie logicielle combinant vérification formelle et IA, déjà expérimenté avec succès par son équipe. L'humain spécifie le comportement attendu dans un langage formel comme Lean ; l'IA écrit à la fois le code et une preuve machine-vérifiable qu'il respecte la spécification, ce qui supprime le besoin de relecture humaine de l'implémentation. Le point central : l'IA fait passer à l'échelle l'écriture de code mais pas sa relecture, créant un nouveau goulot d'étranglement. La vérification formelle est présentée comme un moyen d'utiliser l'IA plus efficacement, la hausse d'assurance n'étant presque qu'un effet secondaire.

## Points clés

- Le paradigme : humains spécifient en langage formel (Lean), l'IA écrit code + preuve machine-vérifiable.
- L'IA seule bute sur le goulot de la relecture : elle scale l'écriture, pas la revue.
- On ne peut pas « YOLO » et supprimer la revue pour la plupart des codebases — l'IA devrait d'abord beaucoup progresser.
- La preuve formelle élimine la revue de deux façons : correction garantie par la spec, et lisibilité/maintenabilité humaine devenues secondaires si l'IA gère tout le code.
- Ce n'est pas réservé aux logiciels critiques type aéronautique : c'est un levier pour du logiciel « ordinaire » qu'on ne veut pas non plus livrer à l'aveugle.
- Le framework distingue contraintes dures (propriétés requises) et objectifs d'optimisation (benchmarks).

## Analyse approfondie

Dans ce billet, j'aimerais rassembler quelques réflexions sur ce que je crois être un nouveau paradigme en ingénierie logicielle. Il est réalisable aujourd'hui, et mes collègues et moi l'avons utilisé avec succès ces deux dernières semaines. En bref, le paradigme combine **vérification formelle et IA** :

- Les humains spécifient ce qu'ils veulent que le logiciel fasse dans un langage formel comme [Lean](https://lean-lang.org/).
- L'IA écrit le logiciel *et* une preuve formelle qu'il respecte la spécification. La preuve est vérifiable par machine, éliminant le besoin de relecture humaine de l'implémentation générée.

### L'IA seule souffre du goulot de la relecture

Je crois que cette combinaison de vérification formelle et d'IA est *bien* plus efficace que l'IA seule. La raison : la revue de code. Même si les agents peuvent écrire du code à coût marginal quasi nul, relire tout ce code devient le nouveau goulot d'étranglement.

Alors pourquoi ne pas « YOLO » et abandonner la revue ? Dans certains domaines, ce serait peut-être acceptable. Mais pour la plupart des codebases, l'IA devrait d'abord devenir *beaucoup* meilleure. Ma façon de le voir : l'IA est peut-être aujourd'hui à peu près au niveau d'un seul humain pour écrire du code. Un développeur seul peut maintenir la qualité, mais ne peut pas passer à l'échelle ; les équipes humaines scalent en distribuant le travail et en utilisant la revue de code pour maintenir la qualité. L'IA scale l'écriture sans scaler la relecture, créant un goulot.

Notez que je ne parle pas d'avions ici. Beaucoup de logiciels « ordinaires » ne sont pas assez critiques pour justifier une vérification formelle en soi, mais ils *le sont* assez pour qu'on ne veuille pas non plus les livrer à l'aveugle. Le point clé de ce billet : **la vérification formelle est un moyen d'utiliser l'IA plus efficacement**. La hausse d'assurance est presque un effet secondaire.

### Éliminer le goulot de la relecture

L'approche vérification formelle + IA peut éliminer la relecture humaine du code d'implémentation généré de deux manières. D'abord, en supposant que la spécification capture le comportement voulu, on n'a plus à se soucier de la correction du code. Ensuite, si le code est entièrement géré par l'IA, sa maintenabilité et sa lisibilité humaine deviennent moins importantes.

Le cadre général est le suivant :

- **Les humains définissent les *contraintes dures*** : ce sont les propriétés requises du logiciel, exprimées comme une spécification formelle. Elles capturent généralement une notion de correction.
- **Les humains définissent les *objectifs d'optimisation*** : les benchmarks mesurent ce que le code doit optimiser. Exemples évidents : le temps d'exécution et l'usage des ressources, mais les objectifs peuvent aussi inclure des propriétés difficiles à formaliser, testables expérimentalement.
- **Les agents écrivent le code et les preuves** : chaque changement proposé s'accompagne d'une preuve formelle que le logiciel satisfait les contraintes dures. Les benchmarks [...].

## Pourquoi ça compte

Si le vrai goulot de l'ère des agents devient la relecture, la vérification formelle propose une sortie radicale : remplacer la revue humaine par une preuve machine — un signal fort pour repenser le rôle du développeur.
