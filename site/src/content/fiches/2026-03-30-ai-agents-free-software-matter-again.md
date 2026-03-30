---
title: "AI Agents Could Make Free Software Matter Again"
date: 2026-03-30
url: https://www.gjlondon.com/blog/ai-agents-could-make-free-software-matter-again/
authors: [George London]
keywords: [free software, open source, AI agents, SaaS, software freedom, Stallman]
theme: IA
tone: opinion
used_in: ["2026-03-30"]
---

## Résumé

George London, CTO d'Upwave, avance une thèse provocatrice : les AI coding agents sont sur le point de redonner toute sa valeur au logiciel libre au sens de Stallman — non pas l'"open source" corporate, mais la liberté concrète d'exécuter, d'étudier, de modifier et de redistribuer les logiciels. Le SaaS avait rendu ces libertés théoriques en faisant disparaître le code source derrière des serveurs distants ; les agents inversent cette dynamique en permettant à n'importe qui d'exercer ces libertés par procuration. L'auteur illustre sa thèse avec son propre échec à automatiser un workflow entre Twitter et Sunsama, échouant sur six couches successives de systèmes fermés. Il conclut que "la compatibilité avec mon agent" va devenir un critère d'achat logiciel majeur, et que les SaaS sans véritable moat stratégique sont menacés.

## Points clés

- Les AI coding agents permettent aux non-développeurs d'exercer par procuration les quatre libertés du logiciel libre (exécuter, étudier, modifier, redistribuer), comblant enfin la faiblesse historique du mouvement
- Le SaaS avait rendu la liberté logicielle académique en supprimant l'accès au code source ; les agents la rendent pratique et concrète pour tous
- L'absence d'API officielle, l'authentification par mot de passe en clair, les écosystèmes mobiles fermés (iOS) — tout cela qui était acceptable dans un monde SaaS devient un obstacle visible et coûteux dans un monde agentique
- Plusieurs penseurs convergent vers la même conclusion : Nawaz Dhandala (OneUptime), Martin Alderson, John Loeber, et même Vitalik Buterin (qui a rejoint le camp copyleft en 2025)
- Contre-point important : le "vibe coding" pourrait tuer l'open source en rompant la boucle de feedback utilisateur-mainteneur, avec des effets déjà observés sur Tailwind CSS (trafic docs -40%, revenus -80%, équipe réduite de 75%)
- "Can my agent fully customize this?" va devenir la nouvelle question que posent les acheteurs de logiciels, au même titre que "est-ce qu'il s'intègre avec Slack ?"

## Analyse approfondie

### Introduction

Je fais beaucoup de vibe-coding ces derniers temps. Vraiment _beaucoup_. Peut-être pas tout à fait l'"AI psychosis" dont Andrej Karpathy a plaisanté récemment sur _No Priors_, mais pas loin. Mais plus je vibe, plus une pensée revient : **les AI coding agents sont peut-être sur le point de rendre le logiciel libre plus important qu'il ne l'a jamais été.** Pas l'"open source" dans son sens corporate édulcoré. Je veux dire le logiciel libre au sens de Stallman : le logiciel qui donne aux utilisateurs la liberté de l'exécuter, de l'étudier, de le modifier et de le partager.

Même pour les rares qui étaient conscients de cette distinction, elle a longtemps semblé essentiellement académique. Le SaaS a rendu difficile de se soucier de la liberté logicielle parce que la plupart des gens n'ont jamais vu ni touché le code source des logiciels dont ils dépendaient. Le code vivait sur les serveurs de quelqu'un d'autre, le vendeur gérait les opérations, et la question pratique est devenue celle de la commodité, pas de la liberté.

Les agents changent cela. Si un agent peut lire une base de code, la comprendre et la modifier en votre nom, alors l'accès au code source cesse d'être un droit symbolique pour les programmeurs et devient une capacité pratique pour bien plus de personnes. Soudainement, la différence entre le logiciel que vous pouvez changer et celui que vous pouvez seulement supplier commence à _vraiment_ compter.

Et je ne pense pas cela dans l'abstrait. J'ai récemment essayé de faire en sorte qu'un AI agent personnalise une application SaaS pour moi, et l'expérience a rendu le problème entier très concret très rapidement.

