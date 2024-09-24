import sys
from dataclasses import dataclass

from candlestick_chart import Candle, Chart


@dataclass(frozen=True, slots=True)
class BinanceKlinesItem:
    open_time: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    close_time: int
    quote_asset_volume: str
    number_of_trades: int
    taker_buy_base_asset_volume: str
    taker_buy_quote_asset_volume: str
    ignore: str


def main() -> int:
    import requests

    url = "https://api.binance.com/api/v1/klines?symbol=CHZUSDT&interval=1h"
    with requests.get(url, timeout=60) as req:
        klines = [BinanceKlinesItem(*item) for item in req.json()]

    candles = [
        Candle(
            open=float(kline.open),
            close=float(kline.close),
            high=float(kline.high),
            low=float(kline.low),
            volume=float(kline.volume),
            timestamp=float(kline.open_time),
        )
        for kline in klines
    ]

    chart = Chart(candles, title="CHZ/USDT")

    chart.set_bull_color(1, 205, 254)
    chart.set_bear_color(255, 107, 153)
    chart.set_volume_pane_height(4)
    chart.set_volume_pane_enabled(True)
    chart.set_highlight("0.2377", "93;45m")

    chart.draw()
    return 0


if __name__ == "__main__":
    sys.exit(main())
