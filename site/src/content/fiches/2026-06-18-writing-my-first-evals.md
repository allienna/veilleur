---
title: "Writing my first evals"
date: 2026-06-18
url: https://links.tldrnewsletter.com/jDZTe8
authors: [Nick Nisi]
keywords: [evals, AI agents, testing, non-déterminisme, WorkOS, Claude Agent SDK]
theme: IA
tone: opinion
used_in: ["2026-06-18"]
---

## Résumé

Nick Nisi raconte comment, après avoir construit deux outils dopés à l'IA chez WorkOS, il a réalisé qu'il n'avait aucune idée s'ils « marchaient » vraiment — non pas s'ils s'exécutaient, mais s'ils amélioraient réellement la vie du développeur, une question difficile quand la sortie change à chaque exécution. Il bâtit deux systèmes d'évaluation très différents : l'un teste un agent CLI (`workos install`) via des projets-fixtures et le diff git comme source de vérité, l'autre fait de l'A/B testing pour savoir si un « skill » de contexte améliore vraiment la sortie d'un LLM. Les deux enseignent la même leçon : les evals ne sont pas des tests — on mesure une qualité statistique (taux de réussite, scores composites) à travers de nombreux essais, pas une sortie déterministe. Conclusion : la confiance n'est pas un sentiment, c'est une mesure.

## Points clés

- `expect(output).toBe(expected)` s'effondre face à un agent IA : même entrée, même prompt, sortie différente à chaque fois.
- Fixtures comme états de départ + `git init` : le diff après passage de l'agent devient la source de vérité de ce qui a changé.
- « Réussir » ≠ « être bon » : un second étage de notation (qualité) évalue style, minimalisme, gestion d'erreurs et idiomaticité (grader « les résultats, pas les chemins »).
- Critères statistiques, pas binaires : viser p. ex. 80 % au premier essai, 90 % avec auto-correction, 95 % avec retries — la suite d'evals ne sera jamais 100 % verte, par design.
- Un « skill » de contexte peut *nuire* : l'A/B testing a révélé des deltas négatifs (-12 %, -20 %) qu'aucune relecture manuelle n'aurait attrapés.
- Le système d'eval lui-même peut avoir des bugs : « quand l'eval dit que quelque chose est cassé, suspectez d'abord l'eval ».

## Analyse approfondie

*Ce billet a été initialement publié sur nicknisi.com et republié avec permission.*

J'ai passé les dernières semaines à construire deux outils de développement dopés à l'IA chez WorkOS. À un moment, j'ai réalisé que je n'avais aucune idée s'ils marchaient vraiment. Pas « marcher » au sens de « est-ce que ça tourne » — ça tournait très bien. Je veux dire « marcher » au sens de « est-ce qu'utiliser cet outil améliore réellement les choses pour le développeur ? ». Question bien plus dure qu'il n'y paraît quand la sortie de l'outil est différente à chaque exécution. J'avais besoin d'evals. Et je n'avais aucune expérience pour en écrire.

Les projets : **WorkOS CLI** (la commande `workos install`, propulsée par le Claude Agent SDK) et **WorkOS Skills** (contexte d'agent auto-généré à partir de notre doc).

### L'agent fait-il la bonne chose ?

`workos install` est une commande CLI qui utilise le Claude Agent SDK pour installer automatiquement WorkOS AuthKit dans votre projet. Vous la pointez vers une app Next.js, une SPA React, un serveur Python Flask, ou l'un des 16 frameworks supportés, et elle détermine quoi faire. C'est magique. Et la magie est intestable par défaut. Le problème pour tester un agent IA, c'est qu'il ne fait pas deux fois la même chose : même projet d'entrée, même prompt, sortie différente. `expect(output).toBe(expected)` s'effondre instantanément. J'ai donc construit un système d'eval.

**Fixtures comme états de départ.** L'eval démarre avec des projets-fixtures : des apps minimales pour chaque framework supporté. 16 frameworks au total, chacun avec plusieurs états de départ (`example`, `example-auth0` pour migrer depuis Auth0, `partial-install`, `conflicting-middleware`). Le gestionnaire de fixtures copie chacun dans un répertoire temporaire, lance `pnpm install` (ou `pip install`, `bundle install`, `go mod download` selon ce qu'il détecte) et initialise un dépôt git. Ce `git init` compte : le diff après passage de l'agent devient la source de vérité de ce qui a changé. Avec ~24 fixtures, je trouvais que c'était « à la fois pas assez et trop à maintenir ». La réponse : utiliser des états de départ réalistes, de vraies structures de projet, pas des montages artificiels. Chaque fixture tourne avant que l'agent n'y touche ; si elle ne marche pas proprement, ce n'est pas un test valide.

