---
title: "If AI Writes Your Code, Why Use Python?"
date: 2026-05-17
url: https://programmingdigest.net/links/22336/8e384055-4ef6-4411-8656-1644e3ae163f/email
authors: [Noah Mitchem, Medium]
keywords: [Rust, Python, AI coding agents, language choice, ecosystem]
theme: IA
tone: opinion
used_in: ["2026-05-17"]
---

## Résumé

Noah Mitchem soutient que l'argument historique en faveur de Python et JavaScript — vitesse de développement et richesse de l'écosystème — s'effondre maintenant que les agents IA codent aussi bien (voire mieux) dans des langages systèmes comme Rust et Go. Les boucles de feedback serrées des langages typés et compilés en font les terrains idéaux pour les agents. Des projets concrets (compilateur TypeScript en Go, compilateur C en Rust écrit par 16 agents Claude pour 20 000 $, port de Ladybird en deux semaines) le confirment. L'écosystème Python lui-même devient un wrapper sur du code Rust.

## Points clés

- Claude Opus 4.7, GPT-5.5, Gemini 3.1 et DeepSeek V4 ont tous franchi 80 % sur SWE-bench Verified en avril 2026.
- Microsoft a réécrit le compilateur TypeScript en Go, 10× plus rapide.
- Nicholas Carlini (Anthropic) a orchestré 16 agents Claude pour produire 100 000 lignes de Rust = un compilateur C qui boot Linux, pour 20 000 $.
- Andreas Kling a porté le moteur JS de Ladybird de C++ vers Rust en deux semaines (25 000 lignes, zéro régression sur 65 000 tests).
- pydantic, polars, tokenizers, orjson, uv, ruff, ty : l'écosystème Python est devenu un écosystème Rust déguisé.
- OpenAI a acquis Astral (uv/ruff/ty) le 19 mars 2026 ; Anthropic a acquis Bun dix semaines plus tôt.
- La nouvelle unité de contribution open source : non plus le patch, mais le port complet.

## Analyse approfondie

Le marché historique avec Python et JavaScript était simple : ces langages t'aidaient à livrer vite, l'écosystème faisait 90 % du travail, tu acceptais que la performance soit décevante et tu te promettais de « la régler plus tard ». Tu ne le faisais jamais, et c'était bien parce que personne d'autre ne le faisait. **Ce marché est terminé, et il est terminé parce que l'IA est devenue bonne dans les langages difficiles.**

### Les langages difficiles sont devenus faciles en premier

Il y a deux ans, GPT-4 ne pouvait pas écrire une fonction Rust sans halluciner des noms de crates. En avril 2026, Claude Opus 4.7, GPT-5.5, Gemini 3.1 et DeepSeek V4 ont tous franchi 80 % sur SWE-bench Verified à quelques semaines d'écart. Les labos optimisent ouvertement pour le travail système : concurrence, race conditions, défauts d'architecture détectés dès la phase de planification.

La meilleure explication en un tweet vient de CtrlAltDwayne :

> _Le meilleur argument pour Rust en 2026, ce n'est pas la memory safety ou la performance. C'est que l'IA écrit mieux du Rust que du C++. La boucle de feedback du compilateur est si serrée que les modèles se corrigent en temps réel. Chaque erreur est un signal d'entraînement gratuit. Rust a été accidentellement conçu pour le développement assisté par IA, dix ans avant que ce soit pertinent._

La même logique vaut pour Go et Swift à des degrés divers. Systèmes de types forts + boucles compile-and-check rapides = itération la plus serrée pour les agents. Les langages systèmes les plus durs pour les humains sont les plus faciles pour les agents.

### Ce qui a réellement été livré

Ce qui a atterri en un seul trimestre :

