#!/usr/bin/env python3
"""
graphify_runner.py v2 -- Skills graph analysis for skills-basin.
Fallback chain: Gemma (local) -> llm_client (Gemini/OpenRouter/Groq) -> name-based

Usage:
  python3 graphify_runner.py            # full run
  python3 graphify_runner.py --dry-run  # Stage 1 only, no API calls
  python3 graphify_runner.py --graph-only  # skip tagging, build graph from existing topics
"""

import sqlite3, json, re, time, sys, requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# llm_client for cloud fallback
sys.path.insert(0, '/home/derek/vault/utils/core-skills')

DB_PATH      = '/home/derek/vault/maeve_brain.db'
BASIN        = Path('/home/derek/vault/skills-basin')
REPORT_PATH  = BASIN / 'GRAPH_REPORT.md'
VOCAB_PATH   = BASIN / 'graphify_vocab.json'
PROGRESS_KEY = 'graphify_batch_progress'
OLLAMA_URL   = 'http://localhost:11434/api/generate'
OLLAMA_MODEL = 'gemma3:4b'
BATCH_SIZE   = 25
LOG_PATH     = '/tmp/graphify.log'

DRY_RUN    = '--dry-run' in sys.argv
GRAPH_ONLY = '--graph-only' in sys.argv

VOCAB = {
    "cloud": ["azure", "aws", "gcp", "cloud", "terraform", "serverless", "hybrid-cloud", "multi-cloud"],
    "devops": ["devops", "ci-cd", "docker", "kubernetes", "helm", "deployment", "gitops", "pipeline"],
    "security": ["security", "pentest", "vulnerability", "compliance", "audit", "sast", "threat-modeling", "red-team"],
    "data": ["data", "sql", "database", "analytics", "etl", "dbt", "spark", "airflow", "postgresql", "nosql"],
    "ai-agents": ["agent", "llm", "prompt", "rag", "langchain", "langgraph", "crewai", "memory", "orchestration"],
    "frontend": ["react", "nextjs", "angular", "tailwind", "ui", "css", "shadcn", "svelte", "vue"],
    "backend": ["api", "fastapi", "django", "nodejs", "graphql", "grpc", "microservices", "rest"],
    "mobile": ["ios", "android", "flutter", "react-native", "swiftui", "kotlin", "expo"],
    "testing": ["testing", "tdd", "playwright", "e2e", "unit-test", "qa", "evaluation"],
    "python": ["python", "fastapi", "django", "pandas", "numpy", "scikit", "asyncio"],
    "typescript": ["typescript", "javascript", "nodejs", "bun", "deno"],
    "rust": ["rust", "cargo", "bevy", "robius", "makepad", "wasm"],
    "dotnet": ["dotnet", "csharp", "asp-net", "blazor", "avalonia"],
    "java": ["java", "spring", "kotlin", "gradle", "maven"],
    "golang": ["golang", "go-lang", "grpc", "temporal"],
    "trading": ["trading", "stocks", "market", "canslim", "vcp", "dividend", "backtesting", "quant"],
    "marketing": ["marketing", "seo", "content", "email", "social", "cro", "growth"],
    "product": ["product", "prd", "roadmap", "okr", "sprint", "agile", "user-story"],
    "architecture": ["architecture", "ddd", "cqrs", "event-sourcing", "saga", "monorepo", "microservices"],
    "monitoring": ["monitoring", "observability", "logging", "tracing", "datadog", "sentry", "pagerduty"],
    "automation": ["automation", "rpa", "power-automate", "zapier", "make", "n8n", "workflow"],
    "blockchain": ["blockchain", "web3", "solidity", "defi", "nft", "crypto", "lightning"],
    "ml": ["machine-learning", "mlops", "fine-tuning", "embedding", "vector", "huggingface", "pytorch"],
    "maeve": ["maeve", "brain", "vault", "session", "skill-basin", "graphify", "claude"],
    "tools": ["github", "jira", "notion", "slack", "linear", "asana", "confluence"],
    "health": ["health", "medical", "fitness", "nutrition", "mental-health", "analyzer"],
    "game": ["game", "unity", "unreal", "godot", "gamedev"],
    "documentation": ["documentation", "readme", "changelog", "wiki", "technical-writing"],
    "performance": ["performance", "optimization", "profiling", "caching", "cdn"],
}

