---
title: "Some uncomfortable truths about AI coding agents"
date: 2026-03-30
url: https://standupforme.app/blog/some-uncomfortable-truths-about-ai-coding-agents/
authors: [Joel Andrews]
keywords: [AI agents, coding agents, LLM limitations, software engineering, vibe coding]
theme: IA
tone: opinion
used_in: ["2026-03-30"]
---

## Résumé

Joel Andrews, développeur indépendant avec deux décennies d'expérience, expose sans détour pourquoi il refuse d'utiliser les AI coding agents pour du code de production professionnel. Son analyse porte sur quatre problèmes structurels : l'atrophie des compétences des ingénieurs, le coût artificiellement bas des modèles génératifs, la vulnérabilité aux prompt injections, et les incertitudes juridiques liées au copyright. Loin d'un rejet de principe, l'auteur reconnaît la puissance de ces outils tout en dénonçant la façon dont l'industrie en minimise les risques réels. Il conclut que les LLMs restent utiles comme outils de recherche et d'exploration, mais pas comme générateurs de code de production.

## Points clés

- L'adoption des AI coding agents entraîne une atrophie des compétences de développement, même chez les ingénieurs chargés de la revue de code
- Les modèles d'IA générative sont massivement déficitaires et leurs prix actuels sont déconnectés de leurs coûts réels — une correction brutale est inévitable
- Le prompt injection est un problème fondamental et structurel des LLMs, non un bug corrigeable, qui devient critique avec les agents autonomes
- Aux États-Unis, la sortie d'un modèle génératif n'est pas protégée par le copyright — le code produit par un agent appartient au domaine public
- Les LLMs restent pertinents pour la recherche, l'exploration de nouvelles APIs, et pour les non-développeurs qui ne visent pas à construire un business
- La spécification humaine du travail à accomplir est couverte par le copyright, mais pas le code généré — une asymétrie juridique dangereuse pour les entreprises

## Analyse approfondie

### Introduction

L'auteur suit le développement de l'IA générative depuis plusieurs années. Initialement impressionné par ce qu'OpenAI a accompli à partir d'un article de recherche en deep learning de Google et d'un peu de reinforcement learning from human feedback, il a longtemps essayé de ne pas sauter aux conclusions. Après mûre réflexion, il est prêt à rendre son verdict : les AI coding agents basés sur des LLMs n'ont pas leur place, maintenant ni jamais, pour générer du code de production dans son travail professionnel.

L'article s'inscrit dans le contexte de l'essor apparemment météoritique des AI coding agents, qui prennent un LLM sujet aux hallucinations et ajoutent une boucle de feedback permettant des résultats impressionnants. Des entreprises entières se construisent sur ce pari, et des acteurs établis comme Notion, Spotify ou Stripe semblent pleinement convaincus — après tout, pourquoi laisser des humains travailler pendant des heures quand un agent peut faire plus vite et moins cher ?

Quatre problèmes principaux motivent son interdiction absolue des AI coding agents dans son travail professionnel : l'atrophie des compétences, le coût artificiellement bas, les prompt injections, et le copyright/licensing.

### Atrophie des compétences

Le problème le plus facile à comprendre, mais aussi le plus difficile à quantifier. Il devient évident que le métier d'ingénieur logiciel évolue radicalement. Certains décrivent la nouvelle fonction comme celle d'un "software engineering manager" : on n'écrit plus soi-même de code, on supervise une équipe d'AI coding agents comme s'il s'agissait d'une équipe de juniors. Les agents font des erreurs, dit-on, mais les ingénieurs expérimentés passent en revue chaque ligne produite pour s'assurer que tout est correct.

Même en acceptant cette affirmation pour valide aujourd'hui, l'auteur soutient que les ingénieurs relégués à la revue de code deviendront rouillés au fil du temps. Leurs compétences en développement et en conception logicielle vont s'atrophier. Même avec les meilleures intentions, ils perdront progressivement la capacité à distinguer un bon changement d'un mauvais — parce qu'ils ont cessé d'écrire du code eux-mêmes. La pratique et les retours des pairs sont essentiels pour maintenir et faire progresser ses connaissances, mais les ingénieurs dans cette position n'en bénéficieront plus.

