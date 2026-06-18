---
title: "Agentic coding and persistent returns to expertise"
date: 2026-06-18
url: https://www.anthropic.com/research/claude-code-expertise
authors: [Anthropic]
keywords: [agentic coding, expertise, Claude Code, productivité, human-AI collaboration]
theme: IA
tone: research
used_in: ["2026-06-18"]
---

## Résumé

Anthropic introduit un cadre d'analyse du codage agentique interactif à partir d'une étude préservant la vie privée de ~400 000 sessions Claude Code, menées par ~235 000 personnes entre octobre 2025 et avril 2026. Dans une session type, l'humain prend la plupart des décisions de planification (quoi faire) et l'agent celles d'exécution (comment le faire) ; plus la personne apporte d'expertise métier, plus l'agent abat de travail par instruction. Sur sept mois, la part des sessions consacrées au débogage a chuté de près de moitié et la valeur estimée d'une tâche type a augmenté d'environ 25 %. Le constat clé : ce n'est pas la maîtrise du code mais la compréhension du problème qui détermine le succès — les agents ne se substituent pas à l'expertise métier, ils la récompensent.

## Points clés

- Division du travail nette : en moyenne, les humains prennent ~70 % des décisions de planification, l'agent ~80 % des décisions d'exécution.
- L'expertise est spécifique à la tâche (pas le titre du poste) : un comptable qui dicte précisément ses règles de réconciliation est « expert » sur cette tâche ; un ingénieur senior posant sa première question Rust est « débutant ».
- Plus l'utilisateur est expert, plus chaque prompt déclenche d'actions et de sortie : ~5 actions et ~600 mots chez les novices, ~12 actions et ~3 200 mots chez les experts.
- Le succès vérifié passe de 15 % (novices) à 28-33 % (intermédiaires/experts) ; l'essentiel du gain se fait entre novice et intermédiaire, pas au-delà.
- L'occupation compte moins que l'expertise : dans les sessions produisant du code, chacune des dix plus grandes professions arrive à moins de sept points des ingénieurs logiciels en taux de succès.
- Composition du travail en évolution : le « fixing » de code cassé passe de 33 % à 19 % des sessions ; l'opération de logiciels, l'analyse de données et la rédaction progressent fortement.

## Analyse approfondie

### Principaux résultats

S'appuyant sur des travaux antérieurs, Anthropic introduit un cadre d'étude du codage agentique interactif fondé sur une analyse préservant la vie privée de ~400 000 sessions Claude Code menées entre octobre 2025 et avril 2026. L'étude évalue la composition des tâches, la collaboration humain-IA et les taux de succès.

Dans une session type, les personnes prennent la plupart des décisions de planification (quoi faire) et Claude la plupart des décisions d'exécution (comment le faire). Plus une personne apporte d'expertise dans un domaine, plus Claude réalise de travail par instruction. Sur les tâches de codage, chaque grande catégorie professionnelle réussit — c'est-à-dire accomplit ce que la personne s'était fixé, avec preuve vérifiable comme des tests qui passent ou du travail commité — à un taux presque équivalent à celui des ingénieurs logiciels, en moyenne.

Plus une personne a d'expertise dans son domaine, plus la session se termine souvent par un succès — même si l'écart entre utilisateurs intermédiaires et experts est modeste. Sur les sept mois observés, la part des sessions passées à déboguer a chuté de près de moitié, et l'usage s'est déplacé vers un usage agentique plus bout-en-bout : déployer et exécuter du code, analyser des données, rédiger des documents non-code. Sur ces sept mois, la valeur de la tâche type, estimée par comparaison à des offres de missions freelance, a augmenté dans presque tous les types de travail — d'environ 25 % en moyenne.

### Introduction

Le codage agentique a décollé. La part des projets GitHub avec activité d'agent de codage a plus que doublé depuis fin 2025, et les utilisateurs de Claude Code passent désormais en moyenne 20 heures par semaine sur l'outil. Des personnes sans expérience formelle de la programmation peuvent-elles réussir à piloter un agent dans un travail technique complexe ? Et que signifiera l'adoption et l'amélioration rapides de ces outils pour le travail intellectuel en général ?

Ce qui se passe dans Claude Code pourrait préfigurer l'avenir du travail intellectuel, à mesure que les agents s'intègrent à des tâches hors-code. Anthropic observe que Claude gère des tâches plus complexes et plus précieuses. En même temps subsiste une division du travail claire : les personnes décident quoi construire, l'agent décide comment.

