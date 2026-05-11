---
title: "A well-architected secretary is 76 agents in a trenchcoat"
date: 2026-05-11
url: https://blog.dataexpert.io/p/ai-architecture-is-misunderstood
authors: [Zach Wilson]
keywords: [AI architecture, agents, orchestration, secretary pattern, scribes, agent design]
theme: IA
tone: opinion
used_in: ["2026-05-11"]
---

## Résumé

Zach Wilson plaide contre la confusion actuelle : ce que la plupart des startups vendent comme "AI scribes" (des agents autonomes spécialisés) est utile mais insuffisant. Ce dont les utilisateurs ont vraiment besoin, ce sont des _secrétaires_ compétents, fiables, proactifs — un seul point de contact qui orchestre une multitude d'agents techniques en arrière-plan. L'analogie : un secrétaire bien architecturé, c'est 76 agents dans un trench-coat. La difficulté n'est pas dans la production d'agents — c'est dans l'orchestration et la confiance.

## Points clés

- L'industrie passe par des affordances successives : GPT playground → ChatGPT → RAG → Claude Code (agents) → workflows agentiques → OpenClaw
- La prochaine couche ne sera pas plus d'agents : ce sera l'orchestrateur de confiance ("le secrétaire")
- Le piège : multiplier les scribes ou hooker tous les outils sur un seul assistant qui en oublie la cohérence
- Un secrétaire compétent doit être proactif, fiable, capable de juger ce qui mérite d'être délégué
- L'utilisateur final ne doit pas avoir à interagir avec 76 outils — un seul point de contact dispatche
- C'est beaucoup plus dur à construire que d'aligner des agents en série, mais c'est faisable

## Analyse approfondie

Des centaines de startups (et peut-être une équipe interne dans ton entreprise) essaient, en ce moment, de te construire et te vendre une armée de scribes IA. C'est bien, et ce sera utile. Mais ce dont tu auras réellement besoin, ce sont **des secrétaires compétents, fiables, proactifs.** C'est **beaucoup plus dur.** Mais faisable !

Donc, on a maintenant des robots (LLMs, agents, comme tu veux les appeler). À quoi peut-on les utiliser ?

Eh bien, les robots ont changé de forme ces dernières années. On est passés par ces affordances :

- GPT playground (autocomplétion)
- ChatGPT (chatbot)
- Setups custom (RAG) — comprendre _tes_ fichiers spécifiquement
- Claude Code (agents, dispatchers)
- Workflows "Agent"
- OpenClaw (autonomie + skills + interface texto)

Chacune était utile ! Des entreprises se construisent dessus.

Donc — quoi ensuite ? Et qu'est-ce qu'on peut en apprendre ?

Eh bien, on est sur le point de voir une nouvelle couche — _l'armée de scribes_. Tu seras tenté de les utiliser directement. Tu seras ensuite tenté de les hooker sur ton robot assistant. OK. Mais la vraie réponse, ce sont les secrétaires.

### Pourquoi les "scribes" ne suffisent pas

Un scribe IA, c'est un agent spécialisé : il génère un rapport hebdomadaire, il classe des emails, il rédige des comptes-rendus. Il est efficace _dans son périmètre_. Le problème, c'est que dès qu'une organisation déploie cinq, dix, vingt scribes différents, l'utilisateur final ne sait plus auquel s'adresser, sous quel format, avec quelles permissions. La charge cognitive remonte d'un cran.

Mettre tous ces scribes sous le capot d'un assistant unique, c'est mieux mais insuffisant : si l'assistant ne connaît pas suffisamment le contexte, il dispatche au mauvais scribe ou rate l'intention de l'utilisateur. On retrouve la fragmentation, juste camouflée derrière une UI unifiée.

### Ce que fait un bon secrétaire

Un secrétaire compétent (humain ou IA) fait quatre choses qu'un scribe ne fait pas :

1. **Il connaît ton contexte** — ton calendrier, tes priorités, ta culture, tes contacts
2. **Il sait dire non** ou repousser une tâche qu'il juge inappropriée, ou demander une clarification
3. **Il est proactif** — il anticipe ce dont tu auras besoin, il prépare le terrain
4. **Il sait déléguer** — il sait quand traiter lui-même et quand passer la main à un spécialiste (le scribe)

C'est cette quatrième capacité qui change tout. Le secrétaire orchestre, le scribe exécute. Le secrétaire est l'interface, les scribes sont l'implémentation.

### Pourquoi c'est dur

Construire un agent qui sache faire ces quatre choses ensemble est significativement plus complexe que construire un agent qui rédige bien un email. Il faut :

- Une mémoire long terme du contexte utilisateur (préférences, historique, relations)
- Un système de jugement pour décider _quoi_ déléguer, _quand_, _à qui_
- Une capacité de planification multi-étapes avec rollback
- Une couche de confiance et de validation (HITL/HOTL adapté à chaque type de tâche)

Beaucoup de startups vendent l'idée du secrétaire mais livrent en réalité un scribe avec une interface qui ressemble à un secrétaire. La différence se voit au bout de quelques jours d'usage réel.

### Le design d'orchestration : 76 dans un trench-coat

L'image du titre est volontairement absurde : un seul personnage cohérent, mais à l'intérieur, 76 agents techniques qui s'affairent. C'est l'inversion du paradigme actuel "agent autonome unique" vers un paradigme "interface unique, orchestration interne riche". L'utilisateur ne voit pas la complexité — il voit un interlocuteur qui comprend, qui agit, qui rend des comptes.

Pour les architectes, ça implique de penser deux couches distinctes :

- **La couche d'orchestration** (le secrétaire) : modèle généraliste fort, mémoire utilisateur, capacités de planification et de jugement
- **La couche d'exécution** (les scribes) : agents spécialisés, optimisés sur leur domaine, sans état utilisateur direct

C'est l'architecture qui va distinguer les produits IA gagnants des produits IA gimmicky dans les deux prochaines années.

## Pourquoi ça compte

C'est l'un des frameworks d'architecture IA les plus actionnables de l'année. Pour les architectes et les CTOs qui construisent des produits IA d'entreprise, c'est la grille de design à adopter pour éviter la fragmentation des "armées d'agents" qui submergent l'utilisateur final.
