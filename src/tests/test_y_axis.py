import pytest

from candlestick_chart import colors
from candlestick_chart.candle import Candle
from candlestick_chart.chart_data import ChartData
from candlestick_chart.y_axis import YAxis

CANDLES = [Candle(open=1, high=2, low=0.5, close=1.2, volume=1_234_567)]
WIDTH = 80
HEIGHT = 24
CHART_DATA = ChartData(CANDLES, width=WIDTH, height=HEIGHT)


@pytest.fixture
def y_axis() -> YAxis:
    return YAxis(CHART_DATA)


def test_render_empty_with_highlighted_price(y_axis: YAxis) -> None:
    price = f"{CANDLES[0].open:.02f}"
    highlights = {"10.00": "green", price: "green"}
    rendered = y_axis.render_empty(y=8, highlights=highlights)  # type: ignore[arg-type]
    assert colors.green(f"{price}         ┤") in rendered
