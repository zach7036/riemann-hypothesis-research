#!/usr/bin/env python3
"""Verify the finite-rank algebra behind complementary-band Hankel detectors.

This script proves/checks algebraic identities only. It does not establish the
analytic explicit-formula transfer or observability for arbitrary zeta-zero
clusters.
"""
from __future__ import annotations

import cmath
import itertools
import math
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent


def binary_symbolic() -> sp.Expr:
    b1, b2, z1, z2 = sp.symbols("b1 b2 z1 z2")
    for r in range(8):
        s = lambda n: b1 * z1**n + b2 * z2**n
        lhs = sp.expand(s(r) * s(r + 2) - s(r + 1) ** 2)
        rhs = sp.expand(b1 * b2 * (z1 * z2) ** r * (z1 - z2) ** 2)
        assert sp.simplify(lhs - rhs) == 0
    return rhs


def hankel_moment(weights, nodes, n):
    return sum(w * z**n for w, z in zip(weights, nodes))


def hankel_det(weights, nodes, K: int, r: int):
    mat = sp.Matrix([
        [hankel_moment(weights, nodes, r + i + j) for j in range(K)]
        for i in range(K)
    ])
    return sp.factor(mat.det())


def vandermonde_sq(nodes):
    out = sp.Integer(1)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            out *= (nodes[j] - nodes[i]) ** 2
    return sp.expand(out)


def exact_k_node_checks() -> list[str]:
    report = []
    examples = {
        2: ([sp.Rational(2, 3), sp.Rational(5, 7)], [sp.Integer(2), sp.Integer(5)]),
        3: ([sp.Rational(1, 2), sp.Rational(3, 5), sp.Rational(7, 11)], [sp.Integer(1), sp.Integer(3), sp.Integer(6)]),
        4: ([sp.Rational(2, 5), sp.Rational(4, 7), sp.Rational(5, 9), sp.Rational(8, 13)], [sp.Integer(1), sp.Integer(2), sp.Integer(4), sp.Integer(7)]),
    }
    for K, (weights, nodes) in examples.items():
        for r in (0, 1, 3):
            det = hankel_det(weights, nodes, K, r)
            expected = sp.prod(weights) * sp.prod(nodes) ** r * vandermonde_sq(nodes)
            assert sp.simplify(det - expected) == 0
        report.append(f"exact {K}-node Hankel--Vandermonde checks passed")
    return report


def cauchy_binet_check() -> str:
    weights = [sp.Rational(2, 3), sp.Rational(3, 4), sp.Rational(5, 6), sp.Rational(7, 8)]
    nodes = [sp.Integer(1), sp.Integer(2), sp.Integer(4), sp.Integer(7)]
    K, r = 3, 2
    lhs = hankel_det(weights, nodes, K, r)
    rhs = sp.Integer(0)
    for subset in itertools.combinations(range(len(nodes)), K):
        ws = [weights[i] for i in subset]
        zs = [nodes[i] for i in subset]
        rhs += sp.prod(ws) * sp.prod(zs) ** r * vandermonde_sq(zs)
    assert sp.simplify(lhs - rhs) == 0
    return "many-node Cauchy--Binet subset expansion passed"


def total_harmonic_checks() -> str:
    for K in range(1, 8):
        for r in range(5):
            totals = {
                sum(r + i + perm[i] for i in range(K))
                for perm in itertools.permutations(range(K))
            }
            assert totals == {K * r + K * (K - 1)}
    return "determinant monomials conserve total harmonic"


def alias_breaking_examples() -> list[str]:
    report = []
    for M in (4, 6, 8, 10):
        r = M // 2 - 1
        z1 = 1.0 + 0.0j
        z2 = cmath.exp(1j * math.pi / M)
        s = lambda n: z1**n + z2**n
        assert abs(s(M)) < 1e-12
        minor = s(r) * s(r + 2) - s(r + 1) ** 2
        expected = (z1 * z2) ** r * (z1 - z2) ** 2
        assert abs(minor - expected) < 1e-12
        assert abs(minor) > 1e-5
        report.append(f"M={M}: linear critical moment cancels, minor magnitude={abs(minor):.12g}")
    return report


def main() -> None:
    report = ["COMPLEMENTARY HANKEL VERIFICATION", "=" * 33, ""]
    binary_symbolic()
    report.append("binary complementary-minor identity passed for r=0,...,7")
    report.extend(exact_k_node_checks())
    report.append(cauchy_binet_check())
    report.append(total_harmonic_checks())
    report.extend(alias_breaking_examples())
    report.append("")
    report.append("All finite-rank algebra checks passed.")
    text = "\n".join(report) + "\n"
    (HERE / "verification.txt").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