En réalité, la charge de revue de code augmentera progressivement à mesure que de moins en moins d'ingénieurs supervisent un nombre toujours croissant d'agents. La complaisance deviendra inévitable — par pure nécessité sanitaire. L'auteur est partisan de la revue de code pour partager la compréhension entre ingénieurs, mais même lui considère souvent la revue d'une grosse PR comme un effort épuisant. Si c'est le travail à plein temps de quelqu'un de passer en revue le travail d'une nuée d'agents, et que l'expérience montre qu'ils ont raison 95% du temps, on ne fera plus suffisamment attention et de mauvais changements passeront. C'est vrai de toutes les revues de code, mais au moins on peut faire confiance à ses collègues humains qu'ils ont de bonnes intentions et qu'ils peuvent apprendre de leurs erreurs. Et on peut leur demander directement pourquoi ils ont implémenté quelque chose d'une certaine façon. Il n'y a aucun moyen de savoir d'où le LLM a tiré l'inspiration pour ce bloc de code compliqué. On peut le lui demander, mais il ne fera qu'inventer une réponse plausible — parce qu'il ne le sait pas vraiment.

L'auteur reconnaît que son point de vue sur ce sujet ressemble peut-être au classique "Old Man Yells at Cloud". Il fait le parallèle avec les anciens qui se plaignaient de la prolifération des langages de haut niveau, prédisant qu'une génération de programmeurs manquerait des bases fondamentales. Ils avaient globalement tort : de nombreux ingénieurs compétents aujourd'hui ne comprennent pas vraiment comment leur runtime alloue et libère la mémoire, sans que cela les empêche de construire des choses utiles. Sa seule défense : "cette fois, c'est différent" — pas particulièrement rigoureux, il l'admet, mais c'est le plus flou des problèmes soulevés.

### Coût artificiellement bas

C'est le domaine où l'auteur se sent le moins qualifié, mais il est convaincu que le problème existe et que personne n'a de solution.

L'idée que nous sommes au milieu d'une bulle de l'IA générative, prête à éclater, est un argument populaire chez les sceptiques. La technologie ne justifie pas le battage médiatique et le robinet à argent finira par se fermer. Les grandes entreprises tech investissent des sommes colossales en GPU, mémoire, stockage et entrepôts pour construire des data centers pour entraîner et faire tourner ces modèles, mais elles peinent à justifier ces dépenses énormes. Libérer les gens de la rédaction d'emails de remplissage est pratique, mais ce n'est pas la killer feature qui justifie les coûts astronomiques. C'est pourquoi, depuis un an environ, elles se sont accrochées aux AI coding agents comme "preuve" que leurs investissements massifs se justifient.

La réalité froide : les modèles d'IA générative sont massivement déficitaires pour les entreprises qui les entraînent et les opèrent. Les AI coding agents n'améliorent pas la situation — ils aggravent même le problème en encourageant une utilisation significativement plus importante. Les grandes entreprises tech suivent le modèle classique de la Silicon Valley : construire d'abord, trouver comment gagner de l'argent ensuite. Elles semblent croiser les doigts en espérant des innovations de l'ordre de l'article original Attention Is All You Need. Elles ont désespérément besoin d'une invention miraculeuse pour améliorer l'efficacité économique de leurs modèles d'IA, ou mieux encore, de découvrir la recette secrète de l'AGI. En l'absence de telles innovations, la bulle éclatera inévitablement. Des géants comme Google et Meta ont des réserves suffisantes pour traverser la tempête, mais les acteurs qui n'ont pas d'autres activités devront soudainement trouver un moyen de gagner vraiment de l'argent ou périr.

Aujourd'hui, les prix pour l'utilisateur final des modèles d'IA générative sont complètement déconnectés du coût réel de l'entraînement et de l'exploitation. Il faudrait des hausses de prix d'un ordre de grandeur et des limites d'utilisation beaucoup plus drastiques, dans le meilleur des cas. Et ce n'est pas que les entreprises qui construisent les modèles fondamentaux : tous ces intermédiaires qui ont construit leur activité en offrant des outils alimentés par des modèles d'IA générative à prix artificiellement bas se retrouveront dans une situation délicate quand leurs coûts monteront en flèche. Le rayon de souffle sera large. Beaucoup ne survivront pas.

Certains pourraient arguer que, même si ce moment viendra, ce n'est pas une raison de ne pas profiter des outils disponibles maintenant. L'auteur n'est pas de cet avis : mieux vaut ne pas devenir trop dépendant des AI coding agents dès le départ, pour être mieux positionné quand la tempête arrivera.

### Prompt injection

