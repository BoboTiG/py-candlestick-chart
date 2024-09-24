#!/bin/bash
set -eu

python -m ruff format src examples
python -m ruff check --fix --unsafe-fixes src examples
python -m mypy src examples
echo "ok"
