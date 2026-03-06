# veilleur — Projet Veille LinkedIn

## Contexte

Ce projet automatise la génération d'articles LinkedIn quotidiens à partir de ma veille tech.
Je suis Aurélien Allienne, Engineering Director & GenAI Architect chez SFEIR Lille.

## Structure du projet

```
../data/
├── YYYY-MM-DD/           # Un dossier par jour
│   ├── raw/              # Fichiers bruts scrapés par n8n
│   │   ├── newsletter-1.json
│   │   ├── newsletter-2.json
│   │   └── ...
│   ├── sources.json      # Sources filtrées et sélectionnées
│   ├── article.md        # Article généré
│   ├── post.md           # Texte du post LinkedIn
│   └── image-prompt.md   # Prompt pour Gemini
```

## Format des fichiers raw (produits par n8n)

Chaque `newsletter-X.json` contient :
```json
{
  "newsletter": "Nom de la newsletter",
  "received_at": "2026-03-06T08:30:00Z",
  "links": [
    {
      "url": "https://...",
      "title": "Titre du lien",
      "content": "Contenu markdown scrapé via Jina Reader"
    }
  ]
}
```

## Commandes disponibles

- `/generate` — Génère l'article du jour (filtre, rédige, push Notion)
- `/sources` — Affiche les sources du jour triées par pertinence

## Règles de génération

### Filtrage des sources
- Retirer les liens marketing, sponsorisés, promotionnels
- Retirer les doublons (même URL ou contenu quasi-identique)
- Prioriser les thèmes : IA, Leadership, Data, actualités tech
- Garder minimum 5 sources pour l'article

### Style de l'article
- Français, direct, personnel — utilise "je" et implique le lecteur
- Phrases courtes, paragraphes légers
- Pas de jargon inutile, pas de ton "corporate"
- Fil narratif cohérent entre les sections, pas une liste de liens commentés

### Références inline
- Format : `[[N](URL)]` placé juste après le fait ou l'idée
- Chaque source référencée dès sa première utilisation
- Les réutilisations ultérieures reprennent le même format

### Structure de l'article
- Titre percutant (question ou affirmation forte)
- Intro (3-4 lignes) : question provocante au lecteur + fait/chiffre. Pas de "je", pas d'anecdote perso
- Sections avec sous-titres en gras, NON numérotés, liés par un fil narratif
- Blockquote si citation forte dans les sources
- Conclusion avec question ouverte
- Section Sources (liste numérotée avec titres originaux + URLs)
- Section "Pour aller plus loin" (3-5 ressources complémentaires)
- Disclaimer en italique

### Titres des sources
- Toujours conservés dans leur langue originale, sans traduction

### Texte du post LinkedIn
- Court, accrocheur, donne envie de lire l'article
- Inclut 2-3 hashtags pertinents
- Termine par une question ou un appel à réaction

### Prompt image
- Descriptif en anglais pour Gemini (Nano Banana)
- Style : illustration conceptuelle, pas de texte dans l'image
- Lié au thème principal de l'article

## Output Notion

Utiliser le MCP Notion pour créer une page dans la base "Veille LinkedIn" avec :
- Titre de l'article
- Propriété "Date" : date du jour
- Propriété "Status" : "À relire"
- Contenu : article complet en markdown
- Bloc "Post LinkedIn" en callout
- Bloc "Prompt Image" en callout
