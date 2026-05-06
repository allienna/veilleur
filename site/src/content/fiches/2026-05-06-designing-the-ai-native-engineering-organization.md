---
title: "Designing the AI-native engineering organization"
date: 2026-05-06
url: https://newsletter.getdx.com/p/designing-the-ai-native-engineering
authors: [Abi Noda, Tim Bozarth, Nancy Wang, Taroon Mandhana]
keywords: [engineering management, SDLC, AI-native, org design, validate]
theme: Leadership
tone: opinion
used_in: ["2026-05-06"]
---

## Résumé

Lors de DX Annual, Abi Noda anime une discussion avec Tim Bozarth (CVP CoreAI chez Microsoft), Nancy Wang (CTO de 1Password) et Taroon Mandhana (CTO AI & Teamwork chez Atlassian) sur la façon dont l'IA modifie le design des organisations engineering. La thèse forte : sur les cinq étapes plan / create / validate / deploy / operate, le ratio historique 80% operate / 10-15% create est en train de s'inverser. Plan et validate deviennent majoritaires, parce que c'est là que les humains restent les "tastemakers". Le PRD long disparaît, remplacé par des prototypes mis devant les clients. Mais attention : ajouter du code en amont déplace le bottleneck en aval — le SDLC est un pipe.

## Points clés

- Inversion du ratio temps : create et operate compressent, plan et validate s'étendent
- Ne pas déléguer validate à l'IA pour les systèmes importants
- Ne pas déléguer la sécurité à l'IA pour produire — l'utiliser pour pen testing et red teaming uniquement
- Chez 1Password : fin des PRDs longs, prototypes directement devant les clients
- Le SDLC est un pipe : plus de makers en amont = plus de PRs en aval = plus de code reviews
- Les gains de productivité doivent être pensés au niveau du système entier, pas juste d'une étape

## Analyse approfondie

### Tim Bozarth (Microsoft, CVP CoreAI) : l'inversion plan/create/validate/deploy/operate

> *"If we use a five-stage frame: plan, create, validate, deploy, operate. Create is already changing. AI is incredibly good at writing a line of code. Whether it's good at building complex systems remains to be seen."*

Historiquement, environ 80% du temps engineering va vers operate, 10 à 15% vers create, et le reste se partage entre plan, validate et deploy. Dans les équipes les plus efficaces, ce ratio s'inverse : plan et validate consomment maintenant la majorité du temps, parce que create et operate compressent. Ce sont les étapes où les humains sont les *tastemakers*, où la compréhension du métier compte le plus.

Mais Bozarth est explicite : *don't delegate validate to AI yet*. On a encore besoin d'humains dans la boucle pour les systèmes importants. Et *don't delegate security to AI* : utilisez-la pour le pen testing, utilisez-la pour les red teams, utilisez-la pour battle-harden votre système, mais ne lui faites pas confiance pour livrer des produits sécurisés toute seule.

> *"Roughly 80% of engineering time goes to operate. In the most effective teams, that's inverting: plan and validate now consume the majority of time."*

### Nancy Wang (1Password, CTO) : la fin du PRD long

Chez 1Password, les équipes ne rédigent plus de PRDs complets. Elles construisent des prototypes et les mettent directement devant les clients. Cela a éliminé presque la moitié des allers-retours où l'engineering demandait au produit "comment tu gères ce edge case ?" — la réponse est déjà venue pendant les phases plan et validate.

Mais Wang prévient : il faut penser au SDLC comme un pipe. Ajouter en amont (plus de prototypes, plus de plan) signifie ajouter en aval. Plus de makers écrivant des PRs signifie plus de code reviews, plus de cycles de validation. Si tu ne réponds pas au goulot d'étranglement de la review, tu n'as fait que déplacer le problème.

C'est un point souvent négligé dans les discussions sur l'IA en engineering. La productivité d'une étape isolée n'est pas la productivité du système. Si l'IA permet à un développeur de produire 10 PRs par jour mais que la capacité de review reste à 5 PRs par jour par senior, le résultat est un backlog de PRs en attente, pas un produit qui s'améliore plus vite.

### Taroon Mandhana (Atlassian, CTO AI & Teamwork) : la coordination

Pour Mandhana, le défi est moins technique qu'organisationnel. L'IA permet à des individus d'agir avec plus de leverage, mais cela demande de repenser comment ces individus se coordonnent. Les rituels existants — daily standups, sprint planning, retro — n'ont pas été conçus pour des équipes où chaque membre a un agent IA permanent à ses côtés.

Atlassian expérimente des formats hybrides : des "agent reviews" en plus des "code reviews", où on examine non pas seulement ce qui a été produit, mais comment l'agent a été utilisé, quels patterns ont émergé, ce qui pourrait être réinjecté dans les outils communs.

### Le rôle qui change

Sur la question du métier d'ingénieur, les trois s'accordent : c'est moins de "writing code from scratch" et plus de "shaping decisions". Le code reste central — mais sa production cesse d'être le bottleneck. Ce qui devient critique : la capacité à juger, à arbitrer, à ressentir ce qui est juste pour l'utilisateur, à garder la cohérence du système.

Cela ne veut pas dire moins d'ingénieurs. Cela veut dire des ingénieurs qui passent moins de temps à écrire du boilerplate et plus de temps à concevoir, valider, raffiner. Le titre ne change pas ; le contenu du job, si.

### Coûts et observabilité

Une partie de la discussion porte aussi sur les coûts. Les organisations découvrent que le coût des tokens monte vite quand chaque ingénieur a un agent permanent. Bozarth explique que Microsoft est en train de mettre en place des dashboards de consommation par équipe et par projet — pas pour limiter, mais pour rendre visible. Sans visibilité, pas de décision rationnelle.

L'observabilité des agents devient elle-même un sujet d'engineering : qui appelle quel modèle, sur quel projet, avec quel résultat ? Les outils mûrs (Datadog, OpenTelemetry, Langfuse) commencent à intégrer cette dimension.

## Pourquoi ça compte

Cette discussion entre trois CTOs majeurs offre un cadre opérationnel pour repenser le SDLC à l'ère de l'IA, au-delà des slogans. Les implications sont concrètes : revoir les ratios de temps, ne pas déléguer validate et security, penser le SDLC comme un pipe global, observer la consommation. Lecture clé pour engineering directors et VPs en charge de la transformation IA de leurs équipes.
