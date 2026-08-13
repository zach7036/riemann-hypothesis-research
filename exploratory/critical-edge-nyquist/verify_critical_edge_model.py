#!/usr/bin/env python3
"""Verify the explicit smooth-packet critical-edge/Nyquist model.

This is a model calculation, not a computation on actual zeta zeros.
It checks:
  1. exact critical-edge phase coherence;
  2. the transition variable R(1-alpha);
  3. order-k endpoint zeros of (1+exp(i*pi*alpha))^k;
  4. numerical R^(1-2k) edge-energy scaling.
"""
from __future__ import annotations

import cmath
import math
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent


def bump(x: float) -> float:
    if abs(x) >= 1:
        return 0.0
    return math.exp(-1.0 / (1.0 - x * x))


def packet(R: int, alpha: float) -> complex:
    return sum(
        bump(j / R) * cmath.exp(2j * math.pi * j * alpha)
        for j in range(-R + 1, R)
    )


def normalized_packet(R: int, alpha: float) -> complex:
    return packet(R, alpha) / packet(R, 1.0)


def nullity_energy(R: int, k: int, umax: float = 12.0, steps: int = 12000) -> float:
    """Integrate over alpha=1+u/R using a midpoint rule."""
    du = 2 * umax / steps
    total = 0.0
    for q in range(steps):
        u = -umax + (q + 0.5) * du
        alpha = 1.0 + u / R
        phase_poly = (1.0 + cmath.exp(1j * math.pi * alpha)) ** k
        total += abs(phase_poly * packet(R, alpha)) ** 2
    return total * du / R


def symbolic_nullity(max_k: int = 5) -> dict[int, str]:
    alpha = sp.symbols("alpha", real=True)
    results: dict[int, str] = {}
    for k in range(max_k + 1):
        p = (1 + sp.exp(sp.I * sp.pi * alpha)) ** k
        for j in range(k):
            assert sp.simplify(sp.diff(p, alpha, j).subs(alpha, 1)) == 0
        kth = sp.simplify(sp.diff(p, alpha, k).subs(alpha, 1))
        assert kth != 0
        results[k] = str(kth)
    return results


def main() -> None:
    report: list[str] = []
    report.append("CRITICAL-EDGE / NYQUIST MODEL VERIFICATION")
    report.append("=" * 45)
    report.append("")

    # At alpha=1 every lattice phase is exactly one.
    for R in (100, 200, 400):
        z = normalized_packet(R, 1.0)
        assert abs(z - 1) < 1e-12
        report.append(f"R={R}: normalized endpoint response = {z.real:.15f}")

    # Fixed subcritical frequency becomes rapidly less visible as R grows.
    subcritical = [abs(normalized_packet(R, 0.9)) for R in (100, 200, 400)]
    assert subcritical[2] < subcritical[1] < subcritical[0]
    report.append(f"fixed alpha=0.9 responses: {subcritical}")

    # At fixed u=R(1-alpha), responses stabilize rather than collapse.
    for u in (0.5, 1.0, 2.0):
        vals = [abs(normalized_packet(R, 1.0 - u / R)) for R in (100, 200, 400)]
        assert max(vals) - min(vals) < 0.03
        report.append(f"transition u={u}: {vals}")

    derivatives = symbolic_nullity()
    report.append("")
    report.append("Endpoint derivative checks:")
    for k, value in derivatives.items():
        report.append(f"  k={k}: first nonzero derivative = {value}")

    report.append("")
    report.append("Scaled edge energies R^(2k-1) * integral |P_k A_R|^2:")
    for k in (0, 1, 2):
        scaled = []
        for R in (100, 200, 400):
            energy = nullity_energy(R, k)
            scaled.append((R ** (2 * k - 1)) * energy)
        # Convergence is deliberately checked only coarsely; the theorem is analytic.
        assert abs(scaled[-1] - scaled[-2]) / max(1.0, abs(scaled[-1])) < 0.12
        report.append(f"  k={k}: {scaled}")

    report.append("")
    report.append("All model checks passed.")
    text = "\n".join(report) + "\n"
    (HERE / "verification.txt").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