### Le logiciel libre a compté profondément, puis s'est effacé quand le SaaS a rendu ces libertés non pertinentes

En 1980, Richard Stallman était programmeur au laboratoire d'IA du MIT, et il avait un problème avec une imprimante. Le laboratoire avait obtenu une nouvelle imprimante laser Xerox, et elle continuait à se coincer. Stallman voulait résoudre le problème — ou du moins ajouter une fonctionnalité pour notifier les utilisateurs quand leurs travaux d'impression se bloquaient — mais Xerox ne lui donnait pas le code source. Le logiciel de l'imprimante était propriétaire.

Cela semble être une petite chose. Ce n'était pas une petite chose pour Stallman.

Il avait grandi dans une culture informatique où le partage de code était la norme. Quand vous obteniez un logiciel, vous obteniez le code source, parce que _bien sûr_ — comment autrement corriger des bugs ou ajouter des fonctionnalités ? L'incident de l'imprimante Xerox a cristallisé quelque chose pour lui : un monde où le logiciel était verrouillé, où vous ne pouviez pas étudier ou modifier les outils dont vous dépendiez, était un monde où les utilisateurs avaient perdu quelque chose de fondamental.

Stallman a donc fondé la Free Software Foundation et a passé les quatre décennies suivantes à évangéliser ce qu'il appelait "les quatre libertés" :

- **Liberté 0 :** La liberté d'_exécuter_ le programme comme vous le souhaitez, à n'importe quelle fin.
- **Liberté 1 :** La liberté d'_étudier_ comment le programme fonctionne, et de le modifier pour qu'il fasse ce que vous voulez.
- **Liberté 2 :** La liberté de _redistribuer_ des copies pour pouvoir aider les autres.
- **Liberté 3 :** La liberté de _distribuer des copies de vos versions modifiées_ à d'autres.

"Free as in speech", disait-il, "pas free as in beer."

Pendant un temps, ce message a résonné. Les années 1990 ont vu une explosion du logiciel libre : Linux, Apache, MySQL, PHP — toute la stack qui allait venir alimenter la majeure partie d'Internet. Des entreprises comme Red Hat ont prouvé qu'on pouvait construire de véritables business autour. Eric Raymond a écrit "The Cathedral and the Bazaar" et a soutenu que le développement ouvert produisait de meilleurs logiciels. Steve Ballmer de Microsoft a qualifié Linux de "cancer." Cela ressemblait à une véritable bataille idéologique pour l'âme de l'informatique.

Et puis, discrètement, la bataille est devenue non pertinente, pour une raison assez ennuyeuse.

Mais nous y reviendrons dans un moment.

### Le rebranding "open source" a préservé le partage de code en supprimant la philosophie des droits des utilisateurs

Voici d'abord un morceau d'histoire que je ne connaissais pas avant de faire des recherches pour cet article. Cela compte pour comprendre ce qui se passe maintenant.

Le 3 février 1998, un groupe de personnes s'est réuni au Foresight Institute à Palo Alto — pas une organisation logicielle, mais un think tank sur les nanotechnologies. Christine Peterson, directrice exécutive de l'institut, a proposé de remplacer "free software" par un nouveau terme : "open source." Son raisonnement était pratique : chaque fois que vous disiez "free software", les gens pensaient que vous vouliez dire gratuit, et vous passiez dix minutes à expliquer la différence au lieu de parler du logiciel réel.

Quelques semaines plus tard, lors du "Freeware Summit" d'avril 1998 organisé par Tim O'Reilly, les participants ont débattu de la dénomination et ont voté 9 contre 6 pour "open source" plutôt que pour des alternatives comme "sourceware" et "free software."

Ce qui compte, c'est ce qui a été perdu dans le rebranding. Eric Raymond et Bruce Perens ont co-fondé l'Open Source Initiative le même mois, et Raymond a publié un manifeste intitulé "Goodbye, 'free software'; hello, 'open source'." Son argument clé : l'ancienne terminologie rendait les gens du corporate nerveux.

