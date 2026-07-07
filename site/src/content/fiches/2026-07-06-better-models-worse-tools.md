---
title: "Better Models: Worse Tools"
date: 2026-07-06
url: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
authors: [Armin Ronacher]
keywords: [tool calling, harness, Claude Code, grammar-constrained decoding, lock-in]
theme: IA
tone: opinion
used_in: ["2026-07-06"]
---

## Résumé

Armin Ronacher raconte comment un bug étrange l'a mené à une découverte contre-intuitive : les modèles Anthropic les plus récents (Opus 4.8, Sonnet 5) sont *moins bons* que leurs aînés pour appeler certains schémas d'outils non standard, inventant des champs qui n'existent pas. Sa thèse : ce n'est pas une dégradation aléatoire mais un artefact d'entraînement, le post-training se faisant dans le harness Claude Code (fermé et très permissif). Conséquence : plus le post-training se concentre dans un harness dominant, plus les autres harnesses héritent de ses tics, et le schéma d'outil cesse d'être un contrat neutre.

## Points clés

- Opus 4.8 et Sonnet 5 ajoutent des clés inventées (`requireUnique`, `matchCase`, `oldText2`…) dans l'outil d'édition de Pi, alors que les anciens modèles ne le font pas.
- Le contenu de l'édition (`oldText`/`newText`) est correct — le modèle rajoute juste du bruit à la fin de l'objet, au point de plus haute entropie.
- Le bug est fortement dépendant du contexte : il apparaît dans un historique agentique long, pas dans un prompt frais ; couper les blocs de raisonnement réduit le taux d'échec de moitié.
- Hypothèse : le post-training se fait dans un harness type Claude Code qui absorbe et répare silencieusement les erreurs (alias, réparation Unicode, filtrage des clés inconnues), donc rien ne pénalise le modèle qui invente des champs.
- Les modèles récents ont un prior très fort sur le schéma d'édition de Claude Code (plat : `old_string`/`new_string`/`replace_all`) et deviennent hostiles aux schémas alternatifs.
- Le mode `strict` (décodage contraint par grammaire côté serveur) corrige le problème, mais impose des limites de complexité aux définitions d'outils.

## Analyse approfondie

Écrit le 4 juillet 2026.

Un problème très étrange (une issue sur Pi) m'a entraîné dans un terrier de lapin ces deux derniers jours. En version courte : les modèles Claude récents appellent parfois l'outil d'édition de Pi avec des champs supplémentaires, inventés, dans le tableau imbriqué `edits[]`. Et pas Haiku ou un petit modèle : Opus 4.8. L'édition elle-même est en général correcte, mais les arguments ne correspondent pas au schéma car le modèle invente des clés bidon, et Pi rejette donc l'appel d'outil et demande de réessayer.

Ça, en soi, n'est pas trop surprenant : les modèles émettent parfois des appels d'outils malformés. Surtout les petits. Ce qui m'a surpris, c'est que ça *empire* avec les modèles Anthropic les plus récents : Opus 4.8 et Sonnet 5 le montrent tous les deux, mais aucun des modèles plus anciens. Autrement dit, les modèles SOTA de la famille sont moins bons sur ce schéma d'outil précis que leurs frères plus âgés.

Au cas où vous seriez curieux à propos de Fable : je ne l'ai volontairement pas testé, car je n'étais pas sûr que les classifieurs qu'ils font tourner ne me rétrograderaient pas silencieusement vers Opus.

### Les appels d'outils sont du texte

Si vous n'avez pas passé trop de temps à regarder les entrailles du tool calling des LLM, l'important à comprendre est que les appels d'outils n'ont rien de magique et utilisent une signalisation « in-band » assez grossière. Le modèle reçoit un transcript, un prompt système et une liste d'outils disponibles. Le serveur transforme tout ça en un gros prompt avec des tokens marqueurs spéciaux. Parce que le modèle a été entraîné et renforcé sur des exemples de ce format, à un moment de la génération il émet quelque chose que l'API ou le client interprète comme « appelle cet outil avec ces arguments ».

Pour un outil d'édition de fichier, la charge utile visée pourrait ressembler à un objet JSON avec un `path` et un tableau `edits` contenant des paires `oldText`/`newText`. Un harness valide ensuite les arguments, effectue l'édition et renvoie le résultat au modèle. Si la validation échoue, le modèle voit une erreur et réessaie généralement.

La façon exacte dont ce formatage se produit n'est pas connue pour les modèles Anthropic, mais certains ont récupéré des marqueurs « ANTML », qui fuitent parfois dans des communications publiques. À ma connaissance, l'appel serait sérialisé sous une forme qui ressemble à du XML sans en être vraiment — juste un format qu'ils ont trouvé pratique à tokeniser et sur lequel entraîner. Point à noter : un paramètre de type chaîne au niveau supérieur apparaît en ligne, tandis qu'un tableau d'objets est implémenté via une sérialisation JSON.

