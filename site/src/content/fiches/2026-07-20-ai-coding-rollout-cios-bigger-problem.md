---
title: "The AI coding rollout worked. Now CIOs have a bigger problem"
date: 2026-07-20
url: https://www.informationweek.com/machine-learning-ai/the-ai-coding-rollout-worked-now-cios-have-a-bigger-problem
authors: [informationweek.com, Stephanie Overby]
keywords: [DSI, productivité, gouvernance, développeurs juniors, cycle de vie logiciel]
theme: Leadership
tone: news
used_in: ["2026-07-20"]
---

## Résumé

Le déploiement des outils de code IA a réussi — 84 % des développeurs les utilisent — mais les gains de productivité plafonnent autour de 10 %. Ce plateau est le symptôme d'un déplacement plus profond : le métier de développeur passe de l'écriture de code à la conception, la revue et le jugement. Les DSI font face à trois défis : mesurer les bons indicateurs (résultats business, pas activité), gérer une bombe à retardement sur la formation des juniors, et déplacer la gouvernance au centre du cycle de vie logiciel.

## Points clés

- 84 % des développeurs utilisent l'IA, mais la productivité plafonne à ~10 % (étude DX Research 2026).
- La compétence rare n'est plus d'écrire du code, mais de savoir quoi construire, comment l'architecturer et si c'est sécurisé.
- Les métriques standards (sièges, tokens, lignes de code) mesurent l'activité, pas les résultats ; privilégier cycle time, fréquence de déploiement, taux d'échec, défauts échappés.
- GitClear : le churn de code a presque doublé (2020-2024) et le refactoring est tombé de 25 % à moins de 10 % ; les PR IA prennent 4,6× plus de temps à relire (+15-18 % de vulnérabilités).
- La "bombe à retardement junior" : l'IA absorbe le travail routinier qui formait les juniors ; couper les postes d'entrée est une "porte à sens unique".
- La gouvernance passe de la marge au cœur du métier : superviser tout le cycle de vie, pas ligne par ligne.

## Analyse approfondie

Les chiffres devraient troubler tout DSI ayant approuvé un déploiement de code IA en espérant une manne de productivité.

