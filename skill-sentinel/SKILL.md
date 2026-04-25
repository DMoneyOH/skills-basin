---
name: skill-sentinel
description: >
  "Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payloads across Windows, macOS, Linux/Unix, and Mobile (Android/iOS)."
  Covers: skill sentinel, skill scanner, skills review, audit skills.
  Use for any task involving skill sentinel, skill scanner, skills review, audit skills.
merged_from:
  - skill-scanner
  - skills-review
  - audit-skills
merged_at: 2026-04-25
---

# skill-sentinel

## Overview

Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de saude.

## When to Use This Skill

- When the user mentions "auditar skills" or related topics
- When the user mentions "qualidade skills" or related topics
- When the user mentions "verificar skills ecossistema" or related topics
- When the user mentions "saude ecossistema skills" or related topics
- When the user mentions "skills duplicadas" or related topics
- When the user mentions "otimizar skills" or related topics

## Do Not Use This Skill When

- The task is unrelated to skill sentinel
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Meta-agente que monitora, audita e evolui o ecossistema de skills. Analisa
todas as skills em 7 dimensoes, identifica problemas, sugere melhorias
e recomenda novas skills especialistas.

## Resumo Rapido

| Area | Script | O que faz |
|------|--------|-----------|
| **Discovery** | `scanner.py` | Descobre todas as skills automaticamente |
| **Qualidade** | `analyzers/code_quality.py` | Complexidade, docstrings, error handling |
| **Seguranca** | `analyzers/security.py` | Secrets, SQL injection, HTTPS |
| **Performance** | `analyzers/performance.py` | API calls, caching, retry |
| **Governanca** | `analyzers/governance_audit.py` | Rate limits, audit log, confirmacoes |
| **Documentacao** | `analyzers/documentation.py` | SKILL.md, triggers, references |
| **Dependencias** | `analyzers/dependencies.py` | requirements.txt, versoes |
| **Cross-Skill** | `analyzers/cross_skill.py` | Duplicacao, padroes compartilhados |
| **Custos** | `cost_optimizer.py` | Tokens, verbosidade, output |
| **Recomendacoes** | `recommender.py` | Gap analysis, novas skills |
| **Relatorio** | `report_generator.py` | Markdown estruturado |
| **Orquestracao** | `run_audit.py` | CLI principal |

## Localizacao

```
C:\Users\renat\skills\skill-sentinel\
├── SKILL.md
├── scripts/
│   ├── requirements.txt
│   ├── config.py
│   ├── db.py
│   ├── governance.py
│   ├── scanner.py
│   ├── analyzers/
│   │   ├── code_quality.py
│   │   ├── security.py
│   │   ├── performance.py
│   │   ├── governance_audit.py
│   │   ├── documentation.py
│   │   ├── dependencies.py
│   │   └── cross_skill.py
│   ├── recommender.py
│   ├── cost_optimizer.py
│   ├── report_generator.py
│   └── run_audit.py
├── references/
│   ├── analysis_criteria.md
│   ├── security_patterns.md
│   ├── skill_template.md
│   └── schema.md
└── data/
    ├── sentinel.db
    └── reports/
```

## Instalacao

```bash
pip install -r C:\Users\renat\skills\skill-sentinel\scripts\requirements.txt
```

## Comandos Principais

```bash

## Auditoria Completa De Todas As Skills

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py

## Auditar Apenas Uma Skill

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py --skill instagram

## Apenas Recomendacoes De Novas Skills

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py --recommend

## Comparar Com Auditoria Anterior (Tendencias)

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py --compare

## Output Em Json (Para Processamento)

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py --format json

## Ver Historico De Auditorias

python C:\Users\renat\skills\skill-sentinel\scripts\run_audit.py --history

## Descobrir Skills Disponiveis

python C:\Users\renat\skills\skill-sentinel\scripts\scanner.py

## Ver Audit Log Do Sentinel

python C:\Users\renat\skills\skill-sentinel\scripts\governance.py

## Verificar Banco De Dados

python C:\Users\renat\skills\skill-sentinel\scripts\db.py
```

## 1. Qualidade De Codigo (Peso: 20%)

- Complexidade ciclomatica por funcao (limiar: 10)
- Tamanho de funcoes (limiar: 50 linhas)
- Tamanho de arquivos (limiar: 500 linhas)
- Cobertura de docstrings
- Padroes de error handling (bare except, broad except)

## 2. Seguranca (Peso: 20%)

- Secrets hardcoded (tokens, passwords, API keys)
- SQL injection (f-strings em queries)
- URLs HTTP inseguras
- Tokens em logs
- Validacao de input

## 3. Performance (Peso: 15%)

- Retry com backoff para APIs
- Timeouts configurados
- Reuso de conexoes HTTP
- N+1 queries
- Async/concorrencia

## 4. Governanca (Peso: 15%)

