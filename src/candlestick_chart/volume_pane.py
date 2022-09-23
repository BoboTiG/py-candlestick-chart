from dataclasses import dataclass
from math import ceil
from typing import Tuple

from . import constants
from .candle import Candle, CandleType
from .colors import truecolor


@dataclass(slots=True)
class VolumePane:
    height: int
    enabled: bool = True
    bearish_color: Tuple[int, int, int] = (234, 74, 90)
    bullish_color: Tuple[int, int, int] = (52, 208, 88)
    unicode_fill: str = constants.UNICODE_FILL

    def _colorize(self, candle_type: int, string: str) -> str:
        color = (
            self.bearish_color
            if candle_type == CandleType.bearish
            else self.bullish_color
        )
        return truecolor(string, *color)

    def render(self, candle: Candle, y: int, max_volume: float) -> str:
        volume_percent_of_max = candle.volume / (max_volume or 1)
        ratio = volume_percent_of_max * self.height

        if y < ceil(ratio):
            return self._colorize(candle.type, self.unicode_fill)

        if y == 1 and self.unicode_fill == constants.UNICODE_FILL:
            return self._colorize(candle.type, constants.UNICODE_HALF_BODY_BOTTOM)

        return " "
