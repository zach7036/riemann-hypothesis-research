#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
PAPER="$ROOT/publication/low-multiplicity-zeta"
cd "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error low_multiplicity_zeta.tex
pdflatex -interaction=nonstopmode -halt-on-error low_multiplicity_zeta.tex
pdflatex -interaction=nonstopmode -halt-on-error low_multiplicity_zeta.tex
printf 'Built %s\n' "$PAPER/low_multiplicity_zeta.pdf"
