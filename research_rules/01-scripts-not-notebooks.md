# Rule: scripts, not notebooks, for anything that's a result

Trigger: writing or citing any experiment/report as a finding.

Every real investigation step is a standalone Python script under
`experiments/`, numbered in the order it was built (`01_...py`, `02_...py`,
...). Each script is self-contained, runnable via
`PYTHONPATH="$PWD" python {{RESEARCH_DIR_NAME}}/experiments/NN_name.py`
from the repo root, and writes structured output (CSV/JSON/HTML plots) to
`experiment_results/NN_name/`. `.ipynb` notebooks, if used at all, are for
human ad hoc exploration ONLY — never cite a notebook run as a finding, and
any verification step must also be a script.
