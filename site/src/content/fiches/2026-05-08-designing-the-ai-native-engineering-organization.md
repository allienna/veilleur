---
title: "Designing the AI-native engineering organization"
date: 2026-05-08
url: https://link.mail.beehiiv.com/ss/c/u001.yC9eJs5Q3flddlsql05gYZaBcLWTqvnQh8p0MtEOhob4N6nfHxwmSjvtA-RQomq5LyYZCmwHPUAMLl2zNolydMUDHEyIEymRDJqAWrxeVZ2HYY70633Jprt4uSzYUghhPEX9v0HGhhwjjgMkGo0pTAnBVLBuiLpx0Lw8EsX0hO_v_4pOA_H7k_vDRHRPASRG/4qg/VpY8OtY9RyeaPKSahVggoA/h8/h001.Yr_GsuWzOMubyTJ5svEA9SmEm5pSn8wpLuPMjs9zn2k
authors: [Engineering Enablement, Abi Noda, Tim Bozarth, Nancy Wang, Taroon Mandhana]
keywords: [engineering org design, developer productivity, AI-native, leadership, plan-validate]
theme: Leadership
tone: research
used_in: ["2026-05-08"]
---

## Résumé

À la conférence DX Annual, Abi Noda a réuni Tim Bozarth (Microsoft), Nancy Wang (1Password) et Taroon Mandhana (Atlassian) pour discuter de l'impact concret de l'IA sur l'organisation des équipes d'ingénierie. Les CTOs constatent une inversion : historiquement 80% du temps allait à _operate_, désormais _plan_ et _validate_ consomment la majorité du temps des équipes performantes. Le rôle de l'ingénieur évolue vers celui de tastemaker, et les rituels (PRDs, design reviews) se simplifient au profit de prototypes mis directement en face des clients.

## Points clés

- Inversion du temps eng : avant 80% en operate, 10-15% en create ; aujourd'hui plan + validate dominent
- Ne pas déléguer le _validate_ à l'IA pour les systèmes critiques — l'humain reste in the loop
- Ne pas déléguer la sécurité à l'IA : usage défensif (red team, pentest) oui, autonomie pour livrer du code sécurisé non
- 1Password a arrêté les PRDs longs : prototypes directement face client → -50% d'allers-retours produit/eng
- Le rôle du dev devient celui de tastemaker, où le craft et le jugement comptent plus que la vélocité de frappe
- Les fondations d'organisation (qualité, plateforme, standards) déterminent si l'IA crée de la valeur ou du chaos

## Analyse approfondie

Bienvenue dans le dernier numéro de Engineering Enablement, une newsletter hebdomadaire qui partage des recherches et des perspectives sur la productivité des développeurs.

Lors de la session d'ouverture de DX Annual, Abi a animé une discussion avec Tim Bozarth (CVP, CoreAI chez Microsoft), Nancy Wang (CTO, 1Password) et Taroon Mandhana (CTO de l'IA & Teamwork chez Atlassian) pour comprendre comment ils s'adaptent à l'impact que l'IA a maintenant et aura demain. Le panel a couvert des sujets comme le design d'organisation, la gestion des coûts et l'évolution du rôle du développeur.

Voici un extrait légèrement édité de la discussion.

### L'inversion des phases du cycle de développement

**Tim :** Si on prend un cadre en cinq étapes — plan, create, validate, deploy, operate — _create_ change déjà. L'IA est incroyablement bonne pour écrire une ligne de code. Est-ce qu'elle est bonne pour construire des systèmes complexes, ça reste à voir. Historiquement, environ 80% du temps eng allait à _operate_, 10 à 15% à _create_, le reste se répartissant sur _plan_, _validate_ et _deploy_. Dans les équipes les plus performantes, ça s'inverse : _plan_ et _validate_ consomment désormais la majorité du temps, parce que _create_ et _operate_ se compriment. Ce sont les étapes où les humains sont des tastemakers, où la compréhension du craft compte le plus.

> "Roughly 80% of engineering time goes to operate. In the most effective teams, that's inverting: plan and validate now consume the majority of time."

Mais ne déléguez pas _validate_ à l'IA pour l'instant. Les humains doivent rester in the loop pour les systèmes importants. Et ne déléguez pas la sécurité à l'IA. Utilisez-la pour le pen testing, utilisez-la pour les red teams, utilisez-la pour durcir votre système, mais ne lui faites pas confiance pour livrer des produits sécurisés toute seule.

### La fin des PRDs longs

**Nancy :** Chez 1Password, on a arrêté d'écrire des PRDs complets. Les équipes construisent des prototypes et les mettent directement face aux clients. Ça a éliminé presque la moitié des allers-retours où l'engineering demandait au product : "Hey, comment ça doit se comporter dans ce cas ?". Le prototype répond à la question avant qu'elle ne soit posée. Et le client te dit en cinq minutes ce que dix pages de PRD n'auraient pas dit.

C'est un changement culturel énorme. Le PRD n'était pas qu'un document, c'était un rituel — une façon de transférer la responsabilité de la définition du problème vers eng. Sans PRD long, les deux disciplines doivent collaborer en continu, et le prototype devient l'artefact partagé.

### Le craft et le jugement comme nouveaux différenciateurs

**Taroon :** Atlassian a beaucoup investi dans l'agentique interne. Ce qu'on a appris, c'est que la vélocité de frappe n'est plus un goulot d'étranglement. Le goulot, c'est le jugement : qu'est-ce qu'on construit, pour qui, et comment on sait que c'est juste ? Les ingénieurs qui réussissent dans cette nouvelle ère sont ceux qui ont le craft pour repérer une mauvaise abstraction, le sens produit pour challenger une feature, et la rigueur pour valider que ce qui sort est bien ce qu'on voulait.

Cela change le profil de recrutement et la trajectoire de carrière. Un junior qui passe trois ans à taper du code "moyen" n'apprend plus rien que l'IA ne fasse mieux. Mais un junior qui passe trois ans à valider, à challenger, à prototyper, développe les muscles qui comptent.

### Les coûts et la mesure

**Abi :** Et les coûts ? Comment vous gérez ça ?

**Tim :** Nous voyons trois catégories. Les coûts d'inférence directs (les tokens). Les coûts d'infrastructure indirects (les agents qui chargent nos systèmes). Et les coûts d'opportunité (ce que les humains arrêtent de faire). Les deux derniers sont les plus importants et les moins mesurés.

**Nancy :** Chez 1Password, on a un budget par équipe. Pas par ingénieur. Ça responsabilise l'équipe dans son ensemble sur le retour, et ça évite les compétitions stériles.

**Taroon :** Et il faut mesurer la valeur, pas la consommation. Combien de bugs en moins, combien d'incidents en moins, quel time-to-customer. La consommation se game en quinze minutes ; la valeur résiste mieux.

### Les fondations comptent plus que jamais

Le panel converge sur un point central : l'IA est un amplificateur. Si tes fondations (qualité, plateforme, standards de code, observabilité) sont solides, l'IA t'amène un cran plus loin. Si elles sont bancales, l'IA accélère le chaos.

Avant d'investir dans plus d'agents, investissez dans ce qui les rend utiles : des tests fiables, une plateforme avec des contrats clairs, une culture du _why_ documenté.

## Pourquoi ça compte

Pour un Engineering Director, cette table ronde donne un cadre concret de réorganisation : où redéployer le temps libéré par l'IA, comment redéfinir le rôle des ingénieurs, et quels rituels supprimer ou transformer. C'est une feuille de route opérationnelle, pas juste une vision.
