# Rule: never import one experiment script from another

Trigger: an experiment script needs logic another experiment script
already wrote.

`experiments/NN_*.py` files must not `import` names from another
`experiments/MM_*.py` file (only from `common.py` or other shared modules).
If a later experiment needs logic an earlier one wrote, promote that logic
to `common.py` first, then have both scripts import it from there. Reading
a prior experiment's *output* (a CSV/JSON under `experiment_results/NN_name/`)
is fine and common — this rule is about Python-level coupling between
experiment modules, not about reusing results.
