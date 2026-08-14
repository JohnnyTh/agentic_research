# Rule: long-running scripts must write progress somewhere the user can tail live

Trigger: any script that can take a while (data pulls, batch inference,
full-dataset sweeps).

Must write to a plain-text log file, not just print a final summary or rely
on a stdout progress bar — a `\r`-based bar (e.g. `tqdm`) doesn't survive a
redirect/pipe, so it's invisible to `tail -f` on a background run and
doesn't count as satisfying this rule on its own (fine to keep alongside
the log file for an interactive foreground run). Concretely:

- Log path: always `result_dir(experiment_name) / "progress.log"` (i.e.
  `experiment_results/NN_script_name/progress.log`) — one fixed name, every
  script, so the user (or a `tail -f` in another terminal) doesn't have to
  go check each script's docstring to find it first.
- Setup: `logger.add(log_path, mode="w")` (loguru, or your logger of choice)
  near the top of `main()`, right after `result_dir(...)` — `mode="w"` so a
  re-run starts a fresh log instead of appending to a stale one from a
  prior attempt.
- What to log, and how often: one info line before the main loop starts
  (what's about to run, expected item count) and then one line every
  `LOG_EVERY_N` items (~every few seconds of work, not every single item —
  pick N so the file doesn't itself become a bottleneck) with a running
  counter (`i/total`) and the current item's identifying key, so a stalled
  run is visible as "counter stopped moving on item X" not just silence.
  A logger like loguru timestamps each line automatically — don't hand-roll
  a `datetime.now()` prefix.
- One line at the end summarizing what was written and where.
- **Log every status/progress/summary message through the logger, never
  bare `print(...)`** — the log-file handler only captures what goes
  through the logger, so a stray `print` for the final numbers is exactly
  the kind of message someone tailing `progress.log` needs and won't see.
  `print` is fine only for output that's the script's actual product piped
  elsewhere (rare here — this package writes CSV/JSON/plots to disk, not
  stdout), not for anything progress- or result-summary-shaped.
