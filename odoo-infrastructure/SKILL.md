---
name: odoo-infrastructure
description: >
  "Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools."
  Covers: odoo infrastructure, odoo docker deployment, odoo backup strategy, odoo performance tuner.
  Use for any task involving odoo infrastructure, odoo docker deployment, odoo backup strategy, odoo performance tuner.
merged_from:
  - odoo-docker-deployment
  - odoo-backup-strategy
  - odoo-performance-tuner
merged_at: 2026-04-25
---

# odoo-infrastructure

<!-- odoo-docker-deployment -->
## Overview

This skill provides a complete, production-ready Docker setup for Odoo, including PostgreSQL, persistent file storage, environment variable configuration, and an optional Nginx reverse proxy with SSL. It covers both development and production configurations.

## When to Use This Skill

- Spinning up a local Odoo development environment with Docker.
- Deploying Odoo to a VPS or cloud server (AWS, DigitalOcean, etc.).
- Troubleshooting Odoo container startup failures or database connection errors.
- Adding a reverse proxy with SSL to an existing Odoo Docker setup.

## How It Works

1. **Activate**: Mention `@odoo-docker-deployment` and describe your deployment scenario.
2. **Generate**: Receive a complete `docker-compose.yml` and `odoo.conf` ready to run.
3. **Debug**: Describe your container error and get a diagnosis with a fix.

## Examples

### Example 1: Production docker-compose.yml

```yaml
# Note: The top-level 'version' key is deprecated in Docker Compose v2+
# and can be safely omitted. Remove it to avoid warnings.

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: odoo
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - odoo-net

  odoo:
    image: odoo:17.0
    restart: always
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8069:8069"
      - "8072:8072"   # Longpolling for live chat / bus
    environment:
      HOST: db
      USER: odoo
      PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./addons:/mnt/extra-addons   # Custom modules
      - ./odoo.conf:/etc/odoo/odoo.conf
    networks:
      - odoo-net

volumes:
  postgres-data:
  odoo-web-data:

networks:
  odoo-net:
```

### Example 2: odoo.conf

```ini
[options]
admin_passwd = ${ODOO_MASTER_PASSWORD}    ; set via env or .env file
db_host = db
db_port = 5432
db_user = odoo
db_password = ${POSTGRES_PASSWORD}        ; set via env or .env file

; addons_path inside the official Odoo Docker image (Debian-based)
addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons

logfile = /var/log/odoo/odoo.log
log_level = warn

; Worker tuning for a 4-core / 8GB server:
workers = 9                ; (CPU cores × 2) + 1
max_cron_threads = 2
limit_memory_soft = 1610612736   ; 1.5 GB — soft kill threshold
limit_memory_hard = 2147483648   ; 2.0 GB — hard kill threshold
limit_time_cpu = 600
limit_time_real = 1200
limit_request = 8192
```

### Example 3: Common Commands

```bash
# Start all services in background
docker compose up -d

# Stream Odoo logs in real time
docker compose logs -f odoo

# Restart Odoo only (not DB — avoids data risk)
docker compose restart odoo

# Stop all services
docker compose down

# Backup the database to a local SQL dump
docker compose exec db pg_dump -U odoo odoo > backup_$(date +%Y%m%d).sql

# Update a custom module without restarting the server
docker compose exec odoo odoo -d odoo --update my_module --stop-after-init
```

## Best Practices

