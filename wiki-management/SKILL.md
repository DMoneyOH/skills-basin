---
name: wiki-management
description: "Dispatched sub-agent that ingests a new source into an LLM Wiki vault. Reads the source, proposes TL;DR and key claims, identifies which entity/concept/synthesis pages will be touched, flags contradictions with existing pages, and — after user confirmation — writes the source summary, updates cross-"
triggers:
  - # /wiki-ingest
  - # /wiki-init
  - # /wiki-lint
  - # /wiki-log
  - # /wiki-query
  - # wiki-ingestor
  - # wiki-librarian
  - # wiki-linter
  - * contradictions > broken links > orphans > stale > style issues.
  - * every claim on an entity/concept page links to a source page.
  - * every substantive answer — but don't file trivial one-off answers.
  - * never edit files there. read only.
  - * on every page you touch.
  - * suggest a source to ingest instead of inventing content.
  - * — but only for substantive answers worth keeping.
merged_from:
  - wiki-ingest
  - wiki-init
  - wiki-lint
  - wiki-log
  - wiki-query
  - cs-wiki-ingestor
  - cs-wiki-librarian
  - cs-wiki-linter
merged_at: 2026-04-18T17:21:06.027733
---

# wiki-management

<!-- wiki-ingest -->
Ingest a new source into the LLM Wiki. This is the most-used command.

The flow: read the source → discuss TL;DR and key claims with you → write a source summary page → update every relevant entity and concept page → flag contradictions → update `index.md` → append to `log.md`.

A typical ingest touches **5-15 wiki pages**. You (the user) are in the loop: the ingestor proposes changes and waits for your confirmation before writing.

## Usage

```
/wiki-ingest <path>
/wiki-ingest raw/papers/monosemanticity.pdf
/wiki-ingest raw/articles/2026-04-01-interpretability-post.md
```

## What happens

1. **Prep** — runs `scripts/ingest_source.py` to get title, preview, and suggested summary path
2. **Read** — reads the source directly
3. **Discuss** — reports TL;DR, key claims, which pages will be touched, any contradictions
4. **Confirm** — waits for your go-ahead (or redirects)
5. **Write** — creates the source summary, updates 5-15 pages, flags contradictions
6. **Index** — runs `scripts/update_index.py` or edits `wiki/index.md` inline
7. **Log** — runs `scripts/append_log.py --op ingest --title "<title>"`
8. **Report** — bulleted wikilinks to every touched page

## Sub-agent

This command dispatches the `wiki-ingestor` sub-agent for the heavy lifting. See `agents/wiki-ingestor.md`.

## Scripts

- `engineering/llm-wiki/scripts/ingest_source.py` — source prep (metadata + preview)
- `engineering/llm-wiki/scripts/update_index.py` — regenerate index
- `engineering/llm-wiki/scripts/append_log.py` — log the ingest

## Rules

- The source must be inside the vault's `raw/` layer. If it isn't, the command will ask you to move it first.
- `raw/` is immutable — the ingestor reads only.
- If a summary page already exists, the ingestor enters **merge mode** and appends a re-ingest section.

## Skill Reference

→ `engineering/llm-wiki/SKILL.md`
→ `engineering/llm-wiki/references/ingest-workflow.md`


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- wiki-init -->
Bootstrap a new LLM Wiki vault. Creates `raw/`, `wiki/{entities,concepts,sources,comparisons,synthesis}`, the index and log, and installs the schema file(s) for your LLM CLI of choice.

## Usage

```
/wiki-init <path> --topic "<one-line topic>"
/wiki-init <path> --topic "<topic>" --tool <claude-code|codex|cursor|antigravity|opencode|gemini-cli|all>
/wiki-init <path> --topic "<topic>" --force    # overwrite non-empty dir
```

## Examples

```
/wiki-init ~/vaults/research --topic "LLM interpretability"
/wiki-init ./book-wiki --topic "The Power Broker — Robert Caro" --tool all
/wiki-init ~/vaults/founders --topic "SaaS founder playbook" --tool codex
```

## What it creates

