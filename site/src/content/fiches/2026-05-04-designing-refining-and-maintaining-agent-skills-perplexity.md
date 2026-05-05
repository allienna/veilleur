---
title: "Designing, Refining, and Maintaining Agent Skills at Perplexity"
date: 2026-05-04
url: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity?utm_source=tldrai
authors: [Perplexity Agents Team]
keywords: [agent skills, perplexity, zen of skills, context engineering, progressive disclosure]
theme: IA
tone: tutorial
used_in: ["2026-05-04"]
---

## Résumé

L'équipe Agents de Perplexity publie le guide qu'elle utilise en interne pour designer, reviewer et maintenir des Agent Skills. Sa thèse principale : écrire un Skill, ce n'est pas écrire du logiciel classique, c'est construire du contexte pour des modèles. Les patterns qui font du bon code Python deviennent des antipatterns en Skill creation. L'article propose un "Zen of Skills" inversant point par point le PEP 20 — la complexité devient feature, l'implicite remplace l'explicite, la densité prime sur la sparsité, les cas particuliers sont l'or du Skill, et tout ce qui est facile à expliquer doit être supprimé parce que le modèle le sait déjà. Perplexity utilise ces Skills sur des cas verticaux (finance, droit, santé) et des utilitaires généraux pour Perplexity Computer.

## Points clés

- Un Skill, c'est un dossier (pas un fichier), parce que la complexité y est une feature et pas un bug
- L'activation d'un Skill se fait par pattern matching implicite et progressive disclosure
- Le contexte est cher : maximiser le signal par token, densité plutôt que sparsité
- Les cas particuliers ("gotchas") sont le contenu de plus haute valeur — c'est là que le modèle se trompe par défaut
- Si une implémentation est facile à expliquer, le modèle la connaît déjà : il faut la supprimer du Skill
- Les Skills sont review avec autant de rigueur que le code applicatif chez Perplexity
- Beaucoup de PRs venant d'excellents ingénieurs reçoivent de nombreux commentaires parce que les bons patterns de code deviennent des antipatterns en Skill

## Analyse approfondie

Les produits agentiques de pointe de Perplexity reposent sur une fondation de savoir-faire et d'expertise métier packagés dans des Agent Skills modulaires. Nous maintenons une bibliothèque de Skills soigneusement curée à travers nos environnements techniques. Ces Skills incluent beaucoup d'utilitaires généraux qui font tourner Perplexity Computer ; des capacités verticales spécifiques en finance, droit, santé ; et une longue traîne de modules pour répondre à des besoins utilisateurs. Certains Skills sont rarement invoqués mais critiques *quand* ils le sont. Pour assurer une qualité d'expérience constante, l'équipe Agents de Perplexity priorise la qualité des Skills autant que la qualité du code.

Les intuitions et bonnes pratiques requises pour développer un Skill de qualité diffèrent significativement de celles requises pour construire du logiciel traditionnel. L'équipe Agents review beaucoup de pull requests d'excellents ingénieurs qui développent des Skills dans le cadre de leur travail. Le résultat est presque toujours de nombreux commentaires et suggestions de révision. C'est parce que beaucoup de patterns utiles pour écrire du code deviennent des antipatterns en création de Skills.

Par exemple, si on prend certains aphorismes du Zen of Python (PEP 20), il devient vite clair qu'écrire du bon code Python est différent d'écrire de bons Skills. Sur 20 lignes de sagesse, au moins la moitié sont fausses ou activement trompeuses quand on écrit des Skills. En voici cinq :

| **Zen of Python** | **Zen of Skills** |
| --- | --- |
| Simple is better than complex | A Skill is a folder, not a file. Complexity is the feature. |
| Explicit is better than implicit | Activation is implicit pattern matching. Progressive disclosure. |
| Sparse is better than dense | Context is expensive. Maximum signal per token. |
| Special cases aren't special enough to break the rules | Gotchas ARE the special cases (they're the highest-value content). |
| If the implementation is easy to explain, it may be a good idea | If it's easy to explain, the model already knows it. Delete it. |

Ce guide est le document utilisé par les ingénieurs à travers Perplexity quand ils développent et reviewent des Skills. Nous le rendons aussi public pour que nos découvertes et apprentissages bénéficient à la communauté plus large. Que tu sois un ingénieur designant des Skills de production au quotidien, un utilisateur de Computer cherchant à développer ton propre Skill dans un domaine que tu connais, ou les deux, ce guide est pour toi.

### Qu'est-ce qu'un Skill ?

Quand tu écris un Skill, tu n'écris pas du logiciel ordinaire (même si les Skills sont maintenant une partie des moteurs logiques principaux des systèmes agentiques). Tu construis plutôt du contexte pour des modèles et leurs environnements. Un Skill a des contraintes différentes et des principes de design différents. Si tu écris un Skill comme tu écrirais un module Python, tu vas probablement faire des choix qui semblent corrects mais qui dégradent la qualité du Skill.

La logique derrière le Zen of Skills :

- **A Skill is a folder, not a file** — la complexité est la feature parce qu'un Skill encapsule un domaine entier de connaissances activables, pas une fonction unique
- **Activation is implicit pattern matching** — le modèle décide d'activer un Skill basé sur des signaux implicites dans le prompt, donc l'explicite (cas typique en code) ne s'applique pas
- **Maximum signal per token** — chaque token dans le contexte coûte du compute et de la latence, donc la densité importe plus que la lisibilité humaine
- **Gotchas ARE the special cases** — c'est là que le modèle se trompe par défaut, donc c'est là que ton Skill apporte le plus de valeur
- **If it's easy to explain, the model already knows it. Delete it.** — n'écris pas dans le Skill ce que le modèle est entraîné à connaître ; écris ce qu'il ne saurait pas autrement

## Pourquoi ça compte

Avec le post d'Addy Osmani, c'est l'un des deux articles fondateurs de la "discipline Skills" qui se met en place en 2026. Particulièrement précieux parce qu'il vient d'une équipe qui design et maintient des Skills en production depuis longtemps, à grande échelle, sur des domaines verticaux exigeants.
