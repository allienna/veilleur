---
title: "Nobody Pushed Back: Why Engineers Stay Silent Until It's Too Late"
date: 2026-05-19
url: https://howtocenterdiv.com/beyond-the-div/nobody-pushed-back?utm_source=tldrdev
authors: [howtocenterdiv]
keywords: [pushback, alignment, dissent, architectural disasters, leadership]
theme: Leadership
tone: opinion
used_in: ["2026-05-19"]
---

## Résumé

La majorité des catastrophes architecturales ne viennent pas d'un manque de connaissance technique — les ingénieurs *savaient*. Elles viennent du fait que parler coûte plus cher que se taire. L'article documente le pattern à travers Nokia, TSB Bank, Boeing et Microsoft : à chaque fois, les objections existaient mais ne sont jamais arrivées à destination. Le mot à surveiller, c'est *alignment* : "in most companies, alignment is just the corporate name for silencing dissent".

## Points clés

- Les désastres architecturaux ne sont pas un problème de connaissance, c'est un problème de coût social
- "Alignment" est souvent le nom corporate du silence imposé
- Nokia : INSEAD a interviewé 76 cadres et ingénieurs, tous savaient que Symbian était fini face à l'iPhone — personne ne l'a dit
- TSB Bank 2018 : Big Bang cutover, objections "not taken into account", 1,9 million de clients bloqués, 48,6 millions £ d'amende
- Boeing MCAS : ingénieurs s'écrivaient "designed by clowns supervised by monkeys", risque connu, calendriers de production ont gagné
- Pattern récurrent : problème technique visible → coût social du pushback élevé → décision passe sous "alignment" → système casse

## Analyse approfondie

> **TLDR :** La plupart des désastres architecturaux ne sont pas un problème de connaissance. Les ingénieurs savaient. Parler ne valait juste pas le coût.

Quelqu'un déroule une décision d'architecture et personne dans la salle n'est réellement d'accord — ils font juste comme si, parce que dire ce qu'on pense vraiment est socialement coûteux. La réunion se termine, la décision passe. Six mois plus tard, la production explose et tout le monde dit "on savait que ça allait arriver".

Oui. Vous saviez.

La plupart des entreprises ne s'effondrent pas parce que quelqu'un a pris une mauvaise décision. Elles s'effondrent parce que les gens qui voyaient venir le problème ont gardé la bouche fermée. Et la raison pour laquelle ils l'ont fermée n'a rien à voir avec une ignorance technique — c'est que parler coûtait plus cher que de se taire.

### Le pattern

Chaque désastre architectural majeur a la même structure dessous : il y a un problème technique visible, quelqu'un — souvent plus d'une personne — peut le voir, mais pousser back coûte quelque chose, donc la décision passe sous le nom d'"alignment" et le système finit par casser.

Faites attention à ce mot — alignment. Dans la plupart des entreprises, "alignment" est juste le nom corporate qu'on donne au fait de faire taire la dissidence. Ça ne veut pas dire que tout le monde est d'accord. Ça veut dire que personne ne dit à voix haute le contraire. Ce sont deux choses différentes.

### Nokia, TSB, Boeing, Microsoft

**Nokia** : les ingénieurs de Nokia savaient que Symbian était un navire qui coulait. Pas pensé pour l'écran tactile, mauvaise architecture pour bâtir un écosystème d'applis. Quand l'iPhone a été lancé, la lecture la plus aiguë de ce que ça signifiait est venue de l'intérieur de Nokia. Des chercheurs de l'INSEAD sont retournés interviewer 76 dirigeants et ingénieurs Nokia après l'effondrement ; ce qu'ils ont trouvé, c'est que les gens *savaient*, ils ne l'ont juste pas dit — parce que chez Nokia, être la personne qui apportait de mauvaises nouvelles vers le haut était un risque de carrière, pas un mouvement de carrière. L'information existait. Elle n'a juste jamais voyagé. Nokia a vendu sa division téléphone en 2013 pour 7,2 milliards de dollars.

**TSB Bank** : en 2018, TSB a migré son infrastructure IT legacy avec un cutover "Big Bang" — un coup, coupure nette. Le rapport d'enquête indépendant fait 262 pages, et une phrase ressort : des objections techniques ont été soulevées, mais "non prises en compte". Le calendrier de go-live a gagné. Le système s'est effondré, 1,9 million de clients n'ont plus pu accéder à leurs comptes, les régulateurs ont infligé 48,6 millions £ d'amende. Quand l'objection n'a pas été prise en compte, est-ce que quelqu'un a poussé back une seconde fois ? Une troisième ? Personne n'a écrit cette partie.

**Boeing** : en 2020, les messages internes de Boeing sont arrivés au Congrès. Des ingénieurs s'écrivaient : *"This airplane is designed by clowns, who in turn are supervised by monkeys."* Personne ne demande ce qu'ils écrivaient au management — on connaît déjà la réponse. MCAS tirait ses données d'un seul capteur, et le rapport du Congrès documente que le risque technique était connu — et que les calendriers de production ont gagné.

L'article continue avec d'autres exemples (Microsoft, et des cas plus récents dans des entreprises tech), et propose une grille pour distinguer le "vrai" alignment du "faux" alignment, et des pratiques concrètes pour rendre le pushback moins coûteux dans les équipes (anonymat structuré, devil's advocate désigné, mécanismes pour retracer les objections jusqu'à l'écrit, etc.).

### Le mot à surveiller

L'argument central de l'article est qu'au-delà des cas historiques, le mot *alignment* est en train de devenir le marqueur d'une décision qui n'a pas été vraiment discutée. Quand un dirigeant dit que l'équipe est "alignée" sur quelque chose, la bonne question à se poser est : est-ce qu'on est d'accord, ou est-ce qu'on a juste arrêté de dire qu'on ne l'est pas ?

## Pourquoi ça compte

Article essentiel pour les Engineering Directors et leads en pleine vague de décisions IA — où la pression à ne pas casser le récit est particulièrement forte. Le mot "alignment" est partout en ce moment ; cet article apprend à le décoder.
