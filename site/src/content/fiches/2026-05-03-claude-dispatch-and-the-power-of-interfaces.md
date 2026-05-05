---
title: "Claude Dispatch and the Power of Interfaces"
date: 2026-05-03
url: https://leadershipintech.com/links/22203/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Ethan Mollick, One Useful Thing]
keywords: [chatbot, AI interfaces, cognitive load, productivity, Claude]
theme: IA
tone: opinion
used_in: ["2026-05-03"]
---

## Résumé

Ethan Mollick avance que la majorité des gens utilisent l'IA via des chatbots, et que c'est probablement la pire interface pour faire du vrai travail avec elle. Une étude récente sur des professionnels de la finance utilisant GPT-4o pour une tâche complexe de valorisation montre que le chatbot impose une "taxe cognitive" : pavés de texte, propositions hors-sujet, conversations qui dérivent. Les juniors sont les plus pénalisés alors qu'ils auraient le plus à gagner. La voie à suivre est celle d'interfaces dédiées à des tâches spécifiques — la programmation est aujourd'hui le seul domaine où ces interfaces sont vraiment matures, parce que les labs IA construisent pour eux-mêmes.

## Points clés

- Le "capability overhang" de l'IA vient autant de la mauvaise utilisation que des limites des modèles.
- Les chatbots imposent une charge cognitive qui absorbe une partie des gains de productivité.
- Une étude sur des financiers et GPT-4o quantifie cette charge tour par tour.
- Les profils les moins expérimentés sont les plus pénalisés par l'interface chatbot.
- Les interfaces dédiées (Claude Code, Cursor, Copilot pour la programmation) sont la voie de sortie.

## Analyse approfondie

Les IA sont déjà bien plus capables que la plupart des gens ne le réalisent. Une grande partie de cet "écart de capacité" perçu vient non pas des limites de l'IA — qui en a encore beaucoup, bien sûr — mais de la façon dont les gens interagissent avec elle. L'écrasante majorité des utilisateurs accèdent à l'IA via des chatbots, et le plus souvent via les versions gratuites avec des modèles moins capables. Un chatbot, c'est très bien pour une question rapide, mais c'est une mauvaise façon d'abattre du travail réel.

Une recherche récente suggère même qu'on paie une taxe mentale lorsqu'on utilise des interfaces chatbot pour travailler. Un nouveau papier (arxiv 2505.10742) a fait passer à un petit groupe de professionnels de la finance une tâche complexe de valorisation avec GPT-4o, en mesurant leur charge cognitive à partir des transcripts, tour par tour. Les participants ont bien observé un gain de productivité avec l'IA, mais une partie de ce gain semblait absorbée par la manière dont l'IA leur présentait l'information : des murs de texte, des propositions de nouveaux sujets, des discussions qui s'éparpillent. L'interface chatbot, et non le travail lui-même, semblait être l'obstacle. Et une fois qu'une conversation avait dérapé, elle restait dérapée. L'IA, optimisée pour être serviable, se contentait de refléter la structure désorganisée fournie par l'utilisateur, qui, débordé, ne réorganisait pas. Les deux côtés amplifiaient le problème.

Les personnes les plus pénalisées étaient les moins expérimentées — exactement celles qui auraient le plus à gagner de l'IA si elles parvenaient à garder le fil de ce qu'elles font avec.

Cela ne devrait pas surprendre quiconque a déjà essayé de faire avancer un sujet avec un chatbot. Vous posez une question précise et vous recevez cinq paragraphes contenant la réponse (quelque part !), pendant que l'IA vous propose trois nouveaux sujets que vous n'avez pas demandés. L'interface elle-même crée un coût cognitif qui peut dépasser les bénéfices de l'intelligence du modèle. À quoi pourrait ressembler une meilleure interface ?

Une option consiste à construire des interfaces spécifiques à des tâches ou des métiers. De toutes les interfaces IA spécialisées, les seules vraiment complètes aujourd'hui sont celles dédiées à la programmation. C'est exactement ce à quoi on pouvait s'attendre : les labs IA sont composés de programmeurs, les modèles sont massivement entraînés sur du code, et les gens qui construisent ces outils les construisent souvent pour eux-mêmes. Claude Dispatch, Claude Code, Cursor ou Copilot illustrent cette logique — ce ne sont plus des fenêtres de chat universelles, ce sont des UI conçues pour un job précis (lire un repo, modifier des fichiers, exécuter des tests, gérer un PR).

Pour les autres métiers, l'enjeu est de répliquer cette spécialisation : interfaces de valorisation pour la finance, interfaces de revue de contrats pour le juridique, interfaces de pilotage produit pour les PMs. Tant qu'on coince ces métiers dans une zone de chat, on continue de payer la taxe cognitive.

## Pourquoi ça compte

Pour un Engineering Director, ce post signe un déplacement stratégique : l'enjeu IA ne se joue plus seulement au niveau du modèle, il se joue au niveau de l'interface. Choisir, financer ou construire des UI dédiées va devenir une décision d'architecture aussi importante que le choix du modèle.