Il y a deux façons très différentes de faire produire une telle structure au modèle : (1) lui *demander* de produire du JSON valide correspondant à un schéma, puis valider après coup ; (2) contraindre le sampler pour que du JSON invalide, ou même des formes de schéma invalides, ne puissent pas être échantillonnés du tout. La seconde approche est ce qu'on appelle le décodage contraint par grammaire (grammar-aware decoding) : le sampler masque les tokens qui violeraient la grammaire. Sans aucune contrainte, le modèle ne fait que suivre une convention apprise.

### La défaillance

L'outil d'édition de Pi permet plusieurs remplacements exacts de chaînes en un seul appel — d'où le tableau `edits`. Dans les cas d'échec, le modèle produit des entrées avec des clés en trop, comme `requireUnique`, ou encore `oldText2`/`newText2`. Sur des essais répétés, j'ai vu tout un zoo de clés finales inventées : `type`, `id`, `kind`, `unique`, `requireUnique`, `matchCase`, `in_file`, `forceMatchCount`, `children`, `notes`, `cost`, `oldText2`, `newText2`, `oldText_2`, `newText_2`, et même une clé `event.0.additionalProperties` à l'intérieur de l'objet d'édition.

Le plus agaçant : les charges utiles `oldText` et `newText` étaient correctes au byte près dans les appels invalides que j'ai inspectés. Le modèle avait bien produit la bonne invocation, puis avait ajouté du n'importe quoi à la fin de l'objet.

La défaillance est aussi fortement dépendante du contexte. Un prompt frais en un seul tour (« édite ce fichier ») ne la reproduisait pas du tout. Un historique agentique où le modèle avait lu des fichiers, diagnostiqué un problème puis composé une édition multi-lignes, si. Et de manière encore plus agaçante, tous les transcripts ne montrent pas ce comportement : j'ai eu besoin des transcripts de Petr Baudis pour reproduire le bug. Dans cette session, continuer faisait échouer Opus 4.8 environ 20 % du temps. Retirer les blocs de raisonnement de l'historique réduisait le taux d'échec de moitié. Activer l'invocation stricte l'éliminait dans mes essais.

### Pourquoi ça empire

Mon hypothèse la plus forte est qu'il ne s'agit pas d'une détérioration aléatoire mais d'un artefact d'entraînement.

Quand les anciens modèles Anthropic ont été entraînés, ils l'ont été sur certains outils (dont certains documentés). Mais cet entraînement n'avait pas encore un harness livré aux utilisateurs, comme Claude Code, comme cible évidente. Les modèles modernes sont probablement différents parce que leur post-training inclut Claude Code, ou un harness qui lui ressemble beaucoup. Le modèle apprend à quoi ressemble un appel d'outil réussi dans cet environnement. Il apprend aussi quelles erreurs sont tolérées par cet environnement.

Les propres outils de Claude Code sont relativement plats. L'outil d'édition ordinaire n'a pas la forme imbriquée `edits[]` de Pi ; il est plus proche de `file_path`, `old_string`, `new_string`, et d'un flag optionnel (`replace_all`). Regarder le client de Claude Code est très instructif : il contient des chemins de reprise pour les tool calls malformés, des alias de paramètres, des coercitions de types, des réparations Unicode et un filtrage des clés inconnues. Autrement dit, le propre client d'Anthropic semble s'attendre à — et accepter — pas mal de « slop », et le répare, le plus souvent silencieusement.

Si l'apprentissage par renforcement se produit dans un harness comme celui-là (ou une simulation de celui-ci), alors des appels d'outils légèrement malformés peuvent tout de même accomplir la tâche et recevoir une récompense. Le harness absorbe entièrement l'erreur et il y a peu de gradient contre le fait d'inventer un alias, d'ajouter un champ parasite ou d'utiliser un nom de paramètre proche.

Pire, le modèle peut devenir très fortement adapté à la forme canonique de l'outil d'édition de Claude Code. Un autre harness peut présenter un outil avec la même intention sémantique mais un schéma différent, de plus en plus « hors distribution ». Le modèle mieux entraîné pourrait en fait vous résister davantage, parce que son prior est plus fort.

Ce n'est pas très surprenant, mais c'est un changement par rapport à il y a quelques mois. Quand Opus 4.5 est sorti, il s'adaptait exceptionnellement bien aux autres outils d'édition. J'étais même assez convaincu qu'on était sur une bonne trajectoire, où les modèles seraient de plus en plus capables de s'adapter à n'importe quelle forme d'outil tant que les instructions sont bonnes. Maintenant, je suis un peu inquiet de la trajectoire prise : des schémas d'outils alternatifs pourraient non seulement être peu familiers, mais implicitement pénalisés par un post-training qui optimise pour une écologie d'outils particulière et indulgente. Et cette écologie n'est pas documentée. Il existe bien un outil « text editor » documenté, mais ce format n'est en fait pas suivi par Claude Code. Ce que Claude Code fait en interne (harness fermé) vous est caché.

