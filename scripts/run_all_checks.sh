#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
PUB="$ROOT/publication/low-multiplicity-zeta"

run() { printf '\n==> %s\n' "$*"; "$@"; }

run python "$PUB/certify_low_multiplicity_exact.py"
if python - <<'PY' >/dev/null 2>&1
import sympy, mpmath
PY
then
  run python "$PUB/audit_low_multiplicity_symbolic.py"
  run python "$PUB/verify_multiplicity_hierarchy.py"
else
  echo 'Optional SymPy/mpmath checks skipped: dependencies not installed.'
fi

echo
echo 'All tracked low-multiplicity checks completed. Passing a script validates only its stated scope.'
