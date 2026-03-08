---
name: merge
description: Copilot review, comment resolution, squash merge
argument-hint: "<pr-number>"
---

# /merge — Copilot review, comment resolution, squash merge

Takes a PR number as argument (`$ARGUMENTS`). If no argument, list open PRs and ask which one to process.

## 1. Check Copilot comments

```bash
gh pr view {PR_NUMBER} --comments
gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments
```

Analyze inline comments from Copilot (or other reviewers).

## 2. Resolve comments

If inline comments exist:
- Display each comment with its file and line
- Evaluate whether the comment is relevant
- If relevant: apply the fix, commit, push, and reply "Fixed, thanks." via API:
  ```bash
  gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments/{COMMENT_ID}/replies -f body="Fixed, thanks."
  ```
- If not relevant: explain why and ask for confirmation before replying

If no inline comments: skip to step 3.

## 3. Squash merge

Prepare a squash commit message:
- First line: PR title with number (e.g. `docs: add ADR-001 (#18)`)
- Body: concise summary of changes (2-3 lines max)
- Reference `Closes #XX` if an issue is linked
- **Do NOT include `Co-Authored-By`**

**Display the proposed commit message and ask for validation before merging.**

Once validated:
```bash
gh pr merge {PR_NUMBER} --squash --delete-branch --subject "{TITLE}" --body "{BODY}"
```

## 4. Local update

```bash
git checkout main
git pull
```

Confirm the merge is done and main is up to date.
