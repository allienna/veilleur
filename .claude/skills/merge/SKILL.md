---
name: merge
description: Revue Copilot, résolution des commentaires, squash merge
argument-hint: "<pr-number>"
---

# /merge — Revue Copilot, résolution des commentaires, squash merge

Prend en argument un numéro de PR (`$ARGUMENTS`). Si pas d'argument, liste les PRs ouvertes et demande laquelle traiter.

## 1. Vérification des commentaires Copilot

```bash
gh pr view {PR_NUMBER} --comments
gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments
```

Analyse les commentaires inline de Copilot (ou d'autres reviewers).

## 2. Résolution des commentaires

Si des commentaires inline existent :
- Affiche chaque commentaire avec le fichier et la ligne concernée
- Évalue si le commentaire est pertinent
- Si pertinent : applique le fix, commit, push, et répond "Fixed, thanks." au commentaire via l'API :
  ```bash
  gh api repos/allienna/veilleur/pulls/comments/{COMMENT_ID}/replies -f body="Fixed, thanks."
  ```
- Si non pertinent : explique pourquoi et demande confirmation avant de répondre

Si aucun commentaire inline : passe directement à l'étape 3.

## 3. Squash merge

Prépare un message de commit squash :
- Première ligne : titre de la PR avec numéro (ex: `docs: add ADR-001 (#18)`)
- Corps : résumé concis des changements (2-3 lignes max)
- Référence `Closes #XX` si une issue est liée
- **Ne PAS inclure `Co-Authored-By`**

**Affiche le message de commit proposé et demande validation avant de merger.**

Une fois validé :
```bash
gh pr merge {PR_NUMBER} --squash --delete-branch --subject "{TITLE}" --body "{BODY}"
```

## 4. Mise à jour locale

```bash
git checkout main
git pull
```

Confirme que le merge est fait et que main est à jour.
