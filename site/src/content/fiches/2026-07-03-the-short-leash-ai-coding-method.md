---
title: "The Short Leash AI Coding Method For Beating Fable"
date: 2026-07-03
url: https://blog.okturtles.org/2026/07/short-leash-ai-method/
authors: [okTurtles, taoeffect]
keywords: [short leash, revue de code, vibe coding, sécurité, AI disclosure]
theme: Leadership
tone: opinion
used_in: ["2026-07-03"]
---

## Résumé

Fruit d'un an de recherche sur l'usage des agents IA pour du logiciel critique, ce billet propose la méthode de la « laisse courte » (short leash). À rebours des influenceurs qui vantent des dizaines d'agents parallèles pilotés depuis la plage, l'auteur défend une discipline stricte : jamais de mode YOLO, lecture de chaque diff avant validation, intervention permanente, commits fréquents. Il détaille aussi sa politique de revue : chaque PR doit être relue par un humain ET une IA, l'IA jouant le rôle de linter. Point clé : si une IA a aidé à écrire la PR, son auteur humain doit la relire ligne par ligne, comme le code d'un autre.

## Points clés

- La méthode « short leash » vise des résultats de haute qualité, même sans modèle frontier, mais elle est réservée aux développeurs experts.
- Refus du mode « YOLO » / « dangerously skip permissions » : chaque diff proposé est analysé avant acceptation.
- Rester dans la boucle en permanence, refuser les permissions et intervenir dès que l'IA « déraille ».
- Commits à la fin de chaque sous-tâche pour se protéger contre les erreurs destructrices de l'agent.
- Une PR relue par un humain ET une IA contient moins d'erreurs qu'une PR relue par un seul des deux ; l'IA est traitée comme un linter.
- Toute PR assistée par IA doit être relue ligne par ligne par son auteur humain, et divulguer les modèles utilisés sous une rubrique « AI Disclosure ».

## Analyse approfondie

Ce billet est l'aboutissement de plus d'un an de recherche sur la façon d'utiliser correctement les agents IA pour écrire du logiciel de haute qualité dans des systèmes critiques en matière de sécurité. J'écris principalement depuis ma perspective de développeur logiciel, développeur de protocole et mainteneur de logiciel critique.

Au cours de l'année écoulée, j'ai plongé en profondeur dans les agents IA. J'ai exploré leurs limites, ce sur quoi on peut ou non compter. J'ai créé nos propres outils de revue IA qui performent aussi bien que des systèmes de revue IA valant plusieurs milliards. J'ai maintenu mon propre fork d'un agent de code appelé Crush. Ce billet est ma distillation de la meilleure approche pour créer du logiciel de haute qualité avec des outils IA.

Certaines personnes détestent l'IA. En effet, beaucoup de développeurs *devraient* détester l'IA, car elle est l'ennemie de leur propre apprentissage. Ce billet n'est pas pour eux. Il s'adresse aux rares développeurs experts dont les compétences dépassent tout « modèle IA frontier » dans leur domaine, et qui veulent utiliser l'IA pour augmenter leur performance *sans sacrifier aucune qualité*.

### Problèmes des approches actuelles

Si vous avez beaucoup utilisé des agents IA, vous savez qu'au cours d'une session, ceci peut arriver :

- Vous pouvez découvrir que votre idée initiale était stupide et qu'une meilleure existe.
- Votre agent peut « dérailler » et se mettre à faire quelque chose que vous ne voulez pas.

J'ai vu des vidéos à des centaines de milliers de vues où des YouTubeurs expliquent avoir inventé des systèmes compliqués de 12 agents parallèles gérés par un orchestrateur, faisant un milliard de choses simultanément, sans plus jamais s'impliquer dans le processus de codage. Ce n'est que de la bouillie (slop) qui écrit et relit de la bouillie pendant que le YouTubeur est sur une plage, aux toilettes, ou sirote un café sans raison.

Il est humainement impossible de construire sa propre compréhension d'une base de code si on utilise une telle approche « Vibe ». L'IA aura déraillé plusieurs fois et vous ne le remarquerez que plus tard, en essayant réellement d'utiliser le logiciel. Cette méthode peut être parfaitement acceptable quand la qualité n'importe pas, mais si vous *y tenez*, une autre approche est nécessaire.

