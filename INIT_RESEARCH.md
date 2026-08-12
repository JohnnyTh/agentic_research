# Init procedure (run once, then delete this file)

You're bootstrapping a new research from the generic template. Before
writing any experiment code, run this interview with the user, then fill in
`AGENT_ENTRYPOINT.md`'s placeholders from the answers.

## Questions to ask

1. **Goal.** What question is this research trying to answer, in one
   paragraph? What decision or action does the answer inform?
2. **Domain.** What system/codebase/dataset does this study? Is there
   existing background documentation to link instead of re-explaining it
   here?
3. **Data.** Where does the data live, or how is it obtained? Any access
   constraints worth encoding as a rule (network/auth limits, size, a lookup
   that needs caching, a known-bad source to avoid)?
4. **Domain gotchas.** Any known traps specific to this domain the agent
   must not trip over? (e.g. a cache that poisons itself on a bad first
   call, a data-provenance issue seen before, a rate limit.) These become
   new files under `research_rules/`, numbered to continue the existing
   sequence.
5. **First step.** What does the first experiment look like — concrete
   enough to name `experiments/01_....py` and write the first
   `RESEARCH_PLAN.md` entry?
6. **Directory name.** What should this research's directory be called (used
   in `AGENT_ENTRYPOINT.md`'s path map)?

Don't treat this as a rigid form — ask conversationally, follow up on vague
answers, and skip a question if the user already answered it unprompted.

## After the interview

1. Fill every `{{PLACEHOLDER}}` in `AGENT_ENTRYPOINT.md` with the answers.
   Add any real domain rules from Q4 as new `research_rules/NN-name.md`
   files and a row each in `AGENT_ENTRYPOINT.md`'s rules table.
2. Add the first entry to `RESEARCH_PLAN.md` (index row + matching
   `research_plan_items/001-slug.md` file) from Q5's answer — enough to
   start `experiments/01_....py` immediately.
3. Delete this file (`INIT_RESEARCH.md`) — its job is done, and a later
   fresh-session agent seeing it present would wrongly think init is still
   pending. Also delete the `<!-- INIT_RESEARCH.md not run yet? -->` comment
   near the top of `AGENT_ENTRYPOINT.md`.
4. Leave `RESEARCH_LOG.md`, `research_log/`, `research_plan_items/`, and
   `report_results/` untouched (empty) — the first real session populates
   them.
