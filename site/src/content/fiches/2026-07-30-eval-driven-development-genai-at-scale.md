---
title: "Eval-driven development: Lessons from evaluating GenAI at scale"
date: 2026-07-30
url: https://links.tldrnewsletter.com/MZa68k
authors: [Rohit Girme, Dan Miller, Mia Zhao, Lifan Yang, Clint Kelly, Airbnb]
keywords: [eval-driven development, LLM-as-judge, calibration, agentic evaluation, golden dataset]
theme: IA
tone: research
used_in: ["2026-07-30"]
---

## Résumé

Les équipes d'Airbnb partagent leurs pratiques d'évaluation des produits GenAI, construites autour de l'*eval-driven development* (EDD) — l'équivalent GenAI du TDD. La thèse : l'évaluation doit être traitée comme une discipline d'ingénierie de premier plan, pas comme une arrière-pensée, parce que les sorties de LLM sont non déterministes et que « correct » est subjectif. L'article détaille les trois méthodes d'évaluation (checks programmatiques, LLM-as-judge, évaluation humaine), la calibration indispensable des juges virtuels, et les spécificités des systèmes agentiques où il faut évaluer le step, la trajectoire et la session.

## Points clés

- La règle numéro un : quand vous doutez, regardez vos données. Sortez 100 exemples de votre prototype et lisez chaque sortie.
- Trois échecs classiques sans stratégie d'évaluation : fausse confiance, régressions non détectées, effort gaspillé sur des métriques non corrélées aux résultats.
- 3 à 5 juges LLM bien calibrés valent mieux que 20 à 30 juges bruyants ; un juge par dimension de correction.
- Un juge virtuel non calibré est pire que pas de juge : il donne une fausse confiance. Objectif d'accord avec l'humain : haut 80 % à 90 %.
- Si vos experts métier ne s'accordent pas sur un label, arrêtez tout : résolvez le désaccord humain avant d'automatiser.
- Pour les systèmes agentiques, évaluer la seule sortie finale est insuffisant : une bonne réponse peut masquer un raisonnement cassé ou une trajectoire inefficace.

## Analyse approfondie

*Comment les équipes d'Airbnb construisent des produits d'IA générative dignes de confiance en traitant l'évaluation comme une discipline d'ingénierie de premier plan — et non comme une arrière-pensée.*

### Introduction

L'IA générative casse beaucoup d'hypothèses qui tenaient jusqu'ici pour le test logiciel. Contrairement au logiciel traditionnel, les sorties de LLM sont non déterministes, et « *correct* » est subjectif. Parce que tant de jugement est en jeu, il faut souvent une IA pour évaluer une IA, ce qui introduit ses propres modes de défaillance. Pour compliquer les choses, une seule interaction avec un LLM peut chaîner de la récupération, du raisonnement, des appels d'outils et de la génération, chacun pouvant échouer indépendamment.

Chez Airbnb, nous construisons des fonctionnalités propulsées par des LLM à travers tout le produit, avec des lancements récents comme les points forts des avis, le support client IA, des fonctionnalités de communication intelligentes pour les voyageurs et les hôtes. En coulisses, nous utilisons aussi l'IA pour repérer des tendances et comprendre ce qui fonctionne, ce qui guide nos prochaines améliorations.

Chaque équipe produit peut avoir ses propres critères d'évaluation, processus, workflows. Mais tous s'appuient sur des fondations et principes communs. Une équipe infrastructure fournit l'outillage et les bonnes pratiques, en intégrant les apprentissages de tous les domaines. Les recommandations ci-dessous ne se veulent pas prescriptives : il n'existe pas d'approche universelle en matière d'évals.

### 1. Fondations

Évaluer des systèmes basés sur des LLM est un travail difficile, et cela doit être planifié dès le départ. Sans stratégie délibérée, trois choses tendent à arriver :

- **Fausse confiance** : une métrique générique de « serviabilité » score bien, vous livrez, mais elle ne capturait pas le mode de défaillance que les gens rencontrent réellement.
- **Régressions non détectées** : un changement de prompt dégrade subtilement une dimension que vous ne mesuriez pas.
- **Effort gaspillé** : vous construisez un pipeline d'évals à l'échelle pour des métriques qui ne corrèlent pas avec les résultats.

Attendez-vous à consacrer une part significative de l'effort total du projet à l'évaluation. Ce n'est pas du surcoût inutile : c'est ainsi qu'on construit des produits qui fonctionnent réellement.

#### 1.1 La règle unique

