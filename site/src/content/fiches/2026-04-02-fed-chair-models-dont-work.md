---
title: "The Fed Chair Just Said What AI Leaders Won't: The Models Don't Work"
date: 2026-04-02
url: "https://vinvashishta.substack.com/p/the-fed-chair-just-said-what-ai-leaders"
authors: ["Vin Vashishta"]
keywords: [LLM, systèmes complexes, prédiction, causalité, architectures agentiques]
theme: "IA"
tone: opinion
used_in: ["2026-04-02"]
---

## Résumé

Le président de la Fed, Jerome Powell, a admis publiquement que les modèles économiques ne fonctionnent pas pour prédire l'économie. Vin Vashishta en tire un parallèle direct avec les LLM : excellents pour comprendre le langage, ces modèles sont fondamentalement incapables de prédire, prescrire et diagnostiquer dans des systèmes complexes. Trois barrières structurelles expliquent cette limite : manque de données interventionnelles, absence de compréhension causale, et contraintes de calcul pour modéliser des systèmes dynamiques. L'auteur explore les pistes de recherche les plus prometteuses — IA causale, Physics-Informed Neural Networks, et modèles multi-échelles — qui ouvrent la voie vers des architectures capables de dépasser ces limites.

## Points clés

- Les LLM sont entraînés à prédire le prochain token, pas à modéliser l'évolution d'un système — ce sont des problèmes fondamentalement différents
- Prédire, prescrire et diagnostiquer dans des systèmes complexes requiert un raisonnement causal que les LLM ne peuvent simuler, même à grande échelle
- La majorité des données disponibles est observationnelle ; ce qu'il faudrait, c'est des données interventionnelles impossibles à collecter à l'échelle économique
- La critique de Lucas s'applique bien au-delà de l'économie : tout système qui intègre des agents intelligents est modifié par l'acte même de le modéliser
- Les recherches les plus prometteuses combinent inférence causale, réseaux de neurones informés par la physique (PINNs), et architectures multi-agents apprises
- Construire des modèles fiables de systèmes complexes nécessitera des architectures, des stratégies d'information et des paradigmes de calcul radicalement différents de ceux qui ont produit les LLM actuels

## Analyse approfondie

Le président de la Fed Powell a été interrogé hier sur ce qu'il ne croyait pas concernant les marchés, et sa réponse a pris une direction que peu de gens attendaient. Powell a déclaré ne pas faire confiance aux modèles utilisés pour prédire les marchés ou l'économie au sens large. « Personne n'a été capable de prédire l'économie avec succès. »

Et il a raison.

Bien que les LLM aient réalisé des progrès considérables en termes de capacités, ils sont mauvais pour prédire, prescrire et diagnostiquer. Ils sont construits pour comprendre le langage sous plusieurs formes (images, vidéo, texte, génétique, code, chimie, etc.). Mais ils ne comprennent pas les systèmes complexes au-delà de ceux définis par le langage sous une forme ou une autre.

Nous sommes devenus bons pour effectuer ces trois opérations à petite échelle, mais à mesure que les systèmes gagnent en complexité ou en dynamisme, même les modèles conçus à ces fins commencent à nous faire défaut.

Trois barrières principales nous empêchent de résoudre ce type de modèle de la même manière que nous avons résolu le langage :

1. Manque de données
2. Manque de compréhension causale
3. Manque de puissance de calcul pour modéliser des systèmes complexes

Si l'on veut construire des plateformes agentiques fiables, les LLM ne suffisent pas. Dans cet article, l'auteur explique pourquoi deux couches (Agentique et Information) dans son architecture de plateforme IA agentique sont critiques pour la cinquième (Environnements de Multi-Simulation). La tokenomique se concentre aujourd'hui sur les LLM comme modèle frontier principal, mais il existe une autre catégorie encore plus exigeante en calcul et en données.

### Pourquoi les LLM échouent ici

Il faut être précis sur les raisons pour lesquelles les LLM sont insuffisants ici, car le mode d'échec n'est pas évident. Les LLM sont entraînés à prédire le prochain token dans une séquence. C'est une tâche de compression et de récupération. Ils construisent des représentations statistiques du fonctionnement du langage, et ces représentations sont utiles pour la synthèse, la traduction, la génération de code et le raisonnement sur des concepts exprimables en texte.

