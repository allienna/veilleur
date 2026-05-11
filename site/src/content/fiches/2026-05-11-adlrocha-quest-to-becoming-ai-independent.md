---
title: "@adlrocha - In a quest to becoming AI-independent"
date: 2026-05-11
url: https://adlrocha.substack.com/p/adlrocha-in-a-quest-to-becoming-ai
authors: [adlrocha]
keywords: [AI independence, local inference, open weights, GitHub Copilot, switching costs, AI economics]
theme: IA
tone: opinion
used_in: ["2026-05-11"]
---

## Résumé

Suite à l'annonce du passage de GitHub Copilot à une facturation usage-based, l'auteur tire le bilan : les subscriptions IA "pas chères" ont toujours été un land grab destiné à créer une dépendance avant l'extraction de valeur. Il raconte son parcours concret pour devenir _AI-independent_ : achat de hardware capable d'inférence locale (Strix Halo Ryzen AI Max+, 128 Go), bascule progressive de ses workflows sur des modèles open weights, réduction de sa dépendance aux APIs cloud. Une vraie stratégie de continuité plutôt qu'une posture geek nostalgique.

## Points clés

- GitHub Copilot passe à la facturation usage-based : la fin de la subscription "all-you-can-eat" à 10 $/mois
- Les subscriptions IA à bas prix sont un mécanisme de capture de marché : chaque appel API est un data point d'entraînement et chaque workflow construit un switching cost
- Les AI labs subventionnent massivement les tokens pour construire la dépendance avant d'extraire la valeur
- Le coût réel par utilisateur dépasse largement les prix affichés des subscriptions
- L'auteur a investi dans un Strix Halo (Ryzen AI Max+ avec 128 Go de mémoire unifiée) comme daily driver pour l'inférence locale
- L'objectif : réduire la dépendance aux gros bills de tokens et aux subscriptions à quotas décroissants
- L'analogie : "l'AI bubble est plus un piège qu'une bulle"

## Analyse approfondie

Il y a quelques semaines, GitHub a annoncé que Copilot passe à la facturation usage-based. Fini les abonnements forfaitaires : à partir de maintenant, tout le monde paie pour les tokens consommés.

Si tu utilisais Copilot sur le free tier ou un plan individuel (comme c'était mon cas via un avantage pour contributeurs open-source actifs), ça pique probablement. Cet abonnement était la façon parfaite de tester chaque nouveau modèle sans devoir s'engager sur des subscriptions spécifiques, _avec un quota mensuel extrêmement généreux_. Je connais beaucoup de gens qui ont acheté Copilot plutôt qu'Anthropic parce que ça donnait accès à Sonnet et Opus avec des quotas plus élevés que ceux fournis dans Claude. **Donc la question évidente : pourquoi c'était si peu cher ?**

La réponse n'est définitivement pas la générosité. C'est notoire que les AI labs et les big tech subventionnent les coûts des tokens pour la même raison qu'une plateforme subventionne l'onboarding : **construire la dépendance avant d'extraire la valeur et d'écraser la concurrence**. Chaque appel API pas cher est aussi un data point d'entraînement. Chaque workflow que tu construis autour de leur service est un switching cost qu'ils accumulent à ton compte. GitHub Copilot à 10 $/mois n'a jamais été un produit soutenable, comme c'est probablement aussi le cas pour des produits plus populaires comme Claude Code et Codex. C'était un land grab déguisé en subscription. Le coût par utilisateur de toutes ces subscriptions IA (au moins de la part des entreprises bien financées qui peuvent se le permettre) excède largement le prix de leurs abonnements.

Mes lecteurs les plus fidèles savent à quel point je suis préoccupé par l'économie de l'IA depuis un moment. Dans un post précédent, j'ai déjà avancé que **"l'AI Bubble est plus un piège qu'une bulle"**, et que en accélérant l'adoption de l'IA pour nos workflows quotidiens, les entreprises essaient de créer une dépendance qu'elles peuvent ensuite exploiter. Quand j'ai pris conscience de ça à la fin de l'année dernière, j'ai **décidé d'acheter du hardware capable de faire tourner de l'inférence locale** pour commencer à minimiser ma dépendance aux gros bills de tokens et aux subscriptions à quotas décroissants.

### Mon parcours hardware

Mon voyage a commencé avec un chip Strix Halo, le Ryzen AI Max+ qui est devenu mon daily driver et qui me donne jusqu'à 128 Go de mémoire unifiée. C'est suffisant pour faire tourner localement des modèles de taille respectable, avec une latence acceptable pour le développement.

L'auteur détaille ensuite son setup logiciel : combinaison de modèles open weights (Qwen, DeepSeek, Llama dérivés), un orchestrateur léger pour router entre tâches courtes (local) et tâches longues (cloud quand nécessaire), des intégrations avec ses outils existants (IDE, terminal) qui basculent transparente entre inférence locale et appels API.

### L'argument économique long terme

Le calcul n'est pas seulement défensif. Sur deux ou trois ans :

- Le hardware s'amortit
- Les modèles open weights deviennent significativement plus capables à chaque release
- Les coûts d'inférence cloud, eux, augmentent (fin des subventions de capture)
- Le contrôle sur ses propres données et workflows augmente

À l'inverse, rester sur des subscriptions cloud signifie accepter de voir le prix triple ou quadrupler dans deux ans, sans avoir aucun levier de négociation parce qu'on a empilé deux ans de switching costs.

### Au-delà du dev individuel

L'auteur tire ensuite la conclusion pour les entreprises : la question stratégique n'est pas "quel cloud LLM on choisit" mais "quel niveau de dépendance on accepte". Les entreprises qui mettent tous leurs workflows critiques sur un seul fournisseur cloud sans aucune alternative locale signent en blanc un chèque pour les augmentations futures. L'inférence locale, même hybride (local + cloud), devient une stratégie de continuité business, pas une lubie technique.

## Pourquoi ça compte

C'est un manifeste pragmatique, ni techno-utopiste ni anti-IA. Pour un Engineering Director ou un Chief Architect, ça pose la question concrète de la dépendance fournisseur et de la souveraineté IA — au moment précis où les tarifs cloud commencent à monter.
