---
name: cicd-pipeline
description: "You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design automation that reduces manual work, i..."
triggers:
  - # ci/cd pipeline builder
  - # deployment pipeline design
  - # deployment procedures
  - # workflow automation
  - ## 1. platform selection
  - ## 10. best practices
  - ## 2. pre-deployment principles
  - ## 3. deployment workflow principles
  - ## 4. post-deployment verification
  - ## 5. rollback principles
  - ## 6. zero-downtime deployment
  - ## 7. emergency procedures
  - ## 8. anti-patterns
  - ## 9. decision checklist
  - ## ⚠️ how to use this skill
merged_from:
  - ci-cd-pipeline-builder
  - cicd-automation-workflow-automate
  - deployment-pipeline-design
  - deployment-procedures
merged_at: 2026-04-18T17:20:54.580626
---

# cicd-pipeline

<!-- ci-cd-pipeline-builder -->
**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** DevOps / Automation

## Overview

Use this skill to generate pragmatic CI/CD pipelines from detected project stack signals, not guesswork. It focuses on fast baseline generation, repeatable checks, and environment-aware deployment stages.

## Core Capabilities

- Detect language/runtime/tooling from repository files
- Recommend CI stages (`lint`, `test`, `build`, `deploy`)
- Generate GitHub Actions or GitLab CI starter pipelines
- Include caching and matrix strategy based on detected stack
- Emit machine-readable detection output for automation
- Keep pipeline logic aligned with project lockfiles and build commands

## When to Use

- Bootstrapping CI for a new repository
- Replacing brittle copied pipeline files
- Migrating between GitHub Actions and GitLab CI
- Auditing whether pipeline steps match actual stack
- Creating a reproducible baseline before custom hardening

## Key Workflows

### 1. Detect Stack

```bash
python3 scripts/stack_detector.py --repo . --format text
python3 scripts/stack_detector.py --repo . --format json > detected-stack.json
```

Supports input via stdin or `--input` file for offline analysis payloads.

### 2. Generate Pipeline From Detection

```bash
python3 scripts/pipeline_generator.py \
  --input detected-stack.json \
  --platform github \
  --output .github/workflows/ci.yml \
  --format text
```

Or end-to-end from repo directly:

```bash
python3 scripts/pipeline_generator.py --repo . --platform gitlab --output .gitlab-ci.yml
```

### 3. Validate Before Merge

1. Confirm commands exist in project (`test`, `lint`, `build`).
2. Run generated pipeline locally where possible.
3. Ensure required secrets/env vars are documented.
4. Keep deploy jobs gated by protected branches/environments.

### 4. Add Deployment Stages Safely

- Start with CI-only (`lint/test/build`).
- Add staging deploy with explicit environment context.
- Add production deploy with manual gate/approval.
- Keep rollout/rollback commands explicit and auditable.

## Script Interfaces

- `python3 scripts/stack_detector.py --help`
  - Detects stack signals from repository files
  - Reads optional JSON input from stdin/`--input`
- `python3 scripts/pipeline_generator.py --help`
  - Generates GitHub/GitLab YAML from detection payload
  - Writes to stdout or `--output`

## Common Pitfalls

1. Copying a Node pipeline into Python/Go repos
2. Enabling deploy jobs before stable tests
3. Forgetting dependency cache keys
4. Running expensive matrix builds for every trivial branch
5. Missing branch protections around prod deploy jobs
6. Hardcoding secrets in YAML instead of CI secret stores

## Best Practices

1. Detect stack first, then generate pipeline.
2. Keep generated baseline under version control.
3. Add one optimization at a time (cache, matrix, split jobs).
4. Require green CI before deployment jobs.
5. Use protected environments for production credentials.
6. Regenerate pipeline when stack changes significantly.

## References

- [references/github-actions-templates.md](references/github-actions-templates.md)
- [references/gitlab-ci-templates.md](references/gitlab-ci-templates.md)
- [references/deployment-gates.md](references/deployment-gates.md)
- [README.md](README.md)