**L'agent tourne pour de vrai.** Pour chaque fixture, l'exécuteur invoque le vrai agent avec le vrai skill — même chemin de code qu'en production, sans mocks. Il suit chaque appel d'outil, chaque tentative de correction, chaque token. Si l'agent échoue, il peut s'auto-corriger, jusqu'à deux retries dans la même session. L'eval distingue si un scénario passe au premier essai, après correction, ou après un retry complet.

**La notation : la partie que j'ai d'abord ratée.** J'ai commencé par de simples vérifications de fichiers : `middleware.ts` existe-t-il ? Importe-t-il `@workos-inc/authkit-nextjs` ? Ça a marché environ une heure. Puis première vraie leçon : **passer n'est pas la même chose qu'être bon.** Le grader Next.js vérifie sept choses (route de callback, middleware *ou* proxy mais pas les deux — Next.js 16 lève une erreur si les deux existent —, import correct du SDK, intégration de `authkitMiddleware` ou du composable `authkit()`, `AuthKitProvider` qui enveloppe le layout, et build du projet). Ce « pas les deux » encode un vrai savoir métier, le genre qu'un développeur attraperait en revue de code. Mais même avec toutes ces vérifications au vert, un agent peut produire du code qu'aucun développeur n'accepterait : gestion d'erreurs sur-conçue, abstractions inutiles, commentaires expliquant ce que fait `const x = 1`. Techniquement correct. Terrible.

J'ai donc ajouté un second étage de notation. Le grader fonctionnel fait du pass/fail. Puis un grader qualité envoie le code à Claude Haiku, qui le note sur quatre dimensions : **style** (respecte-t-il les conventions du projet ?), **minimalisme** (changements ciblés ou fichiers sans rapport modifiés ?), **gestion d'erreurs** (adaptée ou paranoïaque ?), **idiomaticité** (suit-il les patterns du framework ?). Chacune notée de 1 à 5 avec des grilles, raisonnement en chaîne de pensée avant de noter. Le guide d'eval d'Anthropic appelle cela « noter les résultats, pas les chemins » : le grader se moque des outils ou de l'ordre, il regarde à quoi ressemble le projet une fois l'agent fini.

**Pas pass/fail, des taux de réussite.** Mes critères de succès ne sont pas « tous les scénarios passent », mais : 80 % au premier essai sans correction, 90 % avec auto-correction, 95 % avec retries complets. **Les evals ne sont pas des tests** : les tests vérifient un comportement déterministe (entrée X → sortie Y) ; les evals mesurent une qualité statistique (la *distribution* des sorties atteint-elle des seuils ?). Votre suite de tests doit être 100 % verte ; votre suite d'evals ne le sera pas, par design. Une seule défaillance ne veut pas dire que le système est cassé ; un schéma de défaillances, si. 40 scénarios, 16 frameworks. Exemple de sortie après un run complet : premier essai 92 % (requis 80 %), avec correction 94 % (requis 90 %), avec retry 96 % (requis 95 %).

### Le contexte aide-t-il vraiment ?

Le second outil est un autre problème : un ensemble de **skills** (documents de contexte structurés) chargés dans le system prompt quand un développeur pose une question sur WorkOS (SSO, directory sync, RBAC, intégration AuthKit). Ils sont auto-générés depuis la doc via un pipeline Claude. La question n'est pas « l'agent fait-il la bonne chose ? » mais plus basique : **donner ce contexte au LLM rend-il vraiment sa sortie meilleure ?** Je supposais que oui. Je me trompais sur au moins l'un d'eux.

