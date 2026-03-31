---
title: "J'ai donné un accès SSH à une IA sur mon infrastructure. Voici ce qui s'est passé."
date: 2026-03-31
url: https://faridsaid.com/blog/ia-copilote-infrastructure-it.html
authors: [Farid Saïd]
keywords: [Claude AI, infrastructure IT, audit sécurité, monitoring open source, SSH]
theme: IA
tone: tutorial
used_in: ["2026-03-31"]
---

## Résumé

Farid Saïd, Head of IT dans une société financière suisse, raconte trois mois d'utilisation de Claude AI comme co-pilote opérationnel sur son infrastructure on-prem — switches Cisco, firewalls Palo Alto, stockage, serveurs. En créant un utilisateur SSH en lecture seule sur tous les équipements, il a obtenu en quelques jours ce qui aurait pris des semaines : un audit complet du parc réseau avec des dizaines de findings critiques, une documentation structurée générée depuis les configs réelles, et une stack de monitoring open source déployée (Prometheus, Grafana, Loki, Wazuh). L'article détaille les résultats concrets, les limites identifiées, et propose un guide pratique en cinq étapes pour reproduire la démarche.

## Points clés

- Un audit de sécurité complet de l'ensemble du parc switches (chiffrement, ACLs, protocoles non sécurisés, firmware/CVE, Spanning Tree) a été réalisé en une journée au lieu de 2-3 semaines, avec plus d'une centaine de findings dont plusieurs critiques
- La documentation complète de l'infrastructure — inventaire, topologie réseau, analyse par équipement, politiques de sécurité — a été générée directement depuis les configurations de production, versionnée dans Git
- La migration d'un monitoring propriétaire vers une stack 100 % open source (Prometheus, Grafana, Loki, Wazuh SIEM) a été menée avec l'IA, tout en fichiers texte versionnables
- Le garde-fou fondamental : un utilisateur dédié en lecture seule sur chaque équipement, pas de `configure terminal`, pas d'accès en écriture — la confiance se construit progressivement
- Les limites sont clairement identifiées : pas de décisions business, pas de contexte organisationnel, pas de relations humaines, et des erreurs d'interprétation possibles — "la relève humaine est non négociable"

## Analyse approfondie

### Le contexte : une petite équipe face à une infra qui ne dort jamais

L'auteur gère une infrastructure IT multi-sites dans le secteur financier en Suisse : des dizaines d'équipements réseau répartis sur plusieurs sites, des firewalls, des VPNs, du stockage, de la virtualisation, des systèmes de trading critiques qui ne tolèrent pas de downtime. Avec une équipe réduite, la documentation prend du retard, les audits sont repoussés, les risques s'accumulent en silence. Pas par incompétence — par manque de temps.

### Le déclencheur : "Et si l'IA pouvait lire mes configs ?"

