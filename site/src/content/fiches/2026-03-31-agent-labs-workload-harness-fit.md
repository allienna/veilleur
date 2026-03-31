---
title: "Agent Labs: Workload-Harness Fit"
date: 2026-03-31
url: https://www.akashbajwa.co/p/agent-labs-workload-harness-fit
authors: [Akash Bajwa]
keywords: [agent labs, modèles verticaux, entraînement RL, agent engineering, workload-harness fit]
theme: IA
tone: opinion
used_in: ["2026-03-31"]
---

## Résumé

Akash Bajwa analyse comment plusieurs agent labs (Cursor, Intercom, Cognition, Decagon) ont récemment publié des modèles verticaux spécialisés, concrétisant une stratégie d'intégration verticale par l'entraînement de modèles pour réduire leur dépendance aux grands fournisseurs. L'article identifie deux camps : ceux qui investissent dans l'entraînement complet de modèles et ceux qui se concentrent sur l'ingénierie agent (harness, prompts, orchestration). Bajwa propose un cadre d'analyse — le workload-harness fit — basé sur quatre dimensions (volume, valeur, vérifiabilité, horizon temporel) pour déterminer quelle approche est la plus pertinente selon le type de charge de travail.

## Points clés

- Deux approches s'opposent dans les agent labs : l'entraînement de modèles verticaux spécialisés (fine-tuning, RL) versus l'ingénierie agent pure (gestion du contexte, tool use, orchestration de tâches longues)
- Le cadre workload-harness fit évalue les charges de travail selon quatre axes : volume d'exécution, valeur par exécution, propriétés de vérification du signal de récompense, et horizon temporel des tâches
- Cursor a entraîné Composer 2 à partir de Kimi K2.5 (1 000 milliards de paramètres) avec une infrastructure colossale : trois régions GPU, des centaines de milliers de VM isolées, plus de 500 pods/seconde, et environ 50 contributeurs
- Les benchmarks publics comme SWE-bench sont de plus en plus peu fiables — CursorBench exige des modifications médianes de 181 lignes contre 7-10 pour SWE-bench, avec des prompts plus courts et ambigus reflétant la réalité
- Des fournisseurs d'infrastructure comme Prime Intellect et Thinking Machine Labs démocratisent l'accès à l'entraînement, permettant à davantage d'entreprises applicatives de se lancer
- Malgré le risque d'obsolescence face aux modèles frontier toujours plus puissants, les entreprises appliquées créeront une valeur durable grâce à leur focus produit et leur connaissance fine des problèmes clients

## Analyse approfondie

### Le contexte : l'intégration verticale par l'entraînement

Plusieurs agent labs — Cursor, Intercom, Cognition et Decagon — ont publié des modèles verticaux frontier ces derniers mois, concrétisant l'un des scénarios plausibles pour les entreprises de la couche applicative : s'intégrer verticalement par l'entraînement de modèles afin de réduire leur dépendance aux grands labs et protéger leurs marges.

La direction était claire dès que des entreprises comme Thinking Machine Labs ont commencé à abstraire les primitives d'infrastructure, comme Bajwa l'avait couvert en octobre dernier :

> Le fine-tuning et le RL sont en cours de productisation et d'abstraction pour que les agent labs puissent capitaliser sur leurs avantages en matière de données et de distribution. Ces abstractions ouvrent la voie pour que les agent labs démarrent comme consommateurs d'API des model labs, capturent les traces et les évaluations, puis entraînent des modèles étroits (embeddings, autocomplétion, routeur, politique) avant de tenter des runs d'entraînement plus importants avec des modèles open source.

D'autres fournisseurs d'infrastructure se sont positionnés pour catalyser ce marché. Prime Intellect a décrit la vision de son offre d'entraînement récemment lancée : si chaque entreprise avait le même accès à l'infrastructure d'entraînement frontier, la créativité collective du marché débloquerait bien plus de percées.

### Deux camps

Il existe aujourd'hui deux camps quant à la manière dont les agent labs vont concentrer leurs ressources techniques.

Le premier argue que les exemples du coding et du support client seront suivis par les leaders de marché dans d'autres verticales, avec un effort de recherche centré sur l'entraînement et la mise à jour des poids des modèles.

Le second camp s'oppose à tout entraînement, préférant concentrer les talents de recherche sur l'ingénierie agent — gestion du contexte, tool use, tâches à long horizon, et tout ce qui rend un modèle prêt pour la production sur une tâche donnée — autrement dit, construire le meilleur « harness ».

### Le cadre workload-harness fit

La bonne approche dépend de la charge de travail. Les tâches varient selon plusieurs dimensions :

