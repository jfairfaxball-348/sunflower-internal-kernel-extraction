# P001-S006 — Sunflower-Block Packing and Internal Kernel-Compatibility Feasibility

**ONE bounded, source-first child research session — DRAFT, NOT EXECUTED**

## 1. Programme authority and owner decision

Work in:

**Child P001:**  
https://github.com/jfairfaxball-348/sunflower-internal-kernel-extraction  
Repository ID: `1412820282`

**Permanent parent programme:**  
https://github.com/jfairfaxball-348/sunflower-structures-programme  
Repository ID: `1412469441`

The owner has selected:

**Route A — Continue R3 under a genuinely different research approach.**

The proposed method is **SUNFLOWER_BLOCK_COMPATIBILITY**.

This prompt is presented for approval only. Execute exactly ONE bounded P001-S006 session only when the owner subsequently invokes the approved prompt explicitly.

Do not execute P001-S007, parent S001, another mathematical route, a paper, or a new repository.

No automatic mathematical pivot is authorised.

## 2. Entry and reconciliation

Pin live `main` in both repositories. Inspect all open and merged pull requests, intervening commits, actual GitHub Actions runs and jobs, and the verified P001-S005 child-to-parent registration.

Current reference checkpoints (verify again at entry):

- Child main: `79fbbbc35fec42fdde0ada766f892ab83090615c`
- Parent main: `c1c9aa6a0d36e4dc4170713ada36453fa21757a5`
- Child P001-S005: COMPLETE
- Parent mathematical S001: NOT EXECUTED
- Child P001-S006: NOT EXECUTED

Read child `AGENTS.md`, `authoritative/START_HERE.md`, `STATE.json`, `SESSION_PROTOCOL.md`, `STANDARDS.md`, `project_manifest.json`, exact `TARGET.md`/`TARGET.json`, source and novelty records, claims, decisions, experiments, formalisation, publication, validation receipts and the complete S005 closeout and five-session audit.

Read S001–S004 negative analyses, particularly:

- `research/R3_FEASIBILITY.md`
- `research/L_AVG_FEASIBILITY.md`
- `research/S003_CHARGE_SPEC.md`
- `research/S003_CHARGE_ANALYSIS.md`
- `research/S004_AUDIT.md`
- `research/S005_PROGRESS_CORRECTION_AUDIT.md`
- `research/S005_N1_TRIAGE.md`

Read live parent authority, charter, research-integrity, novelty, formalisation and publication policies, tournament `FINAL_DECISION`, milestone, novelty, paper and project registers, and `programme/P001_REGISTRATION.json`.

Confirm S006 uniqueness.

Archive the exact incoming executable P001-S006 owner prompt verbatim in `sessions/P001-S006/INPUT.md`, recording its SHA256 and archival evidence **before replacing** `sessions/NEXT_SESSION.md`.

Record the owner's Route A decision separately. Do not treat this choice as authorisation for unlimited proof exploration.

## 3. Immutable mathematical baseline

The programme headline remains the **Erdős–Rado Sunflower Conjecture**.

The first-paper objective remains quantitative internal-kernel sunflower extraction, TIK.

TIK status:

- Mathematical: `SOURCE_POSED_CONJECTURE`
- Open status: `STRONG_EVIDENCE_OPEN`
- Novelty: `NOVELTY_UNCERTAIN`

The restricted R3 target asks whether there exists an absolute constant `c > 0` such that, for every integer `m >= 2`, every `n >= 3`, and every finite 3-uniform family `F` on `[n]`, some `H ⊆ F` satisfies:

`|H| >= c * m^(-3) * |F|`

and every intersection `K = A ∩ B` of distinct `A, B ∈ H` is the exact kernel of an `m`-petal sunflower entirely inside `H`.

The kernel may be empty. The selected pair need not belong to the witnessing sunflower.

The constant cannot depend on `m`, `n` or `F`.

The known JJSW26 rank-three results are:

- Internal retention: `(24m)^(-8)`
- External retention: `(600m)^(-3)`, with witnesses in ambient `F`

R3 remains unproved by this project, and its exact literature status is `STATUS_UNCERTAIN`.

