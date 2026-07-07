---
title: "Closing the Verification Loop"
date: 2026-07-06
url: https://thinkroom.kieranklaassen.com/d/njrS5TJhis
authors: [Kieran Klaassen]
keywords: [verification, QA agent, dogfood, compound engineering, auditability]
theme: IA
tone: opinion
used_in: ["2026-07-06"]
---

## Résumé

Kieran Klaassen part d'un constat : les agents ont rendu le build bon marché, donc le coût s'est déplacé vers la vérification — « est-ce que quelqu'un sait vraiment que ça marche ? ». Il présente `/ce-dogfood`, une skill de compound engineering qui agit comme un ingénieur QA autonome : elle teste dans un vrai navigateur tout ce qu'une branche a changé, juge à la fois le fonctionnel et l'expérientiel via des personas, corrige les petits bugs et escalade le reste à l'humain. Le principe central : l'autonomie n'est pas la confiance, c'est l'auditabilité — chaque scénario laisse une preuve durable, jusqu'au SHA de commit.

## Points clés

- La boucle de vérification, c'est la distance entre une affirmation (« ça marche ») et sa preuve ; la fermer à la main ne tient plus quand les agents vont plus vite que les humains.
- `/ce-dogfood` est diff-scopé (teste ce que la branche a changé, jamais le trunk) et passe par un vrai navigateur via un binaire Rust `agent-browser`, pas un wrapper MCP.
- On cartographie d'abord les *flows* (parcours utilisateurs) avant d'en dériver la matrice de tests : la règle de l'email dit qu'« un email part » n'est pas un succès — encore faut-il le bon destinataire, le bon fil, un contenu sensé.
- Double jugement : la vérité fonctionnelle vient de l'instrument (le navigateur), la vérité expérientielle vient de personas produit qui traquent les « paper cuts ».
- La boucle de correction a un gouverneur : on juge la taille du fix avant de toucher au code ; auto-fix pour les bugs clairs, escalade sinon. Chaque fix embarque un test de régression et un commit par correction logique.
- Porte de sortie : « une matrice verte avec une suite rouge, ce n'est pas prêt ». L'autonomie se paie en preuves auditables, pas en confiance.

## Analyse approfondie

*Comment une branche prouve qu'elle est prête : la réalité du navigateur, les yeux de personas, et des correctifs qui portent leur propre preuve.*

### 1. La boucle qui doit se fermer

Les agents ont rendu la construction bon marché. Le coût s'est déplacé : la question chère n'est plus « peut-on livrer ça ? » mais « quelqu'un sait-il vraiment que ça marche ? ». Une branche qui compile, passe la revue et merge peut tout de même accueillir son premier vrai utilisateur avec un formulaire qui valide le mauvais champ et un email qui pointe vers le mauvais fil.

La boucle de vérification, c'est la distance entre une affirmation et sa preuve. La plupart des équipes la ferment avec des humains : quelqu'un clique un peu avant la démo, quelqu'un jette un œil sur la staging. Ça marche jusqu'à ce que les agents dépassent les humains — ce pour quoi les agents étaient faits. Le compound engineering (CE, un plugin de skills pour agents de code comme Claude Code) répond que la boucle elle-même est un travail qu'un agent peut faire, de bout en bout, en n'impliquant les gens que là où le jugement leur revient, et là où l'outillage ne peut vraiment pas atteindre. La skill qui incarne cela est `/ce-dogfood`.

### 2. Dogfood en une passe

`/ce-dogfood` agit comme un ingénieur QA qui « dogfoode » la branche active : comprendre chaque changement, tester chaque changement dans un vrai navigateur comme le ferait un utilisateur, et corriger ce qui casse, en autonomie, jusqu'à ce que la branche soit prête. Deux contraintes le définissent :

- **Diff-scopé, jamais toute l'app.** Il teste ce que cette branche a changé par rapport au trunk, et refuse de tourner sur le trunk lui-même : pas de diff, rien à dogfooder.
- **Un vrai navigateur, un seul outil.** Toute l'automatisation passe par le CLI `agent-browser`, un outil shell qui pilote directement le navigateur (un binaire Rust, pas un wrapper, pas un serveur MCP) : aucune exception.

