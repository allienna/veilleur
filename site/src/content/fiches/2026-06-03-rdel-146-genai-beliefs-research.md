---
title: "RDEL #146: Which popular beliefs about GenAI and software engineering hold up to research?"
date: 2026-06-03
url: https://rdel.substack.com/p/rdel-146-which-popular-beliefs-about
authors: [Lizzie, Research-Driven Engineering Leadership]
keywords: [GenAI productivity, developer productivity, SPACE framework, myths, engineering leadership]
theme: Leadership
tone: research
used_in: ["2026-06-03"]
---

## Résumé

Research-Driven Engineering Leadership s'appuie sur un article ACM Queue (co-écrit par des auteurs du framework SPACE) pour examiner huit mythes persistants sur la GenAI dans le génie logiciel. La conclusion : la valeur de la GenAI vient de la façon dont elle est déployée, mesurée et soutenue, pas de l'accès à l'outil. Les développeurs ne passent qu'environ 14 % de leur temps à coder, donc accélérer le coding ne fait que déplacer la pression vers la revue, les tests et l'intégration. L'article propose trois actions concrètes pour les leaders : auditer les 86 %, viser un goulot de l'outer loop, et combler le déficit de confiance.

## Points clés

- Mythe 1 : les devs passent l'essentiel de leur temps à coder → en réalité ~14 % (étude Microsoft 2025, 450+ ingénieurs).
- Mythe 2 : le coding est le goulot → l'accélérer déplace juste la pression vers la revue/test/intégration.
- Mythe 3 : les lignes de code mesurent l'impact IA → métrique invalide, encourage le gaming.
- Mythe 4 : l'IA aide toutes les tâches également → +18 % de temps pour des devs expérimentés en open source ; reformuler un prompt change le code dans 46 % des cas et la correction dans 28 %.
- Mythe 5/6 : l'IA crée des 10x devs / c'est à chaque dev de la faire marcher → les sauts de productivité historiques viennent de refontes systémiques, pas d'outils individuels.
- Mythe 7/8 : adoption automatique / vitesse startup en entreprise → 80 % utilisent l'IA mais seulement 29 % font confiance à la sortie ; les stacks entreprise (legacy, propriétaire) sont mal représentés dans les données d'entraînement.

## Analyse approfondie

Bienvenue dans Research-Driven Engineering Leadership. Chaque semaine, nous posons un sujet intéressant en leadership d'ingénierie et appliquons la recherche la plus récente pour aboutir à une réponse.

Presque chaque leader d'ingénierie s'est vu demander une version de "quelle est votre productivité IA ?" ces douze derniers mois. La réponse attendue est un chiffre unique et impressionnant, mais les preuves réelles sur la GenAI en génie logiciel sont bien plus désordonnées que les gros titres ne le suggèrent. Cette semaine nous demandons : **quelles croyances populaires sur l'IA et la productivité des développeurs la recherche soutient-elle réellement ?**

La conversation de l'industrie sur la GenAI a avancé plus vite que la recherche censée la fonder. Décisions d'achat, plans d'effectifs et OKR trimestriels sont façonnés par des démos de vendeurs, des anecdotes et une poignée d'études contrôlées sur des problèmes-jouets. Le problème, c'est que beaucoup des affirmations les plus populaires reposent sur des hypothèses qui ne tiennent pas. Si les développeurs ne passent pas l'essentiel de leur journée à coder, combien un assistant de coding peut-il vraiment changer ? Si votre dashboard suit les "lignes de code générées par IA", que mesure-t-il réellement ?

Dans un récent article d'ACM Queue, des chercheurs en productivité de premier plan (dont des co-auteurs du framework SPACE) examinent huit des mythes les plus persistants sur la GenAI en génie logiciel. Ils s'appuient sur de grandes études récentes, dont une étude Microsoft 2025 de plus de 450 ingénieurs, des entretiens de développeurs, et une synthèse de recherches de terrain.

- **Mythe 1 : les développeurs passent l'essentiel de leur temps à écrire du code.** Une étude Microsoft 2025 a trouvé qu'ils passent seulement ~14 % de leur temps à coder, des recherches antérieures montrant 18 % un "bon" jour et 11 % un "mauvais". L'essentiel de la journée va aux réunions, au design, à la revue de code et à la collaboration.

