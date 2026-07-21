---
title: "Coding too fast to collaborate | Chris Loy"
date: 2026-07-20
url: https://chrisloy.dev/post/2026/07/19/coding-too-fast-to-collaborate
authors: [chrisloy.dev, Chris Loy]
keywords: [collaboration, agents de code, revue de code, product management, partage de connaissance]
theme: Tech
tone: opinion
used_in: ["2026-07-20"]
---

## Résumé

L'ingénierie logicielle est une discipline collaborative, dont l'équilibre repose sur des pratiques évoluées au fil des décennies. Chris Loy identifie trois de ces pratiques bousculées par les agents de code IA : la conception technique court-circuitée par le dialogue avec l'agent, le backlog produit asséché par une capacité d'ingénierie devenue quasi illimitée, et la revue de code transformée en nouveau goulot. Son avertissement : ne confondons pas chaque pratique collaborative avec de la paperasse inutile, car ces rituels ne servaient pas qu'à la qualité — ils distribuaient la connaissance dans l'équipe.

## Points clés

- La collaboration en ingénierie opère à trois points : entrée (spécification produit), sortie (livraison) et interne (design, revue).
- Désintermédiation du design : les ingénieurs dialoguent avec leur agent plutôt qu'avec leurs collègues, contournant les processus de conception collaborative.
- Famine de produit (product starvation) : la capacité d'ingénierie n'étant plus le goulot, le backlog produit se vide et l'implémentation charge avec une spécification minimale.
- Saturation de la revue : la revue de code humaine devient le nouveau goulot ; l'automatiser retire le double rôle de contrôle qualité ET de partage de connaissance.
- Les modèles IA partagent des angles morts similaires, ce qui fragilise la qualité sur les domaines nouveaux.
- Ne pas prendre chaque pratique collaborative pour de la friction inutile : elles cultivent l'expertise collective et réduisent le bus factor.

## Analyse approfondie

L'ingénierie logicielle est une discipline collaborative, dans laquelle un ingénieur seul travaille typiquement en étroite relation avec d'autres au sein d'une équipe transverse. La collaboration se produit au point d'entrée (spécification produit), de sortie (livraison de logiciel fonctionnel à l'entreprise) et en interne (pratiques d'équipe qui améliorent la qualité, la supportabilité et la maintenabilité du logiciel).

Des exemples courants de ce dernier point incluent les discussions intra-équipe autour de la conception technique et la revue par les pairs du code avant déploiement. Les organisations d'ingénierie logicielle ont fait évoluer un ensemble de pratiques qui maintiennent ces forces concurrentes en équilibre.

Comme je l'ai écrit précédemment, l'IA générative bouleverse la façon dont les ingénieurs produisent du logiciel, notamment en permettant à d'autres de le faire avec un degré de connaissance technique bien moindre qu'auparavant. Mais même dans des équipes d'ingénieurs expérimentés, l'impact de l'IA sur le fonctionnement d'une équipe va bien au-delà de l'accélération de l'écriture du code.

Les pratiques de collaboration sont renversées par des agents de code IA qui brouillent la ligne entre outil et collaborateur, et modifient fondamentalement les pratiques intra-équipe. Considérons trois déplacements qui se produisent dans les équipes aujourd'hui.

### Désintermédiation de la collaboration de conception technique

Il existe un large spectre de pratiques pour faire de la conception technique un processus collaboratif au sein des équipes d'ingénierie. Elles vont du très informel (discussions de standup, rubber ducking, fils Slack sans fin) au formalisé (revues de conception technique, ADR, backlog grooming), de l'exploratoire (whiteboarding, prototypage) à la livraison collaborative directe (pair programming).

Toutes ces formes de collaboration se produisent pendant l'étape d'implémentation du cycle de vie logiciel. Et toutes sont progressivement remplacées par des ingénieurs conversant directement avec leurs agents de code IA plutôt qu'avec leurs collègues. Une adoption naïve conduit à contourner ces processus de conception, car chaque ingénieur est incité à supprimer la paperasse de son processus et à se concentrer sur une livraison plus rapide.

Bien sûr, c'est entièrement par conception : les agents de code sont bâtis pour être conversationnels, si bien qu'en les utilisant il est difficile d'éviter de glisser d'un schéma d'interaction instructif vers un schéma inquisiteur. Mais comme pour le piège de la sur-dépendance à l'IA pour écrire du code, traiter votre agent à la fois comme architecte et pair au détriment de parler à vos coéquipiers ne donnera qu'un gain à court terme, tout en abîmant la capacité de l'équipe à faire croître son expertise collective.

