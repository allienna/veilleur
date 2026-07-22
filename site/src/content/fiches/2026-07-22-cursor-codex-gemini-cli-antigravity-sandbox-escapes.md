---
title: "Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes"
date: 2026-07-22
url: https://links.tldrnewsletter.com/fjbiHH
authors: [bleepingcomputer.com, Pillar Security]
keywords: [sandbox escape, coding agents, prompt injection, CVE, security]
theme: IA
tone: news
used_in: ["2026-07-22"]
---

## Résumé

Des chercheurs en sécurité de Pillar Security ont réussi à s'évader des sandboxes de quatre agents de code très utilisés — Cursor, Codex d'OpenAI, Gemini CLI de Google et Antigravity — sans jamais attaquer le bac à sable de front. L'agent reste sagement dans sa boîte et respecte toutes les règles : il se contente d'écrire un fichier qu'un outil de confiance situé *à l'extérieur* de la sandbox va ensuite exécuter, charger ou scanner, et l'évasion se produit d'elle-même. Le déclencheur est l'injection de prompt, via un README, une issue, une dépendance ou un diff. La plupart des failles sont désormais corrigées et reconnues par les éditeurs.

## Points clés

- Quatre agents touchés : Cursor, OpenAI Codex, Google Gemini CLI et Antigravity.
- L'agent respecte les règles de la sandbox ; ce sont les outils *hors* sandbox qui font confiance aux fichiers qu'il écrit.
- Le déclencheur est l'injection de prompt cachée dans un README, une issue, une dépendance ou un diff.
- Pillar classe les sept découvertes en quatre modes de défaillance (denylist dépassée, config exécutable, allowlist naïve sur le nom de commande, daemons privilégiés hors sandbox).
- Dans Cursor, une config de hook .claude contrôlée par le workspace donnait une exécution de commande non sandboxée — CVE-2026-48124, corrigée en 3.0.0.
- La recherche a été publiée sous forme de série quotidienne : la « Week of Sandbox Escapes ».

## Analyse approfondie

Des chercheurs en sécurité se sont évadés des sandboxes de quatre agents de code largement utilisés, dont Cursor, le Codex d'OpenAI, le Gemini CLI de Google et Antigravity, sans attaquer la sandbox de front.

L'agent reste dans la boîte et suit toutes les règles. Il écrit simplement un fichier qu'un outil de confiance situé hors de la boîte va ensuite exécuter, charger ou scanner, et l'évasion survient d'elle-même.

### Comment fonctionnent les évasions

L'équipe de recherche de Pillar Security — Eilon Cohen, Dan Lisichkin et Ariel Fogel — a reproduit ces contournements sur plusieurs mois et les a publiés sous forme de série baptisée la « Week of Sandbox Escapes », un écrit par jour.

Ces sandboxes tracent une ligne simple : l'agent est de confiance à l'intérieur du workspace du projet, l'hôte à l'extérieur est protégé.

Le piège, c'est que les fichiers du workspace ne sont pas inertes. Des outils qui tournent hors de la sandbox les lisent et agissent dessus : un fichier que l'agent est autorisé à écrire peut donc se transformer en commande que l'hôte exécutera plus tard.

**L'agent reste dans la sandbox, mais les fichiers qu'il écrit sont considérés comme fiables par les outils hors de la boîte** (Pillar Security).

Les IDE et agents CLI lancent en permanence leurs propres outils hors sandbox : extensions Python résolvant des interpréteurs, intégrations Git scannant des repos, VS Code exécutant des fichiers de tâches, moteurs de hooks déclenchant des commandes, Docker Desktop exposant un socket local.

Un agent sandboxé peut obéir à toutes les règles qu'on lui donne et tout de même façonner les fichiers que ces composants lisent.

L'injection de prompt est le déclencheur. Une instruction malveillante plantée dans un README, une issue, une dépendance ou un diff devient une action locale sur la machine du développeur.

Pillar range les sept découvertes en quatre modes de défaillance :

- des sandboxes en denylist incapables de suivre le rythme du système d'exploitation ;
- de la config de workspace qui est en réalité du code exécutable ;
- des allowlists de commandes « sûres » qui font confiance au nom d'une commande plutôt qu'à ses arguments ; et
- des daemons locaux privilégiés qui se trouvent entièrement hors de la sandbox.

### Les bugs, et les correctifs

La plupart des problèmes sont corrigés et reconnus par les éditeurs.

Dans Cursor, une config de hook .claude contrôlée par le workspace se transformait en exécution de commande non sandboxée. C'est désormais suivi sous CVE-2026-48124 et corrigé en version 3.0.0.

Un second bug Cursor permettait à l'agent d'éditer un interpréteur de virtualenv que l'extension Python de l'éditeur [...].

## Pourquoi ça compte

Plus on confie l'exécution de code aux agents sur nos machines, plus le maillon faible n'est plus le modèle mais la frontière de confiance : cette série de failles montre que la sandbox des outils de dev est une surface d'attaque bien réelle.
