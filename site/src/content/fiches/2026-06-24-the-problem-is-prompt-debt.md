---
title: "The Problem is Prompt Debt"
date: 2026-06-24
url: https://www.dbreunig.com/2026/06/22/the-problem-is-prompt-debt.html?utm_source=tldrnewsletter
authors: [Drew Breunig, dbreunig.com]
keywords: [prompt debt, system prompts, model agnostic, evals, specification]
theme: IA
tone: opinion
used_in: ["2026-06-24"]
---

## Résumé

Drew Breunig décrit la « dette du prompt » (prompt debt) : le langage naturel rend le prototypage d'applications IA magique, mais c'est un piège pour construire des systèmes fiables. Au fur et à mesure qu'on ajoute des instructions pour corriger des cas limites, le prompt devient illisible, fragile, et verrouille l'application sur un seul modèle. La solution vient des ingénieurs qui utilisent des agents de code : spécifier le comportement par des mesures (évaluations, métriques, specs typées) plutôt que par de la prose, et arrêter d'écrire les prompts à la main.

## Points clés

- Le langage naturel n'a jamais été conçu pour être un langage de spécification d'ingénierie ; le traiter comme tel plafonne discrètement ce qu'on peut construire.
- Trois symptômes : ralentissement de l'itération, équipe paralysée par un prompt illisible, verrouillage sur un seul modèle.
- Le system prompt de Fable répète sa règle de copyright six fois, sous des sections de sévérité croissante (`mandatory_copyright_requirements`, `hard_limits`, `critical_reminders`).
- Le modèle le plus utilisé en trafic observé par Datadog reste GPT-4o : les entreprises restent sur d'anciens modèles parce que les nouveaux cassent leurs agents existants (étude Berkeley).
- Des énoncés sans rapport changent les réponses : préciser pour quelle équipe NFL on supporte modifie le taux de refus du modèle (étude Harvard).
- Remèdes : spécifier par des mesures (evals, métriques, specs typées) ; arrêter d'écrire les prompts à la main et les faire « rechercher » par des systèmes type DSPy ou GEPA.

## Analyse approfondie

### On ne peut pas être agnostique au modèle si on règle les prompts à la main

Grâce aux interfaces en langage naturel, les applications IA peuvent être prototypées rapidement. On écrit ce qu'on veut en anglais, on le donne à un modèle frontière, et un prototype fonctionnel apparaît dans l'après-midi. C'est extraordinairement puissant et, pour des tâches ponctuelles, optimal. Mais comme façon de construire des systèmes fiables, le prompt en langage naturel est un piège.

Le prompt en anglais simple qui rend les prototypes sans effort se révèle être une mauvaise manière de spécifier comment un système doit se comporter, et la facture arrive lentement, déguisée en progrès ordinaire, jusqu'à ce que l'application puisse à peine bouger. Le problème n'est aucun prompt en particulier. C'est que le langage naturel n'a jamais été conçu comme un langage de spécification pour l'ingénierie, et le traiter comme tel plafonne discrètement ce qu'on peut construire.

### Le piège de la dette du prompt

Le premier symptôme est le ralentissement de l'itération. À mesure que les utilisateurs signalent des erreurs et repèrent des cas limites, on ajoute des consignes aux instructions pour aligner le modèle. Si des comportements indésirables persistent, on répète les instructions, avec une sévérité croissante. Bientôt, le prompt n'est plus simple et les correctifs rapides font régresser des instructions précédentes. Les erreurs ne peuvent plus être gérées par des « hot fixes » d'une ligne, et le cycle de développement ralentit jusqu'à l'arrêt.

Le system prompt de Fable répète ses consignes de copyright jusqu'à six fois, sous des sections nommées `search_instructions`, `search_usage_guidelines`, `mandatory_copyright_requirements`, `hard_limits`, `self_check_before_responding` et `critical_reminders`.

Ensuite, la dette du prompt paralyse l'équipe. Le prompt fragile, plein de cas limites et de menaces en majuscules, est à peine lisible pour soi-même, et carrément impénétrable pour les collègues. Beaucoup d'équipes atténuent cela en découpant les prompts en templates complexes assemblés à l'exécution, chacun isolé sur une préoccupation. Mais ces segments évoluent aussi, et deviennent un fouillis de conditions.

Enfin, la dette du prompt lie à un seul modèle. Les hot fixes marchent sur GPT-4o mais échouent de façons inédites quand on pointe l'appel d'inférence vers GPT-5.4-mini. Alors on reste sur 4o, on espère que les e-mails de dépréciation de plus en plus fréquents du fournisseur sont des menaces creuses, et on renonce à des modèles potentiellement moins chers, plus rapides, *meilleurs*. Un rapport récent de Datadog suggère que c'est une situation courante : le modèle le plus utilisé dans le trafic observé est GPT-4o.