Stallman n'a pas été invité au "Freeware Summit" de Tim O'Reilly en avril 1998 — l'événement qui a contribué à consolider le nouveau récit de leadership. Linus Torvalds y était invité. Larry Wall y était invité. Guido van Rossum y était invité. Stallman ne l'était pas.

Pourquoi cela compte-t-il ? Parce que le rebranding "open source" n'était pas juste un changement marketing — c'était une amputation philosophique. "Open source" a gardé les pratiques de partage de code mais a chirurgicalement retiré la revendication éthique sur ce que les utilisateurs _méritent_. Comme Stallman l'a dit : "L'open source est une méthodologie de développement ; le logiciel libre est un mouvement social." Raymond était explicite sur le fait que "free software" était déroutant et rendait les gens du corporate nerveux.

Le monde corporate a adoré cela. Vous pouviez utiliser du code open source, contribuer à des projets open source, et construire une identité de marque open source sans jamais avoir à vous confronter à la question de ce qui était _dû_ aux utilisateurs. L'open source est devenu une méthodologie de développement que les entreprises pouvaient adopter sans changer du tout leur relation avec leurs utilisateurs.

### Le SaaS a pris de l'ampleur en exploitant une faille de licence qui permettait aux vendeurs d'éviter de partager leurs modifications

Mais ce n'est finalement pas un débat politique ou philosophique qui a vraiment mis de côté le logiciel libre — c'était le SaaS.

La GPL — la principale licence de logiciel libre — exigeait que vous partagiez le code source avec quiconque à qui vous _distribuiez_ le logiciel. Le mot clé est "distribué". Si vous ne distribuiez jamais le logiciel — si vous le faisiez simplement tourner sur vos propres serveurs et permettiez aux gens d'y accéder via le web — la licence ne s'appliquait pas. Vous pouviez prendre du logiciel libre, le modifier, construire un business dessus, et ne jamais partager vos modifications avec personne.

Ce n'était pas hypothétique. Un exemple très médiatisé était AWS offrant des services managés autour de projets comme Elasticsearch, ce qui a déclenché des disputes très publiques sur la capture de valeur, la contribution et les termes de licence. Dans le modèle SaaS, les obligations copyleft de la GPL ne se déclenchent souvent pas à moins que le logiciel ne soit distribué, donc les exigences de partage du code source peuvent être contournées.

Les chiffres racontent ce qui s'est passé ensuite : tout au long des années 2010 et dans les années 2020, les licences permissives sont devenues de plus en plus dominantes dans les données d'utilisation open source.

Il y a eu une tentative de corriger cela. L'AGPL (Affero GPL) a été conçue pour fermer la faille SaaS — si vous modifiiez un logiciel AGPL et le rendiez disponible sur un réseau, vous deviez partager le code source. C'était une idée puissante. Tellement puissante que Google maintient maintenant une politique publique large interdisant le code AGPL à l'intérieur de Google. Comme Drew DeVault l'a soutenu, la position anti-AGPL de Google n'était pas juste une précaution juridique — c'était stratégique : "En décourageant l'utilisation de l'AGPL dans la communauté plus large, Google espère créer un ensemble plus large de logiciels libres et open source qu'ils peuvent utiliser pour leurs propres besoins sans aucune obligation."

La faible adoption de l'AGPL a engendré une cascade d'improvisation. MongoDB a basculé vers la Server Side Public License. Redis Labs a déplacé plusieurs modules Redis vers des licences de type Commons Clause en 2018, et Redis a ensuite déplacé le core Redis vers une double licence source-available avant d'ajouter l'AGPL dans Redis 8. HashiCorp a basculé Terraform vers la Business Source License. Elastic est passé d'Apache à SSPL/ELv2, puis a ajouté l'AGPL. Chaque changement validait le problème sous-jacent tout en échouant à le résoudre pleinement.

Et honnêtement ? Du point de vue de l'utilisateur, la question de la liberté logicielle a juste cessé d'avoir de l'importance. Quand le logiciel tourne sur les serveurs de quelqu'un d'autre, avoir le code source ne vous aide pas. Vous ne pouvez pas faire tourner votre propre version modifiée parce que vous ne faites tourner _aucune_ version — Salesforce le fait, ou Google, ou qui que ce soit. Les quatre libertés sont devenues théoriques.

