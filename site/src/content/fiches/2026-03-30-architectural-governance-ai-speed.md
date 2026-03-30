---
title: "Architectural Governance at AI Speed"
date: 2026-03-30
url: https://www.infoq.com/articles/architectural-governance-ai-speed/
authors: [InfoQ Certified Architect Program]
keywords: [architecture, governance, AI, ADR, Event Modeling, spec-driven development]
theme: IA
tone: opinion
used_in: ["2026-03-30"]
---

## Résumé

L'avènement de la GenAI a considérablement accéléré la production de code, rendant les processus de gouvernance architecturale traditionnels obsolètes. L'article, rédigé par des participants au programme InfoQ Certified Architect, propose un nouveau modèle fondé sur l'**architecture déclarative** : distiller les décisions et contraintes architecturales en déclarations lisibles par les machines, automatiquement appliquées sans dépendance à une autorité centrale. Trois leviers concrets sont explorés : l'Event Modeling, les validateurs OpenAPI et les Architectural Decision Records enrichis d'un fichier `architecture.md` exploitable par des agents. La conclusion est sans ambiguïté — l'avenir de la gouvernance n'est pas dans davantage de comités de révision, mais dans une intention déclarée, continuellement appliquée à la vitesse des systèmes qu'elle gouverne.

## Points clés

- La GenAI exacerbe le problème d'alignement : cadres et product managers peuvent désormais prototyper des systèmes fonctionnels en quelques minutes, court-circuitant les processus de revue classiques
- L'architecture déclarative rend la voie conforme la voie de moindre résistance — la conformité s'encode dans les outils, pas dans les processus
- Un Event Model (`eventmodel.json`) sert de carte machine-readable de l'intention architecturale, à partir de laquelle du code peut être généré et évalué automatiquement
- Les validateurs OpenAPI permettent à une équipe plateforme centralisée d'appliquer des standards transversaux (versioning, pagination, structure d'erreur) sans coordination équipe par équipe
- Le fichier `architecture.md` distille chaque ADR en directives atomiques compréhensibles par les agents — `[Warn]` ou `[Block]` — appliquées en temps réel dans l'IDE ou le pipeline CI/CD
- Les boucles de feedback (métriques de violation, lead time) permettent à l'architecture de s'adapter en continu avec le métier, sans révisions périodiques ad hoc

## Analyse approfondie

### Le code est désormais une commodité, l'alignement non

La GenAI a drastiquement réduit l'effort requis pour produire du code, et le prototypage rapide est de plus en plus courant. En conséquence, le cycle de développement logiciel est désormais contraint par la capacité d'une organisation à mettre les idées en cohérence et à maintenir la cohésion du système.

Historiquement, les organisations s'appuyaient sur des processus manuels et une supervision humaine pour atteindre la cohérence architecturale. Les startups dépendaient de personnes clés pour détecter les désalignements entre intention architecturale et implémentation. Les organisations d'envergure tentaient de maintenir la cohérence via des change boards et une prolifération d'ADR et de documentation. Dans les deux cas, identifier les désalignements était lent car cela nécessitait une dépendance synchrone à une autorité centrale.

La GenAI aggrave ce problème en accélérant le travail soumis à révision. Là où auparavant seuls les développeurs produisaient du code sur plusieurs jours ou semaines, cadres et product managers peuvent désormais prototyper des systèmes fonctionnels en quelques minutes ou heures. Les équipes de développement font face à un choix impossible : se laisser contraindre par le rythme de la supervision manuelle, ou avancer sans savoir si elles sont alignées.

Ces poussées incrémentales s'accumulent en fragmentation architecturale, déclenchant des réponses organisationnelles consistant en davantage de processus et de directives plus strictes. Ce cercle vicieux ralentit la livraison et émousse l'innovation.

### Architecture déclarative, alignement décentralisé

Scaler l'alignement à l'ère de la GenAI exige de dépasser la supervision manuelle pour aller vers des garde-fous automatisés permettant aux équipes de prendre des décisions sûres de manière autonome. La solution est l'**architecture déclarative** : distiller les décisions et contraintes architecturales en déclarations machine-enforceables d'intention, permettant une action autonome sûre.