Quelque 84 % des développeurs utilisent ou prévoient d'utiliser des outils d'IA, selon la [dernière enquête publiée de Stack Overflow](https://survey.stackoverflow.co/2025) auprès de plus de 49 000 développeurs. Pourtant, les gains de productivité ont plafonné autour de 10 %, selon une étude 2026 de la plateforme d'intelligence développeur DX Research, alors même que 93 % des 121 000 développeurs sondés se tournent vers l'IA.

Les chiffres de productivité ne racontent qu'une partie de l'histoire. Ils sont le symptôme d'un déplacement plus profond : l'IA ne change pas seulement la vitesse à laquelle le logiciel est construit. Elle change ce que font les développeurs, la façon dont les équipes sont structurées et — de la manière la plus lourde de conséquences — la façon dont la prochaine génération d'ingénieurs apprend le métier.

Kai Chuang, DSI de Circles, dit l'avoir constaté de première main : le travail de ses développeurs s'est déplacé du code manuel vers la conception et l'architecture système. Les développeurs de ce prestataire de services d'hospitalité en entreprise passent moins de temps "sur la programmation littérale" et davantage à spécifier quoi construire et à tester si ça marche. Le rythme du changement l'a pris de court. Une fois que les développeurs ont commencé à faire confiance aux sorties, "le basculement vers une génération de code quasi entièrement par IA s'est produit rapidement de lui-même", sans mandat descendant.

La compétence rare n'est plus d'écrire du code. Erik Brown, senior partner du cabinet de conseil West Monroe, explique : "C'est de savoir ce qu'il faut construire, comment l'architecturer, si c'est sécurisé, et si ça fait vraiment avancer le résultat business."

Plutôt que d'écrire simplement plus de code, "les entreprises qui réussiront redessineront le cycle de vie du développement logiciel autour de l'IA. Celles qui se contentent de donner des outils aux développeurs obtiendront plus d'activité, pas nécessairement de meilleurs résultats", dit Brown.

### Les développeurs deviennent concepteurs et relecteurs

Une nouvelle division du travail est déjà la norme chez UiPath, entreprise de logiciels d'automatisation, où "bien plus de la majorité du code déployé en production est déjà écrit par des agents de code", dit le directeur technique et produit Raghu Malpani.

"Les développeurs se transforment d'écrivains de code en relecteurs et concepteurs de systèmes. Ils définissent l'intention, valident les sorties et expédient plus de code, plus vite", au lieu d'écrire chaque ligne. Il appelle cela "un déplacement d'une des parties centrales de l'identité du développeur".

Quand le code n'est plus l'étape lente, le goulot remonte vers la conception, que l'IA remodèle aussi. Cela impose de nouvelles exigences aux analystes métier et aux product managers pour rendre les concepts "prêts à pelleter", dit Chuang. Utiliser l'IA pour explorer les cas d'usage et maquetter les interfaces avant d'impliquer les développeurs permet de "livrer un design bien meilleur et plus abouti".

### Au-delà des métriques de productivité

Si la productivité semble plate, les DSI devraient d'abord se demander s'ils mesurent les mauvaises choses. Prenez ce qu'a trouvé Cornerstone Research, cabinet de conseil économique et financier qui accompagne des litiges à fort enjeu. Sur plus d'un million d'enregistrements de temps facturable, "la réponse jusqu'ici est essentiellement : aucun changement", dit le directeur technique et innovation Phil Leslie. Mais cette conclusion, bien qu'exacte, est aussi trompeuse.

"L'usage de l'IA n'a pas réduit de manière mesurable la part d'heures des analystes", dit Leslie. "Mais ce qu'il a fait, c'est déplacer le mix : les analystes rapportent moins de temps sur le code et le débogage, et plus sur l'interprétation, la méthodologie et la réflexion. Le métier a une autre sensation, même si les heures n'ont pas bougé."

Certaines organisations rapportent des gains de productivité nettement plus importants avec le code assisté par IA. Même là, cependant, les dirigeants technologiques soutiennent que les gains de productivité ne sont pas le changement le plus important.

Chez Bank of America, par exemple, qui investit près de 14 milliards de dollars par an dans la technologie, l'assistance au code par IA utilisée par plus de 18 000 développeurs génère des gains d'efficacité de plus de 20 %, selon l'entreprise. Mais la vitesse brute n'est pas le point, dit Hari Gopalkrishnan, directeur technique et information de la banque.

"Le besoin de personnes talentueuses capables de résoudre des problèmes complexes, d'exercer un jugement et de construire des relations restera critique", dit Gopalkrishnan.

#### Métriques d'activité vs. résultats business

La plupart des métriques standards de code IA comptent encore l'effort plutôt que les résultats : sièges déployés, tokens consommés, lignes de code générées, heures économisées auto-déclarées. "Ce sont des métriques d'activité", dit Brown de West Monroe. "La meilleure question est de savoir si les résultats business et ingénierie ont bougé."

Brown recommande un tableau de bord qui ne ressemble en rien à un compteur de tokens et qui suit le cycle time de l'idée à la production, la fréquence de déploiement, le taux d'échec des changements, les défauts échappés, les vulnérabilités de sécurité et la part de code généré par IA nécessitant une correction humaine substantielle. "L'objectif n'est pas plus de code", dit-il. "C'est une livraison plus rapide, plus sûre et de meilleure qualité, liée aux résultats business."

Les données montrent pourquoi la qualité compte. L'analyse par GitClear de 211 millions de lignes de code a révélé que le churn de code a presque doublé entre 2020 et 2024, tandis que le refactoring est tombé de 25 % à moins de 10 %. Un benchmark 2026 de la firme de livraison logicielle Opsera a constaté que les pull requests générées par IA prennent 4,6 fois plus de temps à relire et contiennent 15 à 18 % de vulnérabilités de sécurité en plus que le code écrit par des humains. Le temps économisé à écrire du code réapparaît souvent plus tard dans les files de revue et les corrections de sécurité.

### La bombe à retardement des développeurs juniors

Le risque le plus sérieux n'apparaîtra toutefois pas dans les métriques de cette année. Il se tapit deux ou trois ans plus loin. Le travail routinier que l'IA absorbe désormais — corrections de bugs, documentation, couverture de tests — était exactement la façon dont les développeurs juniors aiguisaient leurs compétences. Retirez cela "sans un nouveau modèle d'apprentissage pour le remplacer, et les entreprises créeront un déficit de talents deux ou trois ans plus tard", avertit Brown.

Couper les postes de niveau débutant sur la théorie que l'IA remplacera les juniors est "presque une porte à sens unique", prévient Leslie de Cornerstone Research. "Le modèle d'apprentissage est la façon dont presque tous les métiers cultivent le jugement sur lequel leurs seniors finissent par s'appuyer."

La solution n'est pas d'arrêter d'embaucher des juniors mais de redéfinir le rôle. Les meilleurs développeurs en début de carrière "ne sauront pas seulement écrire du code — ils sauront poser les bonnes questions, comprendre l'intention business derrière le logiciel, et évaluer si la sortie générée par IA résout réellement le problème", dit Brown.

Le calcul d'embauche change aussi. Chuang dit qu'il favorise désormais les développeurs "plus interdisciplinaires et intéressés par la résolution de problèmes business sous-jacents". Malpani d'UiPath ajoute qu'à mesure que le code devient moins cher, "le jugement de quoi coder et comment devient un actif de valeur", la prime allant aux développeurs qui comprennent la conception système et savent garder les automatisations "sécurisées, conformes et maintenables dans le temps".

### La gouvernance passe au centre

À mesure que le code généré par IA prolifère, la supervision se déplace des marges vers le cœur du métier. "L'accent passe de la relecture de chaque ligne de code écrit à la main à la gouvernance de tout le cycle de vie logiciel : tests, déploiement, permissions, auditabilité et comportement à l'exécution", dit Malpani.

"Les entreprises auront besoin de plateformes offrant une supervision, un contrôle et une traçabilité cohérents, quel que soit l'agent de code ayant produit le code", dit-il, insistant sur le fait que les agents "ont besoin de garde-fous et de relecteurs expérimentés".

C'est une leçon contre-intuitive. Les agents de code "n'ont pas éliminé le besoin de plateformes low-code ou d'entreprise", dit Malpani. "Ils les ont rendues plus précieuses. Une génération de code plus rapide augmente le besoin de revues, de jugement, de gouvernance et de collaboration."

La vitesse fait partie du gain. Mais la pleine valeur des outils de code IA ne se matérialise que lorsque le travail autour du développement logiciel change — comment les équipes sont bâties, comment le travail est mesuré et comment la prochaine génération apprend à juger ce que les machines produisent.

## Pourquoi ça compte

C'est le point de vue DSI qui complète le tableau : si le modèle est devenu une commodité, le vrai chantier est organisationnel — mesure, formation, gouvernance. Le déploiement d'outils ne suffit pas, il faut redessiner le cycle de vie.
