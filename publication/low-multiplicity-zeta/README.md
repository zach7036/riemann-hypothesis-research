# Low-multiplicity zeta-zero publication package

This folder contains version 0.2 of the private expert-review draft and its verification materials.

## Main manuscript

- `low_multiplicity_zeta.pdf` - revised 13-page manuscript, visually preflighted after compilation.
- `low_multiplicity_zeta.tex` - LaTeX source.

## Rigorous decimal certificate

- `certify_low_multiplicity_exact.py` - standard-library-only rational interval certificate used for the revised manuscript.
- `low_multiplicity_certificate.json` and `.txt` - machine-readable and human-readable output.
- `low_multiplicity_constants.csv` - certified cutoff table.
- `exact_multiplicity_upper.csv` - certified exact-multiplicity upper table.

## Independent corroboration

- `audit_low_multiplicity_symbolic.py` - exact symbolic identity and broad numerical stress audit.
- `symbolic_audit.json` and `.txt` - recorded output.
- `certify_low_multiplicity.py` and `verify_multiplicity_hierarchy.py` - independently written certificate and discretized semi-infinite optimization checks retained from version 0.1.
- `low_multiplicity_exact_certificate.txt` and `multiplicity_hierarchy_verification.txt` - their outputs.

## Review and formalization

- `publication_readiness_audit.md` / `.pdf` - claim ledger and pre-submission obligations.
- `FORMALIZATION_MAP.md` - source-level plan for a Lean extension.
- `PRIORITY_SEARCH_LOG.md` - targeted novelty and bibliography audit.
- `REVIEWER_COVER_NOTE.md` - handoff for cold expert review.
- `SUBMISSION_CHECKLIST.md` - completed and outstanding release obligations.
- `EXPLORATORY_BRANCH_STATUS.md` - quarantine ledger for unfinished RH-facing branches.
- `CHANGELOG.md` - version history.
- `SHA256SUMS.txt` - hashes of the folder's deliverables.

## Reproduction

From this folder:

```bash
python certify_low_multiplicity_exact.py
python certify_low_multiplicity.py
python audit_low_multiplicity_symbolic.py
python verify_multiplicity_hierarchy.py
pdflatex low_multiplicity_zeta.tex
pdflatex low_multiplicity_zeta.tex
pdflatex low_multiplicity_zeta.tex
```

The two exact certificate scripts require only Python's standard library. The corroborative scripts require the packages listed in the repository's `requirements-verification.txt`.

## Status

This is an unrefereed theorem candidate built on the recent Claude/Anthropic unconditional two-trace theorem. The scalar derivation and constants are extensively checked, but the new corollaries have not yet been integrated into Lean or independently accepted by specialists. Do not describe this folder as peer reviewed, kernel checked, or a proof of RH.
