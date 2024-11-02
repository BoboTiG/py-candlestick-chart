from unittest.mock import patch

import pytest

from candlestick_chart.candle import Candle
from candlestick_chart.chart_data import ChartData
from candlestick_chart.volume_pane import VolumePane

CANDLE = Candle(open=1, high=2, low=0.5, close=1.2)


@pytest.fixture(scope="module")
def chart_data() -> ChartData:
    return ChartData([CANDLE], width=100, height=50)


def test_candle_eq() -> None:
    candle1 = Candle(open=1, high=2, low=0.5, close=1.2)
    assert candle1 == CANDLE

    candle2 = Candle(open=1.1, high=2.1, low=0.51, close=1.21)
    assert candle2 != CANDLE

    with pytest.raises(NotImplementedError):
        assert object() == CANDLE


def test_candle_repr() -> None:
    assert repr(CANDLE) == "Candle<open=1.0, low=0.5, high=2.0, close=1.2, volume=0.0, timestamp=0.0, type=bullish>"


def test_compute_height_take_into_account_constant_change(chart_data: ChartData) -> None:
    volume_pane = VolumePane(0, enabled=False)
    chart_data.compute_height(volume_pane)
    original_height = chart_data.height
    assert original_height

    with patch("candlestick_chart.constants.MARGIN_TOP", 0):
        chart_data.compute_height(volume_pane)
        new_height = chart_data.height

    assert new_height > original_height
