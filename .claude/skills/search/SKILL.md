---
name: search
description: Recherche sémantique dans l'historique des articles
argument-hint: "<query>"
---

# /search — Recherche dans l'historique des articles

Effectue une recherche sémantique dans les articles passés indexés dans ChromaDB.

## Exécution

```bash
uv run python3 scripts/search_history.py "$ARGUMENTS" --limit 5
```

## Affichage des résultats

Affiche les résultats sous forme de tableau :

| Date | Titre | Pertinence | Thèmes | Extrait |
|------|-------|------------|--------|---------|

Si aucun résultat, indique que l'historique est vide et suggère de lancer `uv run python3 scripts/index_all.py` pour indexer les articles existants.
