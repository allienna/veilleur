---
title: "AI's brave new world of technical debt"
date: 2026-06-03
url: https://www.infoworld.com/article/4178964/ais-brave-new-world-of-technical-debt.html
authors: [Matt Asay, InfoWorld]
keywords: [technical debt, dependencies, supply chain, MCP, prompt debt]
theme: Tech
tone: opinion
used_in: ["2026-06-03"]
---

## Résumé

L'article part du conseil "contre-intuitif" de Mitchell Hashimoto (forker ses dépendances, les trimmer, ne pas mettre à jour sans raison) pour analyser une nouvelle forme de dette technique amplifiée par l'IA. Les agents n'importent pas que des packages : ils lisent des instructions de repo, suivent des prompts, parlent à des serveurs MCP, exécutent du shell — autant de dépendances et de surfaces d'attaque. Des études chiffrent le risque (les agents choisissent plus souvent des versions vulnérables ; les prompts décaient silencieusement) et l'article conclut que l'IA n'élimine pas la discipline d'ingénierie : elle augmente le prix de s'en passer.

## Points clés

- Hashimoto : forker les dépendances, les trimmer à l'usage réel, ne mettre à jour que si quelque chose casse pour les utilisateurs.
- Les attaques npm du printemps (axios compromis, worm Mini Shai-Hulud) ont surtout touché ceux qui tiraient des versions fraîches ; la défense la plus efficace fut un simple "cooldown" de ~10 jours.
- Étude Purdue (117 062 changements de dépendances) : les agents IA choisissent des versions vulnérables 2,46 % du temps contre 1,64 % pour les humains ; net +98 vulnérabilités côté agents vs -1 316 côté humains.
- La dette s'étend au-delà du code : MCP tool poisoning (>25 % de violations de politique quand on se repose sur le modèle), et les prompts eux-mêmes (CLAUDE.md, AGENTS.md) sont de la dette technique qui décaie.
- Avec Mythos, les vieux bugs latents ne restent plus latents : exploits pour un bug FFmpeg de 16 ans et une faille FreeBSD de 17 ans pour moins de 20 000 $.
- La discipline juste : connaître sa surface, la garder petite, la scorer en continu ; traiter MCP, outils et prompts comme des dépendances de production.

## Analyse approfondie

Mitchell Hashimoto veut que vous arrêtiez de mettre à jour vos dépendances, ce qui, historiquement, est carrément insensé. Pourtant, après le printemps que npm vient de vivre, son conseil ressemble moins à une hérésie qu'à du contrôle. Sa règle ? Forkez vos dépendances, trimmez-les à ce que vous utilisez réellement, et ne mettez pas à jour sauf si quelque chose casse pour vos utilisateurs. Vous ne mettez pas à jour juste parce que Dependabot a ouvert une PR ou parce qu'une version plus récente existe. Si vous mettez à jour, le travail de comprendre chaque commit pertinent de l'arbre transitif est le vôtre, pas celui du mainteneur.

Dans une industrie entraînée à assimiler "dernière version" à "sécurisée", cela paraît imprudent — jusqu'à ce qu'on regarde ce qui s'est passé ce printemps. Dans deux des pires attaques npm de l'année, les plus exposés furent ceux qui tiraient les versions fraîches. Quand la librairie axios a été compromise, les attaquants ont poussé deux releases empoisonnées larguant un cheval de Troie d'accès distant sur chaque machine ayant fait une installation fraîche durant une fenêtre d'environ trois heures. Si vous étiez épinglé sur une version propre et n'aviez pas réinstallé, vous avez dormi tranquille. Des semaines plus tard, le worm Mini Shai-Hulud s'est auto-propagé à travers TanStack puis vers Mistral, UiPath, et une longue traîne de packages téléchargés des millions de fois par semaine.

Comment se défendre contre ça ? Peut-être en ne faisant rien. La défense la plus efficace contre Mini Shai-Hulud ne fut ni un scanner ni une signature. Ce fut un cooldown. StepSecurity a retenu les versions nouvellement publiées pendant une fenêtre configurable, environ 10 jours, avant de les servir. Les clients en cooldown continuaient à recevoir la dernière version saine connue et ne furent jamais exposés. Ironiquement, la réponse de l'industrie au développement IA semble être d'ajouter plus de dépendances.

**L'arbre de dépendances a échappé au gestionnaire de paquets.** Depuis des décennies, nous externalisons le travail indifférencié vers des librairies, et c'est globalement bien. Mais partager signifie aussi emprunter les gestionnaires de paquets, comptes mainteneurs, pipelines CI/CD et scripts de release des autres. L'IA aggrave ce risque parce que l'arbre de dépendances n'est plus confiné au code. Un agent de coding n'importe pas que des packages : il lit des instructions de repo, suit des system prompts, choisit des outils, parle à des serveurs MCP, et exécute des commandes shell. Chaque capacité est une dépendance de plus sur un comportement qui vit hors du modèle. Tout cela est de la surface d'attaque.

