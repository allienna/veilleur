---
title: "Separating signal from noise in coding evaluations"
date: 2026-07-09
url: https://links.tldrnewsletter.com/IARtyA
authors: [OpenAI]
keywords: [SWE-bench Verified, benchmark, évaluation, contamination, code]
theme: IA
tone: research
used_in: ["2026-07-09"]
---

## Résumé

OpenAI a audité SWE-bench Verified, l'un des benchmarks de code les plus utilisés, et y a trouvé un taux massif de tâches défectueuses : son pipeline automatique a signalé 200 tâches cassées (27,4 %), et une campagne d'annotation humaine en a identifié 249 (34,1 %). Les défauts se répartissent en quatre familles (tests trop stricts, prompts sous-spécifiés, tests à faible couverture, prompts trompeurs). La conséquence est directe : une part importante des scores publiés ne mesure pas la compétence du modèle mais la qualité du test, ce qui fausse les décisions de déploiement et de sécurité.

## Points clés

- Mesurer correctement les capacités d'un modèle conditionne des décisions de déploiement et de sûreté (cadre Preparedness d'OpenAI).
- OpenAI avait déjà cessé d'utiliser SWE-bench Verified après avoir constaté des problèmes de conception et de contamination.
- Pipeline d'analyse : 200 tâches (27,4 %) signalées comme cassées ; annotation humaine : 249 tâches (34,1 %).
- Quatre catégories de défauts : tests trop stricts, prompts sous-spécifiés, tests à faible couverture, prompt trompeur.
- Chaque tâche suspecte est revue par plusieurs passes d'agents investigateurs puis par cinq ingénieurs expérimentés, les désaccords étant escaladés.

## Analyse approfondie

Mesurer précisément les capacités des modèles est essentiel pour prendre des décisions de déploiement et de sûreté saines, y compris dans le cadre du Preparedness Framework d'OpenAI. À chaque sortie de modèle, OpenAI rapporte des résultats sur une variété de benchmarks externes et internes pour suivre les progrès. Mais quand une évaluation comporte des défauts qui affectent ses résultats, elle peut donner une compréhension erronée des capacités, fausser les dossiers de sûreté et déformer les priorités de recherche.

OpenAI avait récemment enquêté sur la façon dont l'un des benchmarks de code les plus utilisés, SWE-bench Verified, souffrait de problèmes fondamentaux de conception et de contamination, au point de ne plus fournir de signal significatif sur les capacités de développement logiciel. L'équipe avait alors encouragé la communauté à migrer vers une version plus robuste.

La méthode d'audit repose sur un pipeline : chaque tentative du modèle sur une tâche est examinée avec les métadonnées de la tâche et les traces d'échec, afin de repérer les défauts probables d'évaluation. Chaque tâche signalée est ensuite évaluée par plusieurs passes d'agents investigateurs indépendants, puis revue par cinq ingénieurs logiciels expérimentés, les désaccords étant escaladés pour investigation complémentaire.

Résultat : des preuves de problèmes bloquants sur une portion significative du jeu de données. L'analyse automatique a signalé 200 tâches cassées (27,4 %), tandis que la campagne d'annotation humaine en a identifié 249 (34,1 %).

Les problèmes tombent principalement dans quatre catégories :

- **Tests trop stricts** : ils imposent des détails d'implémentation précis non spécifiés dans le prompt, invalidant de nombreuses soumissions pourtant fonctionnellement correctes.
- **Prompts sous-spécifiés** : ils omettent des exigences que des tests cachés font pourtant respecter, exigences non raisonnablement devinables.
- **Tests à faible couverture** : ils vérifient insuffisamment la fonctionnalité demandée, si bien que des correctifs incomplets peuvent passer.
- **Prompt trompeur** : il oriente le modèle vers un mauvais comportement, en contradiction avec ce que les tests exigent.

Ces constats pointent la difficulté intrinsèque de construire des évaluations de code fiables, et rappellent qu'un score de benchmark n'a de valeur que si l'instrument qui le produit est lui-même vérifié.

## Pourquoi ça compte

Quand un tiers du benchmark de référence du code est défectueux, tous les classements de modèles qui s'en réclament perdent en fiabilité. C'est un signal fort pour toute équipe qui choisit un modèle sur la foi de ses scores : il faut auditer l'instrument avant de faire confiance à la mesure.
