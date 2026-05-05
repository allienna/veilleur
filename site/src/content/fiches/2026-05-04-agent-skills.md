---
title: "Agent Skills"
date: 2026-05-04
url: https://addyosmani.com/blog/agent-skills/?utm_source=tldrnewsletter
authors: [Addy Osmani]
keywords: [agent skills, sdlc, claude code, workflows, senior engineering]
theme: IA
tone: opinion
used_in: ["2026-05-04"]
---

## Résumé

Addy Osmani décrit Agent Skills comme la tentative de remettre dans le quotidien des agents de code IA tout ce qui fait le travail d'un dev senior et qui n'apparaît pas dans le diff : specs, tests, reviews, discipline du scope. Il oppose deux approches : la prose comme contexte (essais sur les bonnes pratiques que l'agent ignore) et le workflow (étapes avec critères de sortie que l'agent doit suivre). Le projet open source qu'il décrit a déjà passé les 26K stars sur GitHub, signe que la friction est largement partagée. L'article cartographie chaque choix de design d'Agent Skills sur les pratiques SDLC standard et les guides d'ingénierie publiés par Google.

## Points clés

- Le comportement par défaut d'un agent de code est de prendre le chemin le plus court vers "done", sans spec, sans test préalable, sans considérer le reviewer
- Un Skill n'est pas de la doc : c'est un workflow avec des étapes, des checkpoints qui produisent des preuves, et un critère de sortie défini
- "Process over prose. Workflows over reference. Steps with exit criteria over essays without them."
- Les Skills sont des fragments markdown avec frontmatter, injectés dans le contexte de l'agent quand la situation le réclame
- Si tu mets un essai de 2 000 mots sur les bonnes pratiques de test, l'agent génère du texte plausible et saute le test ; si tu mets un workflow (écrire le test qui échoue, le voir échouer, écrire le code minimum, le voir passer, refactorer), l'agent a quelque chose à faire et tu as quelque chose à vérifier
- Le travail "invisible" (surfacing assumptions, spec, chunks reviewables, design ennuyeux, preuves de correction, taille reviewable) est ce qui sépare les ingénieurs qui shippent du logiciel fiable de ceux qui pushent du code qui casse

## Analyse approfondie

*Le travail d'un ingénieur senior, c'est essentiellement les parties qui n'apparaissent pas dans le diff. Specs. Tests. Reviews. Discipline du scope. Refus de shipper ce qui ne peut pas être vérifié. Les agents de code IA sautent ces parties par défaut. Agent Skills est ma tentative de les rendre non optionnelles.*

Le comportement par défaut de n'importe quel agent de code IA, c'est de prendre le chemin le plus court vers "done". On lui demande une feature, il écrit la feature. Il ne demande pas si tu as une spec, n'écrit pas de test avant l'implémentation, ne se demande pas si le changement traverse une frontière de confiance, ne vérifie pas à quoi ressemblera la PR pour un reviewer. Il produit du code, déclare la victoire, et passe à autre chose.

C'est exactement le mode d'échec que tous les ingénieurs seniors ont passé leur carrière à apprendre à éviter. La version senior de n'importe quelle tâche inclut du travail qui n'apparaît pas dans le diff : faire émerger les hypothèses, écrire la spec, découper le travail en chunks reviewables, choisir le design ennuyeux, laisser des preuves que le résultat est correct, dimensionner le changement pour qu'un humain puisse vraiment le reviewer. Ces étapes sont la majeure partie de ce qui sépare les ingénieurs qui shippent du logiciel fiable à grande échelle de ceux qui pushent du code qui casse.

Les agents sautent ces étapes pour la même raison qu'un junior le ferait. Elles sont invisibles. Le signal de récompense pointe sur "tâche terminée" et pas sur "tâche terminée et le design doc existe". Donc on doit reboulonner le scaffolding senior par-dessus.

Agent Skills est ma tentative de ce scaffolding. Le projet vient de passer les 26K stars, donc apparemment je ne suis pas le seul à le vouloir. Ce post, c'est la partie que le README ne couvre pas vraiment : pourquoi chaque choix de design existe, comment il s'inscrit dans le SDLC standard et les pratiques d'ingénierie publiées par Google, et ce qu'il faut piquer du projet même si tu n'installes jamais un seul Skill.

### Ce qu'est vraiment un "Skill"

Le mot "skill" travaille beaucoup dans le vocabulaire Claude Code / Anthropic, et ça aide d'être précis. Un Skill, c'est un fichier markdown avec frontmatter qui est injecté dans le contexte de l'agent quand la situation le réclame. Quelque part entre un fragment de system prompt et un runbook.

Un Skill, ce n'est *pas* de la doc de référence. Ce n'est pas "tout ce que tu devrais savoir sur les tests". C'est un workflow : une séquence d'étapes que l'agent suit, avec des checkpoints qui produisent des preuves, se terminant par un critère de sortie défini.

Cette distinction, c'est tout le jeu. Si tu mets un essai de 2 000 mots sur les bonnes pratiques de test dans le contexte de l'agent, l'agent le lit, génère du texte plausible, et saute le vrai test. Si tu mets un *workflow* (écrire le test qui échoue d'abord, le lancer, le voir échouer, écrire le minimum de code pour qu'il passe, le voir passer, refactorer), l'agent a quelque chose à faire, et tu as quelque chose à vérifier.

**Process over prose. Workflows over reference. Steps with exit criteria over essays without them.** Cette seule distinction sépare un Skill utile d'un fragment de prompt anémique.

## Pourquoi ça compte

Agent Skills marque le passage d'une approche "donne-lui du contexte et prie" à une approche "donne-lui un workflow vérifiable". C'est le retour de la discipline d'ingénierie dans un monde où on était en train de la perdre dans la précipitation à déléguer aux agents.