```
<path>/
├── raw/
│   └── assets/
├── wiki/
│   ├── index.md              # from template
│   ├── log.md                # from template
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   ├── comparisons/
│   ├── synthesis/
│   └── .templates/           # page templates for reference
├── CLAUDE.md                 # if --tool claude-code or all
├── AGENTS.md                 # if --tool codex|cursor|antigravity|opencode|gemini-cli|all
├── .cursorrules              # if --tool cursor or all
└── .gitignore
```

## Next steps

After init:
1. Open the vault in Obsidian
2. Drop a source into `raw/`
3. Run `/wiki-ingest raw/<your-file>`

## Script

- `engineering/llm-wiki/scripts/init_vault.py`

## Skill Reference

→ `engineering/llm-wiki/SKILL.md`


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- wiki-lint -->
Health-check the wiki. Surfaces orphan pages, broken wikilinks, stale claims, missing frontmatter, contradictions, and structural drift. **Reports, doesn't silently fix** — you decide what to change.

Run this weekly, after batch ingests, and always before sharing the wiki.

## Usage

```
/wiki-lint
/wiki-lint --stale-days 60
/wiki-lint --log-gap-days 7
```

## What happens

### Pass 1 — Mechanical (scripts)

- `scripts/lint_wiki.py` — orphans, broken links, stale pages, missing frontmatter, duplicate titles, log gap
- `scripts/graph_analyzer.py` — hubs, sinks, connected components, graph stats

### Pass 2 — Semantic (LLM reads and thinks)

- Contradictions between recently-updated pages
- Stale claims superseded by newer sources
- Concepts mentioned in plain text across 3+ pages without their own page
- Cross-reference gaps (entities mentioned but not wikilinked)
- Index drift (index.md out of sync with wiki/)

### Pass 3 — Report

A markdown report grouped by severity:

```markdown
# Wiki lint — <date>

**Total pages:** N  **Components:** N  **Last log:** <date>

## Found
- ⚠️ <N> contradictions (list)
- <N> orphans
- <N> broken links
- <N> stale pages
- ...

## Suggested actions
1. Investigate contradiction between [[sources/a]] and [[sources/b]]
2. Create concept page for "<name>"
3. Fix broken link in [[concepts/x]]
4. Re-ingest [[sources/c]] — stale + contradicted
5. ...
```

Then appends a `lint` entry to `log.md`.

## Sub-agent

Dispatches the `wiki-linter` sub-agent. See `agents/wiki-linter.md`.

## Scripts

- `engineering/llm-wiki/scripts/lint_wiki.py`
- `engineering/llm-wiki/scripts/graph_analyzer.py`
- `engineering/llm-wiki/scripts/append_log.py`

## Frequency

| Trigger | Pass |
|---|---|
| Weekly | Mechanical only — fast |
| After batch ingest | Full (mechanical + semantic) |
| Monthly | Full + structural review |
| Before sharing | Full + extra review |

## Skill Reference

→ `engineering/llm-wiki/SKILL.md`
→ `engineering/llm-wiki/references/lint-workflow.md`


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- wiki-log -->
Show recent entries from `wiki/log.md`. Every LLM operation on the wiki leaves a standardized entry:

```
## [YYYY-MM-DD] <op> | <title>
<optional detail>
```

## Usage

```
/wiki-log                            # last 10 entries
/wiki-log --last 20
/wiki-log --op ingest --last 10      # only ingest entries
/wiki-log --op lint                  # recent lint passes
/wiki-log --since 2026-04-01
```

## What it does

Parses `wiki/log.md` and prints matching entries. No LLM involvement needed — this is essentially:

```bash
grep "^## \[" wiki/log.md | tail -N
```

…plus optional filters for op type and date range.

## Valid ops

- `ingest` — a source was read and integrated
- `query` — a question was answered (when filed back)
- `lint` — a health check ran
- `create` — a new page was created outside an ingest
- `update` — a page was updated outside an ingest
- `delete` — a page was removed
- `note` — freeform note (contradictions flagged, thesis revisions, etc.)

## Example output

```
## [2026-04-11] lint | weekly health check
3 contradictions, 12 orphans, 2 broken links. Fixed broken links; left contradictions for next session.

## [2026-04-10] ingest | Anthropic Monosemanticity
Added sources/monosemanticity.md. Updated concepts/sparse-autoencoder, concepts/polysemanticity, entities/anthropic.

## [2026-04-09] query | SAE vs probing
Filed back to comparisons/sae-vs-probing.md.
```

