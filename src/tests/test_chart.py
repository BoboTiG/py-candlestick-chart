from unittest.mock import patch

import pytest
from rich.console import Console

from candlestick_chart import constants
from candlestick_chart.candle import Candle
from candlestick_chart.chart import Chart

CANDLE = Candle(open=1, high=2, low=0.5, close=1.2, volume=1_234_567)
WIDTH = 80
HEIGHT = 24


@pytest.fixture
def chart() -> Chart:
    return Chart([CANDLE], title="BTC/USDT", width=WIDTH, height=HEIGHT)


def test_rich_repr(chart: Chart) -> None:
    console = Console(highlight=False, force_terminal=True, width=WIDTH, height=HEIGHT)
    with console.capture() as capture:
        console.print(chart)

    output = capture.get()
    assert chart.info_bar.name in output
    assert constants.UNICODE_Y_AXIS_LEFT in output
    assert constants.UNICODE_Y_AXIS_RIGHT not in output


def test_rich_repr_with_y_axis_on_the_right(chart: Chart) -> None:
    console = Console(highlight=False, force_terminal=True, width=WIDTH, height=HEIGHT)
    with (
        patch("candlestick_chart.constants.Y_AXIS_ON_THE_RIGHT", True),  # noqa: FBT003
        console.capture() as capture,
    ):
        console.print(chart)

    output = capture.get()
    assert chart.info_bar.name in output
    assert constants.UNICODE_Y_AXIS_LEFT not in output
    assert constants.UNICODE_Y_AXIS_RIGHT in output


def test_set_label(chart: Chart) -> None:
    value = "foo"

    for label in vars(constants.LABELS):
        assert getattr(chart.info_bar.labels, label) != value
        chart.set_label(label, value)
        assert getattr(chart.info_bar.labels, label) == value


def test_set_highlight(chart: Chart) -> None:
    assert not chart.highlights

    # Add highlighted prices
    chart.set_highlight("4.2", "red")
    chart.set_highlight("4.2", "green")
    chart.set_highlight("2.4569", "orange")
    assert chart.highlights == {"2.4569": "orange", "4.2": "green"}

    # Remove a price
    chart.set_highlight("2.4569", "")
    assert chart.highlights == {"4.2": "green"}


def test_set_name(chart: Chart) -> None:
    name = "Magic Chart"
    assert chart.info_bar.name != name

    chart.set_name(name)
    assert chart.info_bar.name == name


def test_set_vol_bear_color(chart: Chart) -> None:
    color = (3, 2, 1)
    assert chart.volume_pane.bearish_color != color

    chart.set_vol_bear_color(*color)
    assert chart.volume_pane.bearish_color == color


def test_set_vol_bull_color(chart: Chart) -> None:
    color = (1, 2, 3)
    assert chart.volume_pane.bullish_color != color

    chart.set_vol_bull_color(*color)
    assert chart.volume_pane.bullish_color == color


def test_set_volume_pane_enabled(chart: Chart) -> None:
    assert chart.volume_pane.enabled

    chart.set_volume_pane_enabled(False)
    assert not chart.volume_pane.enabled


def test_set_volume_pane_unicode_fill(chart: Chart) -> None:
    value = "°"

    assert chart.volume_pane.unicode_fill != value

    chart.set_volume_pane_unicode_fill(value)
    assert chart.volume_pane.unicode_fill == value


def test_update_candles(chart: Chart) -> None:
    assert len(chart.chart_data.main_candle_set.candles) == 1

    chart.update_candles([CANDLE] * 4, reset=True)
    assert len(chart.chart_data.main_candle_set.candles) == 4

    candle = CANDLE
    candle.volume = 0.00001
    chart.update_candles([candle])
    assert len(chart.chart_data.main_candle_set.candles) == 5


def test_update_size(chart: Chart) -> None:
    assert chart.chart_data.terminal_size == (WIDTH, HEIGHT)

    # No change
    chart.update_size(WIDTH, HEIGHT)
    assert chart.chart_data.terminal_size == (WIDTH, HEIGHT)

    # New size
    chart.update_size(WIDTH * 2, HEIGHT * 2)
    assert chart.chart_data.terminal_size == (WIDTH * 2, HEIGHT * 2)

    # No change
    chart.update_size(WIDTH * 2, HEIGHT * 2)
    assert chart.chart_data.terminal_size == (WIDTH * 2, HEIGHT * 2)
