"""Optional: data-gathering/preprocessing this report needs beyond what an
experiments/ script already produced (e.g. pulling from a remote source,
scanning a data directory whose layout may change).

Only add this file when the report needs its own data collection. Delete it
if compute.py can read experiment_results/ directly.

Write this to be re-run, not a one-off throwaway -- discover paths/schema at
run time rather than hardcoding today's layout, and fail loudly on missing
access rather than silently reporting partial/wrong numbers. See
research_rules/06-report-separation.md.
"""


def collect_data() -> dict:
    raise NotImplementedError("fill in or delete this file")
