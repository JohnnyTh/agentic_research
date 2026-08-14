# {{RESEARCH_NAME}} — agent entrypoint

Read this first if you're picking up this research in a new conversation.
It's a map and a rule index, not a summary of findings — for findings, read
`RESEARCH_LOG.md`'s index table, then open only the `research_log/NNN.md`
files relevant to your current question (don't read the whole
`research_log/` directory — it's split precisely so you don't have to).
Check `RESEARCH_PLAN.md`'s index table for queued/open ideas before starting
new work — like the log, it's split so full item detail lives one-per-file
in `research_plan_items/` (don't read the whole directory, only the files
relevant to your question).

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
   measured, against what data, with what success signal.
2. **Run & explore** — implement and run the experiment as a numbered script
   under `experiments/`, inspect its output, iterate until the result is
   trustworthy. Do this via a dispatched subagent, not inline — see
   "Delegate experiment iteration to a subagent" below.
3. **Thesis formulation** — once one or more experiments produce results,
   step back and state what they imply for the research goal: a short,
   falsifiable claim ("X causes Y", "model A beats model B on Z"), grounded
   in specific experiment output, not vibes.
4. **Report** — write a self-contained, human-facing synthesis of one or
   more theses as a numbered script under `reports/` (e.g. `01_report.py`),
   modeled on prior reports in `report_results/` if any exist. A report is a
   deliverable, not a lab notebook — it should read coherently to someone
   who hasn't followed the session-by-session log.

   Stats computation, HTML formatting/rendering, and report prose/wording
   must live in separate files under a `reports/report_components_NN_name/` package
   (`compute.py`, `render.py`) — never inline together in the orchestrator
   script. This is a requirement, not a suggestion: see
   `research_rules/06-report-separation.md`. If the report needs its own
   data-collection/preprocessing beyond reusing an `experiments/` script's
   output, that lives in `reports/report_components_NN_name/collect.py`, checked in alongside
   the report and written to be re-run — not a one-off throwaway, and not
   hardcoded to today's data paths/shape (see the same rule file for why).

## Writes to `RESEARCH_LOG.md` / `research_log/` / `RESEARCH_PLAN.md` need a human go-ahead

**Don't write a log entry or edit `RESEARCH_PLAN.md` just because a stage
finished.** These are checkpoints the human chooses, not an automatic
side-effect of running an experiment:

- After a subagent's stage-2 report comes back, or you've formed a thesis,
  *propose* the log entry / plan addition in your reply — don't write the
  file yet. Wait for the human to say "log it" / "add it to the plan" (or
  otherwise clearly sign off) before writing.
