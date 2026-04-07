---
title: "What is inference engineering? Deepdive"
date: 2026-04-07
url: https://link.mail.beehiiv.com/ss/c/u001.yC9eJs5Q3flddlsql05gYc6Roum41tU9YvWrxTcURupr9TFTmoGO6OCTwo0MrYEwHs8CxH9wrc4EVWV6l1x1Fvsq-UB7KYdUk7DQkJuAnoI6BKsB5FGVlJqhX2TcgmFvRtGdp-K0yO3P1Lt4wbRXO7Ed4gqANVi0Q_ggVMuaVA0z83MdiAOZjCSi8DIsbKI2_mNM3T14ZDILccV7bJrDrQ/4pl/3VF-0GN0Qn2fAP3iSzFi1w/h14/h001.cebkFxZB3-UZq81Dhqy1qwkUlwItpjelQVoikmwVslw
authors: ["Gergely Orosz", "Philip Kiely"]
keywords: [inference, engineering, LLM, optimization, open-source]
theme: IA
tone: tutorial
used_in: ["2026-04-07"]
---

## Résumé

L'inference engineering désigne la discipline qui consiste à optimiser l'exécution des modèles de langage en production — c'est-à-dire la phase où un modèle prend une entrée et génère une sortie, token par token. Longtemps réservée aux quelques milliers d'ingénieurs qui construisent les modèles chez les grands labos, cette discipline devient accessible à tous les ingénieurs grâce à l'essor des modèles open source. Gergely Orosz et Philip Kiely (The Pragmatic Engineer) proposent un tour d'horizon complet des techniques clés et de leur impact concret sur les performances et les coûts. L'exemple de Cursor, qui a construit Composer 2.0 sur le modèle open Kimi 2.5 en appliquant de l'inference engineering, illustre que cette pratique est en train de devenir une compétence mainstream pour les équipes produit.

## Points clés

- L'inference correspond à la phase où un modèle existant prend une entrée et génère une sortie, un token à la fois
- Avec les modèles fermés (closed models), l'inference engineering était le domaine exclusif des équipes internes des grands labos d'IA
- Les modèles open source changent la donne : n'importe quel ingénieur peut désormais optimiser l'inference
- Cursor a construit Composer 2.0 sur le modèle open Kimi 2.5 grâce à de l'inference engineering
- Les techniques clés sont : le batching, le speculative decoding, la quantization et l'optimisation du KV cache
- L'inference engineering est en train de devenir une discipline à part entière du génie logiciel

## Analyse approfondie

### Qu'est-ce que l'inference ?

L'inference, c'est ce qui se passe après l'entraînement. Lorsqu'un modèle de langage reçoit une requête et produit une réponse, il effectue de l'inference — en générant chaque token de manière séquentielle, l'un après l'autre. Contrairement à l'entraînement, qui ne se produit qu'une fois (ou quelques fois, lors des mises à jour du modèle), l'inference se produit des millions ou des milliards de fois par jour dans un système en production. C'est cette fréquence d'exécution qui rend son optimisation si stratégique.

### Du monopole des labos à la discipline mainstream

Pendant longtemps, optimiser l'inference n'était pas un problème que la plupart des ingénieurs avaient à résoudre. Avec des modèles fermés comme GPT-4 ou Claude, le fournisseur gère intégralement l'infrastructure d'inference : le développeur se contente d'appeler une API. Les décisions d'optimisation — combien de requêtes traiter en parallèle, quelle précision numérique utiliser, comment accélérer la génération — restaient l'affaire exclusive des quelques milliers d'ingénieurs IA employés par OpenAI, Anthropic, Google ou Mistral.

L'essor des modèles open source renverse cette logique. Lorsqu'une équipe déploie elle-même un modèle comme Kimi 2.5, Mistral, Llama ou Qwen, elle hérite de toutes les responsabilités d'inference : coûts de compute, latence, débit, disponibilité. L'inference engineering devient alors un levier concurrentiel direct.

### Le cas Cursor : Composer 2.0 sur Kimi 2.5

L'article cite Cursor comme exemple emblématique. L'équipe a construit Composer 2.0 — leur fonctionnalité d'édition de code assistée par IA — en s'appuyant sur le modèle open Kimi 2.5, puis en appliquant des techniques d'inference engineering pour en extraire les meilleures performances possibles. Ce choix illustre une tendance plus large : des équipes produit qui ne se contentent plus de choisir un modèle sur étagère, mais qui s'approprient la couche d'exécution pour optimiser leur expérience utilisateur et leur structure de coûts.

### Les quatre techniques fondamentales

**Batching** — Plutôt que de traiter les requêtes une par une, le batching consiste à les regrouper et à les exécuter simultanément sur le GPU. Les GPUs sont des architectures massivement parallèles : ils sont beaucoup plus efficaces lorsqu'ils traitent de nombreux calculs en même temps. Le batching permet d'augmenter le débit (nombre de tokens générés par seconde) sans augmenter le coût unitaire de manière proportionnelle.

**Speculative decoding** — La génération token par token est intrinsèquement séquentielle, ce qui limite la parallélisation. Le speculative decoding contourne cette contrainte en utilisant un modèle "draft" plus petit et rapide pour proposer plusieurs tokens à l'avance, que le modèle principal valide ou rejette en un seul passage. Lorsque les prédictions du modèle draft sont correctes — ce qui arrive souvent pour les tokens "évidents" — on accélère significativement la génération sans sacrifier la qualité.

**Quantization** — Les modèles de langage stockent leurs poids sous forme de nombres en virgule flottante. Par défaut, chaque poids occupe 32 bits (ou 16 bits en demi-précision). La quantization consiste à réduire cette précision — par exemple à 8 bits ou 4 bits — pour diminuer l'empreinte mémoire et accélérer les calculs. La contrepartie est une légère dégradation de la qualité, que les techniques modernes de quantization parviennent à minimiser. Un modèle quantisé peut tenir sur un GPU moins coûteux, voire sur du matériel grand public.

**Optimisation du KV cache** — Lors de la génération, le modèle calcule des représentations intermédiaires (clés et valeurs dans les couches d'attention) pour chaque token du contexte. Sans optimisation, ces calculs sont refaits à chaque étape. Le KV cache (Key-Value cache) mémorise ces représentations pour les réutiliser, évitant des calculs redondants massifs. L'optimisation du KV cache porte sur sa taille, sa compression et sa gestion en mémoire — des choix qui impactent directement la latence et le coût par token sur de longs contextes.

### Une discipline en cours de structuration

Orosz et Kiely soulignent que l'inference engineering n'est pas encore aussi codifiée que d'autres spécialités du génie logiciel. Les outils, les frameworks (vLLM, TensorRT-LLM, llama.cpp…) et les pratiques évoluent rapidement. Mais la direction est claire : à mesure que les modèles open source gagnent en qualité et que les équipes cherchent à contrôler leurs coûts d'IA, la maîtrise de l'inference devient un avantage compétitif — et bientôt une compétence attendue dans les équipes qui déploient des systèmes d'IA en production.

## Pourquoi ça compte

L'inference engineering marque le passage de l'IA générative d'une consommation passive via API à une discipline d'ingénierie à part entière, où les équipes qui maîtrisent l'optimisation de l'exécution des modèles ouverts gagneront un avantage décisif en termes de coûts, de latence et de différenciation produit.
