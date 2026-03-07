# /sources — Affiche les sources du jour

Lance le script de chargement :

```bash
python3 scripts/load_sources.py {DATE}
```

Où {DATE} est l'argument fourni (ex: `/sources 2026-03-06`) ou la date du jour si pas d'argument.

Affiche un résumé sous forme de tableau à partir du JSON retourné :

| # | Source | Newsletter | Thème | Contenu |
|---|--------|------------|-------|---------|

Où :
- **Source** : titre original (tronqué à 60 chars) + URL
- **Newsletter** : nom de la newsletter d'origine
- **Thème** : IA / Leadership / Data / Tech / Autre
- **Contenu** : longueur du contenu scrapé (ou "vide" si pas de contenu)

Ensuite, affiche les sources filtrées (sponsors) en section séparée.

Indique le total par catégorie à la fin.