Pendant un temps, le compromis semblait correct. Le SaaS était incroyablement pratique. Pas d'installation, mises à jour automatiques, accès de n'importe où, quelqu'un d'autre gère les correctifs de sécurité et les sauvegardes et les appels à 3 heures du matin quand le serveur tombe. Donc le débat sur le logiciel libre s'est estompé en arrière-plan. Le pendule avait décisivement basculé vers la commodité, et la plupart d'entre nous — moi y compris — avons accepté le compromis.

Puis l'IA a commencé à me donner des remords d'acheteur.

### Mon workflow Sunsama montre comment le SaaS fermé bloque la personnalisation utile même pour les utilisateurs motivés

J'utilise Sunsama pour la gestion des tâches. C'est un bon produit et je l'apprécie sincèrement. Mais j'avais un workflow que je voulais construire, et Sunsama le rendait essentiellement impossible.

Le workflow est simple : quand je fais défiler Twitter et que je vois un tweet avec lequel je veux interagir plus tard — qu'il s'agisse d'un article que je veux lire ou d'un outil IA à l'esthétique de wildcatter du Far West que je veux essayer — je veux le sauvegarder dans Sunsama comme une tâche pour pouvoir le programmer par rapport aux 20 milliards d'autres choses que je veux éventuellement faire.

Sunsama a une intégration iOS share sheet, mais iOS l'enterre derrière plusieurs taps et je n'aime pas comment ça fonctionne :

Premièrement, la tâche qu'elle crée est essentiellement juste une URL avec le titre qu'iOS extrait du tweet. J'aimerais qu'un LLM génère un titre de tâche comme "Répondre à @quelqu'un à propos de sa question sur la mesure media" au lieu de "tweet de @dril" ou n'importe quel titre que le comportement de partage par défaut produit.

Deuxièmement, je ne peux pas automatiquement labelliser ou catégoriser ces tâches. Je veux que les tweets sur la santé aillent dans la catégorie #sante, et les tweets sur le recrutement dans #recrutement. Mais le share sheet jette tout dans ma boîte de réception.

Mais mes préférences sont non pertinentes, parce que je ne peux pas ajouter d'intelligence LLM à ce workflow au-delà de ce que Sunsama décide de construire dans leur produit. Si l'équipe de Sunsama livre une fonctionnalité IA qui auto-catégorise les tâches, super. Sinon, je suis bloqué. Je peux seulement soumettre une demande de fonctionnalité et revérifier en 2032.

Ce n'est pas un problème de compétences. Je sais coder. Je pourrais construire mon propre système de gestion des tâches de zéro. La contrainte n'est pas l'expertise technique — c'est le temps et l'attention. J'ai un travail. J'ai une vie. La raison pour laquelle j'utilise Sunsama est que je ne veux pas être dans le business de la maintenance des logiciels de gestion des tâches.

C'est le classique marché SaaS. Obtenir la commodité, abandonner le contrôle.

### J'ai quand même essayé de construire le workflow, et chaque couche fermée a transformé une idée simple en un hack fragile

Officiel ou pas, je voulais mon petit widget idiot. Alors j'ai décidé de réellement tenter de le construire. Je me suis assis avec Codex et j'ai dit : construis-moi un bouton unique dans le iOS Twitter share sheet qui ajoute un tweet-comme-tâche correctement étiqueté à mon Sunsama.

Simple, non ? L'agent a immédiatement compris ce que je voulais. Il pouvait voir toute l'architecture : iOS Shortcut attrape l'URL partagée, appelle une petite fonction serverless, la fonction extrait le contenu du tweet, le passe à un LLM pour générer un titre de tâche intelligent, puis crée la tâche dans Sunsama avec la bonne catégorie.

Conceptuellement, c'est un projet de vingt minutes. En pratique, c'est devenu une visite guidée de tout ce qui cloche avec les logiciels fermés.

**Couche 1 : Sunsama n'a pas d'API officielle.** En 2026. Leur page de demande de fonctionnalité pour une API est ouverte depuis décembre 2019, avec des utilisateurs qui la supplient. Un commentateur a récemment écrit "Les fondateurs ont-ils vraiment ignoré ce ticket pendant près de six ans !? Pathétique." Donc mon agent, aussi intelligent soit-il, n'a aucun moyen approuvé de créer une tâche par programmation.

