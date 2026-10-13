#!/usr/bin/env python3
"""Exact extension identities; finite checks do not verify roof/GME proofs.

Requires SymPy 1.14.0. Run with --negative-controls to require rejection of
specified semantic mutants. Uses explicit exceptions and works under python -O.
"""
import argparse
import itertools
import json
import platform
import sympy as S

Q = S.Rational
CHECKS = []
MUTANTS = []


def equal(label, actual, expected):
    if S.simplify(actual - expected) != 0:
        raise ValueError(f"{label}: exact equality failed")
    CHECKS.append(label)


def positive(label, value):
    if S.simplify(value).is_positive is not True:
        raise ValueError(f"{label}: strict positivity failed")
    CHECKS.append(label)


def reject(label, actual, incorrect):
    if S.simplify(actual - incorrect) == 0:
        raise ValueError(f"mutant survived: {label}")
    MUTANTS.append(label)


def partial(rho, keep, n):
    """Contract matrix entries by separately enumerating kept/traced bits."""
    keep = tuple(keep)
    traced = tuple(j for j in range(n) if j not in keep)
    out = S.zeros(2 ** len(keep))
    def index(kbits, tbits):
        bits = dict(zip(keep, kbits))
        bits.update(zip(traced, tbits))
        return sum(bits[j] * 2 ** (n - 1 - j) for j in range(n))
    words = list(itertools.product((0, 1), repeat=len(keep)))
    for i, left in enumerate(words):
        for j, right in enumerate(words):
            out[i, j] = sum(rho[index(left, rest), index(right, rest)]
                            for rest in itertools.product((0, 1), repeat=len(traced)))
    return out


def purities(rho, n):
    result = {}
    for size in range(n + 1):
        for subset in itertools.combinations(range(n), size):
            red = partial(rho, subset, n)
            result[subset] = S.expand(S.trace(red * red))
    return result


def gme():
    z, t, a, b, d, c, s = S.symbols('z t a b d c s', real=True)
    v0, v1 = S.zeros(8, 1), S.zeros(8, 1)
    v0[0] = v0[6] = 1 / S.sqrt(2)
    v1[1] = v1[7] = c / S.sqrt(2)
    v1[2] = s
    rho = (v0 * v0.T + v1 * v1.T) / 2
    p = {k: S.expand(v).subs(c*c, 1-z).subs(s*s, z).expand()
         for k, v in purities(rho, 3).items()}
    expected = [1, Q(1,2)+z*z/8, Q(1,2)+z*z/8,
                Q(1,2)+z*z/2, 1-z+z*z/2,
                Q(1,4)+z/4+z*z/8, Q(1,4)+z/4+z*z/8, Q(1,2)]
    for (subset, value), target in zip(p.items(), expected):
        equal(f'gme mixed purity {subset}', value, target)
    u = (1+p[(0,1,2)])/2-sum(p.values())/8
    equal('gme U polynomial', u, Q(3,16)+z/16-3*z*z/16)
    # Global phase permits the coefficient of v0 to be real. b+id is arbitrary.
    vec = a*v0+(b+S.I*d)*v1
    pure = vec * S.conjugate(vec.T)
    ideal = S.groebner([a*a-(1-t), b*b+d*d-t, c*c-(1-z), s*s-z],
                      a,b,c,s,d,t,z, domain=S.QQ)
    targets = [Q(1,2)+t*(1-t)*z+t*t*z*z/2]*2+[1-2*t*t*z*(1-z)]
    for j, target in enumerate(targets):
        red = partial(pure, (j,), 3)
        remainder = ideal.reduce(S.expand(S.trace(red*red)-target))[1]
        equal(f'gme all-phase pure marginal {j}', remainder, 0)
    f = (3-sum(targets))/4
    equal('gme pure CE polynomial', f, Q(1,4)-z*t/2+z*(1-3*z/4)*t*t)
    cup, cap = f.subs(t,Q(1,2)), (f.subs(t,0)+f.subs(t,1))/2
    equal('gme Jensen value', cup, Q(1,4)-3*z*z/16)
    equal('gme chord value', cap, Q(1,4)+z/4-3*z*z/8)
    equal('gme deficit polynomial', cup-u, (1-z)/16)
    equal('gme midpoint cup', cup.subs(z,Q(1,2)), Q(13,64))
    equal('gme midpoint cap', cap.subs(z,Q(1,2)), Q(9,32))
    equal('gme midpoint U', u.subs(z,Q(1,2)), Q(11,64))
    return p, u, cup, cap, z


