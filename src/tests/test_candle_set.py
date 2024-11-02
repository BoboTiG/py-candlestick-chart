from pathlib import Path

from candlestick_chart.candle_set import CandleSet
from candlestick_chart.utils import parse_candles_from_csv

EXAMPLES = Path(__file__).parent.parent.parent / "examples"


def test_compute_all() -> None:
    candles = parse_candles_from_csv(EXAMPLES / "BTC-USD.csv")
    candle_set = CandleSet(candles)

    assert candle_set.candles == candles
    assert candle_set.min_price == 28_722.755859
    assert candle_set.max_price == 67_673.742188
    assert candle_set.min_volume == 18_787_986_667.0
    assert candle_set.max_volume == 350_967_941_479.0
    assert candle_set.variation == 133.037_198_615_531_42
    assert candle_set.average == 46_375.191_043_259_58
    assert candle_set.last_price == 67_566.828_125
    assert candle_set.cumulative_volume == 15_472_149_666_480.0
