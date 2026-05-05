---
title: "How I Use AI to Code"
date: 2026-05-01
url: https://www.chrismdp.com/coding-with-ai-2026/
authors: [Chris Parsons]
keywords: [agentic engineering, vibe coding, AI workflow, code review, senior engineering]
theme: IA
tone: opinion
used_in: ["2026-05-01"]
---

## Résumé

Chris Parsons met à jour son guide d'usage de l'IA pour coder, devenu une référence depuis mars 2025. Le message principal : si tu es encore enchaîné à ton IDE — Cursor ou Copilot — tu as un an de retard. Le meilleur outillage est passé de l'éditeur à la ligne de commande, et le job de l'ingénieur senior est désormais d'entraîner l'IA, pas de relire son output. L'auteur distingue clairement *vibe coding* (où on ne vérifie pas) et *agentic engineering* (où on choisit où placer son attention). L'analyse a16z d'avril 2026 confirme que le coding est de loin le premier usage entreprise de l'IA, devant tout le reste d'un ordre de grandeur.

## Points clés

- Le tooling AI sérieux a quitté l'IDE pour la ligne de commande
- "Vérifié" ne veut plus dire "lu par toi" — ça veut dire passé par les tests, le type checker, les automated gates, et lu par toi là où le jugement compte
- Distinction nette : vibe coding (jeté) vs agentic engineering (livrable)
- Savoir où placer son attention sur les diffs (skim UI, lecture attentive sécu/DB) est devenu une compétence senior à part entière
- Selon a16z, le coding est le premier usage entreprise de l'IA d'un ordre de grandeur

## Analyse approfondie

Si tu es encore enchaîné à ton IDE, que ce soit Cursor ou Copilot, tu travailles avec un an de retard. Le coding s'est révélé être le terrain de jeu naturel de l'IA. Le meilleur outillage est passé de l'éditeur à la ligne de commande, et le job de l'ingénieur senior est désormais d'entraîner l'IA, pas de relire son output.

J'ai écrit la version précédente de ce post en mars 2025, je l'ai mise à jour une fois en août, et il est cité dans presque tout ce que j'ai écrit sur l'AI engineering depuis. Les fondamentaux de ce post tiennent toujours : garder les changements petits, construire des guardrails, documenter sans relâche, et s'assurer que chaque modification soit vérifiée avant d'être livrée. Une chose a dû évoluer avec le volume. "Vérifié" voulait dire "lu par toi". Avec le débit moderne des agents, ça doit vouloir dire "vérifié par les tests, par les type checkers, par les gates automatisés, ou par toi là où ton jugement compte". La vérification a toujours lieu ; elle ne se passe simplement plus toujours dans ta tête.

Une distinction s'est durcie au cours de la dernière année, et elle compte pour la suite : le vibe coding et l'agentic engineering sont deux pratiques différentes. Le vibe coding, où tu ne vérifies pas vraiment les résultats et tu regardes juste l'output, c'est très bien tant que tu ne livres pas. L'agentic engineering, c'est autre chose. Ça ne veut pas dire lire chaque diff. Ça veut dire prendre une décision mesurée sur les diffs qui ont besoin de tes yeux et ceux qui n'en ont pas besoin. J'ai tendance à survoler les diffs UI. Je lis attentivement les diffs sécurité et base de données.

Ce jugement, savoir où passer ton attention, est en lui-même une compétence senior et qui vaut la peine d'être bien maîtrisée. Chaque diff est encore vérifié ; pas toujours par toi. Tests, type checkers et automated gates s'occupent du reste, et tu entraînes l'agent pour que les diffs qui atteignent tes yeux soient ceux qui valent l'attention. Confondre les deux, c'est comme ça que des gens finissent par expédier du code vibe-coded en production et se font cramer.

### Le coding s'est révélé être le terrain naturel de l'IA

L'analyse a16z des contrats Fortune 500 et Global 2000 d'avril 2026 a confirmé ce que beaucoup soupçonnaient depuis l'intérieur du travail : le coding est le cas d'usage IA dominant en entreprise, par presque un ordre de grandeur. Ce n'est pas une question de mode passagère. C'est que les LLM sont structurellement bons à la transformation de code : entrée déterministe, sortie déterministe, retour rapide via tests et compilation.

### Les fondamentaux qui tiennent

- Petits changements
- Guardrails forts
- Documentation impitoyable
- Vérification au bon endroit

Et pour le reste, l'agent va plus vite que toi. Accepte-le, et concentre-toi sur ce que toi seul sais faire : juger.

## Pourquoi ça compte

C'est probablement le post de référence le plus partagé sur l'agentic engineering en 2026. La distinction vibe coding / agentic engineering est précieuse pour cadrer les discussions d'équipe sur ce qu'on accepte de livrer en prod.