Chaque déclaration gouverne un périmètre délimité — un contexte clairement défini au sein duquel elle a autorité. Sans cette frontière, les déclarations deviennent le type de guidance tentaculaire qu'elles étaient censées remplacer.

L'architecture déclarative se concentre sur le fait de rendre les décisions impossibles à ignorer. Au lieu de traquer des documents d'architecture ou d'attendre des experts et des review boards, l'intention lisible par machine fait de la voie conforme la voie de moindre résistance. La validation de conformité s'encode dans les outils là où les développeurs se trouvent déjà : éditeurs, pipelines, outils de code review.

La lisibilité par machine est essentielle — pas un détail technique. Une déclaration que seuls des humains peuvent comprendre dépend toujours de l'implication humaine. Seules les déclarations raisonnées par machine font passer la gouvernance au-delà de la bande passante de n'importe quel individu ou review board.

### Les Event Models comme architecture déclarative

Un Event Model décrit comment l'information circule à travers un système, typiquement produit lors d'exercices de modélisation collaborative. Les post-its visuels sont transcrits un à un dans un fichier `eventmodel.json` appuyé par un schéma formel. Ce fichier constitue l'architecture déclarée : une carte machine-readable de l'intention architecturale à partir de laquelle des implémentations alignées peuvent être générées, et contre laquelle des agents peuvent évaluer l'implémentation.

**1. Alimenter l'automatisation**

Les vertical slices sont délimitées en périmètre et contiennent des déclarations décrivant une unité de comportement unique. Ce périmètre minimal déverrouille l'automatisation à tous les niveaux. Les artefacts de code peuvent être générés de manière déterministe à partir de l'Event Model en utilisant des templates. Comme chaque slice est autonome, si quelque chose ne va pas, on remplace une slice plutôt que de démêler des dépendances.

Pour ce que les templates ne peuvent pas couvrir, le schéma formel permet à l'IA d'aller plus loin. Les experts du domaine peuvent réviser et affiner les modèles via des agents IA, permettant une programmation conversationnelle à des niveaux d'abstraction plus élevés que le code. Comme le périmètre est minimal, humains et IA peuvent se concentrer sur une slice en isolation, réduisant drastiquement la charge cognitive.

**2. Décentraliser l'alignement architectural à l'échelle**

Les Event Models ne permettent la décentralisation que si la modélisation est collaborative au-delà des frontières d'équipes. Si les équipes modélisent indépendamment en silos, chaque modèle peut être cohérent en interne tandis que le produit se fragmente. Des organisations comme Adaptech Group et Nebulit ont pratiqué la modélisation collaborative multi-domaine à travers de nombreuses équipes, démontrant que cela passe à l'échelle au-delà des frontières d'une seule équipe.

Les mécanismes d'alignement technique comme `architecture.md` et les validateurs OpenAPI imposent la façon dont les choses sont construites, mais ne peuvent pas garantir que les équipes construisent ensemble la bonne chose. Cela requiert une modélisation partagée sur un périmètre plus large via l'Event Modeling ou d'autres techniques de Collaborative Design. La bonne nouvelle : la gouvernance technique libère l'attention humaine du contrôle des détails d'implémentation, créant de l'espace pour l'alignement au niveau produit.

**3. Le Ralph Loop : des slices au shipping**

Le Ralph Wiggum Loop est une technique d'IA en boucle où un agent tente répétitivement une tâche jusqu'à ce que les critères d'achèvement soient remplis, redémarrant avec un contexte frais à chaque itération pour éviter la dégradation du raisonnement. Les premières itérations impliquent couramment un architecte dans la boucle pour le réglage et la validation.

Chaque vertical slice de l'Event Model correspond à une cible d'itération : l'agent lit la spécification de la slice, implémente, valide contre des spécifications Given-When-Then, et boucle jusqu'à ce qu'elles passent. Comme chaque slice a un périmètre minimal, elle tient dans une seule fenêtre de contexte. Même des modèles peu coûteux produisent des résultats fiables dans ces conditions.

