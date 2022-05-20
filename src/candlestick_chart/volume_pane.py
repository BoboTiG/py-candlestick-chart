from dataclasses import dataclass, field
from math import ceil
from typing import TYPE_CHECKING

from .candle import Candle, CandleType
from .colors import truecolor
from .constants import UNICODE_FILL, UNICODE_HALF_BODY_BOTTOM

if TYPE_CHECKING:
    from .chart_data import ChartData


@dataclass
class VolumePane:
    chart_data: "ChartData"
    height: int
    enabled: bool = field(init=False)
    bearish_color = (52, 208, 88)
    bullish_color = (234, 74, 90)
    unicode_fill: str = UNICODE_FILL

    def __post_init__(self) -> None:
        self.enabled = any(c.volume for c in self.chart_data.visible_candle_set.candles)

    def colorize(self, candle_type: int, string: str) -> str:
        color = (
            self.bearish_color
            if candle_type == CandleType.bearish
            else self.bullish_color
        )
        return truecolor(string, *color)

    def render(self, candle: Candle, y: int) -> str:
        max_volume = self.chart_data.visible_candle_set.max_volume
        volume = candle.volume

        volume_percent_of_max = volume / max_volume
        ratio = volume_percent_of_max * self.height

        if y < ceil(ratio):
            return self.colorize(candle.get_type(), self.unicode_fill)

        if y == 1 and self.unicode_fill == UNICODE_FILL:
            return self.colorize(candle.get_type(), UNICODE_HALF_BODY_BOTTOM)

        return " "
