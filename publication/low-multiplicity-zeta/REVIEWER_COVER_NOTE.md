# Expert-review cover note

**Manuscript:** *Unconditional low-multiplicity profiles for zeros of the Riemann zeta function*  
**Author:** Zach Waddle  
**Status:** Private draft for cold review; not yet submitted or externally validated.

## What the note claims

Starting from the unconditional Montgomery--Taylor two-trace theorem and the arbitrary-`c` multiplicity-aware rank--trace inequality in `anthropics/zeta-23-lean`, the manuscript derives lower bounds for two fixed-cutoff statistics:

1. the fraction of the zero multiset supported on locations of multiplicity at most `r`;
2. the fraction of distinct zero locations having multiplicity at most `r`.

At `r=3`, the proposed unconditional bounds are respectively

- `0.887620008173354...` of the zero multiset;
- `0.969319059130202...` of distinct locations.

Closed forms are supplied for every fixed `r`, together with sharp upper bounds for exact multiplicity `j>=2` and abstract extremal distributions that satisfy the full scalar inequality for every `c>0`. The sharpness is only within that scalar relaxation; realizability by actual zeta evaluation vectors is not claimed.

## The three joints that most need independent checking

1. **Generic-`c` analytic seam.** Confirm that the existing arbitrary-`c` zero-side inequality and generic perturbation estimate combine with the Montgomery--Taylor trace asymptotics exactly as Proposition 2.1 states, with an `o_c(N)` error for each fixed `c`.
2. **Scalar majorants and sharpness.** Check the pointwise on-line/pair inequalities and the piecewise verification of the extremal distributions over all `c>0`.
3. **Priority.** Check whether an unconditional fixed-low-multiplicity hierarchy, especially the distinct-location formulas, has appeared previously as a consequence of pair-correlation multiplicity bounds.

## Reproducibility files

- `low_multiplicity_zeta.pdf` and `.tex`
- `certify_low_multiplicity.py` and its exact output
- `verify_multiplicity_hierarchy.py` and its independent output
- `FORMALIZATION_MAP.md`
- `constants.csv` and `exact_multiplicity_upper.csv`
- `PRIORITY_SEARCH_LOG.md`
- `SHA256SUMS.txt`

The exact certificate uses only Python's standard library and rational interval bounds for the trigonometric constant. The second script is corroborative and uses SymPy/SciPy numerical linear programs. No new Lean theorem has yet been compiled.