**Quand vous doutez, regardez vos données.** Passer manuellement ses données en revue et se construire une intuition de ce qui compte comme succès est toujours le point de départ que nous recommandons. Construisez votre prototype, faites-le tourner sur 100 exemples (synthétiques, c'est très bien). Puis *lisez les sorties*. Lisez les traces et trouvez les erreurs du modèle. Catégorisez-les et construisez une éval.

Cette seule habitude fera plus pour la qualité de votre produit que n'importe quel framework, outil ou méthodologie de ce document.

#### 1.2 L'eval-driven development

Formalisée, cette habitude devient l'**eval-driven development (EDD)**, l'analogue GenAI du test-driven development. Plutôt que de prédire chaque défaillance en amont, l'EDD construit l'infrastructure et les habitudes pour **découvrir, encoder et tester en continu** les modes de défaillance à mesure qu'ils apparaissent. Cela force aussi les parties prenantes à externaliser ce que « bien » signifie, ce qui façonne la roadmap produit.

Cinq principes ancrent l'EDD :

1. **Définir les objectifs et les gates en amont.** Qu'optimisez-vous ? Que doit-il être vrai avant de livrer ? Ces réponses peuvent ne pas être claires immédiatement ; vous les découvrirez peut-être en explorant vos données.
2. **Laisser les erreurs réelles guider vos métriques.** Co-développez-les avec vos partenaires cross-fonctionnels à partir des défaillances observées. Ne les inventez pas dans le vide.
3. **Garder un ensemble d'évaluateurs petit et affûté.** 3 à 5 juges LLM bien calibrés battent 20 à 30 juges bruyants. Chacun doit cibler une dimension de correction spécifique.
4. **Désigner un décideur.** Ce qui constitue la correction doit être discuté en équipe, mais les gens seront parfois en désaccord. Incluez un décideur final (humain) qui tranche sur ce qui constitue un bon ou un mauvais comportement du système.
5. **Collaborer en continu.** Faites régulièrement répondre à votre partenaire produit : « X est-il meilleur ou pire que Y ? » et « Qu'est-ce qui ne va pas dans cette sortie ? »

### 2. Les trois méthodes d'évaluation

Chaque évaluation utilisera l'une de ces trois méthodes, ou une combinaison :

- Couche 1 : checks programmatiques (rapides, peu de ressources — attrapent les défaillances évidentes)
- Couche 2 : LLM-as-a-Judge (nuancé — attrape les problèmes de qualité)
- Couche 3 : évaluation humaine (coûteuse — valide les cas limites, calibre la pile)

#### 2.1 Métriques programmatiques et heuristiques

Des vérifications déterministes, écrites en code, sans appel LLM, doivent être votre premier filtre : elles attrapent les défaillances évidentes avant d'envoyer quoi que ce soit à un juge ou un annotateur humain.

Les types de checks couvrent la validité de format (JSON/schéma — à utiliser toujours), la longueur et la présence (vide ou longueurs suspectes — toujours), les mots-clés et regex (mots interdits — sécurité/conformité), les métriques ML classiques (précision/rappel/F1 — classification) et la similarité sémantique (cosinus — quand on a des références gold-standard).

✅ **À faire** : utiliser des sorties structurées (schémas JSON) pour garantir un typage strict.
❌ **À ne pas faire** : se reposer sur les seules instructions du prompt pour formater les données. Cela casse les pipelines de données en aval.

#### 2.2 LLM-as-judge (juges virtuels)

Utilisez un LLM plus puissant pour évaluer la sortie d'un autre LLM contre une grille soigneusement conçue. C'est ainsi qu'on évalue des qualités nuancées — ton, cohérence, fidélité, pertinence — pour une fraction des ressources nécessaires à l'évaluation humaine.

Cinq règles pour construire des évaluateurs LLM : un évaluateur par dimension, un juge différent du générateur, des exemples few-shot, un schéma de sortie explicite, et un barème clair.

**La conception de la grille compte.** L'ambiguïté est l'ennemi. Une formulation comme « L'explication fournie est-elle lisible et conforme à nos standards ? » n'a que peu de chances d'être efficace : si un humain ne peut pas appliquer la grille de manière cohérente, un LLM ne le pourra certainement pas.

Exemple simplifié de grille d'un juge virtuel :

```
Note la lisibilité des explications d'annonces. Une bonne explication sonne
comme un agent de voyage sympathique : chaleureux mais professionnel,
simple, naturel, grammaticalement complet.
Note 1 si ça se lit proprement.
Note 0 si l'un de ces problèmes est présent :
- Ton : trop formel/jargonneux, trop familier ("awesome vibes"),
  trop commercial ("amazing!"), ou robotique.
- Termes internes : ne jamais utiliser de terminologie interne.
- Formatage : pas de guillemets, pas de puces, pas de fragments.
  Terminer chaque explication par un point — jamais "!" ou "?".
- Grammaire : utiliser articles/déterminants/prépositions pour un flux naturel.
  Dans une énumération, l'article une seule fois puis on l'omet.
- Complexité : des mots simples plutôt que du jargon ("pool" et non
  "aquatic recreation area" ; "near" et non "proximate").

Exemples :
- "Host mentions a pool and hot tub available near downtown." → 1
- "The listing mentions a pool!" → 0 (terme interne "listing" ; finit par "!")
- "This domicile encompasses aquatic amenities." → 0 (mots complexes ; jargon)

Retourne UNIQUEMENT :
{ "reason": "<liste de tuples [type_erreur, explication], ou []>",
  "score": <1 ou 0> }
```

##### 2.2.1 Calibration : rendre votre juge virtuel digne de confiance

**Un juge virtuel non calibré est pire que pas de juge du tout, parce qu'il vous donne une fausse confiance.** Les étapes de calibration recommandées :

1. Créer un dataset doré de 50 à 100 exemples. Il DOIT inclure des mauvais exemples, pas seulement des bons.
2. Faire tourner le juge virtuel sur le golden set.
3. Mesurer l'accord. Viser des pourcentages dans le haut des 80 % à 90 %. On peut mesurer le désaccord avec le kappa de Cohen ou l'alpha de Krippendorff. (L'accord parfait n'est pas atteignable — même les humains divergent.)
4. Analyser les désaccords. Affiner le prompt et mettre à jour les exemples few-shot. Puis relancer la boucle jusqu'à atteindre l'accord cible.
5. Recalibrer périodiquement, à mesure que les modes de défaillance évoluent.

#### 2.3 Évaluation humaine

Le jugement humain reste l'étalon-or pour la vérité terrain, les domaines à enjeux élevés, et la résolution des désaccords entre évaluateurs automatiques. Quatre scénarios où les humains sont essentiels : création de vérité terrain, sécurité et enjeux élevés, nuance et créativité, désaccord entre évaluateurs.

#### 2.4 Scénarios d'évaluation et méthodes recommandées

La règle générale : commencer avec 20 à 100 lignes labellisées par des experts métier. Ne passer à une force d'annotation à l'échelle que lorsque la grille est solide comme un roc et que le volume devient le goulot d'étranglement.

Et si vos experts ne s'accordent pas sur un label, **arrêtez**. Résolvez le désaccord humain avant d'automatiser quoi que ce soit.

### 3. Évaluer les systèmes agentiques

Les systèmes agentiques impliquent du raisonnement multi-étapes, des appels d'outils, de la logique de branchement et des transitions d'état intermédiaires. **Évaluer seulement la sortie finale est insuffisant** : une réponse finale correcte peut masquer un chemin de raisonnement cassé, des paramètres d'outil erronés, ou une trajectoire inefficace.

Il faut donc évaluer sur trois couches :

- **Niveau step** : évaluer les appels d'outils individuels ou les étapes de raisonnement.
- **Niveau trajectoire** : le chemin global était-il raisonnable et efficace ?
- **Niveau session** : l'interaction complète a-t-elle atteint l'objectif de la personne ?

Pour y parvenir, on peut exploiter le fait qu'un agent pousse généralement des traces et des spans sous une racine applicative. Cela contient le type d'agent, le sous-agent éventuellement invoqué, les entrées/sorties de l'agent, les outils appelés, et plus. Ces traces peuvent être écrites vers une plateforme d'observabilité ou un stockage persistant.

Ensuite, on peut utiliser un DFS ou un autre parcours d'arbre pour reconstruire la trace en mémoire. Cela permet de garantir que certains sous-agents ont été invoqués au bon moment, que l'agent a appelé les bons outils, etc. Et de scoper l'évaluation à des agents ou sous-agents spécifiques.

### 4. Une mise en pratique de bout en bout

**Scénario :** vous construisez un assistant IA qui répond aux questions sur les politiques de support d'une plateforme de voyage.

**Étape 1 : explorer et découvrir.** Faites passer 100 entrées dans votre prototype et lisez chaque sortie. Vous trouvez : 15 réponses ont généré des détails de politique absents des documents sources (*problème de fidélité*) ; 8 sont correctes mais trop verbeuses (*concision*) ; 5 ont refusé des questions valides (*sur-refus*) ; 3 avaient du JSON cassé (*format*).

**Étape 2 : construire les évals.** Ajoutez des checks programmatiques pour la validité JSON et les bornes de longueur. Écrivez un juge virtuel pour la fidélité (prompt séparé, modèle différent, chain-of-thought) et un autre pour la concision. Faites labelliser 60 exemples par votre PM ou votre expert métier, échecs inclus, comme golden set.

**Étape 3 : calibrer et itérer.** Votre juge de fidélité s'accorde avec le PM 78 % du temps. Pas assez. L'analyse révèle que le juge pénalise des paraphrases exactes comme « infidèles ». Mettez à jour la grille et ajoutez des exemples few-shot. L'accord grimpe à 88 %. Améliorez l'étape de récupération ; les échecs de fidélité chutent significativement.

*Note : quand on itère sur les modèles et les prompts, il vaut mieux fixer une variable à la fois. D'abord fixer le modèle et varier le prompt, puis fixer le prompt et varier le modèle, puis fixer les deux et varier la configuration de serving. À chaque étape, les résultats du juge virtuel réduisent le pool de candidats.*

## Pourquoi ça compte

C'est le retour d'expérience le plus complet publié sur l'évaluation GenAI en production, avec des seuils chiffrés utilisables tels quels (50-100 exemples dorés, 88-90 % d'accord, 3-5 juges). Et le point sur l'évaluation à trois niveaux des systèmes agentiques est exactement ce qui manque à la plupart des équipes qui déploient des agents aujourd'hui.
