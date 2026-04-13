---
name: maeve-github-devops
description: "Merged GitHub DevOps skill. Use when: creating GitHub Actions workflows, automating PRs/issues/branches, setting up CI/CD pipelines, managing repository permissions, automating code review, handling deployments and rollbacks, triaging issues, or managing branch protection. Combines github-automation (Composio MCP tool sequences, API patterns) + github-workflow-automation (AI-integrated GHA workflows, PR review bots, smart test selection) + github-actions-templates (production-ready workflow YAML for test/build/deploy/security)."
metadata:
  version: 1.0.0
  source: maeve-merge
  merged_from: [github-automation, github-workflow-automation, github-actions-templates]
  date_merged: "2026-04-12"
  preferred_model: sonnet
---

# Maeve GitHub DevOps

Complete GitHub automation: API operations via MCP, AI-integrated workflow patterns, and production-ready Actions templates.

---

## When to Invoke

| Trigger | Action |
|---|---|
| Manage repos/issues/PRs programmatically | Use Composio MCP tool sequences |
| Set up CI/CD pipeline | Use Actions templates section |
| Automate PR review with AI | Use AI workflow patterns section |
| Issue triage automation | Use triage workflow section |
| Deployment + rollback | Use deploy/rollback templates |
| Branch protection, CODEOWNERS | Use permissions section |

---

## MCP Tool Sequences (Composio/Rube)

**Prerequisites:**
- Rube MCP connected at `https://rube.app/mcp`
- GitHub connection active via `RUBE_MANAGE_CONNECTIONS` toolkit `github`
- Always call `RUBE_SEARCH_TOOLS` first for current schemas

### Issue Management
1. `GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER` — find target repo
2. `GITHUB_LIST_REPOSITORY_ISSUES` — list existing (returns PRs too, check `pull_request` field)
3. `GITHUB_CREATE_AN_ISSUE` — create issue (title, body, labels, assignees)
4. `GITHUB_CREATE_AN_ISSUE_COMMENT` — add comment

### Pull Request Workflow
1. `GITHUB_FIND_PULL_REQUESTS` — search/filter PRs
2. `GITHUB_GET_A_PULL_REQUEST` — get mergeable status
3. `GITHUB_LIST_PULL_REQUESTS_FILES` — review changed files
4. `GITHUB_CREATE_A_PULL_REQUEST` — create PR (head, base, title)
5. `GITHUB_LIST_CHECK_RUNS_FOR_A_REF` — verify CI before merge
6. `GITHUB_MERGE_A_PULL_REQUEST` — **always require explicit user confirmation**

### Branch Operations
1. `GITHUB_LIST_BRANCHES` — list branches
2. `GITHUB_CREATE_A_REFERENCE` — create branch from SHA (ref must start with `refs/`)
3. `GITHUB_UPDATE_A_REFERENCE` — update existing reference
4. `GITHUB_GET_BRANCH_PROTECTION` — inspect protection rules (404 = no protection, not an error)

### Code Search
1. `GITHUB_SEARCH_CODE` — search file contents (files <384KB on default branch, max 1000 results)
2. `GITHUB_SEARCH_COMMITS_BY_AUTHOR` — requires keywords + qualifiers
3. `GITHUB_LIST_COMMITS` — repo-specific commit list (409 on empty repos)

### CI/CD + Deployments
1. `GITHUB_LIST_REPOSITORY_WORKFLOWS` — list workflows
2. `GITHUB_CREATE_A_WORKFLOW_DISPATCH_EVENT` — trigger (requires `workflow_dispatch` in workflow)
3. `GITHUB_LIST_DEPLOYMENTS` — list deployments
4. `GITHUB_GET_A_DEPLOYMENT_STATUS` — check status

### Common Pitfalls
- `LIST_REPOSITORY_ISSUES` returns both issues AND PRs — check `pull_request` field
- `CREATE_A_REFERENCE` fails with 422 if reference already exists — use `UPDATE_A_REFERENCE` instead
- Labels/assignees/milestones silently dropped without push access
- Merge can fail: draft status, branch protection, failing checks — always verify `mergeable` first
- All list endpoints paginate: `per_page` max 100, iterate until empty

---

## GitHub Actions Templates

### CI — Test Matrix
```yaml
name: Test
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'
    - run: npm ci
    - run: npm run lint
    - run: npm test
    - uses: codecov/codecov-action@v3
      with:
        files: ./coverage/lcov.info
```

### Build and Push Docker
```yaml
name: Build and Push
on:
  push:
    branches: [main]
    tags: ['v*']
env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
    - uses: actions/checkout@v4
    - uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    - uses: docker/metadata-action@v5
      id: meta
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
    - uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
```

### Deploy to Kubernetes
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
    - run: aws eks update-kubeconfig --name production-cluster --region us-west-2
    - run: |
        kubectl apply -f k8s/
        kubectl rollout status deployment/my-app -n production