- **Mythe 2 : écrire du code est le goulot.** Si le coding est ~15 % de la journée, même un assistant qui double la vitesse de coding apporte moins de 15 % de gain global. Accélérer la création de code déplace souvent la pression vers la revue, les tests et l'intégration, laissant l'"outer loop" du développement largement inchangé.

- **Mythe 3 : les lignes de code sont la meilleure mesure de l'impact IA.** Une étude de 2014 a trouvé que les LoC "échouent aux tests de validité spécifiés et ont donc une utilité limitée", pourtant des organisations (dont Microsoft publiquement) suivent désormais les LoC générées par IA. Les métriques de volume encouragent le gaming, érodent la confiance et récompensent plus de code plutôt qu'un meilleur logiciel.

- **Mythe 4 : l'IA aide toutes les tâches et tous les ingénieurs également.** La recherche Microsoft 2024 a trouvé que les tâches familières voient des gains Copilot plus grands que les non-familières, tandis qu'une étude 2025 de développeurs open source expérimentés a trouvé que les outils IA augmentaient en réalité le temps d'implémentation de 18 %. Même réécrire un prompt de façon sémantiquement équivalente changeait le code généré dans 46 % des cas et changeait la correction dans 28 %.

- **Mythe 5 : l'IA transformera les individus en 10x developers.** Le gain de productivité de 55 % souvent cité vient d'études contrôlées sur des tâches isolées et survit rarement au contact du travail réel en équipe. Une grande partie de la variation de performance est attribuable à la tâche elle-même, pas à l'individu.

- **Mythe 6 : c'est à chaque développeur de faire marcher l'IA.** L'article invoque Cal Newport : les sauts de productivité historiques venaient de refontes systémiques comme la chaîne de montage, pas du fait de donner aux individus de meilleurs outils. La GenAI est déployée à l'inverse, avec des millions en licences et un minimum de guidance organisationnelle.

- **Mythe 7 : les outils IA performants seront adoptés automatiquement.** Si 80 % des développeurs utilisent des outils IA, seuls 29 % font confiance à la précision de la sortie, et beaucoup rapportent passer plus de temps à déboguer la sortie IA qu'à écrire le code eux-mêmes. La recherche documente aussi une "pénalité de compétence", où les développeurs (surtout les femmes et les ingénieurs plus âgés) reçoivent des évaluations plus dures pour un travail assisté par IA, même à sortie identique.

- **Mythe 8 : les entreprises peuvent innover à la vitesse d'une startup avec la GenAI.** Les startups construisent sur des frameworks open source bien représentés dans les données d'entraînement, tandis que les stacks d'entreprise reposent sur des outils propriétaires, du code legacy et des exigences de rétrocompatibilité que les modèles n'ont jamais vues.

Le fil reliant ces mythes : la valeur de la GenAI vient de comment elle est déployée, mesurée et soutenue, pas de l'accès à l'outil. Les leaders qui traitent le déploiement IA comme une décision d'achat obtiendront des résultats de décision d'achat.

**Comment les leaders peuvent appliquer ces résultats :**

- **Auditer les 86 % avant d'optimiser les 14 %.** Avant d'ajouter une métrique d'usage ou d'acheter plus de sièges, cartographiez où va réellement le temps de votre équipe pendant une semaine. Les plus grandes améliorations de livraison vivent presque toujours dans les files de revue de code, les discussions de design, le setup d'environnement et les réunions — pas dans les frappes économisées.
- **Pointer l'IA sur un goulot de l'outer loop et mesurer la métrique de livraison, pas l'outil.** Choisissez une phase lente (délai de revue, temps d'onboarding, triage de tests flaky), posez une baseline, déployez l'IA délibérément, et suivez le résultat qui compte (cycle time, taux d'échec de changement, temps jusqu'à la première PR).
- **Combler le déficit de confiance avant de chercher le gain de productivité.** Lancez un court sondage sur où la sortie IA a coûté du temps, où les ingénieurs revérifient à la main, et où ils évitent l'outil. Utilisez les réponses pour fixer des conventions explicites : quels types de tâches sont éligibles à l'IA, quel niveau de revue s'applique au code assisté par IA, et comment les managers pèseront équitablement le travail assisté par IA pour éviter la pénalité de compétence.

## Pourquoi ça compte

C'est le contrepoint research-driven indispensable au hype : huit mythes démontés avec des études à grande échelle, et trois actions concrètes pour les leaders qui veulent mesurer la vraie valeur de la GenAI plutôt que des lignes de code.
