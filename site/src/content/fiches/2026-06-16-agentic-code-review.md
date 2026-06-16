---
title: "Agentic Code Review"
date: 2026-06-16
url: https://addyosmani.com/blog/agentic-code-review/?utm_source=tldrnewsletter
authors: [Addy Osmani]
keywords: [agentic engineering, code review, trust, coding agents, leverage]
theme: IA
tone: opinion
used_in: ["2026-06-16"]
---

## Résumé

Addy Osmani soutient que les agents de codage sont devenus extraordinairement bons et progressent vite, ce qui déplace la partie difficile de l'ingénierie : non plus écrire le code, mais décider si l'on peut lui faire confiance. La revue de code devient ainsi la compétence la plus à fort levier du moment. Sa thèse centrale est que l'approche dépend entièrement de qui vous êtes : un développeur solo sans utilisateurs et une équipe maintenant une application vieille de dix ans ne résolvent pas le même problème. Les mêmes outils qui génèrent tout ce code supplémentaire sont aussi le meilleur moyen de suivre le rythme.

## Points clés

- Les agents de codage sont aujourd'hui réellement bons et s'améliorent chaque mois.
- La partie difficile est passée de l'écriture du code à la décision de lui faire confiance.
- La revue de code marchait grâce à un accident : un senior lisait plus vite qu'un junior n'écrivait — ce n'est plus vrai.
- Le goulot d'étranglement s'est déplacé vers la seule étape qui n'a pas accéléré : être confiant que le changement est correct.
- La bonne approche dépend du contexte : side-project vs système d'entreprise vieux de dix ans.
- Les agents (Claude Code, Codex) servent aussi à trier les PR entrantes — l'IA aide à relire l'IA.

## Analyse approfondie

Les agents de codage sont extraordinairement bons maintenant, et s'améliorent rapidement. La conséquence intéressante est que la partie difficile de l'ingénierie est passée de l'écriture du code à la décision de lui faire confiance — ce qui fait de la revue la compétence la plus à fort levier en software aujourd'hui. La manière de l'aborder dépend énormément de qui vous êtes : un développeur solo sans utilisateurs et une équipe maintenant une application vieille de dix ans ne résolvent pas le même problème.

L'auteur se dit plus optimiste que jamais sur l'ingénierie agentique. Les agents sont réellement bons, ils progressent chaque mois, et au quotidien il livre désormais des choses qu'il n'aurait pas tentées un an plus tôt. Son texte est une carte de l'endroit où le travail intéressant s'est déplacé — car il s'est bien déplacé, et la plupart des équipes n'ont pas encore rattrapé ce mouvement.

La revue de code fonctionnait grâce à un heureux accident de vitesse relative. Un ingénieur senior pouvait lire le code plus vite qu'un junior ne l'écrivait, donc la revue suivait le rythme sans que personne ne l'ait conçue ainsi, et l'équipe absorbait la façon dont le système s'assemblait comme effet secondaire de la lecture des diffs des autres. Beaucoup de cela n'était pas délibéré : cela découlait d'un seul fait — écrire du code était la partie lente et coûteuse, le lire était rapide et bon marché.

Ce fait ne tient plus. Un agent produira mille lignes de code souvent solide et bien formaté en moins de temps qu'il n'en faut pour lire un paragraphe, alors que la vitesse de lecture d'un humain n'a pas changé depuis le jour où nous avons commencé à fixer des écrans pour gagner notre vie. La contrainte s'est donc déplacée en aval, vers la seule étape qui n'a pas accéléré : une personne étant confiante que le changement est correct. Ce n'est pas une perte, dit-il : c'est l'endroit le plus à fort levier où être bon aujourd'hui, et c'est là qu'il a concentré son attention cette année.

Il y a une heureuse torsion : les mêmes outils qui génèrent tout ce code supplémentaire sont aussi le meilleur moyen de suivre le rythme. Sur ses propres projets, y compris des projets open-source populaires, il pointe désormais Claude Code ou Codex sur un lot de PR entrantes et leur fait trier la file — ce qui a réellement changé sa façon d'occuper son temps. Ce n'est donc pas un argument anti-IA.

Ce n'est pas non plus un énième débat sur le fait de savoir si laisser un modèle écrire votre code est merveilleux ou la fin de l'artisanat, car ce cadrage est inutile. La seule réponse qui survit au contact d'une vraie base de code est que cela dépend entièrement de qui vous êtes. Un développeur qui « vibe-code » un side-project utilisé par une douzaine de personnes, et une équipe gardant en vie un système d'entreprise vieux de dix ans pour un trimestre de plus, ne partagent presque aucune contrainte commune, et la plupart des conseils en circulation reviennent à l'un de ces deux profils expliquant à l'autre comment vivre.

## Pourquoi ça compte

Cette analyse cristallise le glissement de fond de 2026 : dans un monde où le code est abondant et bon marché, la valeur d'un ingénieur se concentre sur le jugement et la revue, devenus le point le plus stratégique de toute la chaîne de livraison.
