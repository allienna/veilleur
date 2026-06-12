---
title: "GitHub - NVIDIA/SkillSpector: Security scanner for AI agent skills"
date: 2026-06-12
url: "https://github.com/NVIDIA/SkillSpector"
authors: ["NVIDIA"]
keywords: ["SkillSpector", "sécurité agents IA", "prompt injection", "vulnérabilités", "MCP"]
theme: "Sécurité"
tone: "news"
used_in: ["2026-06-12"]
---

## Résumé

NVIDIA open-source SkillSpector, un scanner de sécurité statique pour les skills d'agents IA (Claude Code, Codex CLI, Gemini CLI, etc.). Le chiffre clé : 26,1 % des skills contiennent des vulnérabilités, et 5,2 % montrent une intention probablement malveillante. SkillSpector détecte 64 patterns de vulnérabilités répartis en 16 catégories, avec une analyse statique rapide et une évaluation sémantique optionnelle par LLM.

## Points clés

- 26,1 % des skills IA contiennent des vulnérabilités ; 5,2 % montrent une intention probablement malveillante.
- 64 patterns de vulnérabilités couvrant 16 catégories : prompt injection, exfiltration de données, élévation de privilèges, empoisonnement de mémoire, abus d'outils, etc.
- Analyse en deux phases : statique rapide (AST, YARA, taint tracking) + évaluation sémantique LLM optionnelle.
- Support multi-format : repos Git, URLs, fichiers ZIP, répertoires, fichiers individuels.
- Score de risque 0-100 avec labels de sévérité et recommandations claires.

## Analyse approfondie

### Le problème de confiance implicite

Les skills d'agents IA s'exécutent avec une confiance implicite et un contrôle minimal. Quand un développeur installe un skill tiers pour Claude Code ou Codex CLI, ce skill obtient accès aux outils de l'agent — filesystem, exécution de commandes, appels réseau, mémoire. La surface d'attaque est considérable, et le vetting est rarement fait.

### Les 16 catégories de vulnérabilités

SkillSpector couvre un périmètre large : **prompt injection** (manipulation des instructions de l'agent), **data exfiltration** (extraction de données sensibles), **privilege escalation** (obtention de droits supérieurs), **supply chain** (dépendances malveillantes), **excessive agency** (l'agent prend des actions non autorisées), **memory poisoning** (corruption de la mémoire de l'agent), **rogue agent** (comportement d'agent non aligné), et **MCP tool poisoning** (manipulation des outils MCP).

### L'analyse en deux phases

La première phase est une analyse statique rapide : AST (Abstract Syntax Tree) pour le code Python, signatures YARA pour les patterns connus, taint tracking pour suivre les flux de données potentiellement dangereux. La deuxième phase est optionnelle : elle soumet le skill à une évaluation sémantique par LLM pour détecter des intentions malveillantes plus subtiles que les patterns statiques peuvent manquer.

### Lookups de CVE en temps réel

SkillSpector interroge OSV.dev pour vérifier les vulnérabilités connues dans les dépendances utilisées par les skills. Fallback offline automatique si le réseau est indisponible. Les résultats sont exportables en Terminal, JSON, Markdown, ou SARIF (pour intégration dans les pipelines CI/CD).

## Pourquoi ça compte

SkillSpector arrive au bon moment : alors que l'écosystème de skills d'agents IA explose, l'outillage de sécurité est encore embryonnaire. Les chiffres (26 % vulnérables, 5 % malveillants) sont suffisamment alarmants pour que tout engineering manager devrait mettre en place un processus de vetting avant d'autoriser l'installation de skills tiers dans ses équipes.
