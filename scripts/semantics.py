"""Small exact semantic checks. Not a discovery engine or a theorem proof."""
from itertools import combinations


def family(rows):
    edges = tuple(frozenset(row) for row in rows)
    if any(len(edge) != len(row) for edge, row in zip(edges, rows)):
        raise ValueError("Repeated vertex in an edge")
    if len(set(edges)) != len(edges):
        raise ValueError("Family must have distinct members")
    if edges and len({len(edge) for edge in edges}) != 1:
        raise ValueError("Family must be uniform")
    return edges


def has_exact_sunflower(edges, m, kernel):
    if m < 2:
        raise ValueError("At least two distinct petals are required")
    return any(all(a & b == kernel for a, b in combinations(petals, 2))
               for petals in combinations(edges, m))


def witnessed(selected, witnesses, m):
    """selected=H; witnesses=H for internal, F for external semantics."""
    if m < 2:
        raise ValueError("m must be at least two")
    if not set(selected) <= set(witnesses):
        raise ValueError("Selected family must lie in witness family")
    return all(has_exact_sunflower(witnesses, m, a & b)
               for a, b in combinations(selected, 2))


def internal_by_links(edges, m):
    if m < 2:
        raise ValueError("m must be at least two")
    kernels = {a & b for a, b in combinations(edges, 2)}
    for kernel in kernels:
        link = tuple(edge - kernel for edge in edges if kernel <= edge)
        if not any(all(a.isdisjoint(b) for a, b in combinations(matching, 2))
                   for matching in combinations(link, m)):
            return False
    return True
