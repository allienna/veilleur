---
title: "What next for the compute crunch?"
date: 2026-04-07
url: https://martinalderson.com/posts/what-next-for-the-compute-crunch/?utm_source=tldrnewsletter
authors: ["Martin Alderson"]
keywords: [compute, GPU, inference, GitHub, demand]
theme: IA
tone: opinion
used_in: ["2026-04-07"]
---

## Résumé

La crise du compute dans l'IA n'est plus une anecdote de couloir : elle s'installe comme une contrainte structurelle du secteur. Le COO de GitHub a partagé des données spectaculaires — une multiplication par 14 des commits en rythme annualisé sur les trois derniers mois, portée en grande partie par les agents de coding. OpenAI, Sora et les autres grands fournisseurs ressentent le même étranglement : la demande en inférence croît bien plus vite que les datacenters ne peuvent être construits. Le marché du compute devient une course entre des acteurs tous à court de ressources simultanément, ce qui crée des effets de débordement en cascade d'un fournisseur à l'autre.

## Points clés

- Le COO de GitHub a annoncé une augmentation annualisée d'environ 14x des commits en trois mois, attribuée majoritairement aux coding agents
- Le responsable de l'équipe Codex chez OpenAI a confirmé que la demande dépasse l'offre disponible
- Sora aurait été mis en veille pour libérer du compute au profit d'autres tâches — symptôme d'arbitrages internes sous tension
- Effet domino : quand un fournisseur resserre ses limites, ses utilisateurs se déversent chez les concurrents, aggravant leur propre saturation
- Toutes les grandes entreprises IA sont en manque de compute simultanément, sans qu'aucune ne dispose d'un avantage décisif à court terme
- La demande en inférence croît structurellement plus vite que la capacité de construction des datacenters

## Analyse approfondie

### Un chiffre qui change la perspective

Quand le COO de GitHub cite une multiplication par 14 des commits en rythme annualisé sur trois mois, le premier réflexe est de chercher une explication marketing. Mais le contexte donne du poids au chiffre : cette croissance n'est pas tirée par une augmentation du nombre de développeurs humains, elle est portée par les coding agents — des systèmes autonomes qui génèrent, testent et committent du code sans intervention humaine directe. C'est un signal fort que l'IA agentic n'est plus un concept expérimental mais une réalité opérationnelle à l'échelle de millions de repos.

Ce type de croissance, si elle se confirme, a des implications directes sur la consommation de compute : chaque agent génère des appels d'inférence en continu, bien au-delà de ce que produit un développeur humain utilisant un simple assistant de complétion.

### La demande d'inférence comme nouveau goulot

Pendant longtemps, le débat sur les ressources compute s'est concentré sur l'entraînement des modèles — les clusters GPU massifs nécessaires pour produire un GPT-4 ou un Llama. L'inférence — faire fonctionner le modèle en production — était perçue comme moins gourmande, plus maîtrisable.

Ce paradigme est en train de changer. Les agents IA modernes ne font pas un seul appel au modèle : ils enchaînent des dizaines, voire des centaines d'appels dans une même session — pour planifier, exécuter, vérifier, corriger. Multipliez cela par des millions d'utilisateurs et d'agents actifs simultanément, et la demande en inférence devient un problème de magnitude comparable à l'entraînement, mais permanent et en croissance continue.

Le responsable de l'équipe Codex chez OpenAI l'a confirmé sans ambages : la demande dépasse l'offre. Ce n'est pas une formulation prudente pour gérer les attentes — c'est une description d'une situation de pénurie réelle.

### Sora comme variable d'ajustement

La rumeur selon laquelle Sora aurait été temporairement mis de côté pour libérer du compute au profit d'autres tâches est révélatrice d'une réalité peu glamour des opérations IA à grande échelle : les ressources sont finies et les arbitrages sont brutaux.

