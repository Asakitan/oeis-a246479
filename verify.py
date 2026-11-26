"""A246479. Exact polynomial-identity certificate, using only Python integers."""
from itertools import product


def canonical(word):
    mapping = {}
    for x in word:
        if x and x not in mapping:
            mapping[x] = len(mapping) + 1
    return tuple(mapping.get(x, 0) for x in word)


def quotient(k):
    odd = k % 2
    states = sorted({canonical(w) for w in product(range(odd, 4), repeat=3)
                     if w.count(0) <= 1})
    matrix = [[0]*len(states) for _ in states]
    for i, w in enumerate(states):
        distinct = len(set(w) - {0})
        choices = [(a, 1) for a in range(1, distinct+1)]
        choices += [(distinct+1, k + odd - 2*distinct)]
        if not odd and 0 not in w:
            choices += [(0, 1)]
        for a, multiplicity in choices:
            j = states.index(canonical(w[1:] + (a,)))
            matrix[i][j] += multiplicity
    return states, matrix


def recurrence(k):
    if k % 2:
        return [k-2, 2, k-2, 1]
    return [k-3, 2, k-3, k**3-6*k*k+15*k-13, 3*k*k-11*k+13,
            k**3-7*k*k+19*k-19, k*k-4*k+6, 1, k-2, 1]


def residual(k):
    states, matrix = quotient(k)
    c = recurrence(k)
    powers = [[1]*len(states)]
    for _ in c:
        powers.append([sum(a*b for a, b in zip(row, powers[-1]))
                       for row in matrix])
    return [w - sum(a*v[i] for a, v in zip(c, powers[-2::-1]))
            for i,w in enumerate(powers[-1])]


if __name__ == "__main__":
    for first, degree in ((5, 4), (6, 10)):
        samples = range(first, first+2*(degree+1), 2)
        for k in samples:
            r = residual(k)
            if any(r):
                raise AssertionError((k,r))
        print(f"k={list(samples)}: polynomial-vector identity, "
              f"{len(r)} components, degree <= {degree}, verified.")
