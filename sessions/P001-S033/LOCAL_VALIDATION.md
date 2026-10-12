# P001-S033 local validation

Run in the session container on branch `claude/great-bohr-jtk26y` before the PR:
- `python3 scripts/validate.py`;
- `python3 -m unittest discover -s tests -v`;
- the single pre-frozen auxiliary run `python3 -I experiments/s033_t2_check.py`, with output archived verbatim in [T2_CHECK_OUTPUT.txt](T2_CHECK_OUTPUT.txt): 64/64 PASS, spread branches not exercised.

The validator and unittest results are recorded in the closeout as observed. Local PASS is not hosted CI. The required hosted evidence is the final-head research-integrity PR run and job, observed separately after the head exists.

Observed locally (Python 3, session container) on the final content before the PR push:
- `scripts/validate.py` printed `PASS: structure, JSON, quantifiers, witness semantics, statuses, source links, prompt hash, one successor and observed CI receipts`.
- `unittest discover -s tests` printed `Ran 7 tests ... OK`.
