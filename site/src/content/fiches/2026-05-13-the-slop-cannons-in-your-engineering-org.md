---
title: "The slop cannons in your engineering org"
date: 2026-05-13
url: https://www.yoyo.bio/p/the-slop-cannons-in-your-engineering
authors: [Yoni Rechtman]
keywords: [AI agents, productivity, GitHub, code review, METR study]
theme: IA
tone: opinion
used_in: ["2026-05-13"]
---

## Résumé

Yoni Rechtman nomme un phénomène que beaucoup d'équipes croisent sans pouvoir le décrire : les « slop cannons ». Des devs (ou designers) qui ont weaponisé les outils agentiques contre leur propre équipe. PRs massives et confiantes, trois agents en parallèle, et un patch correctif qui tombe deux semaines plus tard. Le texte est étayé par des chiffres frappants : 17 millions de PRs/mois générées par les agents IA en mars 2026 (+325 % en six mois), 1,7× plus d'issues dans les PRs co-écrites par l'IA, et une étude METR où les devs se sentent 20 % plus rapides alors qu'ils sont 19 % plus lents.

## Points clés

- Définition : un slop cannon confond volume et valeur, vélocité et progrès, tokens dépensés et problèmes résolus
- Signaux : 3+ agents en parallèle par défaut, PRs massives, patches récurrents, incapables d'expliquer leur diff
- Volume agentique sur GitHub : 4M PRs/mois (sept 2025) → 17M (mars 2026), soit +325 %
- Légitimité estimée à « 1 sur 10 » par Xavier Portilla Edo (Voiceflow)
- CodeRabbit : 1,7× plus d'issues dans les PRs co-IA, 75 % d'erreurs de logique en plus
- Veracode : 45 % de taux d'échec sur les benchmarks de sécurité du code IA
- Étude METR : 16 devs expérimentés, ressentis +20 %, mesurés −19 % (gap de 39 points)
- Stack Overflow 2025 : 46 % se méfient activement de l'IA, seulement 3 % la trustent vraiment, sentiment positif 70 % → 60 %

## Analyse approfondie

Pour commencer : je dis ça en tant que quelqu'un qui adore Cursor et Claude Code. J'ai passé un dimanche soir à laisser Claude Code écrire des scripts pour compter automatiquement des vidéos de réseaux sociaux pendant que je jouais à Diablo IV, et c'était un excellent dimanche. Vous ne trouverez pas un plus grand croyant dans le dev agentique que moi.

Ce qui rend ce que je vais dire plus crédible, pas moins. Il existe un type de personne identifiable dans les organisations SaaS modernes qui a weaponisé ces outils contre sa propre équipe. Elle fait tourner des agents comme une machine à sous. Elle génère de l'output comme un arroseur génère de l'eau. Elle confond volume et valeur, vélocité et progrès, tokens dépensés et problèmes résolus.

Le terme que j'ai entendu et qui décrit le mieux le phénomène : slop cannons.

### À quoi ils ressemblent

Un slop cannon est souvent un ingénieur ou designer (ou ces hybrides « designer-engineer » avec des bios LinkedIn bizarres) qui a converti son workflow en firehose d'artefacts IA. Ils ont une forme reconnaissable :

- Ils lancent plus de trois agents en parallèle par défaut, pas en exception, souvent depuis leur téléphone le matin pour aller voir le résultat quelques heures plus tard
- Leurs PRs sont grosses, rapides, confiantes, et la médiane nécessite un patch correctif dans les deux semaines
- Ils postent des screenshots de terminal sur Slack avec des emojis fusée
- Ils ne peuvent pas expliquer leur propre diff
- Ils se méfient des reviews humains plus que de celles du modèle
- Ils répètent en boucle « the agent figured it out » et « Claude can handle that »

Les slop cannons ne sont pas intrinsèquement de mauvais devs. Ils sont souvent très bons, et c'est ce qui rend le pattern dangereux. Ils ont assez de goût pour ship quelque chose de désirable, et assez de vélocité pour en ship beaucoup.

### Les chiffres

En mars 2026, les agents IA ont généré environ 17 millions de PRs par mois sur GitHub, contre 4 millions en septembre 2025. Soit +325 % en six mois. Xavier Portilla Edo, head of cloud infrastructure chez Voiceflow, estime le taux de légitimité à « 1 sur 10 » — 90 % des PRs agent-authored sont du bruit que le mainteneur doit trier.

Claude Code représenterait à lui seul environ 4,5 % de tous les commits publics GitHub en mars 2026. Les commits hebdo sur la plateforme ont atteint 275 millions début 2026, soit ×14 en un an. GitHub Actions a franchi 2,1 milliards de minutes par semaine. Rien de tout ça n'a scalé parce que les humains sont devenus 14× plus productifs. Ça a scalé parce que les canons tirent.

La plateforme accuse le coup. Début avril, GitHub a eu cinq pannes en 48 heures : 2,7 h d'épuisement du backend Copilot, 8,7 h de blackout de code search, un incident d'audit log, quatre heures de dégradation du Copilot Cloud Agent, un échec de job-startup du coding agent.

### Au niveau de l'artefact, c'est pire

L'analyse CodeRabbit de décembre 2025 sur 470 PRs open source a trouvé que les PRs co-écrites par l'IA contiennent 1,7× plus d'issues que les PRs purement humaines, avec 1,4 à 1,7× plus de findings critiques ou majeurs, et des erreurs de logique 75 % plus fréquentes. Le rapport Veracode 2025 GenAI Code Security a testé plus de 100 LLMs sur quatre langages et trouvé que le code généré par IA shipped avec un taux d'échec de 45 % sur les benchmarks de coding sécurisé.

Un vrai slop cannon ne ship pas du code propre à grande échelle. Il ship du code sale à grande échelle, puis demande à un autre agent de le fixer.

### Le perception gap

METR a lancé en début 2025 un essai contrôlé randomisé sur 16 devs open source expérimentés, sur 246 tâches, dans des codebases matures sur lesquels ils travaillaient depuis en moyenne cinq ans. Avant l'étude, les devs prévoyaient que les outils IA les rendraient 24 % plus rapides. Après l'étude, les mêmes devs ressentaient être 20 % plus rapides. Le résultat mesuré : l'IA les a rendus 19 % plus lents.

Un écart de 39 points entre perception et réalité, en faveur du sentiment de productivité tout en étant mesurablement moins bon.

Le Stack Overflow Developer Survey 2025 confirme la chose sous un autre angle. 84 % des devs utilisent ou prévoient d'utiliser l'IA, 51 % des pros au quotidien. La confiance s'effondre dans la direction opposée : 46 % se méfient activement de la précision, seuls 3 % « trustent fortement », 45 % rapportent que débugger du code généré par IA prend plus de temps que de l'écrire, et 66 % listent les « solutions IA presque justes, mais pas tout à fait » comme leur première frustration. Le sentiment positif est passé de 70 %+ en 2023-2024 à 60 % en 2025. L'adoption monte, la confiance descend.

## Pourquoi ça compte

Ce papier met un mot — slop cannon — sur un comportement qu'on n'osait pas nommer. Et il l'étaye par des chiffres qui devraient être lus dans toutes les directions engineering : la vitesse ressentie n'est pas la vitesse mesurée. Le management se fait piéger par les métriques d'output.
