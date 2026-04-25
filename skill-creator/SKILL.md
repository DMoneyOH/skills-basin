---
name: skill-creator
description: >
  Master skill for creating, writing, improving, auditing, and synthesizing Maeve/Claude skills (SKILL.md files).
  Use when asked to create a new skill, write a skill from scratch, update or improve an existing skill,
  merge multiple skills into a super skill, audit a skill for quality, optimize a skill description for triggering,
  evaluate skill outputs, or build a skill for Azure SDK, workflow automation, security review, or any domain.
  Also use when the user says "turn this into a skill", "capture this workflow", "build a skill for X",
  "improve this skill", "synthesize these skills", or "make a skill that does Y".
  Always use this skill before writing any SKILL.md -- never freehand a skill without consulting this first.
merged_from:
  - skill-writer
  - skill-developer
  - skill-creator-ms
merged_at: 2026-04-25
---

# skill-creator

Master reference for creating, improving, merging, and evaluating Maeve skills.

---

## Operation Types

Identify which operation applies before starting:

| Operation | When | Entry Point |
|---|---|---|
| `create` | New skill from scratch | Capture Intent section |
| `update` | Improve existing skill | Improving a Skill section |
| `synthesize` | Merge multiple skills into one super skill | Synthesis Workflow section |
| `iterate` | Refine based on eval outcomes | Iteration Loop section |
| `optimize` | Description trigger tuning only | Description Optimization section |
| `audit` | Quality review of existing skill | Audit Checklist section |

---

## Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      — Executable, deterministic operations
    ├── references/   — Docs loaded into context as needed
    └── assets/       — Templates, icons, fonts used in output
```

### Three-Level Loading (Progressive Disclosure)

1. **Metadata** (name + description) — Always in context, ~100 words max
2. **SKILL.md body** — Loaded when skill triggers, target under 500 lines
3. **Bundled resources** — Loaded on demand, unlimited size

If SKILL.md approaches 500 lines: extract detail into references/ files and add a reference table.

### Skill Classification

Classify before authoring -- determines structure and depth requirements:

| Class | Description | Example |
|---|---|---|
| `workflow-process` | Multi-step procedural skill | skill-creator, pentest-core |
| `integration-documentation` | SDK/API usage patterns | azure-cosmos, n8n-expert |
| `security-review` | Audit, threat, scan workflows | skill-sentinel, web-vuln-testing |
| `skill-authoring` | Skills that create/modify skills | this skill |
| `generic` | Domain expertise, best practices | prompt-engineering, react-expert |

---

## Capture Intent

Start here for create operations. If the conversation already contains a workflow the user wants captured, extract from history first -- tools used, sequence, corrections, input/output formats.

Four questions to resolve before writing:

1. What should this skill enable Claude to do?
2. When should it trigger? (phrases, contexts, file types)
3. What is the expected output format?
4. Are test cases needed? (yes for deterministic outputs; optional for subjective)

---

## Writing the SKILL.md

### Frontmatter

```yaml
---
name: skill-name
description: >
  What it does and when to use it.
  Include specific trigger phrases. Be pushy -- Claude undertriggers.
  "Use whenever user mentions X, Y, Z or asks to do A, B, C."