**A/B testing pour LLM.** Pour chaque cas de test, on lance le même prompt deux fois : une fois avec le skill chargé, une fois sans. Même modèle, même température, tout pareil sauf le system prompt. Puis on note les deux sorties et on compare. Les cas de test sont en YAML déclaratif, avec notamment un champ `hallucinations` listant les méthodes qui n'existent pas dans le SDK WorkOS mais que les LLM inventent souvent (p. ex. `workos.sso.authenticate` — ça sonne juste, ça n'est pas réel). Le scoring couvre sept dimensions (exactitude des méthodes, couverture des paramètres, usage des variables d'environnement, imports, correction du flux, évitement des anti-patterns), pondérées en un score composite sur 100. Chaque hallucination pénalise de -5, plafonné à -25 ; une sortie sans hallucination obtient +5. 42 cas de test, les deux bras en parallèle ; le delta avec/sans skill dit si le skill aide, nuit, ou est sans effet.

**Le skill qui nuisait.** Un des skills générés a obtenu un score *négatif*. Le LLM produisait une *moins bonne* sortie avec le skill que sans. Le skill directory sync pour Ruby a atteint -12 %, le cas SSO de validation d'état CSRF -20 %. Je n'aurais attrapé ni l'un ni l'autre manuellement. Le skill enseignait correctement la nuance CSRF mais omettait l'étape de génération de l'URL d'auth, coûtant 20 points. Le LLM apprenait la mauvaise leçon du contexte. La percée est venue en sauvegardant les transcripts complets des deux runs et en construisant des outils pour les differ côte à côte : non pas « lequel a mieux noté ? » mais « qu'a réellement fait le LLM de différent ? ». Je voyais le skill introduire du bruit, trop de contexte tangentiel détournant le LLM du cœur de la tâche. C'est le moment où je suis passé de « les evals sont sans doute nécessaires » à « les evals sont comme je sais ce qui est réel ».

**Détecter ce qui n'est pas réel.** Le scorer gère la négation : si la sortie dit « n'utilisez pas `workos.sso.authenticate`, cette méthode n'existe pas », ce n'est pas une hallucination — le LLM met correctement en garde. Il vérifie les 30 caractères avant chaque correspondance pour des signaux de négation (« don't », « avoid », « should not », « never ») et des étiquettes (« anti-pattern », « trap »). Petit détail, mais c'est ce qui distingue un eval auquel on fait confiance d'un eval qui crie au loup.

### Même question, angle différent

Les deux systèmes ne partagent aucun code. Mais ils répondent à la même question : **comment mesurer la valeur quand le code est non-déterministe et les environnements très variables ?** Tous deux la résolvent pareil : 1) définir à quoi ressemble « bon » (pas la sortie exacte, mais les signaux de qualité) ; 2) mesurer statistiquement (taux de réussite et scores composites sur de nombreux essais) ; 3) tout sauvegarder (transcripts, diffs, scores, appels d'outils — quand ça échoue, il faut comprendre *pourquoi*) ; 4) bloquer les régressions (seuils automatiques empêchant de livrer pire qu'avant). Les tests disent « c'est cassé » ; les evals disent « ça empire », ou « ce truc que tu croyais utile nuit en fait ».

### L'eval aussi peut se tromper

Personne ne vous prévient : votre système d'évaluation peut avoir des bugs comme la chose qu'il évalue. J'ai vu 13 cas à delta négatif et j'ai eu peur. En enquêtant : les 13 « régressions » de flux étaient des bugs du scorer, pas des régressions de skill. Le scorer attendait les étapes dans un ordre conceptuel précis, mais les sorties avec skill suivaient un schéma diagnostic-d'abord (symptôme, cause, vérification, correctif) ; les sorties sans skill collaient par coïncidence à l'ordre attendu. Après être passé à une correspondance par proximité plutôt qu'une séquence stricte, ces 13 « régressions » sont devenues neutres à positives. La leçon : quand votre eval dit qu'une chose est cassée, suspectez d'abord l'eval — surtout au début.

