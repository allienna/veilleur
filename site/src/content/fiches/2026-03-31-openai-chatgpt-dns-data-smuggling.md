---
title: "OpenAI patches ChatGPT flaw that smuggled data over DNS"
date: 2026-03-31
url: https://www.theregister.com/2026/03/30/openai_chatgpt_dns_data_snuggling_flaw/
authors: [The Register, Thomas Claburn]
keywords: [ChatGPT, exfiltration DNS, prompt injection, sécurité IA, Check Point]
theme: IA (Sécurité)
tone: news
used_in: ["2026-03-31"]
---

## Résumé

Des chercheurs de Check Point ont découvert une vulnérabilité dans ChatGPT permettant à un simple prompt malveillant d'exfiltrer des données utilisateur via un canal DNS caché, contournant les protections réseau d'OpenAI qui bloquaient le trafic web sortant mais ignoraient le DNS. Le modèle lui-même ne reconnaissait pas cette exfiltration comme un transfert de données externe, puisqu'il opérait sous l'hypothèse que son environnement d'exécution ne pouvait pas communiquer vers l'extérieur. OpenAI a corrigé la faille le 20 février 2026.

## Points clés

- Un prompt malveillant unique suffisait à activer un canal d'exfiltration caché au sein d'une conversation ChatGPT ordinaire, transmettant des données vers un serveur externe via des requêtes DNS
- L'environnement d'exécution de code de ChatGPT bloquait les requêtes réseau sortantes directes, mais ne filtrait pas les résolutions DNS — un angle mort classique en sécurité réseau
- Le modèle ne détectait pas le comportement comme un transfert de données externe et affirmait à l'utilisateur qu'aucune donnée n'avait été envoyée à l'extérieur
- Check Point a démontré l'attaque via un GPT tiers (application utilisant les API ChatGPT) analysant des résultats de laboratoire médicaux : les données personnelles étaient transmises à un serveur contrôlé par l'attaquant
- La faille soulève des implications majeures pour les industries réglementées (RGPD, HIPAA, conformité financière) qui déploient des services IA
- OpenAI investit par ailleurs massivement dans la protection anti-bots de ChatGPT via Cloudflare Turnstile, empêchant toute interaction avant le chargement complet de l'interface React

## Analyse approfondie

### Une faille dans les garde-fous, pas dans le modèle

OpenAI met en avant la sécurité des données de ses services IA, mais Check Point a montré que ChatGPT permettait à des données de fuiter via un canal latéral DNS avant que la faille ne soit corrigée.

En février, l'entreprise IA a corrigé une vulnérabilité d'exfiltration de données dans ChatGPT qui permettait à un simple prompt de contourner les garde-fous qu'OpenAI avait mis en place.

"Nous avons découvert qu'un unique prompt malveillant pouvait activer un canal d'exfiltration caché au sein d'une conversation ChatGPT ordinaire", ont déclaré les chercheurs de Check Point dans un billet de blog publié lundi.

Ce n'est pas censé être aussi facile. OpenAI a implémenté diverses protections autour de ChatGPT pour limiter l'exfiltration de données par les différents outils que le chatbot peut utiliser. Par exemple, l'entreprise affirme que "l'environnement d'exécution de code de ChatGPT ne peut pas générer de requêtes réseau sortantes directement."

Mais les chercheurs de Check Point ont découvert que ce n'était pas tout à fait exact.

### Le canal latéral DNS

"La vulnérabilité que nous avons découverte permettait de transmettre des informations vers un serveur externe via un canal latéral provenant du conteneur utilisé par ChatGPT pour l'exécution de code et l'analyse de données", ont expliqué les chercheurs. "De manière cruciale, parce que le modèle opérait sous l'hypothèse que cet environnement ne pouvait pas envoyer de données vers l'extérieur directement, il ne reconnaissait pas ce comportement comme un transfert de données externe nécessitant une résistance ou une médiation avec l'utilisateur."

Le canal en question est le DNS (Domain Name System), qui résout les noms de domaine en adresses IP. Les chercheurs de Check Point expliquent que, bien qu'OpenAI empêche ChatGPT de communiquer avec Internet sans autorisation, aucun contrôle n'était en place sur les données passées en contrebande via DNS.

### Trois preuves de concept

L'équipe de sécurité a créé trois attaques proof-of-concept démontrant comment ce canal latéral pouvait être exploité. L'une impliquait un "GPT", une application tierce implémentant les API ChatGPT, servant d'analyste de santé personnel.

Dans la démonstration, un utilisateur téléchargeait un PDF contenant des résultats de laboratoire et des informations personnelles pour que le GPT les interprète. L'application s'exécutait normalement, et lorsqu'on lui demandait si elle avait transmis les données, "ChatGPT répondait avec assurance que non, expliquant que le fichier était uniquement stocké dans un emplacement interne sécurisé."

Malgré cela, l'application GPT transmettait les données vers un serveur distant contrôlé par l'attaquant.

### Implications réglementaires et double standard

Des failles comme celle-ci impliquent des conséquences sérieuses pour les industries réglementées qui déploient des services IA. Si un service IA d'entreprise venait à faire fuiter ce type de données, cela pourrait constituer une violation du RGPD, du HIPAA, ou enfreindre diverses règles de conformité financière.

Par ailleurs, la sécurité d'OpenAI pour ChatGPT semble plus robuste lorsqu'il s'agit de se défendre contre les bots qui scrappent les conversations ChatGPT — précisément ce que les éditeurs tentent de faire aux robots d'exploration de contenu d'OpenAI. Une analyse récente de ChatGPT par un ingénieur en sécurité suggère qu'OpenAI a implémenté le widget Turnstile de Cloudflare de manière à empêcher toute interaction avec le chatbot tant que l'interface web React n'est pas entièrement chargée dans le navigateur de l'utilisateur.

Un individu se présentant comme employé d'OpenAI a écrit sur Hacker News : "Ces vérifications font partie de la façon dont nous protégeons nos produits propriétaires contre les abus comme les bots, le scraping, la fraude, et autres tentatives de détournement de la plateforme."

Ayant aspiré le contenu du monde entier pour l'entraînement de modèles afin de le monétiser, OpenAI ne peut pas se permettre de laisser d'autres explorer gratuitement son travail dérivé.

OpenAI aurait corrigé ce problème particulier le 20 février 2026.

## Pourquoi ça compte

Cette vulnérabilité illustre que la surface d'attaque des systèmes IA ne se limite pas au modèle lui-même mais s'étend à toute l'infrastructure d'exécution — et que les canaux latéraux classiques comme le DNS, souvent négligés par les contrôles réseau, deviennent des vecteurs d'exfiltration critiques dès lors qu'un attaquant peut manipuler les sorties du modèle via prompt injection, avec des conséquences directes pour toute entreprise déployant de l'IA sur des données sensibles ou réglementées.