Le workflow comporte sept phases avec une boucle au milieu. Quelques détails qui portent la philosophie : la phase **Scope** épingle l'identité de la ref testée pour couper le diff contre la bonne base, et propose l'isolation par worktree quand on teste la ref de quelqu'un d'autre. La phase **Serve** est sans intervention : détecter le port (flag explicite, puis instructions projet, `package.json`, `.env`, puis 3000), réutiliser ou démarrer un serveur, attendre qu'il accepte les connexions — sans s'arrêter pour demander la permission. Et **tout est reprenable** : la matrice (la checklist de scénarios) vit deux fois, comme liste de tâches vivante dans la session et comme document de rapport sur disque, mis à jour après chaque scénario et chaque fix. Tuez la session en cours de route, le rapport est le point de reprise.

`ce-dogfood` est délibérément un orchestrateur, pas un soliste : le root-cause délègue à `ce-debug`, les commits passent par `ce-commit`, les leçons réutilisables vont à `ce-compound`.

### 3. Les flows avant la matrice : la règle de l'email

La façon la plus courante dont une QA automatisée vous ment, c'est de tester des pages au lieu de parcours. Chaque page s'affiche ; la fonctionnalité est quand même cassée, parce que la casse vit *entre* les pages. Dogfood interdit donc de sauter à une checklist. La phase 2 cartographie d'abord chaque changement visible comme un flow explicite : point d'entrée, chaque action, chaque branche (erreur de validation, état vide, permission refusée), chaque effet de bord, et le véritable état final. Ce n'est qu'ensuite que la matrice en est dérivée.

L'exemple canonique est la règle de l'email, visant précisément l'email au mauvais fil de l'introduction : « un email part » n'est pas un succès. Bon destinataire ? Le clic mène-t-il au bon fil et défile-t-il jusqu'au bon message ? Le contenu est-il sensé ? La carte du flow doit porter le parcours au-delà de l'envoi. La matrice couvre alors les deux moitiés de la qualité : les vérifications fonctionnelles (les formulaires valident, les liens vont où ils le prétendent, les données font l'aller-retour, les permissions tiennent) ainsi que les états limites, d'erreur et vides ; et les vérifications expérientielles, qui exigent un autre type de juge.

### 4. Deux juges : est-ce que ça marche, et est-ce que ça fait bonne impression

La vérité fonctionnelle vient du navigateur. La vérité expérientielle a besoin d'yeux, et c'est là qu'entre le premier type de persona : le **persona produit**. La phase 1 cherche pour qui le produit est réellement fait et capture un à trois personas primaires et ce à quoi chacun tient. S'il n'en existe aucun, elle en infère un à partir du produit et du diff, et le dit dans le rapport ; la divulgation est la mitigation du fait de juger contre sa propre supposition. Aucun persona du tout, c'est pire : c'est comme ça qu'on obtient un logiciel qui marche et ne plaît à personne.

Chaque scénario est alors jugé deux fois : une fois comme testeur pilotant le navigateur, une fois comme chaque persona relisant le même parcours. La seconde passe est un changement d'yeux, pas un second pilotage. Le parcours persona traque les **paper cuts** : une friction trop petite pour faire échouer un test fonctionnel mais bien réelle pour dégrader l'expérience — un label confus, un clic en trop, une copie qui ne colle pas à la façon dont ce persona pense. La qualité n'est pas un booléen : un scénario peut être fonctionnellement `Pass` et porter des paper cuts, et un paper cut *sharp* (assez sévère pour être corrigé maintenant) entre dans la boucle de correction comme une défaillance. Il faut noter d'où vient chaque verdict : le fonctionnel est une lecture d'instrument ; l'expérientiel vient du même agent, dans la même session, notant un parcours qu'il a imaginé. Deux juges, une seule tête.

### 5. La boucle de correction et son gouverneur

