import sys

from candlestick_chart import Chart
from candlestick_chart.utils import fnum, parse_candles_from_json


def main() -> int:
    # Your JSON data must have "open,high,low,close" header fields.
    candles = parse_candles_from_json("./examples/BTC-chart.json")

    chart = Chart(candles, title="My BTC Chart")

    # Set customs colors
    chart.set_bear_color(1, 205, 254)
    chart.set_bull_color(255, 107, 153)
    chart.set_highlight(fnum(30544.20), (0, 0, 255))

    chart.draw()
    return 0


if __name__ == "__main__":
    sys.exit(main())
