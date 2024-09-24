import sys

from candlestick_chart import Chart
from candlestick_chart.utils import parse_candles_from_csv


def main() -> int:
    # Your CSV data must have "open,high,low,close" header fields.
    candles = parse_candles_from_csv("./examples/BTC-USD.csv")

    chart = Chart(candles, title="BTC/USDT")

    # Set customs colors
    chart.set_bear_color(1, 205, 254)
    chart.set_bull_color(255, 107, 153)

    chart.draw()
    return 0


if __name__ == "__main__":
    sys.exit(main())