No project positive extraction theorem, Lean verification, paper, publication or algorithm has been obtained.

### Retired methods

P001-S003/S004 retired the precise `L_AVG` and `B_CHARGE` fixed-colour-palette mechanisms following a provisionally analytically supported tripartite counterexample.

Those results were checked by the same assistant, not a genuinely independent mathematical reviewer.

They do not refute R3 or TIK.

**S006 must not reuse these methods under different names.**

## 4. One objective

`BLOCK_COMPATIBILITY_FEASIBILITY_GATE`

Investigate whether a deterministic decomposition into complete sunflower blocks can support a quantitative internally valid block selection.

Unlike earlier colour-based approaches, this route starts with already existing, complete `m`-sunflowers. Each selected block comes with its own witnessing sunflower intact.

The unresolved issue is whether intersections between different blocks can be supported without sacrificing too much density.

**One candidate lemma is frozen for S006: BSEL.**

The task is to determine its mathematical feasibility through source-first comparison and one bounded analytical proof-or-counterexample investigation.

Do not assume BSEL is true, original or publishable.

## 5. Frozen candidate: Block-Selection Lemma (BSEL)

Let `m >= 3`, let `F` be a finite simple 3-uniform set family, and suppose

`B_1, ..., B_t`

is any collection of pairwise **edge-disjoint** subfamilies of `F`, each consisting of exactly `m` distinct triples forming an `m`-petal sunflower.

The blocks may have different kernels. Their vertex sets need not be disjoint.

They may have kernels of size `0`, `1` or `2`.

For a set of block indices `J ⊆ {1,...,t}`, put:

`U(J) = union of B_i over i ∈ J`.

Call `J` *kernel-compatible* if, for every distinct `A,B ∈ U(J)`, there are `m` distinct edges of `U(J)` whose pairwise intersections equal exactly `A ∩ B`.

The sunflower witnessing an intersection may use edges from multiple blocks and need not contain `A` or `B`.

### BSEL candidate

Does there exist an absolute constant `gamma > 0`, independent of all parameters, such that **every** such edge-disjoint packing admits a kernel-compatible index set `J` with:

`|J| >= gamma * m^(-3) * t`?

The inequality is literal, including its integer ceiling.

For `t = 0`, the empty selection is admissible.

No requirement is imposed that all selected blocks have the same kernel, a common vertex colouring or a common projected intersection pattern.

### Strength and limitations

BSEL is potentially stronger than R3 because it retains complete blocks from an arbitrary prescribed packing.

BSEL may therefore be false even if R3 is true.

If a valid counterexample exists, it invalidates this exact route only.

Do not weaken `every packing` to `some convenient packing`, allow partial blocks, or introduce a modified selection objective during S006. Those would be different lemmas requiring a separate authorised session.

## 6. Why BSEL would matter

The known sunflower-decomposition argument partitions a 3-uniform family into edge-disjoint `m`-sunflowers, leaving a remainder of fewer than `(3m)^3` triples.

An explicit published version appears in Girão, *Defective Coloring of Hypergraphs* (2024), Lemma 9.

This decomposition is **prior art**, not a new project theorem.

Suppose BSEL held with constant `gamma`.

For an arbitrary family `F`, take such a decomposition. Write `P` for the union of complete blocks and `R` for its remainder.

Then:

`|R| < 27m^3`.

If `F` is nonempty and `|F| < 54m^3`, selecting one triple gives an internally valid singleton meeting an `m^(-3)` density guarantee with constant `1/54`.

Otherwise:

`|P| >= |F|/2`.

Applying BSEL to the packed blocks would produce an internally valid subfamily of size at least:

`(gamma/2) * m^(-3) * |F|`.

The empty-family case is trivial, and `m = 2` is already solved by taking `H = F`.

Consequently, BSEL would imply R3 with a constant no smaller than the conditional choice:

`c = min(1/54, gamma/2)`.

**S006 must independently check the exact validity, constants and quantifiers of this conditional reduction before relying on it.**

The reduction is not a proof of BSEL or R3.

## 7. Mandatory N1 source-first gate

Before attempting the block-selection argument, investigate the exact published mathematical frontier.

Start with:

1. Janzer–Jin–Sudakov–Wu, *Sunflowers and Ramsey Problems for Restricted Intersections*, Combinatorica (2026), especially Theorems 1.5–1.7 and Section 6.

2. António Girão, *Defective Coloring of Hypergraphs*, Random Structures & Algorithms (2024), especially Lemma 9 and its proof.

3. Kupavskii, *Delta-System Method: A Survey*, Section 0.6.3, and relevant earlier delta-system decomposition and packing results.

4. Relevant 2025–2026 sunflower, matching, packing, covering, restricted-intersection and bounded-VC results, comparing their exact hypotheses and conclusions.

Search specifically for:

- Edge-disjoint sunflower packings with large compatible subcollections.
- Delta-system decompositions with intersection-closure requirements.
- Unions of sunflowers whose cross-intersections admit internal witnesses.
- Matching-cover or hypergraph packing theorems that may imply BSEL.
- Known obstructions to preserving whole sunflower blocks.
- Exact rank-three internal extraction results.

For every serious comparator, record author, title, version/date, theorem or lemma locator, precise quantifiers, witness membership, and whether full text or only an abstract was inspected.

Distinguish:

- Known sunflower decomposition.
- Known matching or packing bounds.
- A possible new cross-block compatibility argument.
- Exact BSEL.
- R3 and full TIK.

A search no-hit is **not** evidence that BSEL is novel or that R3 is confirmed open.

Write:

`research/S006_N1_BLOCK_COMPATIBILITY.md`.

If a source already proves BSEL or supplies a decisive counterexample, record it faithfully and terminate the analytical attempt. Do not present a rediscovery as an original theorem.

Otherwise retain `NOVELTY_UNCERTAIN` and proceed only with the bounded investigation below.

## 8. One bounded mathematical investigation

Freeze the exact BSEL statement before doing mathematics.

Investigate only the following obligation:

**Can sufficiently many complete sunflower blocks be retained simultaneously while satisfying all newly realised exact intersection kernels?**

The key distinction is:

- Internal intersections within a selected block are automatically witnessed by that block.
- Cross-block intersections may create additional kernels for which the original block certificates provide no automatic witness.

The analysis must explicitly distinguish all three levels:

- Pair kernels, requiring at least `m` distinct third vertices inside the final union.
- Singleton kernels, requiring an `m`-matching in the residual link graph of the final union.
- Empty kernel, requiring an `m`-matching of triples inside the final union whenever empty intersections occur.

Use a deterministic block-interaction or kernel-compatibility argument, not colour certificates or palette capacity.

One analytical proof architecture may be attempted. A legitimate counterexample investigation may challenge the same frozen lemma.

Do not launch a succession of alternative techniques if the selected approach fails.

A mathematical conclusion must be supported by a written proof, explicit counterexample, or precise account of the first unresolved implication.

If BSEL is too strong, identify exactly which quantifier or block-union requirement fails.

Do not repair it within S006.

### Required tests of reasoning

Check the lemma against known symbolic structures, including complete tripartite families and the standard transversal obstruction, without treating a successful special case as a universal proof.

Ensure that:

- The packing blocks are edge-disjoint, not necessarily vertex-disjoint.
- The selected union consists of whole blocks.
- The selected pair need not be a sunflower witness.
- All cross-block intersections are treated.
- Empty kernels are not omitted.
- Constants remain independent of the ground-set size and `m`.
- No ambient-family matching is silently substituted for a final-union matching.
- A large block collection alone does not imply compatibility.

No fresh enumeration, simulation, random experiment, Monte Carlo study, unbounded computational search or Lean work is authorised in S006.

Symbolic counterexample analysis is permitted.

## 9. Bounded success and failure outcomes

Classify the outcome as exactly one of:

**A — PROVISIONAL_BSEL_PROOF**

A complete written mathematical argument appears to establish the exact frozen BSEL with a positive absolute constant, subject to genuinely independent mathematical scrutiny.

Also document the conditional deduction of R3 and its exact constant.

Do not promote R3 to an independently established original theorem, N2-complete result, Lean verification or publication-ready paper.

The next session must be a distinct proof scrutiny and source/novelty gate.

