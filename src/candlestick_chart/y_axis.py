from dataclasses import dataclass
from typing import TYPE_CHECKING

from .constants import CHAR_PRECISION, DEC_PRECISION, MARGIN_RIGHT
from .utils import fnum

if TYPE_CHECKING:
    from .chart_data import ChartData


@dataclass
class YAxis:
    chart_data: "ChartData"

    def price_to_height(self, price: float) -> float:
        chart_data = self.chart_data
        height = chart_data.height

        min_value = chart_data.visible_candle_set.min_price
        max_value = chart_data.visible_candle_set.max_price
        return (price - min_value) / (max_value - min_value) * height

    def render_line(self, y: int) -> str:
        return self.render_empty() if y % 4 else self.render_tick(y)

    def render_tick(self, y: int) -> str:
        chart_data = self.chart_data
        min_value = chart_data.visible_candle_set.min_price
        max_value = chart_data.visible_candle_set.max_price
        height = chart_data.height

        price = min_value + (y * (max_value - min_value) / height)
        cell_min_length = CHAR_PRECISION + DEC_PRECISION + 1
        return f"{fnum(price):<{cell_min_length}} │┈{' ' * MARGIN_RIGHT}"

    def render_empty(self) -> str:
        cell = " " * (CHAR_PRECISION + DEC_PRECISION + 2)
        margin = " " * (MARGIN_RIGHT + 1)
        return f"{cell}│{margin}"
