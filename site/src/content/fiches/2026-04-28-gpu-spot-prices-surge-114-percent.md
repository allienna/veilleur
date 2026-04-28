---
title: "GPU Spot Prices Surge 114% in Six Weeks"
date: 2026-04-28
url: "https://tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/"
authors: ["Tomasz Tunguz"]
keywords: [GPU pricing, B200, NVIDIA, spot market, model releases]
theme: "IA"
tone: "research"
used_in: ["2026-04-28"]
---

## Résumé

Les prix au comptant du GPU NVIDIA B200 ont bondi de 114 % en six semaines, passant de 2,31 $/h début mars à 4,95 $/h. Tomasz Tunguz montre que ces hausses corrélent avec chaque release de modèle frontier (GPT-5.5, Codex), que le spread entre fournisseurs s'élargit, et que l'écart B200/H200 a doublé. Conclusion : le sellers' market est de retour, et les startups IA qui tablaient sur une baisse continue du coût d'inférence devront revoir leurs unit economics.

## Points clés

- B200 NVIDIA passé de 2,31 $/h (début mars) à 4,95 $/h cette semaine : +114 % en six semaines
- Le spread sur les anciennes générations a doublé : de 0,28 $/h à 1,80 $/h entre B200 et H200
- Chaque release majeure de modèle depuis septembre 2025 précède ou coïncide avec un saut de prix B200
- GPT-5.5 demande de la mémoire B200 que seul Blackwell fournit
- Le spread entre fournisseurs explose : marché opaque avec gros chocs supply/demand
- L'écart B200/H200 s'était effondré en novembre puis a re-creusé depuis février
- Pour les cloud providers : le pricing power revient après six mois de compression de marges
- Pour les startups IA : le marché spot anticipe les contrats — il faut ré-estimer la trésorerie

## Analyse approfondie

Les prix de location GPU les plus récents de NVIDIA sur l'Ornn Compute Price Index ont atteint 4,95 $ par heure cette semaine, contre 2,31 $ début mars : une hausse de 114 % en six semaines.

Le spread de prix par rapport aux puces de génération précédente a doublé, passant de 0,28 $ à 1,80 $ par heure. La nouvelle puce est le B200 de NVIDIA (Blackwell) ; la génération précédente est le H200 (Hopper).

> Le marché GPU devient lucide — même si le brouillard ne s'est pas levé.

### 1. Les releases de modèles frontier corrèlent avec des chocs de demande

Les pics de prix coïncident avec les lancements majeurs de modèles. Chaque release de modèle majeur depuis septembre 2025 a précédé ou coïncidé avec des sauts de prix B200.

La context window étendue de GPT-5.5 nécessite la mémoire que seul Blackwell fournit.

La corrélation n'est pas parfaite. Les chocs d'approvisionnement comptent aussi. Mais le pattern est clair : les nouveaux modèles ont besoin des nouvelles puces.

### 2. L'écart entre fournisseurs les plus chers et les moins chers explose

En septembre 2025, les prix B200 chez les différents fournisseurs étaient regroupés étroitement. Aujourd'hui le spread a plus que doublé. Certains fournisseurs offrent encore le B200 à des prix proches du H200. D'autres demandent des primes de rareté.

Cela porte les marques d'un marché opaque avec de gros chocs supply/demand. Quand un hyperscaler reçoit-il une nouvelle livraison ? Quelle startup IA a sur-acheté de la capacité et la revend maintenant à perte ? L'opacité partout où on regarde.

### 3. L'écart de prix B200-sur-H200 s'est effondré, puis a récupéré

Quand le B200 est arrivé sur le marché en septembre 2025, il coûtait plus par heure que le H200. Les acheteurs payaient plus pour la mémoire supplémentaire et la densité d'inférence.

En novembre, cet écart s'est effondré à 0,28 $ alors que l'offre inondait le marché. Pendant une brève fenêtre, B200 et H200 ont atteint une quasi-parité de prix.

Depuis février, quand GPT-5.3-Codex a été lancé, le spread s'est ré-élargi. L'écart actuel de 1,80 $ est de retour proche des niveaux de lancement.

L'élargissement de l'écart est aussi un signal de dépréciation : les puces plus anciennes perdent de la valeur quand les nouveaux modèles demandent de nouvelles architectures.

### Implications

Pour les cloud providers, le pricing power revient. Après six mois de compression de marge, le sellers' market est de retour.

Pour les startups IA, le marché spot anticipe les prix contractuels.

## Pourquoi ça compte

Ces chiffres anéantissent l'hypothèse implicite de toutes les business cases IA construites en 2025 : "le coût d'inférence va continuer à baisser". En réalité, à chaque saut technologique, les nouveaux modèles demandent les nouveaux GPUs, et le pricing power retombe entre les mains de NVIDIA et des hyperscalers. Pour les CFO et CTO, c'est un argument fort pour modéliser plusieurs scénarios de coûts d'inférence — pas juste le cas optimiste.
