Hostile referee report: amplitude profiles at critical bandwidth

Date: 2026-08-11

Files reviewed:

- `outputs/move37_amplitude_profile.md`
- `work/amplitude_folner_boundary.md`
- `work/soft_edges_critical_bandwidth_audit.md`
- `work/critical_endpoint_boundary_layer.md`

## Verdict

The normalized finite-section boundary theorem is mathematically sound.  Its
Fourier normalization, lattice spacing, right-end phase, signed-density
majorization, and `L`-scaling all check out.  It gives the genuinely stronger
tilde-unit estimate

\[
 \left|L^{-2}\sum_{k,l<d}G_{kl}^{,2}-\mathcal M\right|
 \le C_h(B+1)^2.                                      \tag{R1}
\]

The log-energy endpoint deweighting argument is also sound and closes the
fixed-coefficient `PP` term at `X=T/(2\pi)`.

However, the notes do **not** yet prove the full `lambda=1` xi-prime transfer.
They correctly call it a candidate in the main output, but some supporting
language is too optimistic.  There are two independent strict-subcritical
uses downstream of the end lemma:

1. the current second-trace assembly absorbs its collected error with
   `l^2 X/T -> 0`;
2. the entry-dependent coefficient transfer absorbs an affine-floor
   `PPUpper` remainder with `l^4 X/T -> 0`.

Both fail at `lambda=1`.  The first can be repaired by keeping the improved
base `PP` little-oh and new end estimate separate.  The second needs the
homogeneous/recession `PPUpper` estimate to be threaded through the complete
re-expansion proof.  That threading is not present in the current tree.

Thus the central Move-37 abstraction survives hostile review, but the exact
endpoint theorem remains **STRONGLY SUPPORTED**, not proved.

## 1. Finite-section theorem: detailed check

Let `a=2*pi`, `D>=a`, `d=floor(D/a)`, `I_D=[0,D]`, and

\[
 K_d(x,y)=\sum_{0\le j<d}H(x-aj)H(y-aj),\qquad
 K_\infty(x,y)=\sum_{j\in\mathbb Z}H(x-aj)H(y-aj).
\]

Assume here that `H` is real and has sufficiently rapid decay.  The reality
assumption is automatic in the application because `h` is real and even.

### Interior defect

The bound

\[
 \sup_x\sum_j |H(x-aj)|^2<\infty
\]

implies uniform pointwise bounds for both kernels.  With
`E=K_infty-K_d`,

\[
 |K_\infty^2-K_d^2|\le C_H|E|.
\]

Tonelli gives

\[
 \iint_{I_D^2}|E(x,y)|\,dx\,dy
 \le\sum_{j\notin[0,d)}
       \left(\int_{I_D}|H(x-aj)|\,dx\right)^2.        \tag{R2}
\]

For `j<0` these are left tails.  For `j>=d`, writing
`D=ad+theta`, `0<=theta<a`, the term `j=d` is one bounded boundary term and
the later terms are right tails with starting points shifted by at most
`theta`.  The sum in (R2) is therefore uniformly bounded, including uniformly
in the phase `theta`.  No factor `d` is lost.  Equation (3) of
`amplitude_folner_boundary.md` is valid.

### Exterior defect and logarithmic density

The translate Gram matrix of a rapidly decaying `H` has absolutely summable
diagonals, so the synthesis map is bounded on `ell^2`.  Integrating one
variable first yields

\[
 \int_{x\notin I_D}\int_{\mathbb R}|K_d(x,y)|^2\,dy\,dx
 \ll_H\sum_{j<d}\int_{x\notin I_D}|H(x-aj)|^2\,dx=O_H(1).
\]

The weighted argument is also valid.  If

\[
 q_D(x)=1+\log(1+\operatorname{dist}(x,I_D)),
\]

then

\[
 q_D(y)\le q_D(x)\,[1+\log(1+|x-y|)].
\]

For an outside point `x` and an inside center `aj`, the resulting weight is
absorbed by a fixed polynomial weight on `|x-aj|`.  Rapid decay therefore
gives