---
```

The description is the only thing Claude reads before deciding to load the skill. Make it complete and specific.

### Body Structure by Class

**workflow-process:**
Overview / When to Use / When NOT to Use / Core Workflow (numbered) / Edge Cases / Reference Files table

**integration-documentation:**
Installation / Environment Variables / Authentication / Core Workflow / Feature Reference tables / Best Practices / Reference Files

**generic / domain:**
Core Principles / Techniques per subtopic (one H2 per subtopic) / Anti-Patterns / Quick Reference

### Writing Rules

- Imperative voice throughout ("Run X", not "You should run X")
- Anti-patterns are as valuable as patterns; include both
- Reference files get a table: `| When | File |`
- Large reference files (>100 lines) need a table of contents

### Degrees of Freedom

| Degree | Use When | Format |
|---|---|---|
| Exact | Must be precise | Literal code/commands |
| Pattern | Correct structure, variable content | Pseudocode with placeholders |
| Principle | Flexible approach | Numbered/bulleted guidance |

---

## Synthesis Workflow

For merging multiple skills into a super skill.

### Step 1: Inventory constituents
Read each SKILL.md. Note unique techniques, structural patterns, anti-patterns, reference files.

### Step 2: Gap analysis
Compare against canonical. Identify what is missing, what is better explained, what is duplicate (do not carry forward).

### Step 3: Synthesize
Write a new unified SKILL.md:
- One coherent document, not a concatenation
- Preserve canonical name and frontmatter structure
- Description must enumerate ALL absorbed subtopics for Brain discoverability
- skill_library topics field populated with all constituent keywords
- Best explanation wins regardless of source

### Step 4: Archive constituents
- Move absorbed folders to _merged_archive/
- Set skill_library status = 'archived' for absorbed skills
- Update canonical skill_library row: description, topics, last_indexed

---

## Azure SDK Skills

### Section Order
Installation / Environment Variables / Authentication / Core Workflow / Feature Tables / Best Practices / Reference Files

### Authentication (All Languages)

Always DefaultAzureCredential. Never hardcode credentials.

```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
client = ServiceClient(endpoint, credential)
```

### Standard Azure Verb Semantics

| Verb | Behavior |
|---|---|
| create | Create new; fail if exists |
| upsert | Create or update |
| get | Retrieve; error if missing |
| list | Return collection |
| delete | Succeed even if missing |
| begin_* | Start long-running operation |

Each language gets its own references/lang.md. SKILL.md loads only the relevant one.

---

## Improving a Skill

1. Preserve the original name -- directory name and frontmatter name field unchanged
2. Copy to writable location first if installed path is read-only
3. Identify what is failing, missing, or overconstrained
4. Apply targeted edits -- do not rewrite sections that work
5. Re-run test cases after changes

---

## Iteration Loop

1. Capture positive examples (worked), negative (failed), fix examples (corrected)
2. Identify the pattern delta between working and failing
3. Propose targeted description or body edits based on evidence
4. Re-evaluate after each iteration; stop when outcomes are stable

---

## Description Optimization

### Eval query sets
- Should trigger: 8-12 substantive queries where skill should load
- Should NOT trigger: 5-8 queries where it should not

Queries must be substantive -- simple one-step queries will not trigger skills regardless of description.

### Optimization principles
- Lead with capability, then trigger contexts
- Include domain vocabulary users actually type
- 150-300 words for complex skills; shorter for focused ones

### In Claude Code / Cowork
```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <current-model-id> \
  --max-iterations 5
```

### In Claude.ai
Run test cases manually. Present results inline. Iterate on description based on feedback.

---

## Audit Checklist

**Structure**
- [ ] Frontmatter has name and description
- [ ] Description includes trigger phrases, not just capability
- [ ] Body under 500 lines (or references used for overflow)
- [ ] Reference files table present if references exist

**Content**
- [ ] Imperative voice throughout
- [ ] Anti-patterns documented alongside patterns
- [ ] Examples are concrete and runnable

**Brain / Registry**
- [ ] skill_library row has accurate description
- [ ] skill_library.topics populated with searchable keywords
- [ ] For super skills: all absorbed subtopic terms in topics field

**Critical Issues** (must fix)
- Description missing or too vague to trigger
- Instructions reference files/paths that do not exist
- Hardcoded credentials or environment-specific paths

**Major Issues** (fix before shipping)
- No examples for complex workflows
- Missing anti-patterns for error-prone domains

---

## Output Format

After any operation, return:

1. **Summary** -- what was done
2. **Changes Made** -- specific additions, removals, restructuring
3. **Validation Results** -- test outcomes or manual check
4. **Open Gaps** -- anything deferred

---

## Claude.ai Notes

- No subagents: run test cases sequentially
- No browser: present results inline
- No run_loop.py: optimize descriptions manually
- Always read existing SKILL.md before editing
