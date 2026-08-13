#!/usr/bin/env python3
"""Exact certificate for the low-multiplicity zeta-zero hierarchy.

This script uses only Python's standard library and exact Fraction arithmetic.
It rigorously encloses

    kappa_MT = 1/2 + (1/sqrt(2))*cot(1/sqrt(2))
             = 1/2 + cos(1/sqrt(2)) / (sin(1/sqrt(2))/(1/sqrt(2)))

by alternating Taylor series with rational terms.  It then produces rigorous
lower bounds for the multiset and distinct-location cutoff profiles, together
with rigorous upper bounds for exact multiplicities.

The symbolic proof of the general formulas is in the accompanying manuscript;
this script certifies the displayed decimal constants.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path
from typing import Tuple

DIGITS = 90
TAYLOR_TERMS = 28  # last index; far more than needed for 60 digits


def alternating_bounds(terms: list[Fraction]) -> Tuple[Fraction, Fraction]:
    """Bounds an alternating series by consecutive even/odd partial sums.

    terms[n] is the positive magnitude a_n in sum (-1)^n a_n, assumed
    decreasing.  For a positive alternating series, odd-index partial sums are
    lower bounds and even-index partial sums are upper bounds.
    """
    partial = Fraction(0)
    lower = None
    upper = None
    for n, a in enumerate(terms):
        if n and not (a <= terms[n - 1]):
            raise AssertionError("terms are not decreasing")
        partial += a if n % 2 == 0 else -a
        if n % 2 == 0:
            upper = partial
        else:
            lower = partial
    if lower is None or upper is None or not lower < upper:
        raise AssertionError("failed to form alternating bounds")
    return lower, upper


def kappa_interval() -> Tuple[Fraction, Fraction]:
    # cos(1/sqrt(2)) = sum (-1)^n / (2^n (2n)!)
    cos_terms = [Fraction(1, 2**n * factorial(2 * n)) for n in range(TAYLOR_TERMS + 1)]
    # sin(x)/x at x=1/sqrt(2) = sum (-1)^n / (2^n (2n+1)!)
    sinc_terms = [Fraction(1, 2**n * factorial(2 * n + 1)) for n in range(TAYLOR_TERMS + 1)]
    c_lo, c_hi = alternating_bounds(cos_terms)
    s_lo, s_hi = alternating_bounds(sinc_terms)
    if not (0 < c_lo < c_hi and 0 < s_lo < s_hi):
        raise AssertionError("positive denominator enclosure failed")
    # ratio C/S: lower C_lo/S_hi, upper C_hi/S_lo
    return Fraction(1, 2) + c_lo / s_hi, Fraction(1, 2) + c_hi / s_lo


def sqrt2_interval(digits: int = DIGITS) -> Tuple[Fraction, Fraction]:
    q = 10**digits
    n = isqrt(2 * q * q)
    lo = Fraction(n, q)
    hi = Fraction(n + 1, q)
    assert lo * lo < 2 < hi * hi
    return lo, hi


def frac_decimal_floor(x: Fraction, places: int) -> str:
    """Decimal truncated downward for nonnegative x."""
    if x < 0:
        raise ValueError("expected nonnegative")
    scale = 10**places
    n = (x.numerator * scale) // x.denominator
    whole, rem = divmod(n, scale)
    return f"{whole}.{rem:0{places}d}"


def frac_decimal_ceil(x: Fraction, places: int) -> str:
    """Decimal rounded upward for nonnegative x."""
    if x < 0:
        raise ValueError("expected nonnegative")
    scale = 10**places
    n = (x.numerator * scale + x.denominator - 1) // x.denominator
    whole, rem = divmod(n, scale)
    return f"{whole}.{rem:0{places}d}"


def bounds_from_kappa(k_hi: Fraction, b_hi: Fraction, r: int) -> tuple[Fraction, Fraction]:
    """Rigorous lower bounds, using worst-case upper enclosures."""
    if r == 1:
        mult = 2 - k_hi
        distinct = 1 - (k_hi - 1) / (3 - k_hi)
    elif r == 2:
        mult = (3 - k_hi) / 2
        distinct = 1 - (k_hi - 1) / (2 * (4 - k_hi))
    else:
        mult = 1 - b_hi * Fraction(r + 1, r - 1)
        denom = Fraction(r - 1) - r * b_hi
        assert denom > 0
        distinct = 1 - b_hi / denom
    return mult, distinct


def exact_multiplicity_upper(k_hi: Fraction, b_hi: Fraction, j: int) -> tuple[Fraction, Fraction]:
    """Rigorous upper bounds for exact multiplicity j, rounded from above later."""
    if j < 2:
        raise ValueError("j must be at least 2")
    if j == 2:
        mult = k_hi - 1
        distinct = (k_hi - 1) / (3 - k_hi)
    elif j == 3:
        mult = (k_hi - 1) / 2
        distinct = (k_hi - 1) / (2 * (4 - k_hi))
    else:
        mult = b_hi * Fraction(j, j - 2)
        denom = Fraction(j - 2) - (j - 1) * b_hi
        assert denom > 0
        distinct = b_hi / denom
    return mult, distinct


def main() -> None:
    k_lo, k_hi = kappa_interval()
    rt2_lo, rt2_hi = sqrt2_interval()
    # A=3-2sqrt(2), so reverse the sqrt bounds.
    a_lo = 3 - 2 * rt2_hi
    a_hi = 3 - 2 * rt2_lo
    assert 0 < a_lo < a_hi
    # B=A(kappa-1), both factors positive.
    b_lo = a_lo * (k_lo - 1)
    b_hi = a_hi * (k_hi - 1)

    lines: list[str] = []
    lines.append("EXACT LOW-MULTIPLICITY CERTIFICATE")
    lines.append("==================================")
    lines.append(f"Taylor last index: {TAYLOR_TERMS}")
    lines.append(f"sqrt(2) enclosure digits: {DIGITS}")
    lines.append("")
    lines.append("Rigorous enclosures (60 decimal places shown):")
    lines.append(f"  {frac_decimal_floor(k_lo, 60)} < kappa_MT < {frac_decimal_ceil(k_hi, 60)}")
    lines.append(f"  {frac_decimal_floor(b_lo, 60)} < B        < {frac_decimal_ceil(b_hi, 60)}")
    lines.append("")
    lines.append("Rigorous lower bounds (15 decimal places, rounded down):")
    lines.append(" r | multiset mass <=r | distinct locations <=r")
    lines.append("---+-------------------+-----------------------")
    for r in range(1, 21):
        m, d = bounds_from_kappa(k_hi, b_hi, r)
        lines.append(f"{r:2d} | {frac_decimal_floor(m, 15)} | {frac_decimal_floor(d, 15)}")

    lines.append("")
    lines.append("Rigorous exact-multiplicity upper bounds (15 decimal places, rounded up):")
    lines.append(" j | multiset mass exactly j | distinct locations exactly j")
    lines.append("---+-------------------------+-----------------------------")
    for j in range(2, 21):
        m, d = exact_multiplicity_upper(k_hi, b_hi, j)
        lines.append(f"{j:2d} | {frac_decimal_ceil(m, 15)} | {frac_decimal_ceil(d, 15)}")

    # Exact complement identities: exact-j upper = high-tail upper at r=j-1.
    for j in range(2, 21):
        low_m, low_d = bounds_from_kappa(k_hi, b_hi, j - 1)
        up_m, up_d = exact_multiplicity_upper(k_hi, b_hi, j)
        assert up_m == 1 - low_m
        assert up_d == 1 - low_d

    # Explicit headline assertions, all exact comparisons.
    targets = {
        1: (Fraction(6725007, 10_000_000), Fraction(8041858, 10_000_000)),
        2: (Fraction(8362503, 10_000_000), Fraction(9387279, 10_000_000)),
        3: (Fraction(8876200, 10_000_000), Fraction(9693190, 10_000_000)),
        4: (Fraction(9063500, 10_000_000), Fraction(9797531, 10_000_000)),
        5: (Fraction(9157150, 10_000_000), Fraction(9848913, 10_000_000)),
    }
    for r, (tm, td) in targets.items():
        m, d = bounds_from_kappa(k_hi, b_hi, r)
        assert m > tm, (r, m, tm)
        assert d > td, (r, d, td)
    lines.append("")
    lines.append("All exact decimal assertions passed.")

    out = Path(__file__).with_name("low_multiplicity_exact_certificate.txt")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