Mais heureusement, un utilisateur de Sunsama nommé Robert Niimi s'est suffisamment frustré pour rétro-ingénierer l'API interne de Sunsama et a publié le résultat en open source : une REST API relay auto-hébergée appelée `sunsama-relay`, plus un MCP server appelé `mcp-sunsama` pour que Claude puisse l'utiliser directement. Donc mon agent _peut_ créer des tâches Sunsama — mais seulement parce qu'une personne déterminée a passé son propre temps à rétro-ingénierer les flux d'authentification et a publié le résultat gratuitement. Sans son travail, j'aurais probablement juste abandonné.

**Couche 2 : L'authentification est votre vrai mot de passe.** Puisqu'il n'y a pas d'API officielle, il n'y a pas de clés API ou de tokens OAuth. L'API non officielle s'authentifie en utilisant votre vrai email et mot de passe Sunsama. Donc ma fonction serverless doit stocker mes vraies credentials. C'est une conséquence directe du modèle SaaS — Sunsama n'a jamais anticipé ou béni ce cas d'usage, donc le seul moyen d'entrer est par la porte principale avec votre identité en clair.

**Couche 3 : Le mur iOS.** J'ai fait construire la fonction serverless par Codex, incluant l'extraction de tweets, la génération de titres alimentée par LLM, et la création de tâches Sunsama. Ça a marché. Mais ensuite j'avais besoin de le câbler à un iOS Shortcut pour pouvoir le déclencher depuis le Twitter share sheet. Codex pouvait-il créer l'iOS Shortcut pour moi par programmation ? Non. Apple documente les App Intents pour les développeurs exposant des actions d'application, mais ne fournit pas d'API/format de fichier public documenté pour générer programmatiquement des Shortcuts arbitraires pour les utilisateurs finaux. Donc j'ai quand même dû ouvrir Shortcuts, taper dans un visual builder, et ajouter chaque action manuellement. Mon agent peut écrire un serveur TypeScript de 200 lignes en secondes, mais il ne peut pas automatiser la création d'un iOS Shortcut en cinq étapes. iOS (malgré le fait d'être construit sur BSD et d'utiliser de nombreux composants open source) est l'antithèse du logiciel libre.

**Le résultat :** Voici ce que la solution "fonctionnelle" exige réellement :

1. Une fonction serverless que je dois déployer et héberger moi-même
2. Une clé API Anthropic pour la génération de titres
3. Mon vrai mot de passe Sunsama stocké comme variable d'environnement
4. Une dépendance sur une API non officielle rétro-ingéniérée qui pourrait casser à tout moment
5. Un iOS Shortcut que j'ai dû construire à la main (après une quantité absurde de débogage laborieux, parce que les actions du shortcut continuaient à échouer dans iOS avec des messages d'erreur opaques et aucun log accessible.)
6. L'endpoint oEmbed de Twitter/X pour extraire les métadonnées d'embed de tweet

Au final, ça marche. Je peux partager un tweet et obtenir une tâche joliment titrée dans Sunsama quelques secondes plus tard, et je l'utilise régulièrement.

Mais regardez ce que ça a nécessité :

Six couches de contournements, trois mécanismes d'authentification différents, une dépendance sur le projet de rétro-ingénierie d'un inconnu, une infrastructure dont je suis maintenant responsable, et un iOS Shortcut construit manuellement que je ne peux pas versionner ou partager.

Comparez cela à ce que ça ressemblerait si Sunsama et iOS étaient du logiciel libre : l'agent lit le code source, comprend le modèle de données, modifie le comportement par défaut du share sheet selon mes préférences, c'est fait. Dix minutes pour Codex, pas de rétro-ingénierie, pas d'APIs grises.

### Les AI agents peuvent finalement exercer la liberté logicielle au nom des personnes qui ne savent pas coder

