# Exploratory research archive index

> [!CAUTION]
> Everything in `exploratory/` is unrefereed. These branches contain exact algebra, computational certificates, paper-level lemmas, and proposed proof architectures, but none proves the Riemann Hypothesis or establishes a new general zero-density theorem.

## 1. Exact-amplitude endpoint program

Directory: [`amplitude-endpoint/`](amplitude-endpoint/)

Central representation:

\[
\phi_L(u)=h(u/L),\qquad \widehat{\phi_L}(r)=L\widehat h(Lr),\qquad v=h^2.
\]

Strongest surviving analytic claim: for one fixed real even smooth amplitude, the normalized finite-section boundary defect is uniformly bounded by

\[
\left|L^{-2}\operatorname{tr}G^2-\mathcal M_h\right|\ll_h(B+1)^2.
\]

The log-energy measure

\[
\mu_T=\ell^{-2}\sum_{n\le X}\frac{|c_T(n)|^2}{n}\,\delta_{\log n/\ell}
\]

explains why the fixed prime-prime error is endpoint-negligible when the limiting measure has no atom at the cutoff.

Unclosed seams: componentwise second-trace assembly, homogeneous re-expansion through the full transfer chain, endpoint explicit-formula wrapper, admissible amplitude instances, full Lean replay, and independent specialist review. The hostile referee report in this directory is the controlling status document.

## 2. Xi-prime and short-interval program

Directory: [`xi-prime-and-short-interval/`](xi-prime-and-short-interval/)

Computational result: an exact-rational optimized xi-prime window certificate was reported with approximately

\[
p_{\rm simple}>0.868641500529012,
\qquad
p_{\rm distinct}>0.934320750264506.
\]

This is a window-functional certificate, not an integrated zeta or xi-prime theorem.

Two proposed localization thresholds appear in the research record:

- xi-prime Fredholm crossing: \(0.513319759847686\ldots\);
- zeta scalar-window crossing: \(0.550193964744154\ldots\).

Neither number is presently an established short-interval theorem. The missing work includes a uniform two-scale explicit formula, local prime-side moments, local zero counting, entry-dependent re-expansion, and the final inertia transfer.

## 3. Horizontal-depth spectrum and positivity barrier

Directory: [`depth-spectrum/`](depth-spectrum/)

For an isolated reflected pair at horizontal depth \(y\), the normalized pair block has eigenvalues

\[
\lambda_+(Ly)=m(c_h(Ly)+1),
\qquad
\lambda_-(Ly)=-m(c_h(Ly)-1),
\]

where

\[
c_h(t)=\frac{\int h(s)^2\cosh(2ts)\,ds}{\int h(s)^2\,ds}.
\]

Thus an isolated pair contains exact depth information. An abstract cyclic construction shows that aggregate spectral moments can nevertheless lose all depth information.

Proposed no-go principle: if a scalar or matrix kernel makes every admissible cross interaction positive semidefinite for depths \(|y|\le Y\), then it must obey a decay bound of the form

\[
\|K(u)\|\le \|K(0)\|\operatorname{sech}^2(Yu),
\]

which consumes the desired horizontal exponential gain. This is a harmonic-analysis statement under its explicit positivity hypothesis; it is not an observability theorem for arbitrary zeta-zero configurations.

## 4. Critical-edge resonance and Nyquist nullity

Directory: [`critical-edge-nyquist/`](critical-edge-nyquist/)

A smooth arithmetic-progression packet is super-polynomially small throughout every fixed strictly subcritical bandwidth, but resonates inside a collar of width approximately

\[
|t-\ell|\asymp \ell/R
\]

at the critical edge. Interlaced phase classes can cancel there.

If the phase polynomial has endpoint zero of order \(k\), the model edge energy scales as

\[
\int |P(\alpha)A_R(\alpha)|^2\,d\alpha\asymp R^{1-2k}.
\]

This motivates the term **Nyquist nullity**. The Bessel-family calculation shows that a linear bank cannot recover the lost factor inside this model. No theorem currently rules out such null configurations for actual zeta zeros.

## 5. Complementary-band Hankel program

Directory: [`complementary-hankel/`](complementary-hankel/)

For moments

\[
s_n=\sum_j b_jz_j^n,
\]

the Hankel determinant satisfies the exact finite-rank factorization

\[
\det[s_{r+i+j}]_{0\le i,j<K}
=\left(\prod_j b_j\right)
 \left(\prod_j z_j\right)^r
 \prod_{i<j}(z_j-z_i)^2
\]

when exactly \(K\) nodes are present. A product of prime-side Dirichlet polynomials of normalized support lengths \(\alpha_i\) remains within critical length when

\[
\sum_i\alpha_i\le1.
\]

This gives a plausible nonlinear detector that can defeat certain linear phase aliases without automatically exceeding prime bandwidth. The open problem is not the finite-rank algebra; it is stable observability for arbitrary clusters, including control of cancellation among the Cauchy--Binet subset terms and complete archimedean/convolution bookkeeping.

## Publication boundary

The only branch currently organized as a publication candidate is [`publication/low-multiplicity-zeta/`](../publication/low-multiplicity-zeta/). The exploratory branches should be cited only with their exact status labels and should not be described as established progress toward RH until their listed analytic or observability seams are closed.
