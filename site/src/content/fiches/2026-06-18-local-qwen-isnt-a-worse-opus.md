---
title: "Local Qwen isn't a worse Opus, it's a different tool"
date: 2026-06-18
url: https://blog.alexellis.io/local-ai-is-not-opus/
authors: [Alex Ellis]
keywords: [local LLM, Qwen, Opus, RTX 6000 Pro, quantization, self-hosted AI]
theme: IA
tone: opinion
used_in: ["2026-06-18"]
---

## Résumé

Alex Ellis, fondateur d'OpenFaaS et d'une petite entreprise logicielle bootstrapée, livre un retour d'expérience documenté sur les modèles locaux (Qwen 3.6 27B) tournant sur une carte RTX 6000 Pro à ~12 000 USD. Sa thèse : Qwen local n'est pas un « Opus dégradé » mais un *outil différent*, précieux pour des tâches précises (support client sans fuite de données, maintenance bien bornée, lecture/explication de bases de code) mais impossible à laisser tourner sans supervision sur des tâches longues, où il part en boucles infinies et hallucine. La carte s'est rentabilisée — non en remplaçant Claude, mais grâce à la confidentialité (analyser des données client airgappées) et à une récupération de revenus. Les vraies motivations du local : confidentialité/souveraineté, coûts fixes et protection contre le risque fournisseur.

## Points clés

- Qwen 3.6 27B score 77,2 sur SWE-Bench Verified vs 88,6 % pour Claude Opus 4.8 — mais les benchmarks (issues Python) reflètent mal le code distribué Go réel.
- Métaphore de la trempe de l'acier : le modèle « tourne trop chaud », dépasse l'objectif et se met à boucler ; on ne laisse pas une lame se tremper sans surveillance.
- La carte ~12 000 USD s'est rentabilisée par la confidentialité (analyse de dumps télémétrie/diag client en VM airgappée) et la découverte d'un client sous-payant de 4-5x depuis 12 mois.
- Deux types de boucles : répéter sans fin des suggestions correctes, ou s'enfermer en corrigeant un fichier qu'il corrompt — « coincé au bord de ses capacités sans demander d'aide ».
- Quantization : attention sous Q4_0 sur les clés du cache KV ; suivre les notes de la carte modèle (température, contexte). Le « local AI » devient un problème d'ops (identité, quotas, métering, routage, monitoring d'électricité).
- Bons usages : support client, maintenance bornée, tests bout-en-bout, lecture/explication de code, fine-tunes (Qwopus), Agent Skills — pas le travail agentique long et non supervisé.

## Analyse approfondie

On entend partout que Qwen local 27B ou 35-A3B est « proche du niveau Opus ». Alex Ellis a des reçus tirés d'une vraie entreprise logicielle et de projets open source, et veut être transparent. Ce billet est long pour une raison : ce n'est ni un coup d'œil rapide, ni une déclaration non étayée sur X à propos d'annuler Claude Max, ni un rapport de hobbyiste faisant tourner un modèle à quelques tokens/seconde avec 32K de contexte. C'est le parcours d'un fondateur d'une petite entreprise logicielle où les modèles locaux ont produit une valeur réelle mais nuancée — il a un intérêt en jeu, mais aucune incitation à pousser le cloud ou le local, et un fort désir que les modèles locaux deviennent capables et fiables. Il couvre : comment la carte s'est rentabilisée en deux-trois mois, comment elle sert son cas d'usage métier précis, pourquoi il ne peut toujours pas lui faire confiance sans supervision, et le pire trait de Qwen : les boucles infinies et le risque d'hallucination, surtout quand on le quantize pour tenir sur un GPU grand public.

