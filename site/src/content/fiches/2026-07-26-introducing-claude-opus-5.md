---
title: "Introducing Claude Opus 5"
date: 2026-07-26
url: https://www.anthropic.com/news/claude-opus-5
authors: [Anthropic]
keywords: [Claude Opus 5, effort setting, Frontier-Bench, alignement, coût par tâche]
theme: IA
tone: news
used_in: ["2026-07-26"]
---

## Résumé

Anthropic annonce Claude Opus 5, un modèle décrit comme réfléchi et proactif, proche de l'intelligence frontier de Claude Fable 5 pour la moitié du prix. Il devient state-of-the-art sur des évaluations de code et de travail intellectuel comme Frontier-Bench et GDPval-AA, tout en restant derrière Mythos 5 sur les tâches de cybersécurité. Le point saillant est le réglage d'« effort » : les performances culminent en xhigh puis redescendent en max, et de nombreux partenaires rapportent une qualité maintenue à des niveaux de raisonnement plus bas avec bien moins de tokens. Il devient le modèle par défaut sur Claude Max et le plus puissant sur Claude Pro, au prix inchangé de 5 $ / 25 $ par million de tokens.

## Points clés

- Opus 5 approche l'intelligence de Fable 5 à la moitié du prix, au même tarif qu'Opus 4.8 (5 $ en entrée, 25 $ en sortie par million de tokens).
- Sur Frontier-Bench v0.1, il double plus que la performance d'Opus 4.8 pour un coût par tâche inférieur ; sur ARC-AGI 3, son score est trois fois celui du meilleur concurrent.
- Il vérifie son propre travail : sur un bug réel d'un gestionnaire de paquets open source, il a trouvé la cause racine là où un concurrent n'a corrigé que le symptôme.
- L'audit comportemental automatisé le classe comme le modèle le plus aligné d'Anthropic à ce jour (score de 2,3 de comportement mal aligné, le plus bas de la gamme récente).
- Sur la cybersécurité, il identifie les vulnérabilités presque aussi bien que Mythos 5 mais reste très en retrait sur la génération d'exploits.
- Plusieurs partenaires soulignent la qualité maintenue à raisonnement réduit : 26 % de tokens en moins qu'Opus 4.8 à raisonnement max sur du travail juridique, un septième des tokens de raisonnement sur un benchmark de trading.

## Analyse approfondie

Claude Opus 5 est disponible dès aujourd'hui. C'est un modèle réfléchi et proactif qui s'approche de l'intelligence frontier de Claude Fable 5 pour la moitié du prix.

Sur des évaluations de code et de travail intellectuel comme Frontier-Bench et GDPval-AA, Opus 5 est le nouvel état de l'art, même s'il reste derrière Mythos 5 sur les tâches de cybersécurité.

Opus 5 est conçu pour un usage quotidien : il travaille plus efficacement que les autres modèles. C'est le nouveau modèle par défaut sur Claude Max, et le modèle le plus puissant sur Claude Pro.

### Performance et rapport coût-efficacité

Claude Opus 5 offre des performances nettement améliorées pour le même coût que son prédécesseur, Opus 4.8. Les courbes de cette section montrent comment la performance évolue selon le réglage d'effort du modèle, que les clients peuvent utiliser pour optimiser l'intelligence ou économiser des tokens en visant des résultats plus rapides et moins chers.

Opus 5 excelle sur les tâches d'ingénierie logicielle à forte valeur. Par exemple, sur **Frontier-Bench v0.1**, Opus 5 dépasse tous les autres modèles et fait plus que doubler la performance d'Opus 4.8, à un coût par tâche inférieur. Sur **CursorBench 3.2**, à effort max, le modèle se situe à moins de 0,5 % du meilleur score de Fable 5, mais à moitié prix par tâche ; il obtient aussi, à coût donné, de meilleures performances que tous les autres modèles aux niveaux d'effort high, xhigh et max.

Nous observons des résultats similaires sur les tâches de travail intellectuel et de résolution de problèmes. Par exemple :