Les modèles prédictifs sont fondamentalement différents. Un modèle prédictif tente de prévoir l'état futur d'un système à partir de son état actuel, de ses entrées, et des dynamiques qui régissent l'interaction de ces entrées. Quand on prédit la trajectoire d'un ouragan, on résout des équations différentielles décrivant la dynamique des fluides, la thermodynamique et l'effet de Coriolis.

Quand on prédit comment un marché réagira à une hausse des taux, on a besoin d'un modèle qui capture la chaîne causale allant de la politique monétaire au comportement de prêt, à la tarification des actifs, puis au sentiment des consommateurs. Ce sont des problèmes d'évolution d'état et de dynamique des systèmes, pas des problèmes de prédiction de token. À un moment, il sera peut-être possible d'exprimer les espaces d'états, les espaces d'action et les graphes causaux d'une manière que les Transformers sauront apprendre.

Mais nous n'en sommes pas là.

Les modèles prescriptifs vont encore plus loin. Ils ne se contentent pas de prévoir ce qui va se passer ; ils répondent à la question de ce qu'il faut faire à ce sujet. Un modèle prescriptif optimise des décisions ou des actions en fonction d'une fonction objectif tout en respectant des contraintes.

Les protocoles de dosage médicamenteux, le routage de la chaîne d'approvisionnement sous perturbation, et le rééquilibrage de portefeuille en marchés volatils sont tous des problèmes prescriptifs qui nécessitent un raisonnement contrefactuel. Si on prend l'action A plutôt que l'action B, qu'est-ce qui change en aval ? Les LLM ne peuvent pas faire cela. Ils peuvent en parler, mais ils ne peuvent pas simuler la mécanique causale d'une décision se propageant à travers un système.

Les modèles diagnostiques fonctionnent dans la direction temporelle opposée. Ils observent l'état actuel d'un système et raisonnent en arrière pour identifier ce qui l'a amené là. L'analyse des causes racines en fabrication, le diagnostic différentiel en médecine, et l'analyse des défaillances dans des infrastructures complexes requièrent tous cette capacité.

Le modèle doit distinguer corrélation et causalité, entre symptômes qui co-occurent et mécanismes qui produisent effectivement la défaillance. C'est précisément le type de raisonnement pour lequel les architectures à correspondance de patterns statistiques ne sont pas conçues. Bien que les LLM soient capables d'une découverte causale limitée dans plusieurs domaines, ils ne sont pas prêts pour des tâches d'analyse de systèmes plus complexes.

### Complexité vs complication

Il y a une différence entre compliqué et complexe. Un système compliqué, comme un moteur à réaction, comporte de nombreuses pièces, mais celles-ci interagissent de manière prévisible et bien caractérisée. On peut modéliser un moteur à réaction avec une précision extraordinaire.

Un système complexe, comme une économie nationale ou un climat planétaire, est différent. Les composants interagissent via des boucles de rétroaction créant des comportements émergents. De petites perturbations peuvent se transformer en effets massifs et non linéaires. Le système est souvent dépendant du chemin parcouru, ce qui signifie que son état futur dépend non seulement de son état actuel, mais de la séquence spécifique d'états traversés.

Les systèmes dynamiques ajoutent une autre couche de difficulté. Ce sont des systèmes où les règles régissant le comportement changent elles-mêmes au fil du temps, comme les marchés financiers. Les participants aux marchés s'adaptent aux nouvelles informations, changent de stratégies et modifient les dynamiques mêmes que les modèles tentent de capturer.

C'est la critique de Lucas en économie, et elle s'applique bien plus largement que les économistes ne l'avaient initialement prévu. Tout système où des agents intelligents (personnes et algorithmes complexes) font partie du système présentera cette propriété : l'acte de modéliser le système le modifie.

### Barrière 1 : Manque de données

Cette contrainte est la plus sous-estimée. Nous vivons à une époque de données abondantes, il semble donc bizarre de prétendre qu'elles manquent. Cependant, les données dont nous disposons en abondance sont du mauvais type pour modéliser des systèmes complexes.

