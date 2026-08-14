# Rule: keep prose short and plain, in every artifact

Trigger: always — log entries, plan items, report prose, docstrings, code
comments, progress-log messages, replies in chat. This is a working
document for specialists, not a paper. Favor clarity over completeness.

- **One sentence, one fact.** If a sentence joins two claims with "and" or a
  comma, split it into two sentences.
- **One parenthetical per sentence, and not nested.** A caveat that needs
  its own caveat is a second sentence, not a parenthetical inside a
  parenthetical.
- **State a caveat once.** Don't hedge a hedge ("not just X, though Y,
  unless Z"). Pick the one qualifier that matters and say it plainly.
- **Split compound bullets.** A bullet covering a measurement, a caveat, and
  a next step becomes two or three bullets, or a short sub-list.
- **Plain words over formal ones**: "shows" not "demonstrates," "found" not
  "identified," "use" not "utilize," "about" not "approximately."
- **Keep every number, citation, and caveat.** This rule cuts grammar, not
  content — don't drop a real uncertainty or a real number to make a
  sentence shorter; give it its own sentence instead.

Example rewrite:

> Before: "Rotation being the standout robust axis is a new, specific,
> actionable finding — it argues *against* spending further effort on
> 'widen enrollment rotation-angle coverage' as an embedding-quality fix,
> since this embedding model is far more rotation-robust on average than it
> is blur/occlusion-robust; if TOSTITOS/SWEETART/etc.'s orientation failures
> are real, they're more likely a genuine enrollment-coverage gap than an
> embedding-fragility problem rotation itself causes — though the
> per-visual_id spread above means that conclusion is weaker for whichever
> specific items sit at the high-range end, not a uniform guarantee across
> all items."

> After: "Rotation is far more robust than blur or occlusion on average.
> This argues against widening enrollment rotation-angle coverage as an
> embedding-quality fix. If TOSTITOS/SWEETART's orientation failures are
> real, they're more likely a coverage gap than embedding fragility. That
> conclusion is weaker for the few items with high rotation-drift spread —
> check those individually before generalizing."

Same facts, same numbers, same caveats. Four short sentences instead of one
90-word sentence.