- Sur **ARC-AGI 3**, une évaluation où le modèle doit résoudre des problèmes inédits, le score d'Opus 5 est trois fois plus élevé que celui du meilleur modèle suivant.
- Sur **Zapier AutomationBench**, qui mesure la capacité des modèles à mener des tâches métier de bout en bout, le taux de réussite d'Opus 5 est environ 1,5 fois celui du meilleur modèle suivant, à coût par tâche égal. Même à son niveau d'effort le plus bas, Opus 5 réussit plus de tâches que n'importe quel autre modèle.
- Sur **OSWorld 2.0**, un benchmark d'utilisation de l'ordinateur, Opus 5 surpasse tous les autres modèles à coût donné, dépassant le meilleur résultat de Fable 5 pour un peu plus du tiers du coût.

Opus 5 est aussi une amélioration significative par rapport à Opus 4.8 pour la recherche scientifique. Il fait mieux qu'Opus 4.8 sur chacune de nos évaluations en sciences de la vie, qui couvrent la biologie structurale, la chimie organique et la bio-informatique. Les progrès sont les plus notables sur les tâches de chimie organique, comme l'inférence de structures moléculaires à partir de données de spectroscopie (10,2 points de pourcentage de plus qu'Opus 4.8 sur notre benchmark interne), et sur les tâches liées aux protéines comme la prédiction de l'effet des variations de séquence sur la fonction (7,7 points de plus).

Enfin, Opus 5 est capable de produire des sorties visuelles nettement plus fortes.

### Travailler avec Claude Opus 5

Claude Opus 5 est bien meilleur pour vérifier son travail et itérer soigneusement jusqu'à réussir. Dans nos évaluations et lors des tests en accès anticipé, nous et nos utilisateurs avons trouvé de nombreux exemples de son agentivité et de sa rigueur :

- Sur une tâche Frontier-Bench, Opus 5 a reçu le dessin d'une pièce mécanique et devait écrire le code pour la reconstruire en modèle 3D FreeCAD. Or, dans cette tâche, le modèle n'avait volontairement aucun moyen de *voir* directement le dessin. Opus 5 a répondu en écrivant son propre pipeline de vision par ordinateur pour extraire la géométrie des pixels bruts, puis a reconstruit la pièce complète. Il y est parvenu de façon répétée ; aucun modèle concurrent placé dans le même dispositif n'a résolu la tâche en cinq tentatives.
- Face à un bug réel dans un gestionnaire de paquets open source populaire, Opus 5 a trouvé la cause racine et corrigé un cas limite que le correctif de la communauté avait manqué. Un modèle concurrent n'a corrigé que le symptôme de surface, sans la cause, puis a déclaré le bug résolu.
- Un ingénieur d'une société de trading a utilisé Opus 5 pour construire un flux de données de marché pour une nouvelle place boursière en une seule session. Les modèles précédents ne parvenaient pas du tout à réaliser cette tâche, même avec des plans détaillés fournis par l'ingénieur. Ne trouvant aucun flux en direct pour se valider, Opus 5 a même construit son propre harnais de test pour vérifier que son code parsait correctement les données de la place.

### Retours des clients en accès anticipé

> Sur FrontierCode 1.1, Claude Opus 5 approche le niveau de Fable pour la moitié du coût. Dans Devin, il montre une force particulière sur le débogage difficile et l'analyse de cause racine.

> Claude Opus 5 offre une intelligence proche de Fable 5, à la vitesse et au coût d'Opus. Sur CursorBench, il est juste en dessous de Fable 5 et présente beaucoup des mêmes comportements.

> Claude Opus 5 a pris la tête du classement AutomationBench de Zapier sans dépenser plus de tokens que les modèles Claude précédents. Il a pris un classeur brut de santé des comptes et déroulé une séquence complète de prévention du churn de bout en bout : repérage des comptes à risque, alerte du bon responsable, synthèse pour les équipes de rétention. Les modèles précédents échouaient ; Opus 5 atteint 100 %.

> Sur nos travaux d'analyse génomique, Claude Opus 5 se comporte plus comme un scientifique rigoureux que n'importe quel modèle que nous avons utilisé. Il choisit les bons tests statistiques pour écarter les facteurs de confusion, recoupe ses propres résultats par des méthodes indépendantes, et garde le cap sur de longues analyses multi-étapes.

> Claude Opus 5 devance tous les modèles de sa famille sur nos évaluations internes. Il n'est pas seulement meilleur sur nos tâches de codage agentique les plus dures, +22 % par rapport à Opus 4.7 : il est plus régulier, avec beaucoup moins de variance d'une exécution à l'autre. Pour les millions de builders sur Lovable, cette constance est l'essentiel.

> Claude Opus 5 est le plus grand bond de la famille Opus depuis la 4.5. Sur les mêmes constructions d'applications full-stack, ça se voit d'abord sur le front : les meilleures animations, jeux et travaux 3D que nous ayons vus d'un modèle Opus.

> Nous adorons Claude Opus 5. Pour le travail analytique ouvert que gère notre agent, c'est une amélioration nette par rapport à Opus 4.8, et les gains sont les plus importants là où ça compte : les tâches les plus dures et les plus floues.

> Claude Opus 5 est une amélioration frappante par rapport à Opus 4.8 pour les workflows de recherche financière que nos analystes exécutent quotidiennement. Il se distingue sur le raisonnement numérique, le travail sur tableaux, et un esprit critique plus aiguisé là où la précision compte.

> Box constate qu'Opus 5 surpasse Opus 4.8 de 8 %, avec des gains notables sur l'analyse de données (+11 %) et la due diligence (+17 %).

> C'est un saut générationnel clair par rapport à Opus 4.8. En un week-end, je lui ai confié un rôle de chief-of-staff sur mes environnements de dev : il a construit son propre outil de monitoring, piloté chaque machine, et ne m'a sollicité que pour les décisions de jugement.

> Claude Opus 5 vérifie son propre travail comme le ferait un vrai développeur front. Sur notre benchmark, il a ouvert ses pages dans un navigateur en largeur desktop et mobile, repéré un produit caché sous la ligne de flottaison mobile et un bouton de commande hors écran, et corrigé les deux avant de rendre le travail.

> Nette progression sur le travail d'agent juridique par rapport aux modèles Opus précédents, avec les plus gros gains en gouvernance d'entreprise et arbitrage. Nous avons aussi été impressionnés par sa capacité à maintenir la qualité à des niveaux de raisonnement plus bas, avec en moyenne 26 % de tokens en moins qu'Opus 4.8 à raisonnement max.

> Les plus gros gains pour nous sont sur le travail à long horizon : construire un deck complet, puis le réviser. La qualité de l'artefact décide du modèle que nous expédions, et c'est la progression la plus nette que nous ayons vue.

> Ce qui ressort chez Claude Opus 5, c'est le jugement. Lors d'une passation de PR, il ne se précipite pas pour publier : il vérifie les branches, contrôle le template, et réfléchit aux implications sur les tests pour que la passation soit propre.

> Pendant une session de ré-architecture, Claude Opus 5 a contesté un design que je proposais, et il n'a pas cédé quand j'ai insisté. Il a expliqué précisément ce qui avait de la valeur dans mon idée, resserré son objection sur une seule question de conception, et proposé un compromis qui gardait la bonne partie tout en corrigeant le défaut. C'est ce genre de jugement qui nous permet de lui faire confiance avec moins de supervision.

> Sur les premiers passages de redline, Claude Opus 5 obtient le meilleur score de tous les modèles testés, près du double d'Opus 4.8.

> Claude Opus 5 écrit des diffs propres et resserrés, sans code mort, et repère mieux les dangers subtils spécifiques à une base de code. Nous l'adoptons pour nos charges de production.

> Ce qui distingue Claude Opus 5, c'est le jugement. Il réfléchit davantage avant d'écrire la moindre ligne, attrape ses propres failles logiques pendant la planification plutôt qu'après coup, et raisonne sur *pourquoi* une réponse est juste, pas seulement sur le fait qu'elle fonctionne.

> C'est le plus fort modèle Opus que nous ayons testé sur notre benchmark de trading, et il y parvient en utilisant environ un septième des tokens de raisonnement et moins de la moitié de la latence d'Opus 4.8. De meilleures réponses pour une fraction du calcul.

> Claude Opus 5 permet à des agents de monitoring de gérer une partie de leur propre mémoire en production. L'agent traite son contexte comme un document vivant : après avoir signalé une anomalie potentielle sur un de nos services, il a re-vérifié sa propre hypothèse contre la production, constaté que le signal était bénin, écrit la correction dans sa mémoire, et retiré ses requêtes de surveillance de lui-même.

### Alignement et sûreté

**Alignement.** Lors des tests de pré-déploiement, notre audit comportemental automatisé a trouvé qu'Opus 5 était notre modèle le plus aligné à ce jour. Il respecte mieux la Constitution de Claude qu'Opus 4.8, Sonnet 5 ou Fable 5 ; il présente les taux de comportement trompeur les plus faibles ; et il est le moins susceptible d'être manipulé vers un mésusage. C'est aussi notre modèle le plus sûr en matière d'évitement d'actions imprudentes aux effets secondaires difficilement réversibles. Sur notre audit comportemental automatisé, Opus 5 obtient 2,3 sur le comportement globalement mal aligné, le score le plus bas de nos modèles récents.

**Sûreté.** Opus 5 ne fait pas progresser la frontière sur les capacités dual-use à risque. Lors d'évaluations rigoureuses menées avec des partenaires privés et gouvernementaux, il reste derrière Mythos 5 à la fois en recherche en biologie et en cybersécurité offensive.

Comme pour son prédécesseur, nous avons volontairement évité d'entraîner Opus 5 sur des tâches cyber. Le modèle s'est néanmoins nettement amélioré sur ces tâches du fait de sa montée en capacités générales, et il s'approche de Mythos 5 pour *trouver* des vulnérabilités. En revanche il reste très en retrait sur l'*exploitation* de ces vulnérabilités, c'est-à-dire leur transformation en menaces cyber concrètes. C'est illustré par ses performances sur OSS-Fuzz : Mythos 5 et Opus 5 identifient les vulnérabilités avec un succès similaire, mais le score d'Opus 5 sur le développement d'exploits est très inférieur.

### Garde-fous d'Opus 5

**Cybersécurité.** Les classifieurs cyber d'Opus 5 sont proportionnellement moins restrictifs que ceux de Fable 5. Ils lui permettent de trouver des vulnérabilités dans du code source, mais bloquent le scan de vulnérabilités « basé binaire » (une méthode plus souvent associée aux acteurs malveillants), les tests d'intrusion et la génération d'exploits. Nous estimons que les classifieurs interviendront environ 85 % moins souvent que pour Fable 5. Dans Claude.ai, Claude Code et Claude Cowork, toute requête signalée bascule par défaut sur Opus 4.8. Ce repli peut aussi être activé sur l'API. Notre Cyber Verification Program (CVP) donne aux entreprises et chercheurs déjà membres un accès immédiat à une version d'Opus 5 avec moins de restrictions.

**Biologie.** Comme Opus 5 a une panoplie de garde-fous similaire à Opus 4.8, il est désormais notre modèle le plus capable en accès général pour la recherche scientifique. Le modèle montre néanmoins d'importantes limites sur les tâches de recherche autonomes de longue durée, là où nous attendons les risques biologiques les plus substantiels. Mythos 5 reste le modèle le plus fort pour ce type de travail. Dans le cadre de ce lancement, les requêtes liées à la biologie bloquées sur Fable 5 seront désormais routées vers Opus 5 plutôt que vers Opus 4.8.

### Pour démarrer

Claude Opus 5 est disponible aujourd'hui sur toutes les plateformes, au prix de 5 $ par million de tokens en entrée et 25 $ par million en sortie (identique à Opus 4.8). Les développeurs peuvent démarrer avec `claude-opus-5` sur l'API Claude.

Il est aussi proposé en mode Fast, où il tourne environ 2,5 fois plus vite que par défaut. Comme pour Opus 4.8, le mode Fast est facturé au double du prix de base.

Deux mises à jour sortent en bêta aux côtés d'Opus 5 :

- **Changement d'outils en cours de conversation** sur la Claude Platform : les développeurs peuvent modifier les outils accessibles à Claude sans invalider le cache de prompt.
- **Replis automatiques sur l'API** : les requêtes signalées par nos classifieurs de sûreté sur Opus 5 (ou Fable 5) peuvent être routées automatiquement vers un autre modèle plutôt que bloquées.

Comme pour les modèles Opus précédents, Opus 5 n'impose pas d'exigences de rétention de données en accès général.

## Pourquoi ça compte

L'annonce officialise un déplacement du curseur : la performance ne vient plus mécaniquement de « plus de raisonnement », et le vrai indicateur devient le coût par tâche terminée, pas le prix au token. Les retours partenaires sur le jugement et l'auto-vérification préfigurent des agents qu'on supervise moins et qu'on encadre autrement.