La plupart des données collectées sont observationnelles. On enregistre ce qui s'est passé. Ce dont on a besoin pour la modélisation prédictive et prescriptive, ce sont des données interventionnelles décrivant ce qui se passe quand on change quelque chose, toutes choses égales par ailleurs.

Les essais contrôlés randomisés génèrent des données interventionnelles, mais on ne peut pas mener un tel essai sur l'économie mondiale. On ne peut pas assigner aléatoirement des politiques de taux d'intérêt à des univers parallèles. C'est là que les simulations et les modèles de marché présentent un potentiel significatif, mais comme le souligne Powell, ces modèles n'ont pas encore atteint une fiabilité élevée.

Même les données observationnelles disponibles sont éparses par rapport à la dimensionnalité des systèmes à modéliser. Une économie nationale a des millions d'agents en interaction, des milliers de prix de matières premières, des centaines de variables de politique, et les relations entre eux évoluent dans le temps. On disposera peut-être de décennies de données macroéconomiques, mais c'est une poignée de points dans l'espace des états possibles du système.

Vient ensuite le problème de mesure. Beaucoup des variables les plus importantes dans les systèmes complexes sont latentes. La confiance des consommateurs, la confiance institutionnelle et la fragilité des chaînes d'approvisionnement sont des forces réelles qui pilotent le comportement du système, mais on les mesure via des proxys bruités. L'écart entre ce qu'on peut observer et ce qui compte vraiment est énorme.

### Barrière 2 : Manque de compréhension causale

C'est la contrainte la plus profonde, et c'est elle qui sépare notre succès avec les LLM de nos difficultés avec les systèmes complexes. Le langage a une structure qui peut être apprise à partir de données. La grammaire, la syntaxe et la sémantique sont des patterns qui se répètent, obéissent à des règles, et une architecture comme le Transformer peut les capturer via l'échelle et l'attention. Les mécanismes causaux dans les systèmes complexes ne fonctionnent pas ainsi.

La causalité est directionnelle. La pluie cause des rues mouillées, mais les rues mouillées ne causent pas la pluie. Dans un système complexe avec des milliers de variables et des interconnexions denses, identifier quelles relations sont causales, dans quelle direction elles vont, et comment elles interagissent sous intervention est un problème extraordinairement difficile. C'est le genre de problème où davantage de données n'aident pas automatiquement, car les données observationnelles seules ne peuvent pas résoudre l'ambiguïté causale.

On dispose de cadres mathématiques pour l'inférence causale, principalement le do-calculus de Judea Pearl et le cadre des résultats potentiels de Rubin. Ce sont des outils puissants, mais ils requièrent des hypothèses sur la structure du système qu'on ne peut souvent pas vérifier. Quand ces hypothèses tiennent, l'inférence causale fonctionne bien. Dans la complexité réelle des systèmes du monde réel, où les facteurs confondants sont partout et les graphes causaux sont denses, ces méthodes échouent souvent.

C'est aussi pourquoi les LLM ne peuvent pas simplement être mis à l'échelle pour devenir des raisonneurs causaux. Un LLM peut répéter le langage du raisonnement causal. Il peut écrire sur les contrefactuels et les interventions, mais il a appris ces concepts comme des patterns linguistiques, pas comme des mécanismes computationnels pour simuler ce qui se passe quand on intervient dans un système. Cet écart est architectural.

### Barrière 3 : Calcul pour modéliser des systèmes complexes

Les exigences de calcul de la modélisation des systèmes complexes sont qualitativement différentes de celles de l'entraînement des LLM. Entraîner GPT ou Claude était coûteux, mais c'était un problème d'optimisation tractable. Le calcul s'adapte avec les données et les paramètres, mais l'opération fondamentale est une multiplication matricielle bien comprise sur des clusters GPU.

Simuler un système complexe est une autre affaire. Si l'on veut modéliser un système avec n agents en interaction, l'espace d'états croît de façon combinatoire. Le nombre de patterns d'interaction possibles croît exponentiellement. Si le système est continu et stochastique, chaque simulation prospective nécessite de résoudre des équations différentielles stochastiques couplées à chaque pas de temps.

