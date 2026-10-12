# P001-S032 — simultaneous light-petal allocation: exact light-link certificates and first missing density step

**2026-10-12, exactly ONE bounded proof-first child mathematical gate.** New owner invocation was archived verbatim on the new remote branch at `d1129d4c05ecf2b6866d262a991d7cebb7310b80` (6309 UTF-8 bytes, SHA256 `32c7288fd555a5892d8642260ec38466674e2ef491951dea1832ddee791b6355`, separately recomputed in Python hashlib and standalone JS SHA-256). The standalone frozen C512/original-population gate was committed subsequently at `9bacda7e6b5afe539f1fbaee8f09a3c7b92554b4` BEFORE this research report or any NEXT replacement. There was NO new finite research enumeration. All arguments below are SAME-ASSISTANT symbolic mathematics, not independent mathematical review, formalisation, originality or a publication claim.

## 1. Exactly frozen original population; target and established budget

For EVERY m>=3 and t>=1 the ORIGINAL collection consists of t pairwise edge-disjoint COMPLETE m-petal triple sunflowers B_i, with full ORIGINAL support S_i. Define r(x)=number of ORIGINAL block supports containing x and ORIGINAL Q={x:r(x)>m}. Assume |S_i∩Q|<=2 and therefore every x outside Q belongs to <=m ORIGINAL supports. Original Q and r never change when a family is selected. Partition blocks by ORIGINAL Q into A (at least one petal with <=1 heavy Q label) and B (all m petals contain exactly two heavy Q labels, which must be their compulsory pair core). No privacy of original light labels. Let T=|B|, and w_uv be number of ORIGINAL B blocks with pair core uv. Distinct Q-neighbour counts in the SIMPLE pair graph are NOT w_uv.

Freeze numerical universal C=512: seek FINAL selected INDIVIDUAL ORIGINAL triple edges H with |H|>=t/(512m^2) such that EVERY exact realised intersection K of two distinct H triples, INCLUDING EMPTY K, has m distinct exact sunflower petals entirely IN H. The particular two intersecting triples need not be among the witnesses. The B-only sufficient target is |H_B|>=T/(256m^2); the valid A alternative is |H_A|>=|A|/((3m-2)(m-1)). Choose an alternative, never glue H_A,H_B or independent core/residual outputs without fully rechecking all resulting kernels. Even a completed two-original-Q block bound would not prove unrestricted rank-three R3, much less every-fixed-k TIK.

S031 remains an established same-assistant fallback, with L=2(2m-1) acyclic outdegree-slot two-coloured star forests; D_m=L(m-1)^2, and a collision-safe residual H_R>=T_R/D_m. Choosing one of this output and the S030 2m-core H_C>=T_C/(m-1) gives H_B>=T/[D_m+(m-1)]; then choosing ONE A/B alternative gives |H|>=t/[(m-1)(4m^2-3m+1)]>t/(4m^3). Hall gives globally injective ONE-light representative per ORIGINAL B block; no such conclusion for extra petals. S030 also proves weighted single star W_q/(m-1), small SIMPLE matching case >=T/[2(m-1)^2], and dense 2m-core. NONE of these alone gives universal C512.

## 2. NEW exact five-certificate light-link identity for any B-selected H

This lemma is **an exact diagnostic**, not a numerical extraction. Let H be ANY subset of individual triples drawn from ORIGINAL B blocks. Every selected triple is uniquely of form {u,v,z} with u,v∈ORIGINAL Q and z outside Q.

Define:
* a_uv = number of selected triples with Q-pair uv; because F is a SET this is the number of their distinct light thirds.
* For every ORIGINAL light z, G_z is the SIMPLE Q-graph containing uv exactly when {u,v,z}∈H.
* For every heavy q, J_q is the bipartite graph with sides Q\{q} and the original light labels, having edge (v,z) exactly when {q,v,z}∈H.
* nu denotes maximum cardinality of an actual matching; nu(H) is a matching of pairwise DISJOINT selected triples, not merely their Q-projections.