def ghz():
    # Direct entries on GHZ support; any nonempty proper marginal is diag(1/2,1/2).
    for n in range(2,9):
        e = Q(1,2)-Q(1,2**n)
        for q in [Q(1,7), Q(1,3), Q(1,2), Q(4,5)]:
            logical = S.Matrix([[Q(1,2), q-Q(1,2)], [q-Q(1,2), Q(1,2)]])
            purity = S.trace(logical*logical)
            equal(f'GHZ n{n} q{q} spectrum purity', purity, q*q+(1-q)**2)
            f = (1+(2**n-2)*Q(1,2)+purity)/2**n
            u = (1+purity)/2-f
            equal(f'GHZ n{n} q{q} sharp ratio', (e-u)/(1-purity), e)


def noisy():
    q = S.symbols('q', real=True)
    bell = S.Matrix([1,0,0,1])/S.sqrt(2)
    sigma = q*bell*bell.T+(1-q)*S.eye(4)/4
    rho = S.kronecker_product(sigma,S.eye(2)/2)
    p = purities(rho,3)
    u = (1+p[(0,1,2)])/2-sum(p.values())/8
    equal('noisy total purity', p[(0,1,2)], (1+3*q*q)/8)
    equal('noisy F', sum(p.values())/8, (27+9*q*q)/64)
    equal('noisy U', u, (9+3*q*q)/64)
    y = S.Matrix([[0,-S.I],[S.I,0]])
    yy = S.kronecker_product(y,y)
    for entry in yy*S.conjugate(sigma)*yy-sigma:
        equal('noisy spin flip entry', entry, 0)
    char = sigma.charpoly().as_expr()
    lam = next(iter(char.free_symbols-{q}))
    equal('noisy characteristic polynomial',char,
          (lam-(1+3*q)/4)*(lam-(1-q)/4)**3)
    cup = (3*q-1)**2/16  # Entangled branch q>=1/3 only.
    gap = cup-u
    equal('noisy gap polynomial',gap,(33*q*q-24*q-5)/64)
    root=(12+S.sqrt(309))/33
    equal('noisy threshold root',gap.subs(q,root),0)
    positive('threshold above 1/3',root-Q(1,3))
    positive('threshold below one',1-root)
    equal('q9/10 gap',gap.subs(q,Q(9,10)),Q(13,6400))
    equal('q19/20 gap',gap.subs(q,Q(19,20)),Q(793,25600))
    delta=Q(1,200)
    radius_bound=(Q(37,40)-2*delta)**2/4-Q(4683,25600)-2*delta
    equal('arbitrary perturbation radius deficit',radius_bound,Q(10481,640000))
    positive('radius deficit positive',radius_bound)
    equal('radius minimum eigenvalue',Q(1,160)-delta,Q(1,800))
    return u, q


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative-controls',action='store_true')
    args=parser.parse_args()
    if S.__version__ != '1.14.0':
        raise RuntimeError('Requires exactly SymPy 1.14.0')
    p,u,cup,cap,z=gme()
    ghz()
    noisy_u,q=noisy()
    if args.negative_controls:
        point={z:Q(1,2)}
        reject('omit empty-subsystem term',u.subs(point),(u+p[()]/8).subs(point))
        reject('omit full-subsystem term',u.subs(point),(u+p[(0,1,2)]/8).subs(point))
        reject('count all nonzero parity as even',u.subs(point),(u+(1-p[(0,1,2)])/2).subs(point))
        reject('swap convex and concave roof',cup.subs(point),cap.subs(point))
        reject('wrong quadratic roof coefficient',cup.subs(point),(Q(1,4)-z*z/16).subs(point))
        # GHZ n=3,q=1/2 requires coefficient 3/8, so 1/4 genuinely fails.
        ghz_cap,ghz_u,impurity=Q(3,8),Q(3,16),Q(1,2)
        positive('smaller concave correction rejected',ghz_cap-(ghz_u+Q(1,4)*impurity))
        MUTANTS.append('replace sharp concave coefficient 3/8 by 1/4')
        reject('replace three-qubit statistic by two-qubit core statistic',
               noisy_u.subs(q,Q(9,10)),(1+3*Q(9,10)**2)/16)
    print(json.dumps({'status':'PASS','python':platform.python_version(),
       'sympy':S.__version__,'checks':len(CHECKS),'check_labels':CHECKS,
       'negative_controls_requested':args.negative_controls,
       'rejected_mutants':MUTANTS,
       'scope':'Exact symbolic identities and finite rational checks. Does not verify analytic support, GME, Jensen, roof optimization, Wootters theorem, continuity, novelty, or REF significance.'},indent=2))


if __name__=='__main__':
    main()
