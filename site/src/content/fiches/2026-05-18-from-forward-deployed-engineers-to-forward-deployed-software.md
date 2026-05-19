---
title: "From Forward Deployed Engineers to Forward Deployed Software"
date: 2026-05-18
url: https://enterprisecontextmanagement.substack.com/p/from-forward-deployed-engineers-to?utm_source=tldrit
authors: [Enterprise Context Management]
keywords: [forward deployed engineers, enterprise AI, deployment, customer success]
theme: IA
tone: opinion
used_in: ["2026-05-18"]
---

## Résumé

OpenAI, Google Cloud et Anthropic lancent simultanément des programmes massifs de "forward deployed engineers" pour aider les entreprises à adopter leurs solutions IA. OpenAI Deployment Company (4 Md $ de funding, valorisation 10 Md $), des centaines d'ingénieurs chez Google Cloud, et 1,5 Md $ pour Anthropic avec Blackstone, Hellman & Friedman et Goldman Sachs. L'auteur soutient que c'est un symptôme — pas la solution. Ce que le client veut vraiment, c'est du logiciel qui fonctionne dans son environnement, pas une équipe technique embarquée.

## Points clés

- Les trois principaux labs IA lancent des programmes massifs de "forward deployed engineers" simultanément
- OpenAI Deployment Company : 4 Md $ de funding, valorisation 10 Md $, ancrée par TPG, Bain, Brookfield, Goldman Sachs, McKinsey et Capgemini
- Google Cloud (Thomas Kurian) : embauche de centaines d'ingénieurs forward deployed
- Anthropic : 1,5 Md $ avec Blackstone, Hellman & Friedman et Goldman Sachs pour embedder des ingénieurs dans des entreprises de PE
- Le client ne veut pas d'une équipe technique embarquée — il veut le travail fait, dans son environnement
- Le forward deployed engineer est un symptôme de l'écart entre démo et production, pas la solution finale

## Analyse approfondie

_Le marché a découvert les forward deployed engineers. Ça ne veut pas dire que les clients en veulent vraiment._

Au cours des deux dernières semaines, les trois principaux labs frontiers ont chacun saisi le même instrument. OpenAI a lancé l'OpenAI Deployment Company avec plus de 4 milliards de dollars de soutien à une valorisation de 10 milliards de dollars, ancré par TPG, Bain Capital, Brookfield, Goldman Sachs, McKinsey et Capgemini. Le CEO de Google Cloud Thomas Kurian a annoncé des plans pour embaucher des centaines de forward deployed engineers pour former une nouvelle équipe à l'intérieur de Google Cloud. Anthropic s'est associé à Blackstone, Hellman & Friedman et Goldman Sachs sur une venture de 1,5 milliard de dollars pour embedder des ingénieurs dans les sociétés de portefeuille private equity et redessiner les workflows autour de Claude. Le framing dans chaque cas est à peu près le même : **l'IA enterprise est dure, les clients ont besoin d'aide, envoyons les ingénieurs.** **C'est un symptôme d'où on est dans la courbe d'adoption, pas la réponse.** Alors à quoi ressemble la vraie réponse, et qu'est-ce que les clients achètent vraiment ?

### Le vrai problème

Cette montée du forward deployed engineer nous dit que le marché a trouvé un vrai problème : l'IA ne devient pas valuable juste parce qu'un modèle est disponible, qu'un workflow a été démo, ou qu'une intégration existe en théorie. **La partie difficile commence quand le système rencontre l'environnement opérationnel réel du client**, où le process réel n'est pas tout à fait le process documenté, où les handoffs sont messy, où l'ownership est unclear, où les approbations dépendent du contexte, et où les exceptions sont souvent connues de tous mais écrites par personne.

Dans cet environnement, ça a du sens que les entreprises envoient des ingénieurs plus près du client. Quelqu'un doit comprendre comment le travail se passe vraiment avant que le logiciel puisse faire quoi que ce soit d'utile avec ça. **L'erreur, c'est de supposer que parce que le forward deployment est souvent nécessaire au début, c'est ce que le client veut finalement acheter.**

Le client ne se réveille pas en voulant un forward deployed engineer. Il ne veut pas une autre équipe technique embarquée dans son business, un autre delivery model à gérer, ou une autre fonction d'implémentation permanente qui devient silencieusement partie de l'operating model. Ce qu'il veut est plus simple et beaucoup plus dur : **il veut le travail fait, à l'intérieur de l'environnement où le travail se passe déjà, avec assez de fiabilité et de contrôle pour qu'il puisse faire confiance au résultat.**

### Du FDE au FDS

L'auteur propose une transition naturelle : le "Forward Deployed Software" (FDS). Au lieu d'envoyer des humains qui adaptent péniblement la solution, on construit du logiciel qui s'adapte lui-même au contexte. Cela passe par :

- **Configurabilité fine** : permissions, workflows, intégrations paramétrables sans code
- **Apprentissage du contexte** : agents capables de découvrir les conventions internes
- **Patterns de gouvernance prêts à l'emploi** : approbations, audit, séparation de rôles
- **Templates verticaux** : des produits qui encapsulent les patterns d'usage par industrie

### Pourquoi les labs poussent les FDE maintenant

Trois raisons stratégiques :

1. **Adoption** : la complexité du déploiement est le principal frein. Sans aide humaine, beaucoup de pilotes échouent.
2. **Marges** : les FDE permettent de captiver le client, de comprendre ses besoins en profondeur, et de vendre du compute et des services autour.
3. **Distribution** : les partenariats avec McKinsey, Capgemini, Goldman ne sont pas anodins — ils donnent accès aux décideurs des Fortune 500.

Mais c'est un modèle économiquement difficile à scaler. Et ce n'est pas ce que les clients voudront acheter à long terme.

## Pourquoi ça compte

Le déploiement massif de FDE par les trois labs IA est un signal stratégique fort : on est encore au stade où l'IA ne s'auto-déploie pas. Mais c'est aussi un signal d'opportunité pour les ESN, intégrateurs et éditeurs qui sauront packager le "forward deployed software" — la prochaine génération de produits IA enterprise.
