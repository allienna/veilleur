---
title: "How much can you delegate to agents?"
date: 2026-07-30
url: https://newsletter.posthog.com/p/agent-autonomy?utm_source=tldrdev
authors: [Jina Yoon, PostHog]
keywords: [agent autonomy, delegation, guardrails, LLM-as-judge, context]
theme: Leadership
tone: opinion
used_in: ["2026-07-30"]
---

## Résumé

PostHog propose un cadre de décision pour savoir combien déléguer à un agent. Le point de départ est un refus explicite : la confiance ne dépend pas de la qualité du modèle mais de la nature de la **tâche**. Deux questions — la tâche est-elle facile à vérifier ? est-elle facile à annuler ? — définissent quatre niveaux d'autonomie, du simple assistant au mode self-driving. Pour chaque niveau, l'article donne les leviers d'ingénierie permettant de monter d'un cran plutôt que de rester bloqué.

## Points clés

- Faire confiance à ses agents juste parce que les modèles sont devenus plus intelligents, c'est comme ne pas mettre sa ceinture parce qu'on a une plus belle voiture.
- Deux axes seulement : facile à vérifier (feedback immédiat quand l'agent se trompe) et facile à annuler (un Ctrl+Z garanti).
- Quatre niveaux : 0 assistant, 1 human-in-the-loop, 2 délégation (le plafond par défaut du travail dev aujourd'hui), 3 self-driving.
- Mettre systématiquement un humain en garde-fou du niveau 2 vous transforme en votre propre goulot d'étranglement : mieux vaut encoder les garde-fous dans le pipeline.
- Un manque d'autonomie est souvent juste un déficit de contexte, pas un déficit de modèle.
- L'échelle n'est pas un facteur : si l'autonomie est bien réglée au niveau de la tâche, l'échelle se règle d'elle-même.

## Analyse approfondie

Les gens font confiance à leurs agents pour de plus en plus de travail sans supervision — mais comment décider quand leur faire confiance ?

Certains pensent que la réponse dépend de la qualité du modèle : quand les modèles s'améliorent, on peut leur confier davantage. **Mais faire confiance à ses agents juste parce que les modèles sont devenus plus intelligents, c'est comme ne pas mettre sa ceinture parce qu'on a une plus belle voiture.**

La vraie réponse n'a rien à voir avec le modèle, et tout à voir avec la **tâche**. Il faut se construire un modèle mental de quand déléguer et combien, qu'on peut ensuite adapter.

### Les deux questions préalables

Pour tourner en sécurité de manière autonome, les agents ont besoin d'un **retour immédiat quand ils se trompent**. C'est possible pour la plupart du code avec des vérifications déterministes : tests unitaires et d'intégration. Mais les tâches subjectives, comme renommer un paramètre pour plus de clarté, sont difficiles sans goût et jugement humains.

Comme en ingénierie logicielle traditionnelle, si vous voulez faire confiance à un run d'agent non supervisé, il vous faut un **Ctrl+Z garanti** pour les pires scénarios. C'est pourquoi StampHog, l'agent d'approbation de PR de PostHog, route vers un humain tout ce qui contient des mots-clés de la deny-list.

Ensemble, ces deux facteurs désignent l'un des quatre niveaux pour n'importe quelle tâche :

- **Niveau 0 : l'agent comme assistant.** Pour les tâches difficiles à vérifier et difficiles à annuler. Nécessaire quand on touche du code délicat et sensible.
- **Niveau 1 : human-in-the-loop.** Pour les tâches difficiles à vérifier et faciles à annuler. Généralement quand une évaluation subjective est requise.
- **Niveau 2 : délégation à l'agent.** Pour les tâches faciles à vérifier et difficiles à annuler. Le plafond par défaut de la plupart du travail dev aujourd'hui.
- **Niveau 3 : mode self-driving.** Pour les tâches faciles à vérifier et faciles à annuler. Tout accélère vers ce niveau.

Ces quatre niveaux se mappent sur un arbre de décision très simple, applicable à n'importe quelle tâche. Cela aide à décider combien déléguer — mais on peut aussi *concevoir* son pipeline pour permettre plus d'autonomie sur une tâche donnée.

### Niveau 0 — difficile à vérifier + coûteux à annuler

C'est le niveau d'autonomie le plus bas. Pensez à demander conseil à ChatGPT, ou à l'auto-complétion dans Cursor, comme au bon vieux temps de 2024.

Mais ce n'est pas parce que c'est démodé que c'est mauvais : ce mode est idéal pour des problèmes délicats sur des surfaces de code sensibles.

Par exemple, quand Dylan a mis à jour le moteur de feature flags de PostHog pour supporter le ciblage par propriété générique l'an dernier, il devait migrer une hypothèse indirectement incrustée dans chaque feature flag de PostHog. C'était difficile à vérifier de manière déterministe par un agent, puisqu'on ne pouvait pas le `grep`. La mise à jour avait aussi un rayon d'explosion énorme : elle touchait des flags clients en production, des formes de réponses d'API, et des fonctions de scoring.

**Levier : découper la tâche.** De petits morceaux rendent évident où la délégation est sûre ou non. Dylan a confié le travail moins critique — propager la nouvelle logique de ciblage dans les SDK JavaScript, PHP, Ruby et Flutter — à des agents, tout en faisant à la main la migration cœur, plus risquée.

### Niveau 1 — difficile à vérifier + facile à annuler

Ce niveau est courant pour les tâches nécessitant une évaluation subjective, puisqu'il est difficile d'enseigner le goût et le jugement à des agents (pour l'instant, du moins).

Les tâches human-in-the-loop sont considérées comme faciles à annuler parce que le code reste en brouillon et ne sera pas mergé avant vérification humaine. Un « undo » signifie simplement relancer une itération.

Un refactor de lisibilité de code chez PostHog en est un bon exemple : quelques lignes qui rendaient le code plus compréhensible pour les humains — ajout de commentaires, regroupement d'actions, remplacement de chaînes par une enum — sans aucun breaking change. Un agent n'aurait pas su comment noter ce travail.

Leviers :

- **Utiliser le LLM-as-judge.** C'est ainsi que la plupart des gens construisent leurs systèmes de revue de code agentique. À mesure que les modèles s'améliorent, de plus en plus de tâches réclamant du jugement humain peuvent être vérifiées par des LLM.
- **Définir un objectif cadré et mesurable.** Des métriques de succès ou des contrats peuvent servir de proxy à une évaluation subjective. Par exemple : instruire un système d'expérimenter sur le texte d'une landing page jusqu'à ce qu'une variante atteigne 3 % de conversion.
- **Écrire des skills personnalisés.** Cela aide les agents à produire un travail conforme à vos standards, conventions et goûts avec moins de pilotage. Beaucoup de développeurs écrivent des skills de revue de code spécifiques à leur équipe.

### Niveau 2 — facile à vérifier + coûteux à annuler

C'est le niveau où se situe la majorité des tâches de développement aujourd'hui. Un agent écrit du code testable de manière déterministe, mais l'acte final de merge est protégé par une vérification de sécurité.

Quand Robbie a réécrit le parser SQL de PostHog en Rust depuis zéro, il a à peine lu le code, puisqu'il disposait d'un oracle machine pour vérifier le travail. Mais comme le parser touche chaque requête de PostHog, le travail de l'agent était protégé par plusieurs contrôles : shadow mode en production, puis bascule progressive.

**Levier : encoder les politiques et garde-fous dans le code.** La plupart des gens protègent par défaut les tâches de niveau 2 derrière un humain (c'est-à-dire eux-mêmes), mais cette habitude vous transforme en votre propre goulot d'étranglement. À la place, encodez le plus possible de garde-fous directement dans votre pipeline : dry-run par défaut, credentials scopés, changements derrière des feature flags.

### Niveau 3 — facile à vérifier + facile à annuler

Il n'y a pas encore beaucoup de tâches dans cette catégorie — juste les plus petites : bumps de dépendances, corrections de lint, ajout de couverture de tests sur du code existant. Mais la catégorie grandit vite, en particulier avec les agents longue durée, les boucles pilotées par objectif, et l'orchestration plus complexe.

PostHog mise tout sur le mode self-driving. Le mois dernier, l'équipe a lancé les *Scouts* : des agents qui tournent selon un planning, investiguent des signaux issus des données produit, et rédigent une PR à partir de ce qu'ils trouvent.

Leviers :

- **Entraîner des modèles spécifiques au domaine.** Une grande partie de la prochaine vague d'outillage portera sur l'amélioration des tâches de vérification difficiles aujourd'hui pour les LLM. Une voie évidente : des modèles entraînés spécifiquement, qui savent à quoi ressemble « bien » dans un domaine donné.
- **Construire des banques de contexte de niveau expert.** Un manque d'autonomie d'agent est souvent simplement un déficit de contexte. PostHog a appris de première main, en concevant sa couche de contexte pour le PostHog Wizard, que combler ce déficit avec de la connaissance structurée et fraîche est l'une des choses les plus à effet de levier qu'on puisse construire pour des agents fiables.
- **Concevoir des signaux clairs pour les scouts.** Le goulot d'étranglement des agents longue durée sera de savoir s'il existe du travail qui vaille la peine, et de distinguer les signaux valides du bruit.

### Note en bas de page

L'échelle n'est pas un facteur pour déterminer les niveaux d'autonomie des agents. On confond souvent les deux parce que l'orchestration multi-agents rend l'autonomie urgente. Mais si l'autonomie est bien réglée au niveau de la tâche, l'échelle se règle d'elle-même.

## Pourquoi ça compte

C'est le cadre de délégation le plus simple et le plus opérationnel publié à ce jour : deux questions, quatre niveaux, et des leviers concrets pour monter d'un cran. Directement utilisable en revue d'équipe pour arbitrer ce qu'on confie aux agents sans passer par des débats abstraits sur la qualité des modèles.
