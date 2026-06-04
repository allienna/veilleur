---
title: "Running an AI-native engineering org"
date: 2026-06-04
url: https://claude.com/blog/running-an-ai-native-engineering-org
authors: [Claude Code team, Anthropic]
keywords: [organisation AI-native, goulot vérification, revue de code, planification JIT, processus]
theme: Leadership
tone: opinion
used_in: ["2026-06-04"]
---

## Résumé

Un responsable de l'équipe Claude Code décrit comment l'ingénierie agentique a redessiné l'organisation. Pendant des années, la bande passante d'ingénierie était la ressource chère autour de laquelle on construisait waterfall puis agile. Désormais écrire du code, des tests et refactorer ne ralentit quasiment plus l'équipe — ce sont la vérification, la revue de code et la sécurité qui sont devenues le goulot. L'équipe a réécrit ses normes : planification just-in-time, contexte demandé à Claude plutôt qu'à l'auteur, revue humaine ciblée sur l'expertise, et rôles qui se brouillent. Trois principes restent non négociables, et trois métriques permettent de vérifier que les nouvelles pratiques tiennent.

## Points clés

- Sur l'équipe Claude Code, coder/tester/refactorer ne ralentit quasiment plus — vérification, revue et sécurité ont pris la place du goulot.
- **Planification** : roadmaps à six mois → planification just-in-time (prototype, utilisateurs internes, feedback). Une roadmap à six mois était périmée dès le troisième mois.
- **Contexte** : on ne cherche plus l'auteur du commit, on demande à Claude — puis on se demande si la question peut être automatisée.
- **Revue de code** : Claude gère style, lint, bugs, tests ; l'humain intervient là où l'expertise compte (légal, sécurité, sens produit).
- **Rôles** : les PM codent, les ingénieurs font du design/contenu ; recruter des « creative builders » et des experts systèmes, pas du débit brut.
- Trois principes non négociables : dogfooder le produit, garder l'équipe plate (managers IC d'abord), tuer sans hésiter les process obsolètes.
- Trois métriques à suivre : temps de ramp d'onboarding ↓, cycle time des PR ↓, commits assistés par Claude ↑ (≈100 % chez eux). Ne pas confondre débit et succès.

## Analyse approfondie

L'auteur ouvre sur une perspective historique : pendant des années, la bande passante d'ingénierie était la partie chère de la construction d'applications, et chaque process — waterfall d'abord, agile ensuite — était bâti autour de ce coût. Ayant débuté au début des années 2000 sur Visual Studio, à l'époque des livraisons sur CD-ROM avec des deadlines de fabrication, il a vu le métier passer à la distribution en ligne puis au déploiement continu. Aujourd'hui la manière de travailler change à nouveau, cette fois autour du temps et du nombre de personnes nécessaires pour écrire du logiciel.

Sur l'équipe Claude Code, écrire du code, des tests et refactorer ne ralentit quasiment plus personne. Mais les goulots n'ont pas disparu quand le code agentique a supprimé le besoin de taper du code : la vérification, la revue de code et la sécurité ont pris leur place. On peut tous générer beaucoup de code très vite, ce qui soulève de nouvelles questions : ce code est-il correct ? Comment est-il maintenu ? Et la question récurrente des autres responsables : comment les humains tiennent-ils le rythme des revues de code ?

**Les process qui ont silencieusement cessé de fonctionner.** On met en place des process pour combler un manque ; mais quand ce manque disparaît, les process devenus obsolètes ne s'effacent pas d'eux-mêmes. En adoptant le code agentique comme mode de travail par défaut, l'équipe a vu beaucoup de ses process tomber. Les normes réécrites :

- *Planification — basculer les roadmaps en just-in-time.* L'ancienne norme : beaucoup de pré-planification car le temps de code coûtait cher. À son arrivée, l'auteur avait écrit une bonne roadmap à six mois — qui, à cause de Claude Code, était périmée dès le troisième mois. Il appelle son nouveau modèle la planification JIT (comme le JIT compiling) : faire juste la bonne quantité, au bon moment. Le rituel a glissé des design docs vers des discussions en PR ou des prototypes. Peu de revues produit : on prototype, on met des utilisateurs internes dessus, on agit sur leur feedback.

