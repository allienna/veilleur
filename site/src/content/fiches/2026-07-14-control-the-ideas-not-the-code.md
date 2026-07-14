---
title: "Control the ideas, not the code"
date: 2026-07-14
url: https://antirez.com/news/169?utm_source=tldrnewsletter
authors: [antirez, Salvatore Sanfilippo]
keywords: [programmation IA, revue de code, design, LLM, impact développeur]
theme: IA
tone: opinion
used_in: ["2026-07-14"]
---

## Résumé

Salvatore Sanfilippo (antirez, créateur de Redis) soutient que de nombreux programmeurs ont aujourd'hui moins d'impact qu'ils ne le pourraient parce qu'ils continuent à regarder le code. Son argument : si vous contrôlez les idées de votre logiciel, scruter le code lui-même est sous-optimal et souvent inutile. Ce n'est pas un plaidoyer pour le « vibe coding » (demander juste le produit final), mais un déplacement du curseur d'attention vers le design et l'intention. Il assume ce discours par empathie pour les développeurs, souvent plus jeunes, désarçonnés par le changement.

## Points clés

- Beaucoup de programmeurs ont moins d'impact qu'ils ne le pourraient parce qu'ils se focalisent sur le code.
- On peut générer énormément de code : relire 5 000 lignes par jour est impraticable.
- Les LLM écrivent un code localement optimal mais restent plus faibles (bien qu'en progrès) sur les grandes idées et le design d'ensemble.
- Mieux vaut prompter le design que l'on a en tête et interroger le modèle sur sa conception, plutôt que de scanner fonction par fonction.
- La journée fait 8 heures : lire le code est un arbitrage qui vole du temps à la vraie question — que construit-on et dans quelle direction ?
- Ce n'est pas du vibe coding : il ne s'agit pas d'abandonner le contrôle, mais de le déplacer vers les idées.

## Analyse approfondie

Regardez l'historique de ce blog. Il y a de nombreux billets sur la programmation avec l'IA, certains remontant à janvier 2024. Je suis un programmeur relativement bien considéré, après tout. Je n'ai pas besoin de rester « dans la boucle » comme un vieil homme en quête de pertinence : j'ai récemment rejoint Redis, et je développe aussi un nouveau logiciel open source pour l'inférence locale de LLM, qui a reçu un bon accueil dans la communauté. Pourquoi est-ce que je continue à dire ce que les gens ne veulent pas entendre ? Pourquoi est-ce que je continue à annoncer comment sera la programmation future par défaut ? Parce que je ressens l'urgence de réduire l'impact du changement pour les personnes moins préparées que moi, souvent plus jeunes, et qui, contrairement à moi, n'ont pas vu venir beaucoup de ces choses. (En 2022, avant l'existence de ChatGPT, j'ai publié un livre préannonçant beaucoup de choses qui se sont depuis produites, et d'autres qui, je crois, se produiront ; je peux donc dire cela sans avoir l'air égocentrique.)

Alors la mienne est une ruse. Les gens sentent de plus en plus que la programmation est complètement modifiée par l'IA et ne savent pas ce qu'ils devraient faire — s'ils peuvent vraiment commencer à coder d'une manière complètement différente, sans trop regarder le code comme leur principal produit. Ils ont l'impression de trahir leur propre domaine. Mon intention est donc d'arriver et de dire : « regardez-moi, je sais écrire du code, je ne me cache pas derrière l'IA : et pourtant, les choses ont changé, ce n'est pas votre faiblesse, ce n'est pas que vous êtes AI-pilled. C'est juste que notre domaine évolue dans une direction incroyable et douloureuse (mais aussi joyeuse). »

C'est pourquoi hier, sur X, j'ai dit que je crois que beaucoup de programmeurs ont à ce stade moins d'impact qu'ils ne le pourraient parce qu'ils regardent le code. J'y crois vraiment. Et notez que cela ne signifie pas vibe coder quelque chose en demandant juste le produit final. Le point est : si vous contrôlez les idées de votre logiciel, regarder le code lui-même est sous-optimal et souvent inutile. Pour les raisons suivantes :

1. Vous pouvez désormais générer beaucoup de code, même sans compter la verbosité du code des LLM (qui est aussi l'effet de ne pas savoir bien les instruire, la plupart du temps). Comment êtes-vous censé relire 5 000 lignes de code chaque jour ?

2. Les LLM sont très bons pour écrire du code localement optimal, et moins bons (mais ils s'améliorent) avec les grandes idées. Quel est l'intérêt de scanner fonction par fonction, ligne par ligne ? Au lieu de cela, vous devriez prompter le design que vous avez en tête, parfois demander « comment est exactement le design de cette partie ? Comment fonctionne-t-elle ? », et évaluer si c'est le bon modèle. C'est beaucoup plus rapide.

3. La journée de travail fait 8 heures. Si vous lisez le code, c'est un arbitrage. Vous faites moins de ce qui est aujourd'hui la partie la plus importante de votre travail, à savoir vous demander : qu'est-ce que je fais avec ce logiciel ? Quelles sont les nouvelles directions que je veux [prendre] ?

## Pourquoi ça compte

antirez, figure respectée du monde du code, donne une caution crédible au déplacement du curseur : du code vers les idées. C'est le versant « posture individuelle » du thème du jour, complémentaire des cadres macro (sandwich, économie).
