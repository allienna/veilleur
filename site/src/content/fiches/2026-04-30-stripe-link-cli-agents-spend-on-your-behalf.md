---
title: "GitHub - stripe/link-cli: Let your agents spend on your behalf. Your payment credentials are never exposed. You approve every purchase."
date: 2026-04-30
url: https://github.com/stripe/link-cli
authors: [Stripe]
keywords: [agentic-payments, stripe, link, cli, agent-permissions]
theme: IA
tone: news
used_in: ["2026-04-30"]
---

## Résumé

Stripe ouvre `link-cli`, un outil en ligne de commande qui permet aux agents IA de réaliser des paiements pour le compte d'un utilisateur, sans jamais exposer ses identifiants bancaires. Chaque dépense reste validée explicitement par l'humain, mais l'agent peut désormais commander, acheter ou souscrire de manière autonome dans les limites approuvées. C'est l'une des premières briques d'infrastructure officielle pour faire des agents des consommateurs économiques, et non plus seulement des copilotes textuels.

## Points clés

- Les agents peuvent dépenser au nom de l'utilisateur via Stripe Link, sans accès aux credentials de paiement.
- Chaque achat doit être approuvé explicitement, ce qui place le human-in-the-loop sur la décision financière, pas sur l'exécution technique.
- Le projet est publié en open source par Stripe sur GitHub, signe d'une volonté d'imposer un standard plutôt qu'un produit fermé.
- Le CLI s'inscrit dans la même mouvance que Cloudflare et Meta cette semaine : déplacer le périmètre des permissions des humains vers les agents.
- Pour les développeurs, cela ouvre la voie à des workflows agentiques avec validation budgétaire scriptée.

## Analyse approfondie

Stripe publie `link-cli`, un outil en ligne de commande ouvert qui s'inscrit dans Stripe Link, le système de paiement unifié de Stripe. Le slogan du repo est sans détour : "Laissez vos agents dépenser pour votre compte. Vos identifiants de paiement ne sont jamais exposés. Vous approuvez chaque achat."

L'idée centrale est de découpler le périmètre d'exécution du périmètre d'autorisation. Concrètement, l'agent peut composer une requête de paiement — choisir un fournisseur, un montant, un produit — mais il ne dispose à aucun moment des numéros de carte ou des secrets bancaires. Au moment de finaliser le paiement, le CLI déclenche un flux d'approbation explicite côté utilisateur. C'est ce dernier qui dit "oui" à la transaction, exactement comme on le ferait pour une carte bancaire 3D-Secure. La différence : la requête a été préparée et exécutée par l'agent, pas par un humain qui clique dans une UI.

Le repo expose un modèle de permissions clair : login via Stripe, instanciation d'une session, plafond optionnel par session, journalisation locale et signature des actions. Pour un développeur, intégrer `link-cli` dans un agent revient à appeler une commande pour lancer une commande d'achat ; l'agent reçoit un statut de paiement et continue sa tâche.

Stripe ne se contente pas de publier un outil de plus : la firme positionne explicitement Link comme la couche standard pour les paiements agentiques. La page de référence montre des exemples où un agent achète des grains de café (Pejman Pour-Moezzi a viralisé un de ces exemples sur X la semaine de la sortie), ou où un agent commande des serveurs dans un cloud — toujours avec la même logique : l'agent fait, l'humain approuve.

L'autre dimension importante du projet, c'est sa coordination avec Stripe Projects et avec Cloudflare. Stripe et Cloudflare ont co-conçu un protocole permettant à un agent d'enchaîner achat de domaine, création de compte cloud, démarrage d'abonnement payant et déploiement, le tout sans copier-coller un seul secret. Le `link-cli` est une des briques de cette chaîne.

Pour les ingénieurs et les leaders tech, l'arrivée de cet outil change deux choses. Premièrement, il cristallise une réalité qu'on voyait monter depuis six mois : les agents ne sont plus seulement consommateurs de tokens, ils deviennent consommateurs de services payants — et donc générateurs de coûts variables qu'il faut budgéter et auditer. Deuxièmement, il pousse à formaliser le pattern d'approbation : qui valide quoi, dans quelles limites, avec quel SLA, et comment on remonte l'historique des décisions d'achat.

À noter : le projet est encore jeune au moment de sa publication. Les contributeurs Stripe annoncent une roadmap autour des plafonds dynamiques, des limites par catégorie de marchand, et de l'intégration avec Stripe Issuing pour générer des cartes virtuelles dédiées aux agents. C'est cette dernière piste qui semble le plus intéresser les premières équipes adoptantes : combiner identité de paiement éphémère et approbation human-in-the-loop ouvre la porte à des workflows e-commerce et procurement entièrement agentiques.

## Pourquoi ça compte

`link-cli` matérialise le passage de l'agent-copilote à l'agent-acheteur. C'est une brique d'infrastructure qu'il faut suivre de près si on travaille sur des agents qui interagissent avec le monde extérieur, parce qu'elle redéfinit le périmètre de confiance et d'audit qu'on doit construire autour d'eux.
