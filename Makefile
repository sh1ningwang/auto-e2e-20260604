# Minimal deterministic project for /auto E2E (no toolchain install).
.PHONY: check test

check:
	@echo "build-check ok"

test:
	@echo "running tests"
	@echo "(one skipped test — see src/widget.py::test_rounding)"
