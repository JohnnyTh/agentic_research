# Rule: separate compute, render, and data-collection in every report

Trigger: writing or editing a report script under `reports/`.

A report's orchestrator script (`reports/NN_name_report.py`) must stay thin:
it imports from a `reports/NN_name/` package and calls, in order,
`collect` (if present) → `compute` → `render`. It must not itself compute
stats or build HTML strings.

- **`reports/NN_name/compute.py`** — pure functions, input data in, a stats
  dict out. No HTML, no network/file I/O beyond reading its own inputs.
- **`reports/NN_name/render.py`** — pure functions, stats dict in, HTML (or
  Markdown) string out. No stats computation, no network/file I/O.
- **`reports/NN_name/collect.py`** — optional, only when the report needs its
  own data-gathering/preprocessing beyond reusing an `experiments/` script's
  output (e.g. pulling from a remote source, scanning a data directory).

**Why:** correcting a report's wording later ("say it this way instead")
should only require opening `render.py` — an agent shouldn't have to re-read
or risk re-touching the stats computation to fix prose. Keeping them apart
also means the numbers can be trusted unchanged across wording edits.

**collect.py must not hardcode today's data layout.** Write it to discover
paths/schema at run time rather than assuming a fixed location or shape, and
to fail loudly if expected access/data is missing rather than silently
reporting partial or wrong numbers — data sources move and reshape over
time, and this file is exactly what a future session reaches for instead of
writing a fresh exploration script from scratch. Concretely: discover which
buckets/schemes/hosts exist by scanning what's actually there (don't
hardcode "there are exactly two data generations"), and prefer failing
loudly over silently falling back when something expected isn't found.

This is a narrower exception to `research_rules/04-no-cross-import.md`:
`compute.py`/`render.py`/`collect.py` within one report's own `NN_name/`
package are that report's internal structure, not a separate script — the
no-cross-import ban is about one experiment/report reaching into another's
module, not about a report's own files importing each other.
