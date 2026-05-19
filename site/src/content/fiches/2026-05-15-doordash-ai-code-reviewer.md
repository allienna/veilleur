---
title: "How DoorDash built an AI code reviewer engineers actually listen to"
date: 2026-05-15
url: https://careersatdoordash.com/blog/how-doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/
authors: [careersatdoordash.com, Adam Yarger, Adam Rogal]
keywords: [code review, AI agent, pull request, attention, production]
theme: IA
tone: research
used_in: ["2026-05-15"]
---

## Résumé

DoorDash a déployé un agent de revue de code en production qui inspecte plus de 10 000 PR par semaine sur 56 dépôts (Go, iOS, Android, web, infra, data). Le défi central n'est pas la détection mais l'attention : aider l'agent à se concentrer sur ce qui mérite d'être commenté et à se taire ailleurs. Résultat : 60,2 % des findings critiques font modifier le code avant le merge, contre 46 % avec leur précédent outil tiers, pour environ 3 dollars par review.

## Points clés

- L'agent tourne automatiquement sur les PR et poste ses commentaires environ 7 minutes après l'ouverture, souvent avant le premier reviewer humain
- La métrique cible n'est pas "trouve-t-il des bugs" mais "le dev modifie-t-il son code suite à ses commentaires"
- Le système actuel est une v3, après deux itérations majeures qui ont chacune révélé des angles morts
- Le coût (~3 $/review) est largement inférieur aux outils concurrents (5 à 20 $/review)
- L'acceptation reste homogène à travers les stacks : Go, iOS, frontend web, infra
- Le filtre clé : ne commenter que si la remarque est spécifique, fondée et probablement utile à l'auteur

## Analyse approfondie

### Le problème

Beaucoup d'organisations d'ingénierie ont essayé d'ajouter des reviewers IA sur leurs pull requests. Trop souvent, ces reviewers sont ignorés : les commentaires sont bruyants, les suggestions génériques, et les ingénieurs apprennent à scroller au-dessus d'eux.

L'équipe DoorDash a voulu autre chose. Sur les derniers mois, elle a déployé un agent de revue de code sur l'ensemble de son organisation d'ingénierie. Le défi central s'est révélé être l'attention : aider l'agent à se concentrer sur les parties d'un changement qui méritent une revue, et rester silencieux quand il n'a rien d'utile à apporter.

La barre qu'ils se sont fixée n'était pas "trouve-t-il des choses" mais :
- Les ingénieurs changent-ils réellement leur code quand l'agent commente ?
- L'agent préserve-t-il assez de confiance pour que les équipes le gardent activé ?

### Les chiffres

Dans une semaine type, l'agent revoit plus de 10 000 PR sur 56 dépôts onboardés : services backend Go, apps iOS et Android, frontends web, infrastructure, pipelines data. Beaucoup de reviews se déclenchent automatiquement à l'ouverture d'une PR ; les ingénieurs n'ont pas à les demander. L'agent tourne sur les mêmes PR que les humains, souvent avant qu'un humain ait regardé le diff.

Les mesures clés :
- **60,2 % des findings high et critical settled mènent l'ingénieur à modifier son code avant le merge** (n=2 256), contre **46 % d'acceptation** avec leur précédent outil tiers
- **Les findings déclenchés par webhook sont acceptés à 59 %** — donc même hors invocations manuelles cherry-pickées
- **Une review coûte environ 3 $ en moyenne**, contre 5 à 20 $ pour des produits agentic comparables
- **L'agent poste ses findings ~7 minutes après l'ouverture de la PR**, généralement avant le premier reviewer humain

Ces chiffres tiennent à travers des codebases très différents. L'acceptation sur un repo backend Go ressemble à celle sur iOS ou web. L'agent n'est pas optimisé pour un stack ; il est optimisé pour un équilibre : attraper les problèmes critiques sans spammer l'auteur.

### L'évolution du système

Le système actuel est la v3.

**v1 : un éventail d'agents spécialistes** (sécurité, tests, perf, qualité). Bon pour les bugs mécaniques (nil checks manquants, erreurs non gérées, gaps de tests) mais aveugle aux problèmes d'architecture — un refactor qui change un contrat, une nouvelle abstraction qui ne colle pas, une suppression qui casse un autre repo. Les spécialistes ne voient pas la big picture parce qu'aucun ne la regarde.

**v2 : deux reviewers généralistes en parallèle**, chacun voyant tout le changement. Meilleurs sur les questions cross-boundary, mais chacun avait trop à faire — d'où du bruit et des suggestions plates.

**v3 (actuelle)** combine les deux approches en réintroduisant la spécialisation mais à un niveau différent, et en apprenant à se taire activement.

### Pourquoi ça marche

Le filtre clé est qu'un commentaire n'est posté que si la remarque est spécifique, ancrée dans le code et probablement utile à l'auteur. La discipline du silence est ce qui préserve la confiance — et donc la métrique d'acceptation, qui à son tour préserve l'usage de l'outil.

## Pourquoi ça compte

C'est l'un des rares retours d'expérience chiffrés sur un agent IA à l'échelle de la production. DoorDash montre que le succès se mesure en confiance maintenue dans le temps, pas en taux de détection brut — un cadre transposable à tous les agents qui s'intègrent dans un workflow humain.
