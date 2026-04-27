# Skills Basin Session Notes — 2026-04-27

## What was done this session

### skill_registry — correctly updated via brain_upsert
| id  | skill_name           | tier   | basin_path                                         | source |
|-----|----------------------|--------|----------------------------------------------------|--------|
| 499 | coding-python        | active | ~/vault/skills-basin/user/coding-python            | outcomeeng/python — retrofitted |
| 500 | testing-python       | active | ~/vault/skills-basin/user/testing-python           | outcomeeng/python — retrofitted |
| 501 | reviewing-prose      | basin  | ~/vault/skills-basin/user/reviewing-prose          | outcomeeng/foundation — humaznier supersedes |
| 502 | auditing-skills      | active | ~/vault/skills-basin/user/auditing-skills          | outcomeeng/foundation — retrofitted |
| new | auditing-python      | active | ~/vault/skills-basin/user/auditing-python          | outcomeeng/python — retrofitted |
| new | standardizing-python | basin  | ~/vault/skills-basin/user/standardizing-python     | outcomeeng/python — support skill only |
| new | creating-skills      | active | ~/vault/skills-basin/user/creating-skills          | outcomeeng/foundation — retrofitted |
| new | writing-prose        | active | ~/vault/skills-basin/user/writing-prose            | outcomeeng/foundation — retrofitted |

### SKILL.md files written to ~/vault/skills-basin/user/
All 8 skills above have SKILL.md files. Retrofitted from outcomeeng originals:
- spec-tree dependencies removed
- vault toolchain substituted (uv, ruff, mypy, pytest)
- Maeve/Derek preferences applied (no em-dashes, DI patterns, etc.)

### upstream/SOURCES.md
Written to ~/vault/skills-basin/upstream/SOURCES.md as a markdown reference.
This is supplementary to skill_registry. Does NOT replace the external/ pattern.

## What is PENDING — needs desktop action

### 1. Create upstream_sources table in brain
Script written to: ~/vault/utils/core-skills/create_upstream_sources.py
Run manually on desktop: `python3 ~/vault/utils/core-skills/create_upstream_sources.py`

### 2. Clone external repos to skills-basin/external/ (desktop)
Following existing external/ pattern:
```
cd ~/vault/skills-basin/external
git clone --depth=1 https://github.com/outcomeeng/python outcomeeng-python
git clone --depth=1 https://github.com/outcomeeng/foundation outcomeeng-foundation
```
Then update skill_registry cloned_path entries.

### 3. Repos NOT yet reviewed (README only)
These were identified but not cloned or evaluated:
- alirezarezvani/claude-skills — 232+ skills, candidates: mcp-builder, rag-architect, agent-designer
- Jeffallan/claude-skills — python-pro, fastapi-pro, postgres-pro candidates
- glebis/claude-skills — TDD subagent pattern candidate

## What was NOT done (correct decision)

### reviewing-prose
Created but marked tier=basin. humaznier (id 53, /mnt/skills/user/humaznier/) is already the
superskill covering AI writing detection and humanizing. reviewing-prose is redundant. 
Decision: leave in basin, do not promote.

### upstream/SOURCES.md vs external/ pattern
The existing system uses external/ cloned repos tracked in skill_registry.
upstream/SOURCES.md is an informational supplement, not a replacement.
Future external repos should be cloned to external/<repo-name>/ and registered in skill_registry.

## Key facts for next session
- skill_registry and all brain tables: use MaeveMCP brain_query (read) / brain_upsert (write)
- Never write to brain via python3/sqlite3 locally in Claude container — hits container copy only
- humaznier is the content humanizer superskill — already promoted to /mnt/skills/user/
- external/ is the canonical location for upstream repos on desktop vault