Farid a commencé par utiliser Claude Code (le CLI d'Anthropic) pour documenter du code. Puis il a réalisé que l'agent pouvait se connecter en SSH, lire des running configs et les analyser. Il a créé un utilisateur dédié en lecture seule sur tous ses équipements :

- **Switches Cisco** (NX-OS, IOS, IOS-XE) : commandes `show` uniquement
- **Firewalls Palo Alto** (Panorama) : rôle `superreader`
- **Stockage, serveurs** : accès en lecture aux CLIs

Pas d'accès en écriture. Pas de `configure terminal`. Pas de modification possible. Lecture seule, audit seul.

### Résultat n°1 : audit complet du parc switches

L'IA s'est connectée en SSH à chaque équipement, a récupéré la running config et a analysé selon une grille standardisée : chiffrement des mots de passe, ACLs sur les lignes d'administration, protocoles non sécurisés actifs (HTTP server, Telnet, CDP), Spanning Tree protection (BPDU Guard, Root Guard), ports inutilisés ouverts, NTP, logging, bannières de connexion, firmware et CVE connues.

Résultat : plus d'une centaine de findings, dont plusieurs critiques — serveur HTTP actif sur des switches, lignes d'administration sans ACL, firmware avec CVE non corrigées. Le rapport était structuré par équipement et par sévérité, avec des recommandations concrètes. Un travail qui aurait demandé deux à trois semaines à une personne a été complété en une journée.

### Résultat n°2 : documentation structurée depuis la production

Farid a constitué un repo Git unique avec de la documentation générée directement depuis les configurations réelles : inventaire complet (chaque switch, chaque port, chaque VLAN), topologie réseau en schémas ASCII, analyse détaillée par équipement, documentation sécurité (VPN, règles firewall, politiques d'accès), le tout organisé par site. Ce n'est pas de la documentation théorique — c'est le reflet exact de la production, versionné dans Git.

### Résultat n°3 : audit stockage

L'IA a analysé la configuration complète du système de stockage (baie SAN, haute disponibilité, iSCSI + CIFS) et a révélé une configuration haute disponibilité incomplète, des alertes SNMP non routées, des volumes sans politique de snapshot, et des comptes de service avec droits excessifs. Après application des corrections, un second audit a réduit les findings de deux tiers.

### Résultat n°4 : migration vers un monitoring open source

L'IA a accompagné le passage d'une solution de monitoring propriétaire vers une stack 100 % open source :

- **Prometheus** : collecte de métriques (ICMP, SNMP)
- **Grafana** : dashboards réseau, sécurité, stockage, compute
- **Loki** : agrégation de logs centralisés
- **Wazuh SIEM** : détection d'intrusion et compliance
- **Alertes** : latence, disques, CPU, VPN, certificats expirants

L'avantage clé : tout est en fichiers texte, tout est versionnable dans Git, tout est automatisable.

### Les limites — clairement identifiées

L'auteur identifie quatre limitations importantes :

1. **Pas de décisions business** : l'IA ne peut pas décider si un risque est acceptable en contexte de production
2. **Absence d'expérience contextuelle** : elle ne distingue pas entre un problème réel et un choix architectural volontaire
3. **Relations humaines** : les négociations fournisseurs, les convictions organisationnelles restent humaines
4. **Erreurs possibles** : mauvaise interprétation de configurations, confusion avec des artefacts legacy

"La relève humaine est non négociable."

### Le changement fondamental

La vraie différence n'est pas technique — c'est un changement de posture, du réactif au proactif. Avant l'IA, l'auteur vivait dans l'urgence permanente. Désormais, il peut mener des audits réguliers plutôt que sporadiques, maintenir la documentation à jour, mettre en place un monitoring anticipatif et prendre des décisions informées. Pour une petite équipe IT gérant une infrastructure multi-sites dans un environnement exigeant, c'est un multiplicateur de force.

### Guide pratique en 5 étapes

1. **Commencer par la lecture seule** : accès minimal, construire la confiance progressivement
2. **Documentation d'abord** : générer de la documentation structurée depuis les configs existantes
3. **Puis audits** : formaliser systématiquement sécurité, compliance, bonnes pratiques
4. **Déployer le monitoring** : stack open source (Prometheus, Grafana, Wazuh)
5. **Garder le contrôle** : relire, valider, versionner dans Git

### Outils utilisés

- **Claude Code** (Anthropic) : CLI permettant SSH, lecture de fichiers, exécution de commandes
- **Git** (Gitea self-hosted) : versioning complet
- **Prometheus + Grafana + Loki** : monitoring open source conteneurisé
- **Wazuh** : SIEM open source

L'ensemble est 100 % self-hosted, sans cloud SaaS pour les opérations critiques.

## Pourquoi ça compte

Ce retour d'expérience concret — dans un environnement réglementé, en production, avec des résultats mesurables — démontre que l'IA en tant que co-pilote d'infrastructure est déjà viable pour les équipes IT réduites, à condition de respecter un principe simple : commencer en lecture seule et garder le contrôle humain sur chaque décision.
