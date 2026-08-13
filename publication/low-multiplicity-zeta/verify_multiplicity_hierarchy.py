#!/usr/bin/env python3
"""Independent numerical stress test for the low-multiplicity formulas.

The rigorous decimal source is certify_low_multiplicity.py. This script
independently evaluates the formulas and checks the pointwise scalar
majorants over broad finite ranges.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80
K = mp.mpf("0.5") + mp.cot(1 / mp.sqrt(2)) / mp.sqrt(2)
C = 2 + mp.sqrt(2)
B = (3 - 2 * mp.sqrt(2)) * (K - 1)


def kc(c: mp.mpf, m: int) -> mp.mpf:
    return c*c - max(c-m, mp.mpf("0"))**2


def mult_bound(r: int) -> mp.mpf:
    if r == 1:
        return 2-K
    if r == 2:
        return (3-K)/2
    return 1-B*(r+1)/(r-1)


def distinct_bound(r: int) -> mp.mpf:
    if r == 1:
        return 1-(K-1)/(3-K)
    if r == 2:
        return 1-(K-1)/(2*(4-K))
    return 1-B/(r-1-r*B)


def check_majorants(max_r: int = 100, max_m: int = 500) -> None:
    tol = mp.mpf("1e-60")
    for r in range(1, max_r+1):
        if r == 1:
            c, alpha, beta = mp.mpf(2), mp.mpf(2), mp.mpf(1)
        elif r == 2:
            c, alpha, beta = mp.mpf(3), mp.mpf(3), mp.mpf(2)
        else:
            c = C
            alpha = c*c/(r+1)
            beta = c*c*(r-1)/(2*(r+1))
        for m in range(1, max_m+1):
            ind = mp.mpf(1 if m <= r else 0)
            assert kc(c,m) <= alpha*m + beta*m*ind + tol
            assert c*c <= 2*alpha*m + 2*beta*m*ind + tol

        if r == 1:
            c, alpha, beta, gamma = mp.mpf(2), 4-K, K-1, 3-K
        elif r == 2:
            c, alpha, beta, gamma = mp.mpf(3), 6-K, K-1, 2*(4-K)
        else:
            c, alpha, beta = C, 2*C-K, K-1
            gamma = alpha*(r+1)+beta-C*C
        for m in range(1, max_m+1):
            high = mp.mpf(1 if m >= r+1 else 0)
            assert kc(c,m) <= alpha*m + beta - gamma*high + tol
            assert c*c <= 2*alpha*m + 2*beta - 2*gamma*high + tol


def main() -> None:
    check_majorants()
    print("kappa_MT =", mp.nstr(K, 60))
    print("B        =", mp.nstr(B, 60))
    print("pointwise majorants passed for r<=100 and m<=500")
    print("r | multiset lower | distinct lower")
    for r in [1,2,3,4,5,6,8,10,20]:
        print(r, mp.nstr(mult_bound(r), 18), mp.nstr(distinct_bound(r), 18), sep=" | ")


if __name__ == "__main__":
    main()
