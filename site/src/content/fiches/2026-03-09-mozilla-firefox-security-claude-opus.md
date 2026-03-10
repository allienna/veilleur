---
title: "Partnering with Mozilla to improve Firefox's security"
date: 2026-03-09
url: "https://www.anthropic.com/news/mozilla-firefox-security"
authors: ["Anthropic"]
keywords: [zero-day, Firefox, audit de sécurité, Claude Opus, vulnérabilités]
theme: "Sécurité"
tone: "news"
used_in: ["2026-03-09"]
---

## Résumé

Anthropic détaille son partenariat avec Mozilla : Claude Opus 4.6 a découvert 22 vulnérabilités dans Firefox en deux semaines, dont 14 classées haute sévérité. Les correctifs ont été livrés dans Firefox 148.0 à des centaines de millions d'utilisateurs. L'article décrit la progression méthodologique, des benchmarks CyberGym à la reproduction de CVE réelles, jusqu'à la découverte de zero-days inédits dans le moteur JavaScript.

## Points clés

- Claude Opus 4.6 a trouvé 22 vulnérabilités en deux semaines, dont 14 haute sévérité — soit près d'un cinquième du total annuel 2025 de Firefox
- La méthodologie a progressé par paliers : benchmarks synthétiques, reproduction de CVE connues, puis découverte de zero-days réels
- Les vulnérabilités touchent le moteur JavaScript et d'autres composants critiques du navigateur
- Mozilla a intégré les correctifs dans Firefox 148.0 déployé auprès de centaines de millions d'utilisateurs
- Firefox est l'un des projets open-source les mieux audités au monde, ce qui rend ces découvertes d'autant plus significatives

## Analyse approfondie

Les modèles d'IA sont désormais capables d'identifier de manière autonome des vulnérabilités de haute sévérité dans des logiciels complexes. Anthropic a récemment documenté la découverte par Claude de plus de 500 vulnérabilités zero-day dans des logiciels open-source bien testés.

Dans le cadre d'une collaboration avec les chercheurs de Mozilla, Claude Opus 4.6 a découvert 22 vulnérabilités en deux semaines. Mozilla en a classé 14 comme haute sévérité — soit près d'un cinquième de toutes les vulnérabilités haute sévérité de Firefox corrigées en 2025. L'IA rend possible la détection de failles de sécurité graves à une vitesse considérablement accélérée.

La méthodologie a progressé par étapes. D'abord, l'équipe a utilisé Claude pour reproduire des CVE historiques dans d'anciennes versions de Firefox. Puis, pour éliminer le doute d'une contamination par les données d'entraînement, ils ont ciblé la version courante du navigateur. En seulement vingt minutes d'exploration, Claude Opus 4.6 a signalé une vulnérabilité Use After Free dans le moteur JavaScript — un type de faille mémoire permettant à un attaquant d'écraser des données avec du contenu malveillant.

Au total, l'équipe a scanné près de 6 000 fichiers C++ et soumis 112 rapports uniques. La plupart des correctifs ont été intégrés dans Firefox 148.0, déployé auprès de centaines de millions d'utilisateurs. Mozilla a encouragé Anthropic à soumettre ses découvertes en lot, même sans validation individuelle de chaque cas de crash.

L'équipe a également testé les limites de Claude en matière d'exploitation. Malgré plusieurs centaines de tentatives et environ 4 000 dollars de crédits API, Opus 4.6 n'a réussi à transformer une vulnérabilité en exploit fonctionnel que dans deux cas. Cela indique que Claude est bien meilleur pour trouver les failles que pour les exploiter — ce qui donne un avantage temporaire aux défenseurs.

Anthropic recommande aux agents de patching d'utiliser des « vérificateurs de tâches » : des outils de confiance qui confirment si la sortie de l'agent atteint réellement son objectif. Les soumissions de bugs devraient inclure des cas de test minimaux, des preuves de concept détaillées et des correctifs candidats.

## Pourquoi ça compte

Ce cas démontre que l'IA excelle sur les tâches d'analyse de sécurité à grande échelle — analyser des millions de lignes sans fatigue. C'est un signal fort que l'audit de code assisté par IA devient un avantage compétitif majeur.
