.PHONY: certify verify check paper all

certify:
	cd publication/low-multiplicity-zeta && python certify_low_multiplicity_exact.py

verify:
	cd publication/low-multiplicity-zeta && python audit_low_multiplicity_symbolic.py
	cd publication/low-multiplicity-zeta && python verify_multiplicity_hierarchy.py

check: certify verify

paper:
	./scripts/build_paper.sh

all: check paper
