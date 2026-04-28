---
title: "Welcome to the \"find out\" stage of AI"
date: 2026-04-28
url: "https://stackoverflow.blog/2026/04/27/welcome-to-the-find-out-stage-of-ai/"
authors: ["Stack Overflow Blog", "Ryan Donovan"]
keywords: [agents, trust, production AI, evals, ROI]
theme: "IA"
tone: "opinion"
used_in: ["2026-04-28"]
---

## Résumé

Ryan Donovan, sur le blog de Stack Overflow, dresse le bilan d'un an d'évolution de l'IA en production. Après une phase d'expérimentation où tout le monde testait sans pression, on entre dans la phase "find out" : les agents doivent fonctionner, livrer du ROI mesurable, et gagner la confiance des utilisateurs et des entreprises. La performance des modèles n'est plus le facteur limitant — c'est la confiance, les évaluations, et la capacité à intégrer ces systèmes dans des contextes à fort enjeu.

## Points clés

- En janvier 2025, à HumanX, les agents étaient encore une tech vague ; un an plus tard, le langage a changé : "inflection point", "second phase"
- Les LLMs ne tournent plus en mode call-and-response, ils sont équipés de tooling, d'automation, d'évals et formalisés en agents
- Le facteur limitant de la prochaine phase n'est plus la performance des modèles, mais la confiance
- Dans les secteurs régulés (santé, droit, énergie), les erreurs ont des conséquences réelles, ce qui change radicalement le mindset de déploiement
- La justification du token spend est désormais centrale : les clients exigent des résultats tangibles

## Analyse approfondie

### Du "bottom of the first inning" à l'inflection point

Quand Ryan Donovan s'est rendu à la première conférence HumanX en janvier 2025, les agents étaient une tech frontière mal définie. C'est là qu'il a entendu pour la première fois les lettres MCP. Les grandes conversations tournaient autour de l'inférence, des hallucinations, et du retrieval augmented generation. La techno semblait neuve — Tomasz Tunguz de Theory Ventures parlait du "bottom of the first inning" (début de la première manche). Toutes les entreprises lançaient des expériences IA en permanence.

Depuis, les entreprises ont joué quelques manches. Comme l'a dit Anish Agarwal, CEO de Traversal : "More companies have gone through a renewal cycle with customers. They've understood what it takes to actually win a contract." Les LLMs ne tournent plus en mode call-and-response brut dans les chatbots d'entreprise. On a attaché du tooling, implémenté de l'automation, branché des évals, et formalisé tout ça en agents — souvent avec le mot "claw" dans le nom. Eux, et leurs clients, doivent justifier le token spend qui explose avec des résultats réels.

### La "find out stage"

L'auteur s'est mis à dire qu'on est dans la "find out stage" de l'IA — autrement dit, on est passés de la phase expérimentale à une phase où ça doit fonctionner et apporter de la valeur réelle. HumanX a validé cette intuition : presque tous les intervenants parlaient d'"inflection point", de "second phase d'IA", de "conversation qui se déplace". Voici quelques endroits où la conversation se déplace.

### Du wonder à la responsabilité

Au début de l'IA, le buzz tournait autour de toutes les choses cool que l'IA pouvait faire. On parlait beaucoup d'émergence — comme faire deviner un film à partir d'emojis ou dessiner une licorne. C'était une source d'émerveillement, de la techno cool qui impressionnait les explorateurs.

La promesse de l'IA a grandi, et les grandes entreprises ont commencé à intégrer des features IA dans leurs logiciels et leurs process. Mais les entreprises, traditionnellement, sont les endroits où l'émerveillement et la surprise mènent à des clients perdus et à des procès. Les secteurs comme la santé, le droit et l'énergie ont des conséquences réelles en cas d'erreur. "In these environments, mistakes aren't just technical — they can be fatal", dit Radha Basu, CEO et fondatrice d'iMerit. "That changes the mindset entirely. It forces a more careful, purposeful approach to how we build and deploy these systems."

### La confiance comme nouveau plafond

Pendant deux ans, l'IA a été une histoire de modèles toujours meilleurs entraînés sur toujours plus de données. Mais comme l'a dit Ravindra Mistri, founding operator chez Better Auth : "The next phase of AI adoption won't be limited by model performance — it will be limited by trust." Et comme l'a dit Stefan Weitz, CEO de HumanX, dans son discours d'ouverture : "Without trust, all we're doing is building a high-tech house of cards and hoping no one coughs too hard."

Pour obtenir cette confiance de votre IA, il faut des garde-fous, des évaluations, des observabilités, et des process humains qui valident la sortie avant qu'elle ne touche un client.

## Pourquoi ça compte

C'est probablement le meilleur cadrage en quatre mots de la transition que vit la tech actuellement. Pour les leaders d'engineering, "find out" signifie qu'il ne suffit plus de lancer un PoC IA — il faut le passer en production, mesurer son impact, et l'opérer dans la durée. Ceux qui n'ont pas anticipé l'orchestration, les coûts et la confiance vont découvrir leurs failles en production.
