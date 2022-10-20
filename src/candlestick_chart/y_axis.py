import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Dict, Tuple

from . import constants
from .candle import Candle
from .colors import color
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

    def render_line(
        self, y: int, highlights: Dict[str, str | Tuple[int, int, int]] = None
    ) -> str:
        return (
            self.render_empty(y=y, highlights=highlights)
            if y % constants.Y_AXIS_SPACING
            else self._render_tick(y, highlights or {})
        )

    def _round_price(
        self,
        value: float,
        fn_down: Callable[[float], float] = math.floor,
        fn_up: Callable[[float], float] = math.ceil,
    ) -> str:
        if constants.Y_AXIS_ROUND_MULTIPLIER > 0.0:
            multiplier = constants.Y_AXIS_ROUND_MULTIPLIER
            if constants.Y_AXIS_ROUND_DIR == "down":
                value = fn_down(value * multiplier) / multiplier
            else:
                value = fn_up(value * multiplier) / multiplier
        return fnum(value)

    def _render_price(
        self, y: float, highlights: Dict[str, str | Tuple[int, int, int]]
    ) -> Tuple[bool, str]:
        chart_data = self.chart_data
        min_value = chart_data.visible_candle_set.min_price
        max_value = chart_data.visible_candle_set.max_price
        height = chart_data.height

        cell_min_length = constants.CHAR_PRECISION + constants.DEC_PRECISION + 1
        price = self._round_price(min_value + (y * (max_value - min_value) / height))
        price_upper = self._round_price(
            min_value + ((y + 1) * (max_value - min_value) / height)
        )

        has_special_price = False
        custom_color: str | Tuple[int, int, int] = ""

        for target_price, target_color in highlights.items():
            if not (price <= target_price < price_upper):
                continue
            price = target_price
            has_special_price = True
            custom_color = target_color
            break

        price = (
            f" {color(f'├ {price:<{cell_min_length}}', custom_color)}"
            if constants.Y_AXIS_ON_THE_RIGHT
            else f"{color(f'{price:<{cell_min_length}} ┤', custom_color)}{' ' * constants.MARGIN_RIGHT}"
        )

        return has_special_price, price

    def render_empty(
        self, y: float = None, highlights: Dict[str, str | Tuple[int, int, int]] = None
    ) -> str:
        if highlights and y:
            has_special_price, price = self._render_price(y, highlights)
            if has_special_price:
                return price

        if constants.Y_AXIS_ON_THE_RIGHT:
            return " │"

        cell = " " * (constants.CHAR_PRECISION + constants.DEC_PRECISION + 2)
        margin = " " * (constants.MARGIN_RIGHT + 1)
        return f"{cell}│{margin}"

    def _render_tick(
        self, y: int, highlights: Dict[str, str | Tuple[int, int, int]]
    ) -> str:
        _, price = self._render_price(y, highlights)
        return price
