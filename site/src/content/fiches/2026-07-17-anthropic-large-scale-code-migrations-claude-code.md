---
title: "How Anthropic runs large-scale code migrations with Claude Code"
date: 2026-07-17
url: https://claude.com/blog/ai-code-migration
authors: [claude.com, Anthropic]
keywords: [code migration, Claude Code, judge, multi-agent, rulebook]
theme: IA
tone: tutorial
used_in: ["2026-07-17"]
---

## Résumé

Anthropic détaille une méthode en six étapes pour piloter des migrations de code à grande échelle avec Claude Code, généralisée à partir de deux cas réels (Zig→Rust pour Bun, Python→TypeScript). Le prérequis absolu n'est pas le modèle mais un « juge » fiable : capable d'évaluer l'ancien et le nouveau code sur un pied d'égalité, et validé contre du code volontairement cassé. Le processus repose sur un rulebook, une carte de dépendances, un inventaire des écarts, un stress-test des règles, puis une boucle multi-agents (implémenter, réviser, corriger) rendue reprenable par construction.

## Points clés

- Prérequis : un juge solide, sinon pas de condition de sortie ni de mesure de succès. « Un juge qui n'attrape pas les régressions n'est pas un juge. »
- Étape 1 : rulebook (avant tout), carte de dépendances, inventaire des écarts. Le rulebook précède l'inventaire, testés ensemble en audit conjoint.
- Jarred (Bun) a utilisé 8 sous-agents pour réviser 8 catégories de modes de défaillance ; Bun = 535 496 lignes de Zig, 1 448 fichiers.
- Étape 2 : stress-test sur une mini-migration (« shakedown cruise ») — on jette les fichiers traduits, l'objectif est de raffiner les règles.
- Étape 3 : boucle multi-agents implémenter/réviser/corriger ; on peut confier l'implémentation à des modèles plus petits (Mike a utilisé Sonnet sur 12 sous-agents) et garder les gros pour la revue.
- La file de travail est mécanique et reconstruite depuis le disque à chaque fois → migration reprenable par construction ; deux relecteurs adversariaux évaluent les implémenteurs.

## Analyse approfondie

**Six étapes pour les grandes migrations de code.** Le processus a été généralisé pour être pertinent sur plusieurs langages et scénarios.

### Prérequis

Avant de démarrer, il faut un juge solide, sinon on n'a ni condition de sortie ni mesure de succès. Le juge doit pouvoir évaluer le code d'origine et le code cible sur un pied d'égalité. Les suites de tests écrites dans le langage d'origine dépendent souvent de fonctions internes qui n'existeront pas dans le code cible. Pour le construire :

- **Catégoriser les tests existants.** Utiliser Claude pour identifier lesquels s'expriment comme des appels externes et lesquels dépendent d'internes non portables.
- **Réécrire pour la portabilité.** Convertir les tests orientés externe en assertions exécutables contre l'original et le port. Utiliser des agents adversariaux pour vérifier que les tests réécrits n'affaiblissent pas les assertions.
- **Valider le juge.** Le lancer contre le code d'origine pour confirmer qu'il passe. Puis contre du code délibérément cassé pour confirmer qu'il échoue — un juge qui n'attrape pas les régressions n'est pas un juge.

Jarred disposait d'une grande suite de tests écrite dans un troisième langage (TypeScript), ce qui ne sera pas le cas de la plupart des projets. Pour son port Python→TypeScript, Mike a créé une « parity harness » de sept scénarios réels et a considéré tout changement de comportement comme un bug à corriger.

### Étape 1 — Créer le rulebook, la carte de dépendances et l'inventaire des écarts

On pose les fondations : un inventaire des endroits à refactorer plutôt qu'à simplement traduire, un rulebook de traduction, et une carte de dépendances pour ordonner les chantiers. L'ordre compte : le rulebook doit précéder l'inventaire, car ce dernier est défini par ce que les défauts du rulebook ne couvrent pas ; les deux sont testés ensemble en audit conjoint.

