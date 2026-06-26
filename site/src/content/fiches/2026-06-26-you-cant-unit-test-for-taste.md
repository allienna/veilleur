---
title: "You can't unit test for taste"
date: 2026-06-26
url: https://dev.karltryggvason.com/you-cant-unit-test-for-taste/
authors: [Karl Tryggvason]
keywords: [taste, AI agents, data pipeline, hallucination, DuckDB]
theme: IA
tone: opinion
used_in: ["2026-06-26"]
---

## Résumé

Karl Tryggvason raconte comment il a voulu enrichir son app de running "In the Long Run" avec des points d'intérêt (sites historiques, curiosités) le long de parcours qu'il ne connaissait pas. Il pensait que l'IA serait *la* feature, mais elle a fini en rôle de figuration, à côté du data processing classique. Le fil rouge : le goût et le jugement — savoir ce qui mérite d'être montré — ne se testent pas unitairement, et maîtriser la stack reste la condition pour piloter l'agent plutôt que le suivre aveuglément.

## Points clés

- L'auteur construit "In the Long Run", une app où les coureurs parcourent virtuellement des routes célèbres à partir de leur kilométrage Strava.
- Il voulait enrichir les cartes avec des points d'intérêt, mais ne pouvait pas le faire à la main pour des routes traversant des pays inconnus.
- Stack choisie avec Claude : Python, fichiers Apache Parquet en local, DuckDB comme couche de requête, données issues de GeoNames (licence Creative Commons).
- Ajouter une ou deux technos nouvelles à un projet est la meilleure façon d'apprendre ; tout réapprendre d'un coup décourage.
- Maîtriser *la plupart* des technos permet de mieux piloter l'agent et de prendre des décisions éclairées au lieu de le suivre aveuglément.
- L'IA pensée comme la feature centrale a fini en support : le LLM hallucinait, le goût de sélection ne se programme pas.

## Analyse approfondie

Je construis [In the Long Run](https://inthelongrun.app/), où les coureurs réalisent des courses *virtuelles* sur des parcours célèbres à travers le monde. L'app additionne votre kilométrage Strava et trace votre distance totale comme une progression sur des routes traversant pays et continents. L'intention est de fournir une inspiration et une motivation de long terme ; la vie est un marathon, pas un sprint. Vous pouvez avoir un mauvais mois ou une mauvaise saison et continuer malgré tout à progresser dans votre traversée virtuelle du monde.

L'app montre votre progression sur des cartes interactives, ce qui laisse les utilisateurs explorer par eux-mêmes. Mais je voulais depuis longtemps enrichir les cartes avec des curiosités ou des sites historiques intéressants. Pour les routes que je connaissais, je pouvais construire ces listes moi-même, mais cela ne passe pas à l'échelle pour des routes traversant des pays que je ne connais pas. J'ai donc cherché une source de données de points d'intérêt sur laquelle bâtir un pipeline. En chemin, je me suis débattu avec le goût et les biais, et j'ai lutté contre un LLM qui hallucinait. Je pensais initialement que l'IA serait la feature, mais elle a fini par jouer un simple rôle de support, aux côtés d'autres signaux et des piliers classiques du traitement de données.

### Jeu de données et outillage

[GeoNames](https://www.geonames.org/) était un point de départ évident : une source de données extensive avec localisations, catégories et liens. Le jeu de données complet peut être téléchargé et est sous licence Creative Commons. Donc, avec mon ami Claude, je me suis mis à construire un pipeline allant des dumps bruts jusqu'à servir des points d'intérêt pertinents aux utilisateurs de In the Long Run.

Nous avons utilisé Python comme langage de programmation (bonne disponibilité de bibliothèques pour les tâches à réaliser), stocké les données traitées localement sous forme de fichiers Apache Parquet et utilisé DuckDB comme couche de requête. C'était ma première fois avec Parquet et DuckDB, mais l'ergonomie des deux m'a semblé bonne, et Claude m'a fait découvrir leurs fonctionnalités pas à pas (l'essentiel du travail DuckDB était du SQL que je connais très bien). En général, je trouve qu'ajouter une ou deux nouvelles technos à un projet est la meilleure façon d'apprendre. Si toute la stack vous est nouvelle, la courbe d'apprentissage sera trop raide et risque de vous dégoûter complètement du projet. Les agents de coding IA changent un peu ce calcul, mais même là, avoir une prise sur *la plupart* des technos utilisées me permet de mieux piloter l'agent et de prendre des décisions éclairées au lieu de suivre aveuglément ce qu'il propose.

J'ai construit un plan de projet avec Claude avant de commencer l'implémentation, en détaillant les différentes étapes. Au fil du travail, la difficulté n'était pas tant technique que de jugement : décider, parmi des milliers de lieux candidats, lesquels valaient la peine d'être montrés à un coureur. C'est là que le LLM hallucinait, inventait des sites ou en proposait sans pertinence. Le goût — cette capacité à sélectionner ce qui compte — ne se ramène pas à un test unitaire `expect(x).toBe(y)`. C'est précisément ce qui restait du ressort de l'humain.

## Pourquoi ça compte

Cette histoire concrète illustre la frontière entre ce que l'IA accélère (le pipeline, le SQL, la découverte d'outils) et ce qu'elle ne remplace pas (le goût, le jugement de sélection). C'est exactement la compétence qui prend de la valeur quand le débit de code devient une commodité.