def log(msg):
    ts = datetime.now().strftime('%H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, 'a') as f:
        f.write(line + '\n')

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA journal_mode=WAL")
    return db

def save_vocab():
    VOCAB_PATH.write_text(json.dumps(VOCAB, indent=2))
    log(f"Vocabulary: {len(VOCAB)} categories saved to {VOCAB_PATH}")

def get_progress(db):
    row = db.execute("SELECT value FROM brain_kv WHERE key=?", (PROGRESS_KEY,)).fetchone()
    if row:
        return json.loads(row[0])
    return {"completed_batches": []}

def save_progress(db, progress):
    db.execute("INSERT OR REPLACE INTO brain_kv (key, value) VALUES (?, ?)",
               (PROGRESS_KEY, json.dumps(progress)))
    db.commit()

def build_tag_prompt(batch):
    vocab_summary = "\n".join(f"- {cat}: {', '.join(kws[:5])}" for cat, kws in VOCAB.items())
    skills_text = "\n".join(f"{i+1}. skill_name: {name}\n   brief: {brief[:200]}"
                            for i, (name, brief) in enumerate(batch))
    return f"""You are a skill taxonomy expert. Tag each skill with 2-5 categories from the controlled vocabulary.

CONTROLLED VOCABULARY (use ONLY these category names exactly):
{vocab_summary}

SKILLS TO TAG:
{skills_text}

Return ONLY a JSON object like:
{{"skill_name_1": ["cat1", "cat2"], "skill_name_2": ["cat1", "cat3", "cat4"]}}

Rules:
- Use exact category names from the vocabulary
- 2-5 tags per skill
- No explanation, no markdown, just JSON"""

def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass
    return None

def call_gemma(prompt):
    """Try Gemma local first. Returns dict or None."""
    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 500}
        }, timeout=60)
        if resp.status_code == 200:
            text = resp.json().get('response', '').strip()
            result = extract_json(text)
            if result:
                return result, 'gemma'
    except Exception as e:
        log(f"  Gemma: {e}")
    return None, None

def call_cloud(prompt, batch):
    """Fallback to llm_client cloud chain (Gemini -> OpenRouter -> Groq)."""
    try:
        import llm_client
    except ImportError:
        log("  llm_client not importable -- skipping cloud fallback")
        return None, None

    skill_name = batch[0][0] if batch else "batch"
    try:
        response, tokens, provider = llm_client.call_llm(skill_name, prompt)
        log(f"  Cloud response via {provider} ({tokens} tokens)")
        result = extract_json(response)
        if isinstance(result, dict) and result:
            return result, provider
        log(f"  Cloud returned non-dict: {str(response)[:100]}")
    except Exception as e:
        log(f"  Cloud error: {e}")
    return None, None


def infer_tags_from_name(name):
    n = name.lower()
    tags = []
    keyword_map = {
        'azure': 'cloud', 'aws': 'cloud', 'gcp': 'cloud', 'cloud': 'cloud',
        'terraform': 'devops', 'docker': 'devops', 'kubernetes': 'devops',
        'security': 'security', 'pentest': 'security', 'audit': 'security',
        'sql': 'data', 'data': 'data', 'analytics': 'data',
        'python': 'python', 'agent': 'ai-agents', 'llm': 'ai-agents', 'rag': 'ai-agents',
        'react': 'frontend', 'next': 'frontend', 'angular': 'frontend', 'tailwind': 'frontend',
        'api': 'backend', 'fastapi': 'backend', 'django': 'backend',
        'node': 'typescript', 'typescript': 'typescript',
        'ios': 'mobile', 'android': 'mobile', 'flutter': 'mobile',
        'test': 'testing', 'playwright': 'testing', 'tdd': 'testing',
        'trade': 'trading', 'market': 'trading', 'stock': 'trading',
        'canslim': 'trading', 'vcp': 'trading', 'dividend': 'trading',
        'marketing': 'marketing', 'seo': 'marketing', 'cro': 'marketing',
        'product': 'product', 'roadmap': 'product', 'agile': 'product',
        'rust': 'rust', 'dotnet': 'dotnet', 'csharp': 'dotnet',
        'java': 'java', 'golang': 'golang',
        'blockchain': 'blockchain', 'web3': 'blockchain',
        'ml': 'ml', 'embedding': 'ml', 'vector': 'ml',
        'maeve': 'maeve', 'brain': 'maeve', 'vault': 'maeve',
        'github': 'tools', 'slack': 'tools', 'notion': 'tools',
        'game': 'game', 'unity': 'game', 'unreal': 'game',
        'health': 'health', 'fitness': 'health',
        'automation': 'automation', 'rpa': 'automation', 'workflow': 'automation',
        'monitor': 'monitoring', 'observ': 'monitoring', 'log': 'monitoring',
        'arch': 'architecture', 'design': 'architecture',
        'doc': 'documentation', 'readme': 'documentation',
        'perf': 'performance', 'optim': 'performance', 'cache': 'performance',
    }
    for kw, tag in keyword_map.items():
        if kw in n and tag not in tags:
            tags.append(tag)
    return tags if tags else ['tools']

