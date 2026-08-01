"""Shared paths for reports/ scripts. Mirrors experiments/common.py's pattern."""

import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

REPORT_RESULTS_DIR = REPO_ROOT / "report_results"
EXPERIMENT_RESULTS_DIR = REPO_ROOT / "experiment_results"


def result_dir(script_name: str) -> pathlib.Path:
    """report_results/<script_name>/, created if missing."""
    d = REPORT_RESULTS_DIR / script_name
    d.mkdir(parents=True, exist_ok=True)
    return d
