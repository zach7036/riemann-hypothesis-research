#!/usr/bin/env python3
"""Compact independent symbolic audit of the closed-form hierarchy."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
s2 = sp.sqrt(2)
K, r, c = sp.symbols("K r c", real=True)
C = 2 + s2
A = 3 - 2 * s2
d = K - 1
B = A * d
alpha = C**2 / (r + 1)
beta = C**2 * (r - 1) / (2 * (r + 1))
alpha_d = 2 * C - K
beta_d = K - 1
gamma_d = alpha_d * (r + 1) + beta_d - C**2
a = 1 - d * (s2 - 1)
h = A * d / (r - 1)
b = (1 - a - (r + 1) * h) / 2

checks = {
    "balance_C": sp.simplify(C**2 - 2 * (2 * C - 1)) == 0,
    "alpha_plus_beta": sp.simplify(alpha + beta - C**2 / 2) == 0,
    "multiset_formula": sp.simplify((2*C-K-alpha)/beta - (1-B*(r+1)/(r-1))) == 0,
    "distinct_formula": sp.simplify(beta_d/gamma_d - B/(r-1-r*B)) == 0,
    "sharp_total_count": sp.simplify(a + (r+1)*h + 2*b - 1) == 0,
    "sharp_multiset_mass": sp.simplify(a + 2*b - (1-A*d*(r+1)/(r-1))) == 0,
    "sharp_distinct_ratio": sp.simplify(h/(a+h+2*b) - A*d/(r-1-r*A*d)) == 0,
    "sharp_square": sp.simplify(
        a*(2*c-1) + h*c**2 + b*c**2 - (2*c-K)
        - (h+b)*(c-C)**2
    ) == 0,
}
assert all(checks.values()), checks
(HERE / "symbolic_audit.json").write_text(json.dumps(checks, indent=2) + "\n")
(HERE / "symbolic_audit.txt").write_text(
    "LOW-MULTIPLICITY SYMBOLIC AUDIT\n" + "="*33 + "\n\n" +
    json.dumps(checks, indent=2) + "\n\nAll assertions passed.\n"
)
print("All symbolic identities passed.")
