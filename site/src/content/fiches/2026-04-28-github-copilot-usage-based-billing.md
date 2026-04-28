---
title: "GitHub Copilot is moving to usage-based billing"
date: 2026-04-28
url: "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"
authors: ["GitHub"]
keywords: [Copilot, usage-based billing, AI Credits, agentic platform, pricing]
theme: "IA"
tone: "news"
used_in: ["2026-04-28"]
---

## Résumé

GitHub annonce que tous les plans Copilot basculent en facturation à l'usage le 1er juin 2026. Les "premium request units" sont remplacées par des "GitHub AI Credits" calculés sur la consommation réelle de tokens. Le prix de base reste le même, mais les utilisateurs intensifs d'agents devront acheter des crédits supplémentaires. Le message implicite : le forfait n'est plus tenable face à l'usage agentique qui peut consommer des heures d'inférence en une session.

## Points clés

- Tous les plans Copilot basculent en usage-based billing le 1er juin 2026
- Les premium request units (PRUs) sont remplacées par des GitHub AI Credits
- La consommation est calculée sur les tokens (input, output, cached) selon les tarifs API publics
- Les prix de base ne changent pas : Pro 10 $/mois, Pro+ 39 $/mois, Business 19 $/user/mois, Enterprise 39 $/user/mois
- Code completions et Next Edit suggestions restent inclus, ne consomment pas de credits
- Plus de fallback model : on tape sur les credits ou les contrôles de budget admin
- Copilot code review consommera aussi des minutes GitHub Actions
- Pour les business : pooled credits à travers l'organisation pour éviter la capacité gaspillée
- Une expérience de "preview bill" arrive début mai pour visualiser les coûts projetés

## Analyse approfondie

### Aujourd'hui, l'annonce

GitHub annonce que tous les plans Copilot vont basculer en usage-based billing le **1er juin 2026**.

Au lieu de compter les premium requests, chaque plan Copilot inclura un quota mensuel de **GitHub AI Credits**, avec l'option pour les plans payants d'acheter de l'usage additionnel. La consommation sera calculée sur la consommation de tokens, incluant input, output et cached tokens, en utilisant les tarifs API publiés pour chaque modèle.

Ce changement aligne les prix Copilot avec l'usage réel et est une étape importante vers une expérience et un business Copilot durables et fiables pour tous les utilisateurs.

Pour aider les clients à se préparer, GitHub lance également une expérience de **preview bill** début mai, donnant aux utilisateurs et aux admins de la visibilité sur les coûts projetés avant la transition du 1er juin.

### Pourquoi ce changement

Copilot n'est plus le même produit qu'il y a un an.

Il a évolué d'un assistant in-editor vers une plateforme agentique capable d'exécuter de longues sessions de coding multi-étapes, en utilisant les derniers modèles, et en itérant à travers des repos entiers. L'usage agentique devient le défaut, et il apporte des demandes en compute et inférence significativement plus élevées.

Aujourd'hui, une question rapide en chat et une session de coding autonome multi-heures peuvent coûter le même montant à l'utilisateur. GitHub a absorbé une grande partie du coût d'inférence en escalade derrière cette consommation, mais le modèle actuel de premium request n'est plus tenable.

L'usage-based billing répare ça. Il aligne mieux les prix avec l'usage réel, aide à maintenir la fiabilité du service à long terme, et réduit le besoin de gater les heavy users.

### Ce qui change concrètement

À partir du **1er juin**, les premium request units (PRUs) seront remplacées par des **GitHub AI Credits**.

Les credits seront consommés en fonction de l'usage de tokens, incluant input, output et cached tokens, selon les tarifs API publiés pour chaque modèle.

Quelques détails importants :

- **Le prix des plans de base ne change pas.** Copilot Pro reste à 10 $/mois, Pro+ reste à 39 $/mois, Business reste à 19 $/user/mois, et Enterprise reste à 39 $/user/mois.
- **Code completions et Next Edit suggestions restent inclus** dans tous les plans et ne consomment pas d'AI Credits.
- **Les expériences de fallback ne seront plus disponibles.** Aujourd'hui, les utilisateurs qui épuisent leurs PRUs peuvent basculer sur un modèle moins cher et continuer à travailler. Dans le nouveau modèle, l'usage sera plutôt gouverné par les credits disponibles et les contrôles de budget admin.
- **Copilot code review consommera aussi des minutes GitHub Actions**, en plus des GitHub AI Credits. Ces minutes sont facturées aux mêmes tarifs par minute que les autres workflows GitHub Actions.

### Pour les individus

Les abonnements mensuels Copilot Pro et Pro+ incluront des AI Credits mensuels alignés sur leurs prix actuels :

- **Copilot Pro :** 10 $/mois, incluant 10 $ d'AI Credits mensuels
- **Copilot Pro+ :** 39 $/mois, incluant 39 $ d'AI Credits mensuels

Les utilisateurs sur un plan mensuel Pro ou Pro+ migreront automatiquement vers l'usage-based billing le 1er juin 2026.

Les utilisateurs sur des plans annuels Pro ou Pro+ resteront sur leur plan existant avec la tarification basée sur les premium requests jusqu'à expiration de leur plan.

### Pour les businesses et enterprises

Le prix par siège mensuel de Copilot Business et Copilot Enterprise reste inchangé :

- **Copilot Business :** 19 $/user/mois, incluant 19 $ d'AI Credits mensuels
- **Copilot Enterprise :** 39 $/user/mois, incluant 39 $ d'AI Credits mensuels

Pour soutenir la transition, les clients existants Copilot Business et Copilot Enterprise recevront automatiquement de l'usage promotionnel inclus pour juin, juillet et août :

- **Copilot Business** : 30 $ d'AI Credits mensuels
- **Copilot Enterprise** : 70 $ d'AI Credits mensuels

GitHub introduit aussi du pooled included usage à travers une organisation, ce qui aide à éliminer la capacité orpheline. Au lieu que l'usage inclus inutilisé de chaque user soit isolé, les credits peuvent être mutualisés à travers l'organisation.

Les admins auront aussi de nouveaux contrôles de budget.

## Pourquoi ça compte

C'est un signal majeur que le modèle économique du SaaS forfaitaire ne survit pas au passage à l'agentique. Quand un utilisateur peut déclencher une session multi-heures consommant des dizaines de dollars d'inférence pour 10 $/mois, le forfait devient un cauchemar de coût pour le fournisseur. Pour les Engineering Directors, c'est l'amorce d'une vraie discipline FinOps autour des outils de coding agentique.
