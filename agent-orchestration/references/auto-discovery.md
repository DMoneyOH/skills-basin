# Auto-Discovery (Varredura)
## Overview
The auto-discovery process scans the ecosystem for available skills and updates the registry.
## How It Works
1. The `scan_registry.py` script is executed.
2. The script scans the ecosystem for SKILL.md files in the following locations:
 * `.claude/skills/*/` (skills registered in Claude Code)
 * `*/` (standalone skills in the top-level)
 * `*/*` (skills in subfolders, up to a depth of 3)
3. The script updates the registry with the discovered skills.