La structure est éloquente : les dossiers de plan sont indépendants et parallélisables. Chacun dispose de son propre marqueur de progression, ses checkboxes d'implémentation et ses logs. Les boucles de feedback produisent des décisions et des apprentissages, qui s'accumulent à travers les plans. Quand ils sont significatifs, un développeur humain les révise et met à jour `AGENTS.md`. Le comportement de l'agent évolue sur la base d'une expérience organisée, pas d'une auto-modification automatisée. Chaque itération génère de la connaissance organisationnelle comme sous-produit.

**4. La perspective de l'Event Modeling**

Une Wardley Map illustre l'industrialisation de l'IA combinée à la maturation des outils d'Event Model et aux standards de schémas émergents, aboutissant à quelque chose de nouveau : le Conversational AI Event Modeling. Ce processus réunit experts du domaine humains et GenAI pour modéliser des systèmes par la conversation plutôt que par le code.

Dans le workflow Event Modeling, le code devient jetable. Les slices ont un périmètre minimal, sont totalement spécifiées, gouvernées par des templates et des contraintes architecturales. On ne maintient pas les slices — on les régénère à partir des spécifications. Cela recadre la modernisation legacy : au lieu de réécrire des millions de lignes, on modélise le domaine et on génère du code frais à partir de celui-ci, assurant un alignement continu.

### Les validateurs OpenAPI comme architecture déclarative

Considérons une entreprise de taille moyenne qui exploite une plateforme SaaS hautement distribuée composée de centaines de composants appartenant à des dizaines d'équipes autonomes, connectés principalement via des APIs HTTP. Historiquement, cette organisation s'appuyait fortement sur la propriété architecturale implicite par une seule personne et sur une documentation "standards and practices".

L'organisation a lancé une surface d'API orientée client en priorisant la compatibilité et la facilité d'utilisation pour une adoption maximale. Elle souhaitait maintenir les bénéfices de vélocité des équipes hautement autonomes tout en reconnaissant les goulots d'étranglement dans son approche de gouvernance architecturale ad hoc. Elle voulait une architecture qui suive le rythme des exigences métier changeantes.

Pour réconcilier ces tensions, l'organisation a appliqué une approche déclarative orientée autour des spécifications OpenAPI, avec des standards et des outils de validation définis par une équipe plateforme centralisée. Ces outils de validation encodent l'intention architecturale de l'équipe plateforme et fournissent un retour automatisé sur la conformité, intégré dans le CI/CD protégeant la production contre les désalignements. Les outils sont également intégrés dans les workflows des développeurs pour un retour rapide et une détection des désalignements en shift-left.

Ce modèle combine décision centralisée et application décentralisée, assurant la cohérence pour les préoccupations d'API transversales (conventions de nommage des paths, versioning, compatibilité descendante, pagination, structure d'erreur), résultant en une expérience développeur sans friction pour les équipes produit et les consommateurs d'API externes.

La spécification OpenAPI de chaque équipe sert de configuration de déploiement. La plateforme traduit les documents OpenAPI en configuration API Gateway, politique d'autorisation et documentation orientée utilisateur. Parce que les équipes de développement partagent un pipeline de build-test-deploy standard, l'équipe plateforme dispose d'un seul point prévisible pour appliquer l'intention architecturale — sans coordination par équipe. Les équipes poursuivent leurs processus existants ; la validation au moment du déploiement exclut toute possibilité de désalignement. Le déploiement ne peut pas réussir à moins que la validation ne passe, donc les travaux mal alignés n'atteignent jamais la production.

Cette conception produit une faible charge cognitive et une haute autonomie pour les équipes de développement, une forte cohérence architecturale en production, et in fine une expérience API cohérente et intuitive pour les clients. Les premiers signaux suggèrent que cela fonctionne comme prévu : les premières équipes API ont utilisé les résultats de validation passants comme preuve objective satisfaisant des exigences de gouvernance qui nécessitaient auparavant des jours ou des semaines de revue manuelle.

