"""Stats computation only. Reads experiment_results/, returns a stats dict.
No HTML, no rendering, no I/O beyond reading its own inputs.
"""


def compute_stats() -> dict:
    # Read whatever experiment_results/NN_.../*.csv|json this report
    # synthesizes, and return a plain dict of the numbers the report needs.
    return {"example_metric": 0}
