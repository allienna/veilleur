---
title: "Enterprise identity was built for humans — not AI agents"
date: 2026-03-11
url: https://venturebeat.com/security/enterprise-identity-was-built-for-humans-not-ai-agents
authors: [VentureBeat, 1Password]
keywords: [identité entreprise, IAM, agents IA, Zero Trust, sécurité]
theme: IA
tone: opinion
used_in: ["2026-03-11"]
---

## Résumé

Les systèmes d'identité d'entreprise (IAM, SSO, RBAC) ont été conçus pour des utilisateurs humains avec des comportements prévisibles et une responsabilité directe. L'arrivée des agents IA autonomes — qui prennent des actions, délèguent de l'autorité et opèrent dans des contextes éphémères — casse ces hypothèses fondamentales. Nancy Wang, CTO de 1Password, argumente que les entreprises doivent repenser leur couche de confiance pour traiter les agents comme des entités à part entière avec des identités vérifiables.

## Points clés

- Les systèmes IAM actuels supposent que toutes les identités sont humaines : comportement cohérent, intention claire, responsabilité directe
- Les agents IA cassent ces hypothèses : autorité déléguée, contextes d'exécution éphémères, boucles de décision rapides
- Le NIST Zero Trust (SP 800-207) exige que toute entité non humaine soit authentifiée et autorisée explicitement
- Les agents ont besoin d'identités propres, pas de credentials hérités ou partagés
- Le problème n'est pas théorique : les agents prolifèrent plus vite que les équipes sécurité ne peuvent les instrumenter
- La solution passe par des identités vérifiables, des périmètres d'accès dynamiques et des traces d'audit granulaires

## Analyse approfondie

L'ajout de capacités agentiques aux environnements d'entreprise refaçonne fondamentalement le modèle de menace en introduisant une nouvelle classe d'acteur dans les systèmes d'identité. Le problème : les agents IA agissent au sein de systèmes d'entreprise sensibles — se connectent, récupèrent des données, appellent des outils LLM, exécutent des workflows — souvent sans la visibilité ni le contrôle que les systèmes d'identité et d'accès traditionnels étaient conçus pour imposer.

Les outils IA et agents autonomes prolifèrent dans les entreprises plus vite que les équipes de sécurité ne peuvent les instrumenter ou les gouverner. En même temps, la plupart des systèmes d'identité supposent encore des utilisateurs statiques, des comptes de service à longue durée de vie et des attributions de rôles grossières. Ils n'ont pas été conçus pour représenter une autorité humaine déléguée, des contextes d'exécution éphémères, ou des agents opérant dans des boucles de décision serrées.

En conséquence, les responsables IT doivent prendre du recul et repenser la couche de confiance elle-même. Ce changement n'est pas théorique. L'Architecture Zero Trust du NIST (SP 800-207) stipule explicitement que "tous les sujets — y compris les applications et les entités non humaines — sont considérés comme non fiables tant qu'ils n'ont pas été authentifiés et autorisés."

Dans un monde agentique, cela signifie que les systèmes IA doivent avoir des identités explicites et vérifiables, et ne pas opérer à travers des credentials hérités ou partagés.

Nancy Wang, CTO de 1Password et Venture Partner chez Felicis, pose le diagnostic : "Les architectures IAM d'entreprise sont construites en supposant que toutes les identités système sont humaines, ce qui signifie qu'elles comptent sur un comportement cohérent, une intention claire et une responsabilité humaine directe pour imposer la confiance. Les systèmes agentiques cassent ces hypothèses. Un agent IA n'est pas un utilisateur qu'on peut former ou auditer périodiquement."

### Solutions nécessaires

L'article préconise plusieurs évolutions :
- Des identités vérifiables pour chaque agent, avec des attributs distincts des identités humaines
- Des périmètres d'accès dynamiques qui s'adaptent au contexte d'exécution
- Des traces d'audit granulaires permettant de retracer chaque action d'un agent
- Une gouvernance adaptée au rythme de déploiement des agents, pas au rythme humain

## Pourquoi ça compte

Cet article met le doigt sur un angle mort critique de l'adoption des agents IA en entreprise : les fondations de sécurité (identité, accès, audit) n'ont pas évolué au même rythme que les capacités agentiques, créant un risque systémique croissant.
