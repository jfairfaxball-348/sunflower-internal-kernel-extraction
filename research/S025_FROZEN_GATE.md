# P001-S025 — pre-analysis frozen GLOBAL_EDGE_DICHOTOMY_512

**FROZEN MATHEMATICAL CANDIDATE, NOT A THEOREM.** Date 2026-10-11; archived fresh owner invocation at child branch commit `492f9752a7b10bffd4c2a8e04f41ca1374dd2417`. This specification is committed BEFORE any S025 mathematical proof/counterexample report or audit.

For **every** integer m>=3, every finite *simple* triple family F and **every** packing P=(B_i)_(i=1)^t of pairwise **edge-disjoint**, original **complete m-petal triple sunflowers** in F with arbitrary exact original cores of size 0,1,2, there is a subfamily H of **individual** triples in U(P) with

    |H| >= t/(512*m^2)

and EXACTLY ONE of the following two certificate architectures:

**A (global common-core / EMPTY absent).** A vertex v belongs to every edge of H; every realised exact 2-pair has at least m distinct third vertices IN H, and every realised exact singleton {x} has an m-matching in the final residual link H({x}). EMPTY is unrealised. (If H has <=1 edge, both exact-kernel conditions are vacuous; v belongs to its edge.) No entire-block restriction.

**B (globally spread / actual EMPTY).** H contains two disjoint edges, hence EMPTY is realised, and there is a matching of >=m pairwise disjoint triples IN H. Every realised exact 2-pair has at least m distinct third vertices IN H, and EVERY realised singleton {x} has an m-matching in the FINAL residual link H({x}). No assumption that its edges can be separated into individually certified local hub slices; all original light labels can be shared.

The A and B outputs are alternatives, NOT outputs to be united, and each alone meets the SAME t/(512*m^2) absolute budget. These hypotheses are stricter than merely demanding an arbitrary valid H without a globally common vertex or EMPTY: an intersecting but non-star H would not automatically satisfy either branch. The quantifiers therefore make this an ambitious, independently falsifiable sufficient strengthening of frozen S024 DIRECT_PARTIAL_EDGE_512, **not** an equivalence or a theorem.

For clarity the intended budgeting proof can assign a nonnegative partition t=t_A+t_B into **original** block weights, and establish a certified A output >=t_A/(256m²) OR a certified B output >=t_B/(256m²). Since max(t_A,t_B)>=t/2, this would imply one >=t/(512m²); the partition and both local lower bounds are themselves UNPROVED. The proof may instead establish the full 512 inequality directly. No uncharged collision deletion or extra m² loss is permitted. Original Q={x: number of ORIGINAL block supports containing x >m}, with all original light/heavy labels fixed throughout; no assumption that light labels are private.

Boundaries: t=0 gives H=empty (A vacuous, choose any v only when a vertex exists, otherwise accept empty separately). 1<=t<=512m²: one edge, with any vertex in it, satisfies A and the literal size inequality. At m=2, take H=F for the ORIGINAL TIK question, outside this m>=3 gate. If any step fails, report the FIRST exact false or unproved quantified implication and check TRUE final-H 2/1/EMPTY certificates on parametric positive-dense controls. The original all-fixed-k TIK, R3, DIRECT_PARTIAL_EDGE_512 and this new dichotomy are UNPROVED at freezing; universal whole-block BSEL is previously REFUTED by S023.

No extra mathematics gate, computation without advance immutable specification, N1/N2, Lean, manuscript, parent mathematical S001, outreach or publication.