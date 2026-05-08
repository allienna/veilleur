---
title: "Tokenmaxxing, Promomaxxing, and Misaligned Incentives in Tech"
date: 2026-05-08
url: https://read.engineerscodex.com/p/tokenmaxxing-promomaxxing-and-misaligned?utm_source=tldrnewsletter
authors: [Engineer's Codex, Leonardo Creed]
keywords: [tokenmaxxing, Goodhart's Law, incentives, AI productivity, layoffs]
theme: Leadership
tone: opinion
used_in: ["2026-05-08"]
---

## Résumé

L'auteur analyse comment l'usage des tokens IA devient un proxy de productivité — et comment ce proxy se transforme immédiatement en incentive perverse. Coinbase pousse ses employés à "tokenmaxxer" après des layoffs, Meta a dû fermer un leaderboard interne quand des ingénieurs se sont mis à brûler des millions de tokens via des scripts pour rien. Goodhart's Law en action : "quand une mesure devient une cible, elle cesse d'être une bonne mesure". L'auteur trace le parallèle avec le _promomaxxing_ chez Google, où les ingénieurs créaient de la complexité artificielle pour obtenir leur promotion.

## Points clés

- Coinbase a annoncé des layoffs en demandant aux survivants d'utiliser plus l'IA ("tokenmaxxer")
- Meta a créé puis fermé un leaderboard interne de consommation de tokens, gamifié dans la minute
- Des ingénieurs ont écrit des scripts qui brûlaient des millions de tokens pour zéro productivité
- Goodhart's Law : toute métrique convertie en target finit par être gamée
- Parallèle direct avec le _promomaxxing_ Google : complexité artificielle pour justifier les promotions
- Cobra Effect en Inde : récompense pour cobras tués → élevage de cobras pour primes → relâchage massif quand le programme s'arrête

## Analyse approfondie

Engineer's Codex est une publication sur le software engineering du monde réel.

Coinbase a fait des layoffs récemment. Ils coupent une part importante de leurs employés, et au passage, ils mentionnent vouloir que leurs employés utilisent l'IA davantage. En gros, ils veulent que les gens tokenmaxxent.

**Si tu ne sais pas ce qu'est le tokenmaxxing, c'est l'idée de maximiser le nombre de tokens que tu utilises quand tu travailles avec l'IA. Basiquement, utilise beaucoup l'IA !** Et c'est généralement vu comme une bonne chose. Plus tu utilises de tokens, plus tu es productif, en théorie.

Ce n'est pas toujours vrai.

Meta a effectivement créé un leaderboard interne qui comptait la quantité de tokens consommés par chacun. Tu pourrais penser que les gens qui consomment le plus de tokens sont généralement les plus productifs.

Mais voici le problème : tout ce qui est mesuré _peut et sera_ gamé (**Goodhart's Law : "Quand une mesure devient une cible, elle cesse d'être une bonne mesure".**), surtout par des gens malins et pragmatiques, comme les ingénieurs Meta. Les ingénieurs malins optimisent pour les meilleurs outcomes personnels, ce qui signifie souvent une promotion, plus d'argent, plus de scope. Si tokenmaxxer est le chemin pour y arriver, ils le feront (plus de visibilité, un nombre plus élevé est bien vu).

Donc les gens se sont mis à monter des scripts pour brûler des millions de tokens pour littéralement zéro productivité. Juste brûler des tokens à ne rien faire. Meta a fini par fermer le leaderboard parce qu'il créait la mauvaise incentive.

Le tokenmaxxing me rappelle en réalité une plainte célèbre à propos de Google : à savoir, à quel point il est dur d'y obtenir une promotion et comment ça a mené à beaucoup d'incentives mal alignées. Tu pourrais appeler ça **promomaxxing**.

Les Googlers rendaient les choses plus complexes que nécessaire, écrivaient bien plus de docs que nécessaire, et faisaient ces docs bien plus longues que nécessaire, le tout pour fabriquer l'apparence d'un travail dur et complexe. Parce que chez Google, si ton projet n'était pas assez techniquement complexe ou s'il n'y en avait pas assez, tu n'obtenais pas ta promo.

En théorie, ça a du sens. Les gens qui sont promus devraient faire des choses de plus en plus dures.

Cependant, la bonne ingénierie logicielle devrait pencher vers la simplicité. Mais la promotion récompense la complexité. Et alors que les frameworks et l'infrastructure dev rendent l'ingénierie plus simple (ce qui est génuinement bien), les ingénieurs manquent de complexité adéquate pour justifier leurs promotions. Donc tu obtiens ces décisions irrationnelles pour le business mais complètement rationnelles pour l'individu. C'est un cas d'école d'incentive mal alignée.

L'exemple le plus célèbre auquel je pense dans l'histoire des incentives perverses, c'est le Cobra Effect en Inde.

Pendant la Raj britannique en Inde, le gouvernement était préoccupé par le nombre de cobras venimeux à Delhi. Ils ont mis en place une prime pour chaque cobra mort. Initialement, c'était une stratégie efficace : un grand nombre de serpents ont été tués pour la récompense. Cependant, des gens entreprenants ont commencé à élever des cobras pour le revenu. Quand le gouvernement s'en est rendu compte et a annulé la prime, les éleveurs ont relâché leurs cobras désormais sans valeur, et la population sauvage a explosé.

Le tokenmaxxing peut suivre la même trajectoire. Les boîtes voient les tokens comme un proxy de productivité, donc elles l'optimisent. Les ingénieurs malins optimisent en retour, parfois de façon honnête, parfois pas. Quand la mesure perd son sens, on ne revient pas à l'état initial : on hérite des comportements adaptés à la mauvaise mesure.

La leçon n'est pas "ne mesurez rien". C'est "ne confondez jamais le proxy avec la valeur". La productivité, ce n'est pas la consommation de tokens — c'est le code qui marche, qui est maintenu, qui résout un problème. Si tu mesures la consommation, tu obtiens de la consommation. Si tu mesures la valeur livrée, c'est plus dur, mais c'est ce que tu veux vraiment.

## Pourquoi ça compte

Pour un manager, cet article est un rappel salutaire avant de mettre en place des dashboards de "AI usage" : la métrique que tu choisis va devenir un comportement. Mieux vaut investir dans des indicateurs de valeur livrée (incidents, time-to-merge, qualité) que de compter des tokens consommés.
