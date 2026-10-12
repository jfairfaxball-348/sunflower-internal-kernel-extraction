# P001-S034 — mathematical second pass (SAME ASSISTANT, NOT independent peer review)

1. Apex partition: a selected F-degree-one pair uniquely identifies one triple; fixing one such pair per e prevents double counting. The pair vertices avoid the apex. Distinct original apex groups partition edges, but supports may overlap.
2. Colouring: Gamma is an ordinary finite simple conflict graph. Greedy proper colouring uses Delta+1 classes. One class carries at least 1/(Delta+1) of TOTAL EDGE MASS, not merely number of apex groups; zero-mass groups are discarded.
3. Theorem B usage: for each G_c (including a graph with 1 edge), S033 yields a nonempty valid L_c with >=|G_c|/(8m^2); lifting c preserves every realised intersection exactly after adjoining c.
4. For |I|>=m, every cross-apex intersection is EMPTY because S_c are disjoint; one edge per component makes an m-matching. Nonempty realised intersections are internal, certified by L_c. Size of union is sum of sizes.
5. For |I|<m, the largest original G_c has >=W/|I|; select only its lift. This avoids cross-apex EMPTY altogether. Even if the graph H' had disjoint edges, the lifted triples meet at c and the m-matching required for the singleton {c} is supplied by the graph's EMPTY case.
6. Spread counterexample m>=3,r=108m²: |D|=2mr; singleton bound r/3, pair bound r/(18m), triple bound r/(108m²). All nonzero pairs have degree at most m, all triples unique. For each x_i, all residual A triples share a_i and all residual B triples share b_i; hence nu=2 exactly, not merely <=2. The original FULL D also has an EMPTY r-matching, so this is a singleton-specific failure. Core-free follows degree-one pair in EVERY edge.
7. The positive H={A_ij} has only realised pair kernels {a_i,x_i} and EMPTY; m petals for each pair and r disjoint component choices for EMPTY. Density exactly half, so this is NOT an R3 counterexample.
8. Adversarial check: do not conflate chi(Gamma) (possibly unbounded) and maximum degree; coefficient 1/[8(Delta+1)] cannot be promoted to an absolute c when Delta is unbounded. Do not apply a private-pair partition to forward-private pair pieces.
9. The transversal-copy control requires N>=2 before a multi-copy matching has >=m members. For N=1 use one edge. At m=2 arbitrary H=D works. Complete tripartite N>=6m lies in robust-core, not the core-free DSE class.
10. S033 Theorem B and D are SAME-ASSISTANT baselines, not independently certified. This is an internal re-derivation, not literature screening, formalisation or peer review.

VERDICT: Theorem S034-A's restricted quantitative arithmetic and B's exact counterexample survive this same-assistant pass; all-m DSE_3 and R3 remain UNPROVED.
