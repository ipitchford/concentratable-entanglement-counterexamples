"""Reviewer check using Pauli coefficients; imports no submission code."""
from fractions import Fraction as Q
from itertools import product
import argparse
import json
from pathlib import Path


def check(condition, message):
    if not condition:
        raise ValueError(message)


def pauli_stats(coefficients):
    n = len(next(iter(coefficients)))
    norm = sum((v*v for v in coefficients.values()), Q(0))
    weighted = sum((v*v / 3**sum(c != 'I' for c in s)
                    for s, v in coefficients.items()), Q(0))
    purity = norm / 2**n
    f = Q(3, 4)**n * weighted
    return purity, f, (1 + purity)/2 - f


bell = {'II': Q(1), 'XX': Q(1), 'YY': Q(-1), 'ZZ': Q(1)}
mixed = {p + 'I': v for p, v in bell.items()}
r, f, upper = pauli_stats(mixed)
check((r, f, upper) == (Q(1, 2), Q(9, 16), Q(3, 16)), 'Witness mismatch')

# Arbitrary non-axial pure spectator, including a nonzero Y coefficient.
bloch = {'I': Q(1), 'X': Q(1, 3), 'Y': Q(2, 3), 'Z': Q(2, 3)}
check(sum(bloch[p]**2 for p in 'XYZ') == 1, 'Bloch vector not pure')
rp, fp, up = pauli_stats({p+s: v*b for p,v in bell.items() for s,b in bloch.items()})
check((rp, 1-fp, up) == (1, Q(1,4), Q(1,4)), 'Complex spectator mismatch')

family = []
for epsilon in [Q(0), Q(1, 1000), Q(1, 10), Q(1, 2), Q(9, 10), Q(1)]:
    coeff = {p+s: v*b for p,v in bell.items()
             for s,b in {'I': Q(1), 'Z': 1-2*epsilon}.items()}
    purity, f_value, u_value = pauli_stats(coeff)
    check(Q(1,4)-u_value == epsilon*(1-epsilon)/4, 'Near-pure mismatch')
    family.append({'epsilon':str(epsilon), 'purity':str(purity), 'F':str(f_value), 'U':str(u_value)})

ratios = []
for k in range(1, 9):
    coeff = {''.join(items)+'I': Q((-1)**items.count('YY'))
             for items in product(bell, repeat=k)}
    purity, f_value, u_value = pauli_stats(coeff)
    roof_from_support = 1-Q(3,4)**k
    ratio = (roof_from_support-u_value)/(1-purity)
    check(ratio == (1-Q(3,4)**k)/2, 'Sharpness sequence mismatch')
    check(roof_from_support <= u_value+(Q(1,2)-Q(1,2**(2*k+1)))*(1-purity),
          'Fixed-size bound mismatch')
    ratios.append({'k':k, 'n':2*k+1, 'gap_over_impurity':str(ratio)})

# Bell and spectator local-SWAP distributions factor directly.
dist = {core+spectator: pc*ps for core,pc in {'00':Q(3,4),'11':Q(1,4)}.items()
        for spectator,ps in {'0':Q(3,4),'1':Q(1,4)}.items()}
check(sum(dist.values()) == 1, 'Distribution not normalised')
check(sum(v for s,v in dist.items() if s != '000' and s.count('1')%2 == 0) == upper,
      'Even probability mismatch')
report = {'status':'PASS', 'method':'Pauli orthogonality and weight enumeration; no submission imports',
          'witness':{'purity':str(r),'F':str(f),'U':str(upper),'roof_from_analytic_support_proof':'1/4'},
          'non_axial_pure_spectator':{p:str(v) for p,v in bloch.items()},
          'near_pure_family':family,'sharpness_sequence':ratios,
          'swap_distribution':{s:str(v) for s,v in dist.items()},
          'limits':'Finite checks only; roof equality and uniform sharpness require the analytic arguments.'}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--json', type=Path, help='Optional destination for the result')
args = parser.parse_args()
if args.json is not None:
    args.json.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
