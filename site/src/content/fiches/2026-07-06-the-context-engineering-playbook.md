---
title: "The context engineering playbook (Claire Gouze)"
date: 2026-07-06
url: https://roundup.getdbt.com/p/the-context-engineering-playbook
authors: [Claire Gouze, dbt Labs]
keywords: [context engineering, analytics engineering, evals, data modeling, agents]
theme: Leadership
tone: opinion
used_in: ["2026-07-06"]
---

## Résumé

Dans cet épisode de l'Analytics Engineering Podcast (dbt Labs), Claire Gouze, co-fondatrice et CEO de nao Labs, défend une thèse pragmatique : le context engineering est le nouveau analytics engineering. Elle a mené l'expérience proprement — partie de zéro contexte, elle a ajouté des sources une à une en mesurant la fiabilité de son agent analytics. Les sources « fancy » (historique de requêtes, profiling) plafonnent à 40 % ; ce qui fait passer à 90 %, c'est le travail le moins glamour : nettoyer le modèle de données et écrire de la doc. Sa mise en garde : brancher un agent sur chaque source brute, c'est répéter l'erreur des années 2010 de plugger sa BI sur la prod. Le contexte aura besoin de sa propre stack.

## Points clés

- Le context engineering est le nouveau analytics engineering : même métier (capturer la connaissance métier tacite et la structurer), nouveau support (fichiers markdown au lieu de seuls modèles).
- Les plus gros gains de fiabilité sont ingrats : nettoyer le modèle de données et écrire de la doc ont fait passer l'agent de 40 % à 90 % ; Anthropic a fait le même constat (les query logs aident peu, la mise en ordre aide beaucoup).
- On est dans l'ère du « just plug it into production » pour les agents — brancher un agent sur chaque source brute reproduit l'erreur des années 2010 (BI plugée sur la prod).
- Le contexte aura besoin de sa propre stack : ingestion, transformation, résolution des contradictions, exposition d'une source de vérité unique.
- La valeur ajoutée n'est pas ce qu'on met dans le contexte mais la méthode : commencer petit (10-20 tables), brancher la doc dbt existante, lancer les tests, obtenir une baseline, puis itérer.
- Le chiffre qui rassure une data team pour déployer un agent : « sur mes 50 questions les plus importantes, j'ai 90 % de précision, et ça va le rester. »

## Analyse approfondie

Le contexte est le sujet numéro un dans la data en ce moment. Tout le monde cherche la même chose : un endroit unique où poser une question en langage naturel et recevoir une réponse fiable. Avec ça, on peut construire de l'analytique conversationnelle, mais aussi essentiellement n'importe quel agent qui a besoin de se connecter aux données de l'organisation. À condition d'avoir le contexte.

Claire Gouze est co-fondatrice et CEO de nao Labs, un agent analytics open-source construit sur le context engineering, qu'elle a lancé avec Christophe Blefari. Son parcours dans la data est atypique : diplômée d'école de commerce, elle a appris à coder seule, est devenue l'une des premières recrues « business school » de BCG Gamma, puis a dirigé la data chez sunday, une startup de paiement par QR-code, où elle a construit la stack data de zéro pendant que l'entreprise passait de 20 à 300 personnes. nao est né en appelant 80 équipes data différentes et en écoutant ce qui les ralentissait. Beaucoup parlent de construire des couches de contexte et de recruter des context engineers ; Claire et son équipe le font : elles ont écrit un playbook du context engineering, avec des conseils concrets sur la construction de sa propre couche de contexte et la création d'évals.

### Les trois idées à retenir

1. **Le context engineering est le nouveau analytics engineering.** Le job est le même qu'il a toujours été : rassembler la connaissance métier tacite et la transformer en quelque chose de structuré et digne de confiance. Seul le support est nouveau : des fichiers markdown au lieu de seulement des modèles. Claire connaît déjà des data people renommés « context engineers ».

2. **Les plus gros gains de fiabilité sont ingrats.** Les sources de contexte « fancy » ne font pas bouger l'aiguille autant qu'on l'espère. Nettoyer son modèle de données et écrire une bonne documentation, voilà ce qui a fait passer l'agent de Claire de 40 % à 90 % de fiabilité. Anthropic a fait le même constat : les query logs ajoutent peu, tenir sa maison en ordre ajoute beaucoup.

3. **On est dans l'ère du « just plug it into production » pour les agents.** Connecter un agent directement à chaque source brute, c'est l'erreur des années 2010 (plugger son outil de BI sur la base de production) répétée. Le contexte aura besoin de sa propre stack : une façon de l'ingérer, de le transformer, de résoudre les contradictions, d'exposer une source de vérité unique.

### L'entretien (légèrement édité)