**B — BSEL_COUNTEREXAMPLE**

An exact finite or symbolic parameterised counterexample defeats the quantified block-selection statement.

State the failed quantifier and show why no sufficiently large compatible whole-block selection exists.

Keep R3/TIK unchanged.

Do not automatically try a weaker existential-packing lemma.

**C — RESTRICTED_BSEL_ONLY**

One rigorously established restricted subcase is obtained, but the universal statement remains unresolved.

Record its precise hypotheses, constants, source comparison and why it falls short of R3.

No originality or journal-worthiness claim without a proper N1 and later N2.

**D — NO_DECISIVE_PROGRESS**

Neither proof nor counterexample is established within the one bounded analytical gate.

Identify the first missing estimate and whether this method remains credible.

Do not continue a speculative series of block-compatibility sessions without a new explicitly approved obligation.

**E — PRIOR_ART_OR_SCOPE_KILL**

Source evidence establishes that the target is already known, materially superseded, equivalent to an unsuitable existing claim, or inadequately distinguished for a useful research objective.

Document and close the route without mathematical promotion.

## 10. Research integrity

Keep separate:

- Mathematical correctness.
- Source attribution.
- Novelty.
- Independent review.
- Formal verification.
- Publication status.
- Constructive algorithms.
- Complexity claims.
- Potential applications.

All achieved arguments in this session are AI-assisted unless separately evidenced otherwise.

A self-check is not genuinely independent mathematical review.

Even a complete apparent BSEL proof must undergo exact-result N2, rigorous independent scrutiny, and subsequent formalisation approval before publication promotion.

Do not infer an efficient algorithm from an existence proof.

No researcher contact, paid resources, journal/arXiv/Palomar submission, manuscript, public announcement, rename, new child repository, or parent mathematical session.

## 11. Required research and governance outputs

Update all affected child records, including:

- `research/S006_N1_BLOCK_COMPATIBILITY.md`
- `research/S006_BLOCK_COMPATIBILITY_SPEC.md`
- `research/S006_BLOCK_COMPATIBILITY_ANALYSIS.md`
- `research/CLAIMS.json`
- `research/NOVELTY_LEDGER.md`
- `research/SOURCES.json`
- `research/SEARCH_LOG.md`
- `research/DECISIONS_AND_RISKS.md`
- `research/TARGET.md`, only where a correctly scoped investigative status update is necessary
- `sessions/PROGRESS_AUDITS.md`
- `sessions/HISTORY.md`
- `sessions/AI_USE.md`
- `authoritative/STATE.json`
- `project_manifest.json`
- `validation/GITHUB_EVIDENCE.json`
- `sessions/P001-S006/ENTRY_EVIDENCE.json`
- `sessions/P001-S006/INPUT.md`
- `sessions/P001-S006/INPUT_MANIFEST.json`
- `sessions/P001-S006/CLOSEOUT.md`
- `sessions/NEXT_SESSION.md`

Preserve historical source and failure records without retroactively changing their meaning.

The outgoing handoff must contain one complete, standalone P001-S007 prompt **or** a concrete human decision gate. It must state the exact mathematical outcome, status restrictions, authority, evidence, entry conditions and stop rule.

Do not execute that successor.

## 12. Validation, publication to GitHub and closeout

Run:

`python3 scripts/validate.py`

`python3 -m unittest discover -s tests -v`

Use one child research branch and one pull request for S006.

Require a successful hosted `validate` job on the actual final PR head before merging. Verify the reviewed head SHA and all relevant workflow/job conclusions.

Merge only if authorised and the required checks are green.

Independently verify the actual merged child `main`, merged PR status and successful merged-main workflow/job.

Do not invent local test results, hosted CI receipts or independent proof scrutiny.

Update parent registration **only through a separate verified status PR** referencing the exact child merge, successful main CI and properly scoped mathematical outcome.

Do not execute the parent mathematical S001 session through status registration.

**STOP after exactly P001-S006.**

The guiding principle is to investigate whether complete sunflower blocks provide a structurally different path to internal witness retention, while abandoning the candidate promptly if its exact quantitative claim is false, already known or inaccessible within the bounded session.