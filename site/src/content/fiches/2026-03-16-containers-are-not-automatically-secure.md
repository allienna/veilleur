---
title: "Containers Are Not Automatically Secure"
date: 2026-03-16
url: https://programmingdigest.net/links/21728/8e384055-4ef6-4411-8656-1644e3ae163f/email
authors: [Luca Cavallin]
keywords: [containers, Docker, security, Linux kernel, least privilege]
theme: Tech
tone: tutorial
used_in: ["2026-03-16"]
---

## Résumé

Les conteneurs ne sont pas des frontières de sécurité automatiques — ce sont des processus Linux avec un peu d'isolation. Ils partagent le kernel de l'hôte, ce qui signifie que toute faille du kernel, excès de privilèges ou réseau non segmenté met en danger l'ensemble des workloads. Les correctifs fondamentaux restent les mêmes principes de sécurité vieux de plusieurs décennies : least privilege, defense in depth, réduction de la surface d'attaque.

## Points clés

- Un conteneur est un processus Linux avec de l'isolation, pas une VM — il partage le kernel de l'hôte
- Les namespaces Kubernetes ne sont pas des frontières de sécurité dures entre tenants
- Les correctifs essentiels : tourner en non-root, dropper les capabilities, épingler les digests d'images, restreindre les chemins réseau, gérer les secrets proprement, utiliser seccomp
- La question clé : "si ce workload est compromis, que peut-il atteindre ensuite ?"
- Les conteneurs sont d'excellents outils de packaging mais ne corrigent pas du code applicatif défaillant

## Analyse approfondie

Les conteneurs ont changé la façon dont nous empaquetons et livrons le logiciel, mais ils n'ont pas réécrit les règles fondamentales de sécurité. Les frontières de confiance, les privilèges et la surface d'attaque sont toujours là. C'est l'une des choses apprises en creusant la sécurité des conteneurs, en partie grâce au livre *Container Security* de Liz Rice et en partie en passant du temps avec les composants Linux sous-jacents.

Un conteneur est en réalité juste un processus Linux avec de l'isolation autour. Il communique avec le kernel via des syscalls, s'exécute sous un certain utilisateur, voit un certain système de fichiers, accède à un certain réseau et obtient certaines limites de ressources. Si ces fondations sont faibles, le conteneur l'est aussi.

C'est encore plus évident dans les systèmes réels, car les systèmes réels partagent tout. Clusters partagés, nœuds partagés, machines de build partagées, registres partagés, secrets partagés, erreurs partagées. Quand une couche casse, une autre couche doit empêcher le problème de s'aggraver. C'est pourquoi la sécurité des conteneurs n'est pas une fonctionnalité unique, mais une pile de contrôles pratiques (ennuyeux).

### La sécurité des conteneurs suit les anciennes règles

La première erreur est de traiter un conteneur comme une frontière de sécurité dure. C'est une unité de packaging avec de l'isolation autour — utile et rapide, mais aussi facile à trop faire confiance.

Le modèle de menace commence avec le kernel partagé. Si deux conteneurs tournent sur le même hôte, ils dépendent tous les deux du même kernel. Cela signifie que les bugs du kernel, les montages mal configurés, les capabilities trop larges, les défauts de configuration du runtime, ou même un simple abus de ressources peuvent affecter les autres workloads. C'est beaucoup plus sérieux dans les systèmes multi-tenants. Un service interne de confiance et du code client hostile ne devraient pas être traités comme s'ils avaient le même niveau d'isolation. Il en va de même pour les namespaces Kubernetes : ils sont utiles pour l'organisation et les politiques, mais ne sont pas un mur dur entre les tenants comme l'est une VM.

Rien de tout cela n'est nouveau. Least privilege, defense in depth, réduction de la surface d'attaque, limitation du rayon d'impact, séparation des responsabilités : des idées anciennes qui continuent de réapparaître parce qu'elles résolvent de vrais problèmes.

### Les appels système, les permissions et les capabilities

Chaque conteneur interagit avec le kernel via des appels système. Les capabilities Linux divisent les anciens privilèges root en unités plus fines. Docker accorde un ensemble par défaut qui est raisonnable mais pas minimal. La pratique sûre est de tout dropper et d'ajouter uniquement ce qui est nécessaire.

Les profils seccomp limitent quels appels système un conteneur peut effectuer. Le profil par défaut de Docker bloque environ 44 syscalls sur plus de 300. L'exécution en tant que non-root est la ligne de base.

### Réseau et secrets

Par défaut, les conteneurs Docker sur le même réseau bridge peuvent se joindre librement. En production, les network policies limitent quel conteneur peut parler à quel autre. Les secrets ne doivent jamais être dans les images ou les variables d'environnement.

### Images et supply chain

Épingler les images par digest plutôt que par tag garantit que ce que vous avez testé est ce que vous déployez. Les tags sont mutables. Les images minimales (distroless, scratch) réduisent la surface d'attaque.

## Pourquoi ça compte

Alors que les conteneurs sont devenus le standard de déploiement, cet article rappelle que l'isolation par défaut est insuffisante. Pour tout engineering leader ou architecte, c'est un checklist pratique des fondamentaux de sécurité à ne pas négliger.
