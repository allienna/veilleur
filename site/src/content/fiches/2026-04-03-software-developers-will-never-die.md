---
title: "Software Developers Will Never Die"
date: 2026-04-03
url: "https://fdoml.r.sp1-brevo.net/mk/cl/f/sh/6rqJfgq8dIW5aVMhAfgvBYZtx7Y/z8JUBcwBOo9s"
authors: ["François Zaninotto"]
keywords: [développement logiciel, agents de codage, automatisation, avenir du développement, Marmelab]
theme: "IA"
tone: opinion
used_in: ["2026-04-03"]
---

## Résumé

Un développeur de Marmelab a reconstruit 80 % d'un CRM existant (Atomic CRM) en 8 heures à l'aide d'un agent de codage (GitHub Copilot + Claude Sonnet) avec Angular. Le code produit est propre, mais pas prêt pour la production. Cette expérience révèle que les logiciels existants sont désormais pratiquement gratuits à reproduire. En revanche, les logiciels nouveaux — ceux qui résolvent des problèmes que personne n'a encore résolus — requièrent toujours l'invention humaine.

## Points clés

- Un agent de codage peut reproduire un CRM fonctionnel en une journée de travail, ce qui était impensable il y a deux ans
- Le code généré est propre mais incomplet : tests insuffisants, configuration de déploiement absente, gestion des erreurs lacunaire
- Les logiciels existants tendent vers un coût de reproduction proche de zéro
- Les logiciels nouveaux — qui résolvent des problèmes inédits — exigent encore de l'invention humaine
- L'article identifie trois catégories : les logiciels existants (reproductibles), les nouveaux (invention requise), et le "milieu boueux" (mélanges des deux)
- Le rôle du développeur évolue vers celui d'architecte, de spécifieur et de réviseur — un peu comme un réalisateur de film

## Analyse approfondie

### L'expérience : reconstruire Atomic CRM en 8 heures

François Zaninotto, fondateur de Marmelab, a mené une expérience concrète : reconstruire Atomic CRM, une application open source développée par son équipe, en utilisant exclusivement un agent de codage — une combinaison de GitHub Copilot et Claude Sonnet — dans un projet Angular. En 8 heures de travail effectif, il a reproduit environ 80 % des fonctionnalités de l'application originale.

Le code produit est propre, lisible, cohérent dans son style. L'agent a suivi les conventions du projet, structuré les composants de façon logique et évité les anti-patterns les plus courants. Mais "propre" ne signifie pas "prêt pour la production" : la couverture de tests est insuffisante, la configuration de déploiement est absente, la gestion des cas limites et des erreurs reste superficielle. L'application tourne, mais elle n'est pas livrable telle quelle.

### Les logiciels existants ne coûtent plus rien à reproduire

La première conclusion de cette expérience est radicale : les logiciels existants sont désormais pratiquement gratuits à reproduire. Si vous pouvez décrire un logiciel — ses fonctionnalités, son domaine métier, son interface — un agent peut en produire une version fonctionnelle en quelques heures. Le coût marginal de reproduction d'un CRM générique, d'un outil de gestion de tickets, d'une application de to-do list tend vers zéro.

Cela a des implications profondes pour le marché du logiciel. Les éditeurs qui vendent des logiciels "standards" — sans différenciation forte — vont faire face à une pression croissante. Pourquoi payer une licence pour un outil qu'un agent peut reconstruire à la demande ? La valeur se déplace vers les données, les intégrations, le support, et surtout vers les logiciels qui font quelque chose que personne n'a encore fait.

### Les logiciels nouveaux requièrent encore des humains

La deuxième conclusion nuance la première : tout ce qui est nouveau — vraiment nouveau — échappe encore aux agents. Un agent peut reproduire ce qui existe parce qu'il a été entraîné sur ce qui existe. Il peut interpoler, combiner, adapter. Mais inventer un concept radicalement nouveau, identifier un problème que personne n'a encore formalisé, concevoir une solution qui n'a pas de précédent dans les données d'entraînement — c'est là que l'humain reste irremplaçable.

L'auteur donne un exemple : Atomic CRM lui-même, dans sa version originale, représentait de l'invention. L'équipe de Marmelab avait fait des choix d'architecture, des compromis de design, des paris sur les besoins des utilisateurs. Ces choix ne viennent pas de nulle part — ils viennent d'une compréhension du domaine, d'expériences passées, d'une vision. C'est cela que l'agent ne peut pas reproduire.

### Le milieu boueux

Entre les deux extrêmes — logiciel purement existant et logiciel purement nouveau — se trouve une vaste zone intermédiaire que l'article appelle le "milieu boueux". La plupart des projets réels s'y situent : ils combinent des patterns connus avec des exigences spécifiques, des intégrations particulières, des contraintes métier inédites. L'agent peut faire beaucoup, mais le développeur doit savoir exactement quoi lui demander, comment évaluer le résultat, et où l'invention humaine reste nécessaire.

C'est dans ce milieu boueux que le travail du développeur se transforme le plus. Il ne s'agit plus seulement d'écrire du code, mais de spécifier avec précision, de réviser intelligemment, et de savoir distinguer ce que l'agent peut faire seul de ce qui requiert une intervention humaine.

### Un nouveau rôle : architecte et réalisateur

L'article conclut sur une métaphore forte : le développeur de demain ressemble davantage à un réalisateur de film qu'à un artisan. Un réalisateur ne joue pas lui-même tous les rôles — il dirige, spécifie, évalue, corrige. Il a une vision d'ensemble et sait comment obtenir de chaque intervenant (acteur, chef-opérateur, monteur) le meilleur résultat.

De même, le développeur de demain sera celui qui sait formuler clairement ce qu'il veut construire, qui peut évaluer si l'agent l'a bien compris, qui détecte les angles morts et les risques que l'automatisation ne voit pas. Les développeurs qui survivront et prospéreront sont ceux qui cultivent ces compétences de haut niveau — spécification, révision, invention — plutôt que ceux qui se contentent d'implémenter ce que d'autres ont spécifié.

## Pourquoi ça compte

Cet article offre un cadre pratique et nuancé pour comprendre comment les agents de codage redistribuent la valeur dans le développement logiciel, sans verser ni dans le catastrophisme ni dans l'euphorie. Il aide les équipes techniques à identifier où concentrer leurs efforts humains face à l'automatisation croissante.
