---
title: "Linus Torvalds to critics of AI coding in Linux: \"Fork it. Or just walk away.\""
date: 2026-07-17
url: https://arstechnica.com/ai/2026/07/linus-torvalds-to-critics-of-ai-coding-in-linux-fork-it-or-just-walk-away/
authors: [arstechnica.com, Kyle Orland]
keywords: [Linux, Torvalds, AI coding, open source, maintainers]
theme: IA
tone: news
used_in: ["2026-07-17"]
---

## Résumé

Linus Torvalds a tranché publiquement dans un long message sur la mailing list du kernel Linux : le projet n'est pas anti-IA, et ceux qui ne sont pas d'accord peuvent « forker ou partir ». Sa position se veut pragmatique, fondée sur le mérite technique et non sur la peur des nouveaux outils. Le débat portait sur l'usage d'un système de revue de code agentique capable de trouver la moitié des bugs, mais aussi de noyer les mainteneurs sous les faux positifs. Torvalds refuse d'imposer un bannissement des LLM et promet « d'ignorer très bruyamment » ceux qui militeraient pour l'interdire.

## Points clés

- Torvalds : « Linux n'est pas un de ces projets anti-IA, et si quelqu'un a un problème avec ça, il peut faire la chose open source : forker. Ou juste partir. »
- Le déclencheur : Sashiko, un système de revue de code agentique pour le kernel, qui trouverait 53,6 % des bugs corrigés ensuite par des humains — mais avec un taux de faux positifs « dans les 20 % ».
- La Software Freedom Conservancy défend le droit des contributeurs à rejeter tout code généré par IA ; Torvalds rejette cette exigence.
- Position affichée : « basée sur le mérite technique. Pas sur la peur des nouveaux outils. »
- Nuance sur la productivité : une étude METR de 2025 mesurait -19 % de productivité chez les devs open source utilisant l'IA, mais une mise à jour de février 2026 estime qu'ils sont désormais probablement accélérés.

## Analyse approfondie

L'arrivée massive des outils de code assistés par IA a provoqué des scissions spectaculaires entre ceux qui les intègrent à leur workflow et les « absolutistes anti-IA » qui ne veulent aucun code généré par LLM près de leurs projets. Concernant le kernel Linux, son créateur et mainteneur en chef, Linus Torvalds, s'est dit « prêt à absolument mettre le pied par terre » en faveur de l'usage des outils d'IA pour améliorer ce projet open source de longue date.

Dans un long message sur la mailing list du kernel cette semaine, Torvalds a écrit que « Linux n'est pas un de ces projets anti-IA, et si quelqu'un a un problème avec ça, il peut faire la chose open source et forker. Ou juste partir. »

La déclaration est intervenue au milieu d'un long fil de discussion sur l'usage de Sashiko, un « système de revue de code agentique pour le kernel Linux » dont les créateurs affirment qu'il peut, en test, trouver indépendamment 53,6 % des bugs qui finiraient corrigés par des humains dans des commits ultérieurs. Mais l'outil peut aussi faire perdre du temps aux mainteneurs en envoyant des rapports « faux positifs » de bugs inexistants, à un taux que les mainteneurs de Sashiko estiment « bien dans la fourchette des 20 % ».

En discutant de la question de savoir si les mainteneurs devraient subir un flot de ce genre d'e-mails de rapports de bugs automatisés (vrais ou faux), un participant a cité la récente prise de position de la Software Freedom Conservancy selon laquelle la communauté open source « devrait soutenir, et pas seulement tolérer, ceux qui rejettent purement et simplement les systèmes d'IA générative fondés sur les LLM » et que « chaque contributeur FOSS mérite l'autodétermination concernant l'IA générative fondée sur les LLM ».

Face à cette prise de position, Torvalds a dit rejeter ceux qui exigent que leurs projets open source n'acceptent aucun code ou révision généré par LLM. « On ne force personne à les utiliser, mais j'ignorerai très bruyamment ceux qui essaient d'empêcher d'autres personnes de les utiliser », a-t-il dit.

### C'est simplement utile… ou pas ?

Torvalds a précisé que sa position est pragmatique, « basée sur le mérite technique. Pas sur la peur des nouveaux outils ». Et sur l'utilité : « L'IA est un outil, comme les autres outils qu'on utilise. Et c'est clairement un outil utile. Ce n'était peut-être pas si "clair" il y a un an, mais ça ne fait plus débat aujourd'hui. […] Ceux qui en doutent n'ont clairement pas vraiment essayé. »

L'an dernier, une étude METR avait trouvé que les codeurs open source utilisant des outils d'IA étaient 19 % moins productifs que ceux qui n'en utilisaient pas — alors même que ces codeurs se sentaient 20 % plus productifs. Mais dans une mise à jour de février sur une étude de suivi, ces mêmes chercheurs estiment qu'« il est probable que les développeurs soient davantage accélérés par les outils d'IA maintenant — début 2026 — par rapport à nos estimations de début 2025 ».

Tout en reconnaissant que « l'IA n'est pas parfaite », Torvalds a invité ses détracteurs à comparer la sortie de ces outils à la performance des mainteneurs humains : « Ceux qui pointent les problèmes de l'IA feraient bien de se regarder dans le miroir en même temps. Parce que l'intelligence naturelle non plus n'est pas toujours si géniale. »

Impliqué dans Linux depuis son annonce en 1991, Torvalds indiquait en janvier qu'il expérimentait le « vibe coding » pour créer un visualiseur audio en Python dans le cadre d'un projet amateur de pédale d'effet pour guitare.

## Pourquoi ça compte

Quand la figure la plus emblématique de l'open source déclare que l'utilité de l'IA « ne fait plus débat », le curseur du débat public se déplace : la question n'est plus de savoir si l'on code avec l'IA, mais comment on protège les mainteneurs du bruit qu'elle génère.
