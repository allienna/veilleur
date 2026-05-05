---
title: "Agents can now create Cloudflare accounts, buy domains, and deploy"
date: 2026-04-30
url: https://blog.cloudflare.com/agents-stripe-projects/
authors: [Cloudflare]
keywords: [agents, cloudflare, stripe-projects, domains, deploy, oauth]
theme: IA
tone: news
used_in: ["2026-04-30"]
---

## Résumé

Cloudflare et Stripe annoncent le 30 avril 2026 un nouveau protocole co-conçu permettant aux agents IA de provisionner Cloudflare au nom de leurs utilisateurs : création de compte, démarrage d'un abonnement payant, achat d'un domaine et récupération d'un token API. L'humain n'est sollicité que pour autoriser via OAuth et accepter les CGU. Le reste — du compte vide jusqu'au déploiement en prod — peut s'enchaîner en une seule commande.

## Points clés

- Un agent peut désormais créer un compte Cloudflare, démarrer une souscription payante, acheter un domaine et obtenir un token API sans qu'un humain copie un seul secret.
- Le protocole est co-conçu avec Stripe dans le cadre du lancement de Stripe Projects.
- L'humain reste dans la boucle pour accorder les permissions OAuth et accepter les CGU, mais aucune autre étape humaine n'est nécessaire.
- Cloudflare offre 100 000 $ de crédits aux startups qui s'incorporent via Stripe Atlas, signe d'un alignement go-to-market fort entre les deux acteurs.
- Le protocole est ouvert à toute plateforme avec des utilisateurs authentifiés, pas réservé à Stripe.

## Analyse approfondie

Le constat de départ est simple : les coding agents savent construire du logiciel, mais pour le déployer en production, il leur faut trois choses du cloud cible — un compte, un moyen de paiement, un token API. Jusqu'ici, c'étaient des tâches que les humains géraient à la main. De plus en plus, les agents les gèrent au nom de l'utilisateur. L'agent doit pouvoir faire ce qu'un client humain peut faire : il reçoit un objectif de haut niveau et choisit d'utiliser Cloudflare et d'appeler les APIs Cloudflare.

À partir d'aujourd'hui, les agents peuvent provisionner Cloudflare au nom de leurs utilisateurs. Ils peuvent créer un compte Cloudflare, démarrer un abonnement payant, enregistrer un domaine et récupérer un token API pour déployer du code immédiatement. Les humains peuvent rester dans la boucle pour accorder la permission et doivent accepter les CGU de Cloudflare, mais aucune autre étape humaine n'est requise du début à la fin. Pas besoin d'aller sur le dashboard, de copier-coller des tokens API, ou de saisir des numéros de carte. Sans aucun setup additionnel, les agents disposent de tout ce qu'il faut pour déployer une nouvelle application en production en un seul coup. Et avec le serveur MCP "Code Mode" de Cloudflare et les Agent Skills, ils sont encore meilleurs à l'exercice.

Tout cela fonctionne via un nouveau protocole co-conçu avec Stripe dans le cadre du lancement de Stripe Projects. Cloudflare annonce aussi son partenariat avec Stripe et propose 100 000 $ de crédits Cloudflare à toutes les nouvelles startups qui s'incorporent via Stripe Atlas. Mais ce nouveau protocole permet aussi à toute plateforme avec des utilisateurs authentifiés d'intégrer Cloudflare de la même façon que Stripe le fait, avec zéro friction pour l'utilisateur final.

### Comment ça marche : zéro à la prod sans setup ni étape manuelle

L'utilisateur installe le Stripe CLI avec le plugin Stripe Projects, se connecte à Stripe, et démarre un nouveau projet :

```
stripe projects init
```

Il prompte ensuite son agent pour qu'il construise quelque chose de neuf et le déploie sur un nouveau domaine. Si l'email avec lequel l'utilisateur est connecté à Stripe a déjà un compte Cloudflare, il sera invité à autoriser l'agent via un flux OAuth classique. Sinon, Cloudflare provisionne automatiquement un compte pour l'utilisateur et son agent.

L'agent dispose alors d'un token API scopé, peut acheter un domaine au prix coûtant via Cloudflare Registrar, configurer les DNS, déployer un Worker ou des Pages, et provisionner les services associés (KV, R2, D1) — sans repasser par l'utilisateur sauf pour les étapes de validation explicite.

Côté gouvernance, le protocole repose sur OAuth standard, des scopes explicites, et un audit log qui trace chaque action de l'agent. L'utilisateur peut révoquer l'accès à tout moment. Le ToS de Cloudflare est accepté par l'humain, mais c'est l'agent qui exécute. C'est exactement le découplage que pose `link-cli` côté paiement, transposé côté infrastructure cloud.

L'autre point intéressant : Cloudflare insiste sur le fait que ce protocole est ouvert. N'importe quelle plateforme avec des utilisateurs authentifiés peut s'y intégrer comme Stripe le fait. Autrement dit, ce n'est pas un deal exclusif Stripe-Cloudflare, c'est un standard que les deux acteurs cherchent à diffuser. Pour un CTO qui réfléchit à sa stratégie agentique, c'est un signal fort sur la direction que prend la couche d'orchestration.

### Implications pour les startups

L'offre des 100 000 $ de crédits via Stripe Atlas est un cheval de Troie efficace : une nouvelle startup qui s'incorpore via Stripe Atlas se retrouve avec un compte Cloudflare provisionné, un domaine acheté, un token API en main, et une stack agentique prête à déployer. Pas besoin de passer une journée à configurer DNS, billing, et CI/CD — l'agent fait tout.

Pour les boîtes plus grandes, l'enjeu sera plutôt de comprendre comment intégrer ces protocoles à leur SSO existant et à leurs politiques d'achat. Mais le mouvement est clair : la phase "agents qui peuvent ouvrir des comptes" est lancée, et les politiques internes vont devoir suivre.

## Pourquoi ça compte

L'annonce Cloudflare-Stripe matérialise le passage à l'échelle des agents en production : ils peuvent désormais provisionner toute l'infrastructure dont ils ont besoin sans intervention humaine technique. C'est un changement de périmètre de confiance qui va forcer les organisations à repenser leurs politiques d'achat, d'audit et d'identité.