**Volume** — Combien de fois par jour ou par semaine cette tâche s'exécute-t-elle ? Cela détermine à la fois l'incitation économique à réduire le coût par requête et la vitesse à laquelle le volant de données génère du signal d'entraînement. Les 2 millions de conversations hebdomadaires d'Intercom se situent à un extrême ; les analyses stratégiques trimestrielles d'un cabinet de conseil boutique à l'autre.

**Valeur par exécution** — Quel est l'impact économique de chaque complétion de tâche ? Une déviation de ticket support peut économiser 3 à 5 dollars. Un diagnostic médical correct ou un déploiement en production réussi peut valoir des milliers. Cela détermine combien investir dans la qualité du modèle par requête et quelle tolérance à l'erreur est acceptable.

**Propriétés de vérification** — Les domaines diffèrent fondamentalement dans la vérifiabilité de leurs signaux de récompense. Sean Cai a identifié trois propriétés : la véracité (quelle confiance a-t-on que le signal est correct ?), la prolifération (à quel point le signal est-il largement suivi et disponible ?), et l'asymétrie (à quel point l'expertise nécessaire pour juger de la correction est-elle rare et coûteuse ?).

**Horizon temporel** — Combien de décisions séquentielles, d'interactions avec des outils et de changements de contexte la tâche requiert-elle ? Une complétion de code en un tour est à horizon court. Un refactoring multi-fichiers avec débogage est moyen. La conception d'une expérience scientifique sur plusieurs semaines est à horizon extrêmement long. Des horizons plus longs rendent l'attribution de récompense et la génération de rollouts d'entraînement exponentiellement plus difficiles.

### Études de cas

**Cursor et Cognition** — Charges de travail à haut volume, haute valeur (surtout avec la pénétration entreprise croissante), vérification modérée, et horizon temporel de plus en plus long avec les agents cloud/background. Ces qualités justifient le pré-entraînement et le post-entraînement avec une ingénierie de récompense sophistiquée et multidimensionnelle. La vérification modérée signifie qu'il faut investir lourdement dans la construction de signaux de récompense composites (correction + style + efficacité + pénalités comportementales). Cursor fait explicitement des mises à jour de paramètres complets parce que la barre est très haute quand on essaie de relever le plafond de l'ingénierie logicielle, pas le plancher.

**Intercom et Decagon** — Charges de travail à haut volume, valeur faible à modérée, vérification propre, horizon court à moyen. Chaque exécution a une faible valeur individuelle mais le volume agrégé est massif, créant une forte incitation économique à réduire le coût par requête. La vérification est propre — le ticket a été résolu ou non. Le volume justifie l'investissement dans un pipeline complet de post-entraînement sur un modèle open source solide, rien que par les économies d'inférence, sans compter les améliorations de performance. Il est à noter qu'Intercom a recruté tôt une équipe de chercheurs, avant des entreprises comme Decagon et Sierra.

**Harvey et Legora** — Volume modéré, haute valeur, vérification modérée, horizon moyen. Le verdict n'est pas encore rendu. Harvey aurait tenté des runs d'entraînement par le passé, tandis que Legora s'est tenu à l'écart de tout entraînement pour se concentrer entièrement sur la construction du meilleur harness pour les modèles d'Anthropic.

### Composer 2 de Cursor : l'infrastructure requise