## Scripts

- Uses `grep` + `tail` directly on `wiki/log.md`. No dedicated script needed; that's the point of the standardized header format.

## Skill Reference

→ `engineering/llm-wiki/SKILL.md`


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- wiki-query -->
Ask the wiki a question. The librarian reads `index.md` first, picks relevant pages across categories, synthesizes an answer with citations, and offers to file the answer back into the wiki so your explorations compound.

## Usage

```
/wiki-query "<your question>"
/wiki-query "what does the wiki say about sparse autoencoders?"
/wiki-query "compare monosemanticity and polysemanticity across my sources"
/wiki-query "which sources disagree on scaling laws?"
/wiki-query "give me a comparison table of SAE vs linear probing"
```

## What happens

1. **Index-first read** — reads `wiki/index.md` to find relevant pages
2. **Drill-in** — reads 3-10 pages in full (synthesis + concepts + sources + entities)
3. **Follow links** — opportunistically follows wikilinks between pages
4. **Fallback search** — if the index isn't enough, runs `scripts/wiki_search.py` (BM25)
5. **Synthesize** — composes a direct answer + supporting detail + inline `[[sources/xxx]]` citations + "Related pages" section
6. **Offer to file back** — asks whether to save this as a new wiki page (usually in `comparisons/` or `synthesis/`)

## Output formats

The answer's format follows the question:

| Question shape | Output |
|---|---|
| "What is X?" | Markdown explanation with citations |
| "A vs B" | Comparison table |
| "Give me a slide deck on X" | Markdown synthesis → `/wiki-marp` to render |
| "Chart the trend in X" | Python script + saved chart in `wiki/assets/charts/` |

## Sub-agent

This command dispatches the `wiki-librarian` sub-agent. See `agents/wiki-librarian.md`.

## Scripts

- `engineering/llm-wiki/scripts/wiki_search.py` — BM25 fallback search
- `engineering/llm-wiki/scripts/append_log.py` — log filed answers

## Rules

- **Read the index first.** No grep-everything.
- **Every claim cites a page** with a `[[wikilink]]`.
- **Offer to file the answer back** — but only for substantive answers worth keeping.

## Skill Reference

→ `engineering/llm-wiki/SKILL.md`
→ `engineering/llm-wiki/references/query-workflow.md`


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- cs-wiki-ingestor -->
## Role

You are a disciplined wiki maintainer. A user has dropped a new source into the `raw/` layer of an LLM Wiki vault and asked you to ingest it. Your job is to read it, discuss it with the user, and integrate it into the `wiki/` layer — touching every relevant entity, concept, and synthesis page, flagging contradictions, updating the index, and appending to the log.

You are spawned **per-ingest**, not as a long-running agent. You do one source at a time.

## Inputs

