# {{RESEARCH_NAME}} — agent entrypoint

Read this first if you're picking up this research in a new conversation.
It orients you: what this research is, the stages it moves through, the
rules to follow, where everything lives, and what's open right now. This
file is a map, not a summary of findings — for that, read in this order:

1. `RESEARCH_SUMMARY.md` — quick-scan bullet headlines per session, read
   this first for "what do we know so far."
2. `RESEARCH_LOG.md` — index (date + title, one line each) into `research_log/`,
   where the full detail behind every summary bullet actually lives, one
   file per session (methodology, full reasoning, every gotcha hit). Read
   the index to find the entry, then open only that file — don't read the
   whole `research_log/` directory, it's split precisely so agents don't
   have to.
3. `RESEARCH_PLAN.md` — open ideas to explore next, by priority; check it
   before starting new work and add to it (don't just leave ideas in log
   entries) whenever a session surfaces something worth investigating later.
4. `report_results/` — synthesized, human-facing writeups (see "Stage 4:
   Report" below). Read an existing report before writing a new one that
   covers similar ground — extend or supersede it, don't duplicate it.

<!-- INIT_RESEARCH.md not run yet? Do that first — it turns this file from a
     template into a real entrypoint. Delete this comment once it has been. -->

## What this research is

Goal: {{RESEARCH_GOAL — one paragraph: the question this research answers
and why it matters}}.

System/domain under study: {{DOMAIN_DESCRIPTION}}. Background docs, if any
already exist and don't need re-explaining here:
{{BACKGROUND_LINKS_OR_NONE}}.

## The four stages

Every research effort here moves through the same four stages. A session
can revisit an earlier stage (a report can surface a gap that sends you back
to defining a new experiment) — the order is a loop, not a one-way gate.

1. **Define** — turn an open question (from `RESEARCH_PLAN.md`, or a new one
   surfaced this session) into a concrete, runnable experiment: what's being
   measured, against what data, with what success signal. Write the plan
   entry before writing code if the experiment is non-trivial.
2. **Run & explore** — implement and run the experiment as a numbered script
   under `experiments/`, inspect its output, iterate until the result is
   trustworthy (see the provenance/sanity-check rule below).
3. **Thesis formulation** — once one or more experiments produce results,
   step back and state what they imply for the research goal: a short,
   falsifiable claim ("X causes Y", "model A beats model B on Z"), grounded
   in specific experiment output, not vibes. A thesis can draw on multiple
   experiments. Record it as a `RESEARCH_SUMMARY.md` entry's "Implies" line
   at minimum; promote it to a full report (stage 4) once it's substantial
   or decision-relevant enough that someone outside this research would want
   to read it standalone.
4. **Report** — write a self-contained, human-facing synthesis of one or more
   theses as a numbered script under `reports/` (see "Reports" below),
   modeled on prior reports in `report_results/` if any exist. A report is a
   deliverable, not a lab notebook: it should read coherently to someone who
   hasn't followed the session-by-session log.

## Rules — read before writing any code

1. **Scripts, not notebooks, for anything that's a result.** Every real
   investigation step is a standalone Python script under `experiments/`,
   numbered in the order it was built (`01_...py`, `02_...py`, ...). Each
   script is self-contained, runnable on its own, and writes structured
   output (CSV/JSON/HTML plots) to `experiment_results/NN_name/`. Notebooks,
   if used at all, are for human ad hoc exploration ONLY — never cite a
   notebook run as a finding, and any verification step must also be a
   script.
2. **Log every session as a new file in `research_log/`, add its row to
   `RESEARCH_LOG.md`'s index table, and summarize it in `RESEARCH_SUMMARY.md`
   in the same sitting.** All append-only. The log entry (its own
   `research_log/NNN-slug.md`, next number, `## YYYY-MM-DD — title` header):
   what was run, what was found (headline numbers — point to the result dir
   for full tables), what it implies, what's open/next. Add one
   `| date | [title](research_log/NNN-slug.md) |` row to `RESEARCH_LOG.md`
   for it. The matching summary section: 3-5 bullets, headline
   `Found`/`Implies` facts only, no methodology or open/next, ending with a
   link to the log file. If a later session contradicts an earlier finding,
   add a new entry (new file + index row + summary section) saying so —
   don't edit history in any of these.
3. **Reports are numbered scripts too, under `reports/`, output to
   `report_results/NN_name/`.** Same reproducibility bar as `experiments/`:
   re-running a report script regenerates the report from current experiment
   output, it isn't hand-edited after the fact. A report script may re-read
   `experiment_results/` CSVs/JSON directly rather than recomputing anything.
4. **Long-running scripts must write progress somewhere the user can tail
   live.** Anything that can take a while (data pulls, batch inference,
   full-dataset sweeps) should stream progress (item counts, current
   file/id, timestamps) to a log file under `experiment_results/NN_name/` as
   it runs, not just print a final summary — the user otherwise has no way
   to tell a slow script from a hung one.
5. **Verify data provenance before trusting a comparison.** Before comparing
   two supposedly-distinct sources (two model versions, two time periods,
   two datasets), add a cheap sanity check (hash comparison, row-count
   check, spot-check) that would catch the two actually being the same data
   — this class of bug is easy to hit and easy to miss silently.

### Domain-specific rules

{{Add rules specific to this research's domain here — e.g. data-access
constraints, a cache/lookup gotcha, a known-bad data source to avoid. Delete
this placeholder line once at least one real rule is added, or delete the
whole subsection if none apply yet.}}

## Where things live

```
{{RESEARCH_DIR_NAME}}/
├── AGENT_ENTRYPOINT.md          <- you are here
├── RESEARCH_SUMMARY.md          <- bullet-point headlines per session, read next
├── RESEARCH_LOG.md              <- index (date + title) into research_log/, read this to find an entry
├── research_log/
│   └── NNN-slug.md               <- one file per session, full detail
├── RESEARCH_PLAN.md             <- open ideas to explore, by priority
├── experiments/
│   ├── common.py                <- shared paths, disk-cached lookups, etc.
│   ├── 01_....py                 <- one file per experiment, numbered in build order
│   └── ...
├── experiment_results/
│   └── NN_script_name/          <- one dir per experiment script, its CSV/JSON/PNG/HTML output
├── reports/
│   ├── 01_....py                 <- one file per report, numbered in build order
│   └── ...
└── report_results/
    └── NN_report_name/          <- one dir per report script, its rendered output
```

Data location(s): {{DATA_LOCATION — where source data lives or how it's
obtained; note any access constraints}}.

## Current state (as of {{DATE}} — check RESEARCH_LOG.md for anything newer)

{{Leave empty until the first session produces findings. Once populated,
keep this section to a few headline bullets — same bar as a
RESEARCH_SUMMARY.md entry — and update it each session so a fresh agent
gets the current picture without reading the whole log.}}

See `RESEARCH_PLAN.md` for open threads and what's queued next.
