---
title: "How to Work and Compound with AI"
date: 2026-05-06
url: https://eugeneyan.com/writing/working-with-ai/
authors: [Eugene Yan]
keywords: [productivité, contexte, configuration, MCP, compounding]
theme: IA
tone: tutorial
used_in: ["2026-05-06"]
---

## Résumé

Eugene Yan propose un guide pratique pour travailler avec l'IA non pas en mode "prompt à la volée" mais en mode "compounding" : chaque artefact produit (code, doc, analyse, décision) devient le contexte de la session suivante, et chaque correction met à jour une config qui réduit les erreurs futures. Cinq principes : fournir un bon contexte, encoder son goût en config, rendre la vérification facile, déléguer des tâches plus grosses, fermer la boucle. Aucun de ces principes n'est spécifique à l'IA — c'est ainsi qu'on travaille avec n'importe quel nouveau collaborateur.

## Points clés

- **Compounding** : chaque session enrichit la suivante via des artefacts persistants
- **Contexte comme infrastructure** : organisation des fichiers, INDEX.md annotés par projet
- **MCPs** pour connecter le modèle aux sources organisationnelles (Slack, Drive, Mail)
- **Encoder son goût en config** : style guides, patterns, decisions records
- **Faciliter la vérification** : tests, types, contracts qui rendent l'évaluation rapide
- **Fermer la boucle** : chaque correction devient un pattern réutilisable

## Analyse approfondie

Comment travaille-t-on efficacement avec l'IA ? Quel est le workflow, comment passe-t-il à l'échelle, et comment améliorer ses systèmes au fil du temps ? Idéalement, ça devrait *compounder*. Chaque artefact terminé — code, docs, analyse, décisions — devient le contexte de la session suivante. Et chaque correction met à jour une config qui réduit les erreurs futures.

Eugene Yan apprend encore, mais a répété ses réponses assez souvent pour les écrire ici afin de pouvoir partager un lien la prochaine fois.

Les principes qui suivent s'appliquent largement : fournir un bon contexte, encoder son goût en config, faciliter la vérification, déléguer des tâches plus grosses, fermer la boucle. Si une pratique ne convient pas, adapter le principe et inventer la sienne. À noter : rien de tout cela n'est spécifique à l'IA. C'est simplement comment on onboarde et travaille avec n'importe quel nouveau collaborateur.

### Le contexte comme infrastructure

**Aider les modèles à naviguer ton contexte.** Tout le code de Yan vit dans `~/src` et tout son travail de connaissance dans `~/vault` (organisé en `projects/`, `notes/`, `kb/`, etc.). Quand le travail est organisé, il est plus facile pour le modèle de retrouver le contexte via `grep` ou `glob`. Et avec une arborescence propre, c'est plus simple de naviguer, de trouver et de s'appuyer sur du code antérieur, des docs projet, des analyses, etc. pour améliorer le travail en cours.

**Connecter les modèles au contexte de ton organisation.** Les modèles bénéficient de la connaissance organisationnelle qui vit probablement dans Slack, Drive, Mail, etc. La plupart ont des MCPs (Model Context Protocol) pour Claude Code, Cowork, Claude.ai. Yan maintient en plus un `INDEX.md` par projet : un index annoté des docs et channels pertinents, où chaque entrée inclut l'URL, le propriétaire, et un paragraphe expliquant ce qu'il y a dedans et quand le lire. L'annotation aide énormément. Une liste brute d'URLs force le modèle à ouvrir chaque lien pour comprendre ce qui est pertinent — coûteux en tokens et en latence.

### Encoder son goût en config

C'est probablement le point le plus sous-exploité. Tout le monde a un *goût* — des conventions de nommage qu'il préfère, un style de tests, une façon d'organiser les imports. Au lieu de répéter ces préférences à chaque prompt, Yan les encode dans des fichiers : `STYLE.md`, `PATTERNS.md`, `ARCHITECTURE.md`. Les modèles les lisent au début de chaque session.

Quand l'agent fait quelque chose qui ne correspond pas à ton goût, ne le corrige pas seulement à la main : ajoute une ligne dans `PATTERNS.md`. La fois suivante, il ne se trompera plus. C'est exactement comme apprendre à un nouveau collègue, sauf que la transmission est explicite et persistante.

### Faciliter la vérification

L'IA produit beaucoup. Le bottleneck devient la vérification. Yan pousse fortement pour rendre la vérification cheap :

- **Tests rapides et exhaustifs.** Pas pour valider l'implémentation, mais pour valider le contrat. Plus le test est concret (entrée → sortie attendue), mieux c'est pour évaluer une PR générée par IA.
- **Types stricts.** Quand le système des types attrape une erreur, tu n'as pas besoin de la trouver à la main.
- **Contracts à la frontière des modules.** Si chaque module a un contrat clair (API, schéma, comportement), tu peux faire confiance à l'IA pour modifier l'intérieur tant que le contrat tient.
- **Linters et formatters.** Les choses que l'IA peut elle-même corriger n'ont pas à passer en review.

### Déléguer des tâches plus grosses

Beaucoup de gens utilisent l'IA pour des tâches micro (compléter une fonction, générer un test). Yan pousse à déléguer des tâches macro : "écris un nouveau module qui fait X, en suivant les patterns de Y, avec les tests et la doc". Pour que ça marche, il faut le contexte (cf. plus haut) et la vérifiabilité (cf. plus haut). Sans ces deux choses, déléguer macro produit du chaos.

### Fermer la boucle

Quand une session produit une découverte (un pattern qui marche bien, un anti-pattern à éviter, une heuristique de prompt), elle doit être capturée. Sinon elle se perd. Yan ajoute systématiquement une ligne dans le fichier de config approprié à la fin de chaque session productive. C'est cette étape qui transforme une utilisation individuelle en pratique compoundante.

### Ce que ça donne après plusieurs mois

Au bout de quelques mois de cette discipline, le résultat est un *config repo* qui encode la façon dont Yan travaille. Quand il commence un nouveau projet, il importe les patterns pertinents. Quand il onboarde un collègue, il partage le repo. Quand il change de modèle (Claude → GPT → Gemini), une grande partie de la valeur reste — parce qu'elle est dans la config, pas dans le modèle.

C'est l'antidote au problème que Glaser identifie : les gains individuels qui ne deviennent pas organisationnels. La config partagée *est* la mémoire organisationnelle.

## Pourquoi ça compte

Yan articule de façon concrète et reproductible ce que beaucoup de power users de l'IA ressentent intuitivement : la valeur n'est pas dans le prompt, elle est dans l'infrastructure de contexte qu'on construit autour. Lecture indispensable pour quiconque veut passer d'un usage tactique de l'IA à un usage stratégique.