Parce que l'intention architecturale est vérifiable par machine, l'alignement devient observable. L'équipe plateforme collecte de la télémétrie depuis les validateurs — taux d'erreurs de validation, lead time to change, et retours des équipes produit — identifiant les frictions systémiques. Les violations répétées indiquent souvent des standards peu clairs ou impraticables. Les lead times élevés peuvent signaler des contraintes excessives. Des taux de violation durablement bas confirment des conventions stables.

L'architecture s'adapte avec le métier ; les équipes s'adaptent avec elle.

Les validateurs déterministes protègent les bords du système, mais l'architecture est bien plus que syntaxe et structure. C'est un jugement accumulé — et le jugement ne rentre pas proprement dans une règle de linter.

### Sur les Architectural Decision Records

"L'une des choses les plus difficiles à suivre pendant la vie d'un projet est la motivation derrière certaines décisions", écrivait Michael Nygard en 2011. Les Architectural Decision Records servent de mémoire des motivations derrière les changements significatifs au sein des projets logiciels. Ils permettent le transfert de contexte, souvent perdu en raison du caractère changeant du développement agile, du décideur vers les mainteneurs successifs.

Les ADR fournissent un cadre de décision identifiant les compromis et les alternatives tout en ajoutant des informations contextuelles qui affectent souvent les décisions plus que le choix de meilleures solutions. Les ADR servent d'histoire des forces collectives qui conduisent l'évolution d'un système logiciel.

Avec l'avènement de la GenAI, cependant, le temps de recherche est considérablement réduit et les attentes de productivité ont augmenté. Les ADR pourraient ne plus remplir efficacement leur rôle. Les humains deviennent inévitablement des goulots d'étranglement, surtout dans les organisations nécessitant une approbation avant implémentation. Nygard déclarait aussi : "Personne ne lit jamais de grands documents" lors du développement des ADR. Que se passe-t-il lorsque, parce que les documents peuvent être facilement générés en masse, personne ne lit non plus les petits documents ? Les agents pourraient-ils être la solution ?

### `architecture.md` comme architecture déclarative

C'est une chose d'analyser statiquement des specs OpenAPI avec des fitness functions architecturales, mais à l'ère du Spec Driven Development, on doit aller plus loin. Un validateur déterministe peut valider la syntaxe, le style et la structure — mais qu'en est-il de l'*intention* applicative ?

Les outils déterministes ne connaissent que ce qu'on leur dit. Ils ne peuvent pas signaler que des endpoints REST parfaitement valides violent des décisions architecturales fondamentales exigeant des événements asynchrones pour la communication interne, sans s'appuyer sur des whitelists et des exceptions fragiles. Historiquement, résoudre ce problème signifiait pointer les développeurs vers d'immenses wikis d'Architectural Decision Records. Mais cela noyait les équipes sous une charge cognitive ; au lieu de shifter left, les organisations dumped left, garantissant une dérive architecturale à l'échelle.

On a besoin de mécanismes comprenant à la fois l'*esprit* et la *lettre* de l'architecture. On a besoin d'une architecture distillée en format exécutable que les modèles agentiques peuvent appliquer, guidant les développeurs en temps réel plutôt que de simplement filtrer le code.

**Le fichier `architecture.md`**

Ce fichier est une réduction rigoureuse des directives architecturales en directive agent-friendly, appliquée librement et systématiquement à chaque exécution. Donner aux agents un immense cimetière d'articles wiki ne mène qu'à la confusion et aux hallucinations. Au lieu de cela, chaque ADR se distille en directive concise qu'humain et agent peuvent internaliser et appliquer :

- Nous faisons X plutôt que Y
- Nous préférons A à B quand C est vrai

Chaque ADR et exigence technique reçoit son espace et son traitement, encapsulé en unités d'intention atomiques.

**Exemple de `architecture.md` :**

