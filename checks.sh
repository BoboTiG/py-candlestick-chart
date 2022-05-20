#!/bin/bash
set -eu

python -m black src examples
python -m flake8 src examples
python -m mypy src examples
echo "ok"
