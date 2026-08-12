# agentic_research — template

A template for bootstrapping a new agent-guided research effort: a fresh
Claude Code (or similar) session can pick up an in-progress research from
just the files in this repo, with no prior conversation context.

## Start a new research

1. Copy this directory to a new location/name (or use it as a git template),
   e.g. `cp -r agentic_research my-new-research && cd my-new-research`.
2. Open a fresh agent session in the new directory and tell it to read
   `INIT_RESEARCH.md` — it will interview you (goal, domain, data location,
   known gotchas, first experiment) and fill in `AGENT_ENTRYPOINT.md` from
   your answers, then delete `INIT_RESEARCH.md`.
3. From then on, every new session starts by reading `AGENT_ENTRYPOINT.md`.

## What's in here

- `AGENT_ENTRYPOINT.md` — the map: what the research is, the four stages
  (define → run & explore → thesis formulation → report), the write-approval
  gate, the subagent-delegation pattern, the rules table, and where things
  live.
- `RESEARCH_LOG.md` + `research_log/` — append-only index (date + title +
  headline) into one file per session, where full detail lives.
- `RESEARCH_PLAN.md` + `research_plan_items/` — index (status + priority +
  headline) into one file per open item; finished items are removed, not
  archived (the log is the durable record).
- `research_rules/` — one operational rule per file, read on demand rather
  than all at once.
- `experiments/` + `experiment_results/` — one numbered, standalone script
  per investigation step, each writing structured output to its own result
  dir.
- `reports/` + `report_results/` — one numbered script per synthesized,
  human-facing writeup built from one or more experiments' results.

This structure is itself expected to evolve — treat it as a first iteration,
not a fixed spec.
