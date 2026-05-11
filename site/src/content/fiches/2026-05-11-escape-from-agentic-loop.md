---
title: "Escape from agentic loop"
date: 2026-05-11
url: https://www.proofofconcept.pub/p/escape-from-agentic-loop
authors: [proofofconcept.pub]
keywords: [agentic coding, human-in-the-loop, HITL, HOTL, focus, attention, agent orchestration]
theme: IA
tone: opinion
used_in: ["2026-05-11"]
---

## Résumé

L'auteur raconte son addiction à orchestrer des agents IA en parallèle — Claude Code, Codex, Gemini, Cursor, Replit, Rovo Dev, OpenClaw — et l'épuisement cognitif qui en découle. Plus les agents pensent vite, moins l'humain a le temps de penser. Pour s'en sortir, il introduit la distinction clé issue de la défense aérienne : Human-in-the-loop (HITL) vs Human-on-the-loop (HOTL), et revoit ses rituels quotidiens pour reconquérir du focus tout en continuant à utiliser les agents.

## Points clés

- L'usage massif d'agents en parallèle ressemble à du StarCraft II : exaltant, productif, mais épuisant
- Plus les agents pensent vite, moins l'humain trouve du temps pour penser
- HITL (Human-in-the-loop) = l'agent attend une validation humaine à chaque étape
- HOTL (Human-on-the-loop) = l'agent court tout seul, l'humain supervise et intervient si besoin
- La distinction vient de la défense aérienne (Phalanx, drones) et a été reprise par Stanford HAI pour la HCI moderne
- Il faut être explicite sur où l'humain est assis dans la boucle, plutôt que d'agiter "oversight" sans le définir
- L'auteur reconstruit ses rituels pour préserver du temps de réflexion personnelle

## Analyse approfondie

J'ai beaucoup utilisé des agents cette année, et c'est incroyable comme ils sont devenus puissants. Ça a commencé l'hiver dernier quand tout le monde se mettait à Claude Code. D'un coup, j'utilisais Claude Code, Codex, Gemini, Cursor, Replit, Rovo Dev, et bien sûr OpenClaw. Mes habitudes de concentration sont passées d'un écran et une fenêtre à une douzaine de terminaux où je gérais mes agents comme si je jouais à StarCraft II.

Soyons honnête : c'est très fun. C'est exaltant de voir les agents réfléchir et de co-construire avec eux. C'est un high productif au lieu d'un doom-scroll de réseaux sociaux, mais les effets sont similaires. Je me souviens d'un dîner entre amis. Pendant un omakase incroyable, on a tous naturellement pris une pause pour regarder nos téléphones. Ce n'était pas une pause réseaux sociaux. C'était une pause _orchestration d'agents_.

C'est fun, mais c'est épuisant. Ironiquement, plus les agents pensent, moins j'ai de temps pour penser, moi. C'est là que j'ai changé mon toolchain pour récupérer du temps. Avant d'y entrer, posons ce que sont Human-in-the-loop (HITL) et Human-on-the-loop (HOTL), la différence méthodologique, et comment je modifie mon planning et mes rituels pour reconquérir du focus tout en continuant à construire avec des agents.

### HITL vs HOTL

Human-in-the-loop (HITL) signifie que le système ne peut pas avancer sans toi. L'humain est un point de passage dans la chaîne causale. Tu approuves chaque draft, chaque proposition. L'agent attend une réponse et ne fait rien tant que l'humain n'a pas saisi quelque chose. Le terme vient des simulations de vol et a été adopté par le département de la Défense en 2012 pour décrire les armes semi-autonomes qui ne pouvaient pas engager une cible sans autorisation humaine.

Human-on-the-loop (HOTL) signifie que le système tourne tout seul et que l'humain supervise. Tu regardes le dashboard, tu vérifies les alertes, tu échantillonnes le travail, tu interviens si quelque chose semble aller de travers. L'exemple classique, c'est un système Phalanx de défense aérienne qui peut engager un missile entrant plus vite qu'aucun humain ne pourrait autoriser le tir ; une personne est _sur_ la boucle, pas _dans_ la boucle, parce que la vitesse d'engagement rend une véritable validation impossible.

Je sais. On est passés de la défense missile à ton mardi après-midi assez rapidement. Le vocabulaire vient d'un domaine où les enjeux sont absolus, ce qui est précisément pour ça qu'il est utile pour penser le travail IA quotidien — il te force à être spécifique sur _où_ l'humain est réellement assis, au lieu d'agiter "oversight" en espérant que ça compte. Stanford HAI a reformulé tout ça pour le design IA comme un problème de Human-Computer Interaction plutôt qu'un problème d'automation pure.

### Pourquoi cette distinction compte

Quand tu utilises Claude Code en mode supervisé — chaque commit validé, chaque PR relue avant merge — tu es en HITL. Quand tu fais tourner un agent qui code, teste et commit pendant que tu dors, tu es en HOTL. La plupart des devs glissent en silence de HITL vers HOTL sans avoir consciemment décidé. Et c'est là que le problème commence : tu te retrouves à valider _post-hoc_ des décisions que tu n'aurais pas prises toi-même, ou pire, à ne pas les valider du tout parce que tu n'as plus le temps.

### Reconquérir le focus

L'auteur décrit ensuite comment il a restructuré ses journées :

- Limiter le nombre d'agents en parallèle (au lieu de douze, deux ou trois max)
- Bloquer des plages de _focus solo_ sans aucun agent actif
- Séparer rigoureusement les moments HITL (revue de code critique) des moments HOTL (tâches de refactoring de fond)
- Considérer le temps de réflexion humain comme une ressource rare qu'il faut protéger activement

L'objectif n'est pas de moins utiliser l'IA. C'est de retrouver la capacité de _penser_ entre deux interactions avec les agents, et de redevenir l'architecte de ses propres décisions plutôt qu'un opérateur qui valide.

## Pourquoi ça compte

C'est l'article le plus honnête de l'année sur le coût cognitif réel de l'orchestration d'agents. Pour les leads et les architectes qui voient leurs équipes glisser vers le multi-agent en parallèle, c'est un cadre conceptuel utilisable lundi matin.
