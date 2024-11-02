import pytest

from candlestick_chart import constants
from candlestick_chart.candle import Candle
from candlestick_chart.candle_set import CandleSet
from candlestick_chart.info_bar import InfoBar

CANDLES = [Candle(open=1, high=2, low=0.5, close=1.2, volume=1_234_567)]
CANDLE_SET = CandleSet(CANDLES)
WIDTH = 80


@pytest.fixture
def info_bar() -> InfoBar:
    return InfoBar("BTC/USD")


def test_render_with_currency(info_bar: InfoBar) -> None:
    label = info_bar.labels.currency
    assert label == constants.LABELS.currency
    assert not label

    label = "€€€€€€€"
    info_bar.labels.currency = label
    assert label in info_bar.render(CANDLE_SET, WIDTH)


def test_render_without_average(info_bar: InfoBar) -> None:
    label = info_bar.labels.average
    assert label == constants.LABELS.average
    assert label
    assert label in info_bar.render(CANDLE_SET, WIDTH)

    info_bar.labels.average = ""
    assert label not in info_bar.render(CANDLE_SET, WIDTH)


def test_render_without_variation(info_bar: InfoBar) -> None:
    label = info_bar.labels.variation
    assert label == constants.LABELS.variation
    assert label
    assert label in info_bar.render(CANDLE_SET, WIDTH)

    info_bar.labels.variation = ""
    assert label not in info_bar.render(CANDLE_SET, WIDTH)
