# P001-S028 — petal-first multi-hub direct-edge extraction (restricted POSITIVE)

**2026-10-11. One standalone proof-first child mathematics gate.** The fresh 126-byte literal invocation was archived at child commit `c3d26e51f9ddc52647c416f7ab32ebe9f4937caa` with independently computed UTF-8 SHA256 `f19536cc72c22ee3417531f9327f1cf9477ecb1123539be080b2546ca73b172b`. The C=512 universal quantified original-Q gate was written in a distinct subsequent commit `ab839bcebaa26e0eb6a0aad9251cd371660f5400` **before this report**. The one frozen `PETAL_FIRST_MULTIHUB_512` statement is PROVED in its exact S027 domain, with a strictly stronger SAME-ASSISTANT symbolic bound `t/((3m-2)(m-1)) >= t/(3m²)`. No independent referee or new prior-art screening; not a proven novel paper theorem. General R3, unrestricted S024/S025 edge inequalities, and every-fixed-k TIK remain UNPROVED.

## 1. Frozen population and invariant

Fix m>=3 and t>=1 pairwise edge-disjoint complete original m-petal triple-sunflower blocks `B_i`, i=1,...,t. Let `S_i` be the full vertex support of the original block, `r(x)=|{i:x in S_i}|` and **ORIGINAL** `Q={x:r(x)>m}`. Freeze `Q,t` throughout. Hypotheses: `|Q|>=1`, `|S_i intersect Q|<=1` for every original block; hence each original non-Q light vertex x lies in at most m original block supports. Supports of different original blocks may overlap arbitrarily on light vertices subject to this load; there are NO privacy or whole-support independence assumptions. Original kernel sizes are exactly 0,1,2.

The frozen demand is ONE `H` of individual triples from the original packed union with `|H|>=t/(512m²)` and every realised exact intersection between two distinct final H triples internally m-witnessed in that SAME H. We prove the stronger bound and certify pair, singleton, EMPTY exactly.

## 2. Petal-first light conflict costs O(m), not O(m²)

For EVERY original block `B_i`, choose ONE arbitrary original petal/triple `E_i in B_i`, without filtering or deleting original blocks first. The edge-disjoint packing ensures distinct representatives. Let `L_i=E_i\\Q` be its original-light portion, of size 2 or 3 because `|S_i intersect Q|<=1`. Construct a *representative*-conflict graph `G` on the t original block indices: join i,j if `L_i intersect L_j` is nonempty. Each x in `L_i` belongs to at most m original block supports, hence can belong to representatives of at most m blocks. Thus each i has degree at most

`sum_(x in L_i) (r(x)-1) <= |L_i|(m-1) <=3(m-1)`.

Greedy independence gives an index set I of cardinality

`s=|I| >= t/[3(m-1)+1]=t/(3m-2).`

Set `R={E_i:i in I}`. The full ORIGINAL supports of the blocks indexed by I might still overlap and might have no valid whole-block union; only the selected representative *light parts* are pairwise disjoint. This is exactly the difference from S027's disproved full-original-support-thin-first method.

For each representative define its **actual selected heavy tag** `tag(E_i)=q` when `E_i intersect Q={q}`, or `tag(E_i)=0` when `E_i intersect Q=empty`. Partition I into h nonempty tag classes `I_1,...,I_h` (0 counts as one class). Every two selected reps with the same actual Q tag q have exact intersection {q}; two with tag 0 are disjoint; reps of distinct tags are disjoint. Absolutely NO realised exact 2-point intersection or light singleton intersection can occur in a subset of R.

## 3. One final-H selection, no uncharged extra m² loss

**Case A: h>=m.** In each class with `d_j=|I_j|>=m`, keep ALL `d_j` selected representatives. In each smaller class `1<=d_j<m`, keep ONE representative (arbitrary). Call the union H. Its count satisfies

`|H|=sum_(j:d_j>=m)d_j + sum_(j:d_j<m)1 >= sum_j d_j/(m-1)=s/(m-1).`

All exactly realised 2-point intersections: NONE (so vacuous, not external witnesses). All exactly realised singleton intersections: only heavy tags q from classes with >=2 kept reps, and those classes have >=m kept reps with disjoint original-light residual pairs. These supply a *true matching of m pairs in FINAL H({q})*. If a class was thinned to one representative, its tag singleton is not realised within that class. No light singleton can be realised. Exact EMPTY is realised across at least two tag classes; since h>=m and every class contributes at least one selected representative, choose one representative from each of m different classes. Different Q tags and disjoint original-light parts make these m triples pairwise DISJOINT: a true final-H matching. This jointly checks all pair/singleton/empty kernels, including unexpected light-pair possibilities (ruled out, not assumed away).