**Exact proposition (symbolic iff).** Every realised exact intersection of two distinct H triples has m exact petals in that SAME H if and only if all five conditions hold:

    (HH) for every uv⊂Q:             a_uv∈{0,1}∪[m,∞);
    (HL) for every light z, q∈Q:      deg_G_z(q)∈{0,1}∪[m,∞);
    (HS) for every q∈Q:              nu(J_q)∈{0,1}∪[m,∞);
    (LS) for every light z:           nu(G_z)∈{0,1}∪[m,∞);
    (E)  global triple matching:      nu(H)∈{0,1}∪[m,∞).

**Proof.** Two selected triples have an exact intersection of size two either in their two heavy labels uv (same heavy pair, different light; exactly a_uv possible petals) or in one heavy q and one light z (same q,z but different second heavy; exactly deg_G_z(q) possible petals). A heavy singleton {q} is realised precisely when there exist two disjoint residual pairs (v,z),(v',z') of J_q, and its maximal in-H petal count is exactly nu(J_q). A light singleton {z} is realised precisely when two Q-pairs of G_z are disjoint, and its maximal in-H petal count is exactly nu(G_z). EMPTY is realised precisely when H contains two disjoint original triples and is witnessed by exactly the matching number nu(H). Those are ALL possible intersections because each edge has two Q and one light label. A count 0 or 1 means the corresponding kernel was not realised by two edges; any count between 2 and m-1 fails; count >=m gives m actual in-H petals. Thus the five conditions are necessary AND sufficient. Note: even m disjoint Q-pairs do not ensure an H-matching if their chosen light thirds collide; (E) must concern ACTUAL selected triples, not only the Q graph. This proves the equivalence.

S029's simpler (pair multiplicity / SIMPLE Q degree / SIMPLE Q matching) equivalence follows ONLY for globally injected light representatives: then J_q has matching number equal to the distinct selected Q-neighbour count, every G_z contains at most one edge, and nu(H) equals the Q-graph matching number. This does NOT carry over to additional petals.

## 3. Apply the exact certificates to both independently different original-light collisions

**S030 same-centre failure:** original star q with z appearing on distinct pairs qv_1 and qv_2 after all-petal lifting gives G_z=K_(1,2), hence deg_G_z(q)=2<m (HH and old heavy singleton graph checks may pass). Its realised exact PAIR {q,z} has only two third labels v_1,v_2 and is INVALID. This is (HL), not a singleton or empty exception.

**S031 cross-component failure:** take for each m>=3 r=N=1024m pairwise vertex-disjoint K_(m-1,N) heavy graphs, with w=m-1 ORIGINAL complete m-petal B blocks per pair; all lights private except ONE original light z included in one pair block of component 1 and one pair block of component 2. All ORIGINAL Q are the bipartite endpoints: row/centre load N(m-1)>m, leaf load (m-1)^2>m, and r(z)=2<=m. The SIMPLE 2m-core is empty (a leaf has m-1 distinct neighbours). The S031 all-petal selected stars give G_z TWO DISJOINT EDGES, so nu(G_z)=2<m: the newly realised exact singleton {z} is INVALID, even when every heavy-pair codegree is >=m, selected heavy singleton links match >=m, and the ACTUAL global EMPTY matching is r>=m. This is (LS), not (HL).

In this SAME ORIGINAL F, the valid S031 compressed-forest representative output has rN=1,048,576m² individual edges. The B256 target is

    T=rN(m-1)^2=1,048,576m²(m-1)^2;
    T/(256m²)=4096(m-1)^2;
    |H_rep|/[T/(256m²)]=256m²/(m-1)^2 >256.

The dense repaired all-petal output deletes precisely the two z occurrences, leaving rmN(m-1)-2 edges. Affected heavy pairs retain m(m-1)-1>=m petals; every other chosen Q-pair has m(m-1)>=m, heavy singleton link matching remains N, every remaining light is private, and EMPTY has a true matching of r. This rescue is SAME ORIGINAL F, but its 2-edge special slack deletion does not yield an arbitrary weighted-family repair lemma.

