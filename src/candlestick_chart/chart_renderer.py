from math import ceil, floor
from typing import TYPE_CHECKING, List

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


class ChartRenderer:
    def __init__(self) -> None:
        self.bearish_color = (234, 74, 90)
        self.bullish_color = (52, 208, 88)

    def colorize(self, candle_type: int, string: str) -> str:
        color = (
            self.bearish_color
            if candle_type == CandleType.bearish
            else self.bullish_color
        )
        return truecolor(string, *color)

    def render_candle(self, candle: Candle, y: int, y_axis: YAxis) -> str:
        height_unit = float(y)
        high_y = y_axis.price_to_height(candle.high)
        low_y = y_axis.price_to_height(candle.low)
        max_y = y_axis.price_to_height(max(candle.open, candle.close))
        min_y = y_axis.price_to_height(min(candle.open, candle.close))

        output = UNICODE_VOID

        if ceil(high_y) >= height_unit >= floor(max_y):
            if max_y - height_unit > 0.75:
                output = UNICODE_BODY
            elif max_y - height_unit > 0.25:
                if high_y - height_unit > 0.75:
                    output = UNICODE_TOP
                else:
                    output = UNICODE_HALF_BODY_BOTTOM
            elif high_y - height_unit > 0.75:
                output = UNICODE_WICK
            elif high_y - height_unit > 0.25:
                output = UNICODE_WICK_UPPER
        elif float(max_y) >= height_unit >= ceil(min_y):
            output = UNICODE_BODY
        elif ceil(min_y) >= height_unit >= floor(low_y):
            if min_y - height_unit < 0.25:
                output = UNICODE_BODY
            elif min_y - height_unit < 0.75:
                if low_y - height_unit < 0.25:
                    output = UNICODE_BOTTOM
                else:
                    output = UNICODE_HALF_BODY_TOP
            elif low_y - height_unit < 0.25:
                output = UNICODE_WICK
            elif low_y - height_unit < 0.75:
                output = UNICODE_WICK_LOWER

        return self.colorize(candle.get_type(), output)

    def render(self, chart: "Chart") -> str:
        output: List[str] = []
        chart_data = chart.chart_data
        chart_data.compute_height(chart.volume_pane)

        for y in range(chart_data.height, 0, -1):
            output.extend(("\n", chart.y_axis.render_line(y)))
            output.extend(
                self.render_candle(candle, y, chart.y_axis)
                for candle in chart_data.visible_candle_set.candles
            )

        if chart.volume_pane.enabled:
            for y in range(chart.volume_pane.height, 0, -1):
                output.extend(("\n", chart.y_axis.render_empty()))
                output.extend(
                    chart.volume_pane.render(candle, y)
                    for candle in chart_data.visible_candle_set.candles
                )

        output.append(chart.info_bar.render())
        return "".join(output)
