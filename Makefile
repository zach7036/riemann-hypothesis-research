.PHONY: certify verify exploratory paper all publish

certify:
	cd publication/low-multiplicity-zeta && python certify_low_multiplicity_exact.py
	cd publication/low-multiplicity-zeta && python certify_low_multiplicity.py
	cd exploratory/xi-prime-and-short-interval && python xi_prime_optimal_window_certificate.py --json /tmp/xi_prime_optimal_window_certificate.json

verify:
	cd publication/low-multiplicity-zeta && python audit_low_multiplicity_symbolic.py
	cd publication/low-multiplicity-zeta && python verify_multiplicity_hierarchy.py

exploratory:
	cd exploratory/depth-spectrum && python verify_rh_depth_barrier.py
	cd exploratory/critical-edge-nyquist && python verify_critical_edge_bow.py
	cd exploratory/complementary-hankel && python verify_complementary_hankel.py
	cd exploratory/xi-prime-and-short-interval && python short_interval_constants.py

paper:
	./scripts/build_paper.sh

all:
	./scripts/run_all_checks.sh
	./scripts/build_paper.sh

publish:
	./scripts/publish_to_github.sh