Les modèles climatiques, parmi nos meilleures simulations de systèmes complexes, consomment déjà d'énormes ressources informatiques, et fonctionnent encore à des résolutions spatiales trop grossières pour capturer de nombreux phénomènes importants.

Les modèles basés sur des agents font face au même problème sous un angle différent. Ils sont excellents pour capturer les comportements émergents issus d'interactions locales, mais leur mise à l'échelle à des tailles de population réalistes avec une complexité comportementale réaliste se heurte aux limites matérielles. Comme ces simulations sont stochastiques, de nombreuses exécutions sont nécessaires pour générer des statistiques fiables, multipliant davantage le coût de calcul.

La contrainte de calcul explique aussi pourquoi on ne peut pas passer en force la contrainte de données. En principe, on pourrait générer des données synthétiques en exécutant des simulations massives. En pratique, les simulations sont trop coûteuses à effectuer à l'échelle nécessaire, et elles ne valent que ce que valent les modèles causaux qui les sous-tendent — ce qui ramène à la contrainte deux.

### Pistes de recherche prometteuses

Rien de tout cela ne signifie que le problème est insoluble, mais la solution ne ressemblera pas à une mise à l'échelle des mêmes architectures qui ont résolu le langage. Plusieurs programmes de recherche représentent de vrais progrès vers une modélisation fiable des systèmes complexes.

**Causal AI**

La direction de recherche la plus prometteuse à court terme est l'intégration du raisonnement causal dans les architectures d'apprentissage automatique. L'objectif est de construire des modèles qui effectuent l'inférence causale comme une primitive computationnelle, plutôt que comme une découverte causale linguistique.

Le travail issu du CausalAI Laboratory d'Elias Bareinboim à Columbia est fondamental ici. Son groupe produit régulièrement des résultats sur l'identification causale à partir de données observationnelles, le renforcement robuste face aux confondants, et la transportabilité — le problème de prendre des estimations causales apprises dans un contexte et de les appliquer dans un autre. Cette dernière dimension est essentielle pour les systèmes complexes, où l'on dispose souvent de données d'un régime et a besoin de prédictions dans un régime différent.

L'écosystème Causal AI se mature rapidement. L'initiative PyWhy de Microsoft Research (plus récemment Amazon Research) construit des outils open source qui rendent la découverte causale et l'inférence accessibles au-delà des groupes de recherche spécialisés. L'adoption industrielle s'accélère également. Une intégration précoce dans la planification de la chaîne d'approvisionnement chez des entreprises comme Blue Yonder et Oracle montre les premiers signes que les modèles causaux peuvent ajuster les prévisions et prescrire des réponses aux perturbations d'une manière que les modèles purement corrélationnels ne peuvent pas.

La vraie percée viendra d'architectures hybrides qui utilisent des réseaux de neurones pour la reconnaissance de patterns et l'apprentissage de représentations, tout en imposant une structure causale via des modèles graphiques explicites ou des équations structurelles. Il s'agit de donner aux réseaux de neurones un squelette de logique causale qui contraint ce qu'ils peuvent apprendre.

**Physics-Informed Neural Networks (PINNs)**

Les PINNs représentent un angle d'attaque différent. Au lieu d'apprendre tout à partir de données, les PINNs intègrent directement les lois physiques connues dans la fonction de perte du réseau de neurones. Le réseau est pénalisé non seulement pour s'écarter des données observées, mais aussi pour violer les équations différentielles qui régissent le comportement du système.

Cette approche est puissante car elle réduit considérablement les besoins en données. Si l'on connaît la physique, on n'a pas besoin que les données enseignent la physique au modèle. Les données doivent seulement fixer les paramètres et les conditions initiales.

Les PINNs ont montré de bons résultats en dynamique des fluides, en mécanique des structures et en transfert de chaleur, et ils sont de plus en plus utilisés comme base computationnelle pour les systèmes de jumeaux numériques — des répliques virtuelles de systèmes physiques qui se mettent à jour en temps réel à mesure que de nouvelles données de capteurs arrivent.

