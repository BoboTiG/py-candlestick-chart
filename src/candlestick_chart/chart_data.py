from os import get_terminal_size

from . import chart_renderer, info_bar, y_axis
from .candle import Candles
from .candle_set import CandleSet
from .volume_pane import VolumePane


class ChartData:
    def __init__(self, candles: Candles) -> None:
        self.width, self.height = get_terminal_size()
        self.terminal_size = self.width, self.height

        self.main_candle_set = CandleSet(candles)
        self.visible_candle_set = CandleSet([])

        self.compute_visible_candles()

    def compute_height(self, volume_pane: VolumePane) -> None:
        volume_pane_height = volume_pane.height if volume_pane.enabled else 0
        self.height = (
            self.terminal_size[1]
            - chart_renderer.MARGIN_TOP
            - info_bar.HEIGHT
            - volume_pane_height
        )

    def compute_visible_candles(self) -> None:
        nb_visible_candles = self.width - y_axis.WIDTH
        self.visible_candle_set.set_candles(
            self.main_candle_set.candles[:nb_visible_candles]
        )
