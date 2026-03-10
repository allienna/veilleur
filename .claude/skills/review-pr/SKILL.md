---
name: review-pr
description: Fetch PR review comments, fix issues, reply to each comment
argument-hint: "<pr-number>"
---

# /review-pr — Resolve PR review comments

Takes a PR number as argument (`$ARGUMENTS`). If no argument, detect the current branch PR or list open PRs.

## 1. Detect PR

If no argument provided:
```bash
gh pr view --json number --jq '.number'
```
If that fails, list open PRs and ask.

## 2. Fetch review comments

```bash
gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments --paginate --jq '.[] | select(.in_reply_to_id == null) | "ID: \(.id) | File: \(.path):\(.line // .original_line) | Body: \(.body)"'
```

If no comments: display "No review comments found." and stop.

## 3. Display all comments

For each comment, display:
- File and line number
- Comment body (truncated if very long)
- Your assessment: **relevant** (fix needed) or **not relevant** (explain why)

Ask for confirmation before proceeding with fixes.

## 4. Fix relevant comments

For each relevant comment:
1. Read the file at the referenced line
2. Apply the fix
3. Stage the file

After all fixes are applied:
```bash
git commit -m "fix: address PR review comments"
git push
```

## 5. Reply to each comment

For each comment:

- If it was **fixed**: reply with a short explanation of the fix
  ```bash
  gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments/{COMMENT_ID}/replies -f body="Fixed — {short explanation of what was changed}."
  ```

- If it was **not relevant**: reply explaining why
  ```bash
  gh api repos/allienna/veilleur/pulls/{PR_NUMBER}/comments/{COMMENT_ID}/replies -f body="{explanation why the comment doesn't apply}."
  ```

## 6. Summary

Display a summary:
- Total comments found
- Comments fixed
- Comments dismissed (with reasons)
- Link to the PR
