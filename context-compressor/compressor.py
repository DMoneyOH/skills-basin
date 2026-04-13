#!/usr/bin/env python3
"""
Context Compressor v2 — Maeve Efficiency Layer
Wraps file reads to compress content BEFORE it enters context.
Handles code files (Python/JS/TS) and markdown/prose documents distinctly.
"""

import re
import sys
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime

BRAIN_DB = Path("/home/derek/maeve_brain.db")

# Thresholds (tokens)
PASSTHROUGH_THRESHOLD = 200
STRIP_THRESHOLD = 1000
# Above STRIP_THRESHOLD → summarize

# File type routing
CODE_EXTENSIONS = {'.py', '.js', '.ts', '.tsx', '.jsx', '.go', '.rs', '.java', '.cs', '.cpp', '.c', '.rb', '.sh'}
MARKDOWN_EXTENSIONS = {'.md', '.mdx', '.txt', '.rst'}
CONFIG_EXTENSIONS = {'.json', '.yaml', '.yml', '.toml', '.env', '.ini', '.cfg'}


# ─── Token Estimation ────────────────────────────────────────────────────────

def estimate_tokens(text: str) -> int:
    """Rough estimate: 1 token per 4 characters."""
    return max(1, len(text) // 4)


# ─── File Type Detection ─────────────────────────────────────────────────────

def detect_type(path: str) -> str:
    """Return 'code', 'markdown', 'config', or 'unknown'."""
    ext = Path(path).suffix.lower()
    if ext in CODE_EXTENSIONS:
        return 'code'
    if ext in MARKDOWN_EXTENSIONS:
        return 'markdown'
    if ext in CONFIG_EXTENSIONS:
        return 'config'
    # Sniff content for markdown heuristic
    return 'unknown'


# ─── Code Summarizer ─────────────────────────────────────────────────────────

def summarize_code(text: str, path: str) -> str:
    """Extract structural skeleton from code files."""
    lines = text.splitlines()
    summary_lines = []
    key_identifiers = []
    import_count = 0

    for line in lines:
        stripped = line.strip()

        # Imports (first 15 only)
        if (stripped.startswith('import ') or stripped.startswith('from ')) and import_count < 15:
            summary_lines.append(line)
            import_count += 1
            continue

        # Function/class definitions
        if re.match(r'^(def |class |async def |export function |export class |function |const \w+ = \(|export const )', stripped):
            summary_lines.append(line)
            name = re.split(r'[\s(=]', stripped)[1] if len(re.split(r'[\s(=]', stripped)) > 1 else stripped
            key_identifiers.append(name)
            continue

        # Config constants
        if re.match(r'^[A-Z_]{3,}\s*=', stripped):
            summary_lines.append(line)
            continue

        # Return statements
        if stripped.startswith('return ') and len(stripped) < 80:
            summary_lines.append(f"    {stripped}")
            continue

        # Error raises
        if stripped.startswith('raise ') or 'raise Exception' in stripped:
            summary_lines.append(f"    {stripped}")
            continue

    skeleton = '\n'.join(summary_lines) if summary_lines else "[No extractable structure found]"
    identifiers = ', '.join(key_identifiers[:20]) if key_identifiers else "none detected"

    return (
        f"## Code Summary: {Path(path).name}\n\n"
        f"{skeleton}\n\n"
        f"## Key Identifiers\n{identifiers}"
    )


# ─── Markdown Extractor ──────────────────────────────────────────────────────

def summarize_markdown(text: str, path: str) -> str:
    """
    Extract high-value structure from markdown/prose documents.
    Preserves: YAML frontmatter, headings, tables, code block signatures,
               bullet point first lines, numbered list items.
    Drops: paragraph prose, long code block bodies, repeated blank lines.
    """
    lines = text.splitlines()
    extracted = []
    in_frontmatter = False
    frontmatter_done = False
    in_code_block = False
    code_block_lines = 0
    CODE_BLOCK_PREVIEW = 2  # show first N lines of each code block (lever 2: reduced from 3)
    keep_next_prose = False  # lever 1: preserve first line after heading
    table_row_counts = {}    # lever 3: track rows per table section
    current_table_id = 0
    in_table = False
    table_rows_seen = 0
    TABLE_ROW_LIMIT = 8      # lever 3: max rows per table

    for i, line in enumerate(lines):
        stripped = line.strip()

        # YAML frontmatter (--- delimited at top of file)
        if i == 0 and stripped == '---':
            in_frontmatter = True
            extracted.append(line)
            continue
        if in_frontmatter:
            extracted.append(line)
            if stripped == '---' and i > 0:
                in_frontmatter = False
                frontmatter_done = True
            continue

        # Code block handling
        if stripped.startswith('```') or stripped.startswith('~~~'):
            if not in_code_block:
                in_code_block = True
                code_block_lines = 0
                extracted.append(line)  # opening fence with language tag
            else:
                in_code_block = False
                extracted.append(line)  # closing fence
            continue
        if in_code_block:
            code_block_lines += 1
            if code_block_lines <= CODE_BLOCK_PREVIEW:
                extracted.append(line)
            elif code_block_lines == CODE_BLOCK_PREVIEW + 1:
                extracted.append("    ... [code block truncated]")
            continue

        # Headings — always keep, flag next line for preservation
        if re.match(r'^#{1,4}\s', stripped):
            extracted.append(line)
            keep_next_prose = True
            continue

        # First non-blank line after a heading — keep regardless of type
        if keep_next_prose and stripped:
            keep_next_prose = False
            if len(stripped) <= 200:
                extracted.append(line)
            else:
                extracted.append(line[:200] + '…')
            continue
        elif keep_next_prose and not stripped:
            pass  # blank line after heading, keep waiting
        else:
            keep_next_prose = False

        # Table rows — keep up to TABLE_ROW_LIMIT rows, then truncate
        if stripped.startswith('|'):
            if not in_table:
                in_table = True
                table_rows_seen = 0
            table_rows_seen += 1
            if table_rows_seen <= TABLE_ROW_LIMIT:
                extracted.append(line)
            elif table_rows_seen == TABLE_ROW_LIMIT + 1:
                extracted.append(f"| ... [{table_rows_seen - TABLE_ROW_LIMIT}+ more rows truncated] |")
            continue
        else:
            if in_table:
                in_table = False
                table_rows_seen = 0

        # Bullet points — keep first line only
        if re.match(r'^[-*+]\s', stripped) or re.match(r'^\d+\.\s', stripped):
            # Keep if short or first sentence only
            if len(stripped) <= 120:
                extracted.append(line)
            else:
                extracted.append(line[:120] + '…')
            continue

        # Bold/definition lines (often key info)
        if re.match(r'^\*\*[^*]+\*\*', stripped) and len(stripped) < 150:
            extracted.append(line)
            continue

        # YAML-style key: value lines (common in SKILL.md frontmatter body)
        if re.match(r'^[a-zA-Z_-]+:\s+\S', stripped) and len(stripped) < 120:
            extracted.append(line)
            continue

        # Skip prose paragraphs (lines that don't match above patterns)
        # Keep blank lines between sections for readability
        if not stripped and extracted and extracted[-1].strip():
            extracted.append('')
        continue

    # Deduplicate consecutive blank lines
    result_lines = []
    prev_blank = False
    for line in extracted:
        if not line.strip():
            if not prev_blank:
                result_lines.append(line)
            prev_blank = True
        else:
            result_lines.append(line)
            prev_blank = False

    result = '\n'.join(result_lines).strip()
    fname = Path(path).name

    return (
        f"## Markdown Summary: {fname}\n\n"
        f"{result}\n\n"
        f"## Omitted\n"
        f"Prose paragraphs, code block bodies (preview only), repeated blanks"
    )


# ─── Config Stripper ─────────────────────────────────────────────────────────

def strip_config(text: str, path: str) -> str:
    """Strip comments from config files, preserve structure."""
    lines = text.splitlines()
    cleaned = [
        line for line in lines
        if not line.strip().startswith('#')
        and not line.strip().startswith('//')
        and line.strip()
    ]
    return '\n'.join(cleaned)


# ─── Generic Strip ───────────────────────────────────────────────────────────

def strip_content(text: str) -> str:
    """Remove comments and blank lines from any file."""
    lines = text.splitlines()
    cleaned = []
    in_block_comment = False

    for line in lines:
        stripped = line.strip()
        if '"""' in stripped or "'''" in stripped or '/*' in stripped:
            in_block_comment = not in_block_comment
            continue
        if in_block_comment:
            continue
        if stripped.startswith('#') or stripped.startswith('//'):
            continue
        if not stripped:
            continue
        if any(kw in stripped.lower() for kw in [
            'copyright', 'license', 'all rights reserved',
            'permission is hereby', 'mit license', 'apache'
        ]):
            continue
        cleaned.append(line)

    return '\n'.join(cleaned)


# ─── Brain Logging ────────────────────────────────────────────────────────────

def ensure_log_table():
    try:
        conn = sqlite3.connect(BRAIN_DB)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS compression_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_date TEXT,
                file_path TEXT,
                mode TEXT,
                file_type TEXT,
                tokens_before INTEGER,
                tokens_after INTEGER,
                tokens_saved INTEGER,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()
    except Exception:
        pass


def log_compression(path: str, mode: str, file_type: str, before: int, after: int):
    try:
        conn = sqlite3.connect(BRAIN_DB)
        conn.execute("""
            INSERT INTO compression_log
            (session_date, file_path, mode, file_type, tokens_before, tokens_after, tokens_saved, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d"),
            path, mode, file_type, before, after, before - after,
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()
    except Exception:
        pass


# ─── Core: Read and Compress (THE WRAPPER) ───────────────────────────────────

def read_and_compress(path: str, mode: str = "auto") -> str:
    """
    PRIMARY ENTRYPOINT.
    Reads a file and compresses it before returning content to caller.
    This is the Wozcode pattern: compression intercepts the read,
    not the other way around. Caller never sees uncompressed content.

    Args:
        path: Absolute file path
        mode: auto | strip | summarize | full

    Returns:
        Annotated compressed string ready for context injection
    """
    ensure_log_table()

    try:
        content = Path(path).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return f"[COMPRESSOR ERROR: File not found — {path}]"
    except PermissionError:
        return f"[COMPRESSOR ERROR: Permission denied — {path}]"
    except Exception as e:
        return f"[COMPRESSOR ERROR: {e}]"

    file_type = detect_type(path)
    original_tokens = estimate_tokens(content)

    # Passthrough: small files always pass through unchanged
    if mode == "full" or (mode == "auto" and original_tokens < PASSTHROUGH_THRESHOLD):
        return content

    # Determine effective mode if auto
    if mode == "auto":
        if original_tokens < STRIP_THRESHOLD:
            effective_mode = "strip"
        else:
            effective_mode = "summarize"
    else:
        effective_mode = mode

    # Route by file type and mode
    if effective_mode == "strip":
        if file_type == 'config':
            result = strip_config(content, path)
        else:
            result = strip_content(content)
        final_tokens = estimate_tokens(result)
        saved = original_tokens - final_tokens
        log_compression(path, "strip", file_type, original_tokens, final_tokens)
        return (
            f"[COMPRESSOR: strip | {file_type} | "
            f"~{original_tokens} → ~{final_tokens} tokens | saved ~{saved}]\n\n{result}"
        )

    elif effective_mode == "summarize":
        if file_type == 'markdown' or (file_type == 'unknown' and _looks_like_markdown(content)):
            result = summarize_markdown(content, path)
            actual_type = 'markdown'
        elif file_type == 'code':
            result = summarize_code(content, path)
            actual_type = 'code'
        elif file_type == 'config':
            result = strip_config(content, path)
            actual_type = 'config'
        else:
            # Unknown: try markdown first (more common in our vault/skills)
            result = summarize_markdown(content, path)
            actual_type = 'markdown-fallback'

        final_tokens = estimate_tokens(result)
        saved = original_tokens - final_tokens
        log_compression(path, "summarize", actual_type, original_tokens, final_tokens)
        return (
            f"[COMPRESSOR: summarize | {actual_type} | "
            f"~{original_tokens} → ~{final_tokens} tokens | saved ~{saved}]\n\n{result}"
        )

    return content


def _looks_like_markdown(text: str) -> bool:
    """Heuristic: does this look like markdown prose?"""
    lines = text.splitlines()[:20]
    md_signals = sum(1 for l in lines if
        l.strip().startswith('#') or
        l.strip().startswith('- ') or
        l.strip().startswith('* ') or
        l.strip().startswith('|') or
        l.strip() == '---'
    )
    return md_signals >= 2


# ─── Legacy wrapper (backwards compatibility) ────────────────────────────────

def compress_file(path: str, mode: str = "auto") -> str:
    """Backwards-compatible alias for read_and_compress."""
    return read_and_compress(path, mode)


# ─── Test Suite ───────────────────────────────────────────────────────────────

def run_tests():
    import tempfile, os

    results = []

    # Test 1: Small file passthrough
    small = "x = 1\ny = 2\nprint(x + y)\n" * 5
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(small); tmp = f.name
    out = read_and_compress(tmp, mode="auto")
    results.append(("Small file passthrough", "[COMPRESSOR" not in out))
    os.unlink(tmp)

    # Test 2: Medium code strip
    medium = "# comment\n\ndef foo():\n    pass\n\n" * 30
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(medium); tmp = f.name
    out = read_and_compress(tmp, mode="auto")
    results.append(("Medium code strip", "COMPRESSOR: strip" in out))
    os.unlink(tmp)

    # Test 3: Large code summarize
    large = "".join([f"def function_{i}():\n    # comment\n    x = i * 2\n    return x\n\n" for i in range(300)])
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(large); tmp = f.name
    out = read_and_compress(tmp, mode="auto")
    results.append(("Large code summarize", "COMPRESSOR: summarize" in out and "code" in out))
    os.unlink(tmp)

    # Test 4: Markdown summarize — headings preserved
    md = "---\nname: test-skill\ndescription: A test skill\n---\n\n"
    md += "# Overview\n\nThis is prose text that should be dropped.\n\n"
    md += "## Usage\n\n- Bullet point one\n- Bullet point two\n\n"
    md += "## Reference\n\n| Col1 | Col2 |\n|---|---|\n| a | b |\n\n"
    md += "```python\ndef example():\n    return True\n```\n\n"
    prose_line = "This is long prose content that should be dropped by the markdown extractor. "
    md += (prose_line * 30 + "\n\n") * 8
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(md); tmp = f.name
    out = read_and_compress(tmp, mode="auto")
    md_pass = ("COMPRESSOR: summarize" in out and
               "markdown" in out and
               "# Overview" in out and
               "Bullet point one" in out and
               "Col1" in out)
    results.append(("Markdown summarize — structure preserved", md_pass))
    os.unlink(tmp)

    # Test 5: Markdown tokens saved meaningfully
    long_md = "# Title\n\n"
    long_md += "This is a long prose paragraph. " * 50 + "\n\n"
    long_md += "## Section 2\n\n"
    long_md += "More prose content here. " * 50 + "\n\n"
    long_md += "- Key bullet one\n- Key bullet two\n\n"
    long_md += "## Section 3\n\n"
    long_md += "Even more prose. " * 50 + "\n\n"
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(long_md); tmp = f.name
    out = read_and_compress(tmp, mode="summarize")
    before = estimate_tokens(long_md)
    after = estimate_tokens(out)
    savings_pct = int((before - after) / before * 100)
    results.append((f"Markdown meaningful savings ({savings_pct}% reduction)", savings_pct >= 40))
    os.unlink(tmp)

    # Test 6: Brain log write
    ensure_log_table()
    try:
        conn = sqlite3.connect(BRAIN_DB)
        conn.execute("SELECT COUNT(*) FROM compression_log")
        conn.close()
        results.append(("Brain log write", True))
    except Exception:
        results.append(("Brain log write", False))

    # Print results
    all_passed = True
    for label, passed in results:
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_passed = False
        print(f"[TEST] {label}: {status}")

    if all_passed:
        print("\nAll tests passed.")
    else:
        print("\nSome tests FAILED.")
        sys.exit(1)


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maeve Context Compressor v2")
    parser.add_argument("path", nargs="?", help="File path to compress")
    parser.add_argument("--mode", default="auto",
                        choices=["auto", "strip", "summarize", "full"])
    parser.add_argument("--test", action="store_true", help="Run test suite")
    args = parser.parse_args()

    if args.test:
        run_tests()
    elif args.path:
        print(read_and_compress(args.path, args.mode))
    else:
        parser.print_help()