**Son cas d'usage.** Son parcours de mainteneur et fondateur a commencé avec OpenFaaS, bâti entièrement à la main. Aujourd'hui sa petite équipe maintient OpenFaaS, SlicerVM (sandboxes IA, « l'API manquante de Linux »), Actuated.com (runners CI auto-hébergés pour GitHub/GitLab) et Inlets.com (tunnels HTTP/TCP auto-hébergés). Ces produits utilisent des primitives Linux bas niveau (conteneurs, Kubernetes, microVMs Firecracker) ; ils sont écrits en Go, avec des composants UI React, des landing pages, de la doc, des skills d'agent et des CLI. Il utilise des outils IA depuis leurs débuts ; ce sont Claude ou Codex qui font l'essentiel de son travail, et bien qu'il insiste pour écrire lui-même, il écrit rarement du code à la main.

**Un tournant pour l'intelligence frontière.** Entre novembre 2025 et janvier 2026, un tournant : beaucoup de développeurs sur X ont vanté Claude Opus comme capable de faire *tout* leur travail. Les coûts des plans haut de gamme se sont stabilisés autour de 200 USD/mois pour les individus — un vrai chiffre, mais tolérable au vu de la valeur.

**Ce qui rend les modèles locaux intéressants.** Un argument dit : « pourquoi utiliser moins que le meilleur qu'on puisse s'offrir ? ». 2026 est une nouvelle frontière : n'importe quelle idée peut être clonée du jour au lendemain par un inconnu doté d'un abonnement dans un pays en développement. Dans un marché où le coût du logiciel tend vers zéro, « gratuit et suffisant » peut suffire. Les modèles de tête contiennent entre 0,5 et 2 T de paramètres — pas « un peu plus » mais un autre niveau que le meilleur du matériel local. Pourtant, un petit modèle dense comme Qwen 3.6 27B score 77,2 sur SWE-Bench Verified contre 88,6 % pour Claude Opus 4.8.

**Benchmaxxing.** Les benchmarks sont une cible mouvante, et comme ils sont publics, on peut entraîner un modèle pour y gonfler son score. SWE-Bench Verified repose sur des issues Python ; or la plupart du code y est mono-thread et synchrone, alors qu'Ellis écrit des systèmes distribués en Go (channels, contexts, structs sur un large domaine d'exécution).

**Coût.** « Les modèles locaux ne sont pas une question de coût » vient d'une position de privilège : un individu obtient pour 200 USD/mois de l'intelligence SOTA. Les plans de codage sont clairement subventionnés (cf. le passage de GitHub Copilot au pricing au token et le tollé). Aux tarifs API au token, le point de rupture vient plus vite qu'on ne croit : Uber a plafonné la dépense à 1 500 USD/mois par développeur et par outil — pour deux outils au maximum, ~12 % de la rémunération annuelle médiane. Pour de l'usage intensif (boucles, analyse agentique, capacités en SaaS), les modèles ouverts ou locaux offrent une vraie valeur.

**Souveraineté et confidentialité.** Ses clients entreprise prennent les contrôles de données très au sérieux ; sa gamme entière tourne autour de la confidentialité et de la souveraineté. D'où l'attrait naturel pour le local — par valeurs et par obligations. Même sans données client, vivre hors des États-Unis expose au risque fournisseur : le retrait du modèle Fable 5 d'Anthropic du jour au lendemain a pu choquer. Les modèles locaux sont la solution au « et si les labos frontière font X ? ».

### Tremper la lame

Que veut dire « pas le même outil » ? Ellis fabrique des outils tranchants (ciseaux, couteaux) en travaillant l'acier. On chauffe l'acier puis on le trempe : il devient si dur qu'il se briserait en tombant ; il faut le réchauffer en guettant un arc-en-ciel de couleurs, et si on dépasse d'une nuance, on recommence tout. Son expérience des modèles locaux est exactement comme rater les couleurs de revenu : le modèle tourne si chaud qu'il dépasse l'objectif et se met à boucler — rien n'y fait, sinon fermer le harnais en espérant qu'un contexte vidé donne un autre résultat. Il ne laisserait jamais une lame se tremper sans surveillance, comme il ne laisse jamais Qwen 3.6 27B sur une tâche à long horizon.

