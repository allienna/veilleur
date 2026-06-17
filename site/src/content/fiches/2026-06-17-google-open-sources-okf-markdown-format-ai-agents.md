---
title: "Google Open-Sources OKF, a Markdown Format for AI Agents"
date: 2026-06-17
url: https://www.implicator.ai/google-open-sources-a-knowledge-format-and-wires-it-into-its-catalog/?utm_source=tldrit
authors: [implicator.ai, Marcus Schuler]
keywords: [Google, Open Knowledge Format, markdown, agents IA, standard]
theme: IA
tone: news
used_in: ["2026-06-17"]
---

## Résumé

Google Cloud a publié le 12 juin l'Open Knowledge Format (OKF), un standard ouvert et neutre représentant la connaissance des agents IA comme un répertoire de simples fichiers markdown, avec une seule métadonnée obligatoire. Le même jour, Google a branché ce format dans son Knowledge Catalog payant, qui ingère l'OKF et le sert aux agents — la couche que la spécification laisse hors de son périmètre. L'ouverture du format est ici une stratégie : commoditiser la connaissance pour rediriger la demande vers la couche de service payante.

## Points clés

- OKF représente la connaissance d'un agent comme un dossier de fichiers markdown, avec une unique métadonnée requise (451 lignes de spec).
- Écrit par les tech leads Google Cloud Sam McVeety et Amir Hormati, décrit comme « un format, pas une plateforme ».
- Le jour même de la publication, Google a mis à jour son Knowledge Catalog payant pour ingérer et servir l'OKF aux agents.
- La spec exclut explicitement le stockage, le service et l'infrastructure de requête (non-goals).
- OKF formalise le pattern « LLM wiki » d'Andrej Karpathy, déjà répandu via les fichiers AGENTS.md de plus de 60 000 projets open-source.
- L'adoption par des tiers (Atlan, Alation, Collate) décidera si OKF devient réellement un standard.

## Analyse approfondie

Google Cloud a publié le 12 juin une spécification représentant le contexte dont les agents IA ont besoin comme un répertoire de fichiers markdown en clair, et a mis à jour le même jour son produit Knowledge Catalog pour lire ce format et le servir aux agents. L'Open Knowledge Format, écrit par les tech leads de Google Cloud Sam McVeety et Amir Hormati, fait 451 lignes et n'exige qu'un seul champ de chaque document. Hormati l'a décrit sur LinkedIn comme « un format, pas une plateforme ».

OKF donne ce qui n'a jamais été rare — un fichier que n'importe quel éditeur de texte peut ouvrir — et oriente la demande qu'il crée vers ce que Google vend : la couche qui stocke la connaissance, la sert aux agents et contrôle qui peut la voir. L'ouverture est le mécanisme, car un format libre et portable transforme la couche de connaissance en commodité et redirige la demande vers le catalogue, la gateway et le compute que Google ne donne pas. Le blog de Google le formule autrement : la valeur d'un format de connaissance « vient du nombre de parties qui le parlent, pas de qui le possède ».

### Ce que la spec laisse de côté

La spécification est précise sur ses limites. Dès sa section d'ouverture, OKF liste comme non-goals « la prescription du stockage, du service ou de l'infrastructure de requête » et le remplacement des schémas de domaine tels qu'Avro, Protobuf ou OpenAPI. Autrement dit : OKF décrit comment représenter la connaissance, mais pas comment la stocker, la servir ou en contrôler l'accès — précisément les briques que Google monétise via son Knowledge Catalog.

Le contexte historique est éclairant : OKF formalise le pattern « LLM wiki » popularisé par Andrej Karpathy, déjà largement diffusé à travers les fichiers AGENTS.md utilisés par plus de 60 000 projets open-source. Reste la question de l'adoption : tous les bundles d'exemple ont été construits par Google. Ce sont des acteurs comme Atlan, Alation ou Collate qui, en adoptant ou non le format, décideront si OKF devient un véritable standard de l'industrie.

## Pourquoi ça compte

OKF illustre la nouvelle bataille de plateforme : on ouvre la couche de connaissance (markdown, gratuit) pour mieux capter la valeur sur la couche de service (catalogue, gateway, compute). Pour qui construit des agents durables, la mémoire devient un actif stratégique — et un point de lock-in à surveiller.
