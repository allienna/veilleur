---
title: "Introducing Gemini 3.5 Flash Cyber"
date: 2026-07-23
url: https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/?utm_source=tldrit
authors: [Google DeepMind, Raluca Ada Popa, Four Flynn]
keywords: [Gemini, cybersécurité, CodeMender, dual-use, vulnérabilités]
theme: IA
tone: news
used_in: ["2026-07-23"]
---

## Résumé

Google DeepMind présente Gemini 3.5 Flash Cyber, un modèle de cybersécurité léger construit sur 3.5 Flash et fine-tuné pour trouver, valider et patcher des vulnérabilités rapidement et à moindre coût. Compte tenu de sa nature dual-use, Google le réserve d'abord à un programme pilote en accès limité destiné aux gouvernements et partenaires de confiance, via l'agent CodeMender. Sa légèreté permet de scanner de vastes bases de code en explorant de nombreux chemins d'exécution, là où un unique appel à un gros modèle coûteux créerait un goulot d'étranglement.

## Points clés

- Modèle cyber léger bâti sur Gemini 3.5 Flash, fine-tuné pour trouver, valider et patcher des vulnérabilités.
- Alternative rentable aux gros modèles de cybersécurité coûteux.
- Déploiement intentionnel vu la nature dual-use : accès limité, gouvernements et partenaires de confiance via CodeMender d'abord.
- Les capacités fondamentales de CodeMender arrivent aussi aux clients via les modèles Gemini généralement disponibles (Gemini Enterprise Agent Platform).
- Avantage des modèles légers : explorer un immense espace de recherche d'exécution via de multiples invocations plutôt qu'un seul appel coûteux.
- Intégrable dans les scans fréquents, les processus de lancement time-sensitive et les pipelines de scan de commits à grande échelle.

## Analyse approfondie

*21 juillet 2026 — Raluca Ada Popa et Four Flynn*

Google investit dans la cybersécurité depuis des années, pionnier de la découverte automatisée de vulnérabilités pour sécuriser les bases de code du monde entier. Des outils comme CodeMender, notre agent de sécurité du code, peuvent trouver et corriger automatiquement des vulnérabilités logicielles critiques. Mais alors que les agents IA deviennent plus capables de trouver des vulnérabilités plus vite que les défenseurs ne peuvent les corriger, répondre à cette menace mondiale exige une approche hautement capable, abordable et scalable.

Aujourd'hui, nous étendons nos efforts de longue date pour mieux préparer les défenseurs en introduisant Gemini 3.5 Flash Cyber, notre modèle de cybersécurité léger construit sur 3.5 Flash et fine-tuné pour trouver, valider et patcher des vulnérabilités rapidement et efficacement, le rendant plus performant sur ces tâches que les modèles Flash grand public de Gemini.

La performance et l'efficacité de Flash en font une base idéale pour nos efforts de modèle de cybersécurité. En s'appuyant sur Flash, 3.5 Flash Cyber offre une alternative rentable et hautement capable aux modèles de cybersécurité massifs et coûteux.

Étant donné la nature dual-use de cette technologie, nous avons adopté une approche intentionnelle de son déploiement. Dans le cadre d'un programme pilote en accès limité, 3.5 Flash Cyber sera exclusivement disponible pour les gouvernements et partenaires de confiance via CodeMender prochainement, avec une extension au fil du temps. Cela donnera aux défenseurs de première ligne une longueur d'avance pour trouver et corriger les vulnérabilités critiques avant qu'elles ne soient exploitées, tout en limitant les mésusages plus larges.

Séparément, nous apportons aussi les capacités fondamentales de CodeMender directement aux clients avec les modèles Gemini généralement disponibles, via la Gemini Enterprise Agent Platform.

### Le problème de l'espace de recherche : l'avantage des modèles légers en sécurité du code

Trouver des failles profondément enfouies exige d'explorer un immense espace de recherche d'exécution. S'appuyer sur un unique appel coûteux à un modèle de langage massif peut créer un goulot d'étranglement. 3.5 Flash Cyber est particulièrement adapté pour trouver des vulnérabilités là où l'agent doit scanner une grande base de code et analyser un grand nombre de chemins de code.

CodeMender invoque 3.5 Flash Cyber de multiples fois, afin que les agents puissent analyser bien plus de chemins de code pour découvrir et valider des vulnérabilités. Les sous-agents produisent ensuite un unique rapport de haute qualité.

Grâce à sa vitesse et son coût abordable, 3.5 Flash Cyber peut s'intégrer facilement dans des scans fréquents, des processus de lancement sensibles au temps ou des pipelines de scan de commits à grande échelle.

### Résultats de benchmark : une alternative efficace aux gros modèles de cybersécurité

Google a testé 3.5 Flash Cyber sur une variété de benchmarks de sécurité, le positionnant comme une alternative efficace et abordable face aux modèles de cybersécurité plus larges, avec des performances supérieures aux modèles Flash de base sur les tâches de découverte, validation et correction de vulnérabilités.

## Pourquoi ça compte

L'annonce, deux jours avant la divulgation de l'incident OpenAI/Hugging Face, illustre parfaitement la course offense/défense et le dilemme dual-use : le meilleur outil défensif est gardé sous accès restreint, alors que les capacités offensives, elles, se diffusent.