**Ce qu'il cherchait :** confidentialité, coûts fixes, protection contre le risque fournisseur. Là où il se fait avoir, c'est quand il traite un modèle local dans opencode comme Claude ou Codex. Avec ces derniers, c'en est presque troublant : il peut coller « Eoin a fait tourner des VMs Slicer en boucle et a manqué de FDs, il soupçonne VSock », l'agent répond « voici l'image complète », il dit « fais-le et teste de bout en bout sur mon mini PC », et 5-15 minutes plus tard il ouvre une PR, fait relire automatiquement, et itère. Une boucle merveilleusement efficace pour une petite équipe.

**Leçons d'une 3090.** Il a démarré avec une 3090 en 2023, puis une seconde pour charger des modèles avec assez de contexte. Qwen 3.5 fut le premier à produire du vrai travail. En Q4 avec 200K de contexte (quantizé aussi), il pouvait faire de petites tâches *guidées* — mais ça tournait vite mal : « Explore cette machine sous tous les angles, fais un rapport forensique » a fait lire à Qwen chaque fichier un par un jusqu'à saturer le contexte, puis halluciner des noms de fichiers et même des appels d'outils (`~/faas-netes` devenu `~/faaned`). En réduisant la tâche (« jette un œil rapide, dis-moi qui l'utilise »), il obtenait un rapport lucide à ~40-50 tokens/s. Un modèle 27B ne tient pas en pleine fidélité sur une 3090 : les leviers sont la quantization des poids, la longueur du contexte, la compression des clés/valeurs. Règle empirique : sous Q4_0 sur les clés du cache KV, les ennuis commencent. Les 3090 étaient une source constante de maux de tête.

**Gros investissement.** Pour le support client (où résoudre vite est crucial), il a dépensé ~12 000 USD sur une RTX 6000 Pro Blackwell, 96 Go de VRAM (prix monté depuis à ~15 400 USD). Pari calculé qui a payé — mais pas parce qu'elle remplace les abonnements Claude ; elle ne le peut pas.

**Support indolore sans fuite de données.** Beaucoup d'opérateurs en entreprise sont compétents mais freinés par des procédures manuelles. Ellis a écrit « diag », un CLI capturant un instantané complet d'une installation OpenFaaS sur Kubernetes ; le client l'envoie par email, et l'équipe le passe dans un modèle local airgappé, dans une VM éphémère Slicer.

**Récupération de revenus.** Lors d'un renouvellement, c'est seulement en passant la base télémétrie dans un modèle local qu'il a découvert un client qui sous-déclarait ses licences et sous-payait de 4-5x depuis plus de 12 mois. Cette récupération a payé la carte. Jamais il n'aurait passé ces données dans un plan cloud, quelle que soit sa politique de rétention. Il met en garde sur les plans de codage proche/extrême-orient qui prennent des droits sur l'IP des entrées/sorties. Parfois il donne à GPT ou Opus le schéma de la table télémétrie pour écrire un AGENTS.md que le modèle local suivra. Les données étant rapportées plusieurs fois par jour depuis des réplicas HA, elles ne se somment pas naïvement sur 24h. Sur d'anciennes itérations, le modèle ratait l'arithmétique (27,3K compté comme 273 000) — repéré seulement parce qu'il vérifiait. Une autre fois, il a déduit qu'un client allait churner car il avait peu de fonctions, ignorant qu'il les exécutait souvent. Mieux vaut le cantonner à l'analyse, pas à l'interprétation.

**Configuration actuelle.** Ellis soutient les fine-tunes de modèles ouverts comme Qwopus (qui superpose des traces de chaîne de pensée à Qwen). Son équipe fait tourner Qwopus et Qwen 3.6 27B de base sur le rig RTX 6000, servis par deux instances llama.cpp indépendantes pour garder le contexte plein. Avec le décodage spéculatif MTP, ~93 % d'acceptation et une vitesse passant de 67 à 130-200 tok/s soutenus — « plus rapide qu'un modèle cloud ». Il faut suivre les notes de la carte modèle (Qwopus marche mieux thinking désactivé, température 0,85-1,0).

