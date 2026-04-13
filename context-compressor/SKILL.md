---
name: context-compressor
description: "Wraps file reads to compress content BEFORE it enters context. Use read_and_compress(path) as the primary entrypoint for any file read that will be injected into context. Handles code files (skeleton extraction), markdown/prose (heading/table/bullet preservation, prose dropped), and config files (comment stripping). Three tiers: passthrough <200 tokens, strip 200-1000 tokens, summarize >1000 tokens. Logs all compression events to Brain DB. Use instead of raw file reads for vault docs, skill files, project context, SESSION_STATE, and any large file reads."
metadata:
  version: 2.0.0
  source: maeve-custom
  date_built: "2026-04-12"
  preferred_model: haiku
---

# Context Compressor v2

Intercepts file reads and compresses content before it enters context.
This is the architectural fix: compression wraps the read, not the other way around.

---

## Primary Entrypoint

```python
from compressor import read_and_compress

# Always use this instead of Path(path).read_text()
content = read_and_compress("/path/to/file.md")
```

---

## Compression Tiers

| File Size (tokens) | Action |
|---|---|
| < 200 | Passthrough unchanged |
| 200 to 1,000 | Strip: remove comments, blanks, boilerplate |
| > 1,000 | Summarize: type-aware extraction |

---

## File Type Routing

| Type | Extensions | Summarize Strategy |
|---|---|---|
| Code | .py .js .ts .go .rs .sh | Skeleton: imports, def/class, constants, returns |
| Markdown | .md .mdx .txt .rst | Extract: headings, tables, bullets, code signatures, frontmatter |
| Config | .json .yaml .yml .toml | Strip comments, preserve structure |
| Unknown | anything else | Markdown heuristic fallback |

---

## Output Format

```
[COMPRESSOR: summarize | markdown | ~2,654 → ~1,652 tokens | saved ~1,002]
<compressed content>
```

---

## Modes

- `auto` — applies tier logic (default, always use this)
- `strip` — force strip regardless of size
- `summarize` — force summarize regardless of size
- `full` — bypass compressor, return raw content

---

## Integration Points

- Vault reads: always use read_and_compress
- Skill file reads: always use read_and_compress
- SESSION_STATE.md: use `full` mode (small, must be exact)
- Brain DB large text fields: use summarize mode
- GitHub file reads via MCP: use strip mode

---

## Brain Logging

Every compression event logged to `compression_log` table:
session_date, file_path, mode, file_type, tokens_before, tokens_after, tokens_saved

---

## Verification

```bash
python3 ~/.claude/skills/context-compressor/compressor.py --test
```

Expected: 6/6 PASS
