---
title: "From Zero Trust to Agent Trust"
date: 2026-07-16
url: https://fandf.co/4aunxmT?utm_source=tldrai
authors: [fandf.co]
keywords: [zero trust, agent trust, sécurité, essaims d'agents, comportement émergent]
theme: IA
tone: opinion
used_in: ["2026-07-16"]
---

## Résumé

Le zero trust, socle de la cybersécurité construit sur deux décennies (Kindervag 2010, BeyondCorp de Google 2014, NIST 2020), a prouvé sa durabilité comme posture défensive et comme catalyseur de modèles économiques. Mais les charges de travail agentiques imposent de redéfinir ses principes fondamentaux : des agents opérant à l'échelle ont des caractéristiques sans équivalent humain ou logiciel. Le zero trust reste nécessaire, mais devient insuffisant pour contrôler ou contenir des essaims d'agents autonomes.

## Points clés

- Le zero trust s'est imposé en vingt ans comme posture défensive et comme enabler de produits numériques scalables et indépendants de la localisation.
- Les charges de travail agentiques exigent de redéfinir les principes sous-jacents : elles n'ont pas d'équivalent dans des environnements purement humains ou logiciels.
- Risque d'essaim : des milliers d'agents prenant chacun une décision localement rationnelle, dans leur périmètre de permissions, peuvent produire un résultat globalement destructeur.
- Aucun log d'audit isolé ne signalerait cette dégradation, car aucun agent n'a dépassé ses permissions.
- Nouvelle menace : les attaques accélérées par l'IA, où des agents autonomes opérant en continu et à grande vitesse éliminent la friction qui limitait la découverte et l'exploitation des vulnérabilités.

## Analyse approfondie

### Introduction

Le parcours du zero trust dans le champ de la cybersécurité comporte quelques moments-clés fréquemment cités : l'article de Kindervag « No More Chewy Centers… » en 2010, qui observait qu'il est impossible de différencier interfaces de confiance et interfaces non fiables (le périmètre réseau) ; BeyondCorp de Google en 2014, construit en réponse aux cyberattaques « Operation Aurora » visant les hyperscalers, l'une des premières implémentations pratiques du zero trust ; et l'article Zero Trust du NIST en 2020, soulignant l'urgence pressante d'implémenter le zero trust à grande échelle pendant le COVID.

Au fil de ces deux décennies, le zero trust a prouvé sa durabilité, non seulement comme posture défensive mais comme catalyseur de modèle économique : l'architecture qui rend possibles des produits et services numériques scalables et indépendants de la localisation. Les entreprises qui ont investi en profondeur dans cette approche, que ce soit en réaction à une brèche ou en quête d'opportunité, comptent parmi les plus résilientes aujourd'hui.

Cependant, les charges de travail agentiques d'aujourd'hui nous obligent à redéfinir les principes fondamentaux sous-jacents. Les agents IA opérant à l'échelle ont des caractéristiques sans équivalent dans des environnements purement humains ou logiciels, et le zero trust, tel qu'il est conçu aujourd'hui, est nécessaire mais insuffisant pour les contrôler ou les contenir. Cet article explore ce qui doit changer pour préserver la confiance à mesure que les agents sont déployés dans l'infrastructure d'entreprise.

### Le futur agentique

Considérons un futur où des essaims d'agents, se comptant par milliers ou dizaines de milliers, effectuent un travail de façon autonome. Comment savoir qu'ils convergent vers une solution ou un résultat optimal sans enfreindre les règles de l'exploitation souhaitée ou nécessaire ? Par exemple, un agent peut prendre une décision localement rationnelle dans le périmètre de ses permissions, mais multipliée par dix mille agents travaillant en parallèle, la posture de sécurité d'un système de production peut finir dégradée par une cascade d'actions individuellement autorisées qu'aucun log d'audit isolé ne signalerait comme suspecte. Ainsi, un essaim optimisant des objectifs localement rationnels peut produire des résultats globalement destructeurs. Non pas parce qu'un agent isolé a dépassé ses permissions, mais parce qu'aucun framework ne gouverne le comportement émergent de milliers d'actions autorisées convergeant en même temps.

De plus, avec l'arrivée de modèles frontière sophistiqués, les entreprises doivent désormais réfléchir à la façon de se défendre contre les attaques accélérées par l'IA, où des agents autonomes, opérant en continu et à grande vitesse, éliminent la friction qui limitait naturellement autrefois la rapidité de découverte et d'exploitation des vulnérabilités. Les entreprises doivent aussi se prémunir contre la « lethal trifecta » décrite par Simon Willison — la combinaison, dans un même agent, d'un accès à des données privées, d'une exposition à du contenu non fiable et d'une capacité à communiquer vers l'extérieur, qui ouvre la voie à l'exfiltration de données.

Il faut donc passer d'un modèle de zero trust centré sur l'accès à un modèle d'« agent trust » qui gouverne le comportement émergent, à l'échelle de l'essaim, tout au long du cycle de vie des agents déployés dans l'infrastructure d'entreprise.

## Pourquoi ça compte

Le texte pose le cadre conceptuel du prochain chantier de sécurité : gouverner non plus l'accès individuel mais le comportement collectif d'essaims d'agents. Un angle indispensable pour tout leader qui déploie des systèmes agentiques en production.
