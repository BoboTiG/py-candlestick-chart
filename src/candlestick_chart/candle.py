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

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}<"
            f"open={self.open}, "
            f"low={self.low}, "
            f"high={self.high}, "
            f"close={self.close}, "
            f"volume={self.volume}, "
            f"timestamp={self.timestamp}, "
            f"type={'bullish' if self.type == CandleType.bullish else 'bearish'}"
            ">"
        )


Candles = List[Candle]
