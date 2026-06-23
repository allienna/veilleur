---
title: "Don't rely on instructions, use Agent Hooks to enforce guardrails"
date: 2026-06-22
url: https://zarar.dev/agent-hooks-deterministic-guardrails-for-ai-generated-code/
authors: [zarar.dev]
keywords: [agent hooks, guardrails, déterministe, Claude Code, PreToolUse]
theme: IA
tone: tutorial
used_in: ["2026-06-22"]
---

## Résumé

Pour les développeurs qui utilisent `AGENTS.md` ou `CLAUDE.md` comme garde-fous mais constatent que l'agent ignore parfois les règles, l'auteur propose une approche déterministe : les Agent Hooks. Contrairement aux instructions probabilistes, un hook s'exécute mécaniquement à 100 % du temps. À distinguer des git hooks classiques : les Agent Hooks s'insèrent *pendant* le travail de l'agent, et non après. L'article détaille deux contrôles concrets (bloquer une balise interdite, empêcher l'agent de se déclarer terminé tant qu'un test échoue).

## Points clés

- Les instructions dans `AGENTS.md` / `CLAUDE.md` sont parfois ignorées par l'agent ; un hook, lui, est déterministe.
- Les Agent Hooks diffèrent des git hooks : ils s'invoquent pendant le workflow de l'agent, pas seulement au commit ou en revue.
- Un hook `PreToolUse` se déclenche juste avant l'exécution d'un outil et peut bloquer cette exécution (exit code 2, message sur stderr renvoyé à l'agent comme feedback).
- Un autre hook se déclenche quand l'agent pense avoir terminé, pour vérifier qu'un test (ici un ratchet test de design system) passe.
- Chaque hook reçoit un blob JSON sur stdin dont la forme dépend de l'événement ; on peut le traiter en `jq`, Python, shell, etc.

## Analyse approfondie

Ce billet s'adresse aux développeurs qui utilisent `AGENTS.md` ou `CLAUDE.md` pour fournir des garde-fous au code généré par l'agent, mais qui constatent que l'agent ignore parfois les règles. Si vous voulez une vérification déterministe qui fonctionnera à 100 %, lisez ce qui suit sur les agent hooks.

D'abord, une clarification. Les Agent Hooks sont différents des git hooks que beaucoup de développeurs connaissent. Le git hook le plus populaire est sans doute le pre-commit hook, appelé avant que vous ne tentiez de tout committer, et un endroit courant pour faire un `git pull` ou du formatage de code (par exemple prettier ou `mix format`) afin de garantir que le code est formaté selon les standards du langage. La limite d'un pre-commit hook est qu'il s'exécute bien après la génération du code, juste avant que vous ne pensiez avoir fini (au moment du commit).

Les agent hooks sont invoqués quand l'agent (par exemple Claude Code) est en train de travailler et permettent aux développeurs de s'interposer dans le workflow de l'agent, plutôt qu'après que le travail est fait (par exemple en revue de code). Comme mise en garde : tous les agents n'ont pas les mêmes hooks. Contrairement aux Skills pour lesquels des standards existent, les Hooks sont un peu le désordre, vous devrez donc voir quels hooks votre agent met à disposition. Je vais faire deux vérifications déterministes qui m'ont mordu par le passé :

1. M'assurer que l'agent n'utilise jamais directement une balise `<input>`, parce que je veux qu'il utilise mes composants de design.
2. M'assurer que l'agent ne me dit jamais qu'il a fini tant que mon ratchet test de design system échoue.

Ces deux-là se déclenchent à des moments complètement différents du cycle de vie de l'agent. Le premier s'exécute *avant* que l'agent n'exécute un outil ; le second se déclenche quand l'agent pense avoir terminé.

Chaque hook reçoit un blob de JSON sur stdin, et la forme de ce blob dépend de l'événement. C'est ce que les appels `jq` ci-dessous exploitent. Je montre exactement ce que chaque hook reçoit afin que les chemins utilisés par `jq` aient du sens. J'utilise `jq`, mais on pourrait écrire un script Python, un script shell ou n'importe quoi que l'agent peut appeler.

Le premier est un hook `PreToolUse`. PreToolUse se déclenche juste avant que Claude Code n'exécute un outil, et c'est le seul endroit où l'on peut réellement empêcher l'outil de se produire, en sortant avec un code d'erreur autre que `1` ou `2`. Ce que vous avez écrit sur stderr en sortant avec le code `2` sera vu par l'agent comme du feedback. Le code `1` ne fait que logger un warning et laisse passer l'outil.

Je veux que chaque champ de formulaire passe par mon propre composant `<.cinput>`, pas par un `<input>` nu. Je vérifie donc le contenu que l'agent est sur le point d'écrire et je le bloque si je vois la balise.

## Pourquoi ça compte

C'est le levier d'implémentation concret du discours « il faut superviser les agents » : les hooks transforment des règles probabilistes (instructions) en garde-fous déterministes, exactement ce dont une équipe AI-native a besoin pour livrer avec confiance.
