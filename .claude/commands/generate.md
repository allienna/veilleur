# /generate — Génère l'article de veille du jour

Effectue les étapes suivantes dans l'ordre :

## 1. Chargement et filtrage des sources

Détermine la date cible :
- Si un argument est fourni (ex: `/generate 2026-03-06`), utilise cette date
- Sinon, utilise la date du jour au format YYYY-MM-DD

Lance le script de chargement :

```bash
python3 scripts/load_sources.py {DATE}
```

Ce script retourne un JSON avec les sources filtrées (sponsors retirés, doublons supprimés, classement par thème).

Affiche un résumé des sources retenues et filtrées, puis demande confirmation avant de continuer.

## 2. Lecture du contenu des sources retenues

Une fois les sources validées, lis leur contenu complet avec :

```bash
python3 scripts/read_content.py {DATE} 0 1 2 3 ...
```

Passe les valeurs du champ `index` de chaque source retenue (issues du JSON de `load_sources.py`). Le script retourne les 3000 premiers caractères de chaque source.

## 3. Sélection et fil narratif

- Identifie le fil narratif qui relie les meilleures sources entre elles
- Sélectionne 5 à 8 sources principales + 3 à 5 sources "pour aller plus loin"
- Propose le fil narratif et l'angle de l'article, demande validation

## 4. Génération

Génère trois fichiers :

### {DATE}-article.md
L'article complet en suivant les règles du CLAUDE.md (structure, refs inline, style, etc.)

### {DATE}-post.md
Le texte d'accompagnement du post LinkedIn :
- 3-5 lignes max
- Accrocheur, donne envie de cliquer
- 2-3 hashtags
- Question ou appel à réaction en fin

### {DATE}-image-prompt.md
Un prompt en anglais pour Gemini (Nano Banana) :
- Description visuelle conceptuelle liée au thème
- Pas de texte dans l'image
- Style moderne, épuré

## 5. Écriture locale

Écris les trois fichiers dans `data/output/`.

Crée le dossier `data/output/` s'il n'existe pas.

## 6. Push Notion

Via le MCP Notion, crée une page dans la base "Veille LinkedIn" avec :
- Titre = titre de l'article
- Date = date du jour
- Status = "À relire"
- Contenu = article.md
- Un callout "📝 Post LinkedIn" avec le contenu de post.md
- Un callout "🎨 Prompt Image" avec le contenu de image-prompt.md

Confirme l'URL de la page Notion créée.
