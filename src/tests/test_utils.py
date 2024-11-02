from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

from candlestick_chart import Candle, utils


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, "0"),
        (0.0, "0.00"),
        (123456789, "123,456,789"),
        (1.23456789, "1.23"),
        (1234.56789, "1,234.57"),
        (1.0, "1.00"),
        (0.1, "0.1000"),
        (0.01, "0.0100"),
        (0.001, "0.0010"),
        (0.0001, "0.0001"),
        (0.00001, "0.⦗0×4⦘1000"),
        (0.000001, "0.⦗0×5⦘1000"),
        (0.0000001, "0.⦗0×6⦘1000"),
        (0.000000000012340000, "0.⦗0×10⦘1234"),
        (0.000000000012345678, "0.⦗0×10⦘1234"),
        (0.123456789, "0.1235"),
    ],
)
def test_fnum(value: float, expected: str) -> None:
    assert utils.fnum(value) == expected
    assert utils.fnum(str(value)) == expected
    if value != 0.0:
        assert utils.fnum(value * -1) == f"-{expected}"


def test_fnum_precision() -> None:
    with patch("candlestick_chart.constants.PRECISION", 0):
        assert utils.fnum(1.0) == "1"
    with patch("candlestick_chart.constants.PRECISION", 10):
        assert utils.fnum(1.0) == "1.0000000000"


def test_fnum_precision_small() -> None:
    with patch("candlestick_chart.constants.PRECISION_SMALL", 0):
        assert utils.fnum(0.123456789) == "0"
    with patch("candlestick_chart.constants.PRECISION_SMALL", 6):
        assert utils.fnum(0.123456789) == "0.123457"


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("#b967ff", (185, 103, 255)),
        ("ff6b99", (255, 107, 153)),
    ],
)
def test_hexa_to_rgb(code: str, expected: tuple[int, int, int]) -> None:
    assert utils.hexa_to_rgb(code) == expected


def test_parse_candles_from_csv(data: Path) -> None:
    file = str(data / "BTC-USD.csv")
    candles = utils.parse_candles_from_csv(file)
    assert len(candles) == 312
    assert candles[0] == Candle(
        open=28994.009766,
        close=29374.152344,
        high=29600.626953,
        low=28803.585938,
        volume=40730301359.0,
        timestamp=1652997600.0,
    )
    assert candles[-1] == Candle(
        open=63344.066406,
        close=67566.828125,
        high=67673.742188,
        low=63344.066406,
        volume=41125608330.0,
        timestamp=1679868000.0,
    )


def test_parse_candles_from_json(data: Path) -> None:
    file = str(data / "BTC-chart.json")
    candles = utils.parse_candles_from_json(file)
    assert len(candles) == 2
    assert candles[0] == Candle(
        open=28994.009766,
        close=29374.152344,
        high=29600.626953,
        low=28803.585938,
        volume=0.0,
        timestamp=0.0,
    )
    assert candles[1] == Candle(
        open=29376.455078,
        close=32127.267578,
        high=33155.117188,
        low=29091.181641,
        volume=0.0,
        timestamp=0.0,
    )


def test_parse_candles_from_stdin(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "sys.stdin",
        StringIO(
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
        ),
    )
    candles = utils.parse_candles_from_stdin()
    assert len(candles) == 2
    assert candles[0] == Candle(
        open=28994.009766,
        close=29374.152344,
        high=29600.626953,
        low=28803.585938,
        volume=0.0,
        timestamp=0.0,
    )
    assert candles[1] == Candle(
        open=29376.455078,
        close=32127.267578,
        high=33155.117188,
        low=29091.181641,
        volume=0.0,
        timestamp=0.0,
    )


@pytest.mark.parametrize(
    ("value", "expected_down", "expected_up"),
    [
        (0.0, "0.00", "0.00"),
        (0.01234, "0.0100", "0.0200"),
        (32_574.913_021_333_333, "32,574.91", "32,574.92"),
    ],
)
def test_round_price(value: float, expected_down: str, expected_up: str) -> None:
    with patch("candlestick_chart.constants.Y_AXIS_ROUND_MULTIPLIER", 1 / 0.01):
        with patch("candlestick_chart.constants.Y_AXIS_ROUND_DIR", "down"):
            assert utils.round_price(value) == expected_down
        with patch("candlestick_chart.constants.Y_AXIS_ROUND_DIR", "up"):
            assert utils.round_price(value) == expected_up