Les limites restent significatives. Les PINNs peinent avec des systèmes hautement non linéaires. Leur dynamique d'entraînement peut être pathologique quand la perte physique et la perte de données entrent en compétition. Ils sont aussi actuellement limités aux systèmes dont on connaît les équations gouvernantes.

La trajectoire du domaine reste encourageante. Des travaux récents sur les opérateurs neuronaux étendent l'approche à des classes de problèmes plus larges. L'intégration des PINNs avec des flux de données en temps réel via des architectures de jumeaux numériques crée une boucle de rétroaction entre les systèmes physiques et leurs modèles computationnels qui gagne en précision au fil du temps.

Pour les applications d'entreprise, cela compte parce que les jumeaux numériques construits sur des architectures informées par la physique peuvent fournir la prédiction, la prescription et le diagnostic fiables que les LLM ne peuvent pas offrir. Un jumeau numérique d'une ligne de fabrication peut prédire les défaillances avant qu'elles se produisent, prescrire des calendriers de maintenance minimisant les temps d'arrêt, et diagnostiquer les causes profondes des défauts de qualité.

**Modèles multi-échelles et agents appris**

La troisième frontière concerne moins une architecture unique que la stratégie d'intégration. Les systèmes complexes opèrent simultanément à plusieurs échelles ou sous-systèmes — molécules au sein de cellules au sein d'organes au sein de populations, ou trades au sein de portefeuilles au sein de marchés au sein d'économies. Aucun modèle ou structure d'information unique ne peut représenter toutes ces échelles à la fois.

La recherche qui importera le plus est celle sur le couplage de modèles entre sous-systèmes de manière à ce que les comportements macroscopiques émergent des dynamiques microscopiques sans avoir à simuler chaque particule.

Les modèles basés sur des agents ont toujours été le cadre naturel pour les systèmes avec des agents adaptatifs, mais ils ont été contraints par le coût computationnel et la difficulté de calibration. L'approche émergente consiste à utiliser l'apprentissage automatique comme accélérateur au sein du cadre agent. On entraîne des substituts neuronaux qui approximent le comportement d'agents individuels ou de groupes d'agents, puis on exécute la simulation agent avec ces composants appris plutôt qu'avec des règles artisanales. Cela réduit considérablement le coût de calcul tout en préservant la capacité à capturer les comportements émergents.

Le paradigme Nested Learning de Google, qui traite un modèle unique comme un système de problèmes d'optimisation interconnectés opérant à différentes échelles temporelles, est un cousin conceptuel de cette approche. En isolant les modules à mise à jour rapide et lente, il aborde le problème de l'oubli catastrophique et permet un apprentissage continu d'une manière que les architectures plates ne permettent pas.

### Conclusion

Le récit IA a été dominé par le langage depuis cinq ans. Les LLM sont spectaculaires, et les applications sont réelles, mais ce récit suppose souvent que les progrès sur le langage conduiront à des progrès sur l'intelligence. Le scepticisme de Powell est justifié. Les modèles qui prédisent, prescrivent et diagnostiquent de manière fiable à l'échelle de systèmes complexes réels n'existent pas encore. Les construire nécessitera des architectures, des stratégies d'information et des paradigmes de calcul différents de ceux qui ont produit ChatGPT, Claude et Gemini.

Ce n'est pas un échec de l'IA. Il s'agit de dresser un bilan honnête de la situation et du chemin restant à parcourir pour progresser. La bonne nouvelle est que les directions de recherche sont claires, les premiers résultats sont encourageants, et le problème n'est pas un manque d'imagination. C'est un problème d'ingénierie, d'investissement et d'attention soutenue. Nous avons résolu le langage. Nous n'avons pas résolu la complexité, mais nous y travaillons.

## Pourquoi ça compte

L'aveu de Powell éclaire une limite fondamentale rarement formulée aussi clairement par l'industrie tech : les LLM ne sont pas des moteurs de compréhension des systèmes, et prétendre le contraire dans des contextes à fort enjeu (économie, santé, infrastructure) est dangereux. Pour les architectes de systèmes agentiques, c'est un rappel que les couches au-delà du LLM — inférence causale, simulation, jumeaux numériques — ne sont pas optionnelles si l'on vise une fiabilité réelle.
