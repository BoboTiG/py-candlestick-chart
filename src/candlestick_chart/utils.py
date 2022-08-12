import re
from pathlib import Path
from typing import Any, Iterator, Match, Tuple

from . import constants
from .candle import Candle, Candles

# For compact numbers formatting
REPLACE_CONSECUTIVE_ZEROES = re.compile(r"(0\.)(0{4,})(.{4}).*").sub


def fnum_replace_consecutive_zeroes(match: Match[str]) -> str:
    p1, p2, p3 = match.groups()
    return "".join([p1, f"⦗0×{len(p2)}⦘", p3])


def fnum(value: int | float | str) -> str:
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            value = float(value)

    # 0, 0.00, > 1, and > 1.00 (same for negative numbers)
    if not value or abs(value) >= 1:
        return (
            f"{value:,}"
            if isinstance(value, int)
            else f"{value:,.{constants.PRECISION}f}"
        )

    # 0.000000000012345678 -> 0.⦗0×10⦘1234
    formatted = REPLACE_CONSECUTIVE_ZEROES(
        fnum_replace_consecutive_zeroes, f"{value:.18f}"
    )
    return formatted if "0×" in formatted else f"{value:.{constants.PRECISION_SMALL}f}"


def hexa_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    r = int(hex_code[:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b


def make_candles(iterator: Iterator[Any]) -> Candles:
    return [Candle(**item) for item in iterator]


def parse_candles_from_csv(file: str) -> Candles:
    import csv

    with Path(file).open() as fh:
        return make_candles(csv.DictReader(fh))


def parse_candles_from_json(file: str) -> Candles:
    import json

    return make_candles(json.loads(Path(file).read_text()))


def parse_candles_from_stdin() -> Candles:
    import json
    import sys

    return make_candles(json.loads("".join(sys.stdin)))