L'un de ces problèmes pris isolément est une nuisance ; ensemble, ils font la différence entre un prototype glorifié et un produit capable de grandir avec vous, vos clients et votre activité. Vos belles nouvelles fonctionnalités IA sont gelées, ne peuvent être améliorées que par une reconstruction complète, et sont verrouillées sur un modèle vieillissant.

### Pourquoi la dette du prompt arrive

Les interfaces en langage naturel sont merveilleuses. Elles sont le bon mécanisme pour des tâches ponctuelles et des fils conversationnels larges. On a des ennuis quand on s'appuie sur le langage naturel pour définir un comportement système durable.

L'imprécision du langage naturel, combinée à des modèles probabilistes, fait que des mots différents exprimant la même intention peuvent produire des sorties différentes. Dans une étude récente, une question clinique posée à la voix d'un patient puis reposée à celle d'un médecin, avec des faits identiques, a fait passer Opus du refus systématique (dix fois sur dix) à la réponse systématique (dix fois sur dix).

Et ce n'est pas que le choix des mots. Des énoncés apparemment sans rapport, dans le même prompt, peuvent affecter les résultats. Dans une étude de Harvard, le simple fait d'indiquer pour quelle équipe NFL l'utilisateur supportait changeait la fréquence à laquelle le modèle refusait de répondre sur des sujets sensibles. Les énoncés parasites influencent la passe d'inférence de façons imprévisibles. C'est pourquoi les prompts deviennent plus fragiles à mesure qu'on ajoute des correctifs : une instruction supplémentaire pour étouffer une erreur tenace peut affecter la façon dont le modèle interprète une autre instruction qui marchait hier.

Répéter les instructions nous propulse vers la dette du prompt, mais c'est nécessaire quand le comportement voulu entre en conflit avec l'entraînement du modèle. C'est « combattre les poids » (*fighting the weights*), et une fois qu'on le reconnaît, on le voit partout. Les prompts d'image de ChatGPT instruisaient le LLM huit fois de ne pas répondre quand une image générée était renvoyée, parce qu'il avait été entraîné à toujours poursuivre la conversation. Chaque system prompt d'agent de code analysé contient des instructions répétées, des avertissements sévères et des exigences en majuscules. Claude Code dit sept fois à Opus de renvoyer plusieurs appels d'outils dans une seule réponse.

Pire : ces correctifs sont taillés pour le comportement d'un seul modèle. Une étude menée par Berkeley a trouvé que les entreprises restent sur des modèles plus anciens parce que les plus récents cassent leurs agents existants. Les modèles ne sont pas du logiciel proprement versionné : ils ont des poids différents qui produisent des comportements différents, de façon imprévisible et non documentée. La dette du prompt verrouille une application sur un seul modèle. Notre incapacité à changer facilement de modèle n'est pas le résultat d'un fossé concurrentiel astucieux des labos frontière. C'est le résultat de l'évolution d'une spécification en langage naturel, lossy, contre un modèle probabiliste.

### Prévenir la dette du prompt

Heureusement, pas besoin de théoriser : un domaine a déjà montré la voie. Les programmeurs utilisant des agents de code sont à la pointe de ce que les modèles savent faire. Ces deux dernières années, ils ont fait évoluer des bonnes pratiques qui laissent le modèle écrire plus de code tout en livrant du logiciel maintenable et modulaire.

Premier principe : spécifier le comportement du système par des mesures, pas par de la prose. Quand la sortie du modèle est probabiliste et que le langage est imprécis, on construit des bords durs pour les contraindre : évaluations, métriques, spécifications typées. Ce sont des artefacts lisibles et partagés que les collègues peuvent lire et enrichir, permettant la collaboration que les prompts fragiles empêchaient. Les meilleurs ingénieurs consacrent désormais plus de bande passante aux tests que jamais : ils ne sont plus un filet de sécurité, mais ce qui *laisse le modèle cuisiner*.

Deuxième principe : arrêter d'écrire le prompt à la main. Une fois qu'on a des métriques qui notent les candidats, le prompt n'est plus quelque chose à façonner mais quelque chose à rechercher. La surface des mots, phrases et structures possibles est trop vaste pour y passer des heures humaines. C'est un terrain que les LLM sont faits pour explorer, et il existe déjà des systèmes (comme DSPy et GEPA) qui le font.

## Pourquoi ça compte

La dette du prompt est la version « langage naturel » de la dette technique : invisible au début, paralysante ensuite. L'article relie directement la fragilité des prompts à l'incapacité de changer de modèle — un enjeu stratégique majeur pour toute équipe qui industrialise l'IA.
