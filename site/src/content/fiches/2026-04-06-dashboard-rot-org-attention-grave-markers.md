---
title: "Dashboard rot as org attention grave markers"
date: 2026-04-06
url: https://www.counting-stuff.com/dashboard-rot-as-org-attention-grave-markers/?utm_source=tldrdata
authors: [counting-stuff.com]
keywords: [dashboards, data culture, organizational attention, BI, analytics]
theme: Data
tone: opinion
used_in: ["2026-04-06"]
---

## Résumé
Lors d'un audit de dashboards dans une grande organisation, environ la moitié d'entre eux s'avèrent morts, cassés ou inutilisables — et personne ne l'a remarqué. L'auteur propose de voir ces dashboards abandonnés comme des "pierres tombales" de l'attention organisationnelle : chacun raconte l'histoire d'une initiative qui a perdu son sponsor. Contrairement à la sagesse conventionnelle qui préconise de "créer moins de dashboards", l'auteur argue que même les dashboards apparemment superflus avaient une utilité organisationnelle réelle. Le véritable problème n'est pas la sur-création, mais la dégradation naturelle de l'attention dans les organisations.

## Points clés
- Environ 50 % des dashboards dans les grandes organisations sont abandonnés, cassés ou obsolètes, sans que personne ne s'en alarme
- Chaque dashboard abandonné est un "marqueur funéraire" d'une initiative passée : il témoigne de ce qui comptait pour une équipe à un instant donné
- La recommandation habituelle — créer moins de dashboards — passe à côté du vrai problème, qui est la perte d'attention organisationnelle
- Les dashboards, même inutilisés, ont joué un rôle de proxy pour signaler les priorités d'une équipe ou d'un sponsor à un moment donné
- Le "dashboard rot" est un symptôme de la rotation des priorités, des départs d'équipe et du cycle de vie des initiatives, pas d'une mauvaise hygiène de données
- Comprendre pourquoi un dashboard est mort est plus instructif que simplement le supprimer

## Analyse approfondie

### Le constat de départ : la moitié des dashboards sont des fantômes

Lorsqu'on réalise un audit sérieux des dashboards d'une grande organisation — qu'il s'agisse d'un outil comme Tableau, Looker, Power BI ou Metabase — le résultat est presque toujours le même : une proportion considérable des dashboards existants, souvent autour de 50 %, sont dans un état de délabrement avancé. Certains affichent des erreurs de connexion aux sources de données. D'autres ont été construits sur des modèles dbt ou des tables SQL qui n'existent plus. D'autres encore sont simplement figés dans le temps, présentant des chiffres datant de plusieurs mois ou années, sans aucune mise à jour.

Ce qui est frappant, ce n'est pas le nombre de dashboards cassés en soi — c'est que personne ne s'en est plaint. Aucun ticket de support, aucun message Slack, aucune demande de correction. Ces dashboards ont cessé de fonctionner dans le silence le plus complet.

### La métaphore des pierres tombales

L'auteur introduit une métaphore puissante : les dashboards abandonnés sont des "grave markers" — des pierres tombales — de l'attention organisationnelle. Tout comme une pierre tombale dans un cimetière marque l'endroit où quelqu'un a été enterré et rappelle qu'il a existé, un dashboard mort marque le lieu où une attention organisationnelle a existé, a prospéré, puis s'est éteinte.

Chaque dashboard a été créé par quelqu'un, pour quelqu'un, à un moment précis. Il y avait un sponsor — un chef de produit, un directeur, un responsable data — qui avait besoin de suivre un KPI particulier, de surveiller une métrique, d'observer l'évolution d'une initiative. Ce dashboard était la matérialisation de cette attention. Il représentait une question que l'organisation se posait à ce moment-là : "Est-ce que notre campagne d'acquisition fonctionne ? Est-ce que la latence de notre API s'améliore ? Est-ce que nos utilisateurs reviennent après onboarding ?"

Quand ce sponsor est parti — promotion, départ de l'entreprise, réorganisation, fin de l'initiative — le dashboard a cessé d'avoir une raison d'être. Mais personne ne l'a supprimé, parce que personne ne savait qu'il fallait le faire. La question avait cessé d'être posée, mais l'artefact qui la représentait est resté, comme une pierre tombale.

### La critique de la sagesse conventionnelle

Face à ce constat, la réaction habituelle des équipes data est bien rodée : il faut faire du ménage. "Supprimons les dashboards inutilisés", "créons des standards de gouvernance", "limitons qui peut créer des dashboards". L'objectif est de réduire le volume pour maintenir la qualité. C'est la position de nombreuses équipes de BI qui cherchent à avoir un catalogue de dashboards propre, auditable, maintenu.

L'auteur ne rejette pas complètement cette approche, mais il pointe son principal défaut : elle traite le symptôme plutôt que la cause. Supprimer des dashboards abandonnés ne résout pas le problème de la rotation de l'attention organisationnelle. Demain, de nouvelles initiatives verront le jour, de nouveaux sponsors créeront de nouveaux dashboards, et dans six mois, la moitié d'entre eux seront à nouveau des fantômes.

De plus, cette approche risque d'effacer de précieuses informations historiques. Un dashboard abandonné sur une initiative de rétention d'il y a deux ans peut sembler inutile aujourd'hui — mais il contient peut-être une définition métrique, une logique de segmentation, une approche analytique qui serait précieuse pour une nouvelle initiative similaire. En le supprimant sans réfléchir, on perd ce savoir institutionnel.

### Ce que le "dashboard rot" révèle vraiment

Le phénomène de "dashboard rot" — la dégradation progressive des dashboards dans le temps — est en réalité un reflet fidèle de la manière dont les organisations fonctionnent. Les priorités évoluent. Les équipes se restructurent. Les produits pivotent. Les sponsors changent de poste. C'est inhérent à toute organisation dynamique.

Dans ce contexte, le fait qu'un dashboard soit abandonné n'est pas un échec de la gouvernance des données — c'est un signal que l'organisation a changé. Le dashboard a rempli son rôle : il a servi une attention particulière pendant un temps donné. Son abandon est la preuve qu'il a existé, que quelqu'un s'en souciait, et que cette préoccupation a évolué.

La vraie question, selon l'auteur, n'est donc pas "comment éviter le dashboard rot ?" mais "que nous apprend le dashboard rot sur notre organisation ?" Quelles initiatives ont été abandonnées ? Quelles métriques ont cessé d'être suivies ? Où l'attention organisationnelle s'est-elle déplacée ?

### Implications pratiques

Cette perspective change fondamentalement la manière dont les équipes data devraient aborder l'audit de leurs dashboards. Plutôt que de simplement archiver les dashboards morts, il vaut la peine de comprendre pourquoi ils sont morts. Le dashboard de suivi de la rétention client a été abandonné parce que l'équipe CRM a été dissoute ? C'est une information importante sur l'organisation. Le dashboard de surveillance des performances API n'est plus maintenu parce que l'infrastructure a migré vers un autre outil ? Il faut s'assurer que la nouvelle équipe infrastructure a bien repris ce suivi quelque part.

L'auteur suggère ainsi de traiter les dashboards abandonnés non comme des déchets à nettoyer, mais comme des archives à lire. Chaque dashboard mort est un document historique sur ce qui comptait pour l'organisation à un moment donné.

## Pourquoi ça compte
Le "dashboard rot" est un phénomène universel dans les organisations data-driven, et cette relecture par le prisme de l'attention organisationnelle offre un cadre analytique précieux pour les Engineering Directors et les équipes data qui cherchent à comprendre la culture data de leur organisation au-delà des métriques superficielles de gouvernance.