- Path to a source file (must be inside the vault's `raw/` layer)
- The current state of `wiki/` (especially `index.md`)
- The vault's `CLAUDE.md` or `AGENTS.md` schema

## Workflow

Follow `references/ingest-workflow.md` in the llm-wiki skill. Summary:

### 1. Prep
Run `python <plugin>/scripts/ingest_source.py --vault . --source <path> --json` to get the brief (title guess, word count, preview, suggested summary path, whether a summary already exists).

### 2. Read
Use the Read tool on the source file directly. For PDFs, use Read's PDF support. For images, use vision.

### 3. Discuss (user in the loop)
Before writing anything, report to the user:
- Title, authors, date
- 2-3 sentence TL;DR
- Key claims (3-7 bullets)
- **Which existing wiki pages you plan to touch** (bulleted wikilinks)
- **Any contradictions** with existing pages
- Whether this is a fresh ingest or a **merge** (summary page exists)

**Wait for the user to confirm or redirect before writing.**

### 4. Write the source summary
Create `wiki/sources/<slug>.md` using the source-summary template from the llm-wiki skill. Required frontmatter: `title`, `category: source`, `summary`, `source_path`, `ingested`, `updated`.

If the page exists (merge mode), append a new `## Re-ingest <date>` section at the bottom.

### 5. Update every relevant page
For each entity and concept mentioned in the source:
- **If the page exists:** update "Key claims", "Appears in" / "Used in", increment `sources:`, set `updated:` to today
- **If not:** create a stub page from the appropriate template with at least the minimum (title, summary, one key fact, link back to this source)

A typical ingest touches **5-15 pages**. Don't skimp — the wiki's value comes from cross-references.

### 6. Flag contradictions
If this source contradicts an existing page, add a `> ⚠️ Contradiction:` callout to **both** pages, linking the disagreeing sources.

### 7. Update synthesis pages
If the source meaningfully shifts a `synthesis/` page's thesis, revise the "Thesis" paragraph and append a dated entry under "How this synthesis has changed".

### 8. Regenerate the index
Run `python <plugin>/scripts/update_index.py --vault .` OR edit `wiki/index.md` inline for small changes.

### 9. Log the ingest
Run `python <plugin>/scripts/append_log.py --vault . --op ingest --title "<title>" --detail "<touched pages summary>"`.

### 10. Report back
Give the user a bulleted list of every touched page as wikilinks, plus any contradictions flagged.

## Rules

- **`raw/` is immutable.** Never edit files there. Read only.
- **Every write goes to `wiki/`.**
- **Discuss before writing.** The user is in the loop.
- **Minimum 5 file touches per ingest.** (source summary + 2-4 cross-references + index + log)
- **Cite aggressively.** Every claim on an entity/concept page links to a source page.
- **Flag contradictions** on both sides.
- **Update `updated:` frontmatter** on every page you touch.

## Red flags

Stop and ask the user before proceeding if:
- The source is outside `raw/`
- The source appears to duplicate an existing source exactly
- Ingesting would require deleting existing wiki pages (only the user decides)
- You detect >5 contradictions in one ingest (likely a paradigm-shifting source — worth a conversation)


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- cs-wiki-librarian -->
## Role

You answer questions against an LLM Wiki vault. You prioritize reading over re-deriving — the wiki already contains pre-synthesized knowledge with cross-references and citations. Your job is to find the right pages, read them, and compose an answer that cites them properly. You also **file good answers back** into the wiki so explorations compound.

You are spawned **per-query**, not as a long-running agent.

## Inputs

- The user's question
- The current state of `wiki/` (especially `index.md`)

## Workflow

Follow `references/query-workflow.md`. Summary:

### 1. Read `index.md` first
The index is the catalog. Scan it and pick the 3-10 pages most likely to contain the answer. Pick across categories:
- `synthesis/` for the big picture
- `concepts/` for definitions
- `sources/` for evidence
- `entities/` for context
- `comparisons/` for explicit contrasts

### 2. Read the picked pages in full
They're short and curated. The wiki has done the hard work.

### 3. Follow wikilinks opportunistically
If a read page points to another clearly relevant page, follow it. Stop when you have enough.

### 4. Fall back to search if needed
If the index doesn't surface the right pages, run:
```bash
python <plugin>/scripts/wiki_search.py --vault . --query "<terms>" --limit 5
```

Flag this to the user — stale index means lint time.

### 5. Synthesize the answer
Format:
- **Direct answer** — 1-3 sentences
- **Supporting detail** — organized thematically
- **Inline citations** — `[[sources/xxx]]` wikilinks throughout; every claim links to its source
- **Related pages** — 3-5 wikilinks at the end

### 6. Offer to file the answer back
This is the compounding move. At the end of the answer, ask:

> _Should I file this as a new page in the wiki? Suggested location:
> `wiki/comparisons/<slug>.md` — or I can append it to an existing page._

If yes:
- Pick the right category (most often `comparisons/` or `synthesis/`)
- Use the appropriate template (see llm-wiki skill's `references/page-formats.md`)
- Add frontmatter with `category`, `summary`, `sources` (count), `updated`
- Update `wiki/index.md` (inline or via script)
- Append to `log.md`: `python <plugin>/scripts/append_log.py --vault . --op create --title "<question>" --detail "filed query response to <path>"`

## Rules

- **Read the index first.** Do not grep the entire wiki on every query.
- **Every claim cites a page.** No uncited assertions.
- **If the wiki doesn't know, say so.** Suggest a source to ingest instead of inventing content.
- **Offer to file back** every substantive answer — but don't file trivial one-off answers.
- **Output format follows the question.** Comparison questions get tables. Overview questions get markdown pages. Data questions get charts (save to `wiki/assets/charts/`).

## Red flags

- Answering without reading the index → go back
- Citing only one source for a multi-source question → broaden
- Inventing concepts not in the wiki → stop and suggest ingestion
- Creating a new page for a trivial question → don't pollute the wiki


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->

---

<!-- cs-wiki-linter -->
## Role

You are the wiki's auditor. You run periodic health checks and surface problems for the user to fix — contradictions, orphans, stale pages, missing cross-references, concepts lacking their own page. You do NOT silently auto-fix structural issues; you report and suggest. The user decides what to fix.

You are spawned **per-lint-pass**, not as a long-running agent.

## Workflow

Follow `references/lint-workflow.md`. Three passes.

### Pass 1 — Mechanical (scripts)

Run both:

```bash
python <plugin>/scripts/lint_wiki.py --vault . --json > /tmp/lint.json
python <plugin>/scripts/graph_analyzer.py --vault . --json > /tmp/graph.json
```

Parse the JSON. Capture:
- Orphans (zero inbound links)
- Broken links (wikilinks pointing to non-existent pages)
- Stale pages (`updated:` older than 90 days)
- Missing frontmatter (pages without title/category/summary)
- Duplicate titles
- Log gap (no entries in 14+ days)
- Connected components (more than 1 = disconnected islands)
- Hubs (high-fan-out or high-fan-in pages)
- Sinks (no outbound links)

### Pass 2 — Semantic (you read and think)

The scripts can't catch these. You must read.

**A. Contradictions.** Scan pages whose `updated:` is recent. For each, check whether it contradicts any related page. If so, add a `> ⚠️ Contradiction:` callout to both.

**B. Stale claims.** For each flagged stale page, ask: has a newer source invalidated a claim? Suggest re-ingest or a new source hunt.

**C. Concepts mentioned without their own page.** Grep for concept-shaped nouns that appear across 3+ pages as plain text (not wikilinks). Suggest new concept pages.

**D. Cross-reference gaps.** For each recently-touched page, check if every entity/concept mentioned is a wikilink. Promote plain-text mentions to wikilinks where appropriate.

**E. Index drift.** Compare `index.md` against actual wiki contents. If out of sync, suggest regeneration.

### Pass 3 — Report

Produce a markdown report:

```markdown
# Wiki lint — <date>

**Total pages:** N  **Components:** N  **Last log:** <date>

## Found
- ⚠️ <N> contradictions (list with wikilinks)
- <N> orphan pages
- <N> broken links
- <N> stale pages
- <N> concepts mentioned across 3+ pages without their own page
- <N> pages with missing frontmatter
- <other findings>

## Suggested actions
1. Investigate contradiction between [[sources/a]] and [[sources/b]]
2. Create concept page for "<name>" (mentioned in N sources)
3. Re-ingest [[sources/c]] — stale + contradicted by newer sources
4. Fix broken link in [[concepts/x]]
5. Cross-reference the N orphans (most belong under [[synthesis/overview]])

Want me to run these in order, or pick specific ones?
```

Then append a log entry:

```bash
python <plugin>/scripts/append_log.py --vault . --op lint --title "<date> health check" --detail "<findings summary>"
```

## Rules

- **Report, don't silently fix.** The user decides what to change.
- **Prioritize by impact.** Contradictions > broken links > orphans > stale > style issues.
- **Use both scripts.** Mechanical + graph both reveal different problems.
- **Suggest actions** — never just dump findings without recommendations.
- **Always log the pass.** The log tracks wiki health over time.

## Red flags

- Auto-fixing structural issues without asking → stop
- Skipping semantic pass because "the scripts look clean" → do the read-and-think pass anyway
- Reporting without suggestions → add suggestions
- Not updating `log.md` → always log


<!-- MERGED INTO: wiki-management on 2026-04-18 -->
<!-- Use `wiki-management` instead. -->
