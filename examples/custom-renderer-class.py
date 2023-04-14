import sys
from dataclasses import dataclass
from math import floor

from candlestick_chart import Candle, Chart, constants
from candlestick_chart.chart_renderer import ChartRenderer
from candlestick_chart.colors import truecolor
from candlestick_chart.utils import parse_candles_from_csv
from candlestick_chart.y_axis import YAxis


@dataclass
class MyChartRendered(ChartRenderer):
    def _render_candle(self, candle: Candle, y: int, y_axis: YAxis) -> str:
        height_unit = float(y)
        *_, max_y, min_y = y_axis.price_to_heights(candle)
        return (
            truecolor("•", *self.bullish_color)
            if max_y > height_unit > floor(min_y)
            else truecolor(constants.UNICODE_WICK, *self.bearish_color)
            if floor(max_y) > height_unit
            else constants.UNICODE_VOID
        )


def main() -> int:
    # Your CSV data must have "open,high,low,close" header fields.
    candles = parse_candles_from_csv("./examples/BTC-USD.csv")

    chart = Chart(candles, title="BTC/USDT", renderer_cls=MyChartRendered)
    chart.set_volume_pane_enabled(False)

    # Set customs colors
    chart.set_bear_color(1, 205, 254)
    chart.set_bull_color(255, 107, 153)

    chart.draw()
    return 0


if __name__ == "__main__":
    sys.exit(main())