Le prompt injection est désormais un problème bien connu dans les LLMs. En résumé : les LLMs sont intrinsèquement crédules, à tel point qu'un individu suffisamment motivé peut les amener à dire ou faire quelque chose qu'ils ne sont "censés" pas faire en concevant soigneusement les inputs. Le travail d'un LLM est simplement de prédire le prochain token dans une chaîne de texte en expansion, et leur absence de véritable raisonnement signifie qu'ils peinent à différencier les prompts légitimes des instructions sournoisement enfouies dans le contexte. Tous les grands fournisseurs de LLMs ont fait des progrès pour corriger ce comportement, mais ces correctifs n'ont fait que colmater des fuites dans un navire qui coule. Tout indique que la classe de vulnérabilité connue sous le nom de prompt injection exploite un comportement fondamental du fonctionnement des LLMs. En d'autres termes, l'incapacité fondamentale des LLMs à distinguer de manière fiable les instructions des données est un problème qui a très peu de chances d'être jamais entièrement résolu.

Jusqu'ici, l'industrie n'a eu à faire face aux prompt injections que dans la perspective d'un utilisateur dans une session de chat en tête-à-tête avec un LLM, essayant de le libérer de ses system prompts pour lui faire dire des choses que l'opérateur n'avait pas prévu d'autoriser. Mais avec la propagation rapide des AI coding agents, il n'est qu'une question de temps avant que des acteurs malveillants ne lancent des campagnes coordonnées pour empoisonner des sites web sous leur contrôle et inonder les boîtes de réception d'instructions LLM malveillantes. L'agent de codage tombera alors sur ces instructions malveillantes en cherchant des exemples de résolution de problème sur le web ou en fouillant la boîte de réception pour des emails pertinents.

Et ce n'est pas seulement les coding agents : chaque type d'AI agent avec la capacité de récupérer du contexte depuis des sources non fiables est vulnérable. Si un agent fonctionne avec des restrictions suffisamment souples (comme ils le font tous de nos jours), les dégâts pourraient être véritablement catastrophiques : dans de nombreux cas, attendez-vous à rien de moins qu'une compromission complète de votre système et de tous vos comptes connectés. Bruce Schneier a utilement baptisé cette nouvelle classe d'attaque "promptware". Attendez-vous à en voir beaucoup dans les années à venir, à mesure que les acteurs malveillants trouvent des façons de plus en plus originales d'injecter sournoisement leurs prompts malveillants dans le contexte d'un agent.

Même sans menaces d'acteurs malveillants, on court le risque que l'agent hallucine ou perde le fil et décide qu'il est bon de supprimer des fichiers, des bases de données ou des emails. Le risque n'en vaut pas la peine.

### Copyright/licensing

L'auteur précise qu'il n'est pas juriste. Voici son évaluation non qualifiée de quelques questions juridiques délicates.

Aux États-Unis au moins, la sortie d'un modèle d'IA générative n'est pas protégeable par le copyright.

Ce point est d'une importance capitale : quand on passe tout ce temps à rédiger les spécifications parfaites et qu'on les soumet à un modèle d'IA, le code qu'il produit appartient, au mieux, au domaine public. On ne le possède pas. Personne ne le possède. Ou peut-être est-il plus juste de dire que le monde entier le possède.

Le U.S. Copyright Office a statué que la production d'une IA générative ne peut pas être protégée par le copyright. Depuis, la question a été portée devant les tribunaux américains qui ont confirmé cette décision, jusqu'à la Cour Suprême, qui a refusé d'intervenir, laissant les décisions des juridictions inférieures en vigueur : toute production d'une IA générative n'est pas protégée par le copyright. C'est certes uniquement aux États-Unis, mais ce pays reste une force politique et économique très puissante, et il n'est pas exagéré de supposer qu'au moins certains autres pays avec des définitions similaires du copyright arriveront à la même conclusion dans un avenir prévisible.

Pour illustrer, l'auteur imagine un monde hypothétique où Notion aurait utilisé des AI coding agents dès le début et que ces agents auraient produit tout le code de son logiciel de productivité. Tout ce code hypothétique appartiendrait techniquement à tout le monde aujourd'hui. Si un employé décidait de publier ce code source quelque part en ligne, le monde entier aurait soudainement un accès totalement libre pour en faire ce qu'il voudrait. Il n'est même pas certain que l'entreprise aurait un mécanisme juridique pour empêcher un employé d'exercer son droit fondamental de distribuer quelque chose qui appartient légalement au domaine public. Les NDA protègent les secrets commerciaux, mais peuvent-ils être utilisés pour empêcher un employé de partager quelque chose qui, de droit, appartient à tout le monde ?

