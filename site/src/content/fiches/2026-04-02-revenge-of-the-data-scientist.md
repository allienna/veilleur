---
title: "The Revenge of the Data Scientist"
date: 2026-04-02
url: "https://hamel.dev/blog/posts/revenge/"
authors: ["Hamel Husain"]
keywords: [data scientist, évaluation LLM, métriques, expérimentation, MLOps]
theme: "IA"
tone: opinion
used_in: ["2026-04-02"]
---

## Résumé

Hamel Husain argue que l'essor des LLMs n'a pas rendu les data scientists obsolètes — il les rend plus nécessaires que jamais. Si les APIs de modèles fondationnels permettent aux équipes de livrer de l'IA sans passer par l'entraînement, le vrai travail de fond reste le même : concevoir des expériences, définir des métriques pertinentes, valider des systèmes stochastiques et analyser des données. À travers cinq pièges récurrents dans les projets LLM, il montre que les lacunes observées sont précisément les fondamentaux du métier de data scientist.

## Points clés

- Les APIs LLM ont retiré les data scientists du chemin critique de la livraison IA, mais le travail de fond (métriques, expérimentation, évaluation) n'a pas disparu
- Le premier piège : utiliser des métriques génériques hors-étagère (ROUGE, BLEU, "helpfulness score") au lieu de métriques spécifiques à l'application
- Le deuxième piège : faire confiance à un LLM-juge sans le valider comme un classifieur — il faut des labels humains, un jeu de dev/test, et des métriques de précision/rappel
- Le troisième piège : générer des données de test synthétiques sans ancrage dans les logs de production réels
- Le quatrième piège : déléguer le labelling à des non-experts et ne pas regarder les données brutes — le processus de labelling lui-même définit ce qu'on veut mesurer
- Le cinquième piège : tout automatiser, alors que l'analyse exploratoire et la compréhension des données restent un travail humain irréductible

## Analyse approfondie

### Le harness, c'est de la data science