- ✅ **Do:** Store all secrets in a `.env` file and reference them with `${VAR}` — never hardcode passwords in `docker-compose.yml`.
- ✅ **Do:** Use `depends_on: condition: service_healthy` with a PostgreSQL healthcheck to prevent Odoo starting before the DB is ready.
- ✅ **Do:** Put Nginx in front of Odoo for SSL termination (Let's Encrypt / Certbot) — never expose Odoo directly on port 80/443.
- ✅ **Do:** Set `workers = (CPU cores × 2) + 1` in `odoo.conf` — `workers = 0` uses single-threaded mode and blocks all users.
- ❌ **Don't:** Expose port 5432 (PostgreSQL) to the public internet — keep it on the internal Docker network only.
- ❌ **Don't:** Use the `latest` or `17` Docker image tags in production — always pin to a specific patch-level tag (e.g., `odoo:17.0`).
- ❌ **Don't:** Mount `odoo.conf` and rely on it for secrets in CI/CD — use Docker secrets or environment variables instead.

## Limitations

- This skill covers **self-hosted Docker deployments** — Odoo.sh (cloud-managed hosting) has a completely different deployment model.
- **Horizontal scaling** (multiple Odoo containers behind a load balancer) requires shared filestore (NFS or S3-compatible storage) not covered here.
- Does not include an Nginx configuration template — consult the [official Odoo Nginx docs](https://www.odoo.com/documentation/17.0/administration/install/deploy.html) for the full reverse proxy config.
- The `addons_path` inside the Docker image may change with new base image versions — always verify after upgrading the Odoo image.


<!-- MERGED INTO: odoo-infrastructure on 2026-04-18 -->
<!-- Use `odoo-infrastructure` instead. -->

---

<!-- odoo-backup-strategy -->
## Overview

A complete Odoo backup must include both the **PostgreSQL database** and the **filestore** (attachments, images). This skill covers manual and automated backup procedures, offsite storage, and the correct restore sequence to bring a down Odoo instance back online.

## When to Use This Skill

- Setting up a backup strategy for a production Odoo instance.
- Automating daily backups with shell scripts and cron.
- Restoring Odoo after a server failure or data corruption event.
- Diagnosing a failed backup or corrupt restore.

## How It Works

1. **Activate**: Mention `@odoo-backup-strategy` and describe your server environment.
2. **Generate**: Receive a complete backup script tailored to your setup.
3. **Restore**: Get step-by-step restore instructions for any failure scenario.

## Examples

### Example 1: Manual Database + Filestore Backup

```bash
#!/bin/bash
# backup_odoo.sh

DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="odoo"
DB_USER="odoo"
FILESTORE_PATH="/var/lib/odoo/.local/share/Odoo/filestore/$DB_NAME"
BACKUP_DIR="/backups/odoo"

mkdir -p "$BACKUP_DIR"

# Step 1: Dump the database
pg_dump -U $DB_USER -Fc $DB_NAME > "$BACKUP_DIR/db_$DATE.dump"

# Step 2: Archive the filestore
tar -czf "$BACKUP_DIR/filestore_$DATE.tar.gz" -C "$FILESTORE_PATH" .

echo "✅ Backup complete: db_$DATE.dump + filestore_$DATE.tar.gz"
```

### Example 2: Automate with Cron (daily at 2 AM)

```bash
# Run: crontab -e
# Add this line:
0 2 * * * /opt/scripts/backup_odoo.sh >> /var/log/odoo_backup.log 2>&1
```

### Example 3: Upload to S3 (after backup)

```bash
# Add to backup script after tar command:
aws s3 cp "$BACKUP_DIR/db_$DATE.dump"        s3://my-odoo-backups/db/
aws s3 cp "$BACKUP_DIR/filestore_$DATE.tar.gz" s3://my-odoo-backups/filestore/

# Optional: Delete local backups older than 7 days
find "$BACKUP_DIR" -type f -mtime +7 -delete
```

### Example 4: Full Restore Procedure

```bash
# Step 1: Stop Odoo
docker compose stop odoo  # or: systemctl stop odoo

# Step 2: Recreate and restore the database
# (--clean alone fails if the DB doesn't exist; drop and recreate first)
dropdb -U odoo odoo 2>/dev/null || true
createdb -U odoo odoo
pg_restore -U odoo -d odoo db_YYYYMMDD_HHMMSS.dump

# Step 3: Restore the filestore
FILESTORE=/var/lib/odoo/.local/share/Odoo/filestore/odoo
rm -rf "$FILESTORE"/*
tar -xzf filestore_YYYYMMDD_HHMMSS.tar.gz -C "$FILESTORE"/

# Step 4: Restart Odoo
docker compose start odoo

# Step 5: Verify — open Odoo in the browser and check:
#   - Can you log in?
#   - Are recent records visible?
#   - Are file attachments loading?
```

## Best Practices

- ✅ **Do:** Test restores monthly in a staging environment — a backup you've never restored is not a backup.
- ✅ **Do:** Follow the **3-2-1 rule**: 3 copies, 2 different media types, 1 offsite copy (e.g., S3 or a remote server).
- ✅ **Do:** Back up **immediately before every Odoo upgrade** — this is your rollback point.
- ✅ **Do:** Verify backup integrity: `pg_restore --list backup.dump` should complete without errors.
- ❌ **Don't:** Back up only the database without the filestore — all attachments and images will be missing after a restore.
- ❌ **Don't:** Store backups on the same disk or same server as Odoo — a disk or server failure destroys both.
- ❌ **Don't:** Run `pg_restore --clean` against a non-existent database — always create the database first.

## Limitations

- Does not cover **Odoo.sh built-in backups** — Odoo.sh has its own backup system accessible from the dashboard.
- This script assumes a **single-database** Odoo setup. Multi-database instances require looping over all databases.
- Filestore path may differ between installations (Docker volume vs. bare-metal). Always verify the path with `odoo-bin shell` before running a restore.
- Large filestores (100GB+) may require incremental backup tools like `rsync` or `restic` rather than full `tar.gz` archives.


<!-- MERGED INTO: odoo-infrastructure on 2026-04-18 -->
<!-- Use `odoo-infrastructure` instead. -->

---

<!-- odoo-performance-tuner -->
## Overview

This skill helps diagnose and resolve Odoo performance problems — from slow page loads and database bottlenecks to worker misconfiguration and memory bloat. It covers PostgreSQL query tuning, Odoo worker settings, and built-in profiling tools.

## When to Use This Skill

- Odoo is slow in production (slow page loads, timeouts).
- Getting `MemoryError` or `Worker timeout` errors in logs.
- Diagnosing a slow database query using Odoo's profiler.
- Tuning `odoo.conf` for a specific server spec.

## How It Works

1. **Activate**: Mention `@odoo-performance-tuner` and describe your performance issue.
2. **Diagnose**: Share relevant log lines or config and receive a root cause analysis.
3. **Fix**: Get exact configuration changes with explanations.

## Examples

### Example 1: Recommended Worker Configuration

```ini
# odoo.conf — tuned for a 4-core, 8GB RAM server

workers = 9                   # (CPU_cores × 2) + 1 — never set to 0 in production
max_cron_threads = 2          # background cron jobs; keep ≤ 2 to preserve user-facing capacity
limit_memory_soft = 1610612736  # 1.5 GB — worker is recycled gracefully after this
limit_memory_hard = 2147483648  # 2.0 GB — worker is killed immediately; prevents OOM crashes
limit_time_cpu = 600          # max CPU seconds per request
limit_time_real = 1200        # max wall-clock seconds per request
limit_request = 8192          # max requests before worker recycles (prevents memory leaks)
```

### Example 2: Find Slow Queries with PostgreSQL

```sql
-- Step 1: Enable pg_stat_statements extension (run once as postgres superuser)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Step 2: Also add to postgresql.conf and reload:
-- shared_preload_libraries = 'pg_stat_statements'
-- log_min_duration_statement = 1000   -- log queries taking > 1 second

-- Step 3: Find the top 10 slowest average queries
SELECT
    LEFT(query, 100) AS query_snippet,
    round(mean_exec_time::numeric, 2) AS avg_ms,
    calls,
    round(total_exec_time::numeric, 2) AS total_ms
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Step 4: Check for missing indexes causing full table scans
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE tablename = 'sale_order_line'
  AND correlation < 0.5   -- low correlation = poor index efficiency
ORDER BY n_distinct DESC;
```

### Example 3: Use Odoo's Built-In Profiler

```text
Prerequisites: Run Odoo with ?debug=1 in the URL to enable debug mode.

Menu: Settings → Technical → Profiling

Steps:
  1. Click "Enable Profiling" — set a duration (e.g., 60 seconds)
  2. Navigate to and reproduce the slow action
  3. Return to Settings → Technical → Profiling → View Results

What to look for:
  - Total SQL queries > 100 on a single page  → N+1 query problem
  - Single queries taking > 100ms             → missing DB index
  - Same query repeated many times            → missing cache, use @ormcache
  - Python time high but SQL low             → compute field inefficiency
```

## Best Practices

- ✅ **Do:** Use `mapped()`, `filtered()`, and `sorted()` on in-memory recordsets — they don't trigger additional SQL.
- ✅ **Do:** Add PostgreSQL B-tree indexes on columns frequently used in domain filters (`partner_id`, `state`, `date_order`).
- ✅ **Do:** Enable Odoo's HTTP caching for static assets and put a CDN (Cloudflare, AWS CloudFront) in front of the website.
- ✅ **Do:** Use `@tools.ormcache` decorator on methods pulled repeatedly with the same arguments.
- ❌ **Don't:** Set `workers = 0` in production — single-threaded mode serializes all requests and blocks all users on any slow operation.
- ❌ **Don't:** Ignore `limit_memory_soft` — workers exceeding it are recycled between requests; without the limit they grow unbounded and crash.
- ❌ **Don't:** Directly manipulate `prefetch_ids` on recordsets — rely on Odoo's automatic batch prefetching, which activates by default.

## Limitations

- PostgreSQL tuning (`shared_buffers`, `work_mem`, `effective_cache_size`) is highly server-specific and not covered in depth here — use [PGTune](https://pgtune.leopard.in.ua/) as a starting baseline.
- The built-in Odoo profiler only captures **Python + SQL** traces; JavaScript rendering performance requires browser DevTools.
- **Odoo.sh** managed hosting restricts direct PostgreSQL and `odoo.conf` access — some tuning options are unavailable.
- Does not cover **Redis-based session store** or **Celery task queue** optimizations, which are advanced patterns for very high-traffic instances.


<!-- MERGED INTO: odoo-infrastructure on 2026-04-18 -->
<!-- Use `odoo-infrastructure` instead. -->

---

<!-- odoo-migration-helper -->
## Overview

Migrating Odoo modules between major versions requires careful handling of API changes, deprecated methods, renamed fields, and new view syntax. This skill guides you through the migration process systematically, covering the most common breaking changes between versions.

## When to Use This Skill

- Upgrading a custom module from Odoo 14/15/16 to a newer version.
- Getting a checklist of things to check before running `odoo-upgrade`.
- Fixing deprecation warnings after a version upgrade.
- Understanding what changed between two specific Odoo versions.

## How It Works

1. **Activate**: Mention `@odoo-migration-helper`, specify your source and target versions, and paste your module code.
2. **Analyze**: Receive a list of breaking changes with before/after code fixes.
3. **Validate**: Get a migration checklist specific to your module's features.

## Key Migration Changes by Version

### Odoo 16 → 17

| Topic | Old (v16) | New (v17) |
|---|---|---|
| View visibility | `attrs="{'invisible': [...]}"` | `invisible="condition"` |
| Chatter | `<div class="oe_chatter">` | `<chatter/>` |
| Required/Readonly | `attrs="{'required': [...]}"` | `required="condition"` |
| Python minimum | 3.10 | 3.10+ |
| JS modules | Legacy `define(['web.core'])` | ES module `import` syntax |

### Odoo 15 → 16

| Topic | Old (v15) | New (v16) |
|---|---|---|
| Website published flag | `website_published = True` | `is_published = True` |
| Mail aliases | `alias_domain` on company | Moved to `mail.alias.domain` model |
| Report render | `_render_qweb_pdf()` | `_render_qweb_pdf()` (same, but signature changed) |
| Accounting move | `account.move.line` grouping | Line aggregation rules updated |
| Email threading | `mail_thread_id` | Deprecated; use `message_ids` |

## Examples

### Example 1: Migrate `attrs` visibility to Odoo 17

```xml
<!-- v16 — domain-based attrs -->
<field name="discount" attrs="{'invisible': [('product_type', '!=', 'service')]}"/>
<field name="discount" attrs="{'required': [('state', '=', 'sale')]}"/>

<!-- v17 — inline Python expressions -->
<field name="discount" invisible="product_type != 'service'"/>
<field name="discount" required="state == 'sale'"/>
```

### Example 2: Migrate Chatter block

```xml
<!-- v16 -->
<div class="oe_chatter">
    <field name="message_follower_ids"/>
    <field name="activity_ids"/>
    <field name="message_ids"/>
</div>

<!-- v17 -->
<chatter/>
```

### Example 3: Migrate website_published flag (v15 → v16)

```python
# v15
record.website_published = True

# v16+
record.is_published = True
```

## Best Practices

- ✅ **Do:** Test with `--update=your_module` on each version before pushing to production.
- ✅ **Do:** Use the official [Odoo Upgrade Guide](https://upgrade.odoo.com/) to get an automated pre-upgrade analysis report.
- ✅ **Do:** Check OCA migration notes and the module's `HISTORY.rst` for community modules.
- ✅ **Do:** Run `npm run validate` after migration to catch manifest or frontmatter issues early.
- ❌ **Don't:** Skip intermediate versions — go v14→v15→v16→v17 sequentially; never jump.
- ❌ **Don't:** Forget to update `version` in `__manifest__.py` (e.g., `17.0.1.0.0`).
- ❌ **Don't:** Assume OCA modules are migration-ready; check their GitHub branch for the target version.

## Limitations

- Covers **v14 through v17** only — does not address v13 or older (pre-manifest era has fundamentally different module structure).
- The **Odoo.sh automated upgrade** path has additional steps not covered here; refer to Odoo.sh documentation.
- **Enterprise-specific modules** (e.g., `account_accountant`, `sign`) may have undocumented breaking changes; test on a staging environment with Enterprise license.
- JavaScript OWL component migration (v15 Legacy → v16 OWL) is a complex topic not fully covered by this skill.


<!-- MERGED INTO: odoo-infrastructure on 2026-04-18 -->
<!-- Use `odoo-infrastructure` instead. -->