Le développement de Composer 2 suit un processus en deux étapes. La première étape de pré-entraînement continu a pris un modèle open-weight existant (Kimi K2.5, un modèle d'un billion de paramètres de Moonshot AI) et l'a entraîné davantage sur un jeu de données massif dominé par le code, étendant progressivement sa capacité à traiter des séquences de code plus longues. La seconde étape d'apprentissage par renforcement est celle où le modèle apprend à travailler comme développeur : il est plongé dans des environnements de codage réalistes, reçoit des tâches dérivées de vrais workflows développeur (itération de fonctionnalités, débogage, refactoring, revue de code, documentation), et est évalué sur la qualité de ses solutions de bout en bout. Cursor a démontré empiriquement que la première étape prédit de manière fiable le succès de la seconde : une perte de pré-entraînement plus basse se traduit systématiquement en une récompense RL plus élevée.

Le run d'entraînement a couvert trois régions GPU et quatre régions CPU à l'échelle mondiale. La phase RL seule a nécessité des centaines de milliers de machines virtuelles isolées (des VM Firecracker sur la plateforme de calcul interne de Cursor, Anyrun) pour simuler des environnements de développement réalistes, chacune capable d'exécuter un setup de développement complet incluant un navigateur. Ces environnements devaient être démarrés à un rythme dépassant 500 pods par seconde pour suivre la nature en rafales des charges d'entraînement RL. Cursor s'est associé à Fireworks AI pour l'inférence pendant l'entraînement, exécutant des clusters distribués aux États-Unis et en Europe. L'équipe a également écrit des kernels GPU personnalisés ciblant le dernier matériel Blackwell de NVIDIA, incluant un format numérique modifié en basse précision qu'ils ont jugé nécessaire pour éviter l'instabilité de l'entraînement. La liste des contributeurs atteint environ 50 personnes — une véritable opération mondiale d'infrastructure ML.

### Ingénierie de récompense et façonnage comportemental

Plusieurs des choix de conception les plus conséquents de Cursor concernent la manière dont le modèle est récompensé pendant l'entraînement RL. Au-delà du signal de correction principal, Cursor applique une pénalité de longueur non linéaire qui pénalise le modèle plus sévèrement pour un effort inutile sur des tâches simples tout en tolérant un raisonnement prolongé sur des tâches complexes — incitant le modèle à être rapide quand il le peut et approfondi quand il le doit. Ils superposent des récompenses auxiliaires pour le style de code, la qualité de communication et des comportements spécifiques au produit, incluant des pénalités explicites pour des patterns comme créer des éléments TODO et les laisser inachevés. L'équipe surveille activement les comportements problématiques émergents pendant l'entraînement et introduit des récompenses correctives de manière réactive — par exemple, quand le modèle a commencé à laisser des chaînes de pensée dans les commentaires de code ou s'est effondré sur l'utilisation exclusive de l'outil terminal. La technique d'auto-résumé, héritée de Composer 1.5, permet au modèle d'enchaîner plusieurs générations avec des résumés intermédiaires au sein d'un seul rollout d'entraînement, la récompense finale remontant pour surpondérer les bons résumés et sous-pondérer les mauvais.

### Philosophie de benchmarking : pourquoi CursorBench compte

Les benchmarks publics existants sont des indicateurs de moins en moins fiables de la qualité réelle des agents de codage, avec quatre problèmes structurels : inadéquation de domaine (SWE-bench se concentre étroitement sur la correction de bugs), sur-spécification des prompts (les benchmarks publics supposent des instructions anormalement explicites), contamination des données (OpenAI a suspendu le reporting SWE-bench Verified après avoir découvert que les modèles pouvaient générer des solutions de mémoire), et périmètre d'évaluation étroit (uniquement la correction fonctionnelle, ignorant la qualité du code, la latence, le coût et le comportement interactif). La réponse de Cursor est CursorBench, une suite d'évaluation interne construite à partir de vraies sessions de codage de leur équipe d'ingénierie. Le contraste structurel est net : les tâches CursorBench exigent des modifications médianes de 181 lignes de code contre 7-10 pour SWE-bench, tandis que les prompts sont significativement plus courts et ambigus — reflétant la nature sous-spécifiée des vraies requêtes développeur. Le benchmark est continuellement rafraîchi à mesure que les workflows évoluent, chaque itération augmentant en complexité.

### La résilience du marché applicatif

Malgré l'effort colossal, entraîner Composer 2 était impératif pour Cursor. Les développeurs choisiront le meilleur harness pour leurs charges de travail, et Composer 2, un modèle à l'état de l'art à une fraction du coût, a une chance de reconquérir des charges de travail anciennes et nouvelles.

Il existe un risque réel d'obsolescence face aux grands modèles, mais cette logique ne diffère guère de dire que deux entreprises (ou une seule, si l'on en croit la plupart) captureront toute la valeur créée par l'IA dans les décennies à venir. Comme Bret Taylor (Sierra) l'a noté : « Si nous mettions en pause le développement des modèles, nous aurions encore des milliers de milliards de dollars de valeur économique. » La plupart des utilisateurs métier veulent des solutions concrètes à leurs problèmes, et ils veulent une entreprise qui serve leurs problèmes uniques de manière très spécifique et sur mesure.

Les modèles s'améliorent plus vite que quiconque n'aurait pu l'imaginer, mais le focus compte, comme OpenAI l'a désormais admis. Les startups créeront une valeur durable, et la différenciation technique jouera un rôle sous une forme ou une autre.

## Pourquoi ça compte

Cet article fournit le cadre analytique le plus complet à ce jour pour comprendre pourquoi certains agent labs entraînent leurs propres modèles tandis que d'autres misent tout sur l'ingénierie agent — une distinction stratégique cruciale pour toute entreprise applicative IA qui doit décider où investir ses ressources techniques limitées.
