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

Des hackers attribués à la Corée du Nord ont compromis le compte npm du mainteneur de la librairie Axios — la librairie HTTP JavaScript la plus populaire avec plus de 200 millions de téléchargements hebdomadaires — pour distribuer un RAT (Remote Access Trojan) cross-platform ciblant macOS, Windows et Linux.

## Points clés

- Le compte npm du mainteneur d'Axios a été compromis, permettant la publication de versions malveillantes
- Le malware distribué est un RAT cross-platform ciblant macOS, Windows et Linux simultanément
- L'attaque est attribuée à des hackers nord-coréens, selon les chercheurs en sécurité
- Un simple `npm install` sur une version compromise suffisait pour être infecté
- L'incident illustre la fragilité du modèle de confiance de l'écosystème npm, où un seul compte compromis peut impacter des millions de projets

## Analyse approfondie

Des hackers, que les chercheurs en sécurité attribuent à la Corée du Nord, ont réussi à compromettre le compte npm du mainteneur de la librairie Axios, l'une des librairies les plus utilisées de l'écosystème JavaScript. Avec plus de 200 millions de téléchargements hebdomadaires, Axios est une dépendance critique pour des millions de projets à travers le monde.

L'attaque a consisté à publier des versions malveillantes de la librairie contenant un Remote Access Trojan (RAT) cross-platform. Le malware ciblait simultanément macOS, Windows et Linux, démontrant une sophistication technique notable. Un développeur effectuant un `npm install` ou une mise à jour de ses dépendances pouvait se retrouver infecté sans aucun signe visible.

Ce type d'attaque par supply chain est particulièrement redoutable car il exploite la confiance inhérente au système de packages. Les développeurs font confiance aux librairies qu'ils utilisent quotidiennement, et les mises à jour mineures passent souvent sans revue. L'écosystème npm, malgré ses mécanismes de sécurité (2FA, provenance), reste vulnérable dès qu'un seul compte mainteneur est compromis.

L'attribution à la Corée du Nord s'inscrit dans une tendance documentée : les groupes Lazarus et apparentés ciblent de plus en plus les supply chains logicielles comme vecteur d'attaque, que ce soit pour l'espionnage industriel ou le financement du régime via le vol de cryptomonnaies.

## Pourquoi ça compte

Cet incident rappelle la fragilité structurelle des écosystèmes de packages open source. Quand une seule librairie utilisée par des millions de projets peut être empoisonnée via un compte compromis, c'est tout le modèle de confiance de la supply chain logicielle qui est en question.
