from dataclasses import dataclass
from typing import TYPE_CHECKING

from . import y_axis
from .colors import bold, green, red, yellow
from .utils import fnum

if TYPE_CHECKING:
    from .chart_data import ChartData


HEIGHT: int = 2


@dataclass
class InfoBar:
    name: str
    chart_data: "ChartData"

    def render(self) -> str:
        candle_set = self.chart_data.visible_candle_set

        avg_color = (
            red
            if candle_set.last_price > candle_set.average
            else green
            if candle_set.last_price < candle_set.average
            else yellow
        )
        avg = avg_color(fnum(candle_set.last_price))

        variation_output = ("↖", green) if candle_set.variation > 0.0 else ("↙", red)

        high = green(fnum(candle_set.max_price))
        low = red(fnum(candle_set.min_price))
        var = variation_output[1](
            f"{variation_output[0]} {candle_set.variation:>+.2f}%"
        )
        price = bold(green(fnum(candle_set.last_price)))
        vol = green(fnum(int(candle_set.cumulative_volume)))

        return "".join(
            (
                "\n",
                "─" * (len(candle_set.candles) + y_axis.WIDTH),
                "\n",
                f"{self.name:>{y_axis.WIDTH + 3}}"
                f" | Price: {price}"
                f" | Highest: {high}"
                f" | Lowest: {low}"
                f" | Var.: {var}"
                f" | Avg.: {avg}"
                f" │ Cum. Vol: {vol}",
                "\n",
            )
        )
