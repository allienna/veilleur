---
title: "Zen of AI Coding"
date: 2026-03-10
url: https://nonstructured.substack.com/p/zen-of-ai-coding
authors: [Nonstructured]
keywords: [agentic coding, software development, code economics, AI agents, developer role]
theme: IA
tone: opinion
used_in: ["2026-03-10"]
---

## Résumé

Un manifeste en 16 principes qui redéfinit le métier de développeur à l'ère des agents de codage. L'auteur, qui construit avec des coding agents au quotidien depuis un an, pose un constat radical : le coût marginal du code s'effondre, et le rôle du développeur migre de la production de code vers le cadrage de problèmes, la définition de contraintes et le jugement des résultats. Le goulot d'étranglement se déplace vers les décisions produit, les tests et les processus de livraison.

## Points clés

- Le développement logiciel en tant qu'activité de production manuelle de code est en train de mourir — une nouvelle discipline naît, centrée sur le cadrage de problèmes et le jugement des résultats
- Le coût marginal du code s'effondre, ce qui déplace le goulot d'étranglement vers les décisions produit, les tests, la sécurité et les processus de livraison
- Les agents peuvent inonder les files d'attente en aval — le vrai levier est dans tout ce qui débloque la livraison (evals, guardrails, observabilité)
- "Du déchet rapide reste du déchet" — la vitesse de production ne dispense pas de la rigueur
- Le rôle du développeur migre vers celui de chef d'orchestre : cadrer, contraindre, juger
- Quand on hésite entre acheter et construire, la réponse est de plus en plus souvent : construire

## Analyse approfondie

Dédié à tous ceux qui sont sceptiques quant à l'importance du coding agentique, et à ceux qui ne le sont pas et se demandent ce que cela signifie pour l'avenir de leur profession. Le titre est un hommage au Zen de Python de Tim Peters. Contrairement à Tim, je ne suis pas un maître zen. Mon seul but est de faire le point sur où nous en sommes et où nous pourrions aller. Je construis avec des agents de codage quotidiennement depuis un an, et j'aide aussi des équipes à les adopter sans perdre en fiabilité ou en sécurité.

1. Le développement logiciel est mort
2. Le code est bon marché
3. Le refactoring est facile
4. Tout comme le remboursement de la dette technique
5. Tous les bugs sont superficiels
6. Créez des boucles de feedback serrées
7. N'importe quelle stack est *votre* stack
8. Les agents ne servent pas qu'au codage
9. Le goulot d'étranglement du contexte est dans votre tête
10. Construisez pour un monde qui change
11. Quand on hésite entre acheter et construire, la réponse, plus souvent, est construire
12. Du déchet rapide reste du déchet
13. Le logiciel est un passif, un produit est un actif
14. Les moats coûtent plus cher
15. Construisez pour les agents
16. Anticipez les modes de défaillance

---

### Le développement logiciel est mort

Vous n'avez plus besoin d'écrire une seule ligne de code si vous ne le souhaitez pas. Les agents de codage peuvent accomplir la plupart des tâches de codage avec la bonne direction.

Le développement logiciel, en tant qu'acte de production manuelle de code, est en train de mourir. Une nouvelle discipline est en train de naître. Votre rôle y est vital, mais il n'est plus centré sur la frappe de code. Il est centré sur le cadrage des problèmes, la mise en forme du contexte, la définition des contraintes et le jugement des résultats.

Le coût marginal du code s'effondre. Ce seul fait change tout ce qui suit.

### Le code est bon marché

L'économie du logiciel a changé.

Quand coder est bon marché, l'implémentation cesse d'être la contrainte. Vous pouvez construire dix choses en parallèle. Vous ne pouvez pas décider, valider et livrer dix choses en parallèle, du moins pas sans changer le reste du pipeline.

Le coût du retard se déplace. Il ne s'agit plus de jours-développeur. Il s'agit du temps bloqué dans d'autres goulots d'étranglement : décisions produit, exigences floues, revue de sécurité, tests utilisateur, processus de release et risque opérationnel. Les agents peuvent inonder ces files d'attente. L'inventaire croît. Le lead time croît. Le retard devient plus cher, pas moins.

Cela change la priorisation. Le travail à plus fort levier est celui qui débloque la livraison : boucles de feedback serrées, tests, evals, guardrails, observabilité et critères d'acceptation clairs. Tout ce qui transforme "on peut le construire" en "on peut lui faire confiance".

Les agents peuvent aider à alléger certains de ces goulots d'étranglement. Le défi est de les appliquer en dehors du codage.

## Pourquoi ça compte

Ce manifeste articule de façon claire et structurée le basculement en cours dans le métier de développeur. Il pose les bases intellectuelles d'une réflexion nécessaire pour tout engineering leader qui pilote l'adoption d'agents IA dans ses équipes.