- Nivel 0: Nenhuma
- Nivel 1: Action logging
- Nivel 2: Logging + rate limiting
- Nivel 3: Completa (+ confirmacoes 2-step)
- Nivel 4: Avancada (+ alertas e trends)

## 5. Documentacao (Peso: 15%)

- SKILL.md com frontmatter (name, description, version)
- Trigger keywords (PT-BR e EN)
- Secoes obrigatorias e recomendadas
- Reference files

## 6. Dependencias (Peso: 15%)

- requirements.txt presente
- Versoes pinadas
- Deps importadas vs listadas
- Deps listadas vs importadas

## 7. Cross-Skill (Analise Global)

- Modulos duplicados entre skills
- Padroes de Database compartilhados
- Governanca inconsistente
- Oportunidades de extracao

## Otimizacao De Custos

Alem das 7 dimensoes, o sentinel analisa impacto de custo:
- Tamanho do SKILL.md (tokens consumidos por ativacao)
- References grandes sem indice
- Output verboso dos scripts
- Ausencia de output JSON estruturado

## Gap Analysis E Recomendacoes

O recommender identifica capacidades ausentes no ecossistema comparando
com uma taxonomia de 20 categorias e gera templates de SKILL.md prontos
para novas skills sugeridas.

## Governanca Do Sentinel

O proprio sentinel pratica o que prega:
- Todas as auditorias sao registradas em action_log
- Historico de scores em score_history para tendencias
- Relatorios salvos em data/reports/

## Workflows Comuns

**1. Primeira auditoria do ecossistema:**
```
python run_audit.py
```
Gera relatorio completo com scores, findings e recomendacoes.

**2. Monitorar evolucao ao longo do tempo:**
```
python run_audit.py --compare
```
Mostra delta de scores entre auditorias.

**3. Validar uma skill antes de deploy:**
```
python run_audit.py --skill nome-da-skill
```
Auditoria focada com findings especificos.

**4. Identificar proxima skill a criar:**
```
python run_audit.py --recommend
```
Gap analysis com templates prontos.

## Formato Do Relatorio

O relatorio gerado em `data/reports/` contem:
1. Resumo executivo (tabela de scores)
2. Tendencias (se houver auditoria anterior)
3. Findings por severidade (critico/alto/medio/baixo/info)
4. Analise por skill (detalhada)
5. Recomendacoes de novas skills
6. Plano de acao priorizado

## Referencias

Para detalhes tecnicos, consultar:
- `references/analysis_criteria.md` - Rubricas de scoring
- `references/security_patterns.md` - Padroes de seguranca
- `references/skill_template.md` - Template para novas skills
- `references/schema.md` - Schema do banco de dados

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `skill-installer` - Complementary skill for enhanced analysis

---

<!-- skill-scanner -->
Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks.

**Important**: Run all scripts from the repository root using the full path via `${CLAUDE_SKILL_ROOT}`.

## Bundled Script

### `scripts/scan_skill.py`

Static analysis scanner that detects deterministic patterns. Outputs structured JSON.

```bash
uv run ${CLAUDE_SKILL_ROOT}/scripts/scan_skill.py <skill-directory>
```

Returns JSON with findings, URLs, structure info, and severity counts. The script catches patterns mechanically — your job is to evaluate intent and filter false positives.

## Workflow

### Phase 1: Input & Discovery

Determine the scan target:

- If the user provides a skill directory path, use it directly
- If the user names a skill, look for it under `plugins/*/skills/<name>/` or `.claude/skills/<name>/`
- If the user says "scan all skills", discover all `*/SKILL.md` files and scan each

Validate the target contains a `SKILL.md` file. List the skill structure:

```bash
ls -la <skill-directory>/
ls <skill-directory>/references/ 2>/dev/null
ls <skill-directory>/scripts/ 2>/dev/null
```

### Phase 2: Automated Static Scan

Run the bundled scanner:

```bash
uv run ${CLAUDE_SKILL_ROOT}/scripts/scan_skill.py <skill-directory>
```

Parse the JSON output. The script produces findings with severity levels, URL analysis, and structure information. Use these as leads for deeper analysis.

**Fallback**: If the script fails, proceed with manual analysis using Grep patterns from the reference files.

### Phase 3: Frontmatter Validation

Read the SKILL.md and check:

- **Required fields**: `name` and `description` must be present
- **Name consistency**: `name` field should match the directory name
- **Tool assessment**: Review `allowed-tools` — is Bash justified? Are tools unrestricted (`*`)?
- **Model override**: Is a specific model forced? Why?
- **Description quality**: Does the description accurately represent what the skill does?

### Phase 4: Prompt Injection Analysis

Load `${CLAUDE_SKILL_ROOT}/references/prompt-injection-patterns.md` for context.

Review scanner findings in the "Prompt Injection" category. For each finding:

1. Read the surrounding context in the file
2. Determine if the pattern is **performing** injection (malicious) or **discussing/detecting** injection (legitimate)
3. Skills about security, testing, or education commonly reference injection patterns — this is expected

**Critical distinction**: A security review skill that lists injection patterns in its references is documenting threats, not attacking. Only flag patterns that would execute against the agent running the skill.

### Phase 5: Behavioral Analysis

This phase is agent-only — no pattern matching. Read the full SKILL.md instructions and evaluate:

**Description vs. instructions alignment**:
- Does the description match what the instructions actually tell the agent to do?
- A skill described as "code formatter" that instructs the agent to read ~/.ssh is misaligned

**Config/memory poisoning**:
- Instructions to modify `CLAUDE.md`, `MEMORY.md`, `settings.json`, `.mcp.json`, or hook configurations
- Instructions to add itself to allowlists or auto-approve permissions
- Writing to `~/.claude/` or any agent configuration directory

**Scope creep**:
- Instructions that exceed the skill's stated purpose
- Unnecessary data gathering (reading files unrelated to the skill's function)
- Instructions to install other skills, plugins, or dependencies not mentioned in the description

**Information gathering**:
- Reading environment variables beyond what's needed
- Listing directory contents outside the skill's scope
- Accessing git history, credentials, or user data unnecessarily

### Phase 6: Script Analysis

If the skill has a `scripts/` directory:

1. Load `${CLAUDE_SKILL_ROOT}/references/dangerous-code-patterns.md` for context
2. Read each script file fully (do not skip any)
3. Check scanner findings in the "Malicious Code" category
4. For each finding, evaluate:
   - **Data exfiltration**: Does the script send data to external URLs? What data?
   - **Reverse shells**: Socket connections with redirected I/O
   - **Credential theft**: Reading SSH keys, .env files, tokens from environment
   - **Dangerous execution**: eval/exec with dynamic input, shell=True with interpolation
   - **Config modification**: Writing to agent settings, shell configs, git hooks
5. Check PEP 723 `dependencies` — are they legitimate, well-known packages?
6. Verify the script's behavior matches the SKILL.md description of what it does

**Legitimate patterns**: `gh` CLI calls, `git` commands, reading project files, JSON output to stdout are normal for skill scripts.

### Phase 7: Supply Chain Assessment

Review URLs from the scanner output and any additional URLs found in scripts:

- **Trusted domains**: GitHub, PyPI, official docs — normal
- **Untrusted domains**: Unknown domains, personal sites, URL shorteners — flag for review
- **Remote instruction loading**: Any URL that fetches content to be executed or interpreted as instructions is high risk
- **Dependency downloads**: Scripts that download and execute binaries or code at runtime
- **Unverifiable sources**: References to packages or tools not on standard registries

### Phase 8: Permission Analysis

Load `${CLAUDE_SKILL_ROOT}/references/permission-analysis.md` for the tool risk matrix.

Evaluate:

- **Least privilege**: Are all granted tools actually used in the skill instructions?
- **Tool justification**: Does the skill body reference operations that require each tool?
- **Risk level**: Rate the overall permission profile using the tier system from the reference

Example assessments:
- `Read Grep Glob` — Low risk, read-only analysis skill
- `Read Grep Glob Bash` — Medium risk, needs Bash justification (e.g., running bundled scripts)
- `Read Grep Glob Bash Write Edit WebFetch Task` — High risk, near-full access

## Confidence Levels

| Level | Criteria | Action |
|-------|----------|--------|
| **HIGH** | Pattern confirmed + malicious intent evident | Report with severity |
| **MEDIUM** | Suspicious pattern, intent unclear | Note as "Needs verification" |
| **LOW** | Theoretical, best practice only | Do not report |

**False positive awareness is critical.** The biggest risk is flagging legitimate security skills as malicious because they reference attack patterns. Always evaluate intent before reporting.

## Output Format

```markdown
## Skill Security Scan: [Skill Name]

### Summary
- **Findings**: X (Y Critical, Z High, ...)
- **Risk Level**: Critical / High / Medium / Low / Clean
- **Skill Structure**: SKILL.md only / +references / +scripts / full

### Findings

#### [SKILL-SEC-001] [Finding Type] (Severity)
- **Location**: `SKILL.md:42` or `scripts/tool.py:15`
- **Confidence**: High
- **Category**: Prompt Injection / Malicious Code / Excessive Permissions / Secret Exposure / Supply Chain / Validation
- **Issue**: [What was found]
- **Evidence**: [code snippet]
- **Risk**: [What could happen]
- **Remediation**: [How to fix]

### Needs Verification
[Medium-confidence items needing human review]

### Assessment
[Safe to install / Install with caution / Do not install]
[Brief justification for the assessment]
```

**Risk level determination**:
- **Critical**: Any high-confidence critical finding (prompt injection, credential theft, data exfiltration)
- **High**: High-confidence high-severity findings or multiple medium findings
- **Medium**: Medium-confidence findings or minor permission concerns
- **Low**: Only best-practice suggestions
- **Clean**: No findings after thorough analysis

## Reference Files

| File | Purpose |
|------|---------|
| `references/prompt-injection-patterns.md` | Injection patterns, jailbreaks, obfuscation techniques, false positive guide |
| `references/dangerous-code-patterns.md` | Script security patterns: exfiltration, shells, credential theft, eval/exec |
| `references/permission-analysis.md` | Tool risk tiers, least privilege methodology, common skill permission profiles |


<!-- MERGED INTO: skill-sentinel on 2026-04-18 -->
<!-- Use `skill-sentinel` instead. -->

---

<!-- skills-review -->
Systematically review Playwright test files for anti-patterns, missed best practices, and coverage gaps.

## Input

`$ARGUMENTS` can be:
- A file path: review that specific test file
- A directory: review all test files in the directory
- Empty: review all tests in the project's `testDir`

## Steps

### 1. Gather Context

- Read `playwright.config.ts` for project settings
- List all `*.spec.ts` / `*.spec.js` files in scope
- If reviewing a single file, also check related page objects and fixtures

### 2. Check Each File Against Anti-Patterns

Load `anti-patterns.md` from this skill directory. Check for all 20 anti-patterns.

**Critical (must fix):**
1. `waitForTimeout()` usage
2. Non-web-first assertions (`expect(await ...)`)
3. Hardcoded URLs instead of `baseURL`
4. CSS/XPath selectors when role-based exists
5. Missing `await` on Playwright calls
6. Shared mutable state between tests
7. Test execution order dependencies

**Warning (should fix):**
8. Tests longer than 50 lines (consider splitting)
9. Magic strings without named constants
10. Missing error/edge case tests
11. `page.evaluate()` for things locators can do
12. Nested `test.describe()` more than 2 levels deep
13. Generic test names ("should work", "test 1")

**Info (consider):**
14. No page objects for pages with 5+ locators
15. Inline test data instead of factory/fixture
16. Missing accessibility assertions
17. No visual regression tests for UI-heavy pages
18. Console error assertions not checked
19. Network idle waits instead of specific assertions
20. Missing `test.describe()` grouping

### 3. Score Each File

Rate 1-10 based on:
- **9-10**: Production-ready, follows all golden rules
- **7-8**: Good, minor improvements possible
- **5-6**: Functional but has anti-patterns
- **3-4**: Significant issues, likely flaky
- **1-2**: Needs rewrite

### 4. Generate Review Report

For each file:
```
## <filename> — Score: X/10

### Critical
- Line 15: `waitForTimeout(2000)` → use `expect(locator).toBeVisible()`
- Line 28: CSS selector `.btn-submit` → `getByRole('button', { name: "submit" })`

### Warning
- Line 42: Test name "test login" → "should redirect to dashboard after login"

### Suggestions
- Consider adding error case: what happens with invalid credentials?
```

### 5. For Project-Wide Review

If reviewing an entire test suite:
- Spawn sub-agents per file for parallel review (up to 5 concurrent)
- Or use `/batch` for very large suites
- Aggregate results into a summary table

### 6. Offer Fixes

For each critical issue, provide the corrected code. Ask user: "Apply these fixes? [Yes/No]"

If yes, apply all fixes using `Edit` tool.

## Output

- File-by-file review with scores
- Summary: total files, average score, critical issue count
- Actionable fix list
- Coverage gaps identified (pages/features with no tests)


<!-- MERGED INTO: skill-sentinel on 2026-04-18 -->
<!-- Use `skill-sentinel` instead. -->

---

<!-- audit-skills -->
## Overview

Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payloads across Windows, macOS, Linux/Unix, and Mobile (Android/iOS).
2-4 sentences is perfect.

## When to Use This Skill

- Use when you need to audit AI skills and bundles for security vulnerabilities
- Use when working with cross-platform security analysis
- Use when the user asks about verifying skill legitimacy or performing security reviews
- Use when scanning for mobile threats in AI skills

## How It Works

### Step 1: Static Analysis

Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payloads.

### Step 2: Platform-Specific Threat Detection

Analyzes code for platform-specific security issues across Windows, macOS, Linux/Unix, and Mobile (Android/iOS).

#### 1. Privilege, Ownership & Metadata Manipulation
- **Elevated Access**: `sudo`, `chown`, `chmod`, `TakeOwnership`, `icacls`, `Set-ExecutionPolicy`.
- **Metadata Tampering**: `touch -t`, `setfile` (macOS), `attrib` (Windows), `Set-ItemProperty`, `chflags`.
- **Risk**: Unauthorized access, masking activity, or making files immutable.

#### 2. File/Folder Locking & Resource Denial
- **Patterns**: `chmod 000`, `chattr +i` (immutable), `attrib +r +s +h`, `Deny` ACEs in `icacls`.
- **Global Actions**: Locking or hiding folders in `%USERPROFILE%`, `/Users/`, or `/etc/`.
- **Risk**: Denial of service or data locking.

#### 3. Script Execution & Batch Invocation
- **Legacy/Batch Windows**: `.bat`, `.cmd`, `cmd.exe /c`, `vbs`, `cscript`, `wscript`.
- **Unix Shell**: `.sh`, `.bash`, `.zsh`, `chmod +x` followed by execution.
- **PowerShell**: `.ps1`, `powershell -ExecutionPolicy Bypass -File ...`.
- **Hidden Flags**: `-WindowStyle Hidden`, `-w hidden`, `-noprofile`.

#### 4. Dangerous Install/Uninstall & System Changes
- **Windows**: `msiexec /qn`, `choco uninstall`, `reg delete`.
- **Linux/Unix**: `apt-get purge`, `yum remove`, `rm -rf /usr/bin/...`.
- **macOS**: `brew uninstall`, deleting from `/Applications`.
- **Risk**: Removing security software or creating unmonitored installation paths.

#### 5. Mobile Application & OS Security (Android/iOS)
- **Android Tools**: `adb shell`, `pm install`, `am start`, `apktool`, `dex2jar`, `keytool`.
- **Android Files**: Manipulation of `AndroidManifest.xml` (permissions), `classes.dex`, or `strings.xml`.
- **iOS Tools**: `xcodebuild`, `codesign`, `security find-identity`, `fastlane`, `xcrun`.
- **iOS Files**: Manipulation of `Info.plist`, `Entitlements.plist`, or `Provisioning Profiles`.
- **Mobile Patterns**: Jailbreak/Root detection bypasses, hardcoded API keys in mobile source, or sensitive permission requests (Camera, GPS, Contacts) in non-mobile skills.
- **Risk**: Malicious mobile package injection, credential theft from mobile builds, or device manipulation via ADB.

#### 6. Information Disclosure & Network Exfiltration
- **Patterns**: `curl`, `wget`, `Invoke-WebRequest`, `Invoke-RestMethod`, `scp`, `ftp`, `nc`, `socat`.
- **Sensible Data**: `.env`, `.ssh`, `cookies.sqlite`, `Keychains` (macOS), `Credentials` (Windows), `keystore` (Android).
- **Intranet**: Scanning internal IPs or mapping local services.

#### 7. Service, Process & Stability Manipulation
- **Windows**: `Stop-Service`, `taskkill /f`, `sc.exe delete`.
- **Unix/Mac**: `kill -9`, `pkill`, `systemctl disable/stop`, `launchctl unload`.
- **Low-level**: Direct disk access (`dd`), firmware/BIOS calls, kernel module management.

#### 8. Obfuscation & Persistence
- **Encoding**: `Base64`, `Hex`, `XOR` loops, `atob()`.
- **Persistence**: `reg add` (Run keys), `schtasks`, `crontab`, `launchctl` (macOS), `systemd` units.
- **Tubes**: `curl ... | bash`, `iwr ... | iex`.

#### 9. Legitimacy & Scope (Universal)
- **Registry Alignment**: Cross-reference with `CATALOG.md`.
- **Structural Integrity**: Does it follow the standard repo layout?
- **Healthy Scope**: Does a "UI Design" skill need `adb shell` or `sudo`?

### Step 3: Reporting

Generates a security report with a score (0-10), platform target identification, flagged actions, threat analysis, and mitigation recommendations.

## Examples

### Example 1: Security Review

```markdown
"Perform a security audit on this skill bundle"
```

### Example 2: Cross-Platform Threat Analysis

```markdown
"Scan for mobile threats in this AI skill"
```

## Best Practices

- ✅ Perform non-intrusive analysis
- ✅ Check for privilege escalation patterns
- ✅ Look for information disclosure vulnerabilities
- ✅ Analyze cross-platform threats
- ❌ Don't execute potentially malicious code during audit
- ❌ Don't modify the code being audited
- ❌ Don't ignore mobile-specific security concerns

## Common Pitfalls

- **Problem:** Executing code during audit
  **Solution:** Stick to static analysis methods only

- **Problem:** Missing cross-platform threats
  **Solution:** Check for platform-specific security issues on all supported platforms

- **Problem:** Failing to detect obfuscated payloads
 **Solution:** Look for encoding patterns like Base64, Hex, XOR loops, and atob()

## Related Skills

- `@security-scanner` - Additional security scanning capabilities


<!-- MERGED INTO: skill-sentinel on 2026-04-18 -->
<!-- Use `skill-sentinel` instead. -->

---

<!-- skill-tester -->
---

**Name**: skill-tester
**Tier**: POWERFUL
**Category**: Engineering Quality Assurance
**Dependencies**: None (Python Standard Library Only)
**Author**: Claude Skills Engineering Team
**Version**: 1.0.0
**Last Updated**: 2026-02-16

---

## Description

The Skill Tester is a comprehensive meta-skill designed to validate, test, and score the quality of skills within the claude-skills ecosystem. This powerful quality assurance tool ensures that all skills meet the rigorous standards required for BASIC, STANDARD, and POWERFUL tier classifications through automated validation, testing, and scoring mechanisms.

As the gatekeeping system for skill quality, this meta-skill provides three core capabilities:
1. **Structure Validation** - Ensures skills conform to required directory structures, file formats, and documentation standards
2. **Script Testing** - Validates Python scripts for syntax, imports, functionality, and output format compliance  
3. **Quality Scoring** - Provides comprehensive quality assessment across multiple dimensions with letter grades and improvement recommendations

This skill is essential for maintaining ecosystem consistency, enabling automated CI/CD integration, and supporting both manual and automated quality assurance workflows. It serves as the foundation for pre-commit hooks, pull request validation, and continuous integration processes that maintain the high-quality standards of the claude-skills repository.

## Core Features

### Comprehensive Skill Validation
- **Structure Compliance**: Validates directory structure, required files (SKILL.md, README.md, scripts/, references/, assets/, expected_outputs/)
- **Documentation Standards**: Checks SKILL.md frontmatter, section completeness, minimum line counts per tier
- **File Format Validation**: Ensures proper Markdown formatting, YAML frontmatter syntax, and file naming conventions

### Advanced Script Testing
- **Syntax Validation**: Compiles Python scripts to detect syntax errors before execution
- **Import Analysis**: Enforces standard library only policy, identifies external dependencies
- **Runtime Testing**: Executes scripts with sample data, validates argparse implementation, tests --help functionality
- **Output Format Compliance**: Verifies dual output support (JSON + human-readable), proper error handling

### Multi-Dimensional Quality Scoring
- **Documentation Quality (25%)**: SKILL.md depth and completeness, README clarity, reference documentation quality
- **Code Quality (25%)**: Script complexity, error handling robustness, output format consistency, maintainability
- **Completeness (25%)**: Required directory presence, sample data adequacy, expected output verification
- **Usability (25%)**: Example clarity, argparse help text quality, installation simplicity, user experience

### Tier Classification System
Automatically classifies skills based on complexity and functionality:

#### BASIC Tier Requirements
- Minimum 100 lines in SKILL.md
- At least 1 Python script (100-300 LOC)
- Basic argparse implementation
- Simple input/output handling
- Essential documentation coverage

#### STANDARD Tier Requirements  
- Minimum 200 lines in SKILL.md
- 1-2 Python scripts (300-500 LOC each)
- Advanced argparse with subcommands
- JSON + text output formats
- Comprehensive examples and references
- Error handling and edge case management

#### POWERFUL Tier Requirements
- Minimum 300 lines in SKILL.md
- 2-3 Python scripts (500-800 LOC each)
- Complex argparse with multiple modes
- Sophisticated output formatting and validation
- Extensive documentation and reference materials
- Advanced error handling and recovery mechanisms
- CI/CD integration capabilities

## Architecture & Design

### Modular Design Philosophy
The skill-tester follows a modular architecture where each component serves a specific validation purpose:

- **skill_validator.py**: Core structural and documentation validation engine
- **script_tester.py**: Runtime testing and execution validation framework  
- **quality_scorer.py**: Multi-dimensional quality assessment and scoring system

### Standards Enforcement
All validation is performed against well-defined standards documented in the references/ directory:
- **Skill Structure Specification**: Defines mandatory and optional components
- **Tier Requirements Matrix**: Detailed requirements for each skill tier
- **Quality Scoring Rubric**: Comprehensive scoring methodology and weightings

### Integration Capabilities
Designed for seamless integration into existing development workflows:
- **Pre-commit Hooks**: Prevents substandard skills from being committed
- **CI/CD Pipelines**: Automated quality gates in pull request workflows
- **Manual Validation**: Interactive command-line tools for development-time validation
- **Batch Processing**: Bulk validation and scoring of existing skill repositories

## Implementation Details

### skill_validator.py Core Functions
```python
# Primary validation workflow
validate_skill_structure() -> ValidationReport
check_skill_md_compliance() -> DocumentationReport  
validate_python_scripts() -> ScriptReport
generate_compliance_score() -> float
```

Key validation checks include:
- SKILL.md frontmatter parsing and validation
- Required section presence (Description, Features, Usage, etc.)
- Minimum line count enforcement per tier
- Python script argparse implementation verification
- Standard library import enforcement
- Directory structure compliance
- README.md quality assessment

### script_tester.py Testing Framework
```python
# Core testing functions
syntax_validation() -> SyntaxReport
import_validation() -> ImportReport
runtime_testing() -> RuntimeReport
output_format_validation() -> OutputReport
```

Testing capabilities encompass:
- Python AST-based syntax validation
- Import statement analysis and external dependency detection
- Controlled script execution with timeout protection
- Argparse --help functionality verification
- Sample data processing and output validation
- Expected output comparison and difference reporting

### quality_scorer.py Scoring System
```python
# Multi-dimensional scoring
score_documentation() -> float  # 25% weight
score_code_quality() -> float   # 25% weight
score_completeness() -> float   # 25% weight
score_usability() -> float      # 25% weight
calculate_overall_grade() -> str # A-F grade
```

Scoring dimensions include:
- **Documentation**: Completeness, clarity, examples, reference quality
- **Code Quality**: Complexity, maintainability, error handling, output consistency
- **Completeness**: Required files, sample data, expected outputs, test coverage  
- **Usability**: Help text quality, example clarity, installation simplicity

## Usage Scenarios

### Development Workflow Integration
```bash
# Pre-commit hook validation
skill_validator.py path/to/skill --tier POWERFUL --json

# Comprehensive skill testing
script_tester.py path/to/skill --timeout 30 --sample-data

# Quality assessment and scoring
quality_scorer.py path/to/skill --detailed --recommendations
```

### CI/CD Pipeline Integration
```yaml
# GitHub Actions workflow example
- name: "validate-skill-quality"
  run: |
    python skill_validator.py engineering/${{ matrix.skill }} --json | tee validation.json
    python script_tester.py engineering/${{ matrix.skill }} | tee testing.json
    python quality_scorer.py engineering/${{ matrix.skill }} --json | tee scoring.json
```

### Batch Repository Analysis
```bash
# Validate all skills in repository
find engineering/ -type d -maxdepth 1 | xargs -I {} skill_validator.py {}

# Generate repository quality report
quality_scorer.py engineering/ --batch --output-format json > repo_quality.json
```

## Output Formats & Reporting

### Dual Output Support
All tools provide both human-readable and machine-parseable output:

#### Human-Readable Format
```
=== SKILL VALIDATION REPORT ===
Skill: engineering/example-skill
Tier: STANDARD
Overall Score: 85/100 (B)

Structure Validation: ✓ PASS
├─ SKILL.md: ✓ EXISTS (247 lines)
├─ README.md: ✓ EXISTS  
├─ scripts/: ✓ EXISTS (2 files)
└─ references/: ⚠ MISSING (recommended)

Documentation Quality: 22/25 (88%)
Code Quality: 20/25 (80%)
Completeness: 18/25 (72%)
Usability: 21/25 (84%)

Recommendations:
• Add references/ directory with documentation
• Improve error handling in main.py
• Include more comprehensive examples
```

#### JSON Format
```json
{
  "skill_path": "engineering/example-skill",
  "timestamp": "2026-02-16T16:41:00Z",
  "validation_results": {
    "structure_compliance": {
      "score": 0.95,
      "checks": {
        "skill_md_exists": true,
        "readme_exists": true,
        "scripts_directory": true,
        "references_directory": false
      }
    },
    "overall_score": 85,
    "letter_grade": "B",
    "tier_recommendation": "STANDARD",
    "improvement_suggestions": [
      "Add references/ directory",
      "Improve error handling",
      "Include comprehensive examples"
    ]
  }
}
```

## Quality Assurance Standards

### Code Quality Requirements
- **Standard Library Only**: No external dependencies (pip packages)
- **Error Handling**: Comprehensive exception handling with meaningful error messages
- **Output Consistency**: Standardized JSON schema and human-readable formatting
- **Performance**: Efficient validation algorithms with reasonable execution time
- **Maintainability**: Clear code structure, comprehensive docstrings, type hints where appropriate

### Testing Standards  
- **Self-Testing**: The skill-tester validates itself (meta-validation)
- **Sample Data Coverage**: Comprehensive test cases covering edge cases and error conditions
- **Expected Output Verification**: All sample runs produce verifiable, reproducible outputs
- **Timeout Protection**: Safe execution of potentially problematic scripts with timeout limits

### Documentation Standards
- **Comprehensive Coverage**: All functions, classes, and modules documented
- **Usage Examples**: Clear, practical examples for all use cases
- **Integration Guides**: Step-by-step CI/CD and workflow integration instructions
- **Reference Materials**: Complete specification documents for standards and requirements

## Integration Examples

### Pre-Commit Hook Setup
```bash
#!/bin/bash
# .git/hooks/pre-commit
echo "Running skill validation..."
python engineering/skill-tester/scripts/skill_validator.py engineering/new-skill --tier STANDARD
if [ $? -ne 0 ]; then
    echo "Skill validation failed. Commit blocked."
    exit 1
fi
echo "Validation passed. Proceeding with commit."
```

### GitHub Actions Workflow
```yaml
name: "skill-quality-gate"
on:
  pull_request:
    paths: ['engineering/**']

jobs:
  validate-skills:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: "setup-python"
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: "validate-changed-skills"
        run: |
          changed_skills=$(git diff --name-only ${{ github.event.before }} | grep -E '^engineering/[^/]+/' | cut -d'/' -f1-2 | sort -u)
          for skill in $changed_skills; do
            echo "Validating $skill..."
            python engineering/skill-tester/scripts/skill_validator.py $skill --json
            python engineering/skill-tester/scripts/script_tester.py $skill
            python engineering/skill-tester/scripts/quality_scorer.py $skill --minimum-score 75
          done
```

### Continuous Quality Monitoring
```bash
#!/bin/bash
# Daily quality report generation
echo "Generating daily skill quality report..."
timestamp=$(date +"%Y-%m-%d")
python engineering/skill-tester/scripts/quality_scorer.py engineering/ \
  --batch --json > "reports/quality_report_${timestamp}.json"

echo "Quality trends analysis..."
python engineering/skill-tester/scripts/trend_analyzer.py reports/ \
  --days 30 > "reports/quality_trends_${timestamp}.md"
```

## Performance & Scalability

### Execution Performance
- **Fast Validation**: Structure validation completes in <1 second per skill
- **Efficient Testing**: Script testing with timeout protection (configurable, default 30s)
- **Batch Processing**: Optimized for repository-wide analysis with parallel processing support
- **Memory Efficiency**: Minimal memory footprint for large-scale repository analysis

### Scalability Considerations
- **Repository Size**: Designed to handle repositories with 100+ skills
- **Concurrent Execution**: Thread-safe implementation supports parallel validation
- **Resource Management**: Automatic cleanup of temporary files and subprocess resources
- **Configuration Flexibility**: Configurable timeouts, memory limits, and validation strictness

## Security & Safety

### Safe Execution Environment
- **Sandboxed Testing**: Scripts execute in controlled environment with timeout protection
- **Resource Limits**: Memory and CPU usage monitoring to prevent resource exhaustion
- **Input Validation**: All inputs sanitized and validated before processing
- **No Network Access**: Offline operation ensures no external dependencies or network calls

### Security Best Practices
- **No Code Injection**: Static analysis only, no dynamic code generation
- **Path Traversal Protection**: Secure file system access with path validation
- **Minimal Privileges**: Operates with minimal required file system permissions
- **Audit Logging**: Comprehensive logging for security monitoring and troubleshooting

## Troubleshooting & Support

### Common Issues & Solutions

#### Validation Failures
- **Missing Files**: Check directory structure against tier requirements
- **Import Errors**: Ensure only standard library imports are used
- **Documentation Issues**: Verify SKILL.md frontmatter and section completeness

#### Script Testing Problems  
- **Timeout Errors**: Increase timeout limit or optimize script performance
- **Execution Failures**: Check script syntax and import statement validity
- **Output Format Issues**: Ensure proper JSON formatting and dual output support

#### Quality Scoring Discrepancies
- **Low Scores**: Review scoring rubric and improvement recommendations
- **Tier Misclassification**: Verify skill complexity against tier requirements
- **Inconsistent Results**: Check for recent changes in quality standards or scoring weights

### Debugging Support
- **Verbose Mode**: Detailed logging and execution tracing available
- **Dry Run Mode**: Validation without execution for debugging purposes
- **Debug Output**: Comprehensive error reporting with file locations and suggestions

## Future Enhancements

### Planned Features
- **Machine Learning Quality Prediction**: AI-powered quality assessment using historical data
- **Performance Benchmarking**: Execution time and resource usage tracking across skills
- **Dependency Analysis**: Automated detection and validation of skill interdependencies
- **Quality Trend Analysis**: Historical quality tracking and regression detection

### Integration Roadmap
- **IDE Plugins**: Real-time validation in popular development environments
- **Web Dashboard**: Centralized quality monitoring and reporting interface
- **API Endpoints**: RESTful API for external integration and automation
- **Notification Systems**: Automated alerts for quality degradation or validation failures

## Conclusion

The Skill Tester represents a critical infrastructure component for maintaining the high-quality standards of the claude-skills ecosystem. By providing comprehensive validation, testing, and scoring capabilities, it ensures that all skills meet or exceed the rigorous requirements for their respective tiers.

This meta-skill not only serves as a quality gate but also as a development tool that guides skill authors toward best practices and helps maintain consistency across the entire repository. Through its integration capabilities and comprehensive reporting, it enables both manual and automated quality assurance workflows that scale with the growing claude-skills ecosystem.

The combination of structural validation, runtime testing, and multi-dimensional quality scoring provides unparalleled visibility into skill quality while maintaining the flexibility needed for diverse skill types and complexity levels. As the claude-skills repository continues to grow, the Skill Tester will remain the cornerstone of quality assurance and ecosystem integrity.

<!-- MERGED INTO: skill-sentinel on 2026-04-18 -->
<!-- Use `skill-sentinel` instead. -->
