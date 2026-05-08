---
title: "The Pulse: AI load breaks GitHub – why not other vendors?"
date: 2026-05-08
url: https://blog.pragmaticengineer.com/the-pulse-ai-load-breaks-github/?utm_source=tldrnewsletter
authors: [Gergely Orosz, Pragmatic Engineer]
keywords: [GitHub, agents, infrastructure, scalability, AI load]
theme: Tech
tone: opinion
used_in: ["2026-05-08"]
---

## Résumé

Le 5 mai 2026, GitHub a connu une journée chaotique avec six incidents majeurs en cascade. La cause principale n'est ni un déploiement raté ni une attaque, mais la charge générée par les agents de codage IA — Codex, Claude Code, Copilot — qui clonent, lisent et commitent à un rythme inédit. Gergely Orosz analyse pourquoi GitHub semble plus impacté que GitLab ou Bitbucket : c'est le centre de gravité de l'écosystème dev, donc le premier exposé à cette nouvelle catégorie de charge automatisée.

## Points clés

- Six incidents majeurs en une journée sur GitHub, pic anormal lié à la charge des agents
- Les agents IA génèrent un trafic radicalement différent des humains : volume, parallélisme, persistance
- GitHub est plus exposé que ses concurrents car il est l'hôte de référence de l'écosystème open source et propriétaire
- La question dépasse l'incident technique : c'est un changement structurel de la charge utilisateur des plateformes de code
- Les fournisseurs cloud (AWS notamment) anticipent cette mutation avec des couches dédiées aux agents

## Analyse approfondie

Le 5 mai 2026, GitHub a essuyé une succession d'incidents qui ont rendu de larges pans de la plateforme inutilisables. Six incidents majeurs ont été enregistrés sur la même journée — un volume rare pour un acteur d'infrastructure aussi critique. La cause technique n'est pas un déploiement défectueux ni une attaque externe : c'est la charge applicative générée par les agents de codage IA qui a fini par dépasser les limites de scaling.

Concrètement, Codex, Claude Code, Copilot et leurs équivalents ne se contentent pas de lire passivement un repo : ils clonent, parcourent, ouvrent des centaines de fichiers, lancent des recherches récursives, créent des branches, ouvrent des PRs, font tourner des CI à l'échelle. Multiplié par le nombre d'utilisateurs concurrents et la persistence (un agent ne fait pas de pause), le motif de charge n'a plus rien à voir avec celui d'un développeur humain.

La vraie question posée dans l'article n'est pas "qu'est-ce qui a cassé GitHub" mais "pourquoi GitHub plutôt que GitLab ou Bitbucket". La réponse tient à la position centrale de GitHub dans l'écosystème : c'est l'hôte par défaut des projets open source, des modèles de fondation, des dépôts d'agents eux-mêmes. Quand un nouveau type de charge émerge, GitHub le prend en pleine face avant les autres.

L'article suggère que cette situation va s'amplifier. Les agents deviennent plus autonomes, les sessions plus longues (cf. le `/goal` de Codex qui tourne plusieurs heures sans intervention humaine), les workloads plus parallélisés. Les plateformes de code doivent désormais raisonner comme des plateformes machine-to-machine, pas comme des plateformes humain-à-machine.

Cet incident est aussi un signal politique : les hyperscalers comme AWS sortent au même moment des serveurs MCP managés, conçus pour absorber la charge agentique en GA. La plomberie cloud anticipe ce que GitHub découvre dans la douleur.

## Pourquoi ça compte

Cet incident marque un point de bascule : la charge IA n'est plus une expérimentation, c'est une couche métier qui sature les infrastructures historiques. Pour un Engineering Director, c'est un argument concret pour repenser les SLAs internes et la dépendance à un fournisseur unique.
