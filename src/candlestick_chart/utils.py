from __future__ import annotations

import math
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

from candlestick_chart import constants
from candlestick_chart.candle import Candle

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

    from candlestick_chart.candle import Candles


# For compact numbers formatting
REPLACE_CONSECUTIVE_ZEROES = re.compile(r"(0\.)(0{4,})(.{4}).*").sub


def fnum_replace_consecutive_zeroes(match: re.Match[str]) -> str:
    p1, p2, p3 = match.groups()
    return "".join([p1, f"⦗0×{len(p2)}⦘", p3])


def fnum(value: float | str) -> str:
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            value = float(value)

    # 0, 0.00, > 1, and > 1.00 (same for negative numbers)
    if not value or abs(value) >= 1:
        return f"{value:,}" if isinstance(value, int) else f"{value:,.{constants.PRECISION}f}"

    # 0.000000000012345678 -> 0.⦗0×10⦘1234
    formatted = REPLACE_CONSECUTIVE_ZEROES(fnum_replace_consecutive_zeroes, f"{value:.18f}")
    return formatted if "0×" in formatted else f"{value:.{constants.PRECISION_SMALL}f}"


def hexa_to_rgb(hex_code: str) -> tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    r = int(hex_code[:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b


def make_candles(iterator: Iterator[Any]) -> Candles:
    return [Candle(**item) for item in iterator]


def parse_candles_from_csv(file: str | Path) -> Candles:
    import csv

    with Path(file).open() as fh:
        return make_candles(csv.DictReader(fh))


def parse_candles_from_json(file: str | Path) -> Candles:
    import json

    return make_candles(json.loads(Path(file).read_text()))


def parse_candles_from_stdin() -> Candles:
    import json
    import sys

    return make_candles(json.loads("".join(sys.stdin)))


def round_price(
    value: float, *, fn_down: Callable[[float], float] = math.floor, fn_up: Callable[[float], float] = math.ceil
) -> str:
    if constants.Y_AXIS_ROUND_MULTIPLIER > 0.0:
        multiplier = constants.Y_AXIS_ROUND_MULTIPLIER
        if constants.Y_AXIS_ROUND_DIR == "down":
            value = fn_down(value * multiplier) / multiplier
        else:
            value = fn_up(value * multiplier) / multiplier
    return fnum(value)
