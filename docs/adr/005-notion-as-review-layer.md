# ADR-005: Notion as review and publishing layer

- **Status**: Accepted
- **Date**: 2026-03-08

## Context

After Claude Code generates the daily article, LinkedIn post, and image prompt, the content needs a human review step before publication. We evaluated where this review should happen and how the content should be stored for the editorial workflow.

## Decision

Use Notion as the review and publishing layer, with content pushed via the Notion MCP integration.

Each generated article creates a page in the "Veille LinkedIn" database with:
- **Title**: article title
- **Date**: generation date
- **Status**: "À relire" (to review)
- **Content**: full article in markdown
- **Callout blocks**: LinkedIn post text and image prompt

## Arguments for this approach

1. **Human-in-the-loop by design** — content is never published automatically; review is mandatory
2. **Rich editing** — Notion provides a comfortable editing experience for tweaking articles before posting
3. **Status tracking** — database properties (À relire → Publié) give a clear editorial workflow
4. **MCP integration** — Claude Code can create pages directly without custom API code
5. **Already in daily workflow** — Notion is already used for personal organization, no new tool to adopt
6. **Mobile access** — articles can be reviewed and approved from phone

## Arguments against

1. **Vendor lock-in** — content lives in Notion's proprietary format, export is possible but lossy
2. **No direct LinkedIn API** — still requires manual copy-paste to publish on LinkedIn
3. **MCP dependency** — relies on Notion MCP server availability and API stability
4. **No version history** — edits in Notion don't track diffs like git would

## Alternatives considered

- **Direct LinkedIn API posting**: fully automated but removes the human review step, risky for personal brand content
- **Headless CMS (Strapi, Ghost)**: more control but requires hosting and is overkill for a single author
- **GitHub PR-based review**: version-controlled but poor editing UX for prose content
- **Google Docs**: good editing but weaker API integration and no database/status tracking

## Consequences

- Articles are always reviewed before publication — this is a feature, not a limitation
- The LinkedIn posting step remains manual (copy from Notion → paste to LinkedIn)
- If automatic scheduling is added (#10), it would post from Notion's "Prêt" status, preserving the review gate
- Content is also saved locally in `data/output/` as markdown, providing a git-backed backup
