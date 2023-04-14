#!/bin/bash
set -eu

python -m isort src examples
python -m black --line-length=120 src examples
python -m flake8 src examples
python -m mypy src examples --exclude tests
echo "ok"
