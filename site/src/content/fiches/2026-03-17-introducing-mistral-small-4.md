---
title: "Introducing Mistral Small 4"
date: 2026-03-17
url: https://mistral.ai/news/mistral-small-4
authors: [Mistral AI]
keywords: [Mistral Small 4, MoE, open-source, multimodal, raisonnement]
theme: IA
tone: news
used_in: ["2026-03-17"]
---

## Résumé

Mistral AI annonce Mistral Small 4, un modèle hybride sous licence Apache 2.0 qui unifie les capacités de trois modèles précédents : Magistral (raisonnement), Devstral (coding agentique), et Mistral Small (instruct). Avec 119B paramètres totaux et seulement 6B actifs par token (Mixture of Experts), une fenêtre de contexte de 256k et un raisonnement configurable, le modèle vise à être le couteau suisse de l'inférence open-source.

## Points clés

- Architecture MoE : 128 experts, 4 actifs par token — 119B paramètres totaux, 6B actifs (8B avec embeddings)
- Fenêtre de contexte 256k — supporte les interactions longues et l'analyse documentaire
- Raisonnement configurable via `reasoning_effort` (none → low → medium → high)
- Multimodal natif : texte + images en entrée
- 40% de réduction de latence end-to-end, 3x plus de requêtes/seconde vs Small 3
- Membre fondateur de la NVIDIA Nemotron Coalition
- Apache 2.0 — libre d'utilisation, modification, distribution

## Analyse approfondie

### Le problème que Small 4 résout

Jusqu'ici, Mistral proposait des modèles spécialisés : Magistral pour le raisonnement avancé, Devstral pour le coding agentique, et Mistral Small pour les tâches conversationnelles rapides. Les utilisateurs devaient choisir et potentiellement orchestrer plusieurs modèles selon le contexte.

Mistral Small 4 consolide ces trois capacités dans une seule architecture. Que vous ayez besoin d'un assistant de chat, d'un partenaire de recherche, ou d'un agent de coding, Small 4 s'adapte — sans changer de modèle.

### Architecture technique

**Mixture of Experts (MoE)** : le modèle dispose de 128 experts spécialisés, avec 4 actifs par token. Cela permet d'avoir 119B paramètres totaux (capacité de spécialisation élevée) tout en n'en activant que 6B lors de l'inférence (efficacité computationnelle). C'est le même principe architectural que DeepSeek V3/R1.

**Raisonnement configurable** via le paramètre `reasoning_effort` :
- `none` : réponses rapides, style conversationnel équivalent à Small 3.2
- `low` / `medium` : raisonnement intermédiaire activé
- `high` : analyse approfondie pour les tâches complexes

**Multimodal natif** : accepte texte et images, ce qui ouvre des cas d'usage de parsing documentaire et d'analyse visuelle.

**Fenêtre de 256k** : supporte les interactions longues, l'analyse de gros documents, et les workflows agentiques avec beaucoup de contexte accumulé.

### Performances

- 40% de réduction de la latence end-to-end (configuration optimisée latence)
- 3x plus de requêtes par seconde (configuration optimisée débit) vs Mistral Small 3
- Résultats compétitifs sur les benchmarks de coding, raisonnement et multimodal (selon les graphiques publiés)

### Licences et écosystème

Apache 2.0 : libre d'utilisation commerciale, modification, redistribution. Mistral rejoint également la NVIDIA Nemotron Coalition comme membre fondateur, signalant un rapprochement avec l'écosystème NVIDIA pour l'optimisation de l'inférence.

## Pourquoi ça compte

Mistral Small 4 est un signal fort que la consolidation des capacités en un seul modèle polyvalent est la prochaine étape de l'open-source. Pour les équipes qui veulent déployer un seul modèle pour plusieurs usages (chat, coding, analyse documentaire), c'est une option sérieuse à évaluer.
