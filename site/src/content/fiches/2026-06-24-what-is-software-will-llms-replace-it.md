---
title: "What Is Software, and Will LLMs Replace It?"
date: 2026-06-24
url: https://tomassetti.me/what-is-software-llms-interface-layer/?utm_source=tldrit
authors: [Federico Tomassetti, tomassetti.me]
keywords: [LLM, software, MCP, deterministic systems, databases]
theme: IA
tone: opinion
used_in: ["2026-06-24"]
---

## Résumé

Federico Tomassetti répond à la question « les LLM vont-ils remplacer le logiciel ? » par un non argumenté. Un LLM n'a ni schéma, ni clés étrangères, ni transactions, ni contraintes : il ne peut garantir ni la cohérence des données, ni la même réponse demain qu'aujourd'hui. Le logiciel reste pertinent pour organiser/normaliser les données, faire respecter la cohérence, visualiser et guider les processus. La direction du mouvement n'est donc pas le logiciel absorbé par les LLM, mais l'inverse : les LLM absorbés dans le logiciel, mis en façade via des protocoles comme MCP.

## Points clés

- Quatre rôles durables du logiciel : organiser/normaliser les données, faire respecter cohérence et intégrité, visualiser/filtrer, guider les processus (savoir-faire métier rendu exécutable).
- Un LLM ne stocke pas ses données : sa « mémoire » est souvent un tas de notes, qui n'imposent ni schéma, ni cascade de suppression, ni reproductibilité des réponses.
- L'affaire *Moffatt v. Air Canada* (CRT 149, février 2024) : un chatbot a inventé une politique de remboursement contraire aux règles publiées ; le tribunal a condamné la compagnie. Une table de politique déterministe aurait renvoyé une seule réponse.
- MCP est le « USB-C de l'IA » : il ne remplace pas la base de données, il donne aux modèles un moyen standard et contrôlé d'atteindre les systèmes qui détiennent l'état structuré (Salesforce/Agentforce, Atlassian/Jira-Confluence).
- L'inversion à venir : on n'aura pas une appli LLM saupoudrée de déterminisme, mais du logiciel déterministe utilisant des LLM comme composant. Le logiciel n'est pas remplacé, il est mis en façade.

## Analyse approfondie

On utilise tous des LLM depuis un moment et on a tous été impressionnés. À un moment, il est naturel de se demander : c'est ça ? C'est ça qui va remplacer le logiciel ? Va-t-on simplement parler aux ordinateurs désormais, décrire ce qu'on veut, le voir apparaître et sauter tout ce qu'il y a entre les deux ?

Je ne crois pas, même si c'est tentant. Tapez « montre-moi les ventes des cinq dernières années » et vous obtenez un graphique. Demandez le deck de slides et vous l'obtenez. Fini. Qui a encore besoin de SaaS ?

Mais cela passe à côté de ce que le logiciel a fait pour nous depuis toujours. Selon moi, il reste pertinent de quatre façons :

- Données organisées et normalisées.
- Cohérence imposée.
- Choses visualisées de manière à voir les patterns.
- Processus guidés étape par étape — des années de savoir-faire accumulé sur comment bien faire un travail, capturé et rendu exécutable.

Donc oui, les LLM nous montrent quelque chose de vraiment utile : les interfaces peuvent être bien plus flexibles qu'on ne le supposait. Mais ce n'est pas pareil que le logiciel disparaissant dans la conversation.

### Ce que fait réellement le logiciel

Ancrons cela dans du concret : un CRM. Oui, les CRM sont ennuyeux à mourir, mais toute entreprise B2B en a un.

**Il organise les données sous une forme structurée, requêtable, normalisée.** Une opportunité n'est pas un blob de texte. C'est un enregistrement lié à une entreprise, qui a des contacts avec téléphones et e-mails, un champ source de lead qui alimente l'attribution marketing, et une chaîne remontant aux contrats passés. Cette structure permet de demander « quelles opportunités venaient de recommandations et ont été closes au-dessus de 50 k€ ces six derniers mois ? » et d'obtenir une réponse fiable en millisecondes, pas un paragraphe qui sonne plausible.

**Il impose cohérence et intégrité.** On ne peut pas créer une opportunité sans d'abord créer l'entreprise à laquelle elle appartient. On ne peut pas supprimer une entreprise qui a encore des contrats ouverts. Le système l'empêche, ou cascade la suppression dans un ordre défini. Ce sont les règles qui empêchent les données de devenir des déchets six mois plus tard.

**Il permet visualisation et filtrage.** Les interfaces purement textuelles ne fonctionnent pas bien pour tout. On a besoin de voir les données, de repérer les anomalies dans un graphe, les patterns d'un coup d'œil.

