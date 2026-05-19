---
title: "Interaction Models: A Scalable Approach to Human-AI Collaboration"
date: 2026-05-17
url: https://leadershipintech.com/links/22321/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Thinking Machines]
keywords: [interaction models, real-time AI, multimodal, human-AI collaboration, micro-turns]
theme: IA
tone: research
used_in: ["2026-05-17"]
---

## Résumé

Thinking Machines publie une preview de recherche des « interaction models » : des modèles qui gèrent l'interactivité nativement, et non via un harnais externe. Les modèles actuels fonctionnent en mode tour-par-tour : l'IA est aveugle tant que l'utilisateur n'a pas fini d'écrire ou de parler, et inversement. L'équipe propose une architecture en micro-tours alignés sur le temps réel, capable de percevoir et répondre simultanément en audio, vidéo et texte, avec un modèle de raisonnement asynchrone en arrière-plan. Objectif : que l'interactivité scale avec l'intelligence.

## Points clés

- Les modèles actuels traitent l'interactivité comme un afterthought, optimisé pour l'autonomie pas pour la collaboration.
- Le bottleneck est de bande passante : l'humain ne peut faire entrer toute sa connaissance dans une interface tour-par-tour.
- Design en micro-tours : flux continu d'entrée/sortie, où silence, chevauchement et interruption restent dans le contexte.
- Deux composants : un modèle d'interaction temps-réel + un modèle de fond asynchrone pour le raisonnement long.
- Capacités émergentes : gestion implicite du dialogue, interjections, parole simultanée, conscience du temps, outils en parallèle.
- S'appuie sur la « bitter lesson » : les composants hand-crafted seront dépassés par des capacités générales du modèle lui-même.

## Analyse approfondie

Aujourd'hui, Thinking Machines annonce une preview de recherche des _interaction models_ : des modèles qui gèrent l'interaction nativement, plutôt que via un échafaudage externe. L'équipe pense que l'interactivité doit scaler en même temps que l'intelligence ; la façon dont nous travaillons avec l'IA ne doit pas être un afterthought.

Les interaction models permettent aux gens de collaborer avec l'IA comme nous collaborons naturellement entre nous : ils prennent en entrée continue de l'audio, de la vidéo et du texte, et réfléchissent, répondent et agissent en temps réel.

L'équipe a entraîné un interaction model from scratch. Pour garantir la responsivité temps-réel, elle a adopté un design multi-stream à micro-tours.

### Le goulot d'étranglement de la collaboration

Les labos d'IA traitent souvent la capacité de l'IA à travailler de manière autonome comme la capacité la plus importante du modèle. Résultat : les modèles et les interfaces d'aujourd'hui ne sont pas optimisés pour garder les humains dans la boucle.

Une carte récente d'un modèle de pointe (Anthropic) le dit explicitement : « Quand il est utilisé en mode interactif et synchrone, "mains sur le clavier", les bénéfices du modèle sont moins clairs. Certains utilisateurs trouvent le modèle trop lent et n'en tirent pas toute la valeur. Les harnais d'agents autonomes et longs élicitent mieux les capacités de code du modèle. »

Les interfaces autonomes ont de la valeur, mais dans le vrai travail, les utilisateurs ne peuvent pas tout spécifier d'avance puis partir — un bon résultat vient d'un processus collaboratif. Pourtant, les humains sont poussés hors de la boucle non parce que le travail n'en a plus besoin, mais parce que l'interface n'a plus de place pour eux.

Les gens sont les plus efficaces quand ils peuvent collaborer avec une IA comme avec d'autres personnes : messages, parole, écoute, regard, démonstration et interjections au besoin — et que le modèle puisse en faire autant. La communication est meilleure avec :

- **Coprésence** : les gens interagissent avec ce avec quoi d'autres interagissent.
- **Contemporanéité** : on reçoit l'information au moment où elle est produite, avec retour instantané.
- **Simultanéité** : on reçoit et produit l'information en même temps.

### Au-delà du tour-par-tour

Pour résoudre ce goulot, il faut dépasser l'interface tour-par-tour. Les modèles actuels vivent sur un seul fil. Tant que l'utilisateur n'a pas fini de taper ou de parler, le modèle attend, sans perception de ce que l'utilisateur fait. Tant que le modèle n'a pas fini de générer, sa perception est figée. Ça crée un canal étroit qui limite combien de la connaissance, de l'intention et du jugement humain peuvent atteindre le modèle, et combien du travail du modèle peut être compris.

> Picture trying to resolve a crucial disagreement over email rather than in person.

Chez Thinking Machines, l'équipe pense pouvoir résoudre ce goulot de bande passante en rendant **l'IA interactive en temps réel à travers toute modalité**. Cela permet aux interfaces IA de rencontrer les humains là où ils sont, plutôt que de forcer les humains à se contorsionner.

La plupart des modèles existants ajoutent l'interactivité via un harnais : on assemble des composants pour émuler l'interruption, la multimodalité ou la concurrence. Mais la « bitter lesson » suggère que ces systèmes hand-crafted seront dépassés par les capacités générales. **Pour que l'interactivité scale avec l'intelligence, elle doit faire partie du modèle lui-même.**

### Capacités

- **Gestion de dialogue transparente** : le modèle suit implicitement si l'interlocuteur pense, cède la parole, se corrige, ou invite une réponse. Pas de composant de gestion de dialogue séparé.
- **Interjections verbales et visuelles** : le modèle intervient au besoin selon le contexte, pas seulement quand l'utilisateur a fini de parler.
- **Parole simultanée** : utilisateur et modèle peuvent parler en même temps (ex. traduction live).
- **Conscience du temps** : le modèle a une perception directe du temps écoulé.
- **Outils, recherche et UI génératives simultanés** : en parlant et en écoutant, le modèle peut chercher, naviguer, générer de l'UI, et réinjecter le résultat dans la conversation.

### L'approche

Architecture en micro-tours alignés sur le temps. Les modèles tour-par-tour voient une séquence alternée de tokens. Les interaction models voient un flux continu de micro-tours, où silence, chevauchement et interruption restent dans le contexte.

Le système est articulé autour de deux idées :

1. Un **interaction model** temps-réel qui maintient la présence en continu.
2. Un **modèle de fond** asynchrone qui prend en charge le raisonnement soutenu, l'usage d'outils, et le travail à horizon long.

Quand une tâche nécessite plus de raisonnement que ce qui peut être produit instantanément, l'interaction model délègue au modèle de fond qui tourne en asynchrone. L'interaction model reste présent tout du long — répondant aux follow-ups, recevant de nouveaux inputs, gardant le fil — et intègre les résultats du fond dans la conversation à mesure qu'ils arrivent.

Ce split permet à l'utilisateur de bénéficier à la fois de la responsivité et de toute l'intelligence : planification, usage d'outils et workflows agentiques des modèles de raisonnement, à la latence d'un modèle non-thinking. Les deux modèles partagent leur contexte.

L'audio et la vidéo continus sont le point de départ — modalités intrinsèquement temps-réel. Le texte peut attendre, une conversation live non.

## Pourquoi ça compte

Cette piste de recherche change la grammaire de la collaboration humain-IA : on passe d'une UX « prompt + attente » à une présence partagée. Si elle se généralise, elle rend obsolètes les designs où l'IA est jugée sur des KPIs de débit (tokens consommés, agents lancés) et recentre la valeur sur la qualité du dialogue.
