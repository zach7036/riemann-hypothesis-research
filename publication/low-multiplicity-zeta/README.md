# Low-multiplicity zeta-zero publication package

This directory contains the source and verification materials for the unrefereed manuscript *Unconditional low-multiplicity profiles for zeros of the Riemann zeta function*.

> [!CAUTION]
> This is a theorem candidate for expert review, not a peer-reviewed result, a completed Lean formalization, or a proof of the Riemann Hypothesis.

## Manuscript and claim ledger

- [`low_multiplicity_zeta.tex`](low_multiplicity_zeta.tex) — LaTeX manuscript source.
- [`THEOREM.md`](THEOREM.md) — compact theorem statement and selected constants.
- [`publication_readiness_audit.md`](publication_readiness_audit.md) — authoritative claim ledger and outstanding obligations.
- [`REVIEWER_COVER_NOTE.md`](REVIEWER_COVER_NOTE.md) — suggested handoff for cold expert review.
- [`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md) — completed and outstanding release work.
- [`EXPLORATORY_BRANCH_STATUS.md`](EXPLORATORY_BRANCH_STATUS.md) — separation from unfinished RH-facing branches.

Generated PDFs are intentionally not tracked. Build the manuscript from the repository root with `./scripts/build_paper.sh`; see [`../../BINARY_ARTIFACTS.md`](../../BINARY_ARTIFACTS.md).

## Exact decimal certificate

- [`certify_low_multiplicity.py`](certify_low_multiplicity.py) — standard-library rational interval implementation.
- [`certify_low_multiplicity_exact.py`](certify_low_multiplicity_exact.py) — compatibility entry point used by the documented reproduction command.
- [`low_multiplicity_exact_certificate.txt`](low_multiplicity_exact_certificate.txt) — recorded human-readable output.
- [`low_multiplicity_constants.csv`](low_multiplicity_constants.csv) and [`constants.csv`](constants.csv) — cutoff tables.
- [`exact_multiplicity_upper.csv`](exact_multiplicity_upper.csv) — exact-multiplicity upper profile.

## Independent corroboration

- [`audit_low_multiplicity_symbolic.py`](audit_low_multiplicity_symbolic.py) — exact symbolic identity audit.
- [`symbolic_audit.json`](symbolic_audit.json) and [`symbolic_audit.txt`](symbolic_audit.txt) — recorded symbolic output.
- [`verify_multiplicity_hierarchy.py`](verify_multiplicity_hierarchy.py) — broad pointwise-majorant stress test.
- [`multiplicity_hierarchy_verification.txt`](multiplicity_hierarchy_verification.txt) — recorded numerical output.

These programs verify their stated algebraic and numerical scopes. They do not independently establish the analytic master inequality.

## Formalization and priority

- [`FORMALIZATION_MAP.md`](FORMALIZATION_MAP.md) — declaration-level plan for extending the upstream Lean development.
- [`PRIORITY_SEARCH_LOG.md`](PRIORITY_SEARCH_LOG.md) — targeted, provisional novelty search.
- [`CHANGELOG.md`](CHANGELOG.md) — manuscript-package history.

## Reproduction

From this directory:

```bash
python certify_low_multiplicity_exact.py
python audit_low_multiplicity_symbolic.py
python verify_multiplicity_hierarchy.py
```

The first command uses only Python's standard library. The other checks use packages listed in [`../../requirements-verification.txt`](../../requirements-verification.txt). To compile the paper, run `pdflatex low_multiplicity_zeta.tex` three times or use the repository build script.

## Current assessment

The scalar derivation and constants are internally well checked, and the required arbitrary-parameter rank–trace and perturbation lemmas exist in the pinned upstream source. External specialist review, a compiled generic-parameter Lean endgame, and comprehensive priority review remain outstanding. Until those steps are complete, describe the result as an **unrefereed theorem candidate** or **plausibly novel corollary/optimization**.
