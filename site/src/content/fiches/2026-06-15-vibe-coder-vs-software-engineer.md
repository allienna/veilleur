---
title: "Vibe Coder vs Software Engineer"
date: 2026-06-15
url: https://yusufaytas.com/vibe-coder-vs-software-engineer
authors: [Yusuf Aytaş]
keywords: [vibe coding, ownership, time to safe merge, code review, responsabilité]
theme: IA
tone: opinion
used_in: ["2026-06-15"]
---

## Résumé

Yusuf Aytaş reprend une analogie qu'il avait écrite il y a plus de dix ans (« Java Developer vs Software Engineer ») pour distinguer aujourd'hui le *vibe coder* de l'ingénieur logiciel. La différence n'est pas l'outil mais l'endroit où commence et finit la responsabilité. Là où le vibe coder mesure le « time to first working version », l'ingénieur mesure le « time to safe merge ». L'IA produit des complétions, pas des décisions — et une complétion ne peut pas porter le blâme.

## Points clés

- La vraie métrique n'est pas la vitesse de la démo (« time to first demo ») mais le « time to safe merge » : relecture, tests, rollout, rollback, coordination, maintenance future.
- L'output n'est pas le progrès : si l'outil génère plus, l'humain doit contraindre plus, sinon le travail est repoussé en aval.
- L'ownership est la différence clé : un vibe coder peut dire « c'est le modèle qui l'a généré » ; un ingénieur doit dire « je l'assume ».
- Le contexte d'ingénierie vit hors du code (incidents, migrations, conventions, conformité) ; le modèle ne le porte pas comme un humain.
- Mieux vaut réduire l'espace de décision avant de demander du code : être prescriptif suppose de comprendre ce qu'on fait — c'est là que l'expérience prend de la valeur.

## Analyse approfondie

Il y a plus de dix ans, l'auteur écrivait « Java Developer vs. Software Engineer ». Son but : distinguer quelqu'un défini par un langage de quelqu'un qui pense plus largement la résolution de problèmes. Le schéma était : un outil devient puissant, les gens enroulent leur identité autour, et le métier se réduit à l'outil. L'IA n'est pas qu'un langage de plus — elle change l'économie de l'écriture de logiciel — mais le même schéma se rejoue.

La question n'est plus de savoir si l'IA peut écrire du code : elle le fait, de mieux en mieux. La question est : quel type de travail sort de ce processus, et que se passe-t-il quand il entre dans une vraie base de code, avec de vrais utilisateurs, de vraies données, de vraies exigences de conformité, de vrais incidents et de vraies personnes qui doivent la maintenir ? C'est là qu'apparaît la différence entre le vibe coder et l'ingénieur. Le vibe coder veut tester une idée en générant un prototype. L'ingénieur pense l'ensemble du cycle de vie. La différence n'est donc pas l'outil, c'est où commence et finit la responsabilité.

**La mauvaise métrique.** Une grande partie du discours sur le vibe coding mesure la mauvaise chose : la rapidité du passage de l'idée à l'appli. Cela a de la valeur quand le but est de tester une idée. Mais dans une équipe, quelqu'un doit relire, comprendre l'intention, décider si la dépendance a sa place, vérifier que le test valide vraiment le comportement, appliquer les changements de schéma, coordonner entre équipes, préparer un rollback, écrire un runbook, répondre à une alerte. Aucune de ces choses ne fait partie d'un projet jouet. L'auteur mesure donc le travail généré par l'IA autrement : le **time to safe merge** — relecture, qualité des tests, ownership, rollback, capacité de l'auteur à expliquer les décisions importantes. Si l'IA rend la génération moins chère mais le merge sûr plus cher, l'équipe a moins gagné qu'elle ne le croit. C'est la première différence : le vibe coder mesure le time to first working version, l'ingénieur le time to safe merge.

**L'output n'est pas le progrès.** Le code assisté par l'IA doit être meilleur, pas plus gros. Si l'outil permet de générer plus, l'humain doit contraindre plus — sinon on ne fait que déplacer le travail en aval. Le code IA doit atteindre le même niveau que le code écrit à la main : étroit, avec une seule raison d'exister, sans nettoyage non lié, sans reformater la moitié du fichier, sans ajouter un paquet sans explication claire. Si le changement est gros parce que le modèle a trop généré, il faut le découper. Si l'auteur ne peut pas expliquer pourquoi chaque fichier important a changé, ce n'est pas prêt : c'est de l'ownership de base. Deuxième différence : l'unité de travail. Le vibe coder voit l'output généré comme un progrès ; l'ingénieur traite tout changement comme l'unité de responsabilité.

**L'IA ne peut pas porter le blâme.** Relire du code généré n'est pas comme relire du code normal. Quand un humain écrit, il y a une trace de décision — peut-être imparfaite, mais une personne peut expliquer le chemin. Avec du code généré, certaines « décisions » n'en sont pas : ce sont des complétions. Si l'auteur n'a pas converti l'output généré en travail assumé, le relecteur fait deux métiers : relecture et reconstitution de l'intention. L'ownership est la troisième différence : le vibe coder peut dire « le modèle l'a généré » ; l'ingénieur doit dire « je l'assume ». Le code peut commencer avec le modèle, mais la responsabilité ne peut pas y rester.

**Le contexte n'est pas que des fichiers.** Un modèle peut lire beaucoup de code, sans pour autant comprendre le système. Une grande partie du contexte d'ingénierie vit ailleurs : incidents, vieilles migrations, comportement client, douleur opérationnelle, conventions d'équipe, exigences de sécurité, règles de conformité, décisions étranges du passé. Le modèle ne l'a que si on le lui donne, et même alors, il ne le porte pas comme un ingénieur : il travaille dans sa fenêtre de contexte, et plus la tâche est grande, plus il est facile pour lui d'optimiser localement en cassant globalement. D'où le fait que « demande-lui juste de tout réparer » est une mauvaise habitude qui ne marche pas encore. Mieux vaut réduire l'espace de décision avant de demander du code : être plus prescriptif donne de meilleurs résultats — mais cela suppose de comprendre ce qu'on cherche à faire. C'est là que les ingénieurs expérimentés tireront le plus de valeur de l'IA : non en donnant plus de liberté au modèle, mais moins. La liberté est utile pour un week-end de bidouille ; la production exige des contraintes. Quatrième différence : le vibe coder donne un objectif, l'ingénieur donne une tâche bornée. Un bon prompt n'est pas magique — c'est généralement la preuve que l'ingénieur comprend déjà la frontière.

L'article se poursuit en situant le vibe coding dans le processus de livraison : il a sa place, mais pas partout.

## Pourquoi ça compte

Le « time to safe merge » offre un vocabulaire managérial concret pour piloter la qualité à l'ère de l'IA, et recentre la discussion sur l'ownership — exactement la couche que l'automatisation ne sait pas assumer.
