---
title: "multiplayer AI agents are the future"
date: 2026-07-26
url: https://aiwithremy.beehiiv.com/p/multiplayer-ai-agents-are-the-future
authors: [Remy, AI with Remy]
keywords: [agents multiplayer, BUZZ, Opus 5, cloud agents, skills]
theme: IA
tone: news
used_in: ["2026-07-26"]
---

## Résumé

La newsletter de la semaine défend une thèse simple : tous les agents IA que nous utilisons aujourd'hui sont single-player, et c'est un cul-de-sac. Elle décortique quatre actualités qui pointent dans la même direction : le lancement de BUZZ par Block, une plateforme de chat open source où les agents sont membres à part entière ; la sortie de Claude Opus 5, deux fois moins cher que Fable au token mais souvent plus cher à la tâche ; la nouvelle capacité de Claude à apprendre une compétence en regardant l'utilisateur travailler ; et la sortie discrète de Gemini 3.6 Flash, une release de prix et de vitesse plutôt que d'intelligence. Le fil rouge tient en une phrase du « Builder's notes » : les agents locaux ne sont pas l'avenir, les agents cloud le sont.

## Points clés

- Chaque agent utilisé aujourd'hui est single-player : ton agent, sur ta machine, pour ton travail. BUZZ est la première tentative sérieuse de version « Google Docs ».
- Opus 5 coûte la moitié de Fable 5 au token, mais tourne plus longtemps et brûle plus de tokens — sur une landing page, 35,83 $ / 1 h contre 20,50 $ / 22 min pour un résultat jugé équivalent.
- Contre-intuitif : les niveaux de « thinking » bas donnent souvent de meilleurs résultats que les hauts. Anthropic recommande de partir de « high » et de descendre.
- Claude apprend une skill par enregistrement d'écran : il ne copie pas les clics, il déduit le résultat visé de chaque étape et choisit le chemin le plus rapide.
- 90 % des agents utilisés sont locaux : pas de multijoueur, arrêt dès que la machine se ferme, tâches planifiées cassées, inutilisables depuis le mobile.
- Google n'a pas livré Gemini 3.5 Pro mais 3.6 Flash (même score d'intelligence que 3.5 Flash, un peu moins cher et plus rapide) et 3.5 Flash-Lite.

## Analyse approfondie

### TL;DR

- **Opus 5 est là →** moitié du prix par token de Fable, et sur du travail réel il finit souvent par te coûter plus cher. Le constat utile : baisser le raisonnement le rend meilleur.
- **BUZZ →** Block a construit un Slack où tes agents IA sont de vrais membres du chat. Tous les agents que tu utilises aujourd'hui sont single-player. Voici la première vraie tentative de version multijoueur.
- **Claude apprend en regardant →** enregistre ton écran pendant que tu fais une tâche, commente-la à voix haute, et Claude en fait une skill. Il ne copie pas tes clics, il déduit ce que tu cherchais à obtenir.
- **Les nouveaux modèles de Gemini →** Google n'a pas livré de 3.5 Pro. Il a livré un Flash moins cher et plus rapide, qui n'est pas plus intelligent que le précédent.

### Opus 5 coûte la moitié de Fable, et finit quand même par coûter plus cher

