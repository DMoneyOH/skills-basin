---
name: threat-modeling
description: "Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use for security architecture r..."
triggers:
  - # attack tree construction
  - # stride analysis patterns
  - # threat mitigation mapping
  - # threat modeling expert
  - - merged into: threat-modeling on 2026-04-18 -->
  - 02-27"
  - analyzing existing system architecture
  - annotate leaves with cost, skill, time, and detectability.
  - apply relevant best practices and validate outcomes.
  - attack tree construction
  - avoid including sensitive exploit details unless required.
  - avoid storing sensitive details in threat models without access controls.
  - by-design systems.
  - clarify goals, constraints, and required inputs.
  - communicating risks to stakeholders
merged_from:
  - threat-modeling-expert
  - stride-analysis-patterns
  - attack-tree-construction
  - threat-mitigation-mapping
merged_at: 2026-04-18T17:20:40.231376
---

# threat-modeling

<!-- threat-modeling-expert -->
Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTIVELY for security architecture reviews, threat identification, or building secure-by-design systems.

## Capabilities

- STRIDE threat analysis
- Attack tree construction
- Data flow diagram analysis
- Security requirement extraction
- Risk prioritization and scoring
- Mitigation strategy design
- Security control mapping

## Use this skill when

- Designing new systems or features
- Reviewing architecture for security gaps
- Preparing for security audits
- Identifying attack vectors
- Prioritizing security investments
- Creating security documentation
- Training teams on security thinking

## Do not use this skill when

- You lack scope or authorization for security review
- You need legal or compliance certification
- You only need automated scanning without human review

## Instructions

1. Define system scope and trust boundaries
2. Create data flow diagrams
3. Identify assets and entry points
4. Apply STRIDE to each component
5. Build attack trees for critical paths
6. Score and prioritize threats
7. Design mitigations
8. Document residual risks

## Safety

- Avoid storing sensitive details in threat models without access controls.
- Keep threat models updated after architecture changes.

## Best Practices

- Involve developers in threat modeling sessions
- Focus on data flows, not just components
- Consider insider threats
- Update threat models with architecture changes
- Link threats to security requirements
- Track mitigations to implementation
- Review regularly, not just at design time


<!-- MERGED INTO: threat-modeling on 2026-04-18 -->
<!-- Use `threat-modeling` instead. -->

---

<!-- stride-analysis-patterns -->
Systematic threat identification using the STRIDE methodology.

## Use this skill when

- Starting new threat modeling sessions
- Analyzing existing system architecture
- Reviewing security design decisions
- Creating threat documentation
- Training teams on threat identification
- Compliance and audit preparation

## Do not use this skill when

- The task is unrelated to stride analysis patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: threat-modeling on 2026-04-18 -->
<!-- Use `threat-modeling` instead. -->

---

<!-- attack-tree-construction -->
Systematic attack path visualization and analysis.

## Use this skill when

- Visualizing complex attack scenarios
- Identifying defense gaps and priorities
- Communicating risks to stakeholders
- Planning defensive investments or test scopes

## Do not use this skill when

- You lack authorization or a defined scope to model the system
- The task is a general risk review without attack-path modeling
- The request is unrelated to security assessment or design

## Instructions

- Confirm scope, assets, and the attacker goal for the root node.
- Decompose into sub-goals with AND/OR structure.
- Annotate leaves with cost, skill, time, and detectability.
- Map mitigations per branch and prioritize high-impact paths.
- If detailed templates are required, open `resources/implementation-playbook.md`.

## Safety

- Share attack trees only with authorized stakeholders.
- Avoid including sensitive exploit details unless required.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, templates, and examples.


<!-- MERGED INTO: threat-modeling on 2026-04-18 -->
<!-- Use `threat-modeling` instead. -->

---

<!-- threat-mitigation-mapping -->
Connect threats to controls for effective security planning.

## Use this skill when

- Prioritizing security investments
- Creating remediation roadmaps
- Validating control coverage
- Designing defense-in-depth
- Security architecture review
- Risk treatment planning

## Do not use this skill when

- The task is unrelated to threat mitigation mapping
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: threat-modeling on 2026-04-18 -->
<!-- Use `threat-modeling` instead. -->
