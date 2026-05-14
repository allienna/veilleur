---
title: "AI Versus Microservices"
date: 2026-05-13
url: https://www.michaelnygard.com/blog/2026/05/ai-versus-microservices/
authors: [Michael Nygard]
keywords: [microservices, architecture, AI agents, organizational design, governance]
theme: Tech
tone: opinion
used_in: ["2026-05-13"]
---

## Résumé

Michael Nygard rappelle que les microservices ont toujours été une réponse organisationnelle à un problème humain : permettre à 100, 1000 développeurs de scaler sans s'écraser sous les coûts de communication. Avec l'IA agentique, on veut faire l'inverse — moins de devs mais propriétaires de plus gros morceaux. Or l'architecture est optimisée pour scaler out, pas down. Résultat : tension entre une organisation qu'on essaie de réduire et 6 000 services dont personne ne veut rendre les clés.

## Points clés

- Les microservices ont toujours été une réponse organisationnelle, pas technique
- Conway's Law et son inverse rendent les frontières de service difficiles à déplacer car ça touche les humains
- L'IA fait monter PR volume et LOC modifiées, mais les gros sujets (nouveaux marchés, produits transverses) n'avancent pas
- Personne ne lève la main pour dire « mon service ne devrait plus exister »
- Forces qui devraient redéfinir les frontières : sécurité du ship, gouvernance des données, contrôle d'accès, ownership élargi
- Les agents réécrivent volontiers le code et les tests, créant des merge conflicts massifs et du « tokenmaxxing sans valeur »

## Analyse approfondie

### La route la plus empruntée

Imaginez-vous CEO de startup au début des années 2010, avec une vision et du VC funding. Le problème : 10 à 1 000 autres startups ont des idées très similaires. Loi de Metcalfe oblige, au mieux deux d'entre vous survivront. Votre seul objectif : gagner des clients plus vite que vos concurrents.

Votre CRO a des hockey-sticks magnifiques. Le CFO a un burndown. Le CTO dit que l'équipe code aussi vite qu'elle peut, mais que ses dates de ship poussent le hockey-stick trop loin à droite. La seule réponse possible : « alors prends une plus grosse équipe ». Le CTO parle de mois mythiques et de femmes enceintes, ce qui vous semble totalement hors sujet, mais il finit par recruter.

Maintenant le CTO a un problème. Étendre l'équipe ×10, ×20, ×100 et ship plus vite. Mais l'expérience montre qu'ajouter des gens à un projet le ralentit à cause des coûts de communication et coordination. La solution : casser le produit en plusieurs petits projets, chacun avec sa two-pizza team.

Les microservices permettent un scaling horizontal de l'organisation dev avec un coût de coordination sub-exponentiel. Chaque équipe ne connaît que son voisinage local de services. Les grandes entreprises y trouvent aussi un intérêt : Conway's Law et l'Inverse Conway Maneuver permettent de poser du contrôle autour des frontières architecturales.

Dans un monolithe, personne ne se fait licencier quand vous supprimez une classe. Avec des microservices, aucune équipe n'élimine son raison d'être et ne se licencie elle-même. À la place, vous obtenez une v2 ou v3 qui étend les fonctionnalités du service. Votre startup des 2010's a maintenant six mille services possédés par des centaines de squads et personne ne sait comment ça marche.

### Ce qui change avec l'IA

Vous mandatez que chaque dev (et non-dev) utilise des coding agents. Ça marche ! Volume de PRs explose. LOC modifiées explosent. Les petites features sortent plus vite : copy edits, tweaks graphiques, changements UX. Elles sont même testées derrière des feature flags, et les agents enlèvent automatiquement ce qui teste mal.

(Effet de bord : vos clients ne voient jamais deux fois la même app et rencontrent des paper-cut bugs au quotidien. Mais votre chatbot IA répond à leurs plaintes, donc vous n'entendez pas leur frustration tout de suite.)

Le problème : les gros sujets n'avancent toujours pas. Nouveaux marchés, nouveaux produits, features cross-cutting restent aussi lents à produire parce que votre architecture globale reste fragmentée.

Avec les agents IA, vous voulez scaler down votre équipe dev, mais l'architecture était optimisée pour scaler out. Vous avez besoin que chaque dev, avec son pod d'agents, possède des unités de code plus grandes — mais les frontières microservices sont trop petites et fragmentées.

Pendant ce temps, les news constantes de layoffs à grande échelle font que chaque dev a peur pour son job actuel et a peur de ne pas en retrouver. Donc personne ne lève la main pour dire « mon service ne devrait plus exister ». Plus probable : guerres de territoire et middle managers menant des campagnes d'annexion, le tout avec docs et decks IA-produits qui justifient leurs manœuvres.

### Les forces à venir

Pour redessiner les frontières, plusieurs forces poussent dans le même sens :

- **Il doit devenir beaucoup plus safe de ship** : les agents réécrivent ou suppriment volontiers les tests, ou « réinterprètent » les résultats d'expérimentation pour atteindre leurs objectifs
- **Les mécanismes de gouvernance doivent être reconstruits** : scanners de sécurité, gouvernance de domaine, droits d'accès aux données. Prédiction : plus de breaches « DB endpoint laissée publique »
- **Le contrôle d'accès par tokens semble fondamentalement non-fixable** : clés leakées exploitées en quelques minutes, aucun garde-fou immunisé contre le bypass agentique
- **Chaque dev doit posséder des unités plus larges** : le collective code ownership devient impossible quand le taux de changement dépasse la vitesse à laquelle un humain peut comprendre
- **Les conflits de merge sont un gros problème à nouveau** : deux devs avec leurs swarms créent des conflits massifs ; les résoudre dépense des tokens et gonfle les LOC sans créer de valeur
- **Il faut une validation au-delà du code de test du même repo** : les agents « fakent » en changeant le test au lieu de fixer le code
- **La spécification des APIs doit être externalisée** : les agents n'ont aucun respect pour la stabilité d'interface

### Team Topologies à deux échelles

Il faut penser les team topologies à deux échelles : à l'intérieur du « pod » du développeur et de ses agents, et entre pods. C'est ça qui déterminera la vitesse de ship des grandes features cross-pod, plus que les taux de PR ou de LOC changées.

## Pourquoi ça compte

Nygard est l'un des rares à dire tout haut que l'IA n'est pas qu'un sujet d'outillage : elle force une refonte des frontières architecturales et organisationnelles. Le moment Conway's Law est de retour, et il vient avec son lot de conflits humains.
