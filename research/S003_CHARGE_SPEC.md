# P001-S003 — frozen charge target (pre-analysis specification)

Frozen for the sole bounded L_AVG_HEAVY_LINK_CHARGING slice. This document is a *candidate to test*, NOT a theorem or a reformulation proved equivalent to L_AVG. No experimental computation is authorised.

For m>=3 and an arbitrary finite F of triples, fix lexicographic maximum residual matchings, psi(K), independent M=288m colouring chi, good edges and G_P exactly as in research/R3_FEASIBILITY.md. Write nu for residual matching number, with nu(empty)=0.

Define the **ambient-saturated** edges
A_m(F) = {E in F: nu(F(K))>=m for EVERY proper subset K of E, including K=empty}.
Thus ambient saturation explicitly includes three 2-point residual singleton links, three 1-point residual graph links, and the empty-kernel triple matching; this is a demanding restriction on chargeable edges, not a conclusion about any final palette.

For a fixed colouring and palette P define the **colliding chargeable edges**
D_P = {E in G_P intersect A_m(F): |G_P|>=2}.
Define the **eligible recipient edges**
R_P = union {H: H subset G_P, |H|>=2, and H is internally m-valid}.
An internally valid H requires all exact intersections K of distinct members of H to have nu(H(K))>=m, including the empty kernel; witnesses may be edges other than the selected pair. The union is set-theoretic; an edge is counted once in R_P even if it belongs to many H. Empty union is empty.

**Candidate bounded-multiplicity charge B_CHARGE:** is there an absolute integer B>=1 such that for ALL m>=3 and ALL F there exists, for random chi, a palette-preserving allocation of D_P to R_P with expected total load at most B per *distinct recipient edge*, in the necessary numerical form

    E_chi sum_P |D_P| <= B * E_chi sum_P |R_P| ?           (B_CHARGE)

A pointwise map with at most B preimages for every edge of R_P would be stronger. Unlike L_AVG, the RHS is a union of all *non-singleton* valid subfamilies, not sum of their optimal cardinalities: it can be much larger than sum b_m(G_P). We do NOT use it as a sufficient substitute for L_AVG. The only question here is whether heavy ambient link information guarantees even this weaker charge. A failure here does not logically disprove all conceivable charging schemes.

**Stop criterion:** identify the first exact broken step and a symbolic quantified family, or provide a complete universal proof including all kernel levels and constants. No generic palette-repair claim, repeated selection, all-k target expansion, theorem promotion, enumeration, simulation, Lean or publication.
