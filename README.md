# Low-Multiplicity Profiles for Zeta Zeros

[![Research status: unrefereed](https://img.shields.io/badge/status-unrefereed%20research-orange)](STATUS.md)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Cite this repository](https://img.shields.io/badge/citation-CITATION.cff-blueviolet)](CITATION.cff)

**AI-assisted analytic-number-theory research on zero multiplicity, built on the 2026 Claude/Anthropic two-trace theorem.**

> [!IMPORTANT]
> This repository does **not** prove the Riemann Hypothesis. Its main result is an **unrefereed theorem candidate**. The analytic number-theory input is inherited from the upstream theorem; the proposed contribution here is a low-multiplicity optimization and sharpness analysis.

## At a glance

- **Main candidate:** unconditional lower profiles for zeros of the Riemann zeta function whose multiplicity is at most a fixed integer `r`.
- **What is checked here:** closed-form algebra, exact rational interval certificates, symbolic identities, and broad numerical stress tests.
- **What is still missing:** independent specialist review, a compiled Lean extension for the generic-parameter endgame, and a comprehensive priority search.
- **RH status:** open. Density bounds cannot rule out a sparse exceptional set of off-critical-line zeros.

## Main result candidate

The manuscript [*Unconditional low-multiplicity profiles for zeros of the Riemann zeta function*](publication/low-multiplicity-zeta/low_multiplicity_zeta.tex) starts from the multiplicity-aware rank–trace framework in [`anthropics/zeta-23-lean`](https://github.com/anthropics/zeta-23-lean) and optimizes its full scalar parameter family.

For every fixed cutoff `r >= 1`, it proposes lower bounds for:

1. the fraction of the zero **multiset** supported on locations of multiplicity at most `r`; and
2. the fraction of **distinct zero locations** having multiplicity at most `r`.

Selected rigorously rounded-down values are:

| Maximum multiplicity `r` | Zero-multiset mass | Distinct locations |
|---:|---:|---:|
| 1 | 67.2500703679411% | 80.4185854391506% |
| 2 | 83.6250351839705% | 93.8727930759812% |
| 3 | **88.7620008173354%** | **96.9319059130202%** |
| 4 | **90.6350006811128%** | **97.9753104026191%** |
| 5 | 91.5715006130015% | 98.4891304068350% |
| 10 | 93.1323338328160% | 99.3340918495729% |

The manuscript also derives exact-multiplicity upper bounds and constructs abstract extremal distributions showing that the formulas are optimal **within the scalar rank–trace information model**. This does not assert that the extremal distributions occur among actual zeta zeros.

## Why the result may matter

The potentially new part is a closed-form, fixed-`r` hierarchy—especially the distinct-location profile—and a sharpness theorem for the complete scalar family. A targeted open-web literature search did not locate these formulas previously.

The claim should nevertheless be described as a **plausibly novel corollary/optimization**, not a breakthrough proof:

- the deep analytic estimates and formalized rank–trace machinery come from the upstream Claude/Anthropic work;
- the generic-parameter analytic seam is argued at paper level but is not yet packaged as a compiled Lean theorem here;
- no external referee or analytic number theorist has validated the new corollaries; and
- MathSciNet, zbMATH, citation-chain, and specialist priority checks remain incomplete.

See the [priority-search log](publication/low-multiplicity-zeta/PRIORITY_SEARCH_LOG.md) and [publication-readiness audit](publication/low-multiplicity-zeta/publication_readiness_audit.md) for the detailed claim ledger.

## Repository guide

| Path | Contents | Status |
|---|---|---|
| [`publication/low-multiplicity-zeta/`](publication/low-multiplicity-zeta/) | Manuscript, theorem summary, certificates, audit, and formalization map | Unrefereed publication candidate |
| [`exploratory/`](exploratory/) | Endpoint, short-interval, spectral, Nyquist, and Hankel research directions | Exploratory only |
| [`docs/RESEARCH_MAP.md`](docs/RESEARCH_MAP.md) | Branch-by-branch claim status | Authoritative overview |
| [`STATUS.md`](STATUS.md) | Short project status | Authoritative summary |
| [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md) | Scope of AI assistance | Disclosure |

Useful entry points:

- [Theorem summary](publication/low-multiplicity-zeta/THEOREM.md)
- [Manuscript source](publication/low-multiplicity-zeta/low_multiplicity_zeta.tex)
- [Reviewer cover note](publication/low-multiplicity-zeta/REVIEWER_COVER_NOTE.md)
- [Lean formalization map](publication/low-multiplicity-zeta/FORMALIZATION_MAP.md)
- [Exploratory research overview](exploratory/README.md)

## Reproduce the main checks

The rigorous decimal certificate uses only the Python standard library:

```bash
cd publication/low-multiplicity-zeta
python certify_low_multiplicity_exact.py
```

Optional symbolic and numerical checks use the pinned packages in [`requirements-verification.txt`](requirements-verification.txt):

```bash
python audit_low_multiplicity_symbolic.py
python verify_multiplicity_hierarchy.py
```

On a Unix-like shell, the same checks can be run from the repository root:

```bash
make check
```

Passing these scripts validates the stated algebra and constants; it does not replace review of the analytic argument. The repository intentionally stores source rather than generated PDFs—see [`BINARY_ARTIFACTS.md`](BINARY_ARTIFACTS.md) for build instructions.

## Upstream foundation

This project relies on:

- Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line* (2026);
- the pinned, `sorry`-free Lean artifact [`anthropics/zeta-23-lean`](https://github.com/anthropics/zeta-23-lean), audited here at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`; and
- [Anthropic's research announcement](https://www.anthropic.com/research/riemann-zeta).

The upstream work supplies the unconditional two-trace theorem, including approximately **67.25%** simple critical-line zeros and **83.625%** distinct zeros. This repository does not claim to reprove that foundation.

## Review, authorship, and license

Mathematical scrutiny is welcome, particularly precise gap reports, literature-priority corrections, independent reproduction, and Lean formalization. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [mathematical review template](.github/ISSUE_TEMPLATE/mathematical-review.md).

**Zach Waddle** assembled and is circulating this research program. GPT-5.6 Pro and other AI systems assisted with derivation, adversarial checking, computation, literature organization, and manuscript preparation. Details are in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md), [`NOTICE.md`](NOTICE.md), and [`CITATION.cff`](CITATION.cff).

Original repository contents are licensed under the **Apache License 2.0** unless a file states otherwise. External works are cited but not redistributed.
