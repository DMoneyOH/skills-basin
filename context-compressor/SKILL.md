---
name: context-compressor
description: "Compresses file content before context injection. Strips boilerplate on medium files, summarizes large files. Annotates savings. Prevents runaway token burn on vault/Brain reads."
risk: low
source: maeve-custom
date_added: "2026-04-12"
preferred_model: haiku
---

# Context Compressor

## Purpose

Intercept file reads before they enter context. Reduce token consumption without losing meaning. Annotate what was done so nothing is silently dropped.

---

## Compression Tiers

| File Size (tokens) | Action | Output |
|---|---|---|
| Under 500 | Pass through unchanged | Raw content |
| 500 to 2,000 | Strip mode: remove comments, blank lines, boilerplate headers | Stripped content + annotation |
| Over 2,000 | Summarize mode: structured summary of key content | Summary + `[COMPRESSED]` annotation |

---

## Usage

### Direct invocation
```
compress_file(path, mode="auto")
```

Modes:
- `auto` — applies tier logic based on token estimate
- `strip` — force strip regardless of size
- `summarize` — force summarize regardless of size
- `full` — bypass compressor, return raw content

### In a skill or session
Before reading any file into context, route through compressor:
```python
from context_compressor import compress_file
content = compress_file("/home/derek/vault/Projects/SomeProject/large_file.py")
```

---

## Output Format

Every compressed result includes a header annotation:

```
[COMPRESSOR: strip | original ~1,240 tokens → ~380 tokens | saved ~860 tokens]
<content here>
```

For summarize mode:
```
[COMPRESSOR: summarize | original ~4,800 tokens → ~420 tokens | saved ~4,380 tokens]
## Summary
<structured summary here>
## Key Identifiers
<functions, classes, config keys found>
## Omitted
<what was removed and why>
```

---

## Rules

1. Never silently drop content. Always annotate what was compressed and why.
2. Summarize mode preserves: function signatures, class names, config keys, error messages, return values.
3. Summarize mode drops: docstrings over 3 lines, inline comments, example blocks, license headers.
4. Pass-through mode (`full`) is available when raw content is genuinely needed.
5. Log every compression to Brain DB `compression_log` table (session, path, tokens_saved).

---

## Integration Points

- Vault reads: apply before injecting any file over 500 tokens
- Brain DB queries returning large text fields: apply summarize
- GitHub file reads via MCP: apply strip mode
- SESSION_STATE.md: always pass-through (small, structured, must be exact)

---

## Verification

After install, run:
```bash
python3 ~/.claude/skills/context-compressor/compressor.py --test
```

Expected output:
```
[TEST] Small file (< 500 tokens): PASS - passed through
[TEST] Medium file (500-2000 tokens): PASS - stripped
[TEST] Large file (> 2000 tokens): PASS - summarized
[TEST] Brain log write: PASS
All tests passed.
```
