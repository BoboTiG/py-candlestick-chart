from dataclasses import dataclass
from typing import TYPE_CHECKING, Tuple

from . import constants
from .candle import Candle
from .utils import fnum

if TYPE_CHECKING:
    from .chart_data import ChartData


@dataclass(slots=True)
class YAxis:
    chart_data: "ChartData"

    def price_to_heights(self, candle: Candle) -> Tuple[float, ...]:
        chart_data = self.chart_data
        height = chart_data.height
        candle_set = chart_data.visible_candle_set

        min_open = candle.open if candle.open < candle.close else candle.close
        max_open = candle.open if candle.open > candle.close else candle.close
        min_value = candle_set.min_price
        diff = (candle_set.max_price - min_value) or 1

        return (
            (candle.high - min_value) / diff * height,  # high_y
            (candle.low - min_value) / diff * height,  # low_y
            (max_open - min_value) / diff * height,  # max_y
            (min_open - min_value) / diff * height,  # min_y
        )

    def render_line(self, y: int) -> str:
        return (
            self.render_empty()
            if y % constants.Y_AXIS_SPACING
            else self._render_tick(y)
        )

    def render_empty(self) -> str:
        if constants.Y_AXIS_ON_THE_RIGHT:
            return " │"

        cell = " " * (constants.CHAR_PRECISION + constants.DEC_PRECISION + 2)
        margin = " " * (constants.MARGIN_RIGHT + 1)
        return f"{cell}│{margin}"

    def _render_tick(self, y: int) -> str:
        chart_data = self.chart_data
        min_value = chart_data.visible_candle_set.min_price
        max_value = chart_data.visible_candle_set.max_price
        height = chart_data.height

        price = min_value + (y * (max_value - min_value) / height)
        cell_min_length = constants.CHAR_PRECISION + constants.DEC_PRECISION + 1
        return (
            f" │― {fnum(price):<{cell_min_length}}"
            if constants.Y_AXIS_ON_THE_RIGHT
            else f"{fnum(price):<{cell_min_length}} │―{'M' * constants.MARGIN_RIGHT}"
        )