**Il guide les processus.** Il encode la terminologie de l'entreprise, sa séquence d'approbations, et les petits morceaux de savoir-faire métier qui ont mis des années à être réglés. « Vous ne pouvez pas marquer une opportunité comme gagnée avant que le contrat soit attaché. » Ce n'est pas de la friction. Ce sont des règles.

### Note historique : SQL et le rêve de l'anglais courant

Il y a un vieux rêve derrière tout ça. Dans les années 1970, quand les chercheurs IBM Donald Chamberlin et Raymond Boyce ont conçu SQL, une partie de l'argumentaire était qu'il serait assez simple pour que des non-programmeurs l'utilisent directement — un manager taperait ce qu'il veut dans quelque chose proche de l'anglais courant et obtiendrait une réponse. Cinquante ans plus tard, on essaie toujours de rendre cette promesse vraie, et on découvre toujours que la partie difficile n'a jamais été seulement l'interface.

### Pourquoi un LLM seul ne peut pas remplacer le logiciel métier

Retirez l'interface de chat et demandez : où un LLM garde-t-il ses données ? Nulle part. Un modèle n'a pas de schéma, pas de clés étrangères, pas de transactions, pas de contraintes. Dans beaucoup de setups d'agents, la « mémoire » est une collection de fichiers ou de notes que l'agent lit et écrit entre les sessions. Utile, mais ce n'est pas une base de données. Les notes n'imposent pas qu'une opportunité ait une entreprise. Elles ne cascadent pas les suppressions. Elles ne garantissent pas que le chiffre obtenu aujourd'hui sera le même demain. Et si une réponse ne peut être déterminée de façon fiable à partir de ces notes ? Le LLM répondra quand même. Et la réponse sera plausible. Mais essayez de soumettre ces chiffres au fisc.

### Que montre l'affaire du chatbot d'Air Canada ?

Ce n'est pas un risque hypothétique. En février 2024, le Civil Resolution Tribunal du Canada a tranché contre Air Canada (*Moffatt v. Air Canada*, CRT 149), après que le chatbot de la compagnie a dit à un client qu'il pouvait réserver un vol au prix plein puis demander un tarif deuil ensuite — ce qui contredisait les règles publiées de l'entreprise. La défense d'Air Canada était, en substance, que le chatbot était responsable de ses propres mots. Le tribunal n'a pas accepté cet argument et a ordonné à la compagnie de payer indemnités, intérêts et frais. C'est tout le problème en une phrase : une table de politique déterministe aurait renvoyé exactement une réponse. Une interface de chat, faute de cette table, en a improvisé une, et l'entreprise a payé l'improvisation.

### MCP et le pont vers le logiciel

Que faire quand votre modèle a besoin d'une structure qu'il n'a pas ? On ne cherche pas à fourrer une base de données dans ses poids. On construit un pont vers la base qui existe déjà. Au départ via le tool calling, et maintenant via le Model Context Protocol, « l'USB-C des applications IA ». La métaphore travaille vraiment : l'USB-C n'a pas remplacé votre disque dur, votre écran ou votre clavier — il leur a donné une prise standard. MCP fait pareil entre les modèles et les systèmes qui détiennent l'état structuré.

Salesforce n'a pas reconstruit son CRM en chatbot : il a intégré le support MCP à Agentforce pour que le modèle atteigne le CRM qui, lui, fait respecter le schéma et les règles de cascade. Atlassian n'a pas dissous Jira et Confluence dans la conversation : il a construit un serveur MCP distant pour qu'un modèle puisse requêter et agir sur des données qui vivent toujours, structurées et contraintes, là où elles ont toujours vécu. Remarquez la direction du mouvement : ces entreprises ne dissolvent pas leurs produits dans des chatbots. Ce n'est pas le logiciel absorbé par les LLM. **C'est les LLM absorbés dans le logiciel.**

### L'inversion

On a commencé en n'utilisant que des LLM. Puis les LLM ont commencé à utiliser du logiciel. Ce qui arrivera ensuite, je crois, c'est que le logiciel redeviendra la force motrice, inversant la proportion. Au final, on n'aura pas une application LLM avec un peu de logiciel déterministe. On aura du logiciel déterministe qui utilise des LLM comme un de ses composants. **Le logiciel ne sera pas remplacé par les LLM. Il sera mis en façade par eux.** On a toujours besoin de données normalisées et bien organisées.

## Pourquoi ça compte

Au milieu de l'enthousiasme « le chat va tout remplacer », cet article remet les pendules à l'heure architecturale : les garanties (cohérence, intégrité, reproductibilité) restent l'affaire du logiciel déterministe. C'est un cadre clair pour décider où placer un LLM dans une architecture — en façade, pas au cœur de l'état.
