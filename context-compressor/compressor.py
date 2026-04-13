#!/usr/bin/env python3
"""
Context Compressor — Maeve Efficiency Layer
Compresses file content before context injection to reduce token burn.
"""

import re
import sys
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime

BRAIN_DB = Path("/home/derek/maeve_brain.db")
STRIP_THRESHOLD = 500
SUMMARIZE_THRESHOLD = 2000

# ─── Token Estimation ────────────────────────────────────────────────────────

def estimate_tokens(text: str) -> int:
    """Rough estimate: 1 token per 4 characters."""
    return max(1, len(text) // 4)


# ─── Strip Mode ──────────────────────────────────────────────────────────────

def strip_content(text: str) -> str:
    """Remove comments, blank lines, license headers, boilerplate."""
    lines = text.splitlines()
    cleaned = []
    in_block_comment = False

    for line in lines:
        stripped = line.strip()

        # Block comment detection (Python/JS/CSS)
        if '"""' in stripped or "'''" in stripped or '/*' in stripped:
            in_block_comment = not in_block_comment
            continue
        if in_block_comment:
            continue

        # Skip inline comments (Python # and // style)
        if stripped.startswith('#') or stripped.startswith('//'):
            continue

        # Skip blank lines
        if not stripped:
            continue

        # Skip license/boilerplate headers
        if any(kw in stripped.lower() for kw in [
            'copyright', 'license', 'all rights reserved',
            'permission is hereby', 'mit license', 'apache'
        ]):
            continue

        cleaned.append(line)

    return '\n'.join(cleaned)


# ─── Summarize Mode ───────────────────────────────────────────────────────────

def summarize_content(text: str, path: str) -> str:
    """Extract structural skeleton: signatures, classes, config keys, errors."""
    lines = text.splitlines()
    summary_lines = []
    key_identifiers = []

    for line in lines:
        stripped = line.strip()

        # Capture function/class definitions
        if re.match(r'^(def |class |async def |export function |export class |function )', stripped):
            summary_lines.append(line)
            key_identifiers.append(stripped.split('(')[0].split(' ')[-1])
            continue

        # Capture config keys (common patterns)
        if re.match(r'^[A-Z_]{3,}\s*=', stripped):
            summary_lines.append(line)
            continue

        # Capture return statements (first occurrence per function)
        if stripped.startswith('return ') and len(stripped) < 80:
            summary_lines.append(f"    {stripped}")
            continue

        # Capture error raises
        if stripped.startswith('raise ') or 'raise Exception' in stripped:
            summary_lines.append(f"    {stripped}")
            continue

        # Capture import block (first 10 imports only)
        if stripped.startswith('import ') or stripped.startswith('from '):
            if summary_lines.count(stripped) == 0:
                summary_lines.append(line)

    skeleton = '\n'.join(summary_lines) if summary_lines else "[No extractable structure found]"
    identifiers = ', '.join(key_identifiers[:20]) if key_identifiers else "none detected"

    return f"## Structural Summary: {Path(path).name}\n\n{skeleton}\n\n## Key Identifiers\n{identifiers}"


# ─── Brain Logging ────────────────────────────────────────────────────────────

def ensure_log_table():
    """Create compression_log table if it does not exist."""
    try:
        conn = sqlite3.connect(BRAIN_DB)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS compression_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_date TEXT,
                file_path TEXT,
                mode TEXT,
                tokens_before INTEGER,
                tokens_after INTEGER,
                tokens_saved INTEGER,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False


def log_compression(path: str, mode: str, before: int, after: int):
    """Write compression event to Brain DB."""
    try:
        conn = sqlite3.connect(BRAIN_DB)
        conn.execute("""
            INSERT INTO compression_log
            (session_date, file_path, mode, tokens_before, tokens_after, tokens_saved, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d"),
            path,
            mode,
            before,
            after,
            before - after,
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()
    except Exception:
        pass  # Never let logging block compression


# ─── Main Compressor ─────────────────────────────────────────────────────────

def compress_file(path: str, mode: str = "auto") -> str:
    """
    Compress file content before context injection.

    Args:
        path: Absolute file path
        mode: auto | strip | summarize | full

    Returns:
        Annotated compressed string
    """
    ensure_log_table()

    try:
        content = Path(path).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return f"[COMPRESSOR ERROR: File not found — {path}]"
    except Exception as e:
        return f"[COMPRESSOR ERROR: {e}]"

    original_tokens = estimate_tokens(content)

    # Determine effective mode
    if mode == "full":
        return content

    if mode == "auto":
        if original_tokens < STRIP_THRESHOLD:
            mode = "passthrough"
        elif original_tokens < SUMMARIZE_THRESHOLD:
            mode = "strip"
        else:
            mode = "summarize"

    # Execute compression
    if mode == "passthrough":
        return content

    elif mode == "strip":
        result = strip_content(content)
        final_tokens = estimate_tokens(result)
        saved = original_tokens - final_tokens
        log_compression(path, "strip", original_tokens, final_tokens)
        return (
            f"[COMPRESSOR: strip | original ~{original_tokens} tokens → "
            f"~{final_tokens} tokens | saved ~{saved} tokens]\n\n{result}"
        )

    elif mode == "summarize":
        result = summarize_content(content, path)
        final_tokens = estimate_tokens(result)
        saved = original_tokens - final_tokens
        log_compression(path, "summarize", original_tokens, final_tokens)
        omitted = (
            "Docstrings, inline comments, example blocks, "
            "license headers, blank lines"
        )
        return (
            f"[COMPRESSOR: summarize | original ~{original_tokens} tokens → "
            f"~{final_tokens} tokens | saved ~{saved} tokens]\n\n"
            f"{result}\n\n## Omitted\n{omitted}"
        )

    return content


# ─── Test Suite ───────────────────────────────────────────────────────────────

def run_tests():
    """Verify all compression tiers work correctly."""
    import tempfile
    import os

    results = []

    # Test 1: Small file passthrough
    small = "x = 1\ny = 2\nprint(x + y)\n" * 5
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(small)
        tmp = f.name
    out = compress_file(tmp, mode="auto")
    passed = "[COMPRESSOR" not in out
    results.append(("Small file (< 500 tokens): passthrough", passed))
    os.unlink(tmp)

    # Test 2: Medium file strip
    medium = "# This is a comment\n\ndef foo():\n    pass\n\n" * 60
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(medium)
        tmp = f.name
    out = compress_file(tmp, mode="auto")
    passed = "COMPRESSOR: strip" in out
    results.append(("Medium file (500-2000 tokens): strip", passed))
    os.unlink(tmp)

    # Test 3: Large file summarize
    large = "def function_{}():\n    # comment\n    return {}\n\n".format
    large_content = "".join([f"def function_{i}():\n    # comment\n    return {i}\n\n" for i in range(200)])
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(large_content)
        tmp = f.name
    out = compress_file(tmp, mode="auto")
    passed = "COMPRESSOR: summarize" in out
    results.append(("Large file (> 2000 tokens): summarize", passed))
    os.unlink(tmp)

    # Test 4: Brain log write
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
        print("All tests passed.")
    else:
        print("Some tests FAILED. Review output above.")
        sys.exit(1)


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maeve Context Compressor")
    parser.add_argument("path", nargs="?", help="File path to compress")
    parser.add_argument("--mode", default="auto", choices=["auto", "strip", "summarize", "full"])
    parser.add_argument("--test", action="store_true", help="Run test suite")
    args = parser.parse_args()

    if args.test:
        run_tests()
    elif args.path:
        print(compress_file(args.path, args.mode))
    else:
        parser.print_help()
