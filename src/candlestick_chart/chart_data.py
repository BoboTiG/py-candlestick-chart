from os import get_terminal_size

from .candle import Candles
from .candle_set import CandleSet
from .constants import HEIGHT, MARGIN_TOP, WIDTH
from .volume_pane import VolumePane


class ChartData:
    __slots__ = (
        "height",
        "main_candle_set",
        "terminal_size",
        "visible_candle_set",
        "width",
    )

    def __init__(self, candles: Candles, width: int = 0, height: int = 0) -> None:
        self.main_candle_set = CandleSet(candles)
        self.visible_candle_set = CandleSet([])

        if not width or not height:
            width, height = get_terminal_size()
        self.set_size(width, height)

        self.compute_visible_candles()

    def compute_height(self, volume_pane: VolumePane) -> None:
        volume_pane_height = volume_pane.height if volume_pane.enabled else 0
        self.height = self.terminal_size[1] - MARGIN_TOP - HEIGHT - volume_pane_height

    def compute_visible_candles(self) -> None:
        nb_visible_candles = self.width - WIDTH
        self.visible_candle_set.set_candles(
            self.main_candle_set.candles[-nb_visible_candles:][:]
        )

    def reset_candles(self) -> None:
        self.main_candle_set.set_candles([])
        self.visible_candle_set.set_candles([])

    def add_candles(self, candles: Candles) -> None:
        self.main_candle_set.add_candles(candles)
        self.visible_candle_set.set_candles([])

    def set_size(self, width: int, height: int) -> None:
        self.terminal_size = width, height
        self.width, self.height = width, height
