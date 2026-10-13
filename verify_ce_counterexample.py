#!/usr/bin/env python3
"""Exact arithmetic checks for a CE upper-bound counterexample.

Python >=3.9, standard library only. No floating-point computations.
Run: python3 verify_ce_counterexample.py [--json verification.json]

Two implementations are compared:
  (1) explicit matrix partial traces and subsystem purities;
  (2) local-swap permutations acting on two copies, followed by the
      exact Fourier transform giving all SWAP-test probabilities.

This checks the finite arithmetic certificate, not the analytic theorem
quantifying over all pure-state decompositions. See proof.pdf/proof.tex
for that support argument and the sharp universal correction theorem.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

Matrix = List[List[Q]]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def zeros(d: int) -> Matrix:
    return [[Q(0) for _ in range(d)] for _ in range(d)]


def trace(a: Matrix) -> Q:
    return sum((a[i][i] for i in range(len(a))), Q(0))


def purity(a: Matrix) -> Q:
    return sum((a[i][j] * a[j][i]
                for i in range(len(a)) for j in range(len(a))), Q(0))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    d = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(d)), Q(0))
             for j in range(d)] for i in range(d)]


def scale(q: Q, a: Matrix) -> Matrix:
    return [[q * x for x in row] for row in a]


def kron(a: Matrix, b: Matrix) -> Matrix:
    da, db = len(a), len(b)
    return [[a[i // db][j // db] * b[i % db][j % db]
             for j in range(da * db)] for i in range(da * db)]


def bits(x: int, n: int) -> Tuple[int, ...]:
    return tuple((x >> (n - 1 - site)) & 1 for site in range(n))


def select_index(xbits: Sequence[int], keep: Sequence[int]) -> int:
    out = 0
    for site in keep:
        out = 2 * out + xbits[site]
    return out


def partial_trace(rho: Matrix, n: int, keep: Sequence[int]) -> Matrix:
    require(len(rho) == 2**n, 'Incorrect matrix dimension')
    require(tuple(keep) == tuple(sorted(set(keep))), 'Invalid subsystem')
    require(all(0 <= site < n for site in keep), 'Invalid qubit index')
    drop = tuple(site for site in range(n) if site not in keep)
    out = zeros(2**len(keep))
    for i in range(2**n):
        ib = bits(i, n)
        for j in range(2**n):
            jb = bits(j, n)
            if all(ib[k] == jb[k] for k in drop):
                out[select_index(ib, keep)][select_index(jb, keep)] += rho[i][j]
    return out


def all_purities(rho: Matrix, n: int) -> Dict[int, Q]:
    return {mask: purity(partial_trace(
                rho, n, tuple(site for site in range(n) if mask & (1 << site))))
            for mask in range(2**n)}


def mean_purity(rho: Matrix, n: int) -> Q:
    return sum(all_purities(rho, n).values(), Q(0)) / 2**n


def proposed_upper(rho: Matrix, n: int) -> Q:
    return (1 + purity(rho)) / 2 - mean_purity(rho, n)


def bell_projector() -> Matrix:
    out = zeros(4)
    for i in (0, 3):
        for j in (0, 3):
            out[i][j] = Q(1, 2)
    return out


def witness(epsilon: Q = Q(1, 2)) -> Matrix:
    require(Q(0) <= epsilon <= Q(1), 'epsilon must lie in [0, 1]')
    tau = [[1 - epsilon, Q(0)], [Q(0), epsilon]]
    return kron(bell_projector(), tau)


def direct_swap_expectation(rho: Matrix, n: int, mask: int) -> Q:
    """Tr[(rho tensor rho) S_mask], without using partial traces."""
    out = Q(0)
    for x in range(2**n):
        for y in range(2**n):
            xp, yp = x, y
            for site in range(n):
                if mask & (1 << site):
                    bit = 1 << (n - 1 - site)
                    if bool(x & bit) != bool(y & bit):
                        xp ^= bit
                        yp ^= bit
            out += rho[x][xp] * rho[y][yp]
    return out


def swap_distribution(rho: Matrix, n: int) -> Dict[int, Q]:
    expectations = [direct_swap_expectation(rho, n, mask)
                    for mask in range(2**n)]
    return {z: sum(((-1)**bin(z & mask).count('1') * expectations[mask]
                    for mask in range(2**n)), Q(0)) / 2**n
            for z in range(2**n)}


def outcome_label(mask: int, n: int) -> str:
    return ''.join('1' if mask & (1 << site) else '0' for site in range(n))


def main() -> Dict[str, object]:
    rho = witness()
    require(trace(rho) == 1, 'State is not normalised')
    require(rho == [list(row) for row in zip(*rho)], 'State is not symmetric')
    # Positivity also follows directly from the nonnegative weighted sum
    # of orthogonal rank-one projectors used in witness().
    projector = scale(Q(2), rho)
    require(multiply(projector, projector) == projector, 'Support is not a projector')
    require(trace(projector) == 2, 'Support rank is not two')
    require(multiply(rho, rho) == scale(Q(1, 2), rho), 'Spectrum check failed')

    p = all_purities(rho, 3)
    expected = {0: Q(1), 1: Q(1, 2), 2: Q(1, 2), 4: Q(1, 2),
                3: Q(1), 5: Q(1, 4), 6: Q(1, 4), 7: Q(1, 2)}
    require(p == expected, 'Subsystem purity table does not match')
    require(sum(p.values(), Q(0)) == Q(9, 2), 'Purity sum is not 9/2')
    require(mean_purity(rho, 3) == Q(9, 16), 'Mean purity is not 9/16')
    require(proposed_upper(rho, 3) == Q(3, 16), 'Upper statistic is not 3/16')

    # Representative pure states in the support. The full universal
    # statement about the support is proved analytically in the note.
    for a, b in [(Q(1), Q(0)), (Q(0), Q(1)), (Q(3, 5), Q(4, 5))]:
        tau = [[a*a, a*b], [a*b, b*b]]
        pure_rho = kron(bell_projector(), tau)
        require(purity(pure_rho) == 1, 'Support sample is not pure')
        require(1 - mean_purity(pure_rho, 3) == Q(1, 4), 'Support CE check failed')

    dist = swap_distribution(rho, 3)
    for mask, value in p.items():
        require(direct_swap_expectation(rho, 3, mask) == value,
                'Direct swap and partial trace disagree')
    expected_dist = {'000': Q(9, 16), '001': Q(3, 16), '010': Q(0),
                     '011': Q(0), '100': Q(0), '101': Q(0),
                     '110': Q(3, 16), '111': Q(1, 16)}
    labelled_dist = {outcome_label(z, 3): prob for z, prob in dist.items()}
    require(labelled_dist == expected_dist, 'Swap outcome table does not match')
    require(sum(dist.values(), Q(0)) == 1, 'Swap distribution does not normalise')
    require(all(prob >= 0 for prob in dist.values()), 'Negative outcome probability')
    even = sum((prob for z, prob in dist.items()
                if z != 0 and bin(z).count('1') % 2 == 0), Q(0))
    odd = sum((prob for z, prob in dist.items()
               if bin(z).count('1') % 2 == 1), Q(0))
    require(even == Q(3, 16) and odd == Q(1, 4), 'Parity probabilities failed')

    family = []
    for eps in [Q(0), Q(1, 1000), Q(1, 10), Q(1, 2), Q(9, 10), Q(1)]:
        state = witness(eps)
        r = (1-eps)**2 + eps**2
        upper = proposed_upper(state, 3)
        gap = Q(1, 4) - upper
        require(purity(state) == r, 'Family purity identity failed')
        require(upper == (1 + r) / 8, 'Family upper identity failed')
        require(gap == eps * (1-eps) / 4, 'Family gap identity failed')
        family.append({'epsilon': str(eps), 'purity': str(r),
                       'proposed_upper': str(upper), 'gap': str(gap)})

    # Matrix check of the two-Bell-pair construction (four pure qubits).
    two_bells = kron(bell_projector(), bell_projector())
    require(1 - mean_purity(two_bells, 4) == 1 - Q(3, 4)**2,
            'Bell-product CE identity failed')
    two_bells_mixed = kron(two_bells, [[Q(1, 2), Q(0)], [Q(0), Q(1, 2)]])
    require(proposed_upper(two_bells_mixed, 5) == Q(3, 4)*(1-Q(3, 4)**2),
            'Five-qubit spectator identity failed')

    output: Dict[str, object] = {
        'status': 'PASS',
        'arithmetic': 'Python fractions.Fraction; no floating point',
        'matrix_basis_order': ['000','001','010','011','100','101','110','111'],
        'rho': [[str(x) for x in row] for row in rho],
        'support_rank': 2,
        'subset_purities': {
            ''.join('ABC'[site] for site in range(3) if mask & (1 << site)) or 'empty': str(value)
            for mask, value in p.items()},
        'purity_sum': '9/2', 'global_purity': '1/2',
        'mean_subsystem_purity': '9/16', 'proposed_upper': '3/16',
        'roof_value_from_support_proof': '1/4', 'violation': '1/16',
        'swap_probabilities': {label: str(labelled_dist[label])
                               for label in sorted(labelled_dist)},
        'nonzero_even_probability': str(even), 'odd_probability': str(odd),
        'rational_family_checks': family,
        'scope': ('Finite arithmetic certificate and sample consistency checks. '
                  'All-decomposition and all-dimension claims use the analytic proofs, '
                  'not numerical optimisation or sampling.')
    }
    print(json.dumps(output, indent=2))
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='Optional destination for the exact report')
    args = parser.parse_args()
    report = main()
    if args.json is not None:
        args.json.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
