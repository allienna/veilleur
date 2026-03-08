---
name: sources
description: Affiche les sources du jour triées par thème/priorité
argument-hint: "[date]"
---

# /sources — Affiche les sources du jour

La date cible est `$ARGUMENTS` si fourni, sinon la date du jour (YYYY-MM-DD).

## Exécution

```bash
uv run python3 scripts/load_sources.py {DATE}
```

## Affichage

Affiche un résumé sous forme de tableau à partir du JSON retourné :

| # | Source | Newsletter | Thème | Contenu |
|---|--------|------------|-------|---------|

Où :
- **Source** : titre original (tronqué à 60 chars) + URL
- **Newsletter** : nom de la newsletter d'origine
- **Thème** : IA / Leadership / Data / Tech / Autre
- **Contenu** : longueur du contenu scrapé (ou "vide" si pas de contenu)

Ensuite, affiche les sources filtrées, avec la raison de filtrage (`filter_reason`), en section séparée.

Indique le total par catégorie à la fin.
