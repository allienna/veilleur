---
title: "The Pulse: What can we learn from Bun's rapid Rust rewrite with AI?"
date: 2026-07-17
url: https://blog.pragmaticengineer.com/the-pulse-what-can-we-learn-from-buns-rapid-rust-rewrite-with-ai/
authors: [blog.pragmaticengineer.com, Gergely Orosz]
keywords: [Bun, Rust, rewrite, Fable, multi-agent, memory safety]
theme: IA
tone: opinion
used_in: ["2026-07-17"]
---

## Résumé

Gergely Orosz analyse la réécriture de Bun (runtime JavaScript, 22 millions de téléchargements mensuels) de Zig vers Rust, réalisée avec le modèle Fable d'Anthropic. La motivation : Zig n'est pas memory-safe et générait fuites et crashs récurrents. Un rewrite classique aurait pris à une petite équipe plus d'un an pour zéro impact utilisateur — inacceptable. Jarred Sumner a donc tenté l'IA : 3 heures de préparation pour produire un guide de portage de 600 lignes, un essai sur 3 fichiers avec revue adversariale, puis un déploiement sur 64 agents en parallèle sur 1 448 fichiers, avec une journée passée à empêcher les agents de se marcher dessus (git stash, reset…).

## Points clés

- Motivation : Zig mélange GC et mémoire manuelle → fuites, crashs, use-after-free, double-free. Rust transforme ces bugs en erreurs de compilation (« un meilleur feedback loop qu'un guide de style »).
- Bun = 535 496 lignes de Zig (hors commentaires), 1 448 fichiers ; un rewrite manuel aurait pris à une petite équipe un an complet, sans impact utilisateur — non viable.
- Étape 1 : 3 h de discussion avec Claude → PORTING.md, un guide de 600 lignes (règles précises : pas de tokio/rayon, pas d'async fn, tout en callbacks + machines à états, reshaping du borrow-checker autorisé).
- Étape 2 : essai sur 3 des 1 448 fichiers, suivi de deux revues adversariales dans des sessions séparées.
- Étape 3 : découpage sur 64 agents IA travaillant en parallèle sur des fichiers indépendants.
- Étape 4 : ~1 jour pour stabiliser le run — les agents se marchaient dessus (git stash / pop / reset), résolu en interdisant toute commande git ne committant pas un fichier précis.

## Analyse approfondie

La semaine dernière à San Francisco, Gergely Orosz a rencontré Jarred Sumner, créateur du runtime JavaScript Bun, pour en savoir plus sur la réécriture de Bun de Zig vers Rust. Sur le moment, Jarred ne voulait pas trop en dire, car l'outil utilisé pour la migration, Fable, était hors service à cause de contrôles à l'export imposés par le gouvernement américain. La situation étant depuis résolue et Fable de nouveau disponible mondialement, Jarred a publié un billet détaillé.

**Contexte : Bun est un projet complexe** dont beaucoup de logiciels de production dépendent. Bun fait le transpiling/minifying/bundling de JS, TS et CSS, embarque un test runner, un gestionnaire de paquets compatible npm, la résolution de modules, un client WebSocket, des implémentations Node.js, etc. 22 millions de téléchargements mensuels ; Claude Code et OpenCode en dépendent, et Vercel, Railway, DigitalOcean le supportent en first-party.

### Pourquoi un rewrite ?

Zig n'est pas memory-safe et les bugs mémoire survenaient en continu : fuites, crashs, écritures heap-out-of-bounds. Et cela, après que l'équipe eut patché le compilateur Zig et mis en place des tests end-to-end de fuites mémoire. Jarred : « Notre liste de bugfixes faisait mal et j'étais fatigué de m'endormir en craignant des crashs dans Bun. Je n'en blâme pas Zig — mélanger GC et mémoire gérée manuellement est un besoin assez rare pour qu'aucun langage ne le conçoive vraiment. Gérer correctement les durées de vie des valeurs GC et manuelles a été une source majeure d'instabilité. Chaque allocation doit être méticuleusement revue : où ces octets sont-ils libérés ? Comment garantir qu'ils ne le sont qu'une fois ? »

Passer à un langage memory-safe et performant éliminerait ces erreurs ; Rust convenait. « Un grand pourcentage des bugs de cette liste sont des use-after-free, double-free et "oubli de free" dans un chemin d'erreur. En Rust safe, ce sont des erreurs de compilation, avec un nettoyage automatique via Drop. Les erreurs de compilation sont un meilleur feedback loop qu'un guide de style. »

Mais un rewrite complet a toujours été une mauvaise idée, à cause du temps que ça prend. Le schéma classique : on estime 9 mois ; 9 mois plus tard il reste 6 mois car du code neuf a été ajouté à l'original entre-temps ; à 15 mois il en reste encore ; on finit par imposer un « feature freeze » et terminer en ~18 mois, si l'on a de la chance — les 9 mois estimés deviennent 2 ans et plus. Jarred : « Historiquement, les rewrites sont une terrible idée. Hors commentaires, Bun fait 535 496 lignes de Zig. Un rewrite dans un autre langage prendrait un an complet à une petite équipe d'ingénieurs. Un an sans impact utilisateur n'est pas une option réaliste. […] Et si, à la place, je passais une semaine à tester si le nouveau modèle d'Anthropic [Fable] peut réécrire Bun en Rust ? »

### Réécrire Bun avec Fable

Sans surprise, ce n'était pas aussi simple que « Claude, réécris Bun en Rust. Ne fais aucune erreur. »

**Étape 1 : préparation.** Trois heures de travail intense avec Claude. « Avant d'écrire du code, j'ai passé environ 3 heures à discuter avec Claude de comment mapper étroitement les patterns de notre base Zig vers Rust. Claude a sérialisé cette discussion dans un document PORTING.md », un fichier de 600 lignes avec des règles comme : pas de tokio, rayon, hyper, async-trait, futures ; pas de std::fs, std::net, std::process (Bun possède sa propre event loop et ses syscalls) ; pas d'async fn — tout en callbacks + machines à états, comme en Zig ; le reshaping du borrow-checker est autorisé (capturer le scalaire nécessaire dans un local, lâcher l'emprunt, ré-emprunter), sans recourir aux raw pointers juste pour faire taire le borrowck, en laissant une note `// PORT NOTE:`.

**Étape 2 : essai + revue adversariale.** Demander à Claude de réécrire 3 fichiers sur 1 448. Après quoi Jarred a lancé deux revues adversariales séparées avec Claude pour critiquer le résultat, dans des sessions distinctes de celle ayant produit les changements.

**Étape 3 : répartir le travail sur 64 agents IA.** Jarred a découpé le travail pour que les agents traitent en parallèle des fichiers indépendants les uns des autres.

**Étape 4 : stabiliser le run (~1 jour).** À la première tentative, les agents se gênaient : « J'ai demandé à Claude de boucler le workflow sur les 1 448 fichiers .zig, et environ 2 minutes après, un Claude a lancé git stash avant de committer. Un autre a fait git stash pop. Puis git reset HEAD --hard. Ils se marchaient dessus ! Et si je mettais chaque Claude dans un worktree séparé, je manquais d'espace disque car le dépôt git de Bun est trop gros. » La solution : interdire à Claude git stash, git reset et toute commande git ne committant pas un fichier précis d'un coup. Ni cargo. Aucune commande lente.

## Pourquoi ça compte

C'est le cas d'usage concret qui rend crédible tout le reste : une réécriture longtemps jugée impossible, menée en semaines grâce à un orchestrateur multi-agents et une revue adversariale. La leçon n'est pas « l'IA écrit le code » mais « l'échafaudage — guide de portage, essais, revue, garde-fous git — fait la différence ».
