#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
PUB="$ROOT/publication/low-multiplicity-zeta"

run() { printf '\n==> %s\n' "$*"; "$@"; }

run python "$PUB/certify_low_multiplicity_exact.py"
run python "$PUB/certify_low_multiplicity.py"

if python - <<'PY' >/dev/null 2>&1
import sympy, numpy, scipy, mpmath
PY
then
  run python "$PUB/audit_low_multiplicity_symbolic.py"
  run python "$PUB/verify_multiplicity_hierarchy.py"
else
  echo 'Optional SymPy/NumPy/SciPy/mpmath checks skipped: dependencies not installed.'
fi

run python "$ROOT/exploratory/depth-spectrum/verify_rh_depth_barrier.py"
run python "$ROOT/exploratory/critical-edge-nyquist/verify_critical_edge_bow.py"
run python "$ROOT/exploratory/complementary-hankel/verify_complementary_hankel.py"
run python "$ROOT/exploratory/xi-prime-and-short-interval/xi_prime_optimal_window_certificate.py" --json /tmp/xi_prime_optimal_window_certificate.json
run python "$ROOT/exploratory/xi-prime-and-short-interval/short_interval_constants.py"

echo
echo 'All available checks completed. Passing a script validates only the scope stated in that script.'