Le problème, c'est que même du code écrit et/ou relu par Fable 5 va puer : le code fonctionne, mais il est horriblement inefficace et laid. Et cela arrivera d'autant plus souvent dans un domaine de niche pour lequel le modèle a peu de données d'entraînement sur lesquelles s'appuyer. Contrairement aux déclarations marketing de certains PDG, ces modèles ne savent pas penser au-delà de leurs données d'entraînement.

### La méthode « Short Leash »

Cette méthode ne peut pas être employée par n'importe qui : seuls les développeurs logiciels professionnels le peuvent. Mais elle mène à des résultats qui battent Fable, même sans modèle frontier. Dans la méthode Short Leash :

- Vous utilisez une phase de planification pour rechercher la tâche et formuler un plan, avec quelque chose comme ma « tasks skill » pour suivre l'avancement et découper les grandes tâches (point commun avec beaucoup de méthodes de « vibe engineering » ; l'approche diverge dans les points suivants).
- Vous n'utilisez jamais le mode « YOLO » (alias « dangerously skip permissions »).
- L'IA ne travaille jamais « pendant que vous jouez aux jeux vidéo ».
- Vous utilisez un agent de code qui affiche un diff des changements sur le point d'être faits, via le prompt de permission.
- Vous êtes assis là comme un forcené du 20e siècle, et vous analysez réellement les changements que l'IA propose.
- Vous restez dans la boucle en permanence, au lieu de vous en retirer (la tendance promue par les YouTubeurs).
- Vous utilisez les diffs des prompts de permission pour maintenir à jour votre compréhension de la base de code et garder l'IA en « laisse courte ».
- Vous REFUSEZ les permissions dès que vous voyez l'IA sur le point de faire quelque chose que vous ne voulez pas.
- Vous intervenez fréquemment et autant que nécessaire pour empêcher l'IA de « dérailler ».
- À tout instant, l'IA est « tenue en laisse courte ».
- Des commits sont faits à la fin de chaque sous-tâche pour vous protéger des ratés de l'IA qui pourrait détruire du travail déjà fait (ça arrive, j'ai vu Opus le faire).
- Enfin, on fait une revue.

### Comment faire les revues IA

Une PR relue par un seul humain ou une seule IA contiendra plus d'erreurs qu'une PR relue par les *deux*. L'IA peut être traitée comme un linter : elle attrape vite les erreurs courantes, tandis que l'humain saisit les problèmes de plus haut niveau et les changements de direction nécessaires.

Donc, pour les revues :

- Vous devriez utiliser l'IA pour relire absolument chaque PR.
- L'IA doit avoir accès à un contexte suffisant (l'issue, la description de la PR, la base de code et les changements).
- Vous devriez utiliser les meilleurs modèles disponibles pour relire.
- La description de la PR doit divulguer les modèles précis utilisés (le cas échéant) sous une rubrique « AI Disclosure ». Cela sert à plusieurs choses : informer le mainteneur que l'IA a été utilisée ; lui permettre de suggérer de meilleurs modèles si de faibles ont été employés ; signaler que vous êtes un développeur « réglo » qui ne cherche pas à « faire passer l'IA en douce ».
- Enfin, et c'est le plus important, la PR **doit être relue par son « auteur » si elle a utilisé de l'IA.**

Ce dernier point mérite qu'on s'y attarde. Les PR assistées par IA sont en réalité des PR d'une IA avec assistance humaine. Par conséquent, l'humain qui soumet la PR est censé comprendre ce qu'il soumet, et il ne peut pas le faire s'il n'a pas relu le code écrit par l'IA. Il doit donc traiter sa propre PR comme s'il relisait celle de quelqu'un d'autre, et la relire lui-même, ligne par ligne. Une fois terminé, il peut confirmer sa propre approbation et solliciter l'attention du mainteneur. Cela construit et démontre sa compréhension de la base de code.

### Fin

Et c'est ainsi qu'on utilise l'IA chez okTurtles. Divulgation IA : ce billet a été entièrement écrit par des doigts humains connectés à un cerveau humain ; une « vérification orthographique » façon IA a été faite avant publication.

## Pourquoi ça compte

Face au discours dominant du « vibe coding » qui pousse à déléguer entièrement, ce billet incarne le contre-courant crédible : discipline, revue humaine ligne par ligne et transparence sur l'usage de l'IA comme conditions de la qualité en contexte critique.
