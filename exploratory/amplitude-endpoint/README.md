# Exact-amplitude endpoint program

> [!CAUTION]
> This branch is exploratory. It records a proposed self-similar amplitude formulation for the xi-prime trace method, together with a hostile internal review. It does **not** contain an integrated critical-bandwidth theorem.

## Central candidate

The proposed replacement is to choose one fixed smooth amplitude and dilate it exactly,

`phi_L(u)=h(u/L), v=h^2`,

so that the zero side and finite-section prime-side boundary are controlled by the same profile. The associated log-energy representation is intended to preserve endpoint information that is lost by separate coarse coefficient norms.

## Controlling status

The hostile report concludes that the finite-section boundary estimate and endpoint log-energy deweighting are credible at paper level, but identifies three downstream gaps:

1. componentwise second-trace assembly at `lambda = 1`;
2. integration of a homogeneous `PPUpper` through the entry-dependent re-expansion chain;
3. an endpoint explicit-formula family interface.

Accordingly, this branch is retained as a research program rather than an established theorem.
