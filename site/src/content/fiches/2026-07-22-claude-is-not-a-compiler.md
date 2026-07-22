---
title: "Claude Is Not a Compiler"
date: 2026-07-22
url: https://blog.exe.dev/claude-is-not-a-compiler
authors: [blog.exe.dev]
keywords: [coding agents, abstraction layers, judgment, compiler, mechanical sympathy]
theme: IA
tone: opinion
used_in: ["2026-07-22"]
---

## Résumé

Reprenant un billet de 2025 intitulé « Is Claude a Compiler? », l'auteur tranche : voir un agent de code comme un compilateur est une erreur de catégorie — il est en réalité « mieux » qu'un compilateur. Un compilateur prend des décisions dans une seule couche (du code source au binaire) ; un bon agent, lui, travaille à travers les couches. Le billet rappelle que les abstractions fuient, que les couches se frottent, et que la valeur vient précisément de la capacité à traverser ces frontières. La qualité décisive d'un ingénieur reste le jugement.

## Points clés

- Voir l'agent comme une couche qui « compile » le langage naturel en code est une vision stylisée et fausse : les abstractions fuient.
- Un compilateur prend beaucoup de décisions (inlining, allocation de registres, warnings) mais confinées à une seule couche.
- Un bon compilateur libère l'ingénieur de ces décisions sans qu'il ait à savoir comment il fonctionne.
- Travailler à travers les couches a une valeur énorme : la mécanique de sympathie compte.
- L'exemple de l'Empire State Building (construit en moins d'un an, sous budget) illustre l'intérêt de travailler simultanément sur plusieurs couches.
- Le jugement est le critère d'embauche clé d'un ingénieur — et ne se délègue pas mécaniquement.

## Analyse approfondie

Début 2025, j'ai écrit « Is Claude a Compiler? ». À l'époque, ma réponse était : je ne sais pas.

Je suis désormais assez sûr que la réponse est « non, c'est une erreur de catégorie, c'est *mieux* qu'un compilateur. » Mais cela demande un peu de déballage.

Les programmes informatiques sont notoirement complexes et capricieux. Un programme opère à un niveau de précision extrême. Il n'existe pas d'instruction CPU « à la louche ». Les objectifs de haut niveau, eux, sont profondément sous-spécifiés.

Dans une vision très stylisée du monde, le logiciel se construit en couches, chacune ajoutant de la spécification et masquant du détail « inutile ». La vision devient stratégie, les plans produit deviennent plans de code, le code devient binaires. Chaque étape est prise en charge par un rôle différent : dirigeant, VP, PM, architecte, ingénieur, compilateur.

Point crucial : chaque étape implique de prendre beaucoup de décisions. C'est ce que *signifie* augmenter le niveau de spécification. (C'est pourquoi l'une de mes deux métriques clés pour recruter des ingénieurs est le jugement. L'autre est la comity — la capacité à bien travailler ensemble.)

La couche du bas, du code source au binaire, c'est ce que fait un compilateur. Les compilateurs prennent beaucoup de décisions ! Inlining, allocation de registres, choix d'émettre un warning ou de rejeter carrément un programme. Et ces décisions comptent : elles pilotent la performance, la stabilité du système, la prévisibilité et les modes de défaillance. Le travail d'un ingénieur compilateur consiste à faire en sorte que le compilateur prenne des décisions constamment bonnes.

Un bon compilateur, digne de confiance, libère un ingénieur logiciel d'avoir à prendre ces décisions. La plupart des ingénieurs n'ont guère idée du fonctionnement d'un compilateur ; ils n'en ont pas besoin pour être efficaces.

En 2025, on opérait dans un monde où l'on utilisait les LLM pour générer de petits morceaux de code. Dans ce modèle mental, un agent de code pouvait s'insérer comme une nouvelle couche entre l'ingénieur et le compilateur traditionnel. Il « compile » du langage naturel en code, prenant des décisions pour que l'ingénieur n'ait pas à les prendre. Sa valeur est proportionnelle à sa fiabilité et à l'ampleur des décisions qu'il peut prendre.

Le problème, c'est que cette vision très stylisée du monde est fausse. Les abstractions fuient et les couches se frottent. Et même si ce n'était pas le cas, on y percerait des trous de toute façon.

Travailler à travers les couches a énormément de valeur ; la mécanique de sympathie compte.

Une partie de la manière dont l'Empire State Building a été construit en moins d'un an et sous budget (!!) tient à ce travail systématique à travers les couches. Par exemple, pour décider du bardage extérieur en acier chrome-nickel :

> Ni les architectes, ni les constructeurs, ni les sous-traitants ne se sentaient compétents pour traiter ce problème technique complexe de construction sans consultation complète. En conséquence, après discussion préliminaire approfondie, une réunion réunissant tout le monde fut convoquée, à laquelle assistèrent des représentants du maître d'ouvrage [...].

## Pourquoi ça compte

À l'heure où l'on rêve de déléguer tout le code à des agents, ce billet recentre le débat sur ce qui ne se délègue pas : le jugement et la capacité à travailler à travers les couches d'abstraction.
