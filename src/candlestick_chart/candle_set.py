from dataclasses import dataclass

from .candle import Candles


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

        self.cumulative_volume = sum(candle.volume for candle in self.candles)
        self.last_price = self.candles[-1].close

        open_value = self.candles[0].open
        close_value = self.candles[-1].close
        self.variation = ((close_value - open_value) / open_value) * 100.0

        self.average = sum(candle.close for candle in self.candles) / len(self.candles)

        self.max_price = max(self.candles, key=lambda c: c.high).high
        self.min_price = min(self.candles, key=lambda c: c.low).low
        self.max_volume = max(self.candles, key=lambda c: c.volume).volume
        self.min_volume = min(self.candles, key=lambda c: c.volume).volume