### Construire la confiance avec un système bâti avec l'IA

Partie un peu gênante : j'ai construit les deux systèmes d'eval avec Claude Code. J'utilisais donc l'IA que je cherchais à évaluer pour bâtir le système d'évaluation. Les premiers jours, je faisais aveuglément confiance. J'ai même demandé à Claude : « Sommes-nous des graders ? A-t-on suivi les bonnes pratiques de ces docs ? » — littéralement demander à l'IA de corriger sa propre copie. C'est un peu comme une montre Apple qui suit votre rythme cardiaque : le chiffre absolu n'est pas parfait, mais je n'en ai pas besoin — j'ai besoin qu'elle me dise si ça va mieux ou moins bien. Une base de référence fiable, même imparfaite, vaut mieux qu'aucune.

Puis un doute : j'ai tapé dans Codex « je ne sais pas si les evals sont honnêtes sur l'utilité réelle de ces skills, peux-tu faire une analyse indépendante ? ». J'utilisais *deux* IA, Claude Code et Codex, pour se recouper. Codex signalait des hypothèses du scorer que Claude n'avait pas questionnées ; Claude trouvait des bugs d'implémentation invisibles à Codex. Mais l'IA vérifiant l'IA ne suffisait pas : il me fallait une vérité externe. J'ai lu trois ressources (le guide d'Anthropic « Demystifying Evals for AI Agents », l'analyse de Pragmatic Engineer, les bonnes pratiques d'évaluation d'OpenAI), puis je les ai données à Claude pour vérifier l'alignement de nos systèmes avec ces principes. Verdict : les fondamentaux étaient bons (structure A/B, scoring déterministe, jugements pass/fail mesurés en taux, notation par résultats), à affiner seulement.

### Si vous partez de zéro

- **Commencez par pass/fail.** Pas de système de scoring sophistiqué dès le premier jour : la question la plus simple d'abord (« est-ce que ça marche ? »), une base, puis on itère.
- **Les evals ne sont pas des tests.** Votre suite de tests doit être 100 % verte ; pas votre suite d'evals. Fixez des seuils statistiques et mesurez les tendances.
- **Sauvegardez les transcripts.** Les scores disent *quoi* ; les transcripts disent *pourquoi*.
- **Calibrez contre l'humain.** Un fichier JSONL où je marque « ship » / « no-ship » ; un script mesure l'accord du scorer automatique avec mon jugement. Plus de 20 % de désaccord → c'est le scorer qu'il faut corriger. Un scoring sans calibration humaine est juste une façon plus rapide de se tromper avec aplomb.
- **Mesurez ce qui vous importe vraiment.** Les scores génériques de « helpfulness » ne m'ont pas aidé : les signaux spécifiques au domaine battent les métriques génériques à chaque fois.
- **Vérifiez que vous ajoutez de la valeur, pas que vous dupliquez du savoir.** Si le LLM connaît déjà la réponse, votre skill est du poids mort ; s'il ajoute du bruit, il est nuisible. Le delta A/B est la seule façon honnête que j'aie trouvée d'y répondre.

### La confiance est une mesure

J'ai bâti deux systèmes différents en presque tout. Mais ils m'ont enseigné la même chose : la confiance n'est pas un sentiment, c'est un nombre — un taux de réussite, un delta, un garde-fou de régression. Quand on me demande « est-ce que cet outil IA marche vraiment ? », je n'ai plus à dire « je crois ». Je peux montrer les données. Et quand les données disent que quelque chose que j'ai construit nuit ? Je le corrige ou je le tue. C'est ce que m'a appris le skill au score négatif : mon intuition le disait utile, l'eval disait l'inverse. L'eval avait raison.

## Pourquoi ça compte

Les evals deviennent la discipline d'ingénierie indispensable pour livrer du logiciel à base d'IA en confiance — un test sérieux appliqué au non-déterministe. Un retour d'expérience concret et honnête, riche en pièges réels, précieux pour quiconque met des agents ou des features LLM en production.