- **Microsoft a réécrit le compilateur TypeScript en Go.** TypeScript 7.0 beta livré la semaine dernière, à peu près 10× plus rapide que la 6.0, en portant la base de code décennale TypeScript vers Go. Anders Hejlsberg a expliqué : Go a délivré l'essentiel du bénéfice perf à une fraction du coût d'ingénierie.
- **Nicholas Carlini, chercheur chez Anthropic, a orchestré 16 agents Claude en parallèle** pour écrire un compilateur C de production en Rust. 100 000 lignes. Il boot Linux 6.9 sur x86, ARM et RISC-V. Il compile QEMU, FFmpeg, SQLite, PostgreSQL, Redis. Il fait tourner Doom. Coût total : un peu moins de 20 000 $ sur près de 2 000 sessions Claude Code. _Un compilateur C en Rust, c'était une thèse de doctorat. Ce n'est plus le cas._
- **Steve Klabnik** (auteur de _The Rust Programming Language_) a construit un nouveau langage système, Rue, en deux semaines avec Claude. Environ 70 000 lignes de Rust.
- **Andreas Kling**, créateur de Ladybird, a porté le moteur JS de Ladybird de C++ vers Rust en deux semaines : 25 000 lignes, parité byte-pour-byte, zéro régression sur 65 000+ tests test262 et Ladybird. _« Le même boulot m'aurait pris plusieurs mois à la main. »_

Rien de tout cela n'était possible en 2024. En 2025, c'était marginal. Début 2026, c'est en train de devenir courant.

### Adieu l'argument « mais l'écosystème »

L'argument le plus fort pour Python et JavaScript n'a jamais été les langages eux-mêmes. C'était les écosystèmes : FastAPI, Django, PyTorch, React, Next.js, les 4 millions de paquets npm. Mais quand tu `import pydantic`, le cœur de validation est une lib Rust. Polars est en Rust. Hugging Face tokenizers est en Rust. orjson est en Rust. L'enquête JetBrains 2025 a capté le signal : l'usage de Rust pour les extensions Python binaires est passé de 27 % à 33 % en un an.

**L'écosystème Python est de plus en plus un écosystème Rust déguisé en Python.**

La plomberie suit la même trajectoire. Astral, fondée par Charlie Marsh en 2022, a livré ruff, uv et ty. Les trois sont en Rust, et les trois sont passés de zéro à des centaines de millions de téléchargements mensuels. Le 19 mars 2026, OpenAI a racheté Astral ; la justification interne : uv économise environ un million de minutes de compute par semaine à Codex. Dix semaines plus tôt, Anthropic a racheté Bun (7M de téléchargements mensuels, 89K stars) et l'a positionné comme « infrastructure essentielle pour le software engineering piloté par IA ».

Lee Robinson (VP Product, Vercel) : « We've reached peak optimization with JS. »

Ce qu'il reste de « mais l'écosystème » : les paquets que tu importes en Python ou JS sont de plus en plus des wrappers sur du code écrit dans des langages qu'on te disait que tu ne pouvais pas livrer. Maintenant tu peux livrer directement dans ces langages, et le wrapper commence à ressembler à de la surcharge.

### Pourquoi patcher quand tu peux porter ?

L'ancienne boucle open source : tu choisis Python parce que c'est facile, tu trouves un bug, tu le corriges, tu le remontes upstream. L'écosystème devient meilleur. Les agents ont cassé cette boucle dans un sens précis : **l'unité de contribution est passée du patch au port complet.**

Armin Ronacher (créateur de Flask) a porté sa lib Rust MiniJinja vers Go en janvier avec un agent. 10 heures de run, 3 supervisées et 7 sans supervision. Temps humain réel : 45 minutes. Coût API : 60 $. Si porter une lib d'un langage à l'autre est un job de 45 minutes, l'intérêt d'upstreamer une correction faiblit chaque mois.

> _For me, the value is shifting from the code to the tests and documentation. A good test suite might actually be worth more than the code._

### Là où l'argument se casse

Ce n'est pas un balayage propre. Plusieurs nuances :

- Parfois la bonne réponse reste l'ancienne. Prisma a retiré son query engine en Rust au profit d'un cœur TypeScript/WASM : bundle réduit de 85 %, requêtes jusqu'à 3,4× plus rapides. Les binaires Rust natifs sont hostiles aux runtimes serverless.
- PyTorch détient encore environ 85 % de la recherche deep learning, et ça ne change pas — les poids ne se soucient pas du langage du wrapper.
- L'IA n'est pas également bonne dans tous les langages systèmes. Zig, Haskell, Gleam sont à la traîne, par manque de training data.

Rust et Go ont gagné la loterie parce qu'ils étaient assez populaires pour inonder GitHub.

## Pourquoi ça compte

Le débat « quel langage pour la prochaine décennie ? » bascule sous nos yeux : ce ne sont plus les humains qui définissent les critères, ce sont les boucles d'agents. Pour un Engineering Director, anticiper ce shift conditionne les choix de stack des 3-5 prochaines années — et le profil des recrutements.
