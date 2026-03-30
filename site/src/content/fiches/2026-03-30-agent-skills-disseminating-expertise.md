---
title: "Agent Skills: Disseminating Expertise"
date: 2026-03-30
url: https://roundup.getdbt.com/p/agent-skills-disseminating-expertise
authors: [Tristan Handy]
keywords: [agent skills, dbt, AI agents, expertise encoding, developer tools]
theme: IA
tone: opinion
used_in: ["2026-03-30"]
---

## Résumé

Tristan Handy, fondateur de dbt Labs, partage une réflexion profonde sur les agent skills après avoir utilisé une skill de migration pour faire migrer automatiquement un projet dbt Core vers Fusion sans aucune intervention humaine. Il distingue les skills des outils MCP et de la documentation classique : les skills sont de l'expertise encodée, à mi-chemin entre les deux. L'article explore les implications pour la dissémination des bonnes pratiques, l'écosystème de distribution de skills, et la question fondamentale de ce que devient la documentation "traditionnelle" à l'ère des agents IA. Handy conclut que les skills représentent une forme d'open source appliqué à l'expertise plutôt qu'au code.

## Points clés

- Une skill de 12 ko de markdown peut encoder des centaines, voire des milliers d'heures d'expérience collective humaine — edge cases, jugements, pièges de configuration
- Les agent skills ne sont ni de la documentation, ni des outils MCP : ce sont de l'expertise encodée, chargée dynamiquement par les agents selon le contexte
- Les benchmarks montrent que l'approche CLI + skills est 10 à 32x moins coûteuse que MCP (1 365 tokens vs 44 026) et atteint 100% de complétion de tâches vs 72% pour MCP
- La documentation classique répond à "comment fonctionne ce produit ?" ; les skills répondent en plus à "comment devrait-on l'utiliser ?" — les bonnes pratiques tacites qui circulent dans Slack mais n'atteignent jamais les docs de référence
- Les skills sont forkables : il n'y a pas besoin d'une seule bonne réponse, chaque perspective divergente peut "gagner" dans un marketplace ouvert — de l'OSS, mais pour l'expertise
- L'intégration native des skills dans `dbt deps` permettrait d'installer un package dbt et ses skills associées d'un seul coup, les skills devenant partie intégrante du graphe de dépendances du projet

## Analyse approfondie

### Point de départ : une migration autonome