Dans le monde réel, jusqu'à récemment, tout le code de Notion était écrit par des humains. Si un employé publiait le code propriétaire de Notion en ligne, ce code serait juridiquement très compromettant. Un concurrent qui l'incorporerait dans ses propres produits risquerait des sanctions légales et financières catastrophiques. Le copyright à la rescousse. Et le fait qu'un employé devrait violer son NDA pour publier le code agirait comme un dissuasif efficace.

Mais dans le monde hypothétique imaginé, n'importe qui pourrait démarrer des serveurs exécutant le code publié et lancer un concurrent direct — en sautant complètement les années que la société a passées à guider soigneusement ses AI coding agents pour construire une suite de productivité performante et compétitive. Le nouveau concurrent devrait maintenir sa propre branche du code pour corriger les bugs et ajouter des fonctionnalités, mais c'est à ça que servent les AI coding agents, non ?

Certains argueront que, si une entreprise hypothétique avait utilisé des AI coding agents pour produire à moindre coût tout le code d'une application moderne, le code lui-même n'est pas si important ou précieux de toute façon — ce ne serait pas grave qu'un concurrent utilise ses propres agents pour construire son concurrent. Mais cela ignore complètement tout le travail qui doit encore aller dans la recherche d'un problème, les discussions avec les pairs et la rédaction de spécifications pour qu'un agent puisse les transformer en code fonctionnel, ainsi que tout le raffinement et les révisions qui suivent. L'ingénierie logicielle restera un processus chronophage même si l'écriture de code n'est pratiquement plus un facteur. Ironiquement, les spécifications que les ingénieurs passent tout ce temps à écrire et à soumettre aux AI coding agents seraient probablement couvertes par le copyright, mais cela serait complètement sans importance pour protéger les intérêts de l'entreprise. Grâce à l'utilisation d'AI coding agents par cette entreprise hypothétique, un concurrent pourrait légalement sauter tout le temps et le travail difficile traditionnellement nécessaires pour s'établir.

La question du copyright devient significativement plus complexe quand une base de code est un mélange de code humain et de code généré par IA, ce qui pourrait donner aux entreprises suffisamment de couverture légale tant qu'elles maintiennent un certain niveau de code humain. Ou peut-être que les gouvernements du monde entier amenderont progressivement leurs définitions du copyright pour attribuer la propriété de la production d'une IA générative à la personne ou l'organisation qui a rédigé les prompts — ce qui ne sera pas une mince affaire tant que la Convention de Berne et l'Accord TRIPS existent. L'auteur préfère laisser les humains écrire la majorité ou la totalité du code dès le départ, et éviter toutes les incertitudes juridiques que crée le fait de laisser les bots le faire.

### Alors, à quoi servent les LLMs ?

La recherche ! Mais seulement à condition de vérifier soigneusement tout ce qu'un LLM dit. Quand on rencontre un nouveau package ou une nouvelle API qu'on connaît peu, pouvoir demander à un LLM de générer un exemple de code est absolument brillant. Cela dit, ils font suffisamment d'erreurs pour qu'on ne puisse pas copier-coller directement dans de nombreux cas.

Aussi, à mesure que les AI coding agents arrivent à maturité et implémentent réellement des garanties d'isolation complètes pour les empêcher de devenir incontrôlables et de supprimer tous vos emails, ils pourraient être un formidable outil pour les non-développeurs qui veulent donner vie à leurs idées — à condition que ces utilisateurs ne souhaitent pas construire un business sur les résultats. Ou même pour des développeurs expérimentés qui n'ont pas le temps de construire manuellement tous leurs projets personnels récréatifs.

### Conclusion

Malgré son malaise avec eux, l'auteur est convaincu que les LLMs en général et les AI coding agents en particulier sont là pour rester, sous une forme ou une autre. Mais si cet article convainc certaines personnes de réfléchir plus critiquement aux avantages et inconvénients de la technologie, il aura atteint son objectif.

## Pourquoi ça compte

Dans un contexte où l'industrie célèbre unanimement le "vibe coding" et les agents autonomes, cet article offre une contre-voix argumentée et documentée, soulevant des risques réels — juridiques, sécuritaires et économiques — que les équipes d'ingénierie devraient sérieusement évaluer avant d'adopter massivement les AI coding agents en production. La question du copyright sur le code généré par IA est en particulier sous-estimée et mérite l'attention des décideurs techniques.
