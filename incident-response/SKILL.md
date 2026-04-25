---
name: incident-response
description: >
  "Use when a security incident has been detected or declared and needs classification, triage, escalation path determination, and forensic evidence collection. Covers SEV1-SEV4 classification, false positive filtering, incident taxonomy, and NIST SP 800-61 lifecycle."
  Covers: incident response, incident commander, incident responder, incident response incident response.
  Use for any task involving incident response, incident commander, incident responder, incident response incident response.
merged_from:
  - incident-commander
  - incident-responder
  - incident-response-incident-response
---
# incident-response
Incident response skill for the full lifecycle from initial triage through forensic collection, severity declaration, and escalation routing. This is NOT threat hunting (see threat-detection) or post-incident compliance mapping (see governance/compliance-mapping) — this is about classifying, triaging, and managing declared security incidents.
## Overview
This skill provides the methodology and tooling for **incident triage and response** — classifying security events into typed incidents, scoring severity, filtering false positives, determining escalation paths, and initiating forensic evidence collection under chain-of-custody controls.
## When to Use / When NOT to Use
Use this skill when a security incident has been detected or declared. Do not use for threat hunting or post-incident compliance mapping.
## Core Workflow or Key Techniques
1. Classify the incident using the `incident_triage.py` tool.
2. Determine the severity level and escalation path.
3. Collect forensic evidence under chain-of-custody controls.
## Quick Reference
* `python3 scripts/incident_triage.py --input event.json --classify --json` to classify an event from a JSON file.
* `python3 scripts/incident_triage.py --input event.json --classify --false-positive-check --json` to classify with false positive filtering enabled.
## Reference Files
| File | Description |
|------|-------------|
| incident-classification.md | Incident classification and taxonomy |
| severity-framework.md | Severity framework and escalation paths |
| forensic-evidence-collection.md | Forensic evidence collection and chain-of-custody controls |
| regulatory-notification-obligations.md | Regulatory notification obligations |
