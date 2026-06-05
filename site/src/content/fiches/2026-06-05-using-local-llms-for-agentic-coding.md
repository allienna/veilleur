---
title: "Using local LLMs for agentic coding"
date: 2026-06-05
url: "https://blog.alexewerlof.com/p/local-llms-for-agentic-coding"
authors: ["Alex Ewerlöf"]
keywords: [LLM locaux, agentic coding, Ollama, coût, souveraineté]
theme: "Tech"
tone: "tutorial"
used_in: ["2026-06-05"]
---

## Résumé

Guide pratique pour faire tourner des modèles de langage en local et les brancher sur des outils de code agentiques (Copilot, Pi). Motivé par le passage de GitHub Copilot à une facturation à l'usage, l'auteur — spécialiste des modèles locaux depuis trois ans — montre comment échapper au modèle du revendeur de tokens, pour des raisons de coût, de confidentialité et de souveraineté.

## Points clés

- GitHub a basculé Copilot vers une facturation à l'usage, supprimant même ses anciens modèles gratuits.
- En tant que revendeur de tokens, GitHub répercute des hausses : Google Flash 3.5 est ~3x plus cher que Flash 2.5, GPT 5.5 ~3x plus cher que 5.
- Les modèles locaux ont suffisamment progressé pour servir d'alternative crédible à l'agentic coding.
- L'auteur a expérimenté Llama.cpp, Ollama, LM Studio et Jan sur Linux, Mac et Windows (NVIDIA RTX, Apple M4, AMD ROCm).
- Dompter les petits modèles est plus difficile, mais permet ensuite de mieux exploiter les grands.

## Analyse approfondie

### Le déclencheur : la facturation à l'usage

Le point de départ est concret : il y a quatre jours, GitHub a basculé Copilot vers une facturation à l'usage. L'auteur le note avec ironie — Microsoft n'est pas devenu l'une des plus grandes entreprises du monde en faisant la charité. GitHub fonctionnait auparavant sur un modèle de crédits avec quelques modèles gratuits ; même ceux-ci ne le sont plus. La hausse est d'autant plus visible que GitHub est un revendeur de tokens : les modèles phares arrivent avec des augmentations significatives sans que la performance suive au même rythme. Google Flash 3.5 coûte environ 3 fois plus que Flash 2.5, GPT 5.5 environ 3 fois plus que GPT 5 — et Claude, déjà jugé trop cher, a vu ses prix ajustés à la baisse.

### L'alternative locale

La thèse : on n'est pas obligé de subir, car les modèles locaux ont beaucoup progressé. L'auteur, qui se spécialise sur ces modèles depuis trois ans (d'abord pour le coût lors du développement d'une app IA, puis pour la confidentialité et par passion du hardware), propose un parcours en trois volets : comment faire tourner des modèles locaux (avec une alternative cloud gratuite), comment configurer ses agents (Copilot et Pi), et une app de démo illustrant la puissance des modèles locaux. Il a éprouvé Llama.cpp, Ollama, LM Studio et Jan sur trois OS et trois familles de hardware (NVIDIA RTX, Apple M4, AMD ROCm).

### La courbe d'apprentissage

L'auteur prévient : dompter les petits modèles est bien plus difficile que d'utiliser les gros via API. Mais une fois cette maîtrise acquise, on tire aussi un meilleur parti des grands modèles. Le guide pose ensuite le vocabulaire de base (deep learning, mécanisme d'attention, LLM) avant d'entrer dans la configuration concrète.

## Pourquoi ça compte

Au moment où le code généré par IA devient la norme, ce guide rappelle qu'on peut éviter de remettre toute sa chaîne de production entre les mains d'un revendeur de tokens — la souveraineté technique et la maîtrise des coûts passent aussi par les modèles locaux.
