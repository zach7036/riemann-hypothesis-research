# Proposed low-multiplicity profile

**Status:** unrefereed research draft for expert review. This is not a proof of the Riemann Hypothesis.

Let `M_{<=r}(T,2T)` count copies in the zeta-zero multiset that occur at locations of multiplicity at most `r`, and let `D_{<=r}(T,2T)` count distinct such locations. Put

`kappa_MT = 1/2 + (1/sqrt(2)) cot(1/sqrt(2))`

and

`B = (3 - 2 sqrt(2))(kappa_MT - 1)`.

The proposed corollary of the recent unconditional Claude/Anthropic two-trace theorem is:

- `liminf M_{<=1}/N >= 2-kappa_MT`;
- `liminf M_{<=2}/N >= (3-kappa_MT)/2`;
- for fixed `r>=3`, `liminf M_{<=r}/N >= 1-B(r+1)/(r-1)`.

For distinct locations:

- `liminf D_{<=1}/N_d >= 1-(kappa_MT-1)/(3-kappa_MT)`;
- `liminf D_{<=2}/N_d >= 1-(kappa_MT-1)/(2(4-kappa_MT))`;
- for fixed `r>=3`, `liminf D_{<=r}/N_d >= 1-B/(r-1-rB)`.

Selected rigorously rounded values are stored in `low_multiplicity_constants.csv`: at `r=3`, the bounds are `0.887620008173354` of the zero multiset and `0.969319059130202` of distinct locations; at `r=4`, they are `0.906350006811128` and `0.979753104026191`.

The scalar derivation has exact arithmetic and symbolic checks, but external specialist review, Lean integration, and comprehensive priority review remain outstanding.
