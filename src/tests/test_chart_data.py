from unittest.mock import patch

import pytest

from candlestick_chart.candle import Candle
from candlestick_chart.chart_data import ChartData
from candlestick_chart.volume_pane import VolumePane


@pytest.fixture(scope="module")
def chart_data() -> ChartData:
    return ChartData([Candle(open=1, high=1, low=1, close=1)], width=100, height=50)


def test_compute_height_take_into_account_constant_change(chart_data: ChartData) -> None:
    volume_pane = VolumePane(0, enabled=False)
    chart_data.compute_height(volume_pane)
    original_height = chart_data.height
    assert original_height

    with patch("candlestick_chart.constants.MARGIN_TOP", 0):
        chart_data.compute_height(volume_pane)
        new_height = chart_data.height

    assert new_height > original_height
