.venv:
	python -m venv .venv
	.venv/bin/pip install -U pip

deps: .venv
	.venv/bin/pip install -r requirements.txt

test: format lint typecheck
	.venv/bin/coverage erase
	.venv/bin/coverage run --source=aoc2018 --omit=aoc2018/exercises/*,aoc2018/inputs.py --branch -m unittest discover -s tests -v
	.venv/bin/coverage html
	.venv/bin/coverage report --fail-under 90

format:
	.venv/bin/black aoc2018 tests

lint:
	.venv/bin/flake8 --ignore W503 --max-line-length 88 --max-complexity 5 aoc2018 tests

typecheck:
	.venv/bin/mypy aoc2018 tests

# for linux, switch to time -v
run:
	time -l .venv/bin/python -m aoc2018.exercises.ex$(ex)