L'étude montre aussi que c'est l'expertise métier, et non la maîtrise du code, qui amplifie l'usage efficace de l'outil. Les experts du domaine réussissent plus souvent et se remettent plus facilement des erreurs et malentendus. L'écart entre experts et intermédiaires reste toutefois modeste — une bonne maîtrise d'un domaine suffit à utiliser l'outil presque aussi efficacement que ceux qui en ont une connaissance approfondie.

Conséquence pour le marché du travail : dans ces données, le succès est déterminé par la qualité de compréhension du problème, pas par la formation au code. Si ces schémas se confirment à l'échelle de l'économie, cela suggère que les outils de codage agentique absorbent une partie du travail d'implémentation tout en récompensant ceux qui comprennent fermement les problèmes qu'ils traitent. Les agents de codage ne remplacent pas l'expertise métier : plus un travailleur en apporte, plus l'agent produit de travail de qualité.

### La division du travail

**Ce pour quoi les gens utilisent Claude Code.** Chaque session est classée dans l'un de neuf modes de travail. Quatre touchent directement au code : *construire* quelque chose de neuf, *réparer* quelque chose de cassé, *tester* du code, *orchestrer* d'autres agents ou pipelines. Une catégorie est l'*exploitation* de logiciels (déployer, configurer, exécuter, superviser). Deux relèvent de la réflexion sur quoi faire : *comprendre* un système existant et *planifier* un changement. Deux autres prennent des actions sans rapport direct avec le code : *analyser* des données et *communiquer* via des présentations et documents en prose.

Environ 56 % des sessions consistent à écrire (25 %), réparer (26 %) ou tester/orchestrer du code (5 %). L'exploitation logicielle représente 17 %, la planification ou l'exploration 14 %, et l'analyse ou la prose 13 %.

**Qui décide quoi.** Pour mesurer l'autonomie réelle, Anthropic distingue les décisions de *planification* (quoi faire, quelle approche, ce qui compte comme « terminé ») et d'*exécution* (quels fichiers changer, quel code écrire, quelles commandes lancer). En moyenne, les gens prennent ~70 % des décisions de planification mais seulement ~20 % des décisions d'exécution. Les personnes décident quoi construire, l'agent décide comment.

Côté actions : une session type comporte ~4 tours ; chaque prompt déclenche en moyenne une chaîne d'environ 10 actions de Claude (parfois plus de 100), et Claude écrit en moyenne 2 400 mots de sortie par tour. Quand l'utilisateur garde le contrôle de l'exécution (>80 % des décisions), Claude prend moins d'actions par tour (~8) ; quand Claude prend le contrôle de la planification (>80 %), il en prend le plus (~16).

**Niveau d'expertise.** À partir de chaque transcript, Claude note l'expertise apparente sur la tâche, sur une échelle de cinq points (novice à expert), en s'appuyant sur trois signaux : la précision du cadrage des instructions, ce que l'utilisateur demande de vérifier, et qui corrige qui. L'expertise est *spécifique à la tâche* et distincte du titre de poste. Dans les sessions novices types, chaque prompt déclenche ~5 actions de Claude et ~600 mots ; dans les sessions expertes, des chaînes plus de deux fois plus longues (~12 actions) portant cinq fois plus de sortie (~3 200 mots). Cet écart apparaît dans tous les types de travail et toutes les bandes de valeur, et reste statistiquement significatif (+9 % d'actions et +13 % de sortie par niveau d'expertise) dans une régression contrôlant le mode de travail, la valeur de la tâche, le mois, l'occupation et la famille de modèle.

### Qui utilise Claude Code, et pour quoi

**Les utilisateurs.** L'occupation est inférée à partir du transcript et mappée sur l'une des 23 grandes catégories de la taxonomie SOC du Bureau of Labor Statistics. Le classifieur est explicitement instruit de *ne pas* traiter l'acte de coder comme preuve d'un métier de la programmation : une session où un juriste construit un script pour signaler des clauses manquantes est rangée dans « professions juridiques ». L'occupation a pu être inférée dans ~70 % des sessions. La catégorie « Informatique et mathématiques » est la plus grande ; suivent les opérations commerciales et financières ; les arts, le design et les médias ; le management ; les sciences. Les professions hors-logiciel à plus forte croissance sont le management, la vente et le juridique.

