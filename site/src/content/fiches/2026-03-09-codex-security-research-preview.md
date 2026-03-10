---
title: "Codex Security: now in research preview"
date: 2026-03-09
url: "https://links.tldrnewsletter.com/cB4WOO"
authors: ["OpenAI"]
keywords: [Codex Security, application security, threat model, faux positifs, agent sécurité]
theme: "Sécurité"
tone: "news"
used_in: ["2026-03-09"]
---

## Résumé

OpenAI lance Codex Security (anciennement Aardvark) en research preview. Cet agent de sécurité applicative construit des modèles de menace spécifiques au projet, valide les vulnérabilités dans des environnements sandboxés et propose des correctifs contextualisés. En phase beta, il a réduit le bruit de 84% et les faux positifs de plus de 50%.

## Points clés

- Codex Security construit automatiquement un modèle de menace adapté à chaque projet
- Les vulnérabilités sont validées dans un environnement sandboxé avant d'être signalées
- Réduction du bruit de 84% et des faux positifs de 50%+ par rapport aux outils traditionnels
- Déploiement en cours pour les abonnés ChatGPT Pro, Enterprise, Business et Edu
- La sécurité applicative automatisée devient un terrain de compétition entre les labs IA

## Analyse approfondie

OpenAI lance Codex Security, son agent de sécurité applicative, en research preview. Le système construit un contexte approfondi de chaque projet pour identifier des vulnérabilités complexes que d'autres outils agentiques manquent, en présentant des découvertes à haute confiance avec des correctifs exploitables.

Le contexte est essentiel pour évaluer les risques de sécurité réels, mais la plupart des outils IA de sécurité se contentent de signaler des découvertes à faible impact et des faux positifs, forçant les équipes de sécurité à consacrer un temps considérable au tri. En parallèle, les agents accélèrent le développement logiciel, faisant de la revue de sécurité un goulet d'étranglement de plus en plus critique. Codex Security répond aux deux défis en combinant le raisonnement agentique des modèles frontier d'OpenAI avec une validation automatisée.

Le fonctionnement suit trois étapes. Premièrement, après configuration d'un scan, l'agent analyse le dépôt pour comprendre la structure de sécurité du système et génère un modèle de menace spécifique au projet — ce que le système fait, ce qu'il fait confiance, et où il est le plus exposé. Ce modèle de menace est éditable pour rester aligné avec l'équipe. Deuxièmement, en utilisant le modèle de menace comme contexte, il recherche les vulnérabilités et les catégorise selon leur impact réel attendu. Quand c'est possible, il teste les découvertes dans des environnements sandboxés pour distinguer le signal du bruit, ce qui réduit encore les faux positifs et permet la création de preuves de concept fonctionnelles. Troisièmement, il propose des correctifs alignés avec l'intention du système et son comportement environnant, ce qui permet des patches qui améliorent la sécurité tout en minimisant les régressions.

Codex Security apprend aussi du feedback au fil du temps. Quand on ajuste la criticité d'une découverte, il utilise ce retour pour affiner le modèle de menace et améliorer la précision sur les scans suivants.

Anciennement connu sous le nom d'Aardvark, Codex Security a débuté l'an dernier en bêta privée. Les premiers déploiements internes ont permis de détecter une vraie SSRF, une vulnérabilité critique d'authentification cross-tenant et de nombreux autres problèmes corrigés en quelques heures. Au fil de la bêta, la précision s'est considérablement améliorée : les scans sur les mêmes dépôts au fil du temps montrent une précision croissante, avec dans un cas une réduction du bruit de 84 % depuis le déploiement initial. Le taux de découvertes avec sévérité sur-rapportée a été réduit de plus de 90 %, et les faux positifs ont baissé de plus de 50 % sur tous les dépôts.

Sur les 30 derniers jours, Codex Security a scanné plus de 1,2 million de commits dans les dépôts de la cohorte bêta externe, identifiant 792 découvertes critiques et 10 561 de haute sévérité. Les problèmes critiques apparaissaient dans moins de 0,1 % des commits scannés, montrant que le système peut identifier des problèmes impactant la sécurité dans de grands volumes de code tout en minimisant le bruit.

OpenAI utilise aussi Codex Security pour scanner les dépôts open-source dont ils dépendent le plus, partageant les découvertes à fort impact avec les mainteneurs. Un thème récurrent dans les conversations avec les mainteneurs : le défi n'est pas le manque de rapports de vulnérabilités, mais le trop grand nombre de rapports de faible qualité. Le programme Codex for OSS commence à embarquer une cohorte initiale de mainteneurs open-source avec des comptes ChatGPT Pro et Plus gratuits. Le déploiement commence pour les abonnés ChatGPT Pro, Enterprise, Business et Edu.

## Pourquoi ça compte

Après Anthropic avec Mozilla, c'est OpenAI qui entre dans la sécurité applicative. La convergence des deux leaders montre que l'IA-for-security devient un marché à part entière, pas juste une démonstration technique.
