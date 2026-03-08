# ADR-006: Migrate from commands to skills with concern separation

- **Status**: Accepted
- **Date**: 2026-03-08

## Context

The project's `CLAUDE.md` currently serves two roles: project documentation (data formats, scripts, directory structure) and article generation rules (writing style, persona, structure, tone). This coupling means every conversation loads generation-specific instructions, even for unrelated tasks like `/ship` or code changes.

Additionally, the five custom commands (`.claude/commands/*.md`) use the legacy commands format. Claude Code now offers a richer skills system (`.claude/skills/*/SKILL.md`) with features that directly benefit this project:

- **`context: fork`** — runs the skill in a subagent with its own context window, preventing heavy source processing (~20-50K tokens) from polluting the main conversation
- **Supporting files** — writing style guide, templates, and examples can live alongside the skill definition
- **Frontmatter control** — `argument-hint`, `disable-model-invocation`, and tool restrictions for cleaner UX

## Decision

Migrate from `.claude/commands/` to `.claude/skills/` and split `CLAUDE.md` into project context vs. generation-specific instructions.

### New structure

```
CLAUDE.md                              ← Project context only
.claude/
├── skills/
│   ├── generate/
│   │   ├── SKILL.md                   ← Workflow steps (context: fork)
│   │   ├── writing-guide.md           ← Persona + style + structure rules
│   │   └── article-template.md        ← Output structure template
│   ├── sources/
│   │   └── SKILL.md
│   ├── search/
│   │   └── SKILL.md
│   ├── ship/
│   │   └── SKILL.md
│   └── merge/
│       └── SKILL.md
└── commands/                          ← Removed after validation
```

### What goes where

**`CLAUDE.md`**: project purpose, directory structure, data formats, Python/uv environment, scripts reference, Notion target, current date.

**`generate/writing-guide.md`**: persona (Engineering Director / GenAI Architect at SFEIR Lille), French writing style, reference format (`[[N](URL)]`), article structure, LinkedIn post format, image prompt format, theme prioritization, disclaimer.

**`generate/SKILL.md`**: step-by-step workflow (metrics → sources → trends → content → narrative → write → index → Notion), referencing `writing-guide.md` for style rules.

## Arguments for this approach

1. **Separation of concerns** — project knowledge and generation rules evolve independently
2. **Context isolation** — `context: fork` keeps source processing out of the main conversation, preserving context window for follow-up edits
3. **Composability** — writing guide can be updated without touching the workflow, and vice versa
4. **Leaner CLAUDE.md** — non-generation tasks (coding, `/ship`, `/merge`) load only what they need
5. **Supporting files** — examples of good articles, style references can be added to the skill directory without cluttering the main config
6. **Better DX** — `argument-hint: [date]` in frontmatter provides autocomplete guidance

## Arguments against

1. **Migration effort** — five commands to convert, requires testing each one
2. **Skills format is newer** — less community documentation and examples available
3. **Forked context tradeoff** — the `/generate` subagent won't see conversation history, making mid-conversation adjustments harder (mitigated: `/generate` is self-contained)
4. **Dual format during migration** — commands and skills coexist temporarily, potential confusion

## Alternatives considered

- **Output styles for writing persona**: changes Claude's global behavior, not task-specific. Writing rules only apply during `/generate`, not all interactions
- **Agent teams for parallel generation**: overkill for a sequential, interactive pipeline with one user
- **Keep commands, just split CLAUDE.md**: misses the `context: fork` benefit and supporting files capability
- **Sub-agents without skills**: possible but skills provide the cleaner packaging and invocation pattern

## Consequences

- `/generate` runs in an isolated context — main conversation stays clean after article generation
- Writing guide updates don't require touching workflow logic or project documentation
- The `.claude/commands/` directory is removed once all skills are validated
- Future enhancements (example articles, per-theme templates) can be added as supporting files in the skill directory