L'argument original de Stallman avait une vraie faiblesse légitime — une que les critiques avaient raison d'identifier pendant des décennies. Les quatre libertés — exécuter, étudier, modifier, redistribuer — présupposent la capacité de lire et modifier le code source. Pour la grande majorité des utilisateurs d'ordinateurs, cette capacité n'existe pas.

Cette critique a été faite de nombreuses fois. Protesilaos Stavrou l'a bien articulée : une licence de logiciel libre seule n'habilite pas les utilisateurs à être vraiment libres s'ils manquent de l'expertise pour exercer ces libertés — le mouvement a rétréci son focus aux exigences légales et au code, limitant effectivement son audience aux passionnés techniques. Mahmoud Mazouz a fait un argument connexe : même quand le code source est disponible, les coûts pratiques de construction, de compréhension et de modification sont prohibitifs pour la plupart des gens. Les quatre libertés ont été écrites pour les programmeurs, et la plupart des gens ne sont pas programmeurs.

**Les agents renversent complètement cela.**

Pensez à ce qu'est réellement un AI coding agent : c'est un intermédiaire qui peut exercer la liberté technique au nom d'un utilisateur non technique. Quand vous dites à Claude ou Codex "fais en sorte que mon gestionnaire de tâches catégorise automatiquement les tweets que je sauvegarde", vous exercez la Liberté 1 — la liberté d'étudier et de modifier — via un proxy. Vous n'avez pas besoin de comprendre la base de code. Vous n'avez pas besoin de savoir ce qu'est un schéma GraphQL. Vous avez juste besoin de décrire ce que vous voulez, et l'agent exerce les libertés techniques pour vous.

Cela comble le fossé entre la liberté logicielle comme droit abstrait et la liberté logicielle comme capacité pratique. Les quatre libertés ont toujours été écrites comme si quelqu'un lirait éventuellement le code. En 2026, quelque chose peut finalement le faire, et peut le faire en votre nom.

Considérez ce que cela signifie pour une personne non technique coincée dans ma situation Sunsama. Aujourd'hui, elle a zéro options. Elle ne peut pas coder un contournement. Elle ne peut pas rétro-ingénierer une API. Elle peut soumettre une demande de fonctionnalité et attendre six ans. C'est tout. Sa relation avec le logiciel est une dépendance pure, et quand le logiciel ne fait pas ce dont elle a besoin, elle… vit avec. Quiconque a combattu avec un outil SaaS rigide qui est _presque_ juste mais pas tout à fait connaît ce sentiment intimement.

Maintenant donnez à cette personne un agent. Si le logiciel est free and open source, l'agent peut lire la base de code, comprendre le modèle de données, et faire exactement la modification dont l'utilisateur a besoin. Pas un contournement. Pas un hack. Une vraie modification de la façon dont le logiciel fonctionne, adaptée aux besoins spécifiques d'une personne. La personne qui n'aurait jamais pu écrire une ligne de code est maintenant, effectivement, un power user du plus haut niveau — parce que son agent peut l'être.

Mais si le logiciel est un SaaS propriétaire ? L'agent heurte les mêmes murs que moi. Pas de code source. Une API peut-être (presque certainement avec des rate limits et des opérations supportées limitées.) Sinon, aucun moyen d'entrer.

Cela rend la liberté logicielle bien moins académique et bien plus pratiquement pertinente qu'elle ne l'a été depuis des décennies. Pas juste pour moi (et elle est très pertinente pour moi !) mais de plus en plus pour tout le monde, techniquement compétent ou non. Les quatre libertés cessent d'être un droit théorique et commencent à être la différence pratique entre "mon agent a résolu ça pour moi en dix minutes" et "Espèce d'idiot, buffoon absolu. Tu crois que tu peux résoudre ton propre problème ?"

### Ce changement est déjà visible à travers de multiples penseurs qui voient les agents augmenter la valeur de l'ouverture

D'autres personnes commencent à connecter ces points, bien que depuis des angles différents.

En janvier 2026, Nawaz Dhandala chez OneUptime a écrit sur la façon dont les AI agents donnent aux logiciels open source un "avantage insurmontable" sur les alternatives closed-source, parce que les agents peuvent lire, comprendre et modifier le code source réel plutôt que d'être limités aux APIs approuvées par le vendeur. Son cadrage est utile : la question n'est plus "avons-nous l'expertise pour personnaliser cela ?" mais "voulons-nous le contrôle total sur notre stack logiciel ?"

