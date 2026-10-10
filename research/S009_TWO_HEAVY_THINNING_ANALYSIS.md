# P001-S009 — two-heavy multi-hub slice: precise low-load thinning refutation

## Target and one tested mechanism

The **unchanged target** is full TIK for every fixed k, with in-H exact sunflower witnesses. R3 and universal whole-block BSEL remain auxiliary. The S009 slice: for each m>=3, arbitrary finite edge-disjoint complete m-triple sunflower blocks B_1,...,B_t, with V_i their full supports, r(v)=#{i:v in V_i}, Q={v:r(v)>m}, and |V_i intersect Q|<=2 for **every** i. Kernels 0,1,2 are all permitted; arbitrary overlaps of arbitrarily many heavy vertices are permitted. Want an absolute gamma>0 and J with |J|>=gamma*t/m^3 such that every realised pair intersection in H=union_{i in J}B_i has an m-petal sunflower **inside H** with that exact kernel. For |K|=2 require codegree>=m; for |K|=1 an m-matching in the residual graph; for K=empty an m-matching among triples. Witnesses need not contain the selected pair.

S007 supplies compatible selection only if the *selected subpacking* has every block-vertex load <=m. A natural proposed sufficient preprocessing is:

**THIN_Q(eta), explicitly REFUTED:** There exists an absolute eta>0 such that, for every m>=3, every t>=0, every above two-heavy packing, one can choose whole blocks indexed by J subset [t] satisfying both (i) |J|>=eta*t/m^3 and (ii) r_J(v):=#{i in J:v in V_i}<=m for **each v in the original Q**. Since v not in Q already has r(v)<=m, condition (ii) yields r_J(v)<=m for *every* vertex; hence S007 would produce an internally valid subcollection of size at least |J|/(3m^3), but only a weaker t/m^6 bound under this quantitative formulation. In particular a stronger constant-fraction THIN_Q variant (|J|>=delta*t) would imply the desired BSEL t/m^3 via S007. The negative below defeats **both** variants, and even the t/m^3-sized necessary normalization step. Do not mistake the weaker conditional exponent for a proof of BSEL.

## Explicit parametric mixed-kernel construction

Fix any m>=3 and any integer q>=2m+2. Let the set of **hubs** be X={h_1,...,h_q}. Introduce all private auxiliary vertices below, pairwise distinct and outside X, with no identifications other than the displayed hubs.

1. For each unordered pair {a,b} subset X, define a pair-core block P_{a,b} of m distinct triples {a,b,z_{a,b,j}}, j=1,...,m. All z private.
2. For each hub a in X, define a singleton-core block S_a of m triples {a,x_{a,j},y_{a,j}}, j=1,...,m. All x and y private.
3. Define ONE empty-core block E of m mutually disjoint triples {p_j,q_j,s_j}, j=1,...,m, where all 3m symbols are private.

Every block has exactly m edges and is a COMPLETE m-petal sunflower of its asserted exact kernel. No edge is repeated across blocks (nor within blocks). Number of blocks:
t=binom(q,2)+q+1=q(q+1)/2+1.
Each hub a appears in (q-1) pair-core supports and its own S_a, so r(a)=q>m. Every private vertex belongs to exactly one block, hence r=1. Therefore Q=X **exactly**. The support of P_{a,b} meets Q in exactly 2 hubs, S_a in exactly 1, and E in 0. The packing meets the two-heavy hypothesis without disjoint hubs and uses **all three** allowed core sizes.

## Full-union validity (a positive BSEL control, not its refutation)

Choose ALL t blocks and H their union. Every intersection of two distinct triples is exactly one of:
- A 2-point kernel {a,b} for two triples within P_{a,b}. No other block uses both these hubs in the same triple. The m distinct triples of P_{a,b} witness exactly {a,b}, giving codegree at least m.
- A singleton kernel {a} for triples within S_a, for a triple from S_a and a triple from P_{a,b}, or for triples from two distinct pair-core blocks P_{a,b},P_{a,c} with b!=c. The m triples in S_a have residual pairs {x_{a,j},y_{a,j}} pairwise disjoint. Thus matching number in the singleton link of a is at least m inside H.
- Empty kernel for triples whose hub sets are disjoint (including distinct S blocks and any triple of E). The m edges of E are mutually disjoint, furnishing an m-edge matching INSIDE H.

There are no extra intersections, since all non-hub symbols are private and each pair-core block has unique hub pair. All kernel sizes occur nonvacuously: m>=3 gives two triples per pair/singleton block and E itself has disjoint triples; all witnesses belong to H. Thus J=[t] is BSEL-valid and |J|=t, yielding gamma=1 **for this construction only**.

## Rigorous asymptotic refutation of THIN_Q

Fix m>=3 and let q increase through integers >=2m+2. For any selected subset J of complete blocks with r_J(a)<=m for all hubs a, let e count selected pair-core blocks, s count selected singleton-core blocks and d in {0,1} record selection of E. Double-counting hub incidences gives

2e+s = sum_{a in X} r_J(a) <= m q.

Consequently e+s <=mq and |J|=e+s+d <= mq+1. Yet t=q(q+1)/2+1, so

m^3 * (mq+1) / t -> 0 as q->infinity

for every fixed m, including m=3. Given ANY eta>0, choose q sufficiently large that mq+1 < eta*t/m^3. This makes THIN_Q(eta) impossible irrespective of whether J is internally compatible. Thus **no absolute eta>0 exists**. Stronger constant-density heavy-load normalisation also fails. This is a genuine parametric obstruction to the quantified supporting mechanism, NOT a finite anecdote.

## Exact scope and first unproved step

Refuted: the requirement that one first retain t/m^3 (or any constant fraction of t) blocks while lowering **every** originally heavy hub's selected load to <=m. It is false even for mixed-kernel packings that are wholly internally valid. Also vertex-disjoint heavy-hub-footprint selection would retain only O(q) blocks here. The error is mistaking arbitrary high-load overlaps for incompatibility. The full union is a direct compatible high-load reservoir, so neither this construction nor S008 disproves two-heavy BSEL, general BSEL, R3 or TIK.

**First unproved implication:** for arbitrary two-heavy packings, find Omega(t/m^3) WHOLE blocks with the *original heavy overlaps allowed*, whose newly realised exact 2-point kernels have codegree >=m, singleton residual links have matching >=m, and whose realised empty intersection has an m-matching, all inside the final selected union. Merely bounding heavy-hub degrees, choosing one hub, or avoiding hub-overlap cannot justify this implication. S006's cross-block obstructions remain (a subset selection may create an unwitnessed pair/singleton/empty intersection), and S007 remains applicable when an actual induced low-load subpacking is dense enough.

For t=0, J=empty is trivially valid. For 1<=t<=3m^3, one complete block is internally valid and meets |J|=1>=t/(3m^3). These small-t facts do NOT solve the general t case. No claim is made about gamma for the whole slice; no general BSEL/R3/TIK proof candidate, new project paper theorem, independent math review, novelty promotion, Lean, external submission or computational experiment. All conclusions are symbolic same-assistant calculations.

## Bounded next research gate (S010 not executed)
Study the mixed-kernel two-heavy class with **private light vertices** (every v outside Q has r(v)=1), leaving arbitrary high-hub graph and core sizes. Establish an exact selection bound or refute a nontrivial precise closure mechanism at pair/singleton/empty kernels, without claiming that simplifying the light overlaps solves general BSEL. The tenth-substantive strategic and fifth-session correction audit is compulsory in S010.
