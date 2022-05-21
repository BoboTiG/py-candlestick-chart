from time import sleep

from candlestick_chart.chart import Chart
from candlestick_chart.utils import parse_candles_from_csv
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="candlesticks", size=120),
        Layout(name="main_right"),
    )
    return layout


candles = parse_candles_from_csv("./examples/BTC-USD.csv")
chart = Chart(candles, title="Rich candlesticks!")
chart.set_bear_color(1, 205, 254)
chart.set_bull_color(255, 107, 153)
chart.set_label("average", "")
chart.set_label("volume", "")

layout = make_layout()
layout["candlesticks"].update(Panel(chart))

with Live(layout):
    while True:
        sleep(0.1)
