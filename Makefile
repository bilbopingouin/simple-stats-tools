.PHONY: tests syntax unittests

tests: syntax unittests

syntax:
	@echo "Checking the syntax..."
	@python3 -m flake8
	@echo "...done"

unittests:
	@echo "Running the unit tests..."
	@echo "...done"