Martin Alderson a fait un argument connexe, observant que de nombreuses choses pour lesquelles il aurait précédemment cherché un outil SaaS payant, il les fait maintenant résoudre par un agent "en quelques minutes, exactement comme je le veux." Il aborde aussi l'objection de la maintenance (ce qui me semble important), c'est-à-dire que les agents réduisent drastiquement les coûts de maintenance, et contrairement au seul ingénieur qui a construit votre outil interne puis a quitté l'entreprise, "les agents ne partent pas."

John Loeber a étendu l'argument en février 2026, prédisant une "grande rapatriation des données utilisateur de beaucoup de services fragmentés vers un seul endroit", parce qu'avoir vos données localement rend votre IA dramatiquement plus utile. Il a qualifié cela de "extrêmement encourageant pour les valeurs open source" et de "baissier pour les logiciels propriétaires."

Même Vitalik Buterin a pesé dans la balance, écrivant en juillet 2025 qu'il était passé de licences permissives au copyleft, arguant que "l'ouverture non nulle est la seule façon que le monde ne converge pas éventuellement vers un seul acteur contrôlant tout." Quand le gars qui a construit Ethereum vous dit que le consensus de licence permissive était faux, ça vaut au moins la peine d'y prêter attention.

### Le pendule peut revenir vers l'ouverture, mais la commodité et l'économie des mainteneurs comptent encore

Donc voilà où j'aimerais vous dire que la réponse est évidemment que nous devrions tous basculer vers des logiciels open source auto-hébergés et récupérer notre liberté informatique.

Mais je ne vais pas vous dire ça, parce que j'ai réellement auto-hébergé des logiciels avant, et je sais ce que ça coûte.

L'auto-hébergement signifie que vous êtes responsable des mises à jour de sécurité, des sauvegardes, des certificats SSL, du DNS, et de tout l'overhead opérationnel que les vendeurs SaaS gèrent pour vous. Et je n'ai déjà pas assez de temps. La raison pour laquelle j'utilise Sunsama est que j'essaie de mieux gérer mon temps. Ajouter "maintenir mon infrastructure auto-hébergée" à la liste des tâches va quelque peu à l'encontre du but.

Il y a aussi un contre-point alarmant qui mérite l'attention. Un working paper 2026 affilié à la CEU ("Vibe Coding Kills Open Source") soutient que le vibe-coding peut endommager l'open source en rompant la boucle de feedback utilisateur-mainteneur. Adam Wathan, créateur de Tailwind CSS, a rapporté que le trafic de documentation a chuté d'environ 40% depuis début 2023 même si l'utilisation de Tailwind a augmenté, et a dit que les revenus étaient en baisse d'environ 80% ; il a aussi dit que 75% de l'équipe d'ingénierie de Tailwind venait d'être licenciée. Mitchell Hashimoto, qui a créé Terraform, a publiquement dit qu'il envisageait de fermer les PR externes puis a déplacé Ghostty vers un modèle de contribution par cooptation en réponse à un flood de contributions IA de faible qualité.

Si les agents consomment du logiciel open source sans soutenir l'écosystème qui le crée, tout s'effondre. Les quatre libertés de Stallman nous disent ce que les utilisateurs méritent. Elles ne disent rien sur ce que les mainteneurs méritent. Ce fossé pourrait finir par compter plus que les libertés elles-mêmes.

Donc je ne pense pas que la réponse soit simplement "retournez à tout faire tourner vous-mêmes." Le modèle SaaS a résolu de vrais problèmes, et je ne veux pas abandonner les bénéfices. Et l'écosystème open source a des problèmes de durabilité que les agents pourraient aggraver avant de les améliorer.

Ce que je pense, c'est que nous allons avoir besoin de nouveaux modèles qui nous donnent les bénéfices de personnalisation du logiciel libre tout en préservant la commodité du SaaS. Je ne sais pas exactement à quoi ça ressemble encore. Peut-être des produits SaaS qui sont juste radicalement plus ouverts et extensibles que ce que nous avons aujourd'hui, avec de vrais systèmes de plugins et une couverture API complète et la capacité de faire tourner du code custom sur vos données. Ou peut-être qu'en 2027, Claude ou Codex sera capable non seulement d'écrire mais aussi d'héberger et d'opérer des logiciels.