**À propos des boucles.** On ne peut pas le laisser sur des tâches à long horizon. Interrogé sur les commandes à ajouter à `faas-cli`, il a donné des suggestions correctes puis les a répétées en boucle, brûlant 600 W pendant une demi-heure. Pour « ajoute --json à toutes les commandes get/list », convaincant un ou deux cas puis bloqué : ne sachant pas supprimer un avertissement TLS, il a écrit un reverse proxy Python mal indenté, puis corrompu le fichier en répétant qu'il ne savait pas le réparer, partant progressivement en vrille. Deux types de boucles : l'agent coincé au bord de ses capacités qui ne demande pas d'aide.

**Mesurer et distribuer l'accès.** Deux agents frappant la même instance llama.cpp avec des contextes sans rapport invalident mutuellement le cache de préfixe — le prompt entier est re-traité à chaque fois (thrashing). Dès qu'une autre personne utilise le modèle, ce n'est plus un prototype : qui est sur quelle instance, combien consomment-ils, quel modèle, quel coût électrique, que se passe-t-il si la personne quitte l'équipe ? Il a écrit un provider pour opencode (« Toilgate ») gérant les modèles disponibles, et deux prises Shelly Plus mesurent la consommation au mur (RTX 6000 Pro : 600 W ; deux 3090 : ~750 W combinés et très bruyantes).

**La mauvaise comparaison.** Le piège, une fois qu'on mesure, est de comparer le coût par million de tokens au pricing API de GPT-5.5 : mauvaise comparaison pour la capacité actuelle. « Local AI » devient un problème d'opérations : identité, contrôle d'accès, métering, quotas, routage de modèle, monitoring d'électricité — et surtout la fiabilité du couple agent/modèle et l'uptime pour ceux qui en dépendent.

### Pour conclure

Qwen local n'est pas « proche d'Opus », mais il a de la valeur pour certaines tâches, et c'est très tôt — ça ne peut que s'améliorer. Choses concrètes qui aident :
- Adapter le modèle local et le harnais à des tâches spécialisées : support client, maintenance bien bornée, tests bout-en-bout.
- AGENTS.md : avec des instructions détaillées (cf. alexellis/arkade), le modèle local ajoutait de nouveaux CLI plus vite et plus efficacement que des contributeurs humains, et testait son travail.
- Attention aux notes de réglage de la carte modèle (température, contexte, quantization) ; méfiance envers les quantizations très basses.
- Les modèles locaux lisent et expliquent vite des bases de code, même s'ils ne savent pas les écrire — un superpouvoir.
- Les fine-tunes comme Qwopus existent : être prêt à expérimenter.
- Les Agent Skills aident énormément (un agent local a installé Slicer de zéro sur un nouveau mini PC, avec retour d'usabilité intégré).
- Normaliser de lancer la même tâche avec un modèle local *et* cloud.
- Ne pas lui confier de travail agentique long et non supervisé : c'est là qu'il boucle, et même une carte à ~15 000 USD n'y change rien.

Ellis ne parle pas des modèles 70B (vraiment vieux désormais) ; la variante 35-A3B est populaire car elle paraît plus rapide sur MacBook (seulement 3B de paramètres actifs), mais il préfère troquer la vitesse contre la meilleure qualité. Des modèles plus gros (GLM 5.2, Kimi 2.7, Minimax M3, Deepseek V4 Flash) existent mais demandent 4-6 cartes RTX 6000 Pro — hors de portée. Aujourd'hui, les 27B denses ne sont pas taillés pour écrire du Go toute la journée : leur connaissance et leur attention limitées sautent aux yeux en revue de code (verbosité ingérable, hallucinations de problèmes de concurrence et de races). Le modeste Grok Coder Fast 1 était moins cher, plus rapide, et les a bien servis des mois avant d'être déprécié.

## Pourquoi ça compte

Un contrepoint rigoureux et chiffré au hype « local = Opus du pauvre » : le bon réflexe n'est pas « quel est le meilleur modèle ? » mais « quel outil pour quel usage ? ». Précieux pour quiconque pèse souveraineté, coût et confidentialité face au cloud — et pour comprendre que le différenciateur se déplace du modèle vers le harnais et le jugement.
