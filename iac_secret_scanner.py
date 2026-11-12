#!/usr/bin/env python3
"""Lightweight static scanner for common secrets in IaC/configuration files.

This is a heuristic helper, not a replacement for a dedicated secret scanner.
Run it only against repositories and files you are authorized to inspect.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PATTERNS = {
    "aws_key": re.compile(r"(?i)\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"),
    "password": re.compile(r"""(?i)\b(?:password|passwd|secret)\s*[:=]\s*['"][^'"]{8,}['"]"""),
}
EXTENSIONS = {".tf", ".yml", ".yaml", ".json", ".env", ".sh", ".toml", ".ini"}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def scan_file(path: Path) -> list[str]:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return [f"read_error:{exc.__class__.__name__}"]
    return [name for name, pattern in PATTERNS.items() if pattern.search(content)]


def iter_files(root: Path):
    if root.is_symlink():
        raise ValueError("The scan root must not be a symbolic link")
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")

    for path in root.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        try:
            path.resolve(strict=True).relative_to(root)
        except (OSError, ValueError):
            continue
        if path.suffix.lower() in EXTENSIONS or path.name == ".env":
            yield path


def run(root: Path) -> dict[str, list[str]]:
    results = {}
    for path in iter_files(root):
        hits = scan_file(path)
        if hits:
            results[str(path)] = hits
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("."))
    args = parser.parse_args()
    if not args.path.exists() or not args.path.is_dir():
        parser.error(f"not a directory: {args.path}")
    results = run(args.path)
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())
