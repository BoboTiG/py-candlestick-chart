from time import sleep

from candlestick_chart.chart import Chart
from candlestick_chart.utils import parse_candles_from_csv
from rich.ansi import AnsiDecoder
from rich.console import Console, ConsoleOptions, Group
from rich.jupyter import JupyterMixin
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel


def make_plot(width: int, height: int) -> str:
    candles = parse_candles_from_csv("./examples/BTC-USD.csv")
    chart = Chart(candles, title="Rich candlesticks!", width=width, height=height)

    chart.set_bear_color(1, 205, 254)
    chart.set_bull_color(255, 107, 153)
    chart.set_label("average", "")
    chart.set_label("volume", "")

    return chart.render()


class candlesticksMixin(JupyterMixin):
    def __init__(self) -> None:
        self.decoder = AnsiDecoder()

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Group:
        width = options.max_width or console.width
        height = options.height or console.height
        canvas = make_plot(width, height)
        yield Group(*self.decoder.decode(canvas))


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


layout = make_layout()
layout["candlesticks"].update(Panel(candlesticksMixin()))

with Live(layout):
    while True:
        sleep(0.1)
