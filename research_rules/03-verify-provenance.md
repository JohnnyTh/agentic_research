# Rule: verify data provenance before trusting a comparison

Trigger: comparing two supposedly-different data sources (e.g. two model
versions, two time periods, two datasets).

Before comparing two supposedly-distinct sources, add a cheap sanity check
(hash comparison, row-count check, spot-check) that would catch the two
actually being the same data under different names — this class of bug is
easy to hit (a stale symlink, a copy-paste of the wrong path, a re-export
that didn't actually change) and easy to miss silently, since the numbers
still "look plausible" on their own. If this research hits a real instance
of it, log the incident and encode the fix as a reusable guard in
`experiments/common.py` (e.g. a `_check_not_duplicate_dump`-style function),
not just a one-off check in the script that found it.
