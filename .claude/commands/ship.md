# /ship — Crée une branche, commit, push et ouvre une PR

Effectue les étapes suivantes dans l'ordre :

## 1. Vérification de l'état

```bash
git status
git branch
```

Vérifie qu'il y a des changements à committer. Si aucun changement, préviens et arrête.

## 2. Création de branche

Si on est sur `main`, crée une nouvelle branche avec un nom descriptif basé sur les changements :
- `docs/...` pour de la documentation
- `feat/...` pour des fonctionnalités
- `fix/...` pour des corrections

Si on est déjà sur une feature branch, reste dessus.

## 3. Analyse des changements

```bash
git diff
git diff --cached
```

Analyse les changements staged et unstaged pour comprendre ce qui a été modifié.

## 4. Commit

- Stage les fichiers pertinents (pas de `git add .`, fichiers spécifiques uniquement)
- Propose un message de commit concis au format conventional commits
- **Ne PAS inclure `Co-Authored-By`**
- **Demande validation du message avant de committer**

## 5. Push et PR

```bash
git push -u origin {BRANCH}
```

Ouvre une PR avec :
- Titre court (< 70 caractères)
- Body avec section `## Summary` (bullets) et `## Test plan` (checklist)
- Référence l'issue GitHub si un argument est fourni (ex: `/ship 17` → `Closes #17`)

Confirme l'URL de la PR créée.
