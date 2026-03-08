# veilleur — Projet Veille LinkedIn

## Contexte

Ce projet automatise la génération d'articles LinkedIn quotidiens à partir de ma veille tech.
Je suis Aurélien Allienne, Engineering Director & GenAI Architect chez SFEIR Lille.

## Structure du projet

```
data/
├── raw/                              # Fichiers bruts scrapés par n8n
│   ├── 2026-03-06-newsletter-01.json
│   ├── 2026-03-06-newsletter-02.json
│   └── ...
├── output/                           # Fichiers générés par Claude Code
│   ├── 2026-03-06-article.md
│   ├── 2026-03-06-post.md
│   └── 2026-03-06-image-prompt.md
├── chromadb/                         # Index vectoriel des articles (ChromaDB)
├── metrics.db                        # Métriques LinkedIn (SQLite)
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
- `/search` — Recherche sémantique dans l'historique des articles
- `/ship` — Crée une branche, commit, push et ouvre une PR
- `/merge` — Revue Copilot, résolution des commentaires, squash merge

## Environnement Python

Le projet utilise [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances. Toujours préfixer les commandes Python avec `uv run` :

```bash
uv run python3 scripts/load_sources.py DATE
```

Pour installer les dépendances : `uv sync`

## Scripts utilitaires

Utilise les scripts dans `scripts/` pour les opérations déterministes. Cela évite de réinventer la lecture des données à chaque run.

- `uv run python3 scripts/load_sources.py DATE` — Charge et filtre les sources du jour, retourne du JSON sur stdout (sources classées par thème, sponsors filtrés)
- `uv run python3 scripts/read_content.py DATE 0 2 5` — Lit le contenu complet des sources aux indices donnés (0-indexed depuis la liste complète)
- `uv run python3 scripts/index_article.py DATE` — Indexe l'article du jour dans ChromaDB (vector search)
- `uv run python3 scripts/index_all.py` — Indexe tous les articles existants (backfill)
- `uv run python3 scripts/search_history.py "query" [--limit N]` — Recherche sémantique dans l'historique des articles
- `uv run python3 scripts/track_metrics.py DATE --likes N --comments N --reposts N` — Saisie des métriques LinkedIn d'un post
- `uv run python3 scripts/track_metrics.py --import-csv fichier.csv` — Import CSV des métriques (backfill)
- `uv run python3 scripts/track_metrics.py --latest-untracked` — Retourne en JSON le dernier article sans métriques (`date`, `title`, `themes`, ou `date: null` + `message` si aucun)
- `uv run python3 scripts/track_metrics.py --list` — Liste les métriques récentes
- `uv run python3 scripts/metrics_insights.py` — Rapport d'insights engagement (thèmes, tendances)
- `uv run python3 scripts/metrics_insights.py --for-generate` — Insights formatés pour injection dans /generate

Règle : toujours utiliser ces scripts plutôt que d'écrire du code inline pour lire les fichiers JSON.

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