## Detection Heuristics

The stack detector prioritizes deterministic file signals over heuristics:

- Lockfiles determine package manager preference
- Language manifests determine runtime families
- Script commands (if present) drive lint/test/build commands
- Missing scripts trigger conservative placeholder commands

## Generation Strategy

Start with a minimal, reliable pipeline:

1. Checkout and setup runtime
2. Install dependencies with cache strategy
3. Run lint, test, build in separate steps
4. Publish artifacts only after passing checks

Then layer advanced behavior (matrix builds, security scans, deploy gates).

## Platform Decision Notes

- GitHub Actions for tight GitHub ecosystem integration
- GitLab CI for integrated SCM + CI in self-hosted environments
- Keep one canonical pipeline source per repo to reduce drift

## Validation Checklist

1. Generated YAML parses successfully.
2. All referenced commands exist in the repo.
3. Cache strategy matches package manager.
4. Required secrets are documented, not embedded.
5. Branch/protected-environment rules match org policy.

## Scaling Guidance

- Split long jobs by stage when runtime exceeds 10 minutes.
- Introduce test matrix only when compatibility truly requires it.
- Separate deploy jobs from CI jobs to keep feedback fast.
- Track pipeline duration and flakiness as first-class metrics.


<!-- MERGED INTO: cicd-pipeline on 2026-04-18 -->
<!-- Use `cicd-pipeline` instead. -->

---

<!-- cicd-automation-workflow-automate -->
You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement automation that reduces manual work, improves consistency, and accelerates delivery while maintaining quality and security.

## Use this skill when

- Automating CI/CD workflows or release pipelines
- Designing GitHub Actions or multi-stage build/test/deploy flows
- Replacing manual build, test, or deployment steps
- Improving pipeline reliability, visibility, or compliance checks

## Do not use this skill when

- You only need a one-off command or quick troubleshooting
- There is no workflow or automation context
- The task is strictly product or UI design

## Safety

- Avoid running deployment steps without approvals and rollback plans.
- Treat secrets and environment configuration changes as high risk.

## Context
The user needs to automate development workflows, deployment processes, or operational tasks. Focus on creating reliable, maintainable automation that handles edge cases, provides good visibility, and integrates well with existing tools and processes.

## Requirements
$ARGUMENTS

## Instructions

- Inventory current build, test, and deploy steps plus target environments.
- Define pipeline stages with caching, artifacts, and quality gates.
- Add security scans, secret handling, and approvals for risky steps.
- Document rollout, rollback, and notification strategy.
- If detailed workflow patterns are required, open `resources/implementation-playbook.md`.

## Output Format

- Summary of pipeline stages and triggers
- Proposed workflow files or step list
- Required secrets, env vars, and service integrations
- Risks, assumptions, and rollback notes

## Resources

- `resources/implementation-playbook.md` for detailed workflow patterns and examples.


<!-- MERGED INTO: cicd-pipeline on 2026-04-18 -->
<!-- Use `cicd-pipeline` instead. -->

---

<!-- deployment-pipeline-design -->
Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies.

## Do not use this skill when

- The task is unrelated to deployment pipeline design
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Design robust, secure deployment pipelines that balance speed with safety through proper stage organization and approval workflows.

## Use this skill when

- Design CI/CD architecture
- Implement deployment gates
- Configure multi-environment pipelines
- Establish deployment best practices
- Implement progressive delivery

## Pipeline Stages

### Standard Pipeline Flow

```
┌─────────┐   ┌──────┐   ┌─────────┐   ┌────────┐   ┌──────────┐
│  Build  │ → │ Test │ → │ Staging │ → │ Approve│ → │Production│
└─────────┘   └──────┘   └─────────┘   └────────┘   └──────────┘
```

### Detailed Stage Breakdown

