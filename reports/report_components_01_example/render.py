"""HTML/formatting only. Takes a stats dict, returns an HTML string. No stats
computation, no network/file I/O -- editing report wording/layout only
requires opening this file.
"""


def render_html(stats: dict) -> str:
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Example report</title></head>
<body>
<h1>Example report</h1>
<p>Replace this with a real synthesis of one or more experiments' findings.</p>
<p>example_metric: {stats['example_metric']}</p>
</body></html>
"""
