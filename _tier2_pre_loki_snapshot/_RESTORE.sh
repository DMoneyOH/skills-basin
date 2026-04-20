#!/bin/bash
# TIER 2 Pre-Loki Snapshot Restore
# Created: 2026-04-18T17:13:16.474405
# Usage: bash _RESTORE.sh
SNAPSHOT="/home/derek/vault/skills-basin/_tier2_pre_loki_snapshot"
BASIN="/home/derek/vault/skills-basin"
echo "Restoring TIER 2 snapshot to $BASIN..."
for dir in "$SNAPSHOT"/*/; do
    name=$(basename "$dir")
    [[ "$name" == _* ]] && continue
    dest="$BASIN/$name"
    if [ -d "$dest" ]; then rm -rf "$dest"; fi
    cp -r "$dir" "$dest"
    echo "  restored: $name"
done
echo "Done."
