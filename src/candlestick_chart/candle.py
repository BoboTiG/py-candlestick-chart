from typing import Any, List, NamedTuple


class CandleType(NamedTuple):
    bearish: int = 0
    bullish: int = 1


class Candle:
    __slots__ = ("open", "close", "high", "low", "volume", "timestamp", "type")

    def __init__(self, **kwargs: Any) -> None:
        self.open = float(kwargs["open"])
        self.high = float(kwargs["high"])
        self.low = float(kwargs["low"])
        self.close = float(kwargs["close"])
        self.volume = float(kwargs.get("volume", 0.0))
        self.timestamp = float(kwargs.get("timestamp", 0.0))
        self.type = CandleType.bullish if self.open < self.close else CandleType.bearish


Candles = List[Candle]
