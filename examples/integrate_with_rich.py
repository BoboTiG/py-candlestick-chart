from time import sleep

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel

from candlestick_chart.candle import Candles
from candlestick_chart.chart import Chart
from candlestick_chart.utils import fnum, parse_candles_from_csv


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="candlesticks-static"),
        Layout(name="candlesticks-dynamic"),
    )
    return layout


def make_chart(candles: Candles, nature: str) -> Chart:
    chart = Chart(candles, title=f"Rich candlesticks {nature}!")
    chart.set_bear_color(255, 107, 153)
    chart.set_bull_color(1, 205, 254)
    chart.set_label("average", "")
    chart.set_label("volume", "")
    chart.set_highlight(fnum(53730.68), "red")
    return chart


candles = parse_candles_from_csv("./examples/BTC-USD.csv")
chart_static = make_chart(candles, "static")
chart_dynamic = make_chart([], "dynamic")

layout = make_layout()
layout["candlesticks-static"].update(Panel(chart_static))
layout["candlesticks-dynamic"].update(Panel(chart_dynamic))

use_reset = False

with Live(layout, refresh_per_second=120):
    if use_reset:
        candles_count = 0
        while candles_count <= len(candles):
            chart_dynamic.update_candles(candles[:candles_count], reset=True)
            candles_count += 1
            sleep(0.03)
    else:
        for candle in candles:
            chart_dynamic.update_candles([candle])
            sleep(0.03)