**First UNPROVED step:** Find, for every weighted peeled sparse B residual, a simultaneous choice of additional petals and/or entire original pair blocks satisfying ALL (HH),(HL),(HS),(LS),(E) with |H_B|>=T/(256m²), i.e. an O(m²) original-block-to-selected-edge budget rather than the current O(m³). Neither global one-representative Hall injection nor the existence of a star-forest decomposition produces this quantitative choice. Separately-valid star components can introduce light-kernels with 2..m-1 petals. A large-star forest with >=m components and >=T_R/L weight whose every centre has >=m distinct neighbours suffices, but S031 does not guarantee such a forest. The statement that FULL lift of an existing valid representative forest automatically preserves (HL) and (LS) is FALSE as above. We do NOT infer that the desired bound itself is false.

## 4. New allowed parametric palette control: globally light-injective mass preservation is FALSE, yet full family is valid

To test the stronger attempted shortcut “allocate all additional petals without any repeated selected light, with only CONSTANT loss of petal mass”, freeze a new symbolic family, not a numerical search. For EACH m>=3 and r>=1 take r vertex-disjoint copies of the SIMPLE Q graph K_(m+1,m+1). In each copy let heavy sides be U={u_1,...,u_(m+1)} and V={v_1,...,v_(m+1)}. For EVERY Q-pair uv create exactly ONE COMPLETE original m-petal core-uv block (w_uv=1). For each row u_i, the m blocks on pairs u_i v_j, 1<=j<=m, all have the SAME m light-third labels Z_i (different rows and copies use DISJOINT palettes); the extra block u_i v_(m+1) has its own m private labels Z_i^*, disjoint from all other palettes. Edges are distinct because cores differ, even when the third is reused. No symmetry quotient or finite search is involved. The entire ORIGINAL F has

    T= r(m+1)^2 ORIGINAL B blocks,
    |F|=mT=rm(m+1)^2 individual triples,
    r(u_i)=r(v_j)=m+1>m,
    r(z)=m for z∈Z_i, r(z)=1 for z∈Z_i^*.

Thus ORIGINAL Q is EXACTLY all Q graph endpoints, and every ORIGINAL support has precisely two Q vertices. All repeated labels remain original LIGHT with load <=m; the 2m-core of each K_(m+1,m+1) is empty since m+1<2m for m>=3.

**DENSE SAME-ORIGINAL-F POSITIVE:** H=F ITSELF is internally m-valid! Every Q-pair uv has a_uv=m (HH). For z∈Z_i, G_z is a STAR on m distinct neighbours with centre u_i, so deg_G_z(u_i)=m and all other degrees 1; nu(G_z)=1. For z∈Z_i^* there is one Q-pair, so (HL),(LS) pass. Every u_i has an actual residual bipartite matching of size m+1: choose distinct palette labels for v_1,...,v_m, then one private label for v_(m+1). Every v_j has an actual matching of size m+1 across different rows, whose row palettes are disjoint, so (HS) passes. A global triple matching of at least m+1 comes from the diagonal Q-pairs u_i v_i with one distinct light chosen in each row; this certifies true EMPTY whenever realised. These checks prove all FIVE exact conditions in H, including any realised singleton, pair and EMPTY. Consequently H=F has rm(m+1)^2 valid triples, safely beyond T/(256m²).

**FALSE constant-loss all-light-distinct allocation shortcut:** any subfamily using a selected light label at most once has at most the number of light labels, namely 2mr(m+1), edges. Hence its fraction of the full internally valid F is at most

    2mr(m+1) / [rm(m+1)^2] = 2/(m+1) -> 0.

In particular no positive ABSOLUTE petal-mass fraction can be guaranteed by insisting every selected light appear at most once in this allowed original family. For each row's m shared-palette blocks, two light-distinct selected petals per block would require 2m distinct labels where only m exist. This refutes a proposed **mass-preserving private-light allocation rule**, NOT B256, full C512, R3 or TIK: even the light-distinct cap here vastly exceeds T/(256m²). Saturated repeated-light STARS can be perfectly valid; banning all collisions may lose a factor m unnecessarily. A valid general proof must exploit or jointly control their local exact (HL)/(LS) certificates.

