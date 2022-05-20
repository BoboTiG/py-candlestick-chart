from .candle import Candles
from .chart_data import ChartData
from .chart_renderer import ChartRenderer
from .info_bar import InfoBar
from .volume_pane import VolumePane
from .y_axis import YAxis


class Chart:
    def __init__(self, candles: Candles, title: str = "My chart") -> None:
        self.renderer = ChartRenderer()
        self.chart_data = ChartData(candles)
        self.y_axis = YAxis(self.chart_data)
        self.info_bar = InfoBar(title, self.chart_data)
        self.volume_pane = VolumePane(self.chart_data, int(self.chart_data.height / 6))
        self.chart_data.compute_height(self.volume_pane)

    def draw(self) -> None:
        """Draws the chart by outputting multiples strings in the terminal."""
        self.renderer.render(self)

    def set_name(self, name: str) -> None:
        """Set the name of the chart in the info bar."""
        self.info_bar.name = name

    def set_bear_color(self, r: int, g: int, b: int) -> None:
        """Set the color of the bearish candle.
        The default color is  (234, 74, 90).
        """
        self.renderer.bearish_color = (r, g, b)

    def set_bull_color(self, r: int, g: int, b: int) -> None:
        """Set the color of the bullish candle.
        The default color is  (52, 208, 88).
        """
        self.renderer.bullish_color = (r, g, b)

    def set_vol_bear_color(self, r: int, g: int, b: int) -> None:
        """Sets the color of the volume when the candle is bearish.
        The default color is  (234, 74, 90).
        """
        self.volume_pane.bearish_color = (r, g, b)

    def set_vol_bull_color(self, r: int, g: int, b: int) -> None:
        """Sets the color of the volume when the candle is bullish.
        The default color is  (52, 208, 88).
        """
        self.volume_pane.bullish_color = (r, g, b)

    def set_volume_pane_enabled(self, enabled: bool) -> None:
        """Hide or show the volume pane."""
        self.volume_pane.enabled = enabled

    def set_volume_pane_unicode_fill(self, unicode_fill: str) -> None:
        """Set the character for drawing the volume bars."""
        self.volume_pane.unicode_fill = unicode_fill

    def set_volume_pane_height(self, height: int) -> None:
        """Set the volume pane height.
        Default is 1/6 of the terminal height.
        """
        self.volume_pane.height = height
