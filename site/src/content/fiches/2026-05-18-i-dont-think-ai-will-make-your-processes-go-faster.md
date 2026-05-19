---
title: "I don't think AI will make your processes go faster"
date: 2026-05-18
url: https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/?utm_source=tldrdev
authors: [Frederick Van Brabant]
keywords: [process optimization, theory of constraints, AI productivity, software development]
theme: Leadership
tone: opinion
used_in: ["2026-05-18"]
---

## Résumé

Frederick Van Brabant remet en cause l'idée que l'IA puisse accélérer mécaniquement les process. En s'appuyant sur les classiques The Toyota Way et The Goal, il rappelle que la cause d'un goulot d'étranglement n'est pas toujours là où le temps se passe visiblement. En software dev, le vrai bottleneck est souvent en amont — dans la définition floue du besoin — et l'IA, qui accélère l'exécution d'instructions claires, n'aide pas à clarifier la pensée qui les produit.

## Points clés

- Les exercices d'optimisation de process trop simplistes ratent souvent le vrai problème
- Long duration ne signifie pas automatiquement que le problème vient de là
- En software dev, le bottleneck est souvent amont : traduction d'un besoin métier flou en spec claire
- "On ne fait pas avancer un projet plus vite en tapant plus vite au clavier"
- L'IA accélère l'exécution d'instructions claires, pas la pensée qui les produit
- Les classiques (Toyota Way, The Goal) restent essentiels pour penser les vrais leviers de productivité

## Analyse approfondie

J'ai l'impression que toutes les organisations sont, au moins partiellement, focalisées sur l'optimisation de process — quelque chose qui arrive souvent quand le marché est en baisse. Ces derniers temps, l'angle IA s'y ajoute, avec les attentes irréalistes qui suivent.

Pour être pleinement préparé, j'ai décidé de relire deux classiques absolus du domaine : The Toyota Way et The Goal. J'ai lu ces deux livres en fac, mais les relire m'a fait réaliser que beaucoup de ces exercices d'optimisation de process sont trop simplistes par nature et se trompent souvent sur ce sur quoi se concentrer.

### Le bottleneck visuel

Laissez-moi montrer ce que je veux dire.

Si vous regardez un Gantt chart, vous verrez immédiatement ce qui prend le plus de temps : le développement logiciel. Si votre tâche était d'améliorer le throughput du projet, ce serait votre premier arrêt. Et ce serait correct.

Le problème, cependant, c'est comment les gens s'y prennent typiquement : jeter des gens sur le problème ou supposer que l'IA va rendre les choses bien plus rapides.

Ce que les gens ne font typiquement pas, c'est regarder **pourquoi** ça prend autant de temps, et encore plus important : une longue durée ne signifie pas automatiquement que le problème prend son origine là.

### Résoudre le problème en amont

On parle ici de software dev, mais ça s'applique à tous les process qui prennent plus de temps qu'on ne voudrait.

Tout développeur sait qu'on ne fait pas avancer un projet plus vite en tapant plus vite. Si c'était le cas, on prendrait tous des cours de dactylo.

Le software dev consiste à traduire un problème en une solution qu'un ordinateur peut comprendre et résoudre automatiquement. De préférence d'une manière sûre et scalable.

Pour faire ça, vous avez besoin d'une vue d'ensemble complète du problème. Soit dans des documents de feature ou de scope (si vous êtes plus waterfall), soit avec une itération constante avec les domain experts (plus agile).

C'est souvent la partie qui ralentit le software dev. Essayer de comprendre ce qu'une demande de feature vague, titre uniquement, veut vraiment dire.

Que signifie "envoyer un mail à l'utilisateur quand une vente est terminée" ? Ok, on peut envoyer un mail, mais qu'est-ce qu'il devrait y avoir dans le mail ? Que faire s'il y a eu un problème dans le process de vente, est-ce qu'on envoie quand même un mail d'erreur ? Quand une vente est-elle terminée ?

### Just throw AI at it

Un argument que j'entends sans cesse sur l'automatisation du dev par l'IA, c'est qu'elle peut accélérer la production de code. C'est probablement vrai sur des tâches isolées et bien spécifiées. Mais sur un vrai projet, où la spec est floue et où la moitié du travail est de la clarifier, l'IA ne change pas l'équation. Elle peut même l'aggraver en générant rapidement du code qui ne résout pas le bon problème.

Le vrai gain de productivité vient de meilleures specs, de meilleures conversations avec les domain experts, et d'une discipline d'analyse upstream. Aucun de ces leviers n'est accéléré par un LLM.

### Theory of Constraints

The Goal de Goldratt l'explique très bien : le throughput d'un système est limité par son contrainte la plus serrée. Optimiser ailleurs ne change rien. En software dev, la contrainte est rarement le typing speed des devs.

## Pourquoi ça compte

Un rappel salutaire pour tout COMEX qui pense que l'IA est une baguette magique de productivité. Elle accélère ce qui est déjà clair. Elle n'aide pas à penser.
