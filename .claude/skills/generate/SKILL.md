---
name: generate
description: Génère l'article de veille du jour (filtre, rédige, push Notion)
context: fork
argument-hint: "[date]"
---

# /generate — Génère l'article de veille du jour

Lis attentivement le guide d'écriture et le template avant de commencer :
- `${CLAUDE_SKILL_DIR}/writing-guide.md` — persona, style, règles strictes, structure
- `${CLAUDE_SKILL_DIR}/article-template.md` — template de sortie

La date cible est `$ARGUMENTS` si fourni, sinon la date du jour (YYYY-MM-DD).

Effectue les étapes suivantes dans l'ordre :

## 0.5 Feedback métriques

Vérifie s'il y a un article récent sans métriques :

```bash
uv run python3 scripts/track_metrics.py --latest-untracked
```

Si un article sans métriques est trouvé (champ `date` non null) :
- Affiche : "📊 Ton post du {DATE} ({TITLE}) — combien de likes, commentaires, reposts ?"
- Attend la réponse de l'utilisateur
- Enregistre les métriques :

```bash
uv run python3 scripts/track_metrics.py {DATE} --likes {L} --comments {C} --reposts {R}
```

Puis affiche les insights d'engagement :

```bash
uv run python3 scripts/metrics_insights.py --for-generate
```

Si le script retourne du texte, affiche-le. Ces insights guident le choix de l'angle narratif à l'étape 3.

Si aucun article sans métriques (champ `date` null), passe directement à l'étape 1.

## 1. Chargement et filtrage des sources

```bash
uv run python3 scripts/load_sources.py {DATE}
```

Ce script retourne un JSON avec les sources filtrées (sponsors retirés, doublons supprimés, classement par thème).

Affiche un résumé des sources retenues et filtrées, puis demande confirmation avant de continuer.

## 1.5 Détection de tendances

```bash
uv run python3 scripts/detect_trends.py {DATE}
```

Si des tendances sont détectées (clusters avec score > 0), affiche les clusters avec scores et newsletters.
Utilise ces tendances pour guider le choix de l'angle narratif à l'étape 3.
Si aucune tendance (ex: une seule newsletter), passe à l'étape 2.

## 2. Lecture du contenu des sources retenues

```bash
uv run python3 scripts/read_content.py {DATE} 0 1 2 3 ...
```

Passe les valeurs du champ `index` de chaque source retenue (issues du JSON de `load_sources.py`). Le script retourne les 3000 premiers caractères de chaque source.

## 3. Sélection et fil narratif

- Identifie le fil narratif qui relie les meilleures sources entre elles
- Sélectionne 5 à 8 sources principales + 3 à 5 sources "pour aller plus loin"
- Propose le fil narratif et l'angle de l'article, demande validation

## 4. Génération

Génère trois fichiers en suivant le guide d'écriture (`writing-guide.md`) :

### {DATE}-article.md
L'article complet en respectant la structure du template (`article-template.md`).

### {DATE}-post.md
Le texte d'accompagnement du post LinkedIn (voir section "Texte du post LinkedIn" dans le guide).

### {DATE}-image-prompt.md
Le prompt image (voir section "Prompt image" dans le guide).

## 5. Écriture locale

Écris les trois fichiers dans `data/output/`.
Crée le dossier `data/output/` s'il n'existe pas.

## 5.5 Indexation dans l'historique

```bash
uv run python3 scripts/index_article.py {DATE}
```

Non-bloquant : si l'indexation échoue, affiche un avertissement puis continue vers l'étape 6.

## 6. Push Notion

Via le MCP Notion, crée une page dans la base "Veille LinkedIn" avec :
- Titre = titre de l'article
- Date = date du jour
- Status = "À relire"
- Contenu = article.md
- Un callout "📝 Post LinkedIn" avec le contenu de post.md
- Un callout "🎨 Prompt Image" avec le contenu de image-prompt.md

Confirme l'URL de la page Notion créée.
