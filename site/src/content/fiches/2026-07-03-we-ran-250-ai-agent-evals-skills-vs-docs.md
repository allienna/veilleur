---
title: "We Ran 250 AI Agent Evals to Find Out if Skills Beat Docs. The Answer Is More Complicated Than We Expected"
date: 2026-07-03
url: https://www.wix.engineering/post/we-ran-250-ai-agent-evals-to-find-out-if-skills-beat-docs-the-answer-is-more-complicated-than-we-ex
authors: [Wix Engineering, Adam Friedmann]
keywords: [skills, documentation, évaluation, agents IA, tokens, MCP]
theme: IA
tone: research
used_in: ["2026-07-03"]
---

## Résumé

L'équipe de documentation de Wix a mené 250 évaluations contrôlées pour trancher une question à la mode : les « skills » (guides condensés pour agents) battent-ils la simple documentation ? Résultat nuancé. Optimiser la doc pour les agents apporte un gain majeur (67 % → 87 % de complétion). Mais un skill légèrement périmé ou imprécis devient un handicap qui peut brûler jusqu'à 94 % de tokens en plus. Pire, un skill peut rendre l'agent moins curieux et lui faire rater des solutions plus simples. Conclusion : la doc bien structurée est la colonne vertébrale, les skills ne sont qu'une couche de cache à évaluer en continu.

## Points clés

- 250 évaluations sur deux familles de tâches (extensions Wix CLI et scripts d'API REST), chaque condition rejouée 3 fois.
- Optimiser la doc pour les agents fait passer la complétion de 67 % à 87 % (tâches CLI), avec -35 % de tokens et -9 % de temps.
- Une petite erreur dans un skill efface tout son avantage : scaffolding mal aligné (+94 % de tokens), snippet sans export (+39 %), bonnes pratiques trop lourdes (+52 %).
- Sur les tâches API, doc et skills atteignent la même complétion (80 %), mais la doc est plus rapide quand les skills consomment moins de tokens (fragmentation des appels MCP).
- Un skill peut rendre l'agent moins curieux : guidé par des consignes, il improvise moins et rate des routes plus simples.
- Cadre proposé : doc optimisée = colonne vertébrale ; skills = couche de cache ; évaluations régulières = fraîcheur.

## Analyse approfondie

L'industrie a une nouvelle obsession : les skills IA. La logique semble imparable : si vous voulez qu'un agent utilise votre plateforme, ne lui donnez pas juste de la doc brute, donnez-lui un « skill » — un guide curé, condensé et optimisé. Les skills sont intuitifs et tendance, mais donnent-ils réellement un avantage aux agents par rapport à la simple doc, et si oui, dans quels cas ?

Chez Wix, nous avons décidé de **questionner la hype et de commencer à mesurer**. Nous avons mené 250 évaluations contrôlées comparant la performance d'agents IA sur des tâches avec la doc standard, la doc optimisée pour l'IA, et des skills sur mesure. Les résultats furent surprenants et ont remis en cause toute notre stratégie d'expérience développeur IA-native. Il s'avère qu'un skill légèrement périmé n'est pas seulement inefficace : c'est un handicap.

### Le problème qu'on cherchait à résoudre

L'équipe des tech writers de Wix écrit et maintient la doc développeur (références d'API, guides, tutoriels…). De plus en plus, l'audience de ces docs bascule des développeurs humains vers les agents IA. En parallèle, des skills sont apparus : partout dans l'entreprise, des équipes se sont mises à écrire des skills, mêlant infos extraites des docs et instructions curées, tous maintenus indépendamment, sans coordination avec la doc dont ils dérivaient.

La préoccupation était évidente : dès que le produit sous-jacent change (un scaffold se met à jour, une API gagne un champ requis, une méthode est dépréciée), tout skill dérivé d'une doc périmée dérive. Mais au-delà de la maintenance, une question plus profonde que personne ne posait : les skills sont-ils réellement meilleurs ? On supposait que oui — purpose-built, condensés, optimisés — mais la supposition n'avait jamais été examinée. Nous voulions des **preuves**.

### Méthodologie

Évaluation quantitative sur deux familles de tâches, 250 runs au total :

- **Extensions CLI** : construction d'extensions d'app Wix CLI (pages de dashboard, API backend, widgets, event handlers, scripts embarqués, modals, plugins), contre les skills packagés avec les projets Wix CLI.
- **API REST** : scripting d'API REST (requêter des produits, créer du contenu, gérer des contacts, workflows multi-étapes), contre les skills packagés avec le Wix MCP.

