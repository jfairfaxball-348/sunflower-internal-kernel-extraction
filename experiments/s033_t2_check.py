#!/usr/bin/env python3
"""P001-S033 frozen auxiliary check of the constructive T2 (rank-two) case analysis.

Population, resources and stop rule are frozen in research/S033_FROZEN_GATE.md section 5
BEFORE this script was run. A PASS checks implementation consistency only; it is NOT a proof.
"""
import random
import sys
import time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import semantics  # noqa: E402


def extract(edges, m):
    """Return (H, branch) following the written T2 proof exactly (lambda = 2)."""
    F = [frozenset(e) for e in edges]
    e = len(F)
    if m == 2:
        return F, "m=2: H=F"
    deg = {}
    for E in F:
        for v in E:
            deg.setdefault(v, []).append(E)
    # Non-spread: a vertex T with d(v) > e/(2m).
    for v, inc in deg.items():
        if 2 * m * len(inc) > e:
            if len(inc) >= m:
                return inc, "non-spread vertex star"
            return [inc[0]], "non-spread vertex, d(v)<m: single edge"
    # Non-spread: a pair T (an edge) with 1 > e/(4m^2).
    if e < 4 * m * m:
        return [F[0]], "non-spread pair (e<4m^2): single edge"
    # Spread case. m-core by deleting vertices of current degree < m, orienting out of the deleted vertex.
    alive = set(F)
    cur = {v: set(inc) for v, inc in deg.items()}
    out = {}  # deleted vertex -> list of its out-edges (head = other endpoint)
    queue = [v for v in cur if 0 < len(cur[v]) < m]
    deleted = set()
    while queue:
        w = queue.pop()
        if w in deleted or not (0 < len(cur[w]) < m):
            continue
        deleted.add(w)
        out[w] = list(cur[w])
        for E in list(cur[w]):
            alive.discard(E)
            (x,) = E - {w}
            cur[x].discard(E)
            if 0 < len(cur[x]) < m:
                queue.append(x)
        cur[w] = set()
    C = list(alive)
    if 2 * len(C) >= e:
        return C, "spread: m-core"
    # Label out-edges; each label class is a rooted forest (parent = head).
    classes = {}
    for w, outs in out.items():
        assert len(outs) <= m - 1
        for ell, E in enumerate(outs):
            (x,) = E - {w}
            classes.setdefault(ell, {})[w] = (x, E)

    def depth(par, v):
        d = 0
        while v in par:
            v = par[v][0]
            d += 1
        return d

    best = []
    for par in classes.values():
        for parity in (0, 1):
            S = [(par[w][0], w, par[w][1]) for w in par if depth(par, w) % 2 == parity]
            if len(S) > len(best):
                best = S
    S = best
    stars = {}
    for centre, leaf, E in S:
        stars.setdefault(centre, []).append(E)
    # Vertex-disjointness of the chosen star forest (asserted, part of the proof).
    used = {}
    for centre, es in stars.items():
        for E in es:
            for v in E:
                assert used.setdefault(v, centre) == centre, "star forest not vertex-disjoint"
    big = [es for es in stars.values() if len(es) >= m]
    small = [es for es in stars.values() if len(es) < m]
    big_edges = sum(len(es) for es in big)
    if 2 * big_edges >= len(S):
        if len(big) >= m:
            return [E for es in big for E in es], "spread sparse: >=m big stars"
        return max(big, key=len), "spread sparse: <m big stars, largest big star"
    M = [es[0] for es in small]
    if len(M) >= m:
        return M, "spread sparse: one edge per small star"
    matching, covered = [], set()
    for E in F:
        if not (E & covered):
            matching.append(E)
            covered |= E
    assert len(matching) > m
    return matching, "spread sparse: fallback maximal matching (>m)"


def population():
    for m in (2, 3, 4):
        for N in range(3, 10):
            yield m, f"K_{N}", list(combinations(range(N), 2))
        for a, b in ((1, 8), (2, 5), (3, 3), (4, 4)):
            yield m, f"K_({a},{b})", [(i, a + j) for i in range(a) for j in range(b)]
        yield m, "K_(1,12)", [(0, j) for j in range(1, 13)]
        yield m, "P_10", [(i, i + 1) for i in range(9)]
        yield m, "C_9", [(i, (i + 1) % 9) for i in range(9)]
        if m >= 3:
            for copies in (3, 4):
                s = m - 1
                es = []
                for c in range(copies):
                    base = c * 2 * s
                    es += [(base + i, base + s + j) for i in range(s) for j in range(s)]
                yield m, f"{copies}xK_({s},{s})", es
        yield m, "K_(1,10)+3K_2", [(0, j) for j in range(1, 11)] + [(20, 21), (22, 23), (24, 25)]
        for seed in range(5):
            rng = random.Random(seed)
            es = [p for p in combinations(range(10), 2) if rng.random() < 0.35]
            yield m, f"G(10,0.35) seed {seed}", es


def main():
    start = time.time()
    count = 0
    for m, name, es in population():
        if not es:
            print(f"SKIP empty m={m} {name}")
            continue
        H, branch = extract(es, m)
        F = semantics.family([sorted(E) for E in es])
        Hs = semantics.family([sorted(E) for E in H])
        assert set(Hs) <= set(F) and Hs, (m, name)
        assert 8 * m * m * len(Hs) >= len(F), (m, name, len(Hs), len(F))
        assert semantics.internal_by_links(Hs, m), (m, name, branch)
        count += 1
        print(f"PASS m={m} {name}: |F|={len(F)} |H|={len(Hs)} [{branch}]")
    elapsed = time.time() - start
    assert elapsed <= 10
    print(f"ALL {count} PASS in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
