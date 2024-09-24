from typing import NamedTuple


class CandleType(NamedTuple):
    bearish: int = 0
    bullish: int = 1


class Candle:
    __slots__ = ("open", "close", "high", "low", "volume", "timestamp", "type")

    def __init__(self, **kwargs: float) -> None:
        self.open = float(kwargs["open"])
        self.high = float(kwargs["high"])
        self.low = float(kwargs["low"])
        self.close = float(kwargs["close"])
        self.volume = float(kwargs.get("volume", 0.0))
        self.timestamp = float(kwargs.get("timestamp", 0.0))
        self.type = CandleType.bullish if self.open < self.close else CandleType.bearish

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Candle):
            raise NotImplementedError

        return (
            self.open == other.open
            and self.high == other.high
            and self.low == other.low
            and self.close == other.close
            and self.volume == other.volume
            and self.timestamp == other.timestamp
            and self.type == other.type
        )

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


Candles = list[Candle]
