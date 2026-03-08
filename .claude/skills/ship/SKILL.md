---
name: ship
description: Create branch, commit, push and open a PR
argument-hint: "[issue-number]"
---

# /ship — Create branch, commit, push and open a PR

## 1. Check status

```bash
git status
git branch
```

Verify there are changes to commit. If no changes, notify and stop.

## 2. Create branch

If on `main`, create a new branch with a descriptive name based on the changes:
- `docs/...` for documentation
- `feat/...` for features
- `fix/...` for fixes

If already on a feature branch, stay on it.

## 3. Analyze changes

```bash
git diff
git diff --cached
```

Analyze staged and unstaged changes to understand what was modified.

## 4. Commit

- Stage relevant files (no `git add .`, specific files only)
- Propose a concise commit message using conventional commits format
- **Do NOT include `Co-Authored-By`**
- **Ask for validation before committing**

## 5. Push and PR

```bash
git push -u origin {BRANCH}
```

Open a PR with:
- Short title (< 70 characters)
- Body with `## Summary` (bullets) and `## Test plan` (checklist) sections
- If an argument is provided (e.g. `/ship 17`), add `Closes #$ARGUMENTS` in the body

Confirm the created PR URL.