### Le harness à slop

Claude Code est évidemment fermé, mais on peut regarder le code minifié et se faire une idée. Honnêtement, il est très tolérant vis-à-vis des données entrantes. Il vérifie le texte visible du modèle pour détecter des balises `<invoke` qui auraient fuité, émet de la télémétrie quand ça arrive, et dispose de sa propre machine à états pour réessayer ces appels. Il répare les échappements Unicode cassés. Il a des alias de paramètres par outil (par exemple `Edit` accepte `old_str`, `old_string`, `new_str`/`new_string`, `path` comme alias de `file_path`, et d'autres). Il filtre silencieusement les clés inattendues et n'utilise pas le mode `strict` — car Anthropic applique des limites de complexité aux définitions d'outils qui font échouer les requêtes API en mode strict.

### Stricteness

Ce problème sera-t-il présent dans d'autres harnesses ? Un énorme souci avec Anthropic est que les modèles sont totalement fermés, et le harness aussi. Les modèles Codex sont fermés aussi, mais au moins le harness ne l'est pas. Il y a aussi gpt-oss, entraîné explicitement à utiliser le format de réponse « harmony » d'OpenAI, avec beaucoup de documentation. Harmony intègre les canaux et les types de contenu d'appels d'outils dans le format de prompt, avec un marqueur `<|constrain|>json` qui permet à la pile d'inférence de basculer en échantillonnage contraint JSON pour le corps de l'appel. Anthropic semble différent, mais peut-être pas totalement : si un tableau d'objets est représenté en JSON, le modèle doit écrire du JSON dans le paramètre d'outil, et un échantillonnage contraint basique explique peut-être en partie les clés en trop.

Opus 4.8 et Sonnet 5 semblent avoir des priors bien plus forts sur ce à quoi doit ressembler un appel d'outil d'édition, et ce prior semble être le schéma de Claude Code : une paire plate old/new plus le flag optionnel `replace_all`. Ma supposition : Opus a appris qu'une opération d'édition peut avoir un champ optionnel supplémentaire, mais sous la forme imbriquée de Pi il n'a pas de nom entraîné pour ce champ. Il en échantillonne donc un plausible à chaque fois, d'où des dizaines de clés aléatoires plutôt qu'un alias stable. Comme le mode `strict` d'Anthropic corrige ça, je suppose que côté serveur ils refusent d'échantillonner une clé non permise par le schéma JSON — ce qui expliquerait aussi les limites de complexité en mode strict. Les modèles Codex que j'ai testés n'ont pas montré ce type de régression.

### Ce que ça signifie pour les harnesses

La leçon inconfortable, c'est que les schémas d'outils ne sont pas neutres, en tout cas pas sur les modèles Anthropic. On aime prétendre qu'un schéma est un contrat abstrait et que le modèle est un raisonneur général qui le suivra, mais ce n'est peut-être plus vrai pour certains outils. Les schémas se situent quelque part dans la distribution : certaines formes sont proches de ce que le modèle a vu au post-training, d'autres loin. Le modèle peut être assez intelligent pour comprendre le schéma et rester mauvais pour en échantillonner la forme exacte sous pression.

Si ce comportement continue, quelles implications pour les harnesses ? On peut activer l'échantillonnage `strict` chez Anthropic et le problème devrait disparaître. Mais le fait que le modèle ait ce comportement montre l'impact de l'apprentissage par renforcement : combattre ce prior est probablement futile si on veut la meilleure performance. Aujourd'hui, Claude Code n'est pas open source et on ne sait pas ce qu'ils font dans leurs environnements de RL. On ne peut pas supposer que le comportement entraîné dans Claude Code se transférera proprement à vos outils, sauf s'ils sont très proches. Plus le post-training se concentre dans un harness dominant, plus tous les autres devront hériter de ses tics.

J'étais plus sceptique vis-à-vis de l'invocation d'outils par grammaire contrainte, car le décodage contraint peut avoir des compromis de qualité. Je pense que ça reste vrai en général, mais ce bug a nettement déplacé mes priors : si les modèles les plus récents deviennent meilleurs pour résoudre la tâche tout en devenant moins bons pour émettre fidèlement un schéma d'outil alternatif, alors le harness a besoin de garanties plus fortes quelque part.

## Pourquoi ça compte

C'est un signal fort que le progrès des modèles ne se traduit pas automatiquement en fiabilité au niveau outil, et que le harness d'entraînement dominant crée une forme de lock-in technique invisible pour quiconque construit sa propre stack d'agents.
