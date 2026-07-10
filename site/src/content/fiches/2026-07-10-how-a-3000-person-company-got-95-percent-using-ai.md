---
title: "How a 3,000-person company got 95% of its employees using AI"
date: 2026-07-10
url: https://lore.link/blog/how-a-3000-person-company-got-95-percent-using-ai
authors: [lore.link, Kaia Colban]
keywords: [skills, adoption, AI platform, workflows, SRE]
theme: Leadership
tone: research
used_in: ["2026-07-10"]
---

## Résumé

Une entreprise de 3 000 personnes a fait passer 95 % de ses employés — pas seulement les ingénieurs — à un usage hebdomadaire de l'IA. Son AI Platform Manager explique comment : un pari massif sur les "skills" (fichiers markdown réutilisables qui apprennent à l'IA à faire un job précis), organisés en trois couches (Core, Team, Playground). Les skills remontent du terrain, la qualité prime sur le volume, et même des équipes non techniques comme la SRE remplacent leurs docs par des skills exécutables.

## Points clés

- Trois couches de skills : Core (tout le monde, par défaut), Team (par département), Playground (expérimentation libre).
- Diffusion bottom-up : le skill le plus utilisé ("Grill Me") vient d'un seul employé, promu via un pipeline automatisé avec une seule validation humaine finale.
- Plus de skills n'est pas l'objectif : plafond utile autour de 55, au-delà ils se marchent dessus ; le pipeline traque doublons et qualité.
- Les skills sont des workflows encodés : la SRE a arrêté d'écrire des docs de troubleshooting pour écrire des skills branchés sur son agent de triage.
- Les non-ingénieurs créent des skills sans toucher à Git, via un skill "create skill" qui branche le repo et câble la CI ; ils en livrent plus que l'équipe eng.
- La mesure des 95 % ne compte pas les logins mais des "sessions actives" (10+ questions de fond, raisonnement, décision réelle), via un wrapper interne qui émet des métriques.

## Analyse approfondie

Une entreprise de 3 000 personnes a fait passer 95 % de ses employés à un usage hebdomadaire de l'IA. Pas 95 % des ingénieurs. Tout le monde : ventes, marketing, ops, support. Nous avons parlé à leur AI Platform Manager la semaine dernière pour comprendre comment ils y sont parvenus. Ils ont massivement parié sur les skills (des fichiers markdown réutilisables qui apprennent à l'IA à faire un job précis) et ont bâti tout leur système autour d'eux. Mais on ne peut pas donner tous les skills à tout le monde, car cela conduit les skills à s'annuler entre eux et à sauter le bon skill. Ils ont donc réparti qui reçoit quoi en trois couches :

1. **Core** : tout le monde les a par défaut. Slack, GitHub, notes. Un nouvel arrivant les a déjà.
2. **Team** : assignés par département. Les ventes ont les skills ventes, le marketing les skills marketing.
3. **Playground** : un endroit unique où chacun peut construire et expérimenter ce qu'il veut.

Voici comment ça tourne, et ce qui vaut la peine d'être copié :

1. **Les skills se diffusent de bas en haut.** Leur skill le plus utilisé, "Grill Me" (il interroge vos exigences avant que vous ne construisiez), vient d'un seul employé. Il a atterri dans le playground, l'usage a grimpé, un pipeline automatisé l'a repéré, et il a été promu officiel. Il y a une seule porte de validation humaine à la fin, mais personne ne décide de manière centralisée ce qui est bon.
2. **Plus de skills n'est pas l'objectif.** Il en fait tourner environ 100 mais pense que le plafond utile est plus proche de 55. Au-delà, ils commencent à entrer en collision et à se dupliquer ; le pipeline traque donc activement les recouvrements et la qualité. Il a vu trois skills "Google Docs" différents, dont aucun ne faisait bien le travail. Qualité et couverture priment sur le volume.
3. **Les skills ne sont pas de simples connecteurs d'outils, ce sont des workflows encodés.** L'exemple le plus parlant est leur équipe SRE, qui a arrêté d'écrire des docs de troubleshooting pour écrire des skills à la place. Leur règle : si vous voulez qu'ils supportent votre système, vous uploadez un skill, car c'est ce que fait tourner leur agent de triage. Une doc reste là à attendre d'être lue ; un skill se branche directement sur l'agent de triage qui agit quand quelque chose casse.
4. **Les non-ingénieurs créent des skills sans jamais toucher à Git.** Il y a un skill "create skill" qu'ils invoquent : il crée une branche du repo, câble la CI, et livre. Résultat, les non-ingénieurs livrent désormais plus de skills que l'équipe d'ingénierie.
5. **Ils ont tué leur propre outillage.** Ils construisaient auparavant des agents de revue de code avec LangChain et LangGraph, puis ont tout arraché. La revue n'est plus qu'un skill branché sur une GitHub Action.

En entendant tout cela, j'étais impressionné par le système, mais je me demandais s'il était réellement utilisé. C'est là qu'il m'a dit : "95 % des employés sont sur l'IA chaque semaine", et que tout ce qui précède est ce qui les y a menés. Incrédule, j'ai demandé comment ils calculaient ces 95 %, supposant que la plupart des gens utilisaient juste l'IA pour trouver où déjeuner. Il s'avère qu'ils ont toute une méthode. Au lieu de compter les connexions, ils comptent les "sessions actives", qui doivent comporter 10 questions de fond ou plus, un vrai raisonnement, et une décision réelle. J'ai insisté sur la façon dont ils sauraient qu'une session franchit ce seuil. Il a expliqué :

> Nous avons construit un wrapper interne qui auto-configure le modèle, la télémétrie et les skills par défaut, de sorte que chaque session émet des métriques sans que personne n'ait à opter pour.

Il a fallu six mois à son équipe de 12 ingénieurs pour construire ce système, et il dit qu'il manque encore beaucoup de choses. Il a mis en avant trois éléments qu'il aimerait avoir mais n'a pas :

1. **La couverture, pas seulement l'usage.** Ses métriques lui disent qu'un skill s'est déclenché dans 50 % des sessions ou dans moins de 1 %. Elles ne lui disent pas quelle part du job réel de quelqu'un est couverte par des skills, ni où un skill devrait exister et n'existe pas.
2. **La détection proactive des manques.** Tout est bottom-up. Les skills ne sont construits que lorsqu'une personne motivée décide d'en construire un. Il était direct : "si personne ne le crée, c'est probablement que les gens n'en voient pas le besoin." Les manques restent donc là, invisibles.
3. **La visibilité à l'échelle de l'organisation.** Il gère la plateforme mais ne sait pas réellement à quel point les équipes SRE ou support sont couvertes. Personne n'a la vue top-down.

*(L'article se conclut par l'annonce de Lore, un produit visant à fournir ce système sans les six mois de développement, à la recherche de design partners.)*

## Pourquoi ça compte

C'est un cas concret et chiffré d'adoption de l'IA à l'échelle de toute une entreprise, pas seulement de la tech. Il montre que le vrai levier n'est pas le modèle mais l'organisation du savoir en skills réutilisables, et que la compétence d'équipe de demain sera d'encoder ses workflows plutôt que de les documenter.
