---
title: "A hacker group is poisoning open source code at an unprecedented scale"
date: 2026-05-25
url: https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/
authors: [arstechnica.com]
keywords: [supply chain, open source, TeamPCP, GitHub, sécurité logicielle]
theme: Sécurité
tone: news
used_in: ["2026-05-25"]
---

## Résumé

Le groupe cybercriminel TeamPCP a transformé l'attaque de supply chain logicielle — autrefois rare — en quasi-routine hebdomadaire, corrompant des centaines d'outils open source et extorquant ses victimes. GitHub est la dernière cible en date : un développeur a installé une extension VSCode « empoisonnée », permettant aux attaquants de revendiquer l'accès à environ 4 000 dépôts (au moins 3 800 confirmés compromis, tous contenant le code interne de GitHub). En quelques mois, le groupe a mené 20 « vagues » d'attaques dissimulant des malwares dans plus de 500 logiciels distincts.

## Points clés

- L'attaque de supply chain, jadis exceptionnelle, est devenue un événement quasi hebdomadaire.
- TeamPCP a corrompu plus de 500 logiciels distincts (plus d'un millier en comptant les versions) en seulement quelques mois, sur 20 « vagues ».
- GitHub a été compromis via une extension VSCode piégée installée par un développeur ; ~3 800 dépôts internes touchés.
- Le groupe revend les accès et le code source sur BreachForums et extorque ses victimes.
- Parmi les victimes antérieures figurent OpenAI et la société de data contracting Mercor.

## Analyse approfondie

Une attaque de supply chain logicielle — où des hackers corrompent un logiciel légitime pour y dissimuler leur propre code malveillant — était autrefois un événement relativement rare, mais qui hantait le monde de la cybersécurité par sa menace insidieuse : transformer n'importe quelle application innocente en point d'entrée dangereux dans le réseau d'une victime. Désormais, un groupe de cybercriminels a fait de ce cauchemar occasionnel un épisode quasi hebdomadaire, corrompant des centaines d'outils open source, extorquant ses victimes pour le profit, et semant un nouveau niveau de défiance dans tout un écosystème utilisé pour créer les logiciels du monde entier.

Mardi soir, la plateforme de code open source GitHub a annoncé avoir été victime d'une telle attaque : un développeur de GitHub avait installé une extension « empoisonnée » pour VSCode, un plug-in d'un éditeur de code très répandu qui, comme GitHub, appartient à Microsoft. En conséquence, les hackers derrière la brèche — un groupe de plus en plus notoire appelé TeamPCP — affirment avoir accédé à environ 4 000 dépôts de code de GitHub. La déclaration de GitHub a confirmé avoir trouvé au moins 3 800 dépôts compromis, en notant que, d'après ses constats à ce stade, ils contenaient tous le code propre de GitHub, et non celui de ses clients.

« Nous sommes ici aujourd'hui pour mettre en vente le code source de GitHub et ses organisations internes », a écrit TeamPCP sur BreachForums, un forum et marketplace pour cybercriminels. « Tout pour la plateforme principale est là et je suis très heureux d'envoyer des échantillons aux acheteurs intéressés pour vérifier l'authenticité absolue. »

La brèche de GitHub n'est que le dernier incident de ce qui est devenu la plus longue série d'attaques de supply chain jamais observée, sans fin en vue. Selon la firme de cybersécurité Socket, spécialisée dans les chaînes d'approvisionnement logicielles, TeamPCP a, sur les seuls derniers mois, mené 20 « vagues » d'attaques ayant dissimulé du malware dans plus de 500 logiciels distincts — soit bien plus d'un millier en comptant toutes les versions de code détournées.

Ces morceaux de code corrompus ont permis aux hackers de TeamPCP de pénétrer des centaines d'entreprises ayant installé les logiciels, indique Ben Read, responsable du renseignement stratégique sur les menaces chez la firme de sécurité cloud Wiz. GitHub n'est que le dernier nom d'une longue liste de victimes, qui inclut aussi la société d'IA OpenAI et la firme de data contracting Mercor.

## Pourquoi ça compte

À l'heure où les agents installent et exécutent du code tiers à grande vitesse, la supply chain open source devient une surface d'attaque critique — et l'incident GitHub montre que même les fournisseurs d'outils de dev ne sont pas à l'abri.
