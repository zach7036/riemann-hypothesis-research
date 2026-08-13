# Pre-submission checklist

## Proof and statements

- [x] Define multiset and distinct-location low-multiplicity counts unambiguously.
- [x] State all cutoff and exact-multiplicity constants in closed form.
- [x] Prove the master scalar inequality at paper level from the released arbitrary-`c` source theorem and trace asymptotics.
- [x] Prove all pointwise scalar majorants for `r=1`, `r=2`, and `r>=3`.
- [x] Prove nonnegativity and normalization of every sharpness distribution.
- [x] Verify the sharpness constraints on all three parameter ranges: `0<c<=1`, `1<=c<=r+1`, and `c>=r+1`.
- [x] Distinguish scalar-relaxation sharpness from realizability by actual zeta zeros.
- [x] State explicitly that the result does not prove or materially approach RH.

## Computation and reproducibility

- [x] Enclose `kappa_MT` and `B` with exact rational interval arithmetic.
- [x] Round every advertised lower bound downward and every advertised upper bound upward.
- [x] Run the independent symbolic and discretized-LP audit.
- [x] Record file hashes.
- [x] Include the pinned upstream commit, Lean toolchain, and Mathlib revision.
- [ ] Re-run both scripts on a clean external machine.

## Formalization

- [x] Identify existing arbitrary-`c` source declarations.
- [x] Write a declaration-level integration map.
- [ ] Implement low-multiplicity counting definitions in Lean.
- [ ] Implement the generic-`c` seam and endgame.
- [ ] Kernel-check the scalar majorants and final theorems.
- [ ] Run the complete pinned build and `#print axioms` audit.

## Independent review

- [ ] Obtain a cold read from an analytic number theorist.
- [ ] Obtain a separate optimization/sharpness review.
- [ ] Ask the base-theorem authors/formalizers to confirm the generic-`c` reuse.
- [ ] Resolve every reviewer objection in a versioned response log.

## Priority and bibliography

- [x] Search open arXiv and primary-source records for the closest multiplicity results.
- [x] Correct journal metadata and DOI information for the two closest papers.
- [x] Search exact constants and closed-form expressions.
- [ ] Search MathSciNet and zbMATH comprehensively.
- [ ] Follow Google Scholar citation chains.
- [ ] Obtain a specialist priority opinion.
- [ ] Avoid “first” language until those checks are complete.

## Authorship and release

- [x] Credit the 2026 analytic theorem and formalization as the sole analytic input.
- [x] Disclose GPT-5.6 Pro assistance.
- [ ] Confirm authorship and institutional/contact metadata.
- [ ] Choose an arXiv license and subject classification.
- [ ] Add source repository or immutable archive link.
- [ ] Post only after expert review or label the upload unmistakably as an unrefereed draft.
