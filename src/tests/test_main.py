import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

from candlestick_chart.__main__ import main

EXAMPLES = Path(__file__).parent.parent.parent / "examples"
OPTIONAL_ARGS = [
    "",
    "--chart-name=My BTC Chart",
    "--bear-color=#b967ff",
    "--bull-color=ff6b99",
]


def run(args: list[str]) -> None:
    with patch.object(sys, "argv", new=["candlestick-chart", *filter(lambda a: a, args)]):
        assert main() == 0


@pytest.mark.parametrize("additional_arg", OPTIONAL_ARGS)
def test_mode_stdin(additional_arg: str) -> None:
    data = StringIO(
        """[
  {
    "open": 28994.009766,
    "high": 29600.626953,
    "low": 28803.585938,
    "close": 29374.152344
  },
  {
    "open": 29376.455078,
    "high": 33155.117188,
    "low": 29091.181641,
    "close": 32127.267578
  }
]""",
    )
    with patch.object(sys, "stdin", data):
        run(["--mode=stdin", additional_arg])


@pytest.mark.parametrize("additional_arg", OPTIONAL_ARGS)
def test_mode_csv_file(additional_arg: str) -> None:
    file = EXAMPLES / "BTC-USD.csv"
    run(["--mode=csv-file", f"--file={file}", additional_arg])


@pytest.mark.parametrize("additional_arg", OPTIONAL_ARGS)
def test_mode_json_file(additional_arg: str) -> None:
    file = EXAMPLES / "BTC-chart.json"
    run(["--mode=json-file", f"--file={file}", additional_arg])