Il y a quelques semaines, Tristan a pointé Claude, équipé de la nouvelle [skill migrate-to-fusion](https://github.com/dbt-labs/dbt-agent-skills/blob/main/skills/dbt-migration/skills/migrating-dbt-core-to-fusion/SKILL.md), sur un vrai projet dbt Core de taille décente tournant en version 1.10, et lui a dit de faire ce qu'il avait à faire.

Il a réalisé l'intégralité de la migration sans aucune aide ; Fusion a compilé et tourné sans accroc.

Tristan est resté un instant immobile après que la migration s'est terminée. Cette skill encode des centaines, peut-être des milliers d'heures d'expérience humaine collective au sein de l'équipe et de la communauté : les edge cases, les bizarreries de configuration qui font trébucher tout le monde, les jugements sur ce qu'il faut déprécier et ce qu'il faut préserver. Des choses qu'on ne connaît que si on a fait plusieurs migrations. Tout cela, désormais en 12 ko de markdown, appelable par n'importe quel agent qui supporte les skills.

Et ce n'est qu'une goutte d'eau. Les autres [skills livrées](https://github.com/dbt-labs/dbt-agent-skills) encodent une décennie d'expertise en bonnes pratiques qui s'est accumulée dans toute la communauté dbt au cours des dix dernières années.

Ce n'est pas une question bien formulée, mais… _qu'est-ce que ça signifie ?_ Ça semble important, considérable. L'équipe a construit des centaines d'heures de formation et de contenu de certification, écrit des centaines ou des milliers de pages de documentation, tout cela pour des humains. Et certes, ils n'ont pas répliqué l'expertise d'un analytics engineer humain… pas encore. Mais c'est quand même bien plus que rien.

### Ce que sont les agent skills

Les agent skills sont des bundles de prompts et de guidance procédurale que les agents IA — Claude Code, Cursor, Copilot, Codex, etc. — chargent dynamiquement lorsqu'on leur demande d'accomplir un travail pertinent. Ce ne sont pas de la documentation. Ce ne sont pas des outils MCP. C'est quelque chose entre les deux : de l'expertise encodée qu'un agent peut charger et appliquer sans qu'on ait à expliquer comment faire une tâche à chaque nouvelle session.

dbt Labs a [livré 8 skills liées à dbt jusqu'ici](https://docs.getdbt.com/blog/dbt-agent-skills). Tristan ne les a pas toutes utilisées, mais son équipe l'a fait — des solutions architects aux resident architects en passant par l'équipe DX qui a fait la majeure partie du travail pour les construire — et le retour général est que son expérience est typique. Elles fonctionnent, souvent de manière saisissante.

Une partie de cette efficacité tient au fait que les skills sont optimisées pour un lecteur différent de tout ce qui a été écrit auparavant. Quand on écrit pour des agents, on peut être beaucoup plus déclaratif ("fais ceci"), alors que quand on écrit pour des humains, il faut préserver beaucoup plus d'espace pour les opinions et les goûts individuels. Le premier mode, combiné aux performances des modèles actuels, produit simplement d'excellents résultats.

### Ce qui reste à faire

Huit skills, c'est un début. C'est formidable. Mais il reste clairement beaucoup à faire. Voici quelques domaines à peine effleurés :

- **Workflow de développement** : code review, dbt Mesh, exposures, metadata
- **Data modeling, techniques avancées** : Snapshots, Python models, optimisation warehouse, open table formats
- **Bonnes pratiques de data modeling** : audit de cohérence, détection de duplication

Ce ne sont là que les évidences, et d'autres idées viennent facilement. Si l'un de ces sujets est quelque chose sur lequel vous avez passé du temps réel et développé des opinions, le repo est [ouvert aux contributions](https://github.com/dbt-labs/dbt-agent-skills).

### Skills vs MCP : un vrai débat

Si vous avez déjà mis en place le serveur MCP dbt, vous vous demandez probablement comment les skills s'y rapportent. Pareil ? Différent ? Complémentaire ?

Réponse courte : MCP et skills sont des choses différentes ; les deux sont utiles ; la relation entre eux est assez intéressante. Le récit initial était "ils sont complémentaires : MCP aide avec le tool calling et les skills aident avec l'expertise." Ce n'est pas faux, mais c'est insuffisant.

Le problème avec cette perspective est qu'elle minimise un vrai trade-off. Simon Willison l'a formulé plus crûment, en titrant son post d'octobre 2025 sur le sujet : "[Claude Skills are awesome, maybe a bigger deal than MCP.](https://simonwillison.net/2025/Oct/16/claude-skills/)" L'inconvénient du MCP qu'il pointait était la consommation de tokens, car il injecte les schémas complets des outils qu'ils soient pertinents ou non, rendant chaque interaction moins efficace.

L'approche alternative, pour les produits orientés développeurs, est skills + CLI. [Des benchmarks sur 75 runs](https://www.scalekit.com/blog/mcp-vs-cli-use) montrent que les agents CLI complètent les tâches à 1 365 tokens versus 44 026 pour les agents MCP, presque entièrement parce que le serveur MCP injecte les 43 schémas d'outils du serveur GitHub Copilot MCP dans chaque conversation, qu'ils soient utilisés ou non. L'approche CLI gagne sur le coût par 10 à 32x pour ces tâches, atteint 100% de complétion contre 72% pour MCP, et ajouter un fichier skill de 800 tokens à l'agent CLI réduit les appels d'outils d'un tiers et la latence d'un tiers en plus.

Bien sûr, tout cela dans une seule étude assez contrainte, et il y a plein de raisons pour lesquelles cela peut ou non s'appliquer dans d'autres contextes. Le point est que la bonne manière de faire du tool-calling est actuellement un peu en suspens ; il faudra du temps pour définir les meilleures pratiques de façon plus définitive.

### L'écosystème de distribution des skills

La couche de distribution des skills est, disons, _naissante_. Beaucoup de gens voient l'opportunité et construisent des produits similaires simultanément, et il n'y a pas encore eu de convergence sur les exigences. C'est intéressant à observer — on voit l'infrastructure d'une nouvelle catégorie se construire en temps réel.

Il existe un certain nombre de "gestionnaires de packages de skills", mais trois semblent être en tête : **[Vercel / skills.sh](http://skills.sh/)**, **[Tessl](https://tessl.io/)**, et **[SkillsMP](https://skillsmp.com/)**.

L'analyse de Tristan : cette infrastructure se fait principalement _en dehors_ du contexte des fournisseurs de modèles (les bénéfices multi-plateformes sont réels) et il n'y a pas nécessairement besoin de convergence. L'analogie pré-IA est npm, Homebrew, apt, PyPI : il n'y a jamais eu de convergence sur les gestionnaires de packages et cela n'a pas besoin de changer.

La question plus intéressante est de savoir si le gestionnaire de packages de dbt devrait intégrer nativement le support des skills. Il y a une [discussion active dans le repo dbt-core](https://github.com/dbt-labs/dbt-core/discussions/12521) qui propose exactement cela : **dbt deps** installerait à la fois les packages et les skills en une seule commande. L'idée que les packages dbt embarquent leurs propres skills — installer **dbt_utils** et obtenir les skills qui enseignent à l'agent comment utiliser correctement ces macros — représenterait un onboarding sans friction, les skills comme première classe dans le graphe de dépendances du projet.

Au premier regard, c'est élégant. Mais plus on y réfléchit, plus c'est… assez fondamentalement transformateur. Imaginez référencer dbt-datavault et obtenir non seulement un ensemble de macros mais aussi _un ensemble complet de bonnes pratiques_ que votre agent peut déployer automatiquement.

### La documentation traditionnelle, les formations, les certifications : quel avenir ?

Si tout ce qui précède était un téléchargement d'informations de fond sur l'état des skills, c'est la partie sur laquelle Tristan est genuinement curieux. Quel est le rôle de la documentation "traditionnelle" à l'avenir ? De la formation ? De la certification ? dbt Labs a investi énormément de temps, d'énergie et de ressources pour construire l'expertise d'un écosystème entier d'analytics engineers ; est-ce que des entreprises comme eux continueront à faire ça à l'avenir ? Le devraient-elles ?

Un indicateur intéressant : Microsoft a récemment construit un [pipeline qui convertit automatiquement la documentation produit Azure en agent skills](https://learn.microsoft.com/en-us/training/support/agent-skills), mise à jour en continu quand les docs changent. C'est élégant et répond à un vrai besoin. Mais il manque quelque chose dans cette approche.

La documentation répond typiquement à une question : _comment fonctionne ce produit ?_ Elle donne la syntaxe, les paramètres, les entrées valides. C'est important mais ce n'est pas tout ce que peuvent faire les skills.

Ce que la documentation ne dit typiquement _pas_ : _comment devrait-on utiliser ce produit ?_ Quand faut-il choisir cette fonctionnalité plutôt qu'une autre ? À quoi ressemble un projet bien structuré trois ans après sa création ? Quels sont les patterns qui semblent corrects aujourd'hui mais créent de la dette technique ? Quels sont les pièges dont les praticiens expérimentés se préviennent mutuellement dans Slack mais qui n'atteignent jamais les docs de référence ?

Ce deuxième type de connaissance — appelons-le _connaissance des bonnes pratiques_ — fait partie de ce que dbt-agent-skills tente d'encoder. Pas seulement "voici la syntaxe pour un unit test" mais "voici comment penser quand écrire un unit test, quelles assertions valent la peine d'être faites, et comment structurer les tests pour qu'ils donnent un signal sans ralentir votre CI."

Microsoft ne voit peut-être pas les bonnes pratiques comme sa responsabilité. C'est probablement juste : ils sont dans une position fondamentalement différente de la plupart des éditeurs de logiciels. Auto-générer des skills depuis les docs a peut-être du sens pour eux, même si avec le temps, on peut se demander si ça ne va pas dans l'autre sens. Dans ce monde, les skills, rédigées pour les agents et plus empiriquement testables, seraient écrites en premier.

### La skill-ification comme dissémination de l'expertise

La réflexion récurrente de Tristan : tout comme la communauté dbt s'est réunie au cours des dix dernières années pour définir les bonnes pratiques de l'analytics engineering — à quoi ressemble un bon modèle, comment structurer un projet, quand utiliser un snapshot, comment écrire un test qui vaut vraiment la peine d'être lancé — il pense qu'elle se réunira au cours des prochaines années pour distiller cette connaissance en agent skills.

Et cette skill-ification représente une avancée significative pour la communauté. Les bonnes pratiques encodées dans une skill se propagent plus vite que les bonnes pratiques dans un article de blog. Disséminer la connaissance dans un article de blog implique une friction considérable, où chaque lecteur humain doit faire le travail de lire, mettre à jour son modèle mental et pratiquer la nouvelle compétence. Distribuer des skills à un agent est sans friction.

Elles sont aussi forkables. Il n'y a pas besoin d'une seule bonne réponse, et chaque perspective divergente peut potentiellement "gagner" dans le marketplace ouvert des idées. C'est de l'open source, mais **au lieu de logiciel OSS, c'est de l'expertise OSS**.

dbt Labs a toujours eu une valeur qu'ils appellent "moving up the stack." Le texte exact : _"Nous croyons que tous les membres de l'équipe devraient chercher à se remplacer de manière continue en construisant des processus, des technologies et de la documentation qui rendent leur travail existant obsolète. Nous avons un mindset d'abondance : il y a toujours plus, et du travail plus précieux, à faire. Moving up the stack présente des opportunités de croissance pour l'individu et l'équipe."_

Les agent skills sont l'une des expressions les plus directes de cette valeur que Tristan ait jamais vues. Elles poussent l'expertise — syntaxe, design, expérience — vers le bas, dans la couche agent. Cela libère le praticien humain pour opérer au sommet de sa licence : poser les questions qui comptent, interpréter les résultats, prendre les décisions de jugement qui ne peuvent pas (encore) être "skill-isées".

## Pourquoi ça compte

Cet article pose une question fondamentale que tout éditeur de logiciel devrait se poser : si l'expertise qui prend des années à accumuler peut être encodée en quelques kilooctets de markdown et distribuée sans friction à des millions d'agents, quel est l'avenir de la formation, de la certification, et de la documentation traditionnelle ? La thèse de Handy — que les skills représentent de l'OSS appliqué à l'expertise plutôt qu'au code — esquisse une réponse aussi séduisante que vertigineuse.
