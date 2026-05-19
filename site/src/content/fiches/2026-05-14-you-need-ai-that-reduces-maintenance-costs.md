---
title: "You Need AI That Reduces Maintenance Costs"
date: 2026-05-14
url: https://leadershipintech.com/links/22284/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [James Shore, jamesshore.com]
keywords: [maintenance costs, AI coding, productivity, technical debt, software engineering]
theme: Leadership
tone: opinion
used_in: ["2026-05-14"]
---

## Résumé

James Shore pose une équation brutale : si ton agent IA double ta vitesse d'écriture mais ne divise pas par deux ta dette de maintenance, tu échanges un boost temporaire contre une servitude permanente. À coûts de maintenance "normaux", une équipe passe sous 50 % de productivité en 31 mois. Si tu doubles la maintenance — ce qui arrive typiquement quand on génère du code en masse sans discipline — tu atteins ce seuil en 10 mois.

## Points clés

- Chaque ligne de code écrite doit être maintenue : bugs, cleanup, mises à jour de dépendances
- Une enquête type "wisdom of the crowd" estime ~10 jours de maintenance la première année par mois d'écriture, ~5 jours/an ensuite
- Au régime "normal" : 50 % de productivité atteint en 31 mois
- En cas de doublement des coûts de maintenance : 50 % atteint en 10 mois
- En cas de division par deux : 50 % atteint en 68 mois
- L'IA doit réduire la maintenance autant qu'elle augmente la vitesse d'écriture

## Analyse approfondie

J'irai droit au but : ton agent IA, celui que tu utilises pour écrire du code, doit réduire tes coûts de maintenance. Et pas de peu. Tu écris du code deux fois plus vite ? J'espère pour toi que tu as divisé par deux tes coûts de maintenance. Trois fois plus productif ? Un tiers des coûts de maintenance. Sinon, t'es fichu. Tu échanges un boost de vitesse temporaire contre une servitude permanente.

Tu veux savoir pourquoi ? Allez, on prend la route. Sur un highway désert dans la nuit...

### La productivité est déterminée par les coûts de maintenance

Chaque ligne de code que tu écris doit être maintenue : correctifs de bugs, nettoyages, mises à jour de dépendances, etc. Je ne parle pas des nouvelles features ou des améliorations. Juste de la maintenance. Pour chaque mois passé à écrire du code, tu passeras du temps l'année suivante à le maintenir, et un peu chaque année après ça, pour toujours, tant que ce code existera.

Si tu interrogeais une cinquantaine de développeurs sur ces coûts de maintenance, via une technique de "wisdom of the crowd", tu aurais une estimation raisonnablement précise.

Tu obtiendrais probablement quelque chose comme :
- 10 jours de maintenance la première année, pour chaque mois d'écriture
- 5 jours par an ensuite

Avec ces hypothèses dans un tableur, tu obtiens une courbe nette : le pourcentage de temps consacré à du travail à valeur ajoutée chute rapidement les premiers mois, puis continue de décroître pendant des années.

### Les chiffres clés

- Au régime "normal", une équipe atteint moins de 50 % de productivité au bout de **31 mois**
- En cas de coûts de maintenance divisés par deux : **68 mois**
- En cas de coûts doublés : **10 mois**

Le premier mois d'un nouveau projet est glorieux. Tu passes tout ton temps à construire de chouettes nouvelles features. Le mois suivant l'est un peu moins. Une fraction du temps part en maintenance. Trois ans plus tard, tu y passes la moitié de ton temps.

### Ce que ça change quand on parle d'IA

L'argument central de Shore : tout le marketing autour des coding agents parle de vitesse. Personne ne parle de la trajectoire long terme.

Pourquoi est-ce critique ? Parce que le code écrit vite mais peu compris :
- Devient plus dur à débugger (l'auteur ne se souvient pas pourquoi telle décision a été prise)
- A plus de duplication (l'agent ne sait pas qu'une fonction existait déjà)
- Repose sur des patterns mal adaptés au domaine
- Crée des dépendances entre modules que personne ne suit

Donc l'IA, mal cadrée, **augmente** mécaniquement le coût de maintenance. Pour que la productivité globale monte, il faut que le gain d'écriture compense ce surcoût ET le réduise.

### Ce qu'il faut exiger d'un agent IA

- Qu'il refactorise autant qu'il génère
- Qu'il génère des tests qui survivent au refactor
- Qu'il documente ses choix de design
- Qu'il consolide les patterns au lieu d'en empiler

Sans ça, ce que tu gagnes en mois 1 tu le repaies en mois 18 avec intérêts.

## Pourquoi ça compte

C'est l'un des contre-récits les plus solides face à l'évangile "AI productivity". Pour un engineering director, c'est un cadrage indispensable des objectifs à donner aux équipes qui adoptent Copilot ou Claude Code : pas seulement "code plus vite", mais "réduis la maintenance de ce que tu codes".