Mon parcours dans la data est atypique. J'ai eu mon diplôme d'école de commerce il y a une dizaine d'années, mais je voulais apprendre des choses techniques, alors j'ai rejoint BCG Gamma, le bras data science de BCG. J'y étais la première recrue issue d'une école de commerce. J'ai passé trois ans à construire des modèles de ML pour des clients : forecasting, personnalisation, optimisation. Puis j'ai rejoint une startup, sunday, dans le paiement par QR-code pour restaurants, parce que je voulais monter ma boîte un jour. Ils n'avaient rien, juste une base de production plugée dans Metabase. 20 personnes à mon arrivée, 300 un an plus tard : ça allait vite. Venant du conseil, où on construit tout sur mesure, j'ai construit un ETL toute seule, un pipeline d'ingestion en Python pour les données Salesforce, une couche de transformation en Python. Puis on m'a parlé d'outils qui s'appellent dbt et Airbyte. J'ai donc migré tout mon travail custom sur une stack standard. Dure leçon.

Notre premier produit était un « cursor for data » : ton IDE branché sur la data, avec un agent qui tient tout le contexte. Mais MCP a décollé, Cursor et Claude s'en sortaient bien. La nouvelle chose que voulaient les équipes data, c'était un moyen de laisser n'importe qui dans l'entreprise utiliser des agents sur les données. Les data people ne sont pas excités par la façon de coder ; ils sont excités à l'idée d'aider les utilisateurs métier et d'être valorisés pour ça. Les data teams portent un traumatisme, vues comme une équipe de support. Si on peut les aider à être valorisées par le métier, c'est la plus belle chose qu'on puisse faire pour elles.

La principale valeur qu'on ajoute, c'est l'évaluation et la gouvernance. Chaque équipe met quelque chose de différent dans son contexte : certaines ont une doc complète, d'autres une couche sémantique, d'autres presque rien sur leurs tables. Mais toutes utilisent un framework pour tester la fiabilité de l'agent et continuer à la tester dans le temps en CI/CD. Elles étudient aussi les conversations entre utilisateurs et agent, ce qui montre où s'améliorer. On essaie de ne pas surcompliquer. Certains veulent des ontologies, de la sémantique. Nous voulons que tu démarres simple. La couche de contexte est un système de fichiers. On t'aide à la construire comme un repo GitHub qui t'appartient et ne t'enferme pas ; par-dessus, on ajoute l'évaluation, les permissions et une UI.

C'est plus une question de méthode que de ce qu'il faut mettre exactement dans le contexte, car cela diffère entre une startup à 10 tables et une entreprise à des milliers. Commence focalisé. Prends l'équipe qui demande le plus d'analytique, ou tes métriques principales, et réduis le périmètre à 10 ou 20 tables. Branche ce que tu as déjà, en général tes docs dbt, et lance tes tests. Ça te donne un chiffre de fiabilité de base. Ensuite tu itères : tu regardes où l'agent échoue, tu redessines une partie du modèle de données, tu ajoutes de la doc, tu profiles une table. C'est une boucle itérative.

Soit tu connais déjà tes questions les plus importantes et tu as les requêtes quelque part dans ta BI, tu les collectes ; soit tu utilises une skill qu'on a construite qui regarde les métriques principales de tes tables et suggère des questions clés à tester. Je recommande de les relire, mais ça donne une première base. Ensuite tu peux dire : sur mes 50 questions les plus importantes, j'ai 90 % de précision, et ça va le rester. Ce chiffre-là est ce qui rassure une data team assez pour déployer l'agent.

Oui, je connais des data people renommés context engineers, donc ça arrive déjà. Les data teams sont le fit parfait. L'analytics engineering consistait à rassembler la connaissance métier auprès des parties prenantes et à la traduire en quelque chose de structuré et technique. Le context engineering, c'est exactement ça. Le contexte, c'est juste de la connaissance d'entreprise qu'on veut structurée, optimisée pour ne pas faire exploser le coût en tokens, et traitée comme une source de vérité — de la même façon qu'on veut une source de vérité pour une métrique. Les data teams pensent déjà ainsi.

C'est amusant : le plus grand bond de fiabilité de l'agent vient juste de ta modélisation de données et de ta doc. J'ai fait l'expérience : je suis partie de zéro contexte et j'ai ajouté des sources pas à pas, en mesurant la fiabilité à chaque étape. Le profiling, l'historique de requêtes, ce genre de choses me laissaient coincée autour de 40 %. L'agent échouait à cause d'une ambiguïté entre deux colonnes, ou d'une métrique légèrement différente entre deux tables. Quand j'ai refait des parties du modèle de données et écrit de la doc, je suis montée à environ 90 %. C'est un travail profond de garder un modèle de données propre et non ambigu, mais ça paie avec les agents.

Dans notre framework, tout finit par devenir un fichier markdown, donc le format de départ importe peu. Ce qui compte, c'est où il est maintenu. Si quelqu'un demande s'il faut documenter dans le contexte de l'agent ou dans les docs dbt, je réponds les docs dbt, parce que ça doit vivre au plus près du travail quotidien. Quand tu changes un modèle dbt, tu changes la doc, et ça se synchronise vers l'agent.

## Pourquoi ça compte

Elle démontre chiffres à l'appui que le vrai levier de fiabilité des agents n'est pas le modèle mais la discipline du contexte — un déplacement du travail d'ingénierie que toute équipe data et IA va devoir intégrer.