1. **Source** - Code checkout
2. **Build** - Compile, package, containerize
3. **Test** - Unit, integration, security scans
4. **Staging Deploy** - Deploy to staging environment
5. **Integration Tests** - E2E, smoke tests
6. **Approval Gate** - Manual approval required
7. **Production Deploy** - Canary, blue-green, rolling
8. **Verification** - Health checks, monitoring
9. **Rollback** - Automated rollback on failure

## Approval Gate Patterns

### Pattern 1: Manual Approval

```yaml
# GitHub Actions
production-deploy:
  needs: staging-deploy
  environment:
    name: production
    url: https://app.example.com
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to production
      run: |
        # Deployment commands
```

### Pattern 2: Time-Based Approval

```yaml
# GitLab CI
deploy:production:
  stage: deploy
  script:
    - deploy.sh production
  environment:
    name: production
  when: delayed
  start_in: 30 minutes
  only:
    - main
```

### Pattern 3: Multi-Approver

```yaml
# Azure Pipelines
stages:
- stage: Production
  dependsOn: Staging
  jobs:
  - deployment: Deploy
    environment:
      name: production
      resourceType: Kubernetes
    strategy:
      runOnce:
        preDeploy:
          steps:
          - task: ManualValidation@0
            inputs:
              notifyUsers: 'team-leads@example.com'
              instructions: 'Review staging metrics before approving'
```

**Reference:** See `assets/approval-gate-template.yml`

## Deployment Strategies

### 1. Rolling Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2
      maxUnavailable: 1
```

**Characteristics:**
- Gradual rollout
- Zero downtime
- Easy rollback
- Best for most applications

### 2. Blue-Green Deployment

```yaml
# Blue (current)
kubectl apply -f blue-deployment.yaml
kubectl label service my-app version=blue

# Green (new)
kubectl apply -f green-deployment.yaml
# Test green environment
kubectl label service my-app version=green

# Rollback if needed
kubectl label service my-app version=blue
```

**Characteristics:**
- Instant switchover
- Easy rollback
- Doubles infrastructure cost temporarily
- Good for high-risk deployments

### 3. Canary Deployment

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    canary:
      steps:
      - setWeight: 10
      - pause: {duration: 5m}
      - setWeight: 25
      - pause: {duration: 5m}
      - setWeight: 50
      - pause: {duration: 5m}
      - setWeight: 100
```

**Characteristics:**
- Gradual traffic shift
- Risk mitigation
- Real user testing
- Requires service mesh or similar

### 4. Feature Flags

```python
from flagsmith import Flagsmith

flagsmith = Flagsmith(environment_key="API_KEY")

if flagsmith.has_feature("new_checkout_flow"):
    # New code path
    process_checkout_v2()
else:
    # Existing code path
    process_checkout_v1()
```

**Characteristics:**
- Deploy without releasing
- A/B testing
- Instant rollback
- Granular control

## Pipeline Orchestration

### Multi-Stage Pipeline Example

```yaml
name: Production Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build application
        run: make build
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Push to registry
        run: docker push myapp:${{ github.sha }}

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Unit tests
        run: make test
      - name: Security scan
        run: trivy image myapp:${{ github.sha }}

  deploy-staging:
    needs: test
    runs-on: ubuntu-latest
    environment:
      name: staging
    steps:
      - name: Deploy to staging
        run: kubectl apply -f k8s/staging/

  integration-test:
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - name: Run E2E tests
        run: npm run test:e2e

  deploy-production:
    needs: integration-test
    runs-on: ubuntu-latest
    environment:
      name: production
    steps:
      - name: Canary deployment
        run: |
          kubectl apply -f k8s/production/
          kubectl argo rollouts promote my-app

  verify:
    needs: deploy-production
    runs-on: ubuntu-latest
    steps:
      - name: Health check
        run: curl -f https://app.example.com/health
      - name: Notify team
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"Production deployment successful!"}'
```

## Pipeline Best Practices

