---
title: "North Korean hackers blamed for hijacking popular Axios open source project to spread malware"
date: 2026-04-01
url: "https://techcrunch.com/2026/03/31/hacker-hijacks-axios-open-source-project-used-by-millions-to-push-malware/"
authors: ["TechCrunch"]
keywords: [supply chain, npm, Axios, Corée du Nord, malware, open source]
theme: "Tech"
tone: "news"
used_in: ["2026-04-01"]
---

## Résumé

Des hackers nord-coréens ont compromis le compte npm du mainteneur de la librairie Axios — l'une des plus populaires de l'écosystème JavaScript avec plus de 200 millions de téléchargements hebdomadaires — pour distribuer un RAT (Remote Access Trojan) cross-platform ciblant macOS, Windows et Linux. L'attaque illustre la fragilité des supply chains open source quand un seul compte compromis peut affecter des millions de projets en aval.

## Points clés

- Le compte npm du mainteneur d'Axios a été compromis par des acteurs attribués à la Corée du Nord
- Le malware distribué était un RAT cross-platform ciblant macOS, Windows et Linux simultanément
- Axios cumule plus de 200 millions de téléchargements hebdomadaires sur npm
- Un simple `npm install` suffisait pour être infecté
- L'attaque s'inscrit dans une tendance croissante de compromission de la supply chain open source

## Analyse approfondie

Des hackers attribués à la Corée du Nord ont réussi à compromettre le compte npm du mainteneur principal de la librairie Axios, l'une des bibliothèques HTTP les plus utilisées de l'écosystème JavaScript. Axios est une dépendance critique pour des centaines de milliers de projets, avec plus de 200 millions de téléchargements hebdomadaires sur le registre npm.

L'attaque a consisté à publier une version malveillante de la librairie contenant un RAT (Remote Access Trojan) conçu pour fonctionner sur trois plateformes simultanément : macOS, Windows et Linux. Le malware était intégré de manière à s'exécuter silencieusement lors de l'installation du package via `npm install`, sans nécessiter d'interaction supplémentaire de la part du développeur.

Le RAT permettait aux attaquants d'obtenir un accès distant complet aux machines infectées, incluant l'exécution de commandes, l'exfiltration de données et la persistance sur le système. La nature cross-platform du malware montre une sophistication croissante des attaques supply chain, visant à maximiser la surface d'impact indépendamment du système d'exploitation des développeurs ciblés.

L'incident met en lumière un problème structurel de l'écosystème open source : la sécurité de millions de projets repose sur les comptes individuels de mainteneurs, souvent bénévoles, qui peuvent être compromis par des techniques classiques de social engineering ou de credential stuffing. Un seul point de défaillance — un compte npm — peut transformer une librairie de confiance en vecteur d'attaque massif.

Cette attaque s'inscrit dans une stratégie plus large des groupes nord-coréens qui ciblent de plus en plus les supply chains logicielles. Plutôt que d'attaquer directement les entreprises une par une, la compromission d'un composant open source critique permet d'atteindre des dizaines, voire des centaines de cibles en aval en une seule opération.

## Pourquoi ça compte

L'attaque Axios démontre que la supply chain open source est devenue un vecteur d'attaque stratégique pour des acteurs étatiques. Quand une librairie utilisée par des millions de développeurs peut être compromise via un seul compte, la question n'est plus "si" mais "quand" la prochaine attaque aura lieu — et elle touche directement l'infrastructure IA qui repose massivement sur npm.
