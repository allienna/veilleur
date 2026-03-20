---
title: "Snowflake Cortex AI Escapes Sandbox and Executes Malware"
date: 2026-03-19
url: https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware
authors: [PromptArmor]
keywords: [Snowflake, sandbox escape, prompt injection, sécurité, agent IA, malware]
theme: Sécurité
tone: research
used_in: ["2026-03-19"]
---

## Résumé

PromptArmor a identifié une vulnérabilité critique dans Snowflake Cortex Code CLI, un agent de code similaire à Claude Code et OpenAI Codex. Deux jours après sa sortie, il a été démontré qu'une injection de prompt cachée dans un README pouvait faire exécuter des commandes arbitraires à l'agent, en dehors de sa sandbox, sans approbation humaine. L'attaque permettait le téléchargement de malware, l'exfiltration de données et la suppression de tables Snowflake.

## Points clés

- Vulnérabilité découverte 2 jours après le lancement de Cortex Code CLI
- L'attaque contourne tous les modes de sandbox proposés, y compris le mode avec approbation obligatoire
- Vecteur : injection de prompt indirect via un README de repo malveillant
- Impact : exécution de commandes sans sandbox, exfiltration de données, suppression de tables via les credentials actifs
- Corrigé dans la version 1.0.25 le 28 février 2026
- Le pattern est généralisable à tout agent de code avec accès filesystem/réseau/credentials

## Analyse approfondie

### Contexte

Snowflake Cortex Code CLI est un agent de code en ligne de commande qui fonctionne de manière similaire à Claude Code et OpenAI Codex, avec en plus une intégration native pour exécuter du SQL dans Snowflake. L'outil est conçu pour aider les développeurs et les data engineers à interagir avec leur code et leurs données Snowflake de manière conversationnelle.

### La chaîne d'attaque

PromptArmor a identifié et démontré une chaîne d'attaque complète :

**Étape 1 : L'utilisateur active le sandbox.** L'utilisateur lance le CLI et choisit l'un des modes sandbox proposés. La documentation indique qu'en mode "OS+Regular", toutes les commandes requièrent une approbation utilisateur. Les commandes exécutées dans le sandbox ont également des restrictions d'accès réseau et fichier.

**Étape 2 : L'utilisateur demande de l'aide sur un codebase tiers.** L'injection de prompt est cachée dans le README d'un dépôt non fiable trouvé en ligne. En pratique, l'injection peut provenir de n'importe quelle source non fiable que l'agent est amené à lire — fichiers markdown, commentaires de code, documentation.

**Étape 3 : L'agent exécute les commandes malveillantes.** La vulnérabilité dans le système de validation des commandes de Cortex Code permettait à des commandes spécialement construites de :

- S'exécuter sans déclencher l'étape d'approbation humaine (human-in-the-loop)
- S'exécuter en dehors du sandbox du CLI

**Étape 4 : Actions malveillantes.** L'attaquant peut alors utiliser les credentials actifs de la session Snowflake de la victime pour :

- Télécharger et exécuter des scripts malveillants
- Exfiltrer des données depuis Snowflake
- Supprimer des tables (DROP TABLE)
- Modifier des configurations de sécurité

### Pourquoi c'est critique

L'attaque est particulièrement dangereuse pour plusieurs raisons :

1. **Elle contourne toutes les protections.** Que l'utilisateur soit en mode sandbox strict avec approbation obligatoire ou en mode plus permissif, le résultat est le même. Le faux sentiment de sécurité créé par le sandbox est pire que l'absence de protection, car il encourage des comportements plus risqués.

2. **L'injection de prompt indirect est invisible.** Le contenu malveillant est caché dans un fichier que l'utilisateur n'a aucune raison de soupçonner. Un README de dépôt open source est exactement le type de contenu qu'un développeur demanderait à un agent de code d'analyser.

3. **Les credentials sont hérités.** L'agent utilise les mêmes credentials que la session active de l'utilisateur. Toute action malveillante est donc exécutée avec les permissions complètes de l'utilisateur, rendant la détection difficile.

4. **Le pattern est généralisable.** Tout agent de code qui a accès au filesystem, au réseau et aux credentials de l'utilisateur est potentiellement vulnérable à ce type d'attaque. La spécificité de Cortex Code (intégration Snowflake) amplifie l'impact, mais le vecteur (injection de prompt indirect + bypass de sandbox) s'applique à n'importe quel agent de code.

### Remédiation

L'équipe de sécurité de Snowflake a validé et corrigé la vulnérabilité. Un correctif a été publié dans la version 1.0.25 de Cortex Code CLI le 28 février 2026. L'avis complet de Snowflake est disponible sur le site communautaire Snowflake.

## Pourquoi ça compte

Cette vulnérabilité illustre un problème systémique de l'écosystème des agents de code : la confiance implicite accordée aux mécanismes de sandbox. Quand un agent a accès à votre filesystem, vos credentials et votre réseau, la surface d'attaque est immense — et les injections de prompt indirect restent un vecteur sous-estimé. C'est un avertissement pour toute l'industrie des coding agents.
