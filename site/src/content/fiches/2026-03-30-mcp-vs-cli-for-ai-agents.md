---
title: "MCP is up to 32× more expensive than CLI. Here's why we still use it."
date: 2026-03-30
url: https://www.scalekit.com/blog/mcp-vs-cli-use
authors: [ScaleKit]
keywords: [MCP, CLI, AI agents, benchmark, token cost, delegated access]
theme: IA
tone: research
used_in: ["2026-03-30"]
---

## Résumé

ScaleKit a conduit 75 runs de benchmark comparant CLI et MCP pour des tâches d'agents IA sur GitHub : le CLI gagne sur tous les indicateurs d'efficacité — 10 à 32× moins cher en tokens, fiabilité de 100 % contre 72 % pour MCP. Pourtant, les auteurs continuent d'utiliser MCP. La raison tient à une question architecturale fondamentale : pour qui l'agent agit-il ? Dès qu'un agent agit au nom des utilisateurs d'un tiers — dans des organisations clientes, sur des services tiers — les avantages d'efficacité du CLI deviennent des dettes architecturales : pas d'OAuth par utilisateur, pas d'isolation des tenants, pas de piste d'audit. MCP, malgré son coût en tokens, fournit ces garanties au niveau du protocole.

## Points clés

- Le CLI est 4 à 32× moins cher en tokens que MCP direct, avec 100 % de fiabilité contre 72 % pour MCP (timeouts TCP)
- Le surcoût de MCP vient principalement du "schema bloat" : les 43 définitions d'outils du serveur GitHub Copilot sont injectées dans chaque conversation, même si l'agent n'en utilise qu'une ou deux
- Un fichier de tips CLI de 800 tokens (CLI + Skills) réduit d'un tiers les appels d'outils et la latence — le meilleur retour sur investissement du benchmark
- Le vrai critère de choix n'est pas l'efficacité, c'est l'identité : le développeur est-il lui-même l'utilisateur, ou l'agent agit-il pour le compte des clients du produit ?
- MCP fournit au niveau protocole ce que CLI ne peut pas offrir en contexte multi-tenant : OAuth par utilisateur, isolation des tenants, piste d'audit structurée
- Un MCP gateway résout les problèmes pratiques de MCP direct (schema filtering, connection pooling, auth centralisée) et ramène coût et fiabilité proches des niveaux CLI

## Analyse approfondie

### Le benchmark

**Trois façons de connecter un agent IA à GitHub**

Même modèle (Claude Sonnet 4). Mêmes tâches. Mêmes prompts. Seule l'interface d'outillage change.

- **CLI :** On donne à l'agent un outil bash. Aucune guidance. Il trouve lui-même les commandes `gh`.
- **CLI + Skills :** Même outil bash, plus ~800 tokens de conseils — flags `gh` utiles, patterns de formatage des sorties, workflows courants. C'est ainsi que fonctionnent en pratique des outils comme OpenClaw.
- **MCP :** Connexion au serveur MCP officiel Copilot de GitHub sur `api.githubcopilot.com/mcp/`. L'agent reçoit automatiquement les 43 schémas d'outils.

Cinq tâches en lecture seule sur le dépôt `anthropics/anthropic-sdk-python` : récupérer les infos du repo, les détails d'une PR, des métadonnées, résumer les PRs mergées, trouver les dépendances d'une release. Toutes déterministes, toutes vérifiables.

### Les chiffres

**Utilisation des tokens : MCP coûte 4 à 32× plus cher**

| Tâche | CLI | CLI + Skills | MCP |
|---|---|---|---|
| Langage et licence du repo | 1 365 | 4 724 | 44 026 (32×) |
| Détails et statut de review d'une PR | 1 648 | 2 816 | 32 279 (20×) |
| Métadonnées du repo et installation | 9 386 | 12 210 | 82 835 (9×) |
| PRs mergées par contributeur | 5 010 | 6 107 | 33 712 (7×) |
| Dernière release et dépendances | 8 750 | 6 860 | 37 402 (4×) |

_Médiane de tokens par run. Toutes les différences CLI vs MCP sont statistiquement significatives (p < 0,05)._

Pour la tâche la plus simple — "dans quel langage est ce repo ?" — l'agent CLI a besoin de 1 365 tokens. L'agent MCP en a besoin de 44 026. La différence est presque entièrement due aux schémas : 43 définitions d'outils injectées dans chaque conversation, dont l'agent n'en utilisera qu'une ou deux.

### La plus grande surprise : MCP échoue 28 % du temps

Sur 25 runs MCP, 7 ont échoué avec une `ConnectTimeout`.

- **CLI :** 25/25 (100 %)
- **CLI + Skills :** 25/25 (100 %)
- **MCP :** 18/25 (72 %)

