from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from candlestick_chart.candle import Candles


@dataclass(slots=True)
class CandleSet:
    candles: Candles
    min_price: float = 0.0
    max_price: float = 0.0
    min_volume: float = 0.0
    max_volume: float = 0.0
    variation: float = 0.0
    average: float = 0.0
    last_price: float = 0.0
    cumulative_volume: float = 0.0

    def __post_init__(self) -> None:
        self._compute_all()

    def add_candles(self, candles: Candles) -> None:
        self.candles.extend(candles)
        self._compute_all()

    def set_candles(self, candles: Candles) -> None:
        self.candles = candles
        self._compute_all()

    def _compute_all(self) -> None:
        if not self.candles:
            return

        candles = self.candles

        open_value = candles[0].open
        self.last_price = close_value = candles[-1].close
        self.variation = ((close_value - open_value) / open_value) * 100.0

        cumulative_volume = 0.0
        average = 0.0
        max_price = 0.0
        min_price = float("inf")
        max_volume = 0.0
        min_volume = float("inf")

        for candle in candles:
            volume = candle.volume
            cumulative_volume += volume
            average += candle.close
            max_price = max(candle.high, max_price)
            min_price = min(candle.low, min_price)
            if volume > max_volume:
                max_volume = volume
            elif volume < min_volume:
                min_volume = volume

        self.cumulative_volume = cumulative_volume
        self.average = average / len(candles)
        self.max_price = max_price
        self.min_price = min_price
        self.max_volume = max_volume
        self.min_volume = min_volume