```
# architecture.md
# Executable Architectural Manifest

## Service Communication
* [ADR-088] [Warn] Require asynchronous Kafka events for inter-service communication. Reject synchronous REST calls unless communicating with external 3rd party vendors.
* [ADR-012] [Block] All public-facing APIs must be defined in OpenAPI 3.1 format before implementation code is written.

## Data & Persistence
* [ADR-004] [Block] Services must own their data. Direct database connections to another service's schema are strictly forbidden.
* [ADR-055] [Warn] Prefer DynamoDB for high-throughput, simple-access patterns. Use Postgres only when complex relational joins are required by the domain.

## Infrastructure & Scaling
* [System-Intent] [Block] All microservices must be designed as stateless execution units to support spot instance interruption. Session state must be externalized to Redis.
* [InfoSec] [Block] All authentication must utilize the corporate IdP endpoints. Application specific user tables are forbidden.

## Observability
* [ADR-067] [Warn] Log messages must use structured JSON and include the correlation_id from the request context.
* [ADR-073] [Warn] Do not log request bodies containing PII. Use the Redact() helper on the payload before logging.
```

**Fermer la boucle : gouvernance automatisée**

Un fichier statique est inutile s'il est laissé à pourrir. Pour empêcher `architecture.md` de devenir une autre page wiki obsolète, il faut le traiter comme du code. Un agent de gouvernance peut s'exécuter chaque nuit, comparant le manifeste du repository contre le corpus central d'ADR. S'il détecte des décisions nouvelles ou supplantées, il ouvre des pull requests mettant à jour les spécifications, garantissant que les repositories ne dérivent jamais de la baseline enterprise.

À mesure que l'implémentation mûrit, on peut rencontrer un `architecture.md` surchargé — ce qui se résout facilement via une structure de répertoires similaire aux propositions d'`agents.md`, gardant les sections délimitées dans des fichiers séparés.

Une fois le manifeste vérifié en place, l'application à l'exécution devient simple. Que l'agent tourne comme GitHub Action ou comme Copilot IDE local, il récupère les clauses pertinentes (chargeant uniquement les règles Data quand des fichiers de schéma sont touchés), évalue l'intention sémantique du code et fournit une remédiation in situ.

Si l'architecture est un manifeste exécutable, les outils cessent d'être des critiques et commencent à être des collaborateurs. Le même fichier guidant la revue de code agentique peut générer des fitness functions et valider l'identité d'infrastructure. On ne shifte pas simplement à gauche ; on donne enfin à ce "gauche" une carte.

### Conclusion

À l'ère de la GenAI, où rédiger du code et de la documentation est une commodité, assurer la cohérence et les standards à travers les organisations est de plus en plus critique. Via l'architecture déclarative et les boucles de feedback, les organisations font évoluer et automatisent en continu l'application de l'intention architecturale. En appliquant des techniques standard comme l'Event Modeling, l'inspection OpenAPI et les Architectural Decision Records, et en distillant les résultats en déclarations machine-enforceables, les organisations permettent aux équipes d'avancer rapidement avec un alignement de haute confiance. Ce pattern s'étend aux flux agentiques couvrant une intention que seuls des humains pouvaient auparavant valider.

Pour éliminer les goulots d'étranglement de la gouvernance centralisée, les décisions architecturales doivent être encodées directement dans les outils générant et validant l'implémentation. La voie conforme doit être la voie la plus facile. Les générateurs appartiennent à l'inception du projet et dans les workflows des développeurs. Les validateurs appartiennent à l'IDE, aux pull requests et au déploiement. La gouvernance vivant en dehors du pipeline de livraison est contournée ; la gouvernance incorporée en son sein devient invisible et automatique. Ces mécanismes se couplent à des boucles de feedback faisant évoluer continuellement l'architecture déclarée.

Le code est désormais abondant. L'alignement, non. L'avenir de la gouvernance architecturale n'est pas dans davantage de review boards ou de meilleure documentation. C'est dans une intention déclarée, continuellement appliquée et continuellement affinée, opérant à la même vitesse que les systèmes qu'elle gouverne.

## Pourquoi ça compte

Cet article offre un cadre opérationnel concret pour les équipes d'architecture confrontées à l'accélération de la GenAI : plutôt que de subir la pression en multipliant les processus, il propose de rendre la gouvernance invisible en l'encodant directement dans les outils — une réponse directe aux tensions que vivent aujourd'hui les Engineering Directors et Architects soumis à des attentes de vélocité croissantes.