1. **Fail fast** - Run quick tests first
2. **Parallel execution** - Run independent jobs concurrently
3. **Caching** - Cache dependencies between runs
4. **Artifact management** - Store build artifacts
5. **Environment parity** - Keep environments consistent
6. **Secrets management** - Use secret stores (Vault, etc.)
7. **Deployment windows** - Schedule deployments appropriately
8. **Monitoring integration** - Track deployment metrics
9. **Rollback automation** - Auto-rollback on failures
10. **Documentation** - Document pipeline stages

## Rollback Strategies

### Automated Rollback

```yaml
deploy-and-verify:
  steps:
    - name: Deploy new version
      run: kubectl apply -f k8s/

    - name: Wait for rollout
      run: kubectl rollout status deployment/my-app

    - name: Health check
      id: health
      run: |
        for i in {1..10}; do
          if curl -sf https://app.example.com/health; then
            exit 0
          fi
          sleep 10
        done
        exit 1

    - name: Rollback on failure
      if: failure()
      run: kubectl rollout undo deployment/my-app
```

### Manual Rollback

```bash
# List revision history
kubectl rollout history deployment/my-app

# Rollback to previous version
kubectl rollout undo deployment/my-app

# Rollback to specific revision
kubectl rollout undo deployment/my-app --to-revision=3
```

## Monitoring and Metrics

### Key Pipeline Metrics

- **Deployment Frequency** - How often deployments occur
- **Lead Time** - Time from commit to production
- **Change Failure Rate** - Percentage of failed deployments
- **Mean Time to Recovery (MTTR)** - Time to recover from failure
- **Pipeline Success Rate** - Percentage of successful runs
- **Average Pipeline Duration** - Time to complete pipeline

### Integration with Monitoring

```yaml
- name: Post-deployment verification
  run: |
    # Wait for metrics stabilization
    sleep 60

    # Check error rate
    ERROR_RATE=$(curl -s "$PROMETHEUS_URL/api/v1/query?query=rate(http_errors_total[5m])" | jq '.data.result[0].value[1]')

    if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
      echo "Error rate too high: $ERROR_RATE"
      exit 1
    fi
```

## Reference Files

- `references/pipeline-orchestration.md` - Complex pipeline patterns
- `assets/approval-gate-template.yml` - Approval workflow templates

## Related Skills

- `github-actions-templates` - For GitHub Actions implementation
- `gitlab-ci-patterns` - For GitLab CI implementation
- `secrets-management` - For secrets handling


<!-- MERGED INTO: cicd-pipeline on 2026-04-18 -->
<!-- Use `cicd-pipeline` instead. -->

---

<!-- deployment-procedures -->
> Deployment principles and decision-making for safe production releases.
> **Learn to THINK, not memorize scripts.**

---

## ⚠️ How to Use This Skill

This skill teaches **deployment principles**, not bash scripts to copy.

- Every deployment is unique
- Understand the WHY behind each step
- Adapt procedures to your platform

---

## 1. Platform Selection

### Decision Tree

```
What are you deploying?
│
├── Static site / JAMstack
│   └── Vercel, Netlify, Cloudflare Pages
│
├── Simple web app
│   ├── Managed → Railway, Render, Fly.io
│   └── Control → VPS + PM2/Docker
│
├── Microservices
│   └── Container orchestration
│
└── Serverless
    └── Edge functions, Lambda
```

### Each Platform Has Different Procedures

| Platform | Deployment Method |
|----------|------------------|
| **Vercel/Netlify** | Git push, auto-deploy |
| **Railway/Render** | Git push or CLI |
| **VPS + PM2** | SSH + manual steps |
| **Docker** | Image push + orchestration |
| **Kubernetes** | kubectl apply |

---

## 2. Pre-Deployment Principles

### The 4 Verification Categories

| Category | What to Check |
|----------|--------------|
| **Code Quality** | Tests passing, linting clean, reviewed |
| **Build** | Production build works, no warnings |
| **Environment** | Env vars set, secrets current |
| **Safety** | Backup done, rollback plan ready |

### Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Production build successful
- [ ] Environment variables verified
- [ ] Database migrations ready (if any)
- [ ] Rollback plan documented
- [ ] Team notified
- [ ] Monitoring ready

