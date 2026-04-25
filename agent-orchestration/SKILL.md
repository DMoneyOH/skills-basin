---
name: agent-orchestration
description: >
  "This skill should be used when the user asks to 'design multi-agent system', 'implement supervisor pattern', 'create swarm architecture', 'coordinate multiple agents', or mentions multi-agent patterns, context isolation, agent handoffs, sub-agents, or parallel agent execution."
  Covers: agent orchestration, agent orchestrator, agent orchestration improve agent, agent orchestration multi agent optimize, multi agent patterns, dispatching parallel agents, parallel agents.
  Use for any task involving agent orchestration, agent orchestrator, agent orchestration improve agent, agent orchestration multi agent optimize, multi agent patterns.
merged_from:
  - agent-orchestrator
  - agent-orchestration-improve-agent
  - agent-orchestration-multi-agent-optimize
  - multi-agent-patterns
  - dispatching-parallel-agents
  - parallel-agents
---
# agent-orchestration
## Overview
The agent-orchestration skill is a meta-skill that orchestrates all agents in the ecosystem. It performs automatic scanning of skills, matching by capabilities, coordination of multi-skill workflows, and registry management.
## When to Use / When NOT to Use
Use this skill when you need specialized assistance with agent orchestration. Do not use this skill when the task is unrelated to agent orchestration or when a simpler tool can handle the request.
## Core Workflow
1. Auto-Discovery (Varredura): `python agent-orchestrator/scripts/scan_registry.py`
2. Match De Skills: `python agent-orchestrator/scripts/match_skills.py <solicitacao do usuario>`
3. Orquestracao (Se Matched >= 2): `python agent-orchestrator/scripts/orchestrate.py --skills skill1,skill2 --query <solicitacao>`
## Quick Reference
* `python agent-orchestrator/scripts/scan_registry.py && python agent-orchestrator/scripts/match_skills.py <solicitacao>` (Passo Rapido)
* `agent-orchestrator/data/registry.json` (Skill Registry)
## Reference Files
| File | Description |
| --- | --- |
| [auto-discovery.md](auto-discovery.md) | Auto-Discovery (Varredura) details |
| [skill-matching.md](skill-matching.md) | Skill Matching details |
| [orchestration.md](orchestration.md) | Orquestracao (Se Matched >= 2) details |
| [registry-management.md](registry-management.md) | Registry Management details |
