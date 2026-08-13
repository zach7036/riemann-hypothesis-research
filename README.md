# Riemann Hypothesis Research Program

**AI-assisted research on zeta-zero multiplicity, critical-line methods, and RH-adjacent trace techniques.**

> [!IMPORTANT]
> **This repository does not contain a proof of the Riemann Hypothesis.** Its strongest result is an **unrefereed theorem candidate** on low multiplicities of zeros of the Riemann zeta function. Other RH-facing branches are explicitly labeled exploratory.

## Main result candidate

The most mature work is the manuscript **“Unconditional low-multiplicity profiles for zeros of the Riemann zeta function.”** It builds on the recent unconditional Claude/Anthropic two-trace theorem and optimizes the full multiplicity-aware scalar rank–trace family for every fixed multiplicity cutoff.

For each fixed integer `r >= 1`, the manuscript derives candidate unconditional lower bounds for:

1. the fraction of the zero **multiset** supported on locations of multiplicity at most `r`;
2. the fraction of **distinct zero locations** having multiplicity at most `r`.

Selected bounds:

| Maximum multiplicity | Zero-multiset mass | Distinct locations |
|---:|---:|---:|
| 1 | 67.2500703679411% | 80.4185854391506% |
| 2 | 83.6250351839705% | 93.8727930759812% |
| 3 | **88.7620008173354%** | **96.9319059130202%** |
| 4 | **90.6350006811128%** | **97.9753104026191%** |
| 5 | 91.5715006130015% | 98.4891304068350% |
| 10 | 93.1323338328160% | 99.3340918495729% |

The manuscript also gives exact-multiplicity upper bounds and abstract extremal distributions showing that the formulas are sharp within the scalar rank–trace information model. This sharpness statement is about the relaxation, not a claim that those extremal distributions occur among actual zeta zeros.

## Status

| Workstream | Status |
|---|---|
| **Low-multiplicity profiles** | **Publication candidate** — paper-level proof, exact certificates, computational stress tests; external review and Lean integration still needed |
| **Amplitude / critical-bandwidth endpoint** | Exploratory, substantially developed |
| **Short-interval xi-prime program** | Exploratory theorem candidate; full analytic transfer unfinished |
| **Depth-spectrum / positivity barriers** | Exploratory harmonic analysis |
| **Critical-edge / Nyquist analysis** | Exploratory model results |
| **Complementary Hankel detector** | Exploratory finite-rank algebra |
| **Riemann Hypothesis** | **Open** |

See [`docs/RESEARCH_MAP.md`](docs/RESEARCH_MAP.md) and the [publication-readiness audit](publication/low-multiplicity-zeta/publication_readiness_audit.md) for the authoritative claim ledger.

## Quick links

### Publication candidate

- [Manuscript source](publication/low-multiplicity-zeta/low_multiplicity_zeta.tex)
- [Theorem summary](publication/low-multiplicity-zeta/THEOREM.md)
- [Publication-readiness audit](publication/low-multiplicity-zeta/publication_readiness_audit.md)
- [Exact certificate](publication/low-multiplicity-zeta/certify_low_multiplicity.py)
- [Independent verification](publication/low-multiplicity-zeta/verify_multiplicity_hierarchy.py)
- [Certified constants](publication/low-multiplicity-zeta/constants.csv)
- [Exact-multiplicity bounds](publication/low-multiplicity-zeta/exact_multiplicity_upper.csv)
- [Lean formalization map](publication/low-multiplicity-zeta/FORMALIZATION_MAP.md)
- [Priority-search log](publication/low-multiplicity-zeta/PRIORITY_SEARCH_LOG.md)
- [Reviewer cover note](publication/low-multiplicity-zeta/REVIEWER_COVER_NOTE.md)

### Exploratory research

- [Amplitude endpoint](exploratory/amplitude-endpoint/README.md)
- [Xi-prime and short intervals](exploratory/xi-prime-and-short-interval/README.md)
- [Depth spectrum](exploratory/depth-spectrum/README.md)
- [Critical edge / Nyquist](exploratory/critical-edge-nyquist/README.md)
- [Complementary Hankel](exploratory/complementary-hankel/README.md)
- [Consolidated exploratory findings](docs/EXPLORATORY_FINDINGS.md)

## Reproduce the main result

The exact certificate uses only the Python standard library:

```bash
cd publication/low-multiplicity-zeta
python certify_low_multiplicity_exact.py
```

The independent stress test uses `sympy`, `numpy`, `scipy`, and `mpmath`:

```bash
python verify_multiplicity_hierarchy.py
```

Optional verification dependencies are listed in [`requirements-verification.txt`](requirements-verification.txt). No GitHub Actions workflows are included; verification is intentionally manual.

## Upstream foundation

The publication candidate relies on:

- Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line* (2026)
- [`anthropics/zeta-23-lean`](https://github.com/anthropics/zeta-23-lean)
- [Anthropic research announcement](https://www.anthropic.com/research/riemann-zeta)

That work gives approximately **67.25%** simple critical-line zeros and **83.625%** distinct zeros unconditionally. This repository does not claim to reprove that analytic foundation; the main new contribution here is the low-multiplicity optimization and bookkeeping layer.

## Why this is not RH

A density result does not eliminate a sparse exceptional sequence of off-line zeros. The upstream two-trace architecture is itself insensitive to sufficiently sparse exceptions. The exploratory branches investigate possible phase-sensitive and geometric refinements, but no argument here proves that every nontrivial zero lies on the critical line.

## Review and contributions

Mathematical scrutiny is welcome, especially:

- precise gap-finding or independent proof checks;
- literature-priority checks;
- Lean formalization of the new hierarchy;
- improvements to exploratory branches that preserve a strict theorem/candidate distinction.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [mathematical review template](.github/ISSUE_TEMPLATE/mathematical-review.md).

## Authorship and AI disclosure

**Zach Waddle** assembled and is circulating this research program. GPT-5.6 Pro and other AI systems assisted with derivation, adversarial checking, computation, literature organization, and manuscript preparation.

See [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md), [`NOTICE.md`](NOTICE.md), and [`CITATION.cff`](CITATION.cff).

## License

Unless a file states otherwise, original repository contents are licensed under the **Apache License 2.0**. External works are cited but not redistributed.