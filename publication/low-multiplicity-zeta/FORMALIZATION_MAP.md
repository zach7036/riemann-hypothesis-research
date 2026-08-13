# Lean formalization map for the low-multiplicity hierarchy

**Pinned upstream:** `anthropics/zeta-23-lean`  
**Commit audited:** `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`  
**Toolchain:** `leanprover/lean4:v4.33.0-rc2`  
**Mathlib:** `51e6992efd06126df61a496bebf8f49482a4e129`

## Existing upstream ingredients

| File | Existing declaration / role |
|---|---|
| `Zeta23/ZeroSide/RankTraceMult.lean` | `rank_trace_mult_k_le`, valid for every `c>0`, with `kc c m = c^2 - ((c-m)_+)^2` |
| `Zeta23/Assembly/SeamMult.lean` | `ctr_sub_frobSq_perturb`, generic in the trace coefficient; existing specialized seams at `c=2,3` |
| `Zeta23/ThmD/Mult.lean` | Montgomery-Taylor multiplicity-aware endgames for `c=2,3` |
| `Zeta23/Defs.lean` | abstract `ZeroConfig`, `N`, `Nd`, `N0s`, multiplicity, reflection pairs |
| `Zeta23/Defs/Counting.lean` | finite-window counting and monotonicity lemmas |
| `Zeta23/ThmE/Mult.lean` | fixed primitive Dirichlet L-function analogue |

## Proposed new definitions

For an abstract zero configuration `Z`, integer `r`, and window `(T1,T2]`:

```lean
noncomputable def NleMult (Z : ZeroConfig) (r : Nat) (T1 T2 : Real) : Nat :=
  ∑ᶠ rho ∈ Z.window T1 T2,
    if Z.mult rho ≤ r then Z.mult rho else 0

noncomputable def Dle (Z : ZeroConfig) (r : Nat) (T1 T2 : Real) : Nat :=
  (Z.window T1 T2 ∩ {rho | Z.mult rho ≤ r}).ncard
```

The implementation should use finite-window lemmas so that `finsum` reduces cleanly to `Finset.sum`.

## New scalar lemmas

### Multiset majorants

At `r=1`, `c=2`, `alpha=2`, `beta=1`:

```lean
kc 2 m ≤ 2*m + m * indicator (m ≤ 1)
```

At `r=2`, `c=3`, `alpha=3`, `beta=2`.

For `r≥3`, set `C=2+sqrt 2`,

```lean
alpha = C^2 / (r+1)
beta  = C^2*(r-1)/(2*(r+1))
```

and prove the on-line and pair inequalities by the cases `m≤C`, `C≤m≤r`, and `r+1≤m`.

### Distinct-location majorants

For each case prove

```lean
kc c m ≤ alpha*m + beta - gamma * indicator (r+1 ≤ m)
```

and the doubled pair analogue. For `r≥3`, the only nontrivial low values are `m=1,2,3`; `m≥4` is on the constant branch of `kc`.

## Generic seam

Generalize the current specialized seam to a theorem of the form

```lean
theorem seamA_mult_c
    (c : Real) (hc : 0 < c) ... :
    2*c * rtrace Ghat - frobSq Ghat - boundary_error
      ≤ sum_on_line (kc c mult) + c^2 * pairCount := ...
```

This should combine:

1. `rank_trace_mult_k_le` on the interior matrix;
2. `ctr_sub_frobSq_perturb (2*c)`;
3. the existing boundary-count identities.

## Generic Montgomery-Taylor endgame

Abstract the repeated asymptotic part of `thmD_mult2_abstract` and `thmD_mult3_abstract` into a master theorem yielding, for fixed `c>0`,

```lean
(2*c - kappaMT - eps) * N ≤ scalarMultiplicityCharge c
```

for all sufficiently large `T`.

The two new hierarchy theorems then become elementary applications of the scalar majorants. The dyadic and Dirichlet versions should reuse existing assembly modules.

## Exact-multiplicity corollaries

Define exact-multiplicity counts either directly or as differences of consecutive cutoff counts. For `j>=2`, the upper bounds are complements of the cutoff theorem at `r=j-1`; no additional analytic theorem is required. The scalar sharpness witnesses already put all high-multiplicity mass at multiplicity exactly `j`.

## Verification boundary

This map is based on source inspection. The new Lean code has **not** been compiled in this environment. Do not add `sorry`, `admit`, project-specific axioms, or a new GitHub Action. Run the existing pinned build and the repository's normal `#print axioms` audit locally.