OpenAI a publié un billet sur [l'ingénierie de harness](https://openai.com/index/harness-engineering/) qui décrit comment Codex a travaillé pendant des mois sur un projet logiciel, de façon autonome, avec des agents développant du code encadrés par un harness de tests et de spécifications.

Un détail dans ce billet est facile à manquer : le harness inclut une stack d'observabilité — logs, métriques et traces exposées à l'agent pour qu'il sache quand il déraille. En plus des tests et spécifications, il y a des métriques. C'est un composant clé du système.

Le projet [auto-research](https://x.com/karpathy/status/1936185694238064845) d'Andrej Karpathy montre le même schéma : des modèles qui s'optimisent itérativement contre une métrique de validation loss. Même idée, harness différent.

Ce qu'il faut retenir : une grande partie du harness, c'est de la data science.

Il y a quelques années, les praticiens passaient des heures à examiner les données, vérifier l'alignement des labels et concevoir des métriques. Aujourd'hui, on construit sur des "vibes", on demande au modèle s'il a bien travaillé, et on utilise des bibliothèques de métriques prêtes à l'emploi sans regarder les données.

Cela se manifeste surtout autour du retrieval et des evals. Sans formation en data, les ingénieurs craignent ce qu'ils ne comprennent pas. Ils proclament que "le RAG est mort" ou que "les evals sont morts", tout en construisant des systèmes qui dépendent de ces concepts.

---

### Piège 1 : Les métriques génériques

Il est tentant de saisir un framework d'eval et d'utiliser ses métriques directement. Le problème : on ne sait pas ce qui est réellement cassé. La plupart des équipes affichent un dashboard avec des scores d'utilité, de cohérence, d'hallucination. Ces scores semblent raisonnables. Ils sont aussi suffisamment génériques pour être inutiles pour diagnostiquer les pannes spécifiques d'une application.

Un data scientist n'adopterait pas des métriques prêtes à l'emploi. Il explorerait les données, les traces, poserait la question "qu'est-ce qui est réellement cassé ici ?", et déterminerait la chose la plus précieuse à commencer à mesurer. Il y a une infinité de choses à mesurer. Il faut formuler des hypothèses et itérer.

Le meilleur remède à ce piège : regarder les données.

Que signifie "regarder les données" en pratique ? Cela signifie lire les traces. Coder son propre viewer de traces personnalisé pour éliminer les frictions et adapter l'affichage aux spécificités de son domaine. Prendre des notes sur les problèmes trouvés. Faire de l'analyse d'erreurs : catégoriser les pannes, comprendre quoi prioriser, décider sur quoi travailler.

Quand on regarde ses données, on finit par s'orienter vers des métriques spécifiques à l'application. Les métriques de similarité génériques comme ROUGE ou BLEU s'adaptent rarement aux sorties LLM. Les métriques qui comptent ressemblent à "Échec de planification d'agenda" ou "Échec d'escalade vers un humain".

S'il n'y a qu'une seule chose à retenir de ce billet : regarder les données. C'est l'activité au ROI le plus élevé qu'on puisse mener, et elle est souvent omise.

---

### Piège 2 : Les juges non vérifiés

Beaucoup d'équipes utilisent un LLM comme juge pour déterminer si leur IA fonctionne. La plupart du temps, personne n'a de bonne réponse à "comment faites-vous confiance au juge ?"

Le réflexe par défaut : demander à un LLM de noter les sorties sur une échelle et utiliser les chiffres. Un data scientist traiterait le juge comme un classifieur. On a une boîte noire qui donne une prédiction. Comment lui faire confiance ? Il faut obtenir des labels humains, partitionner les données en train/dev/test, et mesurer si le classifieur est fiable.

Sourcez des exemples few-shot depuis votre jeu d'entraînement. Faites du hill-climbing sur le prompt de votre juge contre un jeu de dev. Gardez un jeu de test de côté pour confirmer qu'on n'a pas surchargé. Si on a déjà fait du machine learning, c'est ennuyeux. Mais les gens ne le font pas. Vérifier les classifieurs est devenu un art perdu dans l'IA moderne.

Traitez également votre juge comme un classifieur dans la façon dont vous reportez les résultats. Partout où on regarde, on voit de l'accuracy reportée. Si un mode de panne se produit 5% du temps, l'accuracy cache les vraies performances du système. Il faut utiliser la précision et le rappel.

---

### Piège 3 : La mauvaise conception expérimentale

Il y a de nombreuses dimensions à ce sujet. En voici deux qui reviennent le plus souvent.

**Construire des jeux de test.** La plupart des équipes génèrent des données synthétiques en promptant un LLM : "Donne-moi 50 requêtes de test." On obtient des données génériques, non représentatives. Un data scientist regarderait d'abord les données de production réelles, utiliserait des hypothèses pour déterminer quelles dimensions comptent, puis générerait des exemples synthétiques le long de ces dimensions.

Ancrez les données synthétiques dans des logs ou traces réels. Déterminez quelles dimensions faire varier. Injectez des cas limites. Basez les données synthétiques sur des données réelles.

**La conception des métriques.** Les équipes regroupent des rubriques entières dans un seul appel LLM et utilisent par défaut des échelles de Likert de 1 à 5. Un data scientist réduirait la complexité, rendrait chaque métrique actionnable et la lierait à un résultat business. Il faut remplacer les échelles subjectives par des passes/échecs binaires sur des critères scoped. Les échelles de Likert masquent l'ambiguïté et reportent les décisions difficiles sur les performances du système.

---

### Piège 4 : Les mauvaises données et labels

Les data scientists ne font pas confiance aux données. Ils ne font pas confiance aux labels. Ils ne font confiance à rien. Ils sont sceptiques par formation. Les ingénieurs IA en général n'ont pas encore développé ce muscle.

Pour le labelling, la plupart des équipes en font le problème de quelqu'un d'autre. Le labelling paraît inglamoureux, alors il est délégué à l'équipe dev ou externalisé. Un data scientist insisterait pour que des experts du domaine labelisent les données, resterait sceptique vis-à-vis des labels, et regarderait les données.

Mais le labelling compte pour une raison plus profonde que la qualité des labels. Il est impossible de savoir ce qu'on veut à moins de regarder les données. Il existe un concept appelé "criteria drift", validé dans un [papier de Shreya Shankar et ses collègues](https://arxiv.org/abs/2404.12272) : les utilisateurs ont besoin de critères pour noter les sorties, mais noter les sorties aide les utilisateurs à définir leurs critères. Les gens ne savent pas ce qu'ils veulent avant de voir les sorties du LLM. Le processus de labelling lui-même révèle ce qui compte.

Les data scientists défendent cette approche : mettre des experts du domaine et des product managers face aux données brutes, pas aux scores de synthèse.

---

### Piège 5 : Trop automatiser

Tout ceci est un travail humain. La tentation est de l'automatiser.

Les LLMs peuvent aider à câbler les choses, écrire la plomberie, générer du boilerplate pour les évaluations. Ils ne peuvent pas regarder les données à votre place, pour la raison exacte qu'on vient de voir : on ne sait pas ce qu'on veut avant de voir les sorties.

---

### Autres pièges

Quelques autres en survol rapide : mal utiliser les scores de similarité. Poser des questions vagues au juge comme "est-ce utile ?". Faire lire du JSON brut aux annotateurs. Rapporter des scores non calibrés sans intervalles de confiance. La dérive des données, l'overfitting, le mauvais échantillonnage, les dashboards qui n'ont pas de sens.

---

### La correspondance

Si on prend du recul, chaque piège ci-dessus a la même cause racine : l'absence d'un fondamental de data science.

Lire les traces et catégoriser les pannes, c'est de l'Analyse Exploratoire des Données. Valider un juge LLM contre des labels humains, c'est de l'Évaluation de Modèle. Construire des jeux de test représentatifs à partir des données de production, c'est de la Conception Expérimentale. Faire labelliser les sorties par des experts du domaine, c'est de la Collecte de Données. Surveiller si son produit fonctionne en production, c'est du ML en Production. Rien de tout cela n'est nouveau. Les noms ont changé, le travail non.

Python reste le meilleur outillage pour regarder ses données et travailler avec des données.

Hamel Husain a aussi construit un [plugin open-source](https://github.com/hamelsmu/evals-skills) qui approfondit ces points. Il suffit de le pointer vers son pipeline d'évaluation et il indique ce qu'on fait de travers.

**Toujours regarder les données.**

## Pourquoi ça compte

Cet article offre un cadre de lecture puissant pour comprendre pourquoi tant de projets LLM échouent en production : non pas par manque d'IA, mais par manque de rigueur data. Il réhabilite des fondamentaux souvent méprisés dans la frénésie actuelle autour des agents.