OpenAI gère un portefeuille de produits aux profils de consommation très différents. La génération vidéo (Sora) est extraordinairement intensive en compute — chaque seconde de vidéo générée mobilise des ressources bien supérieures à un échange textuel. Face à une demande globale qui déborde les capacités, sacrifier temporairement un produit moins stratégique à court terme pour alimenter les usages core (ChatGPT, l'API, les agents) est une décision rationnelle, même si elle est douloureuse sur le plan produit.

Ce type d'arbitrage deviendra probablement plus fréquent et plus visible à mesure que la demande continue de croître.

### L'effet domino entre fournisseurs

L'un des aspects les plus intéressants de la crise actuelle est sa nature systémique. Lorsqu'un fournisseur — OpenAI, Anthropic, Google, ou un acteur plus petit — atteint ses limites de capacité et commence à rationner l'accès (throttling, listes d'attente, augmentations de prix), ses utilisateurs ne disparaissent pas. Ils se reportent sur les fournisseurs alternatifs, qui se retrouvent à leur tour saturés.

Ce phénomène crée une interdépendance inhabituelle dans un secteur pourtant très compétitif. Les acteurs sont en concurrence pour les clients, mais ils souffrent collectivement de la même contrainte. Il n'existe pas de "fuite vers la qualité" possible quand le problème est la disponibilité du compute lui-même, partagée par tous.

Pour les entreprises qui construisent des produits sur ces APIs, cette situation implique de nouveaux risques opérationnels : la dépendance à un unique fournisseur devient dangereuse non pas seulement pour des raisons de coût ou de politique tarifaire, mais pour des raisons de disponibilité brute.

### La construction de datacenters comme contrainte physique

Il y a une limite fondamentale à ce problème : construire un datacenter prend du temps — entre deux et quatre ans pour un grand site, de la planification à la mise en production. La demande en compute croît selon une courbe beaucoup plus agressive que cette capacité à construire des infrastructures physiques.

Cette asymétrie temporelle est structurelle. Même si Microsoft, Google, Amazon et les pure players IA investissent des centaines de milliards de dollars dans de nouveaux datacenters, les capacités supplémentaires arriveront dans un horizon de plusieurs années. Pendant ce temps, la demande — portée par l'adoption massive des agents IA — continue d'accélérer.

La question n'est donc pas "est-ce qu'il y aura assez de compute un jour ?" mais "comment gère-t-on le gap entre maintenant et ce jour-là ?"

### Les réponses possibles à court et moyen terme

Face à cette contrainte, plusieurs leviers sont actionnables, avec des délais et des impacts différents :

- **Optimisation des modèles** : les techniques de distillation, quantization et pruning permettent de réduire significativement le coût d'inférence sans dégradation majeure de la qualité. C'est une voie active pour tous les grands labs.
- **Spécialisation des modèles** : plutôt qu'utiliser un modèle frontier pour toutes les tâches, router vers des modèles plus petits et spécialisés pour les tâches simples. Cela réduit la consommation par requête.
- **Pricing dynamique et rationnement** : faire payer le compute à son coût réel, avec des mécanismes de priorité, pour décourager les usages non critiques et financer l'expansion de capacité.
- **Hardware alternatif** : au-delà des GPU Nvidia, des alternatives (TPU de Google, Trainium d'AWS, puces custom d'OpenAI) peuvent diversifier l'offre et réduire les goulots.
- **Efficacité des agents** : repenser les architectures agentiques pour réduire le nombre d'appels d'inférence par tâche — un défi d'engineering autant qu'un défi de recherche.

Aucune de ces réponses n'est une solution magique à court terme. La crise du compute est partie pour durer, et elle va remodeler les stratégies produit et les décisions d'architecture des équipes qui construisent sur l'IA.

## Pourquoi ça compte

La saturation simultanée du compute chez tous les grands fournisseurs IA n'est pas un problème de croissance temporaire — c'est le signal que l'adoption des agents IA dépasse déjà les capacités d'infrastructure mondiales, et que les équipes qui construisent sur ces plateformes doivent intégrer la disponibilité du compute comme un risque opérationnel à part entière dans leurs architectures et leurs feuilles de route.
