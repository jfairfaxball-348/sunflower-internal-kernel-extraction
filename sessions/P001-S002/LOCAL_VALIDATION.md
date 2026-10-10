# P001-S002 validation methodology

The mathematical work is symbolic and analytical, with no new experiment or Lean implementation. The only numerical computations were exact rational arithmetic for the explicitly displayed constant, not mathematical population enumeration.

Required repository commands: `python3 scripts/validate.py`; `python3 -m unittest discover -s tests -v`. The execution environment's local container has no working GitHub DNS, so it could not obtain the *complete* live repository tree for faithful local execution. Do not record fabricated local passes. The repository's hosted GitHub Actions `validate` job runs those two commands in the actual exact branch checkout and must be inspected as the substitute evidentiary check **before** merge. Their success is structural/semantic CI, not mathematical proof. Incoming prompt SHA-256 is recorded in INPUT_MANIFEST.json; the repository validator checks it. Run/job IDs for final-head and main checks are external receipts, necessarily subsequent to the file commit.

First actual hosted PR run `38057391307`, job `114228553537`, completed **success** for exact branch head `3cf6f348176579a23fb6b0fb5d095f5f91250dcc`. It ran the record validator and fixed semantic tests. Recheck the outgoing final head and main after merge: this file does not self-certify them.