Quand quelque chose casse, le mouvement autonome naïf est de tout corriger. Le mouvement autonome dangereux est aussi de tout corriger. La boucle de correction de dogfood a un gouverneur : **juger la taille du fix avant de toucher au code.** Le territoire de l'auto-fix est étroit à dessein : un bug clair, un correctif évidemment correct, quelques fichiers, aucun compromis de schéma, d'architecture ou de produit. Tout le reste est escaladé, pas tenté ; la section « Décisions pour un humain » du rapport reçoit ce qui est cassé, les options avec leurs compromis, et une recommandation.

Le chemin d'auto-fix paie son autonomie d'avance : chaque fix est livré avec un test de régression conçu pour échouer avant et passer après ; un seul fix logique par commit, pour que l'historique se lise comme une suite de preuves ; on rejoue le scénario, puis on re-teste les parcours adjacents (les fixes cassent leurs voisins). Deux états sont terminaux car ils attendent des humains : `Blocked (human decision)` du gouverneur, et `Blocked (needs human verify)` pour les jambes externes que le navigateur ne peut pas piloter seul (OAuth, livraison d'email réelle, paiements). La porte de sortie : avant de déclarer la branche prête, lancer toute la suite automatisée. **Une matrice verte avec une suite rouge, ce n'est pas « prêt ».** Le rouge bloque même s'il paraît flaky ; la porte est conservatrice par conception. Tout cela est plus lent qu'un smoke test. C'est le compromis.

### 6. La stratégie de personas : spécialistes ensemencés, pas agents permanents

À la fin de la boucle de correction, une seule tête a tout fait : cartographié les flows, piloté le navigateur, écrit les fixes, déclaré qu'ils sont corrigés. Le second type de persona est architectural : le plugin ne livre aucun agent autonome. Quand une skill a besoin d'un spécialiste, elle garde un fichier persona dans son propre répertoire et ensemence un sous-agent générique avec le contenu de ce fichier au moment du dispatch. Avantages : les skills restent auto-contenues ; chaque run lit le persona courant sur disque (pas d'enregistrement périmé) ; le niveau de modèle est choisi par l'appelant, pas par le persona ; la sortie structurée permet de fusionner les résultats mécaniquement.

Le principe profond est le **budget d'indépendance** : une conclusion ne vaut que par l'indépendance de qui l'a confirmée. La skill de revue de code traite la similarité comme un défaut : la lecture rapide de l'orchestrateur est plafonnée à basse confiance et ne peut rien corroborer, car elle partage les angles morts du modèle de session ; deux personas d'accord promeuvent une conclusion d'un cran ; des validateurs par conclusion reçoivent un contexte frais ; et la passe adverse peut appeler une autre famille de modèles. Dogfood dépense le même budget au niveau produit : l'indépendance du navigateur est physique, on ne peut pas le convaincre d'être d'accord ; celle du parcours persona est simulée. Dogfood achète l'indépendance dans ses instruments, pas dans ses jugements ; pour les jugements, il achète une trace que quelqu'un d'autre peut vérifier.

### 7. Une seule boucle, à toutes les altitudes

Dogfood est la boucle de vérification la plus visible parce qu'elle pilote un navigateur, mais ce n'est qu'un barreau d'une échelle que la pipeline gravit pour chaque fonctionnalité, chaque barreau ayant la même grammaire : affirmation plus preuve indépendante. `ce-work` refuse de dire qu'une unité est complète sans preuve de vérification. `ce-code-review` refuse la haute confiance sans une ligne citée (`file:line`). Les skills en prose reçoivent des évals comportementales. `lfg`, la pipeline de livraison de bout en bout, surveille la CI et répare, mais s'arrête après trois tentatives et écrit le résidu dans le corps de la PR. Et ce qu'aucune boucle ne peut fermer devient un résidu durable : une ligne `Blocked`, une issue, une section de rapport. La vérification autonome, ce n'est pas des agents confiants ; c'est des agents auditables, jusqu'au SHA de commit par scénario. La boucle est fermée quand la preuve est durable, et qu'un humain peut entrer à tout moment, lire la trace et reprendre exactement là où son jugement est nécessaire.

## Pourquoi ça compte

C'est le manuel concret du nouveau goulot d'étranglement de l'ère agentique : quand produire devient gratuit, ce sont la vérification et l'auditabilité qui deviennent le vrai travail d'ingénierie.
