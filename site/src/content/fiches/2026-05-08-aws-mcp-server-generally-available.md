---
title: "The AWS MCP Server is now generally available | Amazon Web Services"
date: 2026-05-08
url: https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/?utm_source=tldrit
authors: [AWS, Amazon Web Services]
keywords: [MCP, AWS, agents, IAM, cloud infrastructure]
theme: IA
tone: news
used_in: ["2026-05-08"]
---

## Résumé

AWS annonce la disponibilité générale (GA) de son AWS MCP Server, une couche managée qui permet aux agents IA et aux assistants de coding d'accéder de façon authentifiée aux 15 000+ APIs AWS via un petit nombre d'outils compacts. L'objectif : donner aux agents un accès productif au cloud sans exploser leur fenêtre de contexte ni distribuer des permissions trop larges. Cette GA marque une étape clé : le cloud commence à proposer une infra spécifiquement pensée pour les agents.

## Points clés

- AWS MCP Server passe en GA, intégré au "Agent Toolkit for AWS"
- Outil principal `call_aws` : exécute n'importe quelle des 15 000+ APIs AWS avec les credentials IAM existants
- Outils `search_documentation` et `read_documentation` : accès en temps réel à la doc AWS pour éviter les hallucinations
- Support des IAM context keys : plus besoin de permission séparée pour utiliser le serveur
- Documentation accessible sans authentification, surface d'outils compacte pour économiser le contexte modèle

## Analyse approfondie

Cela fait un moment que je construis avec des agents IA et des outils MCP, et une question revient sans cesse : comment donner à un agent un accès réel et authentifié à AWS sans lui confier toutes les clés du royaume ? Aujourd'hui, il y a une réponse.

J'ai le plaisir d'annoncer la disponibilité générale du AWS MCP Server, un serveur Model Context Protocol (MCP) managé et distant qui offre aux agents IA et aux assistants de coding un accès sécurisé et authentifié à tous les services AWS via un ensemble réduit et fixe d'outils.

Le AWS MCP Server fait partie de l'Agent Toolkit for AWS, une suite d'outillage qui inclut le MCP Server, des skills et des plugins permettant aux agents de coding de construire plus efficacement sur AWS.

Les agents de coding sont déjà utiles pour de nombreuses tâches, mais ils rencontrent de vrais problèmes dès qu'il s'agit de travailler avec AWS en profondeur. Sans accès à la documentation AWS à jour, ils se basent sur des données d'entraînement qui peuvent avoir plusieurs mois de retard et ne pas connaître des services comme Amazon S3 Vectors, Amazon Aurora DSQL ou Amazon Bedrock AgentCore. Quand on leur demande de construire de l'infrastructure, ils ont tendance à se rabattre sur l'AWS CLI plutôt que sur AWS CDK ou CloudFormation, et ils produisent des politiques IAM beaucoup trop permissives. Le résultat : une infrastructure qui marche en démo mais qui n'est pas production-ready.

Le AWS MCP Server résout ce problème via un ensemble compact d'outils qui ne consomment pas la fenêtre de contexte du modèle. L'outil `call_aws` exécute n'importe laquelle des 15 000+ opérations APIs AWS en utilisant les credentials IAM existants. Quand AWS lance de nouvelles APIs, elles sont supportées en quelques jours. Les outils `search_documentation` et `read_documentation` récupèrent la documentation AWS et les bonnes pratiques à jour au moment de la requête, donc l'agent travaille toujours avec des informations fraîches.

Avec la GA, plusieurs nouvelles capacités sont introduites. Le AWS MCP Server supporte désormais les IAM context keys : tu n'as plus besoin d'une permission IAM séparée pour utiliser le serveur, et tu peux exprimer un contrôle d'accès fin via une politique IAM standard. La récupération de documentation ne nécessite plus d'authentification. Le nombre d'outils a été réduit pour limiter la surface et améliorer la fiabilité.

Le serveur peut s'utiliser depuis n'importe quel client compatible MCP (Claude Code, Q Developer, Cursor, etc.). L'authentification se fait via un flow OAuth qui réutilise les credentials AWS existants. Une fois connecté, l'agent peut lire la documentation, requêter les services et — avec les permissions adéquates — créer ou modifier des ressources.

Le positionnement stratégique est clair : AWS ne cherche pas à freiner la charge agentique, mais à offrir une couche d'abstraction qui la rend gérable, auditable et conforme aux pratiques de sécurité existantes.

## Pourquoi ça compte

La sortie en GA d'un MCP Server par un hyperscaler, c'est le signal que l'infra cloud commence à se réorganiser autour des agents. Pour un architecte, c'est l'occasion de clarifier le standard MCP côté entreprise, et de poser la question des permissions d'agents avant qu'elle ne devienne un sujet d'audit.
