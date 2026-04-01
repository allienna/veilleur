---
title: "Harness design for long-running application development"
date: 2026-03-31
url: https://www.anthropic.com/engineering/harness-design-for-long-running-agents
authors:
  - Prithvi Rajasekaran (Anthropic Labs)
keywords:
  - agent harness
  - multi-agent architecture
  - autonomous coding
  - evaluator design
  - GAN-inspired
theme: IA
tone: research
used_in:
  - "2026-03-31"
---

## Résumé

Anthropic Labs présente une architecture multi-agents pour le développement logiciel autonome de longue durée. Le design repose sur trois agents spécialisés — planificateur, générateur et évaluateur — inspiré des GANs. L'insight clé est que la qualité de l'évaluateur, et non celle du générateur, constitue le facteur limitant du système. L'approche produit des applications full-stack complètes lors de sessions autonomes de plusieurs heures.

## Points clés

- Les implémentations naïves à agent unique échouent sur les tâches complexes : l'agent accumule des erreurs, perd le contexte et tourne en boucle sur les mêmes problèmes
- L'architecture à trois agents (planificateur, générateur, évaluateur) résout ces problèmes en séparant décomposition, implémentation et jugement
- L'évaluateur utilise des critères structurés inspirés des GANs : des grilles de notation concrètes transformant les jugements subjectifs en évaluations graduées
- La qualité de l'évaluateur est la contrainte limitante du système — améliorer le générateur sans améliorer l'évaluateur ne produit aucun gain
- La décomposition en morceaux gérables et le transfert de contexte via des artefacts structurés sont essentiels pour les sessions longues
- Le cycle générateur-évaluateur tourne en autonomie pendant des heures, produisant des applications full-stack complètes

## Analyse approfondie

### Pourquoi les implémentations naïves échouent

Anthropic a précédemment montré que le design du harnais a un impact substantiel sur l'efficacité des agents de code longue durée. Dans une expérimentation antérieure, ils utilisaient un agent initialiseur pour décomposer une spécification produit en liste de tâches, et un agent de code qui implémentait les tâches feature par feature avant de transférer des artefacts pour maintenir le contexte entre les sessions. La communauté développeur au sens large a convergé vers des insights similaires, avec des approches comme la méthode "Ralph Wiggum" utilisant des hooks ou scripts pour maintenir les agents dans des cycles d'itération continus.

Mais certains problèmes persistaient. Pour des builds plus complexes, les agents avaient tendance à tourner en rond — échouant à reproduire un résultat correct après un changement, perdant du temps à basculer entre solutions partielles, ou accumulant silencieusement de la dette technique. Ces problèmes ne se résolvent pas en améliorant la capacité du modèle. Ils nécessitent une meilleure structure autour du modèle.

### L'architecture planner-generator-evaluator

En s'inspirant des Generative Adversarial Networks (GANs), Prithvi Rajasekaran a conçu une structure multi-agents avec un **générateur** et un **évaluateur**. Construire un évaluateur capable de noter les sorties de manière fiable — et avec du goût — a d'abord nécessité de développer un ensemble de critères capables de transformer des jugements subjectifs comme "est-ce que ce design est bon ?" en termes concrets et évaluables.

Le **planificateur** décompose la spécification produit en tâches ordonnées, optimisées pour la mise en œuvre séquentielle. Chaque tâche contient suffisamment de contexte pour être autonome tout en restant cohérente avec le plan global.

Le **générateur** implémente les tâches une par une, produisant du code fonctionnel à chaque étape. Il reçoit le plan, le contexte accumulé des implémentations précédentes, et les éventuels feedbacks de l'évaluateur.

L'**évaluateur** est le composant le plus innovant. Il note chaque sortie selon des grilles de qualité structurées, avec des critères concrets allant de "les pages sont vides" à "production-ready". Quand l'évaluateur rejette une itération, le générateur reçoit le feedback détaillé et recommence.

### L'insight central : le goût est la contrainte limitante

Le résultat le plus contre-intuitif de cette recherche est que la qualité de l'évaluateur plafonne les performances du système entier. Améliorer le modèle qui génère le code ne sert à rien si le modèle qui juge n'a pas les bons critères ou le bon niveau d'exigence.

> « The key insight from our research was that taste and evaluation quality were the binding constraint on the system, not generation capability. »

Cela signifie que l'investissement le plus rentable n'est pas dans un meilleur modèle de génération, mais dans de meilleurs critères d'évaluation, de meilleures grilles de notation, et une meilleure capacité à distinguer "ça compile" de "c'est réellement bon".

### Application au design frontend

L'approche a été validée sur deux domaines très différents : le design frontend (jugement subjectif, question de goût) et le code autonome (correction vérifiable, fonctionnalité). Le fait que les mêmes principes architecturaux tiennent dans les deux cas renforce la généralité de l'approche.

Pour le frontend spécifiquement, l'évaluateur a dû développer des critères de "goût" — des grilles capables de noter la qualité visuelle, la cohérence de design, l'utilisabilité. Ces critères ont permis de dépasser le plafond que les approches à agent unique atteignaient systématiquement.

### Résultats

L'architecture finale produit des applications full-stack riches lors de sessions de code autonome de plusieurs heures. La combinaison planification-génération-évaluation permet de maintenir la qualité sur des durées beaucoup plus longues que les approches traditionnelles, tout en réduisant l'accumulation de dette technique et les boucles de régression.

## Pourquoi ça compte

Cette recherche marque un tournant dans la conception d'agents de code : le modèle seul ne suffit plus, c'est l'architecture du système autour (le "harnais") qui détermine la qualité des résultats. L'insight sur l'évaluateur comme contrainte limitante a des implications profondes pour toute équipe construisant des agents autonomes.