```

### Security Scan
```yaml
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        format: 'sarif'
        output: 'trivy-results.sarif'
    - uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'
```

---

## AI-Integrated Workflows

### AI PR Review Bot
```yaml
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - name: Get diff
      id: diff
      run: |
        diff=$(git diff origin/${{ github.base_ref }}...HEAD)
        echo "diff<<EOF" >> $GITHUB_OUTPUT
        echo "$diff" >> $GITHUB_OUTPUT
        echo "EOF" >> $GITHUB_OUTPUT
    - name: AI Review
      uses: actions/github-script@v7
      with:
        script: |
          const { Anthropic } = require('@anthropic-ai/sdk');
          const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
          const response = await client.messages.create({
            model: "claude-sonnet-4-20250514",
            max_tokens: 4096,
            messages: [{ role: "user", content: `Review this PR diff:\n${{ steps.diff.outputs.diff }}\nProvide: summary, potential issues, suggestions, security concerns.` }]
          });
          await github.rest.pulls.createReview({
            owner: context.repo.owner,
            repo: context.repo.repo,
            pull_number: context.issue.number,
            body: response.content[0].text,
            event: 'COMMENT'
          });
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Issue Triage Automation
```yaml
name: Issue Triage
on:
  issues:
    types: [opened]
jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
    - name: Analyze and label
      uses: actions/github-script@v7
      with:
        script: |
          const issue = context.payload.issue;
          // AI classifies: type (bug/feature/question), severity, area
          // Auto-applies labels, requests repro steps if bug without them
```

**Triage prompt template:**
```
Analyze this GitHub issue and classify:
Title: {title} / Body: {body}
Return JSON: { type, severity, area, summary, hasReproSteps, suggestedLabels }
```

### Smart Test Selection
```yaml
- name: Analyze changed paths
  run: |
    changed=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
    if echo "$changed" | grep -q "^src/api/"; then suites="api"; fi
    if echo "$changed" | grep -q "^src/frontend/"; then suites="frontend"; fi
    if echo "$changed" | grep -q "^src/database/"; then suites="database,api"; fi
```

### AI Deployment Risk Assessment
```yaml
- name: AI Risk Assessment
  # Analyzes commit log since last tag
  # Returns riskLevel (low/medium/high), concerns, recommendations
  # Blocks high-risk deploys for manual approval
```

### Automated Rollback
```yaml
- name: Find last stable version
  run: stable=$(git tag -l 'v*' --sort=-version:refname | head -1)
- name: Rollback and notify Slack
  run: |
    git checkout $stable
    npm run deploy
```

---

## Branch Protection Config
```yaml
required_status_checks:
  strict: true
  contexts: ['test', 'lint', 'ai-review']
enforce_admins: true
required_pull_request_reviews:
  required_approving_review_count: 1
  require_code_owner_reviews: true
  dismiss_stale_reviews: true
required_linear_history: true
allow_force_pushes: false
```

## CODEOWNERS Pattern
```
* @org/core-team
/src/frontend/ @org/frontend-team
/src/api/ @org/backend-team
/.github/ @org/devops-team
/src/auth/ @org/security-team
```

## Slash Commands (AI Bot)
| Command | Action |
|---|---|
| `@ai-helper review` | AI code review |
| `@ai-helper explain` | Explain code |
| `@ai-helper fix` | Suggest fixes |
| `/rebase` | Rebase PR onto main |
| `/label bug` | Add label |

---

## Workflow Best Practices

- Use specific action versions (@v4, not @latest)
- Cache dependencies for speed
- Store all secrets in GitHub Secrets, never in workflow files
- Implement approval gates (`environment:`) for production
- Add `timeout-minutes` to all jobs
- Use `path` filters to skip unrelated workflows
- Implement retry logic for flaky external calls
- Stale branch cleanup: weekly cron, create issue not auto-delete

---

## Quick Reference: MCP Tool Map

| Task | Tool |
|---|---|
| List repos | `GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER` |
| Create issue | `GITHUB_CREATE_AN_ISSUE` |
| Find PRs | `GITHUB_FIND_PULL_REQUESTS` |
| Create PR | `GITHUB_CREATE_A_PULL_REQUEST` |
| Merge PR | `GITHUB_MERGE_A_PULL_REQUEST` (user confirmation required) |
| Create branch | `GITHUB_CREATE_A_REFERENCE` |
| Search code | `GITHUB_SEARCH_CODE` |
| Trigger workflow | `GITHUB_CREATE_A_WORKFLOW_DISPATCH_EVENT` |
| Check CI | `GITHUB_LIST_CHECK_RUNS_FOR_A_REF` |
| Branch protection | `GITHUB_GET_BRANCH_PROTECTION` |
