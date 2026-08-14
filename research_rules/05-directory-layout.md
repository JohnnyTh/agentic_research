# Reference: directory layout

Trigger: need to locate a specific script/module/output dir, or orient in
a new session.

```
{{RESEARCH_DIR_NAME}}/
├── AGENT_ENTRYPOINT.md          <- map + rules manifest, read first
├── RESEARCH_LOG.md              <- index (date + title + headline) into research_log/
├── research_log/
│   └── NNN-slug.md               <- one file per session, full detail
├── RESEARCH_PLAN.md             <- index (status + priority + headline) into research_plan_items/
├── research_plan_items/
│   └── NNN-slug.md                <- one file per open item, full detail
├── research_rules/
│   └── NN-name.md                <- one operational rule per file (this file's siblings)
├── experiments/
│   ├── common.py                <- shared paths, disk-cached lookups, reusable helpers
│   ├── 01_....py                 <- one file per experiment, numbered in build order
│   └── ...
├── experiment_results/
│   └── NN_script_name/          <- one dir per experiment script, its CSV/JSON/PNG/HTML output
├── reports/
│   ├── common.py                 <- report_results path helper (result_dir)
│   ├── NN_name_report.py         <- thin orchestrator, one file per report, runnable
│   ├── NN_name/
│   │   ├── compute.py             <- stats computation only
│   │   ├── render.py              <- HTML/formatting only, no computation
│   │   └── collect.py             <- optional: data gathering/preprocessing,
│   │                                 re-runnable, tolerant of source drift
│   └── ...
└── report_results/
    └── NN_report_name/          <- one dir per report script, its rendered output
```

Data location(s): {{DATA_LOCATION — fill in during INIT_RESEARCH.md, or
point here to wherever experiments/common.py resolves paths from}}.
