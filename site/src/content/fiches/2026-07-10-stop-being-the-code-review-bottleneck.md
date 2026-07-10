---
title: "Stop being the code review bottleneck"
date: 2026-07-10
url: https://newsletter.posthog.com/p/code-review-tips
authors: [newsletter.posthog.com]
keywords: [code review, agents, workflow, automation, pipeline]
theme: IA
tone: tutorial
used_in: ["2026-07-10"]
---

## Résumé

Les agents écrivent du code plus vite que n'importe quel humain ne peut le relire. La réponse naïve serait de reviewer plus vite ; la bonne réponse est de reviewer le moins possible soi-même, en sortant de la boucle et en déléguant la relecture à d'autres agents. PostHog partage quatre changements de workflow concrets, dont la règle d'or : l'agent qui a écrit le code ne peut pas être celui qui le relit, car il est aveugle à ses propres angles morts.

## Points clés

- Les agents produisent du code plus vite que les humains ne le relisent : si vous êtes dans chaque revue, vous êtes le goulot d'étranglement.
- Solution : construire un pipeline qui délègue la relecture à des agents et ne remonte à un humain que ce qui l'exige vraiment.
- L'agent qui écrit ne peut pas s'auto-relire ; mieux vaut plusieurs reviewers avec des instructions, des objectifs, des modèles et des fournisseurs différents.
- Exemple concret : le système `qa-swarm` de Paul D'Ambra lance quatre agents reviewers spécialisés (qa-team, security-audit, paul-reviewer, xp-reviewer), puis un `review-triage` classe les retours en actionable / nits / ambiguous.
- Ces systèmes coûtent cher en tokens (~60 % du budget d'un ingénieur), mais réduisent la fatigue de context switching en automatisant le "babysitting" de PR.

## Analyse approfondie

Les agents écrivent du code plus vite que n'importe quel humain ne peut le relire.

La solution naïve serait que les développeurs relisent le code plus vite. Le point de vue "500 de QI" est que les développeurs relisent le moins de code possible.

Si vous devez être impliqué dans chaque revue de code, vous serez toujours le goulot d'étranglement. À la place, sortez-vous de la boucle de revue en construisant un pipeline qui délègue les tâches à des agents.

Nous avons demandé aux ingénieurs de PostHog comment ils relisent le code généré par l'IA pour continuer à livrer vite sans perdre en qualité. Voici quatre changements de workflow que vous pouvez leur voler (prompts inclus) pour vous simplifier la vie.

La première chose à ajouter, si ce n'est pas déjà fait, c'est un moyen pour les agents de relire le code à votre place. L'objectif est de décharger les revues les plus simples sur les agents, et de signaler ce qui a réellement besoin d'un humain.

Le point crucial : l'agent qui a écrit le code ne peut pas être celui qui le relit. Les agents sont mauvais pour vérifier leur propre travail, car ils ignorent souvent leurs propres angles morts. Pour la même raison, il vaut mieux avoir plusieurs agents avec des instructions et des objectifs différents pour couvrir davantage de failles, ainsi que des modèles et des fournisseurs différents pour les différents reviewers.

Voici comment l'un de nos ingénieurs, Paul D'Ambra, fait fonctionner son propre système de revue par agents :

1. D'abord, **qa-swarm** lance quatre agents reviewers, chacun avec ses instructions spéciales :
   - **qa-team** — lance des sous-agents techniques qui traquent la sécurité, la base de données, la performance, etc.
   - **security-audit** — sonde les vulnérabilités comme les injections SQL ou de prompt.
   - **paul-reviewer** — utilise la "voix" de Paul et se concentre sur l'observabilité, les déploiements, le nommage.
   - **xp-reviewer** — applique une grille de lecture Extreme Programming.
2. Ensuite, **review-triage** trie ces revues pour classer les fils de discussion en trois catégories :
   - **actionable** → corrigé et poussé.
   - **nits** → résolus, avec une réponse en commentaire.
   - **ambiguous** → remonté et mis de côté pour que Paul le traite avec l'agent plus tard.
3. Une boucle externe itère jusqu'à trois fois, ou jusqu'à ce qu'aucun nouveau fil "actionable" n'apparaisse.

À partir de là, vous pouvez connecter cela à une autre boucle qui pilote la PR jusqu'à ce qu'elle soit prête à merger.

**Le takeaway** : gagnez du temps de relecture en faisant se relire les agents entre eux. Cela élimine les revues faciles pour que seules les PR qui ont vraiment besoin d'attention humaine soient signalées.

Cela dit, ces systèmes peuvent devenir coûteux en tokens : *"Environ 60 % de ma dépense en tokens part dans l'automatisation de la corvée de CI et de revue, et je ne regrette pas un seul dollar"* — Paul. Si faire tourner plusieurs agents ou boucles n'est pas envisageable pour votre équipe, cherchez des designs mono-agent.

Le context switching qui accompagne le codage agentique est épuisant. Un moyen simple de réduire cette fatigue est d'automatiser les tâches adjacentes à la revue qui ne demandent pas votre attention. Par exemple, "babysitter" une seule PR peut impliquer des tâches fastidieuses : surveiller la CI, relancer des tests flaky, vérifier les notifications de commentaires, garder la branche à jour. Pourquoi gaspiller votre ressource la plus précieuse — votre énergie — quand vous pouvez tout déléguer à une boucle ?

**Le takeaway** : réduisez le context switching et la fatigue en déléguant les tâches simples comme le babysitting de PR à une boucle.

Enfin, les équipes qui bougent vite génèrent beaucoup de petites PR à faible risque, et chacune a quand même besoin d'une approbation sur GitHub (un "stamp"). PostHog gérait cela dans Slack, via un canal #dev-stamp-exchange où l'on dépose sa PR en attendant que quelqu'un l'approuve — un processus lui aussi automatisable.

## Pourquoi ça compte

Quand les agents deviennent asynchrones et produisent en continu, le goulot d'étranglement humain ne disparaît pas : il se déplace de l'écriture vers la revue. Cette fiche donne un patron concret — des essaims de reviewers spécialisés — pour industrialiser cette relecture sans y noyer ses ingénieurs.
