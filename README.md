# Quantitative Internal-Kernel Sunflower Extraction

First-paper project **P001** in the [sunflower structures programme](https://github.com/jfairfaxball-348/sunflower-structures-programme), repository ID **1412469441**. This child repository has ID **1412820282** and owns its mathematical work.

**P001-S000:** bootstrap and mathematical-frontier audit. **No new extraction theorem, Lean verification, manuscript, or publication is claimed.**

The target asks whether every finite k-uniform family F has a subfamily H of size at least c_k m^(-k)|F| such that each intersection of two distinct members of H is the exact kernel of an m-petal sunflower **inside H**. The constant may depend on k only. This is the question in Janzer–Jin–Sudakov–Wu, Combinatorica 46 (2026), article 29, Section 6.

Open status: **STRONG_EVIDENCE_OPEN**, supported by the published question and the source comparison dated 2026-10-10. Novelty: **NOVELTY_UNCERTAIN**; this is not an exhaustive or independently certified open-problem verdict. The rank-three restriction has a separate **STATUS_UNCERTAIN** small-rank novelty assessment.

Start with [authority](authoritative/START_HERE.md), [exact target](research/TARGET.md), [frontier audit](research/FRONTIER_AUDIT.md), [sources](research/SOURCES.json), [claims](research/CLAIMS.json), and [project manifest](project_manifest.json).

The only frozen successor objective is **R3**, a bounded analytical feasibility investigation of rank-three internal extraction. [P001-S001 handoff](sessions/NEXT_SESSION.md) is prepared, **not executed**.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. The checks validate governance and a fixed semantic fixture population; they do not establish the proposed theorem. GitHub Actions uses the same commands. There is no Lean build because no Lean theorem is claimed.

The child manifest records the latest already-observed validated checkpoint, not a self-referential future commit. The parent registration receipt and the GitHub PR/Actions records establish publication and cross-repository status.
