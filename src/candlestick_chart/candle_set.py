from dataclasses import dataclass

from .candle import Candles


@dataclass
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

    def __post__init__(self, candles: Candles) -> None:
        self.set_candles(candles)

    def set_candles(self, candles: Candles) -> None:
        self.candles = candles
        if not self.candles:
            return

        self.compute_min_and_max_values()
        self.compute_variation()
        self.compute_average()
        self.compute_last_price()
        self.compute_cumulative_volume()

    def compute_cumulative_volume(self) -> None:
        self.cumulative_volume = sum(candle.volume for candle in self.candles)

    def compute_last_price(self) -> None:
        self.last_price = self.candles[-1].close

    def compute_variation(self) -> None:
        open_value = self.candles[0].open
        close_value = self.candles[-1].close
        self.variation = ((close_value - open_value) / open_value) * 100.0

    def compute_average(self) -> None:
        self.average = sum(candle.close for candle in self.candles) / len(self.candles)

    def compute_min_and_max_values(self) -> None:
        self.max_price = max(self.candles, key=lambda c: c.high).high
        self.min_price = min(self.candles, key=lambda c: c.low).low
        self.max_volume = max(self.candles, key=lambda c: c.volume).volume
        self.min_volume = min(self.candles, key=lambda c: c.volume).volume
