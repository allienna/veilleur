---
title: "The Bill Arrives: How to Manage Agentic AI Costs at Scale"
date: 2026-06-15
url: https://cockroachlabs.com/blog/agentic-ai-costs-at-scale
authors: [Cockroach Labs]
keywords: [agentic AI, coûts, tokens, re-sent context, FinOps]
theme: IA
tone: opinion
used_in: ["2026-06-15"]
---

## Résumé

L'article part du « budget blowout » d'Uber — budget IA annuel cramé en quatre mois — pour expliquer pourquoi les modèles de coût conçus pour les chatbots s'effondrent face aux agents. Un agent déclenche 10 à 20 appels de modèle par tâche et consomme 5 à 30 fois plus de tokens qu'une requête classique. Le coût le plus invisible est le *re-sent context* : 62 % de la facture d'inférence d'un agent. La déflation du coût du token ne sauvera personne, car la consommation grimpe plus vite que le prix unitaire ne baisse.

## Points clés

- Uber : adoption de Claude Code de 32 % à 84 % de 5 000 ingénieurs en trois mois ; budget IA annuel épuisé en quatre mois ; 500–2 000 $/ingénieur/mois.
- Les workflows agentiques consomment 5 à 30 fois plus de tokens par tâche qu'un chatbot (Gartner) ; l'unité pertinente devient le coût par tâche complétée, pas par prompt.
- Le coût du token a chuté de 98 % depuis début 2024, mais les factures montent quand même.
- Re-sent context (renvoi répété des prompts système, définitions d'outils, état) = 62 % de la facture d'inférence d'un agent (Stanford Digital Economy Lab).
- Sam Altman qualifie la question du ROI de « critique la plus juste » ; Goldman Sachs projette ×24 la consommation de tokens d'ici 2030.

## Analyse approfondie

Le récit s'ouvre en avril 2026 sur une phrase du CTO d'Uber, Praveen Neppalli Naga, que tout dirigeant tech ou finance devrait méditer : « Je repars de zéro, parce que le budget que je pensais nécessaire est déjà pulvérisé. » Entre décembre 2025 et mars 2026, l'adoption de Claude Code passe de 32 % à 84 % des 5 000 ingénieurs d'Uber. En avril, tout le budget IA annuel est parti. Les coûts API mensuels par ingénieur oscillent entre 500 et 2 000 dollars. L'inférence IA en entreprise représente désormais 85 % des budgets IA totaux, et les workflows agentiques consomment 5 à 30 fois plus de tokens par tâche qu'une requête de chatbot standard.

Uber n'est pas un cas isolé d'adoption imprudente. L'auteur a eu la même conversation avec des dirigeants d'entreprises de toutes tailles : les chiffres du pilote étaient une chose, ceux de la production une tout autre bête. Ce qui est arrivé à Uber arrive discrètement à toute organisation faisant tourner de l'IA agentique à l'échelle, parce que l'économie des agents est fondamentalement différente de tous les modèles de pricing précédents.

L'économie agentique ne se résume pas au prix du modèle : c'est le coût total pour accomplir une tâche quand un agent planifie, récupère du contexte, appelle des outils, écrit un état, valide des sorties et réessaie les étapes échouées. En juin 2026, Sam Altman (OpenAI) déclare à CNBC que la question de savoir si la dépense IA produira un jour un retour est « la critique la plus juste de l'IA en ce moment ». Il reconnaît que des clients lui disent avoir déjà épuisé tout leur budget IA 2026, et que la préoccupation des coûts est passée de jamais évoquée à deuxième sujet le plus fréquent en quelques mois.

**Pourquoi votre budget IA actuel ne marche pas pour les agents.** La plupart des équipes gèrent le coût par token d'un modèle. Cette hypothèse tenait pour les chatbots, elle casse pour les agents. Le coût par token de l'intelligence a chuté de 98 % depuis début 2024, et pourtant les factures montent. La raison : une requête de chatbot déclenche un appel d'inférence, mais un workflow agentique — où un LLM raisonne de façon itérative, appelle des outils, vérifie ses sorties et s'autocorrige — peut déclencher 10 à 20 appels de modèle pour une seule tâche initiée par l'utilisateur. L'unité pertinente n'est plus le coût par prompt mais le coût par tâche complétée.

Selon Gartner (mars 2026), les modèles agentiques exigent 5 à 30 fois plus de tokens par tâche qu'un chatbot. Les entreprises l'ont découvert seulement après l'arrivée de leurs factures de production : l'économie du pilote n'avait aucun rapport avec celle des boucles agentiques multi-étapes tournant des milliers de fois par jour. Goldman Sachs projette une multiplication par 24 de la consommation de tokens d'ici 2030 (120 quadrillions de tokens/mois). Altman donne un repère : il y a six ans et demi, le plus gros consommateur de tokens d'OpenAI utilisait 100 000 tokens/mois — c'est aujourd'hui la moyenne mondiale par habitant, et le leader actuel en consomme ~100 milliards/mois, une multiplication par un million de la consommation par utilisateur. Gartner projette une inférence 90 % moins chère sur un modèle à mille milliards de paramètres d'ici 2030, mais des tokens moins chers ne produiront pas des factures moins chères, car : les modèles agentiques consomment bien plus de tokens par tâche ; la croissance de la consommation dépasse la baisse des coûts unitaires ; les fournisseurs ne répercuteront pas entièrement les baisses. Comme le résume l'analyste Will Sommer : « Les Chief Product Officers ne doivent pas confondre la déflation des tokens-commodité avec la démocratisation du raisonnement de frontière. »

**Les coûts qu'on oublie de budgéter.** L'inférence n'est que la pointe de l'iceberg. Quatre couches dirigent réellement les coûts d'exploitation. La première — et le plus gros coût invisible — est le *re-sent context* : la retransmission répétée des prompts système, définitions d'outils, skills, instructions et historique d'état à travers les multiples appels d'un même workflow. En pratique, on paie le modèle pour relire ce qu'il a déjà vu. La recherche du Stanford Digital Economy Lab (Agentic AI Cost Attribution, 2025) établit que le re-sent context représente 62 % de la facture totale d'inférence d'un agent. Cela vaut aussi bien pour une API propriétaire (facturation au token) que pour un modèle open-source auto-hébergé (coût GPU) : dans les deux cas, le contexte redondant coûte. Pour l'auto-hébergé, il se manifeste en pression mémoire GPU, inférence plus lente et débit plus faible par serveur — voire, pour un modèle Llama fine-tuné embarqué dans une voiture, en temps de réaction dégradé.

L'article détaille ensuite les autres couches de coût et les stratégies pour bâtir un vrai business case avant que la facture n'arrive.

## Pourquoi ça compte

C'est le rappel FinOps que l'ère agentique impose : le coût ne se pilote plus au token mais à la tâche complétée, et le re-sent context est l'angle mort budgétaire numéro un de toute organisation qui passe ses agents en production.
