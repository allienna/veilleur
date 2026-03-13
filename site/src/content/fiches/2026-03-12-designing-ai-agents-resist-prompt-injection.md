---
title: "Designing AI agents to resist prompt injection"
date: 2026-03-12
url: "https://links.tldrnewsletter.com/IifO3y"
authors: ["OpenAI"]
keywords: ["prompt injection", "social engineering", "sécurité agents", "défense en profondeur", "manipulation"]
theme: "Sécurité"
tone: "research"
used_in: ["2026-03-12"]
---

## Résumé

OpenAI publie son analyse de l'évolution de la prompt injection : les attaques les plus efficaces ressemblent désormais à du social engineering plutôt qu'à de simples injections de commandes. L'article défend une approche de défense en profondeur — concevoir les systèmes pour que l'impact d'une manipulation reste contenu, même si certaines attaques réussissent.

## Points clés

- Les attaques par prompt injection évoluent vers du social engineering sophistiqué, pas de simples overrides
- Le filtrage des entrées ("AI firewalling") ne suffit pas car détecter une attaque revient à détecter un mensonge
- La défense efficace repose sur le design du système : limiter l'impact même si la manipulation réussit
- OpenAI compare le modèle à un employé de service client : même manipulé, ses actions doivent rester bornées
- L'approche privilégiée est la défense en profondeur plutôt que la détection parfaite

## Analyse approfondie

### L'évolution de la prompt injection vers le social engineering

Les premières attaques par prompt injection étaient rudimentaires : éditer un article Wikipedia pour y inclure des instructions directes aux agents IA qui le visitaient. Les modèles, sans expérience d'un environnement adversarial à l'entraînement, suivaient souvent ces instructions sans question. Mais à mesure que les modèles sont devenus plus intelligents, les attaques ont évolué pour intégrer des éléments de social engineering — des techniques de manipulation qui ne reposent plus sur une simple chaîne malveillante mais sur du contenu trompeur en contexte.

L'article souligne que les systèmes de type « AI firewalling », où un intermédiaire tente de classifier les entrées en malveillantes ou légitimes, échouent face à ces attaques sophistiquées. Le problème de détection devient équivalent à celui de détecter un mensonge ou de la désinformation, souvent sans le contexte nécessaire.

### Le modèle de l'agent de service client

OpenAI propose une analogie éclairante : l'agent IA existe dans un système à trois acteurs similaire à un employé de service client. L'agent veut agir au nom de son employeur, mais est continuellement exposé à des inputs externes qui tentent de le tromper. Un client peut prétendre qu'un remboursement n'a pas été effectué, ou menacer de représailles. Dans le monde réel, l'agent humain dispose de règles mais aussi de systèmes déterministes qui limitent le nombre de remboursements possibles, signalent les emails de phishing, et contraignent l'impact d'une compromission individuelle.

### La défense déployée dans ChatGPT : Safe Url

OpenAI combine ce modèle de social engineering avec des approches classiques d'ingénierie de sécurité, notamment l'analyse source-sink. Un attaquant a besoin d'une source (un moyen d'influencer le système) et d'un sink (une capacité dangereuse dans le mauvais contexte). Pour les agents, cela signifie combiner du contenu externe non fiable avec une action comme la transmission d'informations à un tiers.

La plupart des attaques contre ChatGPT tentent de convaincre l'assistant de transmettre des informations sensibles de la conversation à un tiers malveillant. Dans la majorité des cas, le safety training du modèle provoque un refus. Pour les cas restants, OpenAI a développé la mitigation « Safe Url » : quand de l'information apprise dans la conversation serait transmise à un tiers, le système affiche l'information à l'utilisateur et demande confirmation, ou bloque l'action et demande à l'agent de trouver une autre approche.

## Pourquoi ça compte

À mesure que les agents IA gagnent en autonomie (navigation web, actions pour l'utilisateur), la surface d'attaque par prompt injection explose. Cet article d'OpenAI pose un cadre de réflexion essentiel pour quiconque déploie des agents en production.