def run_tagging(db):
    rows = db.execute("""
        SELECT skill_name, compressed_brief FROM skill_registry
        WHERE compressed_brief IS NOT NULL AND LENGTH(compressed_brief) >= 30
        ORDER BY skill_name
    """).fetchall()

    progress = get_progress(db)
    completed = set(progress.get("completed_batches", []))
    batches = [rows[i:i+BATCH_SIZE] for i in range(0, len(rows), BATCH_SIZE)]
    log(f"Total skills: {len(rows)} | Batches: {len(batches)} | Already done: {len(completed)}")

    tagged = 0
    cloud_used = 0
    name_fallback = 0

    for batch_num, batch in enumerate(batches):
        if batch_num in completed:
            continue

        log(f"Batch {batch_num+1}/{len(batches)} ({len(batch)} skills)...")
        prompt = build_tag_prompt(batch)

        # Tier 1: Gemma local
        result, provider = call_gemma(prompt)

        # Tier 2: Cloud (Gemini/OpenRouter/Groq via llm_client)
        if result is None:
            log(f"  Gemma failed -- trying cloud fallback...")
            result, provider = call_cloud(prompt, batch)
            if result:
                cloud_used += 1

        updates = 0
        for skill_name, brief in batch:
            if result and skill_name in result:
                tags = result[skill_name]
                valid_tags = [t for t in tags if t in VOCAB]
            else:
                valid_tags = []

            if not valid_tags:
                valid_tags = infer_tags_from_name(skill_name)
                if result is None:
                    name_fallback += 1

            db.execute("UPDATE skill_registry SET topics=? WHERE skill_name=?",
                       (','.join(valid_tags), skill_name))
            updates += 1

        db.commit()
        completed.add(batch_num)
        save_progress(db, {"completed_batches": list(completed)})
        tagged += updates
        src = provider or 'name-based'
        log(f"  ✓ Tagged {updates} skills via {src}")
        time.sleep(0.3)

    log(f"Tagging complete: {tagged} tagged | cloud fallbacks: {cloud_used} | name-based: {name_fallback}")

def normalize_tags(db):
    rows = db.execute("SELECT skill_name, topics FROM skill_registry WHERE topics IS NOT NULL").fetchall()
    tag_counts = Counter()
    for _, topics in rows:
        for t in (topics or '').split(','):
            t = t.strip()
            if t:
                tag_counts[t] += 1

    rare = {t for t, c in tag_counts.items() if c < 2 and t not in VOCAB}
    if rare:
        log(f"Cleaning rare tags: {rare}")
        for skill_name, topics in rows:
            if topics:
                clean = ','.join(t for t in topics.split(',') if t.strip() not in rare)
                if clean != topics:
                    db.execute("UPDATE skill_registry SET topics=? WHERE skill_name=?", (clean, skill_name))
        db.commit()

    log(f"Tag distribution (top 15): {dict(tag_counts.most_common(15))}")
    return tag_counts