Chaque échec était un timeout au niveau TCP — la connexion au serveur MCP Copilot de GitHub n'a jamais abouti. Pas une erreur de protocole MCP. Pas un mauvais appel d'outil. Le serveur distant n'a simplement pas répondu à temps.

Les agents CLI n'ont pas ce problème. `gh` tourne en local. Il n'y a pas de serveur distant susceptible de timeout.

### Sous le capot : le problème du schema bloat

Le surcoût de MCP n'est pas un problème de protocole. C'est un problème d'injection de schémas.

Le serveur MCP Copilot de GitHub expose 43 outils. Chaque fois que l'agent effectue un appel d'outil, le schéma complet des 43 outils fait partie du contexte de conversation. Pour un simple appel "récupérer les infos du repo", l'agent transporte des schémas pour créer des gists, gérer les reviews de PR, configurer des webhooks — des outils qu'il ne touchera jamais.

L'agent CLI n'a pas ce problème. Il connaît `gh` depuis ses données d'entraînement. Il compose la bonne commande en une seule fois. Pas de surcharge de schémas. Pas d'étape de découverte.

> **L'astuce des 800 tokens :** un CLI augmenté d'un fichier de skills — juste un document de 800 tokens de conseils `gh` — réduit les appels d'outils d'un tiers et la latence d'un tiers par rapport au CLI naïf. C'est le meilleur ROI de tout ce benchmark. N'importe quelle équipe peut l'appliquer dès aujourd'hui.

### À l'échelle : 3,20 $ vs 55,20 $ pour le même travail

Aux tarifs de Claude Sonnet 4 (3 $/M tokens en entrée, 15 $/M tokens en sortie), pour 10 000 opérations par mois :

- **CLI :** ~3,20 $/mois
- **MCP (direct) :** ~55,20 $/mois
- **MCP via Gateway :** ~5 $/mois (estimation, avec schema filtering)

Soit un multiplicateur de coût de 17× pour MCP, plus un taux d'échec de 28 %.

À ce stade, le cas pour CLI semble écrasant. Moins cher, plus fiable, plus simple. Si on s'arrêtait là, on conclurait que MCP est un protocole à la recherche d'un problème.

Cette conclusion serait correcte pour les outils pour développeurs. Elle serait dangereusement fausse pour tout le reste.

### Ce que la plupart des analyses ratent : la vraie question

**La question n'est pas "CLI ou MCP ?". C'est "pour qui votre agent agit-il ?"**

Tous les benchmarks du débat CLI vs MCP, y compris le leur, testent le même scénario : un développeur unique qui automatise son propre workflow. Dans ce monde, CLI gagne. Évidemment. L'agent hérite de vos credentials, agit avec vos permissions, et la seule personne à risque c'est vous.

Mais ce n'est pas à quoi ressemblent la plupart des produits IA en production. Si vous construisez un SaaS B2B, un outil de gestion de projet, une plateforme de support, un assistant de code review, votre agent n'agit pas en tant que vous. Il agit en tant qu'employés de vos clients, dans les organisations de vos clients, touchant les données de vos clients sur des services que vos clients contrôlent.

Concrètement, imaginons un assistant IA pour une plateforme de gestion de projet. Un utilisateur chez Acme Corp dit : "Crée un ticket Jira depuis cette PR GitHub et notifie l'équipe sur Slack." L'agent doit lire depuis GitHub, écrire dans Jira, et envoyer sur Slack — en utilisant les permissions de cet utilisateur spécifique, limitées aux données d'Acme, sans rien faire fuiter vers le Jira de Globex ou le Slack d'Initech.

C'est trois couches d'identité à résoudre simultanément à chaque action :

**Identité de l'agent** — quel agent fait cette requête ? C'est ainsi qu'on limite les débits, prévient les abus, et maintient une piste d'audit jusqu'à son produit.

**Identité de l'utilisateur** — quel utilisateur a autorisé cette action ? L'agent ne peut faire que ce que cet utilisateur spécifique peut faire. Les scopes OAuth appliquent cela au niveau du protocole.

**Identité du tenant** — à quelle organisation cet utilisateur appartient-il ? Les repos d'Acme ne doivent jamais apparaître dans le Jira de Globex. C'est de l'isolation de données, et se tromper là-dessus n'est pas un bug — c'est une violation.

### Essayons de faire ça avec `gh auth login`

Quand on fait `gh auth login`, l'agent hérite de son token personnel. Un credential, un utilisateur. Maintenant, multipliez par trois organisations, chacune avec des dizaines d'utilisateurs, chacun avec des niveaux de permissions différents sur GitHub, Jira et Slack.

**Un credential, plusieurs utilisateurs.** L'auth CLI donne à l'agent VOTRE token GitHub. Pour agir en tant qu'Utilisateur A chez Acme et Utilisateur B chez Globex, il faudrait gérer un coffre-fort de tokens, swapper les credentials par requête, et gérer les cycles de refresh — tout en code applicatif. _On vient de reconstruire la moitié d'OAuth dans son backend._