**Rulebook.** Sa forme dépend de décisions architecturales de départ, notamment : le nouveau code suivra-t-il la même structure ou sera-t-il entièrement redessiné ? Dans le premier cas (Jarred), le rulebook est surtout des tables de correspondance de types et d'idiomes pointant vers l'inventaire des écarts pour les composants durs à traduire. Dans le second (Mike), c'est un document de conception. Jarred a créé son rulebook en discutant avec Claude, formulant une politique pour chaque zone d'ambiguïté, et a utilisé huit sous-agents dédiés à huit catégories de modes de défaillance courants.

**Carte de dépendances.** Nécessaire pour découper les chantiers d'une migration parallèle : savoir quels fichiers migrer d'abord et lesquels regrouper dans un même lot. Certains langages ont des manifestes explicites ; pour les bases legacy et des langages comme C/C++ ou Python, ces dépendances doivent être découvertes et cartographiées. Claude Code peut déployer des agents pour créer et exécuter un script déterministe produisant cette carte.

**Inventaire des écarts et relecteurs sceptiques.** Le nouveau langage a des exigences différentes. Pour Zig→Rust, l'écart était la gestion manuelle de la mémoire (en Rust, use-after-free, double-free et fuites deviennent des erreurs de compilation avec nettoyage automatique via Drop). Pour Python→TypeScript, l'écart était les interfaces et contrats : Python n'exige pas de déclarer la forme des objets acceptés ou renvoyés, TypeScript oui — le contrat doit être écrit avant que ça compile. Jarred et Mike ont créé des fichiers d'inventaire capturant ce savoir implicite ; Jarred en amont, Mike par audit après traduction. Les deux peuvent être nécessaires.

### Étape 2 — Stress-tester les règles

Une mini-migration qui sert de « croisière d'essai ». Jarred a utilisé un agent pour traduire trois fichiers avec le rulebook, un agent pour les traduire « comme un ingénieur Rust senior », et un agent pour créer de nouvelles règles à partir du diff. Il a attrapé deux problèmes critiques qui auraient posé de nombreux soucis une fois étendus aux 1 448 fichiers. Ce test ne marche que pour les migrations préservant la structure, où deux traductions du même fichier sont comparables ligne à ligne ; pour un redesign (Mike), l'équivalent est d'attaquer le document de conception avec des relecteurs adversariaux, puis de le valider avec un run end-to-end jetable. Dans tous les cas, on jette les fichiers traduits : l'objectif est de raffiner les règles, pas de progresser.

### Étape 3 — Tout traduire

Pour les étapes restantes, on lance la même architecture de boucle multi-agents : implémenter, réviser, corriger. On peut déléguer le travail d'implémentation à des modèles plus petits et garder les relecteurs sur les plus gros (Mike a utilisé Claude Sonnet en déployant 12 sous-agents pour la migration principale). La file de travail doit être mécanique : un script batch décide de ce qui est fait en vérifiant si le fichier traduit existe sur le disque, puis découpe les fichiers restants en lots. Comme la file est reconstruite depuis le disque à chaque fois, la migration est reprenable par construction. Les agents peuvent être trop prudents ; le correctif est une instruction franche indiquant que le compilateur attrapera les erreurs à l'étape suivante. Ce que le traducteur ne peut pas exécuter avec confiance est marqué `// TODO(port): <raison>`. Ensuite, les to-do s'écrivent d'elles-mêmes : le compilateur énumère les erreurs, les smoke tests trouvent les crashs, la suite rapporte les échecs. Deux relecteurs adversariaux évaluent le travail des implémenteurs.

## Pourquoi ça compte

C'est la contrepartie méthodologique du discours « l'implémentation est le vrai enjeu » : Anthropic montre que la fiabilité d'une migration IA ne tient pas au modèle mais à l'échafaudage humain — juge, rulebook, revue adversariale — un patron directement réutilisable par les équipes.
