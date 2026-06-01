---
title: "I think Anthropic and OpenAI have found product-market fit"
date: 2026-06-01
url: https://leadershipintech.com/links/22429/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Simon Willison]
keywords: [product-market fit, coding agents, prix API, enterprise, tokens]
theme: IA
tone: opinion
used_in: ["2026-06-01"]
---

## Résumé

Simon Willison analyse la vague de hausses de prix d'avril 2026 chez Anthropic et OpenAI et y voit la preuve qu'ils ont enfin trouvé leur product-market fit avec les agents de code. Ces produits brûlent énormément de tokens mais deviennent les outils quotidiens de professionnels très bien rémunérés. Conséquence : les deux labs ont aligné leurs offres entreprise sur le prix API réel, mettant fin aux remises extrêmes des forfaits forfaitaires.

## Points clés

- Sur son usage perso, Willison a consommé ~2 180 $ de tokens en un mois (1 200 $ Claude Code + 980 $ Codex), facturés 200 $ via Max et Pro.
- Anthropic est fortement pressentie pour son premier trimestre rentable ; les entreprises découvrent des factures LLM bien plus lourdes que prévu.
- Depuis avril 2026, Codex et Claude Code/Cowork sont facturés au prix API réel pour les plans entreprise (20 $/siège + usage).
- GPT-5.5 coûte 2x le prix API de GPT-5.4 ; Opus 4.7 environ 1,4x Opus 4.6 (nouveau tokenizer inclus).
- ChatGPT : 900 M d'utilisateurs hebdomadaires en février, mais seulement 50 M (5,6 %) payants — d'où le pivot vers les pros qui dépensent 200 $+/mois.

## Analyse approfondie

27 mai 2026

Anthropic est fortement pressentie pour réaliser son premier trimestre rentable. Des histoires circulent d'entreprises surprises par le coût de leurs factures LLM dû à l'usage de leurs salariés. Je pense que c'est parce qu'OpenAI et Anthropic ont tous les deux trouvé leur product-market fit.

### Les clients entreprise paient désormais les prix API

Je suis abonné au plan Max à 100 $/mois d'Anthropic et au plan Pro à 100 $/mois d'OpenAI. Si vous êtes un gros utilisateur d'agents de code, ces plans sont une affaire formidable. Je viens de lancer l'outil ccusage sur mon laptop pour estimer ce que j'aurais dépensé en tokens API sur les 30 derniers jours :

- 1 199,79 $ pour Anthropic Claude Code
- 980,37 $ pour OpenAI Codex

Soit 2 180,16 $ de tokens pour 200 $ — pas mal du tout ! Je suis un utilisateur modérément intensif de ces outils, mais je ne fais certainement pas tourner des agents à toute heure du jour et de la nuit.

J'avais supposé que les entreprises faisant un usage intensif d'agents bénéficiaient de remises similaires. Il s'avère que je ne pouvais pas avoir plus tort.

Je n'ai pas réussi à dater précisément l'événement, mais à un moment des six derniers mois Anthropic a fait basculer son plan Enterprise (à l'origine « les sièges Claude incluent assez d'usage pour une journée de travail type », en août 2025) vers 20 $/siège/mois plus la tarification API pour l'usage. Cette histoire de changement, rapportée par The Information, est datée du 14 avril 2026 mais cite un porte-parole d'Anthropic affirmant que le changement a eu lieu en novembre 2025. Les clients existants le découvrent au renouvellement de leurs contrats.

OpenAI a fait un changement similaire en avril. La grille tarifaire de Codex indique désormais :

> Note : Le 2 avril 2026, nous avons mis à jour la tarification de Codex pour l'aligner sur l'usage de tokens API, au lieu d'une tarification par message. Ce changement s'appliquait aux plans Plus, Pro, ChatGPT Business et aux nouveaux plans ChatGPT Enterprise. Le 23 avril 2026, nous avons étendu cette mise à jour à tous les plans ChatGPT Enterprise existants, y compris Edu, Health, Gov et ChatGPT for Teachers.

C'est un peu plus difficile à décoder car ils chiffrent en « crédits », mais pour autant que je puisse en juger, ces coûts en crédits correspondent exactement aux coûts des tokens API listés pour ces modèles.

Tout cela revient à dire qu'en avril 2026, le coût « Enterprise » pour OpenAI Codex comme pour Anthropic Claude Code/Cowork est le même que le prix API affiché.

GPT-5.5 (sorti le 23 avril) coûte 2x le prix API de GPT-5.4. Opus 4.7 (16 avril) coûte environ 1,4x le prix d'Opus 4.6 quand on tient compte de leur nouveau tokenizer.

Avril a donc vu les deux leaders sortir de nouveaux modèles de pointe à un prix API plus élevé, et ces deux entreprises mettre en place des mesures pour verrouiller leurs clients entreprise (qui signent généralement des contrats à l'année) sur ces prix API, et non sur les remises extrêmes précédentes.

### Je pense qu'ils ont trouvé leur product-market fit

Pourquoi ces mouvements de prix soudains et agressifs ? Anthropic et OpenAI prévoient tous deux de s'introduire en bourse, mais je soupçonne un facteur plus important : je pense qu'ils ont enfin trouvé leur product-market fit, avec les produits d'agents de code / généralistes que sont Claude Code/Cowork et Codex.

Des outils comme ChatGPT sont follement populaires, mais cette popularité a été difficile à transformer en revenus. En février, OpenAI se vantait de plus de 900 millions d'utilisateurs actifs hebdomadaires pour ChatGPT, mais seulement 50 millions — 5,6 % — étaient des abonnés grand public payants.

Facturer 10-20 $/mois par utilisateur est un business correct, mais il vous faudrait 1 à 2 milliards d'abonnés restant fidèles pendant quatre ans pour couvrir 1 000 milliards de dollars d'infrastructure.

Des entreprises dépensant 200 $+/mois/utilisateur vous y amènent beaucoup plus vite — et comme noté plus haut, en power user, je suis déjà à ~1 000 $/mois de coûts API par fournisseur.

Les agents de code ont vraiment tout changé. Ce sont des outils qui brûlent vastement plus de tokens, mais qui deviennent aussi rapidement les outils quotidiens du travail effectué par des professionnels extrêmement bien rémunérés. Pour l'instant, c'est surtout des ingénieurs logiciels, mais un agent de code est un outil capable d'automatiser tout ce qu'on peut faire en tapant des commandes dans un ordinateur… donc il s'applique clairement à un ensemble bien plus large de travailleurs du savoir qualifiés.

Comme je l'ai longuement discuté sur ce site, les modèles sortis en novembre 2025 ont élevé les agents au rang de réellement utiles. On a eu six mois pour s'habituer à l'idée — pas étonnant que les entreprises commencent à dépenser de l'argent réel.

## Pourquoi ça compte

Willison apporte la lecture optimiste du même phénomène : si les prix montent, c'est que les agents de code ont enfin de la valeur. C'est l'argument à opposer aux titres alarmistes sur le « coût de l'IA » — et un repère utile pour estimer son propre coût réel via ccusage.
