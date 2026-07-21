---
title: "The LLM Critics Are Right. I Use LLMs Anyway."
date: 2026-07-17
url: https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/
authors: [theocharis.dev]
keywords: [LLM, dissonance, open source, trust, local models]
theme: IA
tone: opinion
used_in: ["2026-07-17"]
---

## Résumé

L'auteur décrit la dissonance qu'il ressent — et qu'il observe partout à la Local-First Conf de Berlin : des ingénieurs lucides critiquent les LLM tout en gardant Claude Code ouvert. Il passe en revue les critiques valides (slop, effondrement de la confiance dans l'open source, disparition des juniors, tensions géopolitiques, biais silencieux) puis explique pourquoi il continue d'utiliser les LLM malgré tout. Sa thèse : les LLM amplifient ce que vous avez déjà. Avec des idées, elles ressortent plus vives et plus vite ; sans idées, il ne sort rien, mais très couramment. La valeur, pour lui, est de faire moins de choses, mais de meilleure qualité.

## Points clés

- La dissonance est partout : les gens applaudissent les critiques des LLM tout en les utilisant à plein.
- Earendil (Pi.dev, un « open-source coding agent harness ») auto-ferme presque toutes les PR/issues pour survivre au flot généré par les LLM. Leur devise : « we believe humans are the best agents ».
- Le vrai problème de l'open source est la confiance : créer une PR ne coûte plus d'effort humain, donc le filtre naturel contre les trolls a disparu.
- Deux effets sur les juniors : on ne peut plus juger l'effort derrière leur code, et les seniors n'ont plus d'incitation à les former.
- Risque géopolitique concret : en juin 2026, une directive d'export control américaine a forcé Anthropic à désactiver Fable 5 et Mythos 5 pour tous les clients étrangers.
- Argument pour les modèles open-weights locaux : ils ne peuvent pas être coupés du jour au lendemain et tiennent les gros vendeurs en respect.

## Analyse approfondie

« Je suis presque d'accord avec tous les critiques des LLM, et pourtant je les utilise beaucoup. Je sais que ça sonne comme du déni, et je le ressens parfois moi-même à cause de cette dissonance, mais je ne pense pas être seul. »

Cette semaine, l'auteur était à la Local-First Conf de Berlin, où la dissonance était partout. Armin Ronacher — créateur de Flask, membre des débuts de Sentry, fondateur d'Earendil qui construit Pi.dev, un « open-source coding agent harness » — venait de donner une conférence. Interrogé en direct sur la manière dont ils gèrent le flot de PR issues des LLM, il a répondu qu'ils auto-ferment quasiment toutes les PR et issues, tout en encourageant à en ouvrir « parce que l'humain finira toujours par transparaître ». Sur la page « purpose » d'Earendil : « In a world hurtling towards AI, we believe humans are the best agents. » Encore la dissonance.

Dans la salle, beaucoup avaient Claude Code ouvert. Et quand les orateurs critiquaient les LLM, ils recevaient de grandes salves d'applaudissements — y compris de ceux qui avaient Claude Code ouvert.

### Les LLM, c'est mauvais

L'auteur est d'accord avec presque tous les points des détracteurs : matériaux sous copyright, impact environnemental, problèmes éthiques, et ce « circle-jerk » financier NVIDIA/OpenAI qui finira mal — une bulle qui va éclater.

**Le slop.** Oui, les LLM produisent beaucoup de contenu de mauvaise qualité. De plus en plus de projets open source refusent toutes les contributions ou installent des filtres — comme l'auto-fermeture d'Earendil. Le cœur du problème est la confiance. Avant les LLM, produire une PR correcte demandait du temps humain, ce qui écartait naturellement les trolls et les contributions de faible qualité. Ce socle n'existe plus : n'importe qui crée un compte GitHub et lâche son LLM. Des projets comme Zig ou Gentoo refusent déjà les PR générées par LLM (ce qui n'est pas une solution selon l'auteur : comment le savoir ?). Il pense que les LLM pourraient sérieusement tuer l'open source si on ne restaure pas cette confiance — une idée serait de ne laisser contribuer qu'un petit ensemble de personnes vérifiées, la vérification passant par une rencontre physique.

**Les juniors.** Deux problèmes : (a) on ne peut plus se fier à l'effort derrière le code d'un junior — a-t-il vibecodé en 10 minutes ou passé des heures sans les bonnes intuitions ? (b) Les seniors n'ont plus d'incitation à former les juniors : les tâches banales qu'on leur confiait pour les faire grandir peuvent désormais être externalisées à un LLM. Alors pourquoi embaucher des juniors ?

**La géopolitique.** Que se passe-t-il si la Chine ou les États-Unis nous coupent du jour au lendemain de ces technologies ? Quelques semaines plus tôt, le gouvernement américain a montré qu'il en était capable : une directive d'export control a forcé Anthropic à désactiver brutalement Fable 5 et Mythos 5 pour tous les clients étrangers (déclaration d'Anthropic du 12 juin 2026). Comme le disait Martin Kleppmann sur scène : « la probabilité d'un conflit entre l'Europe et les États-Unis reste très faible. Mais l'an dernier, elle était nulle. »

**Le biais silencieux.** Même en recherche, les LLM glissent silencieusement les idées majoritaires de leurs données d'entraînement, parfois les convictions politiques de leurs créateurs. C'est comme deux humains qui discutent : leurs opinions finissent par converger — sauf qu'ici, l'un des participants n'est pas humain.

### Les LLM, c'est bon

On ne peut plus les faire disparaître. Ils sont là pour rester. Plutôt que de lutter contre le courant, on peut aller avec, puis le contrôler et le façonner. Par exemple en veillant à ce que des modèles tournent sur son laptop : ils s'améliorent, rendent les programmeurs indépendants des grandes entreprises, et quand les subventions cesseront et que les prix monteront, ce sont les modèles open-weights qui tiendront les gros vendeurs en respect. Un modèle local ne peut être coupé du jour au lendemain par aucun gouvernement. Quand la bulle éclatera, beaucoup d'entreprises tomberont — mais les modèles open-weights, eux, resteront disponibles.

Dans beaucoup de conférences, l'IA n'apparaissait qu'en passant : « on a construit ça avec Claude Code. » Certains orateurs disaient ouvertement « ouais, j'ai juste demandé à Fable 5 de l'implémenter ». Ça sonne « tech-bro », mais leurs talks ont été acceptés et applaudis. L'essentiel : ce sont des humains qui mettent leur crédibilité en jeu. S'ils présentaient du slop, ils la perdraient. Ils ne laissent pas le LLM penser à leur place : ce sont leurs pensées, dopées.

« Les LLM amplifient ce que vous avez déjà : opinions, structure, cadres. Si vous avez des pensées, elles ressortent plus vives et plus vite. » Ils sont bons pour le brainstorming, la relecture, l'itération de phrases, le rôle de rubber duck ou d'avocat du diable. Mais « si vous n'avez rien, rien ne sort, très couramment ». La valeur, pour l'auteur : produire des choses de meilleure qualité qu'il ne le pourrait seul, en faisant **moins de choses, mieux**, quitte à consommer énormément de tokens pour préparer quelques phrases destinées à un humain.

## Pourquoi ça compte

Cette pièce nomme précisément la tension que vivent beaucoup d'équipes en 2026 : la lucidité sur les défauts des LLM et leur usage quotidien ne s'excluent pas. C'est un argument nuancé, loin des postures pro/anti, utile pour cadrer une politique d'usage réaliste.
