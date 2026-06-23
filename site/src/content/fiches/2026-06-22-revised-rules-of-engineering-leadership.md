---
title: "Revised rules of engineering leadership."
date: 2026-06-22
url: https://leadershipintech.com/links/22601/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Will Larson]
keywords: [leadership, harness, migrations, agents, jugement]
theme: Leadership
tone: opinion
used_in: ["2026-06-22"]
---

## Résumé

Will Larson révise ses règles de leadership technique à l'aune du tournant des agents IA. Sa thèse centrale : si le code de première passe est désormais quasi gratuit, le coût du code *qui fonctionne* dépend toujours du harnais de développement (tests, CI/CD, environnements de validation), et lui n'est pas gratuit. Les migrations complexes peuvent maintenant être détenues à 95 % par un individu, ce qui décuple l'impact du jugement individuel. La conclusion rassurante : les leviers qui accéléraient l'ingénierie il y a deux ans restent les plus efficaces aujourd'hui.

## Points clés

- Une migration complexe peut être détenue à 95 % par un seul individu, en 10 % du temps : l'impact du jugement individuel n'a jamais été aussi élevé.
- Le code de première passe est quasi gratuit, mais le code qui marche dépend du harnais de développement.
- Optimiser le cas de base des processus pour les agents : la plupart des étapes peuvent être automatisées avec les bons harnais, contrôles, contexte et jugement.
- Les sources de mauvaise qualité (petits sharp edges) brisent les modèles mentaux des collègues qui co-maintiennent le code.
- Les pratiques qui accéléraient l'ingénierie il y a deux ans restent les plus précieuses aujourd'hui.

## Analyse approfondie

De début 2014 à fin 2020, j'ai travaillé dans des environnements en hypercroissance, qui sont exigeants mais aussi formateurs. La caractéristique la plus précieuse de l'hypercroissance est que vos erreurs se révèlent le mois suivant plutôt que l'année suivante, parce que les choses tournent mal très bruyamment quand vous bougez vite. Je repense beaucoup à l'hypercroissance ces derniers temps, parce que le business d'Imprint grandit rapidement et que nous avons beaucoup recruté l'an dernier, mais aussi parce que le virage de l'outillage IA a changé le rythme auquel il est possible de travailler.

Ce billet documente les nouvelles règles autour desquelles j'ai révisé mon approche du leadership technique, puis détaille les projets concrets de l'année écoulée qui m'ont amené à y croire.

### Règles révisées

1. **Les migrations peuvent être faites par un individu plutôt que par une équipe.** Même les changements complexes et de grande ampleur peuvent être détenus à 95 % par l'individu ou l'équipe qui les pilote, et réalisés en 10 % du temps. À mesure que le coût initial des migrations baisse, la récompense/pénalité liée à la qualité de chaque migration augmente : même de petits sharp edges briseront les modèles mentaux de vos collègues sur le logiciel que vous co-maintenez. L'impact du jugement individuel sur votre entreprise n'a jamais été aussi élevé.

2. **Si le code de première passe est quasi gratuit, le coût du code qui fonctionne dépend de votre harnais de développement, et lui n'est pas gratuit.** Nous sommes à une époque où beaucoup d'entreprises disent que *tout le monde* devrait écrire du code ; or notre expérience montre qu'écrire du code qui fonctionne bien, tout en évitant les cas limites pénibles, reste difficile. À quel point c'est difficile reste fonction de votre harnais de développement : tests, CI/CD, environnements de validation, capacité à prévisualiser les changements, etc. Personnellement, je n'imagine pas qu'il soit utile que la plupart des gens d'une entreprise contribuent du code, mais je soupçonne que la plupart des désaccords sur ce sujet relèvent en fait d'un malentendu : même dans une entreprise où « tout le monde code », l'équipe marketing ne réduit pas les allocations sur vos serveurs ; il s'agit plutôt de savoir s'il existe une frontière sûre où elle *peut* participer (comme un produit SaaS qui permet la personnalisation par l'écriture de logiciel).

La bonne nouvelle, c'est que cela signifie que les choses les plus précieuses pour accélérer l'ingénierie il y a deux ans sont toujours les choses les plus précieuses pour l'accélérer aujourd'hui.

3. **Optimiser le cas de base des processus pour les agents.** La plupart des étapes de la plupart des processus peuvent être entièrement automatisées dans la plupart des cas. Avec les bons harnais, les bons contrôles, le contexte métier et un bon jugement de la part de leurs concepteurs, vous pouvez automatiser entièrement le cas de base de la plupart des processus dans les entreprises tech modernes. Par exemple, le cas de base de la revue de code par un humain est plus lent et moins efficace qu'une première passe automatisée bien conçue.

## Pourquoi ça compte

Larson apporte la contrepartie pragmatique et opérationnelle au cadre conceptuel d'Ajey Gore : oui le code devient gratuit, mais le harnais (tests, CI/CD, validation) est ce qui rend ce code fiable — et c'est là que les leaders doivent investir.
