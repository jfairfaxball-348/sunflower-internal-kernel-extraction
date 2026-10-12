# P001-S033 — frozen populations, constants, candidate statements and auxiliary-check specification

2026-10-12. The new owner invocation (multi-route "Grand Breakthrough Attempt") was archived FIRST at branch commit `7bbba4e130451788080eb93594ea01b30030bf7c`: 20107 UTF-8 bytes, SHA256 `1b504b82d0f4e25414f0849d7b68cecc49dbcb9a7f81296c505d7edc0b5c409c`. Python hashlib, GNU sha256sum and Node crypto agree, and each reproduces the SHA256(abc) vector. The manifest was committed next at `27ff9d1e1bea8c7cb415bac6e815f3bd70acc4a2`. This gate is committed BEFORE any S033 research report and BEFORE NEXT_SESSION is replaced. Entry: child main `cffa73b2ad4710cfcdabe4500776e71e02e71ac2`, parent main `96e4f1196ba601c145be53d08b270c27cc340534` (see [entry evidence](../sessions/P001-S033/ENTRY_EVIDENCE.json)).

## 1. Immutable target (unchanged)
TIK exactly as in [TARGET.md](TARGET.md). For each fixed k>=1, there is c_k>0 depending only on k such that for all m>=2, n>=k and every k-uniform F there is H ⊆ F with |H| >= c_k m^-k |F|, and for every realised exact intersection K=A∩B (A≠B in H, K=∅ included) ν(H(K)) >= m, where H(K)={E\K : E∈H, K⊆E}. Witnesses lie in H and need not contain A or B. Write a_k(m) for the infimum over nonempty k-uniform F of max |H|/|F| over internally valid H. TIK_k means: a_k(m) >= c_k m^-k for all m>=2.

## 2. Original packed-block populations (unchanged from S032, frozen without recomputation)
For every m>=3 and t>=1, there are t pairwise edge-disjoint ORIGINAL complete m-petal triple sunflowers B_i with ORIGINAL supports S_i. Here r(x)=#{i : x∈S_i} and Q={x : r(x)>m}; both are fixed once and never recomputed after selection.
- At-most-two-Q slice: |S_i∩Q| <= 2. Class A: some petal has <=1 Q vertex. Class B: compulsory two-Q pair cores. w_uv is the ORIGINAL weighted simple heavy-pair graph; T_C is the 2m-core weight and T_R the peeled residual weight.
- Constants frozen and neither assumed true nor false:
  - C512: |H| >= t/(512m²).
  - B256: |H_B| >= |B|/(256m²), with residual objective |H_R| >= T_R/(128m²).
  - A alternative: |H_A| >= |A|/((3m-2)(m-1)).
  - S031 fallback: D_m=2(2m-1)(m-1)², giving |H| >= t/((m-1)(4m²-3m+1)) > t/(4m³).
- S032 five-level B criterion: HH/HL/HS/LS/EMPTY.
- Alternatives are SELECTED, never glued.

## 3. New frozen definitions and candidate statements for S033 (Route E / Route D)
- d_F(T)=#{A∈F : T⊆A}.
- **λm-spread:** F is λm-spread when d_F(T) <= (λm)^-|T| |F| for every nonempty T with |T| <= k.
- **Robust core C(F):** the largest G ⊆ F such that every nonempty T properly contained in some edge of G has ν(G(T)) >= m. The defining property is closed under union, so C(F) is unique.
- **Core-free:** C(F)=∅.

Candidate statements, frozen with their exact constants BEFORE proof:
- **LR (link reduction), every k>=2, any fixed λ>=1:**
  a_k(m) >= min{ λ^-k m^-k , min_{1<=j<=k-1} λ^-j m^-j a_{k-j}(m) , s_k(m,λ) },
  where s_k(m,λ) is the infimum of the best ratio over nonempty λm-spread k-uniform families.
- **T2 (rank two):** a_2(m) >= 1/(8m²) for every m>=2. This is the full immutable target at k=2 with c_2=1/8. The tested route uses λ=2.
- **RC (robust core):** if F is λm-spread, γ∈(0,1], λ >= k/γ and |C(F)| >= γ|F|, then H=C(F) is internally valid.
- **DS (degenerate-spread reduction), every k>=2:** given TIK_j for j<k, TIK_k is equivalent to a bound c m^-k for the class of nonempty λm-spread core-free families, for one fixed λ>=2k (γ=1/2).
- **P3 (rank-three deletion pieces):** core deletion with pair priority yields two kinds of piece. Pair pieces have <= m-1 edges sharing a pair. Vertex pieces at x have link graphs on <= 2m-1 vertices with minimum degree >= m, so fewer than (2m-1)(m-1) edges.
- **DSE_3 (degenerate spread extraction):** to be proved or reduced; NOT assumed. Every nonempty λm-spread core-free triple family D admits valid H with |H| >= c m^-3 |D|.

No statement above is assumed true. A failure is recorded at its FIRST false or unproved implication.

## 4. Mandatory stress population (symbolic)
The following must be tested symbolically:
- S032 row-palette K_(m+1,m+1), with the full valid F and the 2/(m+1) private cap;
- S031 1024m disjoint-star family with its shared light z and the dense repair;
- S030 repeated-light {q,z};
- S029 K_(m-1,m-1) with w=m-1;
- S018/S019 mixed families;
- S022 repeated light;
- the full S023 nested q-plane;
- S024 K_N;
- the (m-1)^k transversal family;
- m=2, t=0, small t, large m, and empty or degenerate H.

## 5. Frozen auxiliary finite check (bounded; NOT a search; NOT a proof)
- **Purpose:** detect implementation-level or case-analysis mistakes in the constructive T2 proof. The script implements the case analysis exactly as written (non-spread vertex/star, m-core, star forests from the deletion orientation, big/small stars, matching fallback). It validates each output H with the existing exact checker `scripts/semantics.py::internal_by_links`, and asserts 8m²|H| >= |F|, H ⊆ F, and H nonempty.
- **Population (complete list; labelled; no symmetry quotient):** for each m ∈ {2,3,4}:
  - K_N for N ∈ {3,...,9};
  - K_(a,b) for (a,b) ∈ {(1,8),(2,5),(3,3),(4,4)};
  - star K_(1,12);
  - path P_10 and cycle C_9;
  - 3 disjoint copies of K_(m-1,m-1) (m>=3) and 4 disjoint copies of K_(m-1,m-1) (m>=3);
  - the union of a K_(1,10) star and a disjoint 3-edge matching;
  - 5 graphs from Python `random.Random(seed)` G(n=10,p=0.35) with seeds 0..4.
  That is at most 3×(7+4+1+2+2+1+5)=66 graphs in total.
- **Resources:** <= 10 seconds wall-clock and 256 MiB.
- **Stop rule:** a single run. Any assertion failure is recorded verbatim as a negative finding and the proof is re-examined. The population is not extended after seeing results.
- **Expected output:** all PASS. A PASS supports implementation consistency only and is NOT a proof. The asymptotic statement rests solely on the written proof.

No other computation, CAS, SAT/ILP or enumeration. No Lean, no new detailed N1/N2, no manuscript, no external action. S035 remains the next mandatory fifth correction audit; S033 is not S035.