### Famine des exigences produit

Un product manager a typiquement un rôle large et varié, servant d'interface entre de nombreuses fonctions de l'entreprise, dont la stratégie, le service client, la technologie, le design et le juridique, entre autres. La fonction est généralement responsable de recueillir puis de spécifier les exigences, c'est-à-dire une liste de choses que le logiciel devrait faire, et pour les équipes d'ingénierie le PM tend à être le représentant du "client".

La complexité de ce rôle implique un outillage étendu, et une grande partie du travail est recherche, stratégie et construction de consensus, menée par la collaboration humaine. De ce fait, alors que l'outillage IA commence à mûrir, les product managers ne connaissent pas encore le bond d'un ordre de grandeur dans la vitesse de livraison potentielle qui est disponible pour les équipes d'ingénierie.

Comme la capacité d'ingénierie n'est plus un goulot, certaines équipes commencent à connaître une famine de produit : un assèchement complet du backlog d'exigences, et l'établissement d'un nouvel équilibre dans lequel seule une spécification minimale est fournie à l'équipe avant que l'implémentation ne charge en avant, menant à des pratiques de développement plus fragmentées et itératives.

Certaines équipes ont embrassé cela en déplaçant la phase de conception exploratoire dans la phase d'ingénierie, et en encourageant les équipes à démarrer le processus de développement en sautant directement à la construction de prototypes. Que ce soit là, ou d'autres adaptations de processus, la formule gagnante, reste à voir.

### Saturation de la capacité de revue de code

Alors que la famine de produit vient de l'excès de demande produit par des équipes d'ingénierie accélérées, il y a aussi un impact de l'excès d'offre correspondant pour le processus en aval du code. Dans la plupart des équipes, c'est la revue de code, dans laquelle des pairs de l'équipe relisent le code des uns et des autres pour la correction, la lisibilité et d'autres mesures de qualité.

Une pratique de revue est fondamentale dans la plupart des équipes d'ingénierie, car elle sert un double objectif important : elle fournit une porte imposée pour le contrôle qualité du logiciel, et elle inscrit le partage de connaissance latéral dans les opérations quotidiennes, réduisant le risque de bus factor lié à la connaissance cloisonnée dans la tête d'un seul ingénieur.

Ces deux objectifs sont difficiles à atteindre en utilisant des revues automatisées par IA qui retirent l'humain de la boucle. La qualité est à plus haut risque, en particulier dans les domaines nouveaux où différents modèles IA sont susceptibles d'exhiber des angles morts et des biais similaires. De plus, bien sûr, tout processus qui omet la supervision humaine dégradera évidemment le partage de connaissance, en supprimant le besoin pour quiconque d'autre que l'auteur de lire le code.

De ce fait, beaucoup d'équipes choisissent de continuer à utiliser un processus de revue mené par des humains, pour conserver à la fois la porte de qualité et la croissance de l'expertise collective. La revue devient alors le nouveau goulot de livraison, et une proportion croissante du temps d'ingénierie doit y être consacrée.

### Trouver un nouvel équilibre

Les agents de code IA ont perturbé l'équilibre délicat des équipes d'ingénierie, en augmentant dramatiquement le rythme auquel chaque ingénieur peut produire du code, mettant une énorme pression sur les pratiques d'équipe existantes. De nouvelles pratiques émergeront inévitablement en réponse, mais alors que nous expérimentons de nouvelles façons de travailler, nous devrions veiller à ne pas prendre chaque pratique collaborative pour de la paperasse ou une friction inutile.

Les organisations d'ingénierie logicielle ont fait évoluer leurs pratiques de collaboration sur des décennies, équilibrant non seulement les demandes concurrentes de vitesse et de qualité, mais aussi le besoin de distribuer la connaissance à travers l'équipe. Cette distribution de la connaissance permet aux équipes de bâtir une expertise collective plus large que ce qu'un seul ingénieur pourrait posséder, tout en restant profonde et pertinente pour chaque entreprise et ses problèmes uniques.

Alors que nous développons de nouvelles pratiques d'équipe qui nous permettent de capturer plus pleinement les bénéfices de l'IA, nous devons aussi veiller à ne pas perdre notre capacité à collaborer efficacement les uns avec les autres.

## Pourquoi ça compte

C'est la dimension humaine et organisationnelle du code IA que les métriques ignorent : en accélérant l'individu, l'IA fragilise les rituels collectifs qui distribuaient l'expertise. Un rappel essentiel pour les leads qui redessinent leurs pratiques d'équipe.
