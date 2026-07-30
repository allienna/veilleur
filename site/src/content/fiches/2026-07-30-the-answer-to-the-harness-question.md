---
title: "The Answer to the Harness Question"
date: 2026-07-30
url: https://danielmiessler.com/blog/the-answer-to-the-harness-question?utm_source=tldrai
authors: [Daniel Miessler]
keywords: [harness, intent engineering, bitter lesson, context, agents]
theme: IA
tone: opinion
used_in: ["2026-07-30"]
---

## Résumé

Daniel Miessler répond à l'hésitation publique de Martin Casado sur la valeur des harness d'IA. Sa thèse : la question paraît insoluble parce qu'on traite le harness comme une seule chose alors qu'il en contient deux — le WHAT (le contexte de ce que vous voulez) et le HOW (les instructions pour l'obtenir). Ces deux moitiés vieillissent en sens opposés : le HOW pourrit à mesure que les modèles s'améliorent, le WHAT s'apprécie. D'où la conclusion : oui au harness, mais pour votre contexte, en restant hors du chemin du modèle pour l'exécution.

## Points clés

- Martin Casado oscille entre trois croyances contradictoires sur les harness ; Miessler affirme que deux d'entre elles sont vraies, mais sur des moitiés différentes du harness.
- Le HOW (instructions pas-à-pas) pourrit : c'est la Bitter Lesson de Sutton qui se joue dans vos fichiers de config.
- Le WHAT (qui vous êtes, ce que vous construisez, à quoi ressemble « bien ») s'apprécie : un modèle plus intelligent en fait plus, pas moins.
- Les labos peuvent post-entraîner les modèles à être de meilleurs agents, mais ils ne peuvent pas post-entraîner *votre* contexte : il doit être capturé et transmis depuis l'extérieur, à chaque tâche.
- Miessler appelle ce principe de conception l'*Intent Engineering* : capturer ce que l'humain veut réellement, le transmettre au modèle à chaque tâche, et sinon rester à l'écart.

## Analyse approfondie

> Les harness servent à l'intention ; les modèles servent à l'exécution.

Martin Casado a publié quelque chose sur les harness d'IA qui capture exactement là où beaucoup de gens intelligents sont bloqués en ce moment.

> Sur les harness, j'oscille entre trois croyances : moins de harness, mieux c'est. Les modèles sont la magie. Post-entraîner un modèle *et* un harness ensemble est nettement meilleur, et les fournisseurs de modèles gagnent. Les harness ont une valeur réelle indépendante du modèle. Je n'ai aucune idée de laquelle est la bonne. — Martin Casado

Je crois que je peux répondre à ça.

La raison pour laquelle la question semble impossible, c'est que nous traitons le harness comme une seule chose. **C'est en réalité deux choses.** Chaque harness porte un mélange de WHAT et de HOW : du contexte sur ce que vous voulez, et des instructions sur la manière de l'obtenir. Et ces deux moitiés vieillissent dans des directions opposées.

**La moitié HOW pourrit.** C'est la [Bitter Lesson de Sutton](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) qui se joue dans vos fichiers de configuration : plus les modèles deviennent intelligents, plus vos instructions pas-à-pas ont l'air stupides en comparaison. Si votre harness est majoritairement du HOW, alors la première croyance de Martin est la bonne. Moins de harness, c'est mieux, parce que le modèle est la magie.

**La moitié WHAT s'apprécie.** Qui vous êtes, sur quoi vous travaillez, ce que vous cherchez à accomplir, et à quoi ressemble « bien » pour vous. Un modèle plus intelligent fait *plus* avec ce contexte, pas moins. Si votre harness est majoritairement du WHAT, alors sa troisième croyance est la bonne : il a une valeur réelle et indépendante, et cette valeur croît à chaque nouvelle sortie de modèle.

Donc les croyances une et trois sont **toutes les deux justes**. Elles portent simplement sur des moitiés différentes du harness.

La deuxième croyance — que les fournisseurs de modèles post-entraînent le harness dans le modèle et gagnent — a raison sur l'exécution et tort sur l'intention. Les labos peuvent absolument entraîner leurs modèles à être de meilleurs agents, et ils le feront. **Mais ils ne peuvent pas post-entraîner VOTRE contexte dans le modèle.** Ce que vous cherchez à construire, pour qui, avec vos contraintes et votre goût. Cela doit être capturé et transmis depuis l'extérieur, à chaque fois.

C'est à ça que sert le harness. J'appelle ça l'[Intent Engineering](https://danielmiessler.com/blog/intent-engineering), et c'est tout le principe de conception derrière [mon propre harness](https://danielmiessler.com/blog/personal-ai-infrastructure) : capturer ce que l'humain veut réellement, le transmettre au modèle à chaque tâche, et sinon rester hors du chemin.

Donc OUI au harness. Extrêmement puissant. Mais pour votre contexte, en restant hors du chemin du modèle pour l'exécution.

## Pourquoi ça compte

C'est le cadre conceptuel le plus net pour trancher une décision d'architecture qui revient dans toutes les équipes : que met-on dans les fichiers de config, les skills et les prompts système, et que laisse-t-on au modèle ? La règle est actionnable immédiatement — auditez votre harness et supprimez le HOW.
