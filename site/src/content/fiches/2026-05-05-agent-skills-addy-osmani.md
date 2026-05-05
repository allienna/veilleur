---
title: "Agent Skills"
date: 2026-05-05
url: https://addyosmani.com/blog/agent-skills/?utm_source=tldrdev
authors: [Addy Osmani]
keywords: [agent skills, Claude Code, senior engineering, SDLC, scaffolding]
theme: IA
tone: opinion
used_in: ["2026-05-05"]
---

## Résumé

Addy Osmani décrit le mode d'échec par défaut des agents de coding : prendre le chemin le plus court vers "done", sans spec, sans test préalable, sans prise en compte des trust boundaries. C'est le même mode d'échec qu'un ingénieur senior passe sa carrière à éviter. Son projet open source Agent Skills (26K stars) est une tentative de remettre par-dessus l'agent l'échafaudage de l'ingénierie senior, sous forme de skills — des workflows markdown injectés dans le contexte avec des checkpoints qui produisent des preuves.

## Points clés

- Le comportement par défaut d'un agent : produire du code, déclarer victoire, passer à autre chose.
- Le travail d'un senior, c'est ce qui ne se voit pas dans le diff : specs, tests, scope, design ennuyeux, preuves.
- Les agents skip ces étapes pour la même raison qu'un junior : elles sont invisibles, et le signal de récompense pointe sur "task complete".
- Une "skill" = fichier markdown + frontmatter, injecté dans le contexte selon la situation.
- Une skill n'est pas de la doc de référence, c'est un workflow avec checkpoints et critère de sortie.
- Le projet a déjà 26 000 étoiles GitHub.

## Analyse approfondie

*Le travail d'un ingénieur senior, c'est surtout les morceaux qui n'apparaissent pas dans le diff. Les specs. Les tests. Les revues. La discipline du scope. Refuser de livrer ce qui ne peut pas être vérifié. Les agents de coding IA sautent ces parties par défaut. Agent Skills est ma tentative pour les rendre non optionnelles.*

Le comportement par défaut de tout agent de coding IA, c'est de prendre le chemin le plus court vers "done". Demande-lui une feature et il écrit la feature. Il ne demande pas si tu as une spec, il n'écrit pas un test avant l'implémentation, il ne se demande pas si le changement traverse une trust boundary, il ne vérifie pas à quoi va ressembler la PR pour un reviewer. Il produit du code, déclare victoire, passe à autre chose.

C'est exactement le mode d'échec que tout ingénieur senior a passé sa carrière à apprendre à éviter. La version senior de n'importe quelle tâche inclut du travail qui n'apparaît pas dans le diff : faire émerger les hypothèses, écrire la spec, découper le travail en morceaux reviewables, choisir le design ennuyeux, laisser des preuves que le résultat est correct, dimensionner le changement pour qu'un humain puisse réellement le reviewer. Ces étapes, c'est l'essentiel de ce qui sépare les ingénieurs qui livrent du logiciel fiable à grande échelle de ceux qui pushent du code qui casse.

Les agents sautent ces étapes pour la même raison qu'un junior. Elles sont invisibles. Le signal de récompense pointe sur "task complete", pas sur "task complete et le design doc existe". Donc il faut reboulonner par-dessus l'échafaudage senior-engineer.

Agent Skills est ma tentative de cet échafaudage. Le projet vient de dépasser 26 000 étoiles, donc apparemment je ne suis pas le seul à le vouloir. Ce post couvre ce que le README ne dit pas tout à fait : pourquoi chaque choix de design existe, comment il s'aligne sur le SDLC standard et les pratiques d'ingénierie publiées par Google, et ce que tu devrais voler au projet même si tu n'installes jamais une seule skill.

### Ce qu'est vraiment une "skill"

Le mot "skill" fait beaucoup de travail dans le vocabulaire Claude Code / Anthropic, et il est utile d'être précis. Une skill est un fichier markdown avec frontmatter qui est injecté dans le contexte de l'agent quand la situation l'appelle. Quelque part entre un fragment de system prompt et un runbook.

Une skill n'est pas de la documentation de référence. Ce n'est pas "tout ce que tu dois savoir sur les tests". C'est un workflow : une séquence d'étapes que l'agent suit, avec des checkpoints qui produisent des preuves, se terminant par un critère de sortie défini.

Cette distinction, c'est tout le jeu. Si tu mets un essai de 2 000 mots sur les bonnes pratiques de testing dans le contexte de l'agent, l'agent le lit, génère du texte plausible, et passe à autre chose sans avoir rien appliqué. Si tu mets un workflow de 7 étapes avec checkpoints, l'agent les exécute parce qu'il y a une condition de sortie à valider.

## Pourquoi ça compte

Osmani propose une grammaire concrète pour transformer un agent de coding en collaborateur senior. C'est probablement la pratique la plus actionnable de la semaine pour quiconque cherche à industrialiser l'usage des agents — et le pendant micro de la grande question macro "comment on harnache l'IA en entreprise".
