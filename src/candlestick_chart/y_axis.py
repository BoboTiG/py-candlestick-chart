from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from candlestick_chart import constants
from candlestick_chart.colors import color
from candlestick_chart.utils import round_price

if TYPE_CHECKING:
    from candlestick_chart.candle import Candle
    from candlestick_chart.chart_data import ChartData


@dataclass(slots=True)
class YAxis:
    chart_data: ChartData

    def price_to_heights(self, candle: Candle) -> tuple[float, ...]:
        chart_data = self.chart_data
        height = chart_data.height
        candle_set = chart_data.visible_candle_set

        # sourcery skip: min-max-identity
        min_open = min(candle.close, candle.open)
        max_open = max(candle.close, candle.open)
        min_value = candle_set.min_price
        diff = (candle_set.max_price - min_value) or 1

        return (
            (candle.high - min_value) / diff * height,  # high_y
            (candle.low - min_value) / diff * height,  # low_y
            (max_open - min_value) / diff * height,  # max_y
            (min_open - min_value) / diff * height,  # min_y
        )

    def render_line(self, y: int, *, highlights: dict[str, str | tuple[int, int, int]] | None = None) -> str:
        return (
            self.render_empty(y=y, highlights=highlights)
            if y % constants.Y_AXIS_SPACING
            else self._render_tick(y, highlights or {})
        )

    def _render_price(self, y: float, highlights: dict[str, str | tuple[int, int, int]]) -> tuple[bool, str]:
        chart_data = self.chart_data
        min_value = chart_data.visible_candle_set.min_price
        max_value = chart_data.visible_candle_set.max_price
        height = chart_data.height

        cell_min_length = constants.CHAR_PRECISION + constants.DEC_PRECISION + 1
        price = round_price(min_value + (y * (max_value - min_value) / height))
        price_upper = round_price(min_value + ((y + 1) * (max_value - min_value) / height))

        has_special_price = False
        custom_color: str | tuple[int, int, int] = ""

        for target_price, target_color in highlights.items():
            if not (price <= target_price < price_upper):
                continue
            price = target_price
            has_special_price = True
            custom_color = target_color
            break

        price = (
            f" {color(f'{constants.UNICODE_Y_AXIS_RIGHT} {price:<{cell_min_length}}', custom_color)}"
            if constants.Y_AXIS_ON_THE_RIGHT
            else (
                f"{color(f'{price:<{cell_min_length}} {constants.UNICODE_Y_AXIS_LEFT}', custom_color)}"
                f"{' ' * constants.MARGIN_RIGHT}"
            )
        )

        return has_special_price, price

    def render_empty(
        self,
        *,
        y: float | None = None,
        highlights: dict[str, str | tuple[int, int, int]] | None = None,
    ) -> str:
        if highlights and y:
            has_special_price, price = self._render_price(y, highlights)
            if has_special_price:
                return price

        if constants.Y_AXIS_ON_THE_RIGHT:
            return f" {constants.UNICODE_Y_AXIS}"

        cell = " " * (constants.CHAR_PRECISION + constants.DEC_PRECISION + 2)
        margin = " " * constants.MARGIN_RIGHT
        return f"{cell}{constants.UNICODE_Y_AXIS}{margin}"

    def _render_tick(self, y: int, highlights: dict[str, str | tuple[int, int, int]]) -> str:
        _, price = self._render_price(y, highlights)
        return price