Pour chaque tâche, des agents en sandbox avec différents accès à la doc, chaque condition rejouée 3 fois pour tenir compte de la variance :

- **Baseline** : l'agent utilise le service llms.txt du portail via web-fetch.
- **Optimisée** : la doc avec des améliorations ciblées après analyse des échecs (ajout d'un appel de méthode manquant, correction d'incohérences de noms de champ, ajout d'une étape d'installation de dépendance oubliée).
- **Contenu curé** : l'agent n'a accès qu'aux skills, ou au Wix MCP + ses skills packagés.

Après le développement, on demandait à l'agent de changer de casquette et d'évaluer son propre travail (tâche accomplie ? sinon pourquoi ?), avec collecte déterministe des tokens, du nombre de tours et du temps.

### Ce qu'on a trouvé

**1 — La doc peut et doit être optimisée pour les agents.** Sur les tâches CLI, la seule optimisation de la doc a fait passer la complétion de 67 % à 87 %, tout en coupant 35 % de tokens et 9 % de temps. Une doc à structure navigable, aux noms de champs cohérents et aux dépendances explicites est une intervention à fort ROI. Avant d'écrire le moindre skill, mettez votre doc au carré.

**2 — Les petites erreurs dans les skills érodent leur avantage.** Sur les tâches CLI, les runs doc-optimisée atteignent 85 % de complétion contre 78 % pour les skills seuls, avec 10 % de tokens en moins, 8 % plus vite, 14 % de tours en moins. La raison : de petites erreurs anéantissent l'avantage de vitesse. Exemples : un scaffolding mal aligné (le skill fait bâtir un widget avec une lib React quand le projet attend une solution Wix propriétaire → reconstruction, +94 % de tokens) ; un snippet sans déclaration d'export qui ne compile pas (+39 %) ; des bonnes pratiques qui gonflent le code (+52 %). À l'inverse, quand les skills sont bien alignés au produit et au scaffolding, ils gagnent nettement (-30 à -50 % de tokens, -30 % de temps). Conclusion : des skills précis apportent un vrai bénéfice, mais leurs erreurs peuvent l'annuler entièrement.

**3 — Optimiser les tokens peut augmenter le temps réel.** Sur les tâches API, doc-optimisée et skills atteignent une complétion identique de 80 %. Mais l'efficacité diverge : la doc tourne 31 % plus vite avec 33 % de tours en moins, tandis que les skills consomment 29 % de tokens en moins. La raison de cette lenteur malgré moins de tokens : la fragmentation des outils MCP. Un seul web-fetch renvoie une page markdown complète (description, schéma requête/réponse, paramètres, exemples) en un aller-retour ; le MCP fragmente la même information en plusieurs appels séquentiels — plus d'appels, plus de latence d'inférence, plus de tours.

**4 — Les skills peuvent rendre les agents moins curieux.** Constat inattendu : quand un agent reçoit des consignes officielles dans un skill, il les suit de près et improvise donc moins face à un cas limite. Plusieurs agents en mode doc-optimisée ont trouvé des routes plus directes précisément parce qu'ils n'étaient pas ancrés à une approche prescrite. L'autorité du skill devient une contrainte, qui rétrécit l'espace des solutions.

### Un cadre pour docs et skills

- **La doc optimisée pour agents est la colonne vertébrale.** Un agent doit pouvoir accomplir n'importe quelle tâche imaginable via la doc, structurée pour la consommation machine (points d'entrée llms.txt clairs, nommage cohérent, dépendances explicites).
- **Les skills sont une couche de cache.** Ils existent pour rendre les tâches courantes et bien définies plus rapides et moins chères — des raccourcis distillés, dérivés de la doc, pas indépendants d'elle.
- **Des évaluations régulières maintiennent la fraîcheur des skills.** Dès qu'un skill sous-performe la doc, c'est le signal que quelque chose a dérivé.

### Conclusion

Les agents IA deviennent l'audience principale de la documentation développeur. Toute plateforme qui veut rester compétitive doit s'assurer que les agents peuvent l'utiliser efficacement. En même temps, ce n'est pas parce que l'industrie survend un nouveau format comme les skills que son efficacité est garantie. Il faut prendre du recul et adopter une approche pilotée par les données : notre étude montre que la bonne vieille doc reste un composant critique d'une plateforme optimisée pour les agents.

## Pourquoi ça compte

C'est un rare exemple de démarche empirique face à la hype des skills : mesurer plutôt que croire. Le résultat rappelle que les fondamentaux (une doc solide) l'emportent souvent sur le raccourci à la mode, un enseignement directement transposable à toute équipe qui outille ses agents.
