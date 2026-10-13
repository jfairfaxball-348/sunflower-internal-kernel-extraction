# P001-S041 — adversarial second pass independent of the theorem report's proof lines

Date 2026-10-13. SAME ASSISTANT fresh reconstruction, **NOT** an independent mathematician, formal proof, source novelty screen or machine checking. Audited exact frozen original-mass statement separately from section numbering of research/S041_REGIONAL_OVERLAP_AND_ALL_K_LINK.md.

## A. Rebuild every inequality without trusting the report

1. **Fractional cover duality is not needed.** Given any feasible weights a_v on a nonempty original rank-k D, |D|=Σ_{e∈D}1≤Σ_eΣ_{v∈e}a_v=Σ_v a_v deg_D(v)≤Δ(D)Σ_v a_v. Minimising weights yields Δ≥|D|/τ*. No assumption τ* integral, no reversal of bound, τ*≥1 for nonempty D.
2. **One-apex lifting is EXACT.** Pick x achieving Δ, let L=D(x). Distinct chosen (k-1)-sets lift injectively. Any two lifted edges intersect in {x}∪(A∩B), and their m witness sets have identical lifted exact kernel. The residual EMPTY in L becomes singleton {x} in lifted H, so it is genuinely certified; EMPTY in H cannot occur. Selected quantity c_{k-1} Δ/m^(k-1) ≥ c_{k-1}|D|/[τ* m^(k-1)]. Both original-link versus final-link and selected-pair-not-required issues respected.
3. **Disjoint islands criterion.** Every cross-island selected pair is disjoint (hypothesis is vertex-support disjoint, NOT just edge-disjoint). For an internal pair's nonempty kernel, its J_i witnesses survive in the union. For internal EMPTY kernels J_i already supplies m whole selected disjoint petals. If a cross pair creates EMPTY, the explicit ν(∪J_i)≥m supplies exactly the needed global sunflower. No theorem says a mere sum of component cardinalities suffices.
4. **When ν<m**, at most m-1 NONEMPTY selected islands, because one selected edge from each is a disjoint matching; if r≥1, max_i |F_i|/τ_i ≥(Σ_i |F_i|/τ_i)/r. A standalone J_i is internally valid even if its own matching is 1 and all its pair intersections are nonempty. For r=0 W=0 handled. Hence weighted W/m loss is valid for every m≥2; no hidden second factor m.
5. **Mixing a potentially intersecting F_0 with islands is forbidden.** The theorem takes the larger of two independently valid candidates, not their union. Division by τ*(F_0) only if F_0 nonempty; bounded-cover corollary uses max(n_0,n_islands)≥n/2, *not* a false additive lower bound. All constants: if τ0≤Bm, n0/τ0≥n0/(Bm); if τ_i≤B, W≥n_islands/B; therefore selected fraction ≥ c_{k-1}/(B m^k)·max(n0,n_islands) ≥ c_{k-1}n/(2B m^k). At rank3 c2=1/8 gives 1/(16 Bm³).
6. **Empty family:** H empty, n=0. **m=2:** everything internally valid, no invalid middle link interval. **Rank two case:** assume only rank-one c1=1 (known elementary); formula remains correct.

## B. Try to break sharpness and the scope claim

Consider original E_m = ⊔_{i=1}^{m-1} { {x_i,y,z}: y∈Y_i, z∈Z_i }, |Y_i|=|Z_i|=m-1, and all clusters support-disjoint. For any two edges in SAME island there are precisely three intersection forms:
- same y and distinct z: exact PAIR {x_i,y}, original residual link size m-1<m;
- same z and distinct y: exact PAIR {x_i,z}, original residual size m-1<m;
- different y and different z: exact SINGLETON {x_i}, original residual graph K_(m-1,m-1) matching m-1<m.
Thus selecting two such edges always violates m-validity, independently of chosen H.
For edges in DIFFERENT islands, exact EMPTY. Every original triple contains a distinct island apex and a matching can contain at most one triple per apex, thus ν(E_m)≤m-1<m. Two cross-island selected edges cannot have EMPTY witnesses in H. Consequently any valid H has ≤1 edge; singleton attains 1. n=(m-1)^3 and τ_i*=1. This is a sharp exponent illustration within the scoped class, **not an HDSE3 negative**: m³ maxvalid/n = [m/(m-1)]³→1.
For m=2 there is only one island and one triple. Formula remains literally correct.

**Potential flaw attacked:** If the local corollary tried to dispense with whole-support disjointness between islands, two certified J_i might realise a cross kernel K≠EMPTY with 2..m-1 in-H matching, invalidating union. S039's two-hub shared-vertex counterexample already shows this. The current statement **retains** island-to-island vertex disjointness. It only drops separation between F_0 and islands, and avoids their union, so the counterexample does not falsify it.

**Potential flaw attacked:** Is the alleged example of arbitrary core-island overlap actually a permitted partition? Yes, edges of F_0 contain a separate t and an island x_i with an additional b, while island edges omit t and use {x_i,a,z}; choose b outside each island to avoid edge duplication. Supports of different islands remain disjoint because their x_i,a,z are disjoint. F_0 intersects all of them through their x_i, so its conflict graph has arbitrarily high degree, and the explicit cover {t} gives τ0*=1. Islands may have arbitrary bipartite incidence; each contains its x_i, giving τ_i*=1. This is a restricted **positive** demonstration; it need not meet the 6m-spread/core-free HDSE3 input conditions.

## C. Adversarial external known controls and overclaims

- S023 projective-plane whole-block obstruction does not invalidate (1): (1) may yield a small W when no bounded local-cover separated-island mass exists, but makes no promise for that E absent the partition. Dense S024 partial-edge rescue is retained as counter-control.
- S024 K_N and S029 bipartite high-overlap families are not declared covered by S041's bounded B; S035 already warns spread forces a **lower**, not an upper, fractional-cover bound.
- S030/S031 shared nonprivate light, S032 row, S034 twins, S036 bridges, S037 shared palettes, S038 nearly-full tensor failure and S039 private-per-spoke all remain possible ORIGINAL input geometries. Theorem (1) neither uses original pair-codegree as selected certificate nor assumes a thick tensor. It does not turn a hub-heavy family into a bounded-local-cover decomposition.
- S040 disjoint complete star-forest products can have island τ* arbitrarily large, so S041-B is **not** a strict generalisation of S040. Conversely an arbitrary partially occupied regional K_(d,d) minus a matching is not generally a complete product, and core F_0 can overlap every island. The two structural classes are incomparable; coefficient 1/(16B) is smaller than S040's 1/3.
- A hypothetical universal all-k induction cannot promote (1) unless the decomposition premise is proved in EVERY rank, with B bounded independently of m and |F|. No such mass-capture theorem was obtained; no rank-three result alone implies all k.
- No parametric ORIGINAL HDSE3 E_m satisfying m³ maxvalid(E_m)/|E_m|→0 was constructed or claimed.

**Second-pass outcome:** No counterexample found to the exact stated weighted/core-island theorem or sharpness argument. This is a same-assistant symbolic second pass, not independent proof endorsement. First unproved universal implication is quantitative access to high-degree overlap through arbitrary ORIGINAL E without a bounded-cover/core-island decomposition; in-H multi-link synchronisation remains unsolved. No numerical enumeration was run or newly specified.
