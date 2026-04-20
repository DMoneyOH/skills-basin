---
name: agent-memory
description: "Memory is the cornerstone of intelligent agents. Without it, every interaction starts from zero. This skill covers the architecture of agent memory: short-term (context window), long-term (vector s..."
triggers:
  - # agent memory skill
  - # agent memory systems
  - # conversation memory
  - *clone the repository**:
  - *install dependencies**:
  - *start the mcp server**:
  - - merged into: agent-memory on 2026-04-18 -->
  - ------|----------|----------|
  - --|---|
  - .memory/decisions.md
  - .memory/inbox.md
  - .memory/patterns.md
  - 02-27"
  - agent-memory
  - aware prompting
merged_from:
  - agent-memory-systems
  - agent-memory-mcp
  - conversation-memory
  - hierarchical-agent-memory
merged_at: 2026-04-18T17:20:40.186829
---

# agent-memory

<!-- agent-memory-systems -->
You are a cognitive architect who understands that memory makes agents intelligent.
You've built memory systems for agents handling millions of interactions. You know
that the hard part isn't storing - it's retrieving the right memory at the right time.

Your core insight: Memory failures look like intelligence failures. When an agent
"forgets" or gives inconsistent answers, it's almost always a retrieval problem,
not a storage problem. You obsess over chunking strategies, embedding quality,
and

## Capabilities

- agent-memory
- long-term-memory
- short-term-memory
- working-memory
- episodic-memory
- semantic-memory
- procedural-memory
- memory-retrieval
- memory-formation
- memory-decay

## Patterns

### Memory Type Architecture

Choosing the right memory type for different information

### Vector Store Selection Pattern

Choosing the right vector database for your use case

### Chunking Strategy Pattern

Breaking documents into retrievable chunks

## Anti-Patterns

### ❌ Store Everything Forever

### ❌ Chunk Without Testing Retrieval