- *Recueil de contexte — demander à Claude, pas à l'auteur.* Avant, la première étape pour répondre à une question était de trouver qui avait écrit le code. Comme tous les PR sont désormais assistés par Claude, « qui a fait ce changement ? » ne suffit plus. La nouvelle norme : descendre d'un cran — de quoi avez-vous *vraiment* besoin ? (qui a causé une régression ? un expert pour répondre à un client ? le contexte d'une décision ?) On pose la question à Claude, qui peut souvent y répondre directement. Et toujours se demander : peut-on l'automatiser ? Exemple : faire résumer chaque matin les canaux de feedback client par Claude est passé d'un rituel manuel au café à une tâche tournant automatiquement en arrière-plan.

- *Revue de code — faire confiance mais vérifier.* L'équipe utilise massivement Code Review : Claude gère style et lint, les demandes de feedback sur PR, la détection et correction de bugs avant un commit complet, l'ajout de tests. L'humain reste indispensable pour l'expertise : revue légale (tolérance au risque avec le partenaire juridique), frontières de confiance et code sensible à la sécurité (experts du domaine), sens et goût produit (PM et designers). Il faut réévaluer en continu, car le bon équilibre confiance/vérification bougera à mesure que les modèles s'améliorent.

- *Composition d'équipe — les rôles se brouillent.* Les PM codent beaucoup maintenant ; des codeurs non traditionnels font davantage d'ingénierie, et des ingénieurs prennent en charge du contenu et du design. L'auteur a privilégié deux profils : les *creative builders* dotés de sens produit, et les ingénieurs à forte expertise systèmes (il manquait ces derniers pour bâtir Claude Code on the Web). Ce qu'il valorise *moins* : le débit brut, que les modèles gèrent.

Un tableau résume le avant/après sur ces quatre axes (planification, contexte, revue, composition).

**Comment ces normes ont été déployées.** Certaines ont été imposées comme principes d'équipe non négociables, d'autres laissées à l'initiative de petits sous-groupes (pods). Les « must dos » du noyau Claude Code : (1) *dogfooder sans relâche son produit* — chaque membre, y compris les partenaires transverses, utilise Claude Code (et Claude Cowork) ; (2) *garder l'équipe aussi plate que possible* — chaque manager commence comme IC pour comprendre ce qu'est être ingénieur chez Anthropic, une seule mission d'équipe, les managers soutenant des pods tout en gardant l'agilité ; (3) *ne pas hésiter à tuer les process qui ne fonctionnent plus* — chacun a la permission explicite de questionner et supprimer les anciens process. Dans ce cadre restreint, chaque pod garde beaucoup d'autonomie sur le triage, les rituels de planification et l'ordre de « Claudification » des workflows.

**Savoir que les nouveaux process tiennent.** Trois chiffres à suivre dès maintenant : (1) *le temps de ramp d'onboarding baisse* — ingénieurs, designers ou PM deviennent efficaces plus vite (les ingénieurs livrent du vrai code dès leur première semaine) ; (2) *le cycle time des PR baisse* — intéressant à creuser, car il révèle où le pipeline peine à passer à l'échelle (CI/build qui suivent mal le volume de code) ; (3) *les commits assistés par Claude augmentent* — chez eux, par défaut, chaque commit est assisté par Claude ; l'auteur n'en a pas vu un seul non assisté depuis quatre mois. Avertissement : ne pas confondre débit et succès — le débit n'est qu'une métrique, la vraie mesure est le problème qu'on cherche à résoudre.

**Pour démarrer.** S'il ne devait retenir qu'une chose : *choisissez votre workflow le plus bruyant* — le plus coûteux, celui que l'équipe redoute. Et demandez : sert-il encore son objectif ? Si oui, peut-on l'automatiser ? Il raconte une réunion hebdomadaire coûteuse où tout le monde était sur son ordinateur sauf au moment de son propre point de statut ; une simple question — « pourquoi tient-on encore cette réunion ? » — a suffi à la supprimer.

## Pourquoi ça compte

Retour d'expérience direct, de l'intérieur d'Anthropic, sur la réorganisation d'une équipe d'ingénierie quand le code n'est plus le goulot. Concret et transposable : quels process tuer, quels rôles repenser, quelles métriques suivre — sans confondre débit et valeur.
