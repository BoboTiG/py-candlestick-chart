from dataclasses import dataclass
from math import ceil, floor
from typing import TYPE_CHECKING, List, Tuple

from .candle import CandleType, Candle
from .colors import truecolor
from .constants import (
    UNICODE_VOID,
    UNICODE_BODY,
    UNICODE_HALF_BODY_BOTTOM,
    UNICODE_HALF_BODY_TOP,
    UNICODE_WICK,
    UNICODE_TOP,
    UNICODE_BOTTOM,
    UNICODE_WICK_UPPER,
    UNICODE_WICK_LOWER,
)
from .y_axis import YAxis

if TYPE_CHECKING:
    from .chart import Chart


@dataclass(slots=True)
class ChartRenderer:
    bearish_color: Tuple[int, int, int] = (234, 74, 90)
    bullish_color: Tuple[int, int, int] = (52, 208, 88)

    def _colorize(self, candle_type: int, string: str) -> str:
        color = (
            self.bearish_color
            if candle_type == CandleType.bearish
            else self.bullish_color
        )
        return truecolor(string, *color)

    def _render_candle(self, candle: Candle, y: int, y_axis: YAxis) -> str:
        height_unit = float(y)
        high_y, low_y, max_y, min_y = y_axis.price_to_heights(candle)
        output = UNICODE_VOID

        ceil_ = ceil
        floor_ = floor

        if ceil_(high_y) >= height_unit >= floor_(max_y):
            max_diff = max_y - height_unit
            high_diff = high_y - height_unit
            if max_diff > 0.75:
                output = UNICODE_BODY
            elif max_diff > 0.25:
                output = UNICODE_TOP if high_diff > 0.75 else UNICODE_HALF_BODY_BOTTOM
            elif high_diff > 0.75:
                output = UNICODE_WICK
            elif high_diff > 0.25:
                output = UNICODE_WICK_UPPER
        elif ceil_(min_y) >= height_unit >= floor_(low_y):
            min_diff = min_y - height_unit
            low_diff = low_y - height_unit
            if min_diff < 0.25:
                output = UNICODE_BODY
            elif min_diff < 0.75:
                output = UNICODE_BOTTOM if low_diff < 0.25 else UNICODE_HALF_BODY_TOP
            elif low_diff < 0.25:
                output = UNICODE_WICK
            elif low_diff < 0.75:
                output = UNICODE_WICK_LOWER
        elif max_y >= height_unit >= ceil_(min_y):
            output = UNICODE_BODY

        return self._colorize(candle.type, output)

    def render(self, chart: "Chart") -> str:
        output: List[str] = []
        chart_data = chart.chart_data
        chart_data.compute_height(chart.volume_pane)
        candle_set = chart_data.visible_candle_set
        candles = candle_set.candles

        render_line = chart.y_axis.render_line
        for y in range(chart_data.height, 0, -1):
            output.extend(("\n", render_line(y)))
            output.extend(
                self._render_candle(candle, y, chart.y_axis) for candle in candles
            )

        if chart.volume_pane.enabled and candle_set.max_volume:
            render_empty = chart.y_axis.render_empty
            render = chart.volume_pane.render
            max_volume = candle_set.max_volume
            for y in range(chart.volume_pane.height, 0, -1):
                output.extend(("\n", render_empty()))
                output.extend(render(candle, y, max_volume) for candle in candles)

        output.append(
            chart.info_bar.render(chart_data.main_candle_set, chart_data.width)
        )
        return "".join(output)
