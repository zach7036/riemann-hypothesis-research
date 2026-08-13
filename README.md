# Riemann Hypothesis research program

Research drafts, exact certificates, verification scripts, and exploratory notes on zeta-zero multiplicity and RH-adjacent trace methods.

> [!IMPORTANT]
> **This repository does not contain a proof of the Riemann Hypothesis.** Its strongest item is an unrefereed publication candidate deriving low-multiplicity profiles from the recent unconditional Claude/Anthropic two-trace theorem. Other branches are explicitly exploratory.

## Main publication candidate

[`publication/low-multiplicity-zeta/`](publication/low-multiplicity-zeta/) contains the manuscript

**“Unconditional low-multiplicity profiles for zeros of the Riemann zeta function.”**

For each fixed integer `r`, it derives lower bounds for:

1. the fraction of the zero **multiset** supported on locations of multiplicity at most `r`;
2. the fraction of **distinct zero locations** having multiplicity at most `r`.

Selected proposed unconditional bounds are:

| Maximum multiplicity | Multiset mass | Distinct locations |
|---:|---:|---:|
| 3 | 88.7620008173354% | 96.9319059130202% |
| 4 | 90.6350006811128% | 97.9753104026191% |

The manuscript also gives exact-multiplicity upper profiles and abstract extremal distributions showing sharpness within the complete scalar rank–trace information model.

### Status

- Paper proof and exact arithmetic certificates: present.
- Independent computational stress tests: present.
- External specialist review: outstanding.
- New Lean integration: outstanding.
- Comprehensive priority determination: outstanding.

Read the [publication-readiness audit](publication/low-multiplicity-zeta/publication_readiness_audit.md) before quoting any result.

## Repository layout

- `publication/low-multiplicity-zeta/` — manuscript, LaTeX, exact certificates, data tables, review material, formalization map, and audit.
- `exploratory/amplitude-endpoint/` — proposed exact-dilation endpoint architecture and hostile referee audit.
- `exploratory/xi-prime-and-short-interval/` — exact window-functional certificate and unfinished localization program.
- `exploratory/depth-spectrum/` — provisional depth-sensitive harmonic-analysis work.
- `exploratory/critical-edge-nyquist/` — historical model note on edge resonance and nullity.
- `exploratory/complementary-hankel/` — historical finite-phase-rank detector note.
- `docs/RESEARCH_MAP.md` — concise claim ledger.
- `references/` — upstream foundation and citation information.

## Reproduction

The main exact certificate uses only Python's standard library:

```bash
cd publication/low-multiplicity-zeta
python certify_low_multiplicity_exact.py
```

The independent stress test additionally needs `sympy`, `numpy`, `scipy`, and `mpmath`:

```bash
python verify_multiplicity_hierarchy.py
```

Run the complete local verification suite with:

```bash
./scripts/run_all_checks.sh
```

Rebuild the manuscript with:

```bash
./scripts/build_paper.sh
```

No GitHub Actions workflows are included; verification is intentionally manual. A convenience `Makefile` is provided, and optional numerical dependencies are pinned in `requirements-verification.txt`.

## Upstream analytic input

The publication candidate relies on the unconditional theorem and formal development in:

- Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line*.
- <https://github.com/anthropics/zeta-23-lean>
- <https://www.anthropic.com/research/riemann-zeta>

This repository does not claim to reprove that analytic number theory.

## Authorship and AI disclosure

Zach Waddle assembled and is circulating the research program. GPT-5.6 Pro and other AI systems assisted with derivation, adversarial checking, computation, source organization, and manuscript preparation. Human responsibility for any public mathematical claim requires independent expert review.

## Publishing

See [`PUBLISHING.md`](PUBLISHING.md) for the exact GitHub CLI command. No GitHub Actions workflows are included.

## License

Unless a file says otherwise, original repository contents are licensed under the Apache License 2.0. External works are cited but not redistributed.