- Exception: the human can pre-authorize a batch ("log everything from this
  session at the end") — follow what was actually asked, not the default.
- This applies to `RESEARCH_PLAN.md` edits too: propose the candidate line,
  don't add it unqueued. An idea worth remembering but not yet approved can
  be held in your reply, not the file — it isn't lost, it just isn't
  written until asked for.

Once approved, the mechanics are unchanged: one file per session under
`research_log/`, next number, `## YYYY-MM-DD — title` header; add a row to
`RESEARCH_LOG.md`'s index (see headline standard below); append-only — if a
later session contradicts an earlier finding, add a new entry saying so,
don't edit history.

### Headline standard for `RESEARCH_LOG.md`'s index

There's no separate summary file — the index table's headline column is the
*only* per-entry summary that exists, so it has to let a future session
judge relevance without opening the full file. A vague headline defeats the
entire point of the split:

- **Name the subject and the result, not the activity.** Bad: "tried a new
  clustering approach." Good: "colour-split clustering drops agreement
  88.8%→68.5%." It must contain the number or verdict that makes this entry
  distinguishable from other entries on a related topic — not something
  equally true of half the log ("ran experiment NN", "investigated X").
- **Include the entity/metric a future search would grep for** — a
  category name, script number, metric name — whatever term someone
  scanning for "anything about accuracy" or "anything about category X"
  would type.
- **State corrections as corrections, explicitly** — if this entry reverses
  or narrows an earlier one, the headline says "correction: ...".
- **One line, one clause.** Two unrelated findings from one session get two
  index rows pointing at the same file, not one compound headline that
  hides the second finding from a search matching only the first clause.

## Delegate experiment iteration to a subagent

Stage 2 is where a session's context balloons: write script, run, inspect
output, fix a bug or tweak the approach, run again — often several rounds
per experiment. None of that iteration is worth keeping in the master
session's context once the script is trustworthy — only the final numbers
and interpretation get cited going forward. So:

1. **Default: stage 2 runs in a dispatched subagent, not inline.** Once an
   experiment is defined (stage 1 has produced a concrete script name, what's
   measured, what success looks like), dispatch a subagent to implement, run,
   debug, and iterate on it, rather than doing that work in the master
   session. Only skip dispatch for a script you're confident needs zero
   iteration.
2. **Dispatch prompt should point the subagent at:** the specific rule
   files it needs from `research_rules/` (below — pick by what the
   experiment actually does, don't just say "read research_rules/"), the
   experiment number/name to use, the concrete question/success signal from
   stage 1, and any prior scripts to reuse code from (e.g.
   `experiments/common.py`, or "reuse NN's indices like MM did from NN").
   The subagent should iterate internally until the script runs cleanly and
   the result looks trustworthy — that back-and-forth stays in its own
   context, never the master's.
3. **The subagent returns a short structured report, not a transcript:**
   script path + result dir written; the headline finding; any gotcha worth
   flagging (provenance risk, skipped/unresolvable-item counts, data-scope
   caveats); and open questions it hit but didn't resolve (candidates to
   propose for `RESEARCH_PLAN.md` — still needs human sign-off per the gate
   above). The master session doesn't need intermediate runs, stack traces,
   or fix history.
4. **After dispatch, the master session's job** is to hold the dispatch spec
   and report, propose the log/plan writes (per the gate above), and decide
   the next experiment — not to carry scripts, stdout, or fix history.
5. **More than one experiment queued → dispatch subagents in parallel**, not
   inline serially.

## Rules — read only the ones your current task triggers

Each rule lives in its own file under `research_rules/` so you only pay for
what you need this session — don't read the whole directory.

| Rule | Trigger | File |
|---|---|---|
| Writing style | always — any prose you write this session | `research_rules/07-writing-style.md` |
| Scripts, not notebooks | writing/citing any finding | `research_rules/01-scripts-not-notebooks.md` |
| Progress logging | script may take a while (batch/sweep) | `research_rules/02-progress-logging.md` |
| Verify provenance | comparing two data sources | `research_rules/03-verify-provenance.md` |
| No cross-import | experiment script needs another's logic | `research_rules/04-no-cross-import.md` |
| Directory layout + data paths | orienting, or locating a script/dir | `research_rules/05-directory-layout.md` |
| Report separation | writing/editing a report script | `research_rules/06-report-separation.md` |

Add domain-specific rule files here as they come up (a data-access
constraint, a cache/lookup gotcha, a known-bad source — from
`INIT_RESEARCH.md`'s "domain gotchas" question or surfaced later), numbered
to continue the sequence above, and add a row to this table pointing at
each one.

## Where things live

```
{{RESEARCH_DIR_NAME}}/
├── AGENT_ENTRYPOINT.md          <- you are here
├── RESEARCH_LOG.md              <- index (date + title + headline) into research_log/
├── research_log/
│   └── NNN-slug.md               <- one file per session, full detail
├── RESEARCH_PLAN.md             <- index (status + priority + headline) into research_plan_items/
├── research_plan_items/
│   └── NNN-slug.md                <- one file per open item, full detail
├── research_rules/
│   └── NN-name.md                <- one operational rule per file, read on demand
├── experiments/
│   ├── common.py                <- shared paths, disk-cached lookups, etc.
│   ├── 01_....py                 <- one file per experiment, numbered in build order
│   └── ...
├── experiment_results/
│   └── NN_script_name/          <- one dir per experiment script, its CSV/JSON/PNG/HTML output
├── reports/
│   ├── NN_name_report.py        <- thin orchestrator, one file per report, runnable
│   ├── NN_name/
│   │   ├── compute.py            <- stats computation only
│   │   ├── render.py             <- HTML/formatting only, no computation
│   │   └── collect.py            <- optional: data gathering/preprocessing,
│   │                                re-runnable, tolerant of source drift
│   └── ...
└── report_results/
    └── NN_report_name/          <- one dir per report script, its rendered output
```

Data location(s): {{DATA_LOCATION — where source data lives or how it's
obtained; note any access constraints}}.

## Current state (as of {{DATE}} — check RESEARCH_LOG.md for anything newer)

{{Leave empty until the first session produces findings. Once populated,
keep this section to a few headline bullets and update it each session so a
fresh agent gets the current picture without reading the whole log.}}

See `RESEARCH_PLAN.md` for open threads and what's queued next.