\[
 \iint_{\mathbb R^2\setminus I_D^2}|K_d(x,y)|^2
 q_D(x)q_D(y)\,dx\,dy=O_H(1).                         \tag{R3}
\]

This handles a signed density because the proof uses
`|nu(x)nu(y)|`, not positivity of `nu`.  The theorem statement should require
`B>=0`; then

\[
 |\nu(T+x/L)|\le B+\log^+\frac{|T+x/L|}{4T}
 \le (B+1)q_{LT}(x).
\]

### Fourier and Poisson normalization

With the paper convention

\[
 H(x)=\int_{\mathbb R}h(s)e^{ixs}\,ds,
 \qquad \phi_L(u)=h(u/L),
\]

one has exactly

\[
 \widehat\phi_L(t)=L H(Lt).                           \tag{R4}
\]

For the grid `tau_j=T+2*pi*j/L` and normalized coordinates
`x=L(tau-T)`, `y=L(tau'-T)`,

\[
 K^{\rm phys}_d(\tau,\tau')=L^2K_d(x,y),\qquad
 d\tau\,d\tau'=L^{-2}dx\,dy.                         \tag{R5}
\]

There is no missing `2*pi`: the lattice in normalized frequency is exactly
`2*pi*Z`.  Poisson summation gives

\[
 \sum_{j\in\mathbb Z}H(x-2\pi j)H(y-2\pi j)
 =\int h(s)h(-s)e^{i(x-y)s}\,ds.
\]

For real even `h` this is the transform of `h^2`, agreeing with the released
identity `K_infty=L Phi`.  If the support reaches the endpoints, the aliases
at shifts `+/-1` still vanish because the endpoint values are zero; strict
interior support is sufficient but not necessary.

Squaring (R5) and using the Jacobian gives a raw error `O_h(L^2(B+1)^2)`.
The released tilde trace carries an additional factor `L^-2`, proving (R1).
The scaling asserted in the finite-section note is correct.

## 2. Coefficient endpoint check

Put

\[
 a_T(n)=|c_T(n)|^2/n,\qquad
 \mu_T=l^{-2}\sum_{n\le X}a_T(n)\,\delta_{\log n/l},
 \qquad X=e^{\lambda l}.
\]

Weak convergence of `mu_T` to a measure with no atom at `lambda` gives

\[
 \sum_{n\le X}|c_T(n)|^2=o(Xl^2).                    \tag{R6}
\]

The separate two-block Cauchy--Schwarz argument gives

\[
 S_1(c_T;X)^2=o(Xl^2).                               \tag{R7}
\]

The shrinking-collar step is legitimate: for every fixed `delta>0`, the
collar of width `A/l` is eventually contained in the closed interval
`[lambda-delta,lambda]`; Portmanteau followed by `delta downarrow 0` uses
exactly the no-atom assumption.  The integer counting factor in (R7) is
essential and is correctly present.

At `lambda=1`, the exact fixed-coefficient `PP` remainder

\[
 L\left(\sum |c_n|^2/n+\sum|c_n|^2+S_1(c;X)^2\right)
\]

is consequently `o(T L l^2)`.  This part of the endpoint argument is valid.

## 3. Fatal issues for an unconditional `lambda=1` claim

These issues are fatal only to the claim that the **full transfer is already
proved**.  They do not invalidate the finite-section theorem.

### F1. The current second-trace assembly still uses strict subcriticality

`XiPrime/PrimeSide/Traces.lean` defines `FactsXi.lam_lt_one` and proves `tr2`
by bounding the collected remainder with

\[
 E(T)=2l(T)^2X(T)/T.
\]

The decisive call is to `tendsto_l_sq_mul_X_div`; at `lambda=1`, `E(T)` does
not tend to zero.  Replacing `lem_ends` alone therefore does not make the
existing proof compile or become valid.

This is repairable, but the proof must be reorganized: use (R6)--(R7) for the
base `PP` error, use (R1) for the end error, and compare the remaining cross
terms separately.  Their endpoint ratios do vanish:

\[
 \frac{L l^2\sqrt X}{T L l^2}=O(T^{-1/2}),\qquad
 \frac{L X l}{T L l^2}=O(l^{-1}).
\]

The first trace also survives at `lambda=1`; its current proof merely encodes
a stronger-than-needed `lambda<1` hypothesis.

### F2. Entry-dependent coefficient transfer has a second strict use

`XiPrime/Transfer.lean` proves entry dependence negligible using

\[
 l(T)^4X(T)/T\longrightarrow0,
\]

at the construction of `hsmallX`.  This comes from the coefficient-independent
end floor in the current `ReexpansionGeom.sumSq_le`.  At `lambda=1` the limit
fails.

Radial recession supplies the right repair in principle: every re-expansion
coefficient `e_r` carries a factor `(rho_0/l)^r`, and a genuinely homogeneous
`PPUpper` preserves its square.  For the first variation this gives a factor
`O(l^-2)`, enough at the endpoint.  But the homogeneous theorem has not yet
been substituted through `reexpansionGeom_of`, `hatNegligible_of_geom`, and
`xiTraceTransfer_of`.  Moreover, there are currently two isolated
`PPUpperHomogeneous` prototypes with overlapping names and different local
coefficient-sum facades; this needs one canonical integrated interface.

Without that integration, the full endpoint transfer does not follow.

### F3. The explicit-formula family interface still states `lambda<1`

`FamilyHyps.lam_const` and all downstream xi explicit-formula theorems require
strict `lambda<1`.  The displayed analytic error is based on
`X^(3/4)`, so at `lambda=1` there remains a genuine power saving
`T^(-1/4)` before logarithms; the proof appears extendable.  Nevertheless,
the endpoint version is not a theorem in the tree and must be restated and
checked.  It should not be described as already released for `lambda<=1`.

### F4. The hard profile itself is not obtained as one admissible amplitude

For the flat, quartic, or degree-eight target, `sqrt(v)` followed by abrupt
extension by zero is not smooth because `v` is positive at the endpoints.
The collar construction proves results for smooth `h_eta`, and continuity
recovers any **strictly slack numerical inequality** or an iterated limiting
constant.  It does not prove a fixed-window theorem for the discontinuous
hard amplitude `sqrt(v) 1_{[-1/2,1/2]}`.

This distinction is harmless for the published decimal bounds, which have
strict slack, but it must be explicit in a theorem statement.

## 4. Nonfatal corrections and qualifications

1. The notation `h in C_c^infinity((-1/2,1/2))` means support a positive
   distance from the endpoints.  The intended flat endpoint bump that is
   nonzero arbitrarily close to `+/-1/2` should instead be stated as
   `h in C_c^infinity(R)` with `supp h subset [-1/2,1/2]`.

2. The compatibility claim using an old `P.atV(h^2)` for `h` supported a
   positive distance from the endpoints is true, but such a window has
   strictly smaller effective exponential type.  It is not the same object
   as the endpoint-reaching collar used to test exact bandwidth.  The latter
   needs the proposed new amplitude interface because the old microscopic
   taper changes it near the endpoint.

3. The standalone finite-section theorem should state `H` real, or replace
   ordinary products and squares by the appropriate conjugated kernels.  The
   application is real, so this is only a statement-level correction.

4. The density version should state `B>=0`, measurability/integrability, and
   the precise pointwise majorant.  The xi density satisfies these conditions.

5. `H3` is needed for the base `PP` endpoint.  It is not needed merely to
   make the new full-density end estimate negligible: the released H1-sized
   bound `B^2=O(Xl^2)` already gives a factor `1/L` against `T L l^2` at
   `lambda=1`.

6. Equation (13) in the soft-edge audit has the correct scale
   `O_h((LT^2)^-1)` when two integrations by parts are available, but the
   finite-section logarithmic-weight proof is cleaner and avoids relying on
   that sharper auxiliary estimate.

7. The informal signed-Gram/operator proof needs trace-class bookkeeping for
   the omitted infinite block.  The elementary normalized proof avoids this
   issue and should be the canonical proof.

## 5. Corrected theorem statements

### A. Unconditional analytic core

> **Finite-section amplitude theorem.**  Let
> `h in C_c^infinity(R)` be real and even, with
> `supp h subset [-1/2,1/2]`, and put
> `phi_L(u)=h(u/L)`.  Let `T,L>=1`,
> `d=floor(LT/(2*pi))`, and `tau_k=T+2*pi*k/L`.
> If `nu` is real measurable and, for some `B>=0`,
> \[
> |\nu(\tau)|\le B+\log^+(|\tau|/(4T)),
> \]
> then, whenever the displayed Gram integrals exist,
> \[
> \left|L^{-2}\sum_{k,l<d}
> \left(\int\widehat\phi_L(\tau-\tau_k)
>              \widehat\phi_L(\tau-\tau_l)\nu(\tau)\,d\tau\right)^2
> -\mathcal M_h(\nu;T)\right|
> \le C_h(B+1)^2,
> \]
> where
> \[
> \mathcal M_h(\nu;T)=
> \iint_{[T,2T]^2}L^2\widehat{h^2}(L(\tau-\tau'))^2
> \nu(\tau)\nu(\tau')\,d\tau\,d\tau'.
> \]

The normalization of `M_h` agrees with the released `Mform`, since
`Phi_L(r)=L widehat{h^2}(Lr)` and the tilde normalization cancels `L^2`.

### B. Honest endpoint-transfer candidate

> **Critical amplitude transfer, conditional integration form.**  Fix a
> real even nonzero smooth amplitude `h`, `0<=h<=1`, with
> `supp h subset [-1/2,1/2]`.  Assume:
>
> 1. the `lambda=1` amplitude-window local and zero-side hypotheses;
> 2. the `lambda=1` xi explicit formula with its entry error;
> 3. the coefficient diagonal law with a continuous endpoint density;
> 4. the exact fixed-coefficient `PP` estimate;
> 5. a homogeneous `PPUpper` threaded through every re-expansion coefficient;
> 6. the existing gamma, Riemann--von Mangoldt, cross-term, and re-expansion
>    hypotheses.
>
> Then the two trace asymptotics extend to `lambda=1`, with limiting window
> constant computed from `v=h^2`.

This statement is supported by the audited estimates, but it is not yet a
theorem of the Lean development.  For a target hard energy profile positive
at the endpoints, it applies to each fixed collared amplitude `h_eta`.
Continuity as `eta downarrow 0` transfers any numerical certificate with
strict slack; it does not turn the hard discontinuous amplitude into an
admissible fixed window.

## 6. Status ledger

### PROVED at paper level

- uniform finite-section interior and weighted exterior bounds;
- exact Fourier/Poisson normalization and raw/tilde `L`-scaling;
- validity for signed densities under an absolute pointwise majorant;
- H3/no-endpoint-atom deweighting, including `sum |c_n|^2` and `S1^2`;
- continuity of the mass, energy, autocorrelation, `jWin`, `cWin`, and
  `kappaXi` functionals under fixed collars.

### KERNEL-CHECKED BUT NOT INTEGRATED INTO THE ENDPOINT TRANSFER

- radial recession/homogenization lemmas;
- coefficient scaling identities in the isolated homogeneous `PPUpper`
  prototypes.

### STRONGLY SUPPORTED

- a complete fixed-amplitude `lambda=1` two-trace theorem after the four
  interface/assembly changes identified above;
- recovery of the existing strict decimal certificates with one sufficiently
  small fixed collar.

### NOT PROVED

- the full `lambda=1` theorem in the current source tree;
- an admissible theorem for the discontinuous hard amplitude itself;
- any new numerical percentage solely from setting `lambda=1`;
- the Riemann Hypothesis.

## Bottom line

The simple abstraction is correct:

\[
 \boxed{\text{Choose one smooth amplitude and dilate it exactly.}}
\]

It really removes the old boundary loss.  The remaining work is not a new
analytic idea; it is a precise endpoint refactor of the trace assembly,
entry-dependent homogeneous `PPUpper`, explicit-formula family interface,
and collared-window certificate.
