# Priority-search log: unconditional low-multiplicity profiles for zeta zeros

**Search date:** August 12, 2026  
**Candidate paper:** *Unconditional low-multiplicity profiles for zeros of the Riemann zeta function*  
**Scope:** Lower bounds, without RH, for the fraction of the zero multiset and the fraction of distinct zero locations supported on multiplicities at most a fixed integer `r`; sharp upper profiles for exact multiplicity `j`; optimization of the full scalar `c>0` multiplicity-aware rank-trace family.

## Search strategy

The targeted search used combinations of:

- `Riemann zeta zeros multiplicity at most r unconditional`
- `low multiplicity zeros Riemann zeta function`
- `multiplicity at most two/three zeta zeros`
- `distribution/density of zeros of given multiplicity`
- the exact constants `0.887620008173354` and `0.969319059130202`
- citation chains around Montgomery--Taylor, Conrey--Ghosh--Gonek, Chirre--Goncalves--de Laat, Goncalves--de Laat--Leijenhorst, and Simonic--Trudgian--Turnage-Butterbaugh.

The search covered arXiv, primary journal/publisher records discoverable on the open web, the bibliography of the 2026 Claude/Anthropic preprint, and the public `anthropics/zeta-23-lean` source tree. MathSciNet and zbMATH were not comprehensively searched from this environment.

## Closest located results

### Goncalves--de Laat--Leijenhorst

Felipe Goncalves, David de Laat, and Nando Leijenhorst, *Multiplicity of nontrivial zeros of primitive L-functions via higher-level correlations*, Mathematics of Computation 94 (2025), no. 354, 2041--2058, DOI `10.1090/mcom/4005`, arXiv:2303.01095.

- Assumes GRH.
- Uses higher-level correlation asymptotics.
- For the Riemann zeta function, proves at least `0.9614` of the zero multiset has multiplicity at most two and at least `0.9787` has multiplicity at most three.
- This is numerically stronger but conditional and uses higher correlations, so it is not the same theorem or input regime.

### Simonic--Trudgian--Turnage-Butterbaugh

Aleksander Simonic, Timothy S. Trudgian, and Caroline L. Turnage-Butterbaugh, *Some explicit and unconditional results on gaps between zeroes of the Riemann zeta-function*, Transactions of the AMS 375 (2022), no. 5, 3239--3265, DOI `10.1090/tran/8571`, arXiv:2010.10675.

- Unconditional.
- Gives an explicit upper bound for the density of zeros of **exactly** multiplicity `j`:
  `N_j(T)/N(T) <= 1.014 exp(-6.459e-7 j)` for sufficiently large `T`.
- The authors note that this improves the elementary simple-zero-derived exact-multiplicity estimate only for extremely large `j` (about `2.8e7` and above).
- It does not supply the fixed-low cumulative hierarchy or distinct-location profile in the candidate paper.

### Claude/Anthropic 2026 base theorem

*More than two thirds of the zeros of the Riemann zeta function lie on the critical line* and public repository `anthropics/zeta-23-lean`, audited at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`.

- Gives the unconditional simple/on-line and distinct headline bounds used as analytic input.
- The repository contains the general scalar theorem `rank_trace_mult_k_le` for every fixed `c>0`, although the paper's headline multiplicity applications specialize to `c=2` and `c=3`.
- No fixed-`r` low-multiplicity hierarchy or the closed-form sharpness distributions were located in the paper or source tree.

## Exact-match checks

No match was located for:

- the title phrase `unconditional low-multiplicity profiles` in this context;
- the exact constants `0.887620008173354` or `0.969319059130202`;
- the formulas
  `1-(3-2 sqrt(2))(kappa_MT-1)(r+1)/(r-1)` or
  `1-B/(r-1-rB)`;
- a theorem optimizing the complete `c>0` scalar family for every fixed cutoff `r`.

## Priority conclusion

The open-web search supports the description **plausibly novel corollary/optimization of the 2026 rank-trace method**, not a definitive priority claim. Before the manuscript says “first” or “new” without qualification, complete these checks:

- MathSciNet and zbMATH searches by subject code `11M06` / `11M26` and the terms multiplicity distribution, bounded multiplicity, and zero multiplicity;
- Google Scholar “cited by” chains for the three closest papers above;
- direct inquiry to the Claude/Anthropic paper authors and formalization team;
- a specialist check of older work by Farmer, Conrey--Ghosh--Gonek, Cheer--Goldston, and papers using Montgomery's pair-correlation multiplicity moment.

Until then, the manuscript should use wording such as “we did not locate a prior unconditional fixed-low-multiplicity hierarchy with these formulas” rather than “this is the first.”