**Le travail.** La composition a beaucoup changé entre octobre 2025 et avril 2026. Le changement le plus net : la part des sessions de réparation de code cassé est passée de 33 % à 19 %. À la place, le travail *autour* du code a augmenté : exploitation logicielle de 14 % à 21 %, écriture et analyse de données à peu près doublées (de ~10 % à ~20 %). La valeur économique estimée de la session moyenne a augmenté de 27 % entre octobre et avril, avec des hausses d'environ un tiers ou plus pour les tâches de construction (~43 %), d'exploitation (~34 %) et de réparation (~32 %). Ces estimations sont grossières et servent surtout à comparer les tâches entre elles dans le temps.

### Le succès dépend de ce que l'utilisateur apporte

À travers toutes les mesures, plus une personne montre d'expertise dans une session, plus la probabilité de succès est élevée. L'essentiel du gain se concentre dans le bas de l'échelle : l'écart novice → intermédiaire est plus grand qu'intermédiaire → expert.

Anthropic mesure le succès via deux indicateurs complémentaires fondés sur le transcript : le *succès jugé* (un classifieur décide si la personne a réussi ce qu'elle voulait : réussi, partiellement réussi, échoué, pas d'objectif clair) et le *succès vérifié*, qui exige en plus au moins un signal dur vérifiable (commits, pull requests, suites de tests qui passent, confirmation explicite de l'utilisateur).

Une session notée novice atteint le succès vérifié 15 % du temps et au moins un succès partiel 77 % du temps. Une session notée intermédiaire ou plus atteint le succès vérifié 28-33 % du temps et le succès partiel 91-92 %.

Quand une session *rencontre des difficultés* (erreur, test échoué, tentatives répétées, frustration de l'utilisateur), la part de succès vérifiés monte de 4 % (novice) à 15 % (expert), contrôles inclus. Inversement, 19 % des sessions où l'utilisateur paraît novice sont *abandonnées* (jugées échouées et zéro ligne de code écrite), contre 5-7 % pour les autres : les moins expérimentés abandonnent plus souvent quand ils peinent. Une partie de la valeur de l'expertise tient à la capacité d'orienter l'agent dans la bonne direction.

**L'occupation compte peut-être moins que l'expertise.** Les professions liées au logiciel atteignent le succès vérifié dans ~30 % des sessions, les autres dans ~26 % (34 % vs 29 % parmi les sessions produisant du code). Sous la définition plus large, l'écart se réduit (89 % vs 88 % de succès au moins partiel). Cet écart de cinq points est faible et n'a ni grandi ni rétréci en sept mois. Les professions de management affichent même le plus haut taux de succès vérifié, légèrement au-dessus des ingénieurs logiciels — peut-être des compétences de pilotage transférables, peut-être un effet de mesure (les managers communiquent davantage quand ils obtiennent ce qu'ils demandent).

### Perspectives

Le codage agentique amplifie certaines formes de savoir et de compétence tout en se substituant à d'autres. Dans les sessions produisant du code, chaque grande profession réussit à quelques points des professions logicielles : les agents rendent un bagage de codeur moins déterminant pour réussir à programmer. En même temps, les sessions réussies montrent davantage d'expertise métier : les sessions notées expert atteignent le succès vérifié plus de deux fois plus souvent que les novices, et face aux difficultés les novices abandonnent à un taux bien supérieur. La capacité d'orienter Claude vers le succès vient davantage de la maîtrise d'un domaine que de la capacité à écrire du code — et les gains viennent surtout de la *compétence*, pas de la *maîtrise absolue* : une bonne prise en main du domaine capte l'essentiel du bénéfice.

Ces résultats sont préliminaires : on ne mesure pas les résultats réels (le code écrit est-il utilisé ou jeté ?), l'usage non-interactif (une part substantielle de l'activité) est exclu, et toutes les classifications reposent sur la lecture des transcripts par un modèle. Anthropic surveillera notamment deux bascules : si les rendements de l'expertise se mettent à diminuer (les modèles fourniraient alors le jugement que les utilisateurs apportent aujourd'hui), et si la part de sessions réussies par des non-informaticiens continue de croître (la production logicielle deviendrait une part du travail ordinaire de tous les métiers).

Citation : Hitzig, Massenkoff, Lyubich, Heller, McCrory, *Agentic coding and persistent returns to expertise*, Anthropic, 2026-06-16.

## Pourquoi ça compte

C'est un signal de premier ordre, données à l'appui, sur la recomposition du travail technique à l'ère des agents : l'expertise métier ne disparaît pas, elle devient le multiplicateur. De quoi nourrir la réflexion des dirigeants tech sur le recrutement, la montée en compétence et la valeur réelle dans un monde où coder se démocratise.