**Pas d'isolation des tenants.** Avec des credentials ambiants, il n'y a pas de frontière au niveau protocole entre les tenants. Un bug dans le code de swap de tokens pourrait envoyer les données d'Acme vers le Jira de Globex. _C'est une violation de données, pas un bug._

**Pas de flux de consentement.** Les tokens CLI sont créés par le développeur. Il n'y a aucun moyen pour les utilisateurs finaux d'accorder un accès scopé et de le révoquer plus tard. Il faudrait collecter les credentials directement ou construire sa propre intégration OAuth par service. _On construit de l'infrastructure d'auth, pas son produit._

**Pas de piste d'audit.** L'historique shell enregistre des commandes, pas qui les a autorisées. Quand l'équipe sécurité d'Acme demande "lequel de nos utilisateurs a déclenché cette action GitHub ?", il n'y a pas de réponse au niveau protocole. _Les clients enterprise ne déploieront pas sans ça._

### Ce n'est pas théorique

OpenClaw a montré ce qui se passe quand des agents CLI passent en multi-utilisateur sans autorisation au niveau protocole :

- **Plus de 10 000 instances exposées** faisant fuiter des credentials, des clés API et des tokens de session sur l'internet public. _(Bitsight)_
- **12 % des community skills** s'avèrent malveillants — injectant du code, exfiltrant des données, ou établissant de la persistance. _(Astrix Security)_
- **770 000 agents** ouverts au détournement à distance via une vulnérabilité permettant à des sites malveillants de prendre le contrôle des sessions d'agents. _(SecurityWeek)_

Ce ne sont pas des bugs dans le code d'OpenClaw. Ce sont les conséquences d'une architecture où l'accès shell et les credentials ambiants opèrent sans frontières d'autorisation. Les propriétés qui rendent les agents CLI rapides — auth ambiante, exécution arbitraire, zéro overhead de protocole — sont exactement les propriétés qui créent des incidents de sécurité quand les agents passent d'outil pour développeur à produit orienté client.

### Ce que MCP fait bien : le "protocol tax" achète trois choses que CLI ne peut pas fournir

**Autorisation par utilisateur.** OAuth 2.1 avec PKCE. Chaque utilisateur accorde un accès scopé à l'agent. Il peut voir ce qu'il a autorisé. Il peut le révoquer. L'application ne touche jamais ses credentials. _C'est ainsi qu'on passe la revue de sécurité enterprise._

**Frontières d'outils explicites.** L'agent ne peut appeler que des outils déclarés. Pas de commandes shell arbitraires. Pas de "l'agent a trouvé comment faire un `curl` vers une API privée". Chaque opération est typée, scopée et prévisible. _C'est ainsi qu'on prévient le mode d'échec OpenClaw._

**Piste d'audit structurée.** Chaque appel d'outil produit un enregistrement typé qui adresse le problème de contrôle d'accès des agents : qui l'a autorisé, ce qui a été demandé, ce qui a été retourné. Pas de l'historique shell — structuré, interrogeable, attribuable à un utilisateur et un tenant spécifiques. _C'est ce que la conformité enterprise requiert._

Les propriétés qui rendent MCP cher — schémas explicites, handshakes OAuth, réponses structurées — sont les mêmes qui le rendent gouvernable. On ne paie pas une taxe pour de l'overhead. On paie pour de l'infrastructure d'autorisation que les agents CLI auraient besoin de reconstruire from scratch.

### Framework de décision : adapter le mode au déploiement

| Catégorie | CLI + Skills | MCP (Direct) | MCP via Gateway |
|---|---|---|---|
| **Efficacité en tokens** | Meilleure | Overhead 4-32× | ~Niveau CLI |
| **Fiabilité** | 100 % | 72 % | ~99 % |
| **OAuth par utilisateur** | Non supporté | OAuth 2.1 | OAuth 2.1 + SSO |
| **Isolation des tenants** | Couche applicative uniquement | Session-scopée | Pilotée par policy |
| **Piste d'audit** | Historique shell | Par requête | Centralisée |
| **Idéal pour** | Le développeur est l'utilisateur | Agents agissant pour des clients | Multi-tenant enterprise |

- **Vous construisez un outil pour développeurs où l'utilisateur est le développeur ?** Utilisez CLI + Skills. Ajoutez un fichier de skills de 800 tokens. Vous obtiendrez la meilleure efficacité mesurée, et vous n'avez pas besoin d'auth par utilisateur parce que vous êtes l'utilisateur.
- **Vous construisez un produit où les agents agissent au nom de clients ?** Vous avez besoin du modèle d'autorisation de MCP. Mais ne vous connectez pas directement à des serveurs avec 43 outils — les chiffres de coût et de fiabilité présentés sont réels.
- **Vous construisez de l'infrastructure enterprise multi-tenant ?** Vous avez besoin des deux : le modèle d'auth de MCP pour la gouvernance, plus un gateway qui résout les problèmes d'efficacité et de fiabilité exposés par ce benchmark.