Dans une étude de 117 062 changements de dépendances à travers sept écosystèmes, des chercheurs de Purdue ont trouvé que les agents IA sélectionnaient des versions vulnérables connues plus souvent que les humains, 2,46 % du temps contre 1,64 %. Les mauvais choix des agents étaient aussi plus durs à défaire : 36,8 % nécessitaient une mise à jour de version majeure pour être corrigés, contre 12,9 % pour les humains. Au niveau agrégé, le travail de dépendances piloté par agents a produit un gain net de 98 vulnérabilités, tandis que le travail humain en produisait une réduction nette de 1 316. Les agents inventent aussi des dépendances qui n'existent pas, qui deviennent une surface d'attaque dès que quelqu'un enregistre le nom halluciné.

La couche MCP est sa propre version du même piège. Microsoft a documenté le tool poisoning, où des instructions malveillantes se cachent dans les métadonnées d'outil que le modèle lit pour décider quoi appeler. Dans son propre travail de red-team, Microsoft a trouvé que se reposer sur le modèle pour suivre les instructions de sécurité produisait des violations de politique plus de 25 % du temps, et a conclu que le simple suivi d'instructions ne devrait pas être traité comme une frontière de sécurité. OWASP l'a dit plus clairement : une réponse d'outil va directement dans le contexte du modèle sans équivalent de la revue qu'une description d'outil reçoit à la connexion.

Sean Goedecke a récemment argumenté que les prompts introduisent aussi de la dette technique et décaient silencieusement. Un prompt qui marchait contre un modèle se comporte différemment contre le suivant. Empilez-en assez — les fichiers `AGENTS.md` et `CLAUDE.md`, les skills, les règles, les descriptions d'outils — et vous avez discrètement construit un plan de contrôle alternatif de la façon dont votre logiciel est écrit. La plupart des équipes ne le testent jamais, ne le revoient jamais, ne l'élaguent jamais.

**"Latest" n'est pas synonyme de "safe".** La version extrême des règles de Hashimoto ne marchera pas pour la plupart des équipes. Mais la discipline sous-jacente est exactement juste : chaque dépendance devrait avoir une raison d'exister, et chaque mise à jour une raison d'atterrir. Cela va à contre-courant du développement moderne, où ajouter un package semble moins cher que réfléchir — et encore plus à contre-courant de la façon dont les agents travaillent. Les agents sont très bons pour trouver une librairie, l'importer, et passer à autre chose. Ils optimisent pour le chemin le plus rapide vers un test qui passe, pas pour la santé long terme de votre graphe de dépendances. L'IA n'élimine pas la discipline d'ingénierie ; elle augmente le prix de s'en passer.

**Les bugs latents ne resteront pas latents.** Le pari de Hashimoto suppose que le défaut non découvert dans votre dépendance gelée reste non découvert. Avec l'IA, cette hypothèse ne tient plus. En avril, le Claude Mythos Preview d'Anthropic a trouvé et construit de façon autonome des exploits fonctionnels pour un bug de 16 ans dans FFmpeg et une faille d'accès root de 17 ans dans le serveur NFS de FreeBSD, pour moins de 20 000 $ sur environ un millier de runs. Un mois plus tard, les chercheurs de Google ont signalé le premier zero-day développé par IA observé dans la nature. Ces vieilles dépendances semblaient sûres, mais maintenant un attaquant peut louer à bas coût la découverte des failles. Trimmer une dépendance à votre seul cas d'usage donne un meilleur contrôle : chaque fonction que vous n'avez pas importée ne peut pas être transformée en zero-day contre vous.

**Moins de choses, mieux comprises.** Les meilleures équipes d'ingénierie IA ne seront pas celles qui câblent des agents partout. Les ingénieurs avisés sauront précisément ce qu'ils ont câblé, pourquoi c'est là, et ce qui se passe quand ça change. Cela ne signifie pas bannir les serveurs MCP, les outils d'agent ou les packages tiers. Cela signifie tous les traiter comme des dépendances de production. Si un serveur MCP peut lire des emails, interroger des données client ou exécuter du code, il mérite le scrutin de toute autre intégration privilégiée. Si un fichier de prompt façonne la manière dont un agent édite votre code, il appartient au contrôle de version, est revu, et est supprimé quand il cesse d'être utile. Ce n'est pas nouveau : les microservices, Kubernetes ont suivi le même schéma — libérateurs en apparence, fardeaux opérationnels en réalité. Les agents suivent le même schéma, juste plus vite.

## Pourquoi ça compte

L'article nomme et chiffre une dette technique d'un genre nouveau, propre à l'ère des agents : dépendances, serveurs MCP et prompts deviennent tous des surfaces d'attaque à gouverner comme du code de production. C'est le contrepoint sécurité indispensable à l'enthousiasme AI-native.
