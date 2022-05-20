from dataclasses import dataclass
from enum import IntEnum
from typing import List


class CandleType(IntEnum):
    BEARISH = 0
    BULLISH = 1


@dataclass(slots=True)
class Candle:
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0
    timestamp: float = 0.0

    def __post_init__(self) -> None:
        self.open = float(self.open)
        self.high = float(self.high)
        self.low = float(self.low)
        self.close = float(self.close)
        self.volume = float(self.volume)
        self.timestamp = float(self.timestamp)

    def get_type(self) -> CandleType:
        return CandleType.BULLISH if self.open < self.close else CandleType.BEARISH


Candles = List[Candle]