### L'architecture : un gateway offre l'efficacité CLI avec l'autorisation MCP

**Schema filtering.** Au lieu d'injecter les 43 schémas d'outils GitHub, un gateway ne retourne que les 2-3 outils pertinents pour la requête courante. Cela fait passer MCP de 44 000 tokens à ~3 000 — proche de l'efficacité CLI. _~90 % de réduction des tokens._

**Connection pooling.** Au lieu que chaque session d'agent établisse sa propre connexion TCP vers chaque serveur MCP, un gateway maintient des connexions persistantes et absorbe les failures transitoires. _Taux d'échec de 28 % → ~1 %._

**Auth centralisée.** Au lieu que chaque agent gère des tokens OAuth par service, le gateway gère le refresh des tokens, l'application des scopes et la journalisation des audits en un seul endroit. _Une seule frontière d'auth par tenant._

### Reproduire le benchmark

Le framework de benchmark complet est open source :

```bash
git clone https://github.com/scalekit-inc/mcp-vs-cli-benchmark
cd mcp-vs-cli-benchmark
uv sync
uv run bench run --skills --runs 5 --service github --clean
```

Il faut un GitHub PAT et une clé API Anthropic. Le harness exécute les trois modalités, génère des comparaisons statistiques et produit des graphiques interactifs.

### Questions fréquentes

**Quelle est la différence entre MCP et CLI pour les agents IA — et pourquoi est-ce important ?**
MCP est un protocole standardisé pour connecter les agents IA à des outils et sources de données externes via des interfaces structurées et typées avec autorisation intégrée. CLI donne aux agents un accès shell direct pour exécuter des outils en ligne de commande comme `gh`, `psql`, ou `kubectl`. CLI gagne sur l'efficacité — plus rapide, moins cher, plus déboguable. MCP gagne sur la gouvernance — OAuth par utilisateur, frontières d'outils explicites, pistes d'audit structurées. Le choix dépend moins des préférences personnelles que de l'identité pour qui l'agent agit.

**Mon agent fonctionne bien avec CLI aujourd'hui. Quand faut-il penser à MCP ?**
Le point d'inflexion est quand votre agent cesse d'agir en tant que vous et commence à agir au nom d'autres personnes. Si on automatise son propre workflow GitHub, CLI est le bon choix — plus simple et bien moins cher. Mais si on construit un produit où l'agent lit les repos d'un client, écrit dans leur Jira, ou envoie des messages à leur équipe Slack, on est entré dans un territoire où les credentials ambiants de CLI deviennent une dette architecturale.

**Qu'est-ce que le schema bloat et comment le corriger ?**
Le schema bloat se produit parce que les serveurs MCP injectent les définitions de tous les outils disponibles dans chaque conversation d'agent, quelle que soit la tâche. La correction consiste en un schema filtering au niveau du gateway — au lieu de passer les 43 définitions, le gateway ne retourne que les 2-3 outils pertinents pour la requête courante. Cela peut réduire l'utilisation des tokens MCP d'environ 90 %, ramenant les coûts proches de l'efficacité CLI tout en préservant le modèle d'autorisation de MCP.

**Qu'est-ce qu'un MCP gateway fait réellement, et en ai-je besoin ?**
Un MCP gateway se place entre les agents et les serveurs MCP upstream, résolvant les trois problèmes pratiques qui rendent les connexions MCP directes coûteuses et peu fiables. Premièrement, il filtre les schémas — retournant uniquement les définitions d'outils pertinentes pour la tâche courante. Deuxièmement, il pool les connexions — maintenant des connexions TCP persistantes vers les serveurs upstream. Troisièmement, il centralise l'auth — gérant le refresh des tokens OAuth, l'application des scopes et la journalisation des audits en un seul endroit. Si on construit un outil pour développeurs pour son propre usage, on n'a pas besoin d'un gateway. Si on construit un produit multi-tenant où les agents agissent au nom de clients, un gateway est ce qui rend le modèle d'autorisation de MCP économiquement viable.

## Pourquoi ça compte

Ce benchmark ancré dans des données réelles fournit enfin un cadre de décision rationnel pour choisir entre CLI et MCP dans une architecture d'agents IA : l'efficacité seule ne suffit pas comme critère — c'est la frontière d'identité ("le développeur agit-il pour lui-même ou pour ses clients ?") qui détermine le bon choix architectural, avec des implications directes sur la sécurité et la conformité des produits B2B intégrant des agents.