## 5. Exact constants and preserved stress controls

Writing D_m=2(2m-1)(m-1)^2, the S031 whole restricted-slice denominator is

    a_m + D_m + (m-1) = (m-1)(4m²-3m+1)
                       = 4m³-7m²+4m-1.

The S031 proof already certified C512 for m<=128 by the coarse upper bound <4m³. More precise **arithmetic only** extends the exact same known inequality through m=129: denominator/m²=4m-7+4/m-1/m² is increasing for integer m>=3; at m=129 denominator 8,470,784 <=512*129²=8,520,192, whereas at m=130 denominator 8,670,219 >512*130²=8,652,800. The existing B fallback denominator D_m+(m-1)=4m³-10m²+9m-3 similarly beats 256m² precisely for integer 3<=m<=66 (m=66:1,107,015 <=1,115,136; m=67:1,158,762 >1,149,184). This marginal finite-m sharpening does NOT solve the UNIVERSAL unbounded-m constant: these denominators grow as m³ and their ratios to the target m² grow linearly in m.

S029 original K_(m-1,m-1), w=m-1, has Q load (m-1)^2>m, rep-only optimum one because pair< m, degree<m and graph matching<m; a whole original single pair gives m(m-1) valid petals in the SAME F. S018 mixed channels have failed actual singleton and EMPTY matchings with valid density-half alternative, and S019 mixed saturated star has actual EMPTY matching 3<m with valid pair-core alternative fraction m/(m+2)>=2/3. Their mixed blocks may fall in A: do not relabel as pure B or concatenate outputs. S022 repeated light remains fatal for an unsaturated selected light-pair link. FULL S023 nested q-plane is an ORIGINAL A example and admits the known direct-petal A bound despite whole-block BSEL failure. S024 dense K_N with simple min-degree >=2m falls in the S030 2m-core regime with true m matching; do not assume all graphs are sparse stars. Literal m=2 permits H=F because the two intersecting edges witness themselves. Literal t=0 permits H=empty. For m>=3 and t<=512m³, one original complete m-petal block gives |H|=m>=t/(512m²), including its exact core (possibly EMPTY). No small-t excuse is used to imply a universal allocation.

## 6. S032 outcome, provenance and explicit open implication

**SAME-ASSISTANT POSITIVE:** exact five-link certificate iff for every chosen triple subfamily in ORIGINAL B; successful dense saturated-light ORIGINAL palette family; exact finite-m C512 consequence improved from <=128 to <=129 (B256 to <=66) by sharpening an ALREADY proved bound. No new universal m saving.

**METHOD-ONLY NEGATIVE:** Full-petal lift fails at S030 exact {q,z} pair and S031 exact light {z} singleton. Additional universal constant-loss global light-private allocation is refuted by the ORIGINAL B palette family with cap 2/(m+1) despite the full H=F being valid. None of these is a counterexample to numerical B256, original C512, arbitrary R3, all-k TIK or a proof of novel mathematics.

**FIRST UNPROVED UNIVERSAL IMPLICATION:** A weighted star decomposition and one Hall light representative per B block do not imply existence of an additional-petal selection satisfying (HH),(HL),(HS),(LS),(E) with B256 mass. Achieving the missing m factor by certifiably-safe saturated light-star bundles, while also preserving heavy singleton and EMPTY matchings, remains the mathematical task. This is not rescued by treating w_uv as degree or by combining separately-valid A/B, core/residual or individual star outputs. Universal whole-block BSEL remains provisionally REFUTED, and full every-fixed-k TIK/R3 remain UNPROVED.

No new detailed N1/N2 because there is no complete every-k TIK candidate; the historical JJSW26 Section 6 source attribution is unchanged, exact rank-three literature status STATUS_UNCERTAIN, originality NOVELTY_UNCERTAIN. No independent referee, Lean, formal verification, publication, manuscript, contact, parent S001 or successor S033 mathematical execution. Mandatory S005/S010/S015/S020/S025/S030 audits remain complete; S035 is next.
