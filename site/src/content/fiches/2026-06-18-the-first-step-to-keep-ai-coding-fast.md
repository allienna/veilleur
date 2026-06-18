---
title: "The First Step to Keep AI Coding Fast as Your Project Grows"
date: 2026-06-18
url: https://substack.com/app-link/post?publication_id=3009345&post_id=202444220&isFreemail=true&r=7v5lmc&token=eyJ1c2VyX2lkIjo0NzU1OTI2MjgsInBvc3RfaWQiOjIwMjQ0NDIyMCwiaWF0IjoxNzgxNzI3NjU5LCJleHAiOjE3ODQzMTk2NTksImlzcyI6InB1Yi0zMDA5MzQ1Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.AGX301-IpAP4uMyiuB_z91CaEJK4iH0hZm4DHAcgIuc
authors: [Nir Diamant]
keywords: [SDD, specification driven development, AI coding, discipline d'ingénierie, scaling]
theme: IA
tone: tutorial
used_in: ["2026-06-18"]
---

## Résumé

Nir Diamant décrit une courbe que presque tout développeur codant avec l'IA finit par toucher : la première feature prend dix minutes, la cinquième prend deux jours parce que l'IA casse ce qui marchait déjà. La cause n'est pas un modèle devenu moins bon, mais le fait de demander à l'IA de suivre un plan qui n'existe que dans votre tête. La réponse est le Specification Driven Development (SDD) : écrire la spec avant le code, donner à l'IA un contrat écrit (où vont les fichiers, quels patterns suivre, ce que « terminé » veut dire) plutôt que des demandes une phrase à la fois. La spec n'est que le premier geste d'une vraie discipline d'ingénierie — pas la totalité du métier.

## Points clés

- La courbe de ralentissement est normale : à mesure que le projet prend forme, « fais quelque chose de bien » ne suffit plus, car l'IA ne voit pas les décisions jamais écrites.
- Les bons développeurs donnent à l'IA *plus de limites*, pas plus de liberté, à mesure que le projet grandit.
- SDD = écrire la spec avant le code ; toute l'industrie va dans ce sens (GitHub Spec-Kit, Amazon Kiro, ou à la main avec Cursor/Claude Code).
- Une spec peut être un simple fichier `specs.md` en phrases normales : quoi construire, où vont les données, quels patterns réutiliser, ce que « terminé » signifie.
- Les erreurs coûtent selon leur place : une mauvaise ligne coûte une ligne, un mauvais plan coûte cent lignes, une mauvaise compréhension coûte la feature entière.
- Savoir quand « vibe-coder » (jetable, prototype) et quand « specifier » (production, ce dont d'autres dépendent) est la vraie compétence.

## Analyse approfondie

> *(Le billet est précédé d'une annonce commerciale pour un cours « Prompt to Production » et une liste d'attente, écartée ici : seule la partie blog sur le SDD est traduite.)*

**Votre première feature a volé. Votre cinquième a rampé.** Voici la courbe que tout codeur IA finit par toucher, et le premier geste qui la fait redescendre.

Votre première feature a pris dix minutes. Vous avez écrit une phrase, l'IA a écrit le code, et ça marchait. Vous vous êtes senti·e imbattable. Puis vous avez ajouté une cinquième feature, et elle a pris deux jours. L'IA n'arrêtait pas de casser ce qui marchait déjà. Chaque correctif créait un nouveau bug ailleurs. Le démarrage rapide avait disparu.

Ce ralentissement n'est pas votre faute, et le modèle n'est pas devenu moins bon. C'est une courbe normale, que presque tout développeur rencontre.

### La première feature ressemblait à de la magie

Au début, le projet est vide. Pas d'autres features à casser, pas de patterns à suivre, pas de décisions passées à respecter. Une phrase suffit. Pensez à un constructeur posant un simple abri dans un champ vide : pas de voisins, pas de fondation à raccorder, pas de tuyaux à contourner. Vous dites « fais-le bien » et il le peut. L'instruction est courte parce que le travail est petit. Tout le monde adore cette partie — elle cache aussi ce qui vient après.

### Pourquoi la courbe arrive

À la cinquième feature, votre projet a une forme : une structure, des conventions de nommage, des décisions prises trois features plus tôt que le nouveau code doit respecter. Le champ vide est devenu une maison avec des tuyaux dans les murs. « Fais-le bien » ne suffit plus. Le constructeur ne voit pas les tuyaux, alors il les perce. L'IA ne voit pas les décisions que vous n'avez jamais écrites, alors elle les casse. Le modèle n'échoue pas : vous lui demandez de suivre un plan qui n'existe que dans votre tête.

### Ce que font les bons développeurs

Voici la différence entre ceux qui livrent et ceux qui s'enlisent. Les bons développeurs ne donnent pas à l'IA *plus de liberté* à mesure que le projet grandit. Ils lui donnent *plus de limites*. La liberté est ce qui fait percer les tuyaux. Une limite, c'est l'inverse : une règle écrite que l'IA ne peut pas franchir. Où vont les fichiers. Quels sont les patterns de nommage. Quelles décisions passées sont fixes. Les écrire paraît plus lent pour une feature. C'est bien plus rapide sur cinquante.

### Specification Driven Development, en clair

Cette idée a maintenant un nom, et elle grandit vite. Le *specification driven development* signifie écrire la spec avant le code, l'IA construisant contre la spec plutôt que contre une demande d'une ligne. Toute l'industrie va dans ce sens : GitHub a sorti un kit appelé Spec-Kit, Amazon a intégré l'idée dans un outil appelé Kiro, et les utilisateurs de Cursor et Claude Code le font à la main. Outils différents, même idée : arrêter de décrire ce qu'on veut une phrase à la fois, et donner à l'IA un contrat écrit qu'elle doit suivre.

Une spec n'est pas un long document. La version la plus simple est un fichier que l'IA lit à chaque fois, avant d'écrire quoi que ce soit. Il dit ce que vous construisez, où vont les choses, les patterns à suivre, et ce que « terminé » veut dire. Pas besoin d'outil lourd : ouvrez un fichier `specs.md` et décrivez le travail en phrases normales. Ce que vous construisez : comptes email/mot de passe. Où vont les données : la table `users` existante, pas une nouvelle. Quels patterns réutiliser : le même flux de login et de session que l'app a déjà. Nommer les nouvelles fonctions comme le code voisin. Quelques lignes simples, écrites avant tout code, et l'IA construit contre elles au lieu d'inventer sa propre version.

### La même feature, deux manières

Imaginez un lundi : vous ajoutez les comptes utilisateurs.

*La manière « demande »* : vous écrivez « ajoute le login ». L'IA invente une nouvelle façon de stocker les utilisateurs, ignore la structure de base de données posée la semaine dernière, et nomme tout différemment du reste du code. Ça paraît bien à l'écran. Puis deux anciennes features tombent en panne, car elles attendaient l'ancienne structure. Vous passez l'après-midi à chercher quel changement a cassé quoi, et l'IA propose des correctifs qui cassent une troisième chose.

*La manière « spec »* : vous passez dix minutes d'abord. Vous ouvrez `specs.md` et écrivez ce que « terminé » signifie pour le login. Une personne peut s'inscrire, se connecter, se déconnecter, et rester connectée après un rafraîchissement. Puis vous pointez l'IA vers le fichier et la laissez construire. Elle construit dans les limites. Elle réutilise votre structure de base de données, parce que vous lui avez dit où elle est. Elle respecte vos noms, parce qu'ils sont écrits. Rien d'autre ne casse, parce que les limites ont dit quoi laisser tranquille. L'après-midi reste libre.

Même modèle, même feature, même développeur. La seule différence : dix minutes passées au départ.

### Là où les erreurs coûtent le plus

Une erreur coûte des montants très différents selon l'endroit où elle survient. Une mauvaise ligne de code vous coûte une mauvaise ligne. Un mauvais plan coûte cent lignes bâties dessus. Une mauvaise compréhension du problème coûte la feature entière, parfois le week-end entier. Les erreurs les moins chères à corriger sont près du clavier. Les chères sont en amont, dans la réflexion qu'on a sautée. Une spec déplace votre attention vers l'amont, là où une bonne décision protège les cent décisions en dessous. Vous ne payez pas dix minutes pour en économiser dix : vous payez en haut, ou vous payez en bas, un bug à la fois, pour le reste du projet.

### Quand « vibe-coder », quand « specifier »

Rien de tout cela ne rend mauvaise la manière rapide d'une seule phrase. C'est le bon outil pour le bon travail ; la compétence est de savoir lequel est lequel. *Vibe* quand refaire est moins cher que planifier : scripts jetables, prototypes, un test rapide que vous supprimerez demain. C'est l'abri dans le champ vide, et la vitesse y est réelle. *Spec* quand une erreur grandit : tout ce qui est en production, ce dont d'autres dépendent, tout ce qui est plus grand qu'une seule séance. Le test honnête tient en une question : si ça tourne mal, est-ce que je le jette, ou est-ce que je dois l'extraire de tout le reste ? « Jeter » = vibe. « Extraire » = spec.

### Ce qu'une spec ne réglera pas

L'image de la maison est utile mais imparfaite. Le code n'est pas du béton : on change un mur en logiciel bien plus facilement, et une bonne spec se met à jour quand on apprend quelque chose. Traitez la spec comme un plan que vous gardez à jour, pas un design figé. Une spec n'est pas non plus un bouclier : elle ne transformera pas une idée vague en bon produit, et ne vous sauvera pas de construire la mauvaise chose avec soin. Si vous ne comprenez pas le problème, une spec propre ne fait que vous aider à construire la mauvaise réponse plus vite. Et une spec qui se périme se remplit lentement d'affirmations qui ne sont plus vraies, que l'IA suit ensuite jusqu'au bug.

### Là où commence le métier

Les développeurs qui prennent de l'avance avec l'IA ne sont pas ceux qui ont les prompts les plus malins. Ce sont ceux qui ont cessé de donner une demande d'une ligne et commencé à donner un plan écrit. Une spec n'est toutefois que le premier geste, pas tout le métier. Un plan ne fait pas monter la maison tout seul : il faut encore une structure solide, de vrais tests, une revue soignée, et une façon sûre de livrer. La spec est là où la discipline commence, pas là où elle finit.

## Pourquoi ça compte

Le SDD nomme et systématise un réflexe d'ingénierie qui distingue ceux qui livrent durablement avec l'IA de ceux qui s'enlisent : déplacer l'effort vers l'amont, en écrivant le contrat avant de coder. Un repère concret et actionnable pour des équipes qui passent du prototype « vibe-codé » à des produits de qualité production.
