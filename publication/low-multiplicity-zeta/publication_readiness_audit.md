# Publication-readiness audit

**Date:** August 12, 2026  
**Prepared for:** Zach Waddle

## Executive decision

The repository has one defensible publication core: the proposed unconditional low-multiplicity profiles for zeta zeros. The analytic input is the released Claude/Anthropic two-trace theorem and its Lean development; the new contribution is scalar optimization and multiplicity bookkeeping.

The manuscript is ready for private specialist review, but the new corollaries are not yet externally refereed or added to the Lean tree. They must therefore be described as an unrefereed theorem candidate.

## Claim ledger

| Workstream | Status |
|---|---|
| Low-multiplicity multiset and distinct-location profiles | Main publication candidate; paper proof and exact certificates present |
| Exact-multiplicity upper profiles | Corollaries of the cutoff profiles; same review obligations |
| Fixed-amplitude endpoint transfer | Paper-level candidate with unresolved integration work |
| Short-interval zeta and xi-prime programs | Threshold calculations and partial geometry only; complete theorem absent |
| Depth-spectrum, Nyquist, and Hankel branches | Exploratory harmonic analysis and finite-rank algebra |
| Riemann Hypothesis | Not solved |

## Proposed theorem package

With

\[
\kappa_{\rm MT}=\frac12+\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right),
\qquad
B=(3-2\sqrt2)(\kappa_{\rm MT}-1),
\]

the proposed multiset lower profile is

\[
2-\kappa_{\rm MT}\quad(r=1),\qquad
\frac{3-\kappa_{\rm MT}}2\quad(r=2),\qquad
1-B\frac{r+1}{r-1}\quad(r\ge3).
\]

The proposed distinct-location lower profile is

\[
1-\frac{\kappa_{\rm MT}-1}{3-\kappa_{\rm MT}},\qquad
1-\frac{\kappa_{\rm MT}-1}{2(4-\kappa_{\rm MT})},\qquad
1-\frac{B}{r-1-rB}\quad(r\ge3).
\]

Selected rigorously rounded decimals are:

- multiplicity at most three: `88.7620008173354%` of the multiset and `96.9319059130202%` of distinct locations;
- multiplicity at most four: `90.6350006811128%` and `97.9753104026191%` respectively.

The manuscript also gives exact-multiplicity upper bounds and abstract extremal distributions. Sharpness is claimed only within the scalar information model, not as realizability by actual zeta-zero configurations.

## Closed internal obligations

- Source inspection located an arbitrary-parameter rank--trace inequality in the upstream Lean tree.
- The manuscript records the generic perturbation and asymptotic transfer used to obtain the scalar master inequality.
- Pointwise majorants and extremal distributions are proved algebraically.
- Exact rational interval arithmetic certifies every displayed decimal with directed rounding.
- A separate symbolic and discretized optimization audit reproduces the closed forms.

## Outstanding obligations

1. Obtain a cold read from an analytic number theorist.
2. Obtain a separate review of the scalar optimization and sharpness theorem.
3. Ask the upstream authors/formalizers to confirm reuse of the arbitrary-parameter seam.
4. Implement the new counting functions, generic seam, scalar majorants, and final corollaries in Lean.
5. Run the pinned full build and axiom audit.
6. Complete MathSciNet, zbMATH, and citation-chain priority searches.
7. Avoid priority language such as “first” until those checks are complete.

## Publication rule

The manuscript may be circulated privately now. A public preprint should either wait for specialist review or be labeled unmistakably as an unrefereed draft. None of the exploratory branches should be bundled into the theorem claim, and the repository must not be described as proving RH.
