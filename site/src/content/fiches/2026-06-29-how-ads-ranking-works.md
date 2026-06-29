---
title: "How Ads Ranking Works: The Data System Behind Every Ad You See"
date: 2026-06-29
url: https://substack.com/redirect/b7c9b0ca-8a46-4796-b73e-7b7c7631aff9?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [DataStrata]
keywords: [ads ranking, ML, funnel, pCTR, auction, latence]
theme: Data
tone: tutorial
used_in: ["2026-06-29"]
---

## Résumé

DataStrata décortique le système de données derrière chaque publicité affichée : en moins de 100 ms, il faut évaluer des millions de candidats, faire tourner des modèles ML, tenir une enchère et désigner un gagnant. La solution est un entonnoir à trois étages qui arbitre rappel (ne pas rater une bonne pub) contre latence. Les étages sont progressivement plus précis et plus coûteux : filtrage booléen déterministe, puis ranking léger (GBDT), puis ranking lourd (deep learning) suivi d'une enchère au second prix pondérée par la qualité.

## Points clés

- Le problème : une seule slot, des millions de candidats, moins de 100 ms — impossible de faire tourner un modèle lourd sur chaque candidat.
- Étage 1, Selection : pur filtrage booléen (géo, démo, budget, segment, format, frequency cap). « L'éligibilité est déterministe et binaire ; la qualité est probabiliste et continue. Confondre les deux est une erreur de design. »
- Étage 2, Light Ranking : un GBDT (XGBoost/LightGBM) sur features pré-calculées élague les perdants évidents — le débit prime sur la précision, le rappel sur la précision.
- Étage 3, Heavy Ranking : un réseau profond (type DLRM de Meta) calcule un pCTR précis sur le jeu de features temps réel complet.
- L'enchère : généralisée au second prix avec multiplicateur de qualité — `Total Value = bid × pCTR × quality_score`. La plus forte valeur totale gagne, pas la plus forte enchère.

## Analyse approfondie

À chaque fois que vous faites défiler une publicité, un système a pris une décision en moins de 100 millisecondes. Il a évalué des millions de candidats, fait tourner des modèles de machine learning, tenu une enchère, et choisi un gagnant. Voici comment ça marche — du point de vue ingénierie et données que la plupart des explications passent sous silence.

### Le problème central

Imaginez que vous opérez une plateforme publicitaire. À tout instant, il y a des millions de pubs qui *pourraient* s'afficher pour un utilisateur. Vous avez une seule slot. Et vous avez moins de 100 millisecondes pour décider. Vous ne pouvez pas faire tourner un modèle ML lourd sur chaque candidat. Vous ne pouvez pas faire de jointures complexes sur des millions de lignes en temps réel. Alors comment faire ? La réponse est un entonnoir.

### L'entonnoir à trois étages

Chaque étage arbitre deux choses : le **rappel** (ne pas rater une excellente pub) contre la **latence** (impossible d'être lent). L'entonnoir devient progressivement plus précis et plus coûteux.

### Étage 1 : Selection — qui peut légalement enchérir ?

La sélection n'a rien à voir avec le ML. C'est du pur filtrage — des vérifications booléennes rapides qui éliminent les pubs non éligibles en quelques millisecondes. Une pub est éliminée si :

- **Ciblage géographique** — l'annonceur a dit « US only », l'utilisateur est en France.
- **Ciblage démographique** — la pub cible les 25-34 ans, l'utilisateur a 55 ans.
- **Budget épuisé** — plafond de dépense quotidien atteint.
- **Segment d'audience** — la pub cible les « amateurs de randonnée », l'utilisateur n'a aucun signal rando.
- **Mismatch de format** — pub vidéo dans un emplacement statique uniquement.
- **Frequency cap** — l'utilisateur a déjà vu cette pub 10 fois aujourd'hui.

**La sélection répond à : « cette pub est-elle éligible ? » Le ranking répond à : « cette pub doit-elle gagner ? »** Ce sont deux questions très différentes, et les confondre est une erreur de design. L'éligibilité est déterministe et binaire. La qualité est probabiliste et continue.

### Étage 2 : Light Ranking — approximation rapide

Le ranking léger prend des milliers de candidats éligibles et les réduit à des centaines. Il ne choisit pas un gagnant — il élimine les perdants évidents. La vitesse est la contrainte : le modèle doit scorer des milliers de candidats en quelques millisecondes. Cela implique :

- **Features pré-calculées uniquement** — CTR historique mis en cache pour la pub, buckets larges de catégories utilisateur. Aucun calcul temps réel.
- **Modèle peu profond** — typiquement un Gradient Boosted Decision Tree (GBDT) type XGBoost ou LightGBM. Inférence rapide par lookups d'arbres if/else. Pas de calcul matriciel, pas de normalisation.

Pourquoi un GBDT plutôt qu'un réseau de neurones ici ? Parce qu'à cet étage, **le débit prime sur la précision**. Le ranker lourd s'occupe de la précision. Le rappel compte plus que la précision : rater une excellente pub est pire que laisser passer une pub médiocre — le modèle lourd fera le ménage.

### Étage 3 : Heavy Ranking + enchère — précision et pricing

C'est là que se fait le vrai travail ML, et où vit l'essentiel de l'investissement ML. Le **Heavy Ranking** prend les centaines de survivants et attribue à chacun un score de qualité précis via : le jeu de features temps réel complet (comportement de session courant, embeddings profonds de la pub, cross-features utilisateur×pub), une architecture deep learning (par ex. le DLRM de Meta), avec pour sortie principale le **pCTR** — la probabilité prédite qu'un utilisateur clique sur cette pub.

### L'enchère : ce n'est pas la plus forte enchère qui gagne

C'est la partie que la plupart des gens comprennent de travers. Les enchères publicitaires chez Meta et Google sont des **enchères généralisées au second prix avec un multiplicateur de qualité** :

```
Total Value = bid × pCTR × quality_score
```

La pub avec la **plus forte valeur totale gagne** — pas la plus forte enchère. Cela compte pour trois raisons : (1) une pub à enchère plus basse mais de haute qualité peut battre une pub à enchère haute mais de basse qualité ; (2) les annonceurs sont incités à bien cibler et à écrire de bons créatifs, car une pub de haute qualité a un coût par impression effectif plus bas ; (3) le gagnant paie au second prix — juste assez pour battre la valeur totale du second, divisée par sa propre qualité. **Prix de réserve :** si aucune pub ne franchit un seuil minimal de qualité/valeur, aucune pub ne s'affiche. Mieux vaut ne rien montrer qu'une mauvaise pub — cela protège la confiance des utilisateurs sur le long terme.

### pCTR — le problème ML central

Le Predicted Click-Through Rate est la probabilité qu'un utilisateur clique sachant qu'il voit la pub. C'est un modèle de classification binaire calibré. La calibration importe : la sortie brute du modèle est un score, pas une probabilité. Il faut la calibrer contre les taux de clic historiques avant de la brancher dans la formule d'enchère — un pCTR non calibré casse les maths de l'enchère.

## Pourquoi ça compte

C'est l'illustration parfaite d'une discipline d'ingénierie qu'on oublie à l'ère du « tout-LLM » : on ne lance pas le modèle coûteux sur tout. On filtre d'abord avec du déterministe pas cher, on n'escalade vers le ML lourd que sur les survivants. Cheap-before-expensive, éligibilité avant qualité.