### ❌ Single Memory Type for All Data

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Contextual Chunking (Anthropic's approach) |
| Issue | high | ## Test different sizes |
| Issue | high | ## Always filter by metadata first |
| Issue | high | ## Add temporal scoring |
| Issue | medium | ## Detect conflicts on storage |
| Issue | medium | ## Budget tokens for different memory types |
| Issue | medium | ## Track embedding model in metadata |

## Related Skills

Works well with: `autonomous-agents`, `multi-agent-orchestration`, `llm-architect`, `agent-tool-builder`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: agent-memory on 2026-04-18 -->
<!-- Use `agent-memory` instead. -->

---

<!-- agent-memory-mcp -->
This skill provides a persistent, searchable memory bank that automatically syncs with project documentation. It runs as an MCP server to allow reading/writing/searching of long-term memories.

## Prerequisites

- Node.js (v18+)

## Setup

1. **Clone the Repository**:
   Clone the `agentMemory` project into your agent's workspace or a parallel directory:

   ```bash
   git clone https://github.com/webzler/agentMemory.git .agent/skills/agent-memory
   ```

2. **Install Dependencies**:

   ```bash
   cd .agent/skills/agent-memory
   npm install
   npm run compile
   ```

3. **Start the MCP Server**:
   Use the helper script to activate the memory bank for your current project:

   ```bash
   npm run start-server <project_id> <absolute_path_to_target_workspace>
   ```

   _Example for current directory:_

   ```bash
   npm run start-server my-project $(pwd)
   ```

## Capabilities (MCP Tools)

### `memory_search`

Search for memories by query, type, or tags.

- **Args**: `query` (string), `type?` (string), `tags?` (string[])
- **Usage**: "Find all authentication patterns" -> `memory_search({ query: "authentication", type: "pattern" })`

### `memory_write`

Record new knowledge or decisions.

- **Args**: `key` (string), `type` (string), `content` (string), `tags?` (string[])
- **Usage**: "Save this architecture decision" -> `memory_write({ key: "auth-v1", type: "decision", content: "..." })`

### `memory_read`

Retrieve specific memory content by key.

- **Args**: `key` (string)
- **Usage**: "Get the auth design" -> `memory_read({ key: "auth-v1" })`

### `memory_stats`

View analytics on memory usage.

- **Usage**: "Show memory statistics" -> `memory_stats({})`

## Dashboard

This skill includes a standalone dashboard to visualize memory usage.

```bash
npm run start-dashboard <absolute_path_to_target_workspace>
```

Access at: `http://localhost:3333`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: agent-memory on 2026-04-18 -->
<!-- Use `agent-memory` instead. -->

---

<!-- conversation-memory -->
You're a memory systems specialist who has built AI assistants that remember
users across months of interactions. You've implemented systems that know when
to remember, when to forget, and how to surface relevant memories.

You understand that memory is not just storage—it's about retrieval, relevance,
and context. You've seen systems that remember everything (and overwhelm context)
and systems that forget too much (frustrating users).

Your core principles:
1. Memory types differ—short-term, lo

## Capabilities

- short-term-memory
- long-term-memory
- entity-memory
- memory-persistence
- memory-retrieval
- memory-consolidation

## Patterns

### Tiered Memory System

Different memory tiers for different purposes

### Entity Memory

Store and update facts about entities

### Memory-Aware Prompting

Include relevant memories in prompts

## Anti-Patterns

### ❌ Remember Everything

### ❌ No Memory Retrieval

### ❌ Single Memory Store

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Memory store grows unbounded, system slows | high | // Implement memory lifecycle management |
| Retrieved memories not relevant to current query | high | // Intelligent memory retrieval |
| Memories from one user accessible to another | critical | // Strict user isolation in memory |

## Related Skills

Works well with: `context-window-management`, `rag-implementation`, `prompt-caching`, `llm-npc-dialogue`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: agent-memory on 2026-04-18 -->
<!-- Use `agent-memory` instead. -->

---

<!-- hierarchical-agent-memory -->
Scoped memory system that gives AI coding agents a cheat sheet for each directory instead of re-reading your entire project every prompt. Root CLAUDE.md holds global context (~200 tokens), subdirectory CLAUDE.md files hold scoped context (~250 tokens each), and a `.memory/` layer stores decisions, patterns, and an inbox for unconfirmed inferences.

## When to Use This Skill

- Use when you want to reduce input token costs across Claude Code sessions
- Use when your project has 3+ directories and the agent keeps re-reading the same files
- Use when you want directory-scoped context instead of one monolithic CLAUDE.md
- Use when you want a dashboard to visualize token savings, session history, and context health
- Use when setting up a new project and want structured agent memory from day one

## How It Works

### Step 1: Setup ("go ham")

Auto-detects your project platform and maturity, then generates the memory structure:

```
project/
├── CLAUDE.md              # Root context (~200 tokens)
├── .memory/
│   ├── decisions.md       # Architecture Decision Records
│   ├── patterns.md        # Reusable patterns
│   ├── inbox.md           # Inferred items awaiting confirmation
│   └── audit-log.md       # Audit history
└── src/
    ├── api/CLAUDE.md      # Scoped context for api/
    ├── components/CLAUDE.md
    └── lib/CLAUDE.md
```

### Step 2: Context Routing

The root CLAUDE.md includes a routing section that tells the agent exactly which sub-context to load:

```markdown
## Context Routing

→ api: src/api/CLAUDE.md
→ components: src/components/CLAUDE.md
→ lib: src/lib/CLAUDE.md
```

The agent reads root, then immediately loads the relevant subdirectory context — no guessing.

### Step 3: Dashboard ("ham dashboard")

Launches a web dashboard at localhost:7777 that visualizes:
- Token savings (HAM-on vs HAM-off sessions)
- Daily token and cost trends
- Per-directory session breakdown
- Context file health (missing/stale/inherited CLAUDE.md coverage)
- Routing compliance (how often the agent follows the routing map)
- Carbon/energy estimates

## Commands

| Trigger | What it does |
|---|---|
| `go ham` | Set up HAM — auto-detect platform, generate CLAUDE.md files |
| `ham savings` | Show token and cost savings report |
| `ham dashboard` | Launch the interactive web dashboard |
| `ham audit` | Health check on memory files |
| `ham insights` | Generate actionable insights from session data |
| `ham route` | Add/update Context Routing section in root CLAUDE.md |
| `ham carbon` | Show energy and carbon efficiency data |

## Examples

### Example 1: First-time setup

```
User: go ham

Agent: HAM setup complete. Created 8 files.
  - CLAUDE.md (root)
  - .memory/decisions.md
  - .memory/patterns.md
  - .memory/inbox.md
  - src/api/CLAUDE.md
  - src/components/CLAUDE.md
  - src/lib/CLAUDE.md
  - src/utils/CLAUDE.md

Baseline captured in .memory/baseline.json
Run "HAM savings" to see your token and cost savings.
```

### Example 2: Checking savings

```
User: ham savings

Agent:
  Before HAM: ~7,500 tokens/prompt
  After HAM:    ~450 tokens/prompt
  Savings:    7,050 tokens (94%)

  Monthly projection (1,500 prompts):
    Sonnet: ~$31.73 saved
    Opus:   ~$158.63 saved
```

## Best Practices

- Keep root CLAUDE.md under 60 lines / 250 tokens
- Keep subdirectory CLAUDE.md files under 75 lines each
- Run `ham audit` every 2 weeks to catch stale or missing context files
- Use `ham route` after adding new directories to keep routing current
- Review `.memory/inbox.md` periodically — confirm or reject inferred items

## Limitations

- Token estimates use ~4 chars = 1 token approximation, not a real tokenizer
- Baseline savings comparisons are estimates based on typical agent behavior
- Dashboard requires Node.js 18+ and reads session data from `~/.claude/projects/`
- Context routing detection relies on CLAUDE.md read order in session JSONL files
- Does not auto-update subdirectory CLAUDE.md content — you maintain those manually or via `ham audit`
- Carbon estimates use regional grid averages, not real-time energy data

## Related Skills

- `agent-memory-systems` — general agent memory architecture patterns
- `agent-memory-mcp` — MCP-based memory integration


<!-- MERGED INTO: agent-memory on 2026-04-18 -->
<!-- Use `agent-memory` instead. -->
