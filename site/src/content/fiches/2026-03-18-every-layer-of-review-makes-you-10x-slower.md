---
title: "Every layer of review makes you 10x slower"
date: 2026-03-18
url: https://apenwarr.ca/log/20260316
authors: [Avery Pennarun]
keywords: [code review, approbation, wall-clock time, bottleneck, bureaucratie]
theme: Leadership
tone: opinion
used_in: ["2026-03-18"]
---

## Résumé

Avery Pennarun, CEO de Tailscale, démontre que chaque couche d'approbation dans un processus de livraison multiplie le temps de cycle par un facteur 10. Un bug fix de 30 minutes devient 5 heures avec une code review, une semaine avec un design doc, un trimestre si une coordination inter-équipes est nécessaire. L'IA ne peut pas résoudre ce problème parce que le goulot d'étranglement n'est pas l'écriture du code.

## Points clés

- Chaque couche d'approbation multiplie le wall-clock time par un facteur ~10x
- Progression type : bug fix 30min → code review 5hrs → design doc 1 semaine → coordination inter-équipes 1 trimestre
- Le temps ajouté n'est pas du travail actif — c'est du temps d'attente dans des files d'attente humaines
- L'IA ne résout pas ce problème car le bottleneck n'est pas l'écriture de code mais les processus d'approbation
- La multiplication exponentielle signifie que 4 couches d'approbation transforment une tâche de 30 minutes en projet de 3 mois

## Analyse approfondie

Avery Pennarun, cofondateur et CEO de Tailscale, propose une loi empirique simple mais dévastatrice : chaque couche de revue ou d'approbation dans un processus de développement logiciel multiplie le temps de livraison par un facteur d'environ 10.

### L'échelle exponentielle

L'observation part d'un cas concret, familier à tout développeur :

- **Bug fix** : 30 minutes. Le développeur identifie le problème, écrit le correctif, le teste localement. Le travail technique est fait.
- **Code review** : 5 heures. Le correctif doit être soumis en pull request, un reviewer doit être disponible, lire le contexte, comprendre le changement, faire des commentaires, attendre les réponses, approuver. Même si le travail de revue ne prend que 15 minutes, le wall-clock time explose à cause des files d'attente et des changements de contexte.
- **Design doc** : 1 semaine. Si le changement est jugé suffisamment important pour nécessiter un document de design, il faut le rédiger, le faire circuler, recueillir les commentaires de plusieurs parties prenantes, itérer, obtenir l'approbation. Chaque intervenant a son propre emploi du temps et ses propres priorités.
- **Coordination inter-équipes** : 1 trimestre. Si le changement touche plusieurs équipes, il faut aligner les roadmaps, planifier dans les sprints respectifs, négocier les priorités, gérer les dépendances. On entre dans le temps organisationnel, mesuré en semaines et en mois.

### Pourquoi le facteur est de 10x et non de 2x

Le multiplicateur n'est pas linéaire parce que chaque couche n'ajoute pas simplement du travail — elle ajoute de l'attente. Le travail de revue proprement dit peut être court, mais le temps entre la soumission et le début de la revue, entre les commentaires et les réponses, entre la demande de changements et la re-soumission, ces temps morts s'accumulent.

Chaque personne impliquée dans le processus a ses propres priorités, ses propres réunions, ses propres urgences. Le changement en attente de revue n'est jamais la priorité numéro un du reviewer. Il attend dans une file, parmi d'autres changements, d'autres tâches, d'autres sollicitations.

### L'IA ne résout pas ce problème

Pennarun souligne que l'enthousiasme actuel pour les agents IA de codage passe complètement à côté de ce problème. L'IA peut écrire le bug fix en 5 minutes au lieu de 30. Elle peut même rédiger le design doc plus vite. Mais elle ne peut pas réduire le temps que le reviewer met à trouver un créneau pour lire la PR. Elle ne peut pas accélérer l'alignement entre équipes qui ont des objectifs différents.

Le goulot d'étranglement n'est pas le temps de production — c'est le temps d'approbation. Et ce temps d'approbation est fondamentalement un problème humain et organisationnel, pas un problème technique.

### Implications organisationnelles

La conclusion implicite est que les organisations qui veulent réellement accélérer leur livraison devraient se concentrer sur la réduction du nombre de couches d'approbation plutôt que sur l'accélération de l'écriture de code. Chaque couche retirée divise le temps par 10. Investir dans la confiance, l'autonomie des équipes et des processus de déploiement plus directs a un effet multiplicateur bien supérieur à n'importe quel outil de codage IA.

## Pourquoi ça compte

Cet article quantifie de manière concrète et mémorable un problème que tout développeur ressent intuitivement. Le facteur 10x par couche est un outil rhétorique puissant pour les engineering managers qui veulent plaider en faveur de processus plus légers — et pour relativiser l'impact réel de l'IA sur la vitesse de livraison.