Anthropic a livré **Claude Opus 5** le 24 juillet. Il coûte moitié moins que Fable 5 (même prix qu'Opus 4.8).

Ce prix ne survit pas au travail réel. D'après de nombreux tests utilisateurs, le modèle tourne plus longtemps et brûle plus de tokens : sur certaines tâches, il finit donc par coûter plus cher.

Nate Herk a fait tourner les deux modèles sur des travaux identiques dans Claude Code. Une landing page est revenue à 35,83 $ sur Opus, en une heure environ. Fable a fait le même travail pour 20,50 $ en 22 minutes, et il a jugé les deux résultats équivalents.

C'est à peu près pour ça que je ne m'excite pas sur les benchmarks. Avec ces modèles, tout est affaire de vibe, de la sensation qu'ils donnent quand on les utilise vraiment.

Chaque nouveau modèle ressemble aujourd'hui à un nouvel iPhone. Les sauts du 3 au 4, du 4 au 5, du 5 au 6 étaient massifs. L'écart entre un 14, un 15 et un 16 est minuscule.

Là où Opus a gagné : la chasse aux bugs dans un vrai codebase. Il a marqué 93 sur 95 contre 66 pour Fable, et il était moins cher pour le faire.

Et sur une tâche de recherche d'audience, il a traité environ 2 200 commentaires YouTube et 480 posts de communauté — plus exhaustif que Fable, et à nouveau moins cher.

Là où Fable garde l'avantage : tout ce qui demande du goût ou du jugement visuel. Les carrousels, les slide decks, l'apparence d'une landing page.

La partie que j'ai trouvée intéressante, ce sont les « thinking levels » (le petit curseur qu'on peut régler dans la plupart des harnais d'agents IA comme Claude Code).

Les niveaux les plus bas semblent mieux fonctionner ?!

L'équipe de Dan Shipper chez Every a passé une semaine à tester et a obtenu de meilleurs résultats en low et medium qu'en high.

Et les chiffres d'Anthropic eux-mêmes le confirment : leur courbe montre Opus 5 culminant autour de 44,5 % en thinking xhigh, puis redescendant à environ 43,3 % en max.

Le conseil d'Anthropic est de démarrer au thinking « high » et de descendre. Donc si le modèle t'agace, essaie de baisser le raisonnement avant d'aller chercher un autre modèle.

### Les agents IA deviennent multijoueurs : voici BUZZ

Cette année, nous sommes tous passés du chat aux agents.

Mais tous les agents que les gens utilisent en ce moment sont single-player. C'est ton agent, sur ta machine, qui fait ton travail.

Ça me rappelle Microsoft Word avant qu'on puisse collaborer sur des fichiers. Tu finissais ton document, tu l'exportais, tu l'envoyais par mail à ton équipe, et on t'en renvoyait un autre. Puis Google Docs est arrivé et tout le monde a simplement travaillé au même endroit.

C'est à peu près là qu'en sont les agents, et **BUZZ** est la première vraie tentative de version Google Docs. C'est Block qui l'a construit, la boîte de Jack Dorsey, et c'est gratuit et open source.

C'est une app de chat qui ressemble beaucoup à Slack, sauf que tes agents IA en sont de vrais membres, et non des bots greffés dessus.

Tu mentionnes un agent comme tu mentionnerais une personne, et il répond dans le fil avec des points d'avancement au fur et à mesure de son travail.

Chaque agent a sa propre identité : tu vois exactement quel agent a fait quoi, comme tu verrais quel collègue a fait quoi.

BUZZ n'est que l'interface, et tu choisis l'agent que tu branches derrière. Pour l'instant tu as le choix entre Claude Code, Codex ou Goose, et d'autres sont attendus. Tu n'es donc pas enfermé dans l'IA d'une seule entreprise : tu amènes ton propre agent.

Un point vraiment sympa : quand tu crées un nouvel agent et que tu le déposes dans un canal au milieu d'un projet, il lit tout ce qui s'est déjà passé. L'historique, les décisions, les fichiers. Puis il continue à partir de là.

Un agent peut aussi passer du travail à un autre, en déléguant au reste de l'équipe sans que tu aies à gérer ça.

Ils ont aussi sorti une app mobile BUZZ sur iPhone et Android, pour parler à tes agents en déplacement.

Cette app a l'air géniale, et je pense que c'est clairement l'avenir.

Je l'ai testée, elle est encore à un stade très très précoce, donc je n'y déplace aucun de mes vrais travaux pour l'instant. Mais je vais la garder à l'œil, et je me vois bien l'utiliser.

Ce qui m'a le plus gêné : je n'arrivais pas vraiment à voir et gérer mes skills dans l'interface, ni mes outils et mes fichiers de contexte.

Block livre des correctifs quotidiennement, donc attends-toi à des améliorations rapides.

### Claude peut désormais apprendre une compétence en te regardant travailler

Tu enregistres ton écran pendant que tu réalises une tâche, tu commentes ce que tu fais au fur et à mesure, et Claude transforme ça en une skill qu'il peut rejouer.

Cette fonctionnalité vit dans Cowork. Elle est dans le menu **+** de l'application desktop Claude, sous **Record a skill**, pour les plans Pro, Max et Team.

La partie maligne, c'est qu'il ne copie pas tes clics.

À la place, pour chaque étape, il déduit le *résultat* que tu as produit. Un fichier modifié, un message envoyé, une donnée récupérée, etc. Puis il choisit le moyen le plus rapide et le plus fiable d'atteindre ce résultat, qui est souvent plus rapide que ta propre méthode.

Ce n'est donc pas une copie aveugle des actions souris et clavier que tu as effectuées.

Parler pendant que tu travailles est optionnel, mais c'est tout l'intérêt. La narration est ce qui lui permet d'apprendre *pourquoi* tu as fait quelque chose plutôt que seulement sur quoi tu as cliqué.

Claude te propose ensuite la skill et tu appuies sur Save ou Dismiss.

OpenAI a livré la même idée dans Codex le 18 juin, environ un mois plus tôt.

**Quelques points à connaître avant d'essayer :**

- Mac uniquement, et pas sur les plans Free ou Enterprise.
- Environ 10 minutes par enregistrement.
- Tout ce qui est à l'écran est capturé, mais les champs mot de passe sont exclus de l'enregistrement.
- Tu dois la construire dans Cowork, mais tu peux déplacer une skill enregistrée vers Claude Code à la main.

**Deux remarques de ma part :**

1. Tu serais étonné de voir à quel point tu peux être maladroit en naviguant sur ton ordinateur et malgré tout obtenir de Claude une skill cohérente.
2. Utilise un gros modèle pour générer la skill, puis un modèle bon marché pour l'exécuter. Une sorte de mini-distillation (le post de TobinSouth).

### Google n'a pas livré Gemini 3.5 Pro

Ce qu'ils ont réellement livré le 21 juillet, ce sont trois modèles. Deux que tu peux utiliser, et un que tu ne peux pas.

**Gemini 3.6 Flash** est celui du quotidien. Il obtient le même score que 3.5 Flash sur l'indice d'intelligence, mais il est légèrement moins cher et plus rapide. C'est donc une release de vitesse et de prix plutôt qu'un modèle plus intelligent.

**Gemini 3.5 Flash-Lite** est le modèle pas cher pour le gros volume, et le plus rapide de la famille 3.5.

Honnêtement, il n'y a que deux raisons pour lesquelles j'irais chercher un modèle Flash. La vitesse, si tu construis ton propre produit ou app IA et que tu veux quelque chose de rapide avec une grande fenêtre de contexte. Et la vision, si tu fais beaucoup d'analyse visuelle sur des images ou des vidéos. C'est à peu près tout.

### Aussi cette semaine

- **Notion as Code** → construire tout un workspace Notion en code et le déployer.
- **Midjourney V8.2** → une mise à jour esthétique et de personnalisation du goût, avec beaucoup moins de générations ratées.
- **Le plugin Claude Security** → scanner ton code à la recherche de vulnérabilités avant de commit, ou lancer un scan complet sur toute la base de code.
- **Le connecteur Economic Index d'Anthropic** → demander à Claude quels métiers utilisent le plus l'IA et ce que les gens automatisent, réponses tirées directement du jeu de données d'Anthropic. Gratuit, tous plans.

### Builder's notes

**Les agents cloud sont l'avenir**

J'ai beaucoup réfléchi cette semaine aux agents cloud.

Aujourd'hui, 90 % des agents que nous utilisons sont des agents locaux, c'est-à-dire qu'ils vivent simplement sur notre ordinateur (comme Claude Code). Et il m'est apparu très clairement que les agents locaux ne sont pas l'avenir.

Les agents locaux ont quelques avantages, comme pouvoir agir sur ton ordinateur, mais ils viennent avec bien plus d'inconvénients…

Il n'y a pas de multijoueur qui te permette de les utiliser avec ton équipe. Si tu éteins ton ordinateur, ton agent s'arrête, tes tâches planifiées cessent de fonctionner, et tu ne peux pas non plus les utiliser correctement depuis ton téléphone.

Il est bien plus logique d'avoir des agents dans le cloud, et je pense que c'est la prochaine évolution qu'on va voir se déployer.

**Une boutique Shopify construite entièrement avec Claude Code**

J'ai montré à mon pote Jack comment utiliser Claude Code, et il carbure maintenant. Il a construit toute sa boutique Shopify avec Claude.

### Outils à essayer

- **Paper** → un canvas de design pensé pour les équipes qui travaillent avec des agents. Branche-le à Claude pour de meilleurs sites.
- **Comms** → donne à ton agent son propre numéro iMessage.

### Brain food

Je viens de terminer la 6e et dernière session de The AI Course hier soir, avec 60 fondateurs et dirigeants d'entreprise. La plupart n'avaient jamais touché à un agent avant ça.

Aujourd'hui ils ont embarqué leur propre équipe d'agents, écrit leurs propres skills, et délégué leurs processus répétables pour qu'ils tournent en autonomie.

**Quelques réalisations :**

- Sabe a automatisé la publication de ses publicités et récupéré 2 heures par jour.
- Ben a transformé tout son processus de reporting client en une seule skill : d'une demi-journée à une demi-heure.
- Jai a enregistré sa façon de relire et annoter des contrats, et un agent le fait désormais pour lui.

Et ça, c'est 3 sur 60. Emmener quelqu'un de « je ne sais même pas par où commencer » à faire tourner sa propre équipe IA en quelques semaines, c'est la meilleure sensation du monde.

## Pourquoi ça compte

C'est la synthèse la plus claire du basculement en cours : l'unité de travail passe de l'individu augmenté à l'équipe hybride humains + agents, hébergée dans le cloud. Pour un lead ou un directeur technique, ça reformule les questions d'outillage, de traçabilité et de coût réel par tâche.