**Case B: 1<=h<m.** Choose a largest class I_j with d>=s/h>=s/(m-1). If d>=m, take ALL d representatives of this ONE tag class as H. If the tag is q, each pair has exact kernel {q} and the d disjoint light residual pairs witness it with >=m petals; EMPTY is absent. If the tag is 0, all representatives are mutually disjoint and they themselves form an m-matching for the only realised kernel EMPTY. If instead d<m, choose ANY ONE complete original block B_i from the original packing and set H=B_i. Its m triples are exactly an m-petal sunflower at its own original kernel, so all realised exact intersections (including original empty kernel if applicable) are internally certified. Numerically `|H|=m>d>=s/(m-1)`. This small-class fallback is not glued onto any other output.

The two cases exhaust all populations. In either case a FINAL H exists with

`|H|>=s/(m-1)>= t/[(3m-2)(m-1)] >=t/(3m²)>=t/(512m²)`

for every m>=3. **C=3** is an available stronger constant on the frozen population; C=512 is therefore proven. Costs: one representative-light conflict factor `3m-2`, and ONE heavy-tag compression factor `m-1`, not two overlapping O(m²) filters. In the small fallback m triples replace a too-small representative class; their original complete sunflower supplies every relevant witness, without using outside-F or outside-H witnesses.

## 4. Exact stress controls, original heavy identity, scope

- **S023 full three-tier q-plane:** m=q+2, h=g=m-1 original heavy hubs, `L=m²-3m+3` lines per plane, `t=(m-1)²L`. Every original block has exactly one Q hub and original non-Q support load <=m: IN DOMAIN. Taking the block-private `{v_a,x_(a,b,l),w_(a,b,l)}` representatives yields no representative-light collisions at all (`I=all t`). There are h=m-1<m tag classes, so the largest (one hub) has `(m-1)L=t/(m-1)` representatives; each pair intersects in exactly that hub, its residual matching has `(m-1)L>=m` disjoint light pairs, EMPTY ABSENT and no exact 2-pair realised. This is distinct from, and compatible with, S024 denser `H_good=(m-1)(L+m-1)`; the same population provably defeats *whole original-support* thinning but not *petal-first* thinning. At q=1024,m=1026, the report's universal bound guarantees >=ceil(1,102,737,050,625/3,152,900)=349,754 triples; this explicit one-hub scheme gives 1,075,841,025; the original S024 H_good gives 1,076,891,650. All are above the original C512 threshold 2047.
- **S018/S019 mixed original two-Q-per-support examples:** generally OUTSIDE <=1 original-Q/support and cannot be declared solved. Their exact heavy pair, singleton and EMPTY mismatches remain warnings for the next gate. The present H has at most one actual Q vertex per representative; pair Q-Q kernels cannot arise. Combining separately selected mixed-Q outputs is NOT sanctioned.
- **S024 dense K_N pair-core control:** for N>=2m+1 both original core vertices per block belong to ORIGINAL Q, so OUTSIDE this gate; its valid dense graph m-core representatives cannot be forced into one-heavy-tag classes. Any later two-Q extension must preserve the K_N positive certificate.
- **S022 Q=empty:** outside frozen positive-Q premise, but the same proof works verbatim if Q=empty; only the tag 0 class exists, representatives are pairwise light-disjoint after greedy filtering, and the one-class/m-small fallback is internally certified. This is a corollary, NOT a change of original Q nor a proof for two-Q cases.
- **m=2** (outside the frozen m>=3 gate): H=the packed union F works for any triples because the two selected triples themselves witness their exact intersection as a two-petal sunflower. **t=0:** H=empty; original Q necessarily empty, so the frozen positive-Q premise is void. **Low t:** if s/(m-1)<m and fewer than m classes, the ONE whole-block fallback literally supplies all m petals, not merely a vacuously valid one-edge H.
- No computation/enumeration/random search was performed: the finite symbolic population, charge, exact codegrees and matching arguments are parameter-uniform. No purported algorithmic complexity claim.

## 5. What is solved and what is NOT

**PROVED symbolically, same-assistant and still needing external mathematical review:** S028 frozen **MULTIHUB_NONPRIVATE_DIRECT_EDGE_512** (the unresolved S027 exact <=1-original-Q/block subclass), in fact `MULTIHUB_NONPRIVATE_DIRECT_EDGE_3`. This supersedes S027's *unproved frozen numerical status*, NOT its correct negative finding that whole-full-support-thin-first is false. The S026 one-global-Q positive remains true but weaker for this overlap of hypotheses.

**NOT proved:** S024 fully arbitrary original heavy-support DIRECT_PARTIAL_EDGE_512; S025 GLOBAL_EDGE_DICHOTOMY_512; general two- or three-Q per block petal skeleton; arbitrary rank-three R3 or the immutable every-k TIK statement. The restriction to an already existing edge-disjoint packing is significant; no absolute TIK fraction of an arbitrary 3-uniform F has been established. S023 universal whole-block BSEL remains provisionally FALSE. New project-level independently verified/original paper theorems remain zero. No source-intensive N1/N2, Lean, independent referee, new manuscript, contact, submission, publication or parent mathematical S001. Fifth correction audit due P001-S030, NOT in S028.

Next fresh session P001-S029 must tackle **two-Q representatives with actual heavy pair codegrees, singleton matchings and EMPTY globally**, without claiming the S028 proof extends to them.