def build_graph(db):
    try:
        import networkx as nx
    except ImportError:
        import subprocess
        subprocess.run(['pip', 'install', 'networkx', '--break-system-packages', '-q'])
        import networkx as nx

    rows = db.execute("SELECT skill_name, topics, tier FROM skill_registry WHERE topics IS NOT NULL AND topics != ''").fetchall()

    G = nx.Graph()
    tag_to_skills = defaultdict(list)
    skill_tags = {}

    for skill_name, topics, tier in rows:
        tags = [t.strip() for t in (topics or '').split(',') if t.strip() and t.strip() in VOCAB]
        if tags:
            G.add_node(skill_name, tier=tier or 'basin', tags=tags)
            skill_tags[skill_name] = tags
            for tag in tags:
                tag_to_skills[tag].append(skill_name)

    for tag, skills in tag_to_skills.items():
        for i in range(len(skills)):
            for j in range(i+1, len(skills)):
                if G.has_edge(skills[i], skills[j]):
                    G[skills[i]][skills[j]]['weight'] += 1
                else:
                    G.add_edge(skills[i], skills[j], weight=1)

    log(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    degree_cent = nx.degree_centrality(G)
    try:
        between_cent = nx.betweenness_centrality(G, k=min(200, G.number_of_nodes()))
    except:
        between_cent = {n: 0 for n in G.nodes()}

    isolated = [n for n in G.nodes() if G.degree(n) == 0]
    clusters = defaultdict(list)
    for skill, tags in skill_tags.items():
        if tags:
            clusters[tags[0]].append(skill)

    return G, degree_cent, between_cent, isolated, clusters, tag_to_skills, skill_tags

def write_report(G, degree_cent, between_cent, isolated, clusters, tag_to_skills, skill_tags, tag_counts):
    now = datetime.now().strftime('%Y-%m-%d %H:%M ET')
    top_god = sorted(degree_cent.items(), key=lambda x: -x[1])[:20]
    top_bridge = sorted(between_cent.items(), key=lambda x: -x[1])[:15]

    lines = [
        "# GRAPH_REPORT.md",
        f"Generated: {now}",
        f"Corpus: {G.number_of_nodes()} skills | {G.number_of_edges()} edges | {len(isolated)} isolated",
        "", "---", "",
        "## God Nodes (Top 20 by Degree Centrality)",
        "Skills connected to the most other skills -- foundational hubs.",
        "",
        "| Rank | Skill | Centrality | Connections | Tags |",
        "|------|-------|------------|-------------|------|",
    ]
    for rank, (skill, cent) in enumerate(top_god, 1):
        tags = ','.join(skill_tags.get(skill, []))
        lines.append(f"| {rank} | {skill} | {cent:.4f} | {G.degree(skill)} | {tags} |")

    lines += [
        "", "## Bridge Skills (Top 15 by Betweenness Centrality)",
        "Skills connecting distinct clusters.",
        "",
        "| Rank | Skill | Betweenness | Tags |",
        "|------|-------|-------------|------|",
    ]
    for rank, (skill, cent) in enumerate(top_bridge, 1):
        tags = ','.join(skill_tags.get(skill, []))
        lines.append(f"| {rank} | {skill} | {cent:.4f} | {tags} |")

    lines += [
        "", "## Tag Clusters",
        "| Tag | Total Skills | Top 5 Members |",
        "|-----|-------------|---------------|",
    ]
    for tag in sorted(tag_to_skills.keys(), key=lambda t: -len(tag_to_skills[t])):
        members = tag_to_skills[tag]
        top5 = ', '.join(members[:5])
        more = f" +{len(members)-5} more" if len(members) > 5 else ""
        lines.append(f"| {tag} | {len(members)} | {top5}{more} |")

    lines += [
        f"", f"## Isolated Skills ({len(isolated)})",
        "Skills with no graph connections -- review for tagging gaps.", "",
    ]
    for skill in sorted(isolated)[:50]:
        lines.append(f"- {skill}")
    if len(isolated) > 50:
        lines.append(f"... and {len(isolated)-50} more")

    lines += ["", "## Tag Frequency", "| Tag | Count |", "|-----|-------|"]
    for tag, count in tag_counts.most_common():
        if tag in VOCAB:
            lines.append(f"| {tag} | {count} |")

    REPORT_PATH.write_text('\n'.join(lines))
    log(f"Report written: {REPORT_PATH}")


def inject_keys():
    """Decrypt vault_secrets and inject into environment for llm_client."""
    import os, sqlite3
    try:
        from cryptography.fernet import Fernet
        for kp in ['/home/derek/.vault_key', '/mnt/d/maeve_backup/vault_key.key']:
            if Path(kp).exists():
                vault_key = open(kp, 'rb').read().strip()
                fernet = Fernet(vault_key)
                db = sqlite3.connect(DB_PATH)
                for key in ['GROQ_API_KEY', 'GEMINI_API_KEY', 'OPENROUTER_API_KEY']:
                    row = db.execute("SELECT value_enc FROM vault_secrets WHERE key=? AND project='global'", (key,)).fetchone()
                    if row:
                        try:
                            os.environ[key] = fernet.decrypt(row[0].encode()).decode()
                        except: pass
                db.close()
                log("API keys injected from vault")
                return
        log("WARNING: vault key not found -- cloud fallback disabled")
    except Exception as e:
        log(f"Key injection failed: {e}")

def main():
    inject_keys()
    log(f"graphify_runner.py v2 starting {'(DRY RUN)' if DRY_RUN else ''}")
    with open(LOG_PATH, 'a') as f:
        f.write(f"\n{'='*60}\n")

    save_vocab()
    if DRY_RUN:
        log("DRY RUN complete")
        return

    db = get_db()

    if not GRAPH_ONLY:
        log("--- Stage 2: Batch tagging (Gemma -> Cloud -> name-based) ---")
        run_tagging(db)
    else:
        log("--- Skipping tagging (--graph-only) ---")

    log("--- Stage 3: Normalizing tags ---")
    tag_counts = normalize_tags(db)

    log("--- Stage 4: Building graph ---")
    G, degree_cent, between_cent, isolated, clusters, tag_to_skills, skill_tags = build_graph(db)

    log("--- Stage 5: Writing report ---")
    write_report(G, degree_cent, between_cent, isolated, clusters, tag_to_skills, skill_tags, tag_counts)

    db.execute("DELETE FROM brain_kv WHERE key=?", (PROGRESS_KEY,))
    db.commit()
    db.close()

    log("=== GRAPHIFY COMPLETE ===")
    log(f"Report: {REPORT_PATH}")

if __name__ == '__main__':
    main()
