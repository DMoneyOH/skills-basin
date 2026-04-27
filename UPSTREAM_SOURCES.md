# Skills Basin — Upstream Sources
*Last updated: 2026-04-27*

## Authoritative skill repositories

| Repo | What's there | URL |
|---|---|---|
| anthropics/skills | Official Anthropic skills — docx, pdf, pptx, xlsx source of truth | https://github.com/anthropics/skills |
| outcomeeng/claude | Plugin marketplace: spec-tree, python, typescript, foundation, prose meta-skills | https://github.com/outcomeeng/claude |
| outcomeeng/python | Python coding, testing, architecting, reviewing skills | https://github.com/outcomeeng/python |
| outcomeeng/foundation | Prose writing/reviewing, skill creating/auditing meta-skills | https://github.com/outcomeeng/foundation |
| outcomeeng/spec-tree | Spec-driven development core (requires spx CLI — not pulled) | https://github.com/outcomeeng/spec-tree |
| alirezarezvani/claude-skills | 232+ skills: engineering, marketing, compliance, MCP builder, RAG architect | https://github.com/alirezarezvani/claude-skills |
| Jeffallan/claude-skills | 66 full-stack dev skills: Python Pro, FastAPI, Postgres Pro | https://github.com/Jeffallan/claude-skills |
| glebis/claude-skills | High quality, actively maintained: TDD multi-agent, NotebookLM | https://github.com/glebis/claude-skills |
| travisvn/awesome-claude-skills | Best curated index — primary discovery reference | https://github.com/travisvn/awesome-claude-skills |
| BehiSecc/awesome-claude-skills | Second aggregator — cross-check for coverage gaps | https://github.com/BehiSecc/awesome-claude-skills |
| ComposioHQ/awesome-claude-skills | Composio-curated list with action-capable skills | https://github.com/ComposioHQ/awesome-claude-skills |

## Author reference: simonheimlicher
Simon Heimlicher (https://github.com/simonheimlicher) — creator of outcomeeng.
Primary repo of interest: outcomeeng/claude (pinned).
Other repos are Hugo theme/website work (not skill-relevant).

## Skills pulled and retrofitted from outcomeeng (2026-04-27)

| Skill | Upstream source | Notes |
|---|---|---|
| python-coding | outcomeeng/python — coding-python/SKILL.md | Maeve vault/MCP patterns added; spec-tree dependency removed |
| python-testing | outcomeeng/python — testing-python/SKILL.md | DI-first testing; Maeve Brain DB and MCP fixtures added |
| reviewing-prose | outcomeeng/foundation — reviewing-prose/SKILL.md | Merged with humaznier anti-pattern catalog; listing context added |
| auditing-skills | outcomeeng/foundation — auditing-skills/SKILL.md | Scoped to Maeve skills-basin; Maeve vault paths added |

## Skills intentionally NOT pulled

| Skill | Reason |
|---|---|
| architecting-python | Requires spec-tree/spx workflow — not useful standalone |
| creating-skills | Overlaps with existing skill-creator in /mnt/skills/examples |
| writing-prose | Overlaps with humaznier; reviewing-prose covers the need |
| spec-tree plugins | Full spx CLI workflow — evaluate separately if adopting spec-driven dev |
