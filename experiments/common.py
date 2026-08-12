"""Shared paths and helpers for experiments/ scripts.

Each script in this package is a standalone, auditable experiment: run it, it
writes a structured result (CSV/JSON/plots) under EXPERIMENT_RESULTS_DIR,
under its own subdirectory. No notebook state, no manual cell ordering.

Grow this file with real domain helpers as the research needs them (data
loaders, shared constants) — the disk-cache example below is illustrative,
not a framework to force every lookup through.

experiments/NN_*.py scripts must not import each other directly — promote
shared logic here first (see research_rules/04-no-cross-import.md).
"""

import json
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

EXPERIMENT_RESULTS_DIR = REPO_ROOT / "experiment_results"


def result_dir(script_name: str) -> pathlib.Path:
    """experiment_results/<script_name>/, created if missing."""
    d = EXPERIMENT_RESULTS_DIR / script_name
    d.mkdir(parents=True, exist_ok=True)
    return d


def disk_cached_json(cache_path: pathlib.Path, key: str, compute):
    """Look up `key` in a JSON-file-backed cache at `cache_path`, computing
    and persisting it via `compute()` on a miss.

    ponytail: single flat JSON file re-read/re-written whole on every miss —
    fine for the hundreds-to-low-thousands-of-keys scale this kind of
    research lookup usually has. Swap for sqlite/shelve if a research needs
    tens of thousands of keys and this starts showing up as slow.
    """
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    if key not in cache:
        cache[key] = compute()
        cache_path.write_text(json.dumps(cache, indent=2))
    return cache[key]
