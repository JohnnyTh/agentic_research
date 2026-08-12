# {{RESEARCH_NAME}} — log index

Index into `research_log/`, one row per session, in chronological order.
The table below is the *only* per-entry summary — its headline column must
be specific enough that a future session can judge relevance without
opening the file; see the headline standard in `AGENT_ENTRYPOINT.md` before
adding a row. Append-only — if a finding is later contradicted or refined,
add a new row/file that says so; don't edit history.

Entries are written, and rows added, only at a checkpoint the human
selects — see the write-approval gate in `AGENT_ENTRYPOINT.md`.

Each `research_log/NNN-slug.md` file uses this format:
- **Date / session**
- **Ran**: script(s) + key inputs/params
- **Found**: headline numbers only — see the linked result dir for full detail
- **Implies**: what this suggests, with appropriate hedging (this is the
  "thesis formulation" stage from `AGENT_ENTRYPOINT.md` — ground it in the
  specific result, don't overreach)
- **Open / next**: what's unresolved or queued (mirror into `RESEARCH_PLAN.md`
  too — don't leave ideas stranded only here)

| Date | Entry | Headline |
|---|---|---|
<!-- | YYYY-MM-DD | [title](research_log/001-slug.md) | one-clause result | -->

<!-- First real entry goes here. Delete this comment once added. -->