Honnêtement, c'est TBD. L'industrie n'a pas encore résolu ça. Mais je pense que la demande va devenir très forte, parce que les agents vont rendre le coût des logiciels fermés extrêmement visible.

### Le prochain critère d'achat sera de savoir si votre agent peut réellement changer le logiciel pour l'adapter à vos besoins

Je pense aussi qu'au cours des 1 à 2 prochaines années nous allons voir un changement significatif dans la façon dont les gens évaluent les logiciels. "Mon agent peut-il entièrement personnaliser ça ?" va devenir une vraie question que les gens normaux posent, de la même façon que nous demandons actuellement "est-ce qu'il a une application mobile ?" ou "est-ce qu'il s'intègre avec Slack ?"

Je ne voudrais certainement pas être le CTO d'un SaaS legacy qui vit de l'hypothèse que les "switching costs" lui permettront de continuer à forcer les utilisateurs dans une UX douteuse et des workflows rigides.

John Gilmore a dit fameux que "le Net interprète la censure comme des dommages et la contourne." Je pense que nous sommes sur le point de voir une version de cela pour les logiciels fermés. À mesure que les agents deviennent la façon principale dont les gens interagissent avec leurs outils, ils vont interpréter les logiciels non libres comme des dommages — comme un obstacle entre l'utilisateur et ce que l'utilisateur veut — et les contourner. Parfois ça voudra dire rétro-ingénierer des APIs comme Robert Niimi l'a fait pour Sunsama. Parfois ça voudra dire que les agents construisent des remplacements open source légers à la volée. Parfois ça voudra juste dire déposer des demandes RGPD-style "télécharger mes données" au nom des utilisateurs et reconstruire entièrement un remplaçant personnalisé de zéro.

Dans mon rôle de CTO d'Upwave, je suppose aussi que l'ère où nos logiciels sont utilisés par des humains touche à sa fin, et je nous oriente vers la construction de capacités aussi faciles que possible pour que les AI agents les intègrent (et le fassent de la façon que leurs utilisateurs préfèrent.) Nous ne prévoyons pas encore de laisser les utilisateurs modifier directement le code analytique ou les data pipelines qui tournent sur nos serveurs, mais honnêtement... peut-être que nous devrions.

Je ne voudrais certainement pas être le CTO d'une entreprise SaaS qui n'a pas un véritable moat de type "7 powers" — un fort effet de réseau, un dataset propriétaire (la force d'Upwave,) une capture réglementaire, etc. Si la seule chose qui maintient les utilisateurs sur votre plateforme est la commodité et les switching costs, vous êtes en difficulté, parce que les agents vont effondrer les switching costs vers zéro.

En net, je pense que le pendule du logiciel libre est sur le point de balancer. Pas parce que les gens se sont soudainement convertis à l'église de la liberté logicielle, mais parce qu'ils veulent que leurs agents les aident réellement, et les agents ne peuvent pas aider quand le logiciel est verrouillé.

J'aime vraiment Sunsama. Je ne veux pas changer. Mais quand je peux voir, concrètement, que mon agent aurait pu résoudre mon problème tweet-to-task en dix minutes avec du logiciel libre et open source. Au lieu de ça j'ai passé un après-midi à construire une machine de Rube Goldberg autour de six couches de systèmes fermés. Et ça change ma façon de penser à quel logiciel je suis prêt à dépendre.

## Pourquoi ça compte

Cet article offre le cadre le plus concret à date pour comprendre pourquoi les AI agents vont transformer la valeur économique du logiciel libre — non plus comme principe idéologique, mais comme avantage compétitif mesurable : un logiciel que l'agent peut modifier directement vs. un SaaS fermé qui oblige à six couches de contournements. Pour les équipes tech et les CTOs, c'est un signal fort que "API-first" et "agent-compatible" vont devenir des critères de sélection logicielle aussi déterminants que la sécurité ou la scalabilité.