---

## 3. Deployment Workflow Principles

### The 5-Phase Process

```
1. PREPARE
   └── Verify code, build, env vars

2. BACKUP
   └── Save current state before changing

3. DEPLOY
   └── Execute with monitoring open

4. VERIFY
   └── Health check, logs, key flows

5. CONFIRM or ROLLBACK
   └── All good? Confirm. Issues? Rollback.
```

### Phase Principles

| Phase | Principle |
|-------|-----------|
| **Prepare** | Never deploy untested code |
| **Backup** | Can't rollback without backup |
| **Deploy** | Watch it happen, don't walk away |
| **Verify** | Trust but verify |
| **Confirm** | Have rollback trigger ready |

---

## 4. Post-Deployment Verification

### What to Verify

| Check | Why |
|-------|-----|
| **Health endpoint** | Service is running |
| **Error logs** | No new errors |
| **Key user flows** | Critical features work |
| **Performance** | Response times acceptable |

### Verification Window

- **First 5 minutes**: Active monitoring
- **15 minutes**: Confirm stable
- **1 hour**: Final verification
- **Next day**: Review metrics

---

## 5. Rollback Principles

### When to Rollback

| Symptom | Action |
|---------|--------|
| Service down | Rollback immediately |
| Critical errors | Rollback |
| Performance >50% degraded | Consider rollback |
| Minor issues | Fix forward if quick |

### Rollback Strategy by Platform

| Platform | Rollback Method |
|----------|----------------|
| **Vercel/Netlify** | Redeploy previous commit |
| **Railway/Render** | Rollback in dashboard |
| **VPS + PM2** | Restore backup, restart |
| **Docker** | Previous image tag |
| **K8s** | kubectl rollout undo |

### Rollback Principles

1. **Speed over perfection**: Rollback first, debug later
2. **Don't compound errors**: One rollback, not multiple changes
3. **Communicate**: Tell team what happened
4. **Post-mortem**: Understand why after stable

---

## 6. Zero-Downtime Deployment

### Strategies

| Strategy | How It Works |
|----------|--------------|
| **Rolling** | Replace instances one by one |
| **Blue-Green** | Switch traffic between environments |
| **Canary** | Gradual traffic shift |

### Selection Principles

| Scenario | Strategy |
|----------|----------|
| Standard release | Rolling |
| High-risk change | Blue-green (easy rollback) |
| Need validation | Canary (test with real traffic) |

---

## 7. Emergency Procedures

### Service Down Priority

1. **Assess**: What's the symptom?
2. **Quick fix**: Restart if unclear
3. **Rollback**: If restart doesn't help
4. **Investigate**: After stable

### Investigation Order

| Check | Common Issues |
|-------|--------------|
| **Logs** | Errors, exceptions |
| **Resources** | Disk full, memory |
| **Network** | DNS, firewall |
| **Dependencies** | Database, APIs |

---

## 8. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Deploy on Friday | Deploy early in week |
| Rush deployment | Follow the process |
| Skip staging | Always test first |
| Deploy without backup | Backup before deploy |
| Walk away after deploy | Monitor for 15+ min |
| Multiple changes at once | One change at a time |

---

## 9. Decision Checklist

Before deploying:

- [ ] **Platform-appropriate procedure?**
- [ ] **Backup strategy ready?**
- [ ] **Rollback plan documented?**
- [ ] **Monitoring configured?**
- [ ] **Team notified?**
- [ ] **Time to monitor after?**

---

## 10. Best Practices

1. **Small, frequent deploys** over big releases
2. **Feature flags** for risky changes
3. **Automate** repetitive steps
4. **Document** every deployment
5. **Review** what went wrong after issues
6. **Test rollback** before you need it

---

> **Remember:** Every deployment is a risk. Minimize risk through preparation, not speed.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: cicd-pipeline on 2026-04-18 -->
<!-- Use `cicd-pipeline` instead. -->
