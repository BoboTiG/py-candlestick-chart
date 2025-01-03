from __future__ import annotations

from typing import TYPE_CHECKING

from candlestick_chart.chart_data import ChartData
from candlestick_chart.chart_renderer import ChartRenderer
from candlestick_chart.info_bar import InfoBar
from candlestick_chart.volume_pane import VolumePane
from candlestick_chart.y_axis import YAxis

if TYPE_CHECKING:
    from collections.abc import Iterable

    from rich.console import Console, ConsoleOptions

    from candlestick_chart.candle import Candles


class Chart:
    __slots__ = (
        "chart_data",
        "info_bar",
        "renderer",
        "highlights",
        "volume_pane",
        "y_axis",
    )

    def __init__(
        self,
        candles: Candles,
        *,
        title: str = "My chart",
        width: int = 0,
        height: int = 0,
        renderer_cls: type[ChartRenderer] = ChartRenderer,
    ) -> None:
        self.renderer = renderer_cls()
        self.chart_data = ChartData(candles, width=width, height=height)
        self.y_axis = YAxis(self.chart_data)
        self.info_bar = InfoBar(title)
        self.volume_pane = VolumePane(int(self.chart_data.height / 6))

        # A dict of price -> color to display custom colors on specific prices on the Y-axis
        self.highlights: dict[str, str | tuple[int, int, int]] = {}

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Iterable[str]:
        from rich.ansi import AnsiDecoder
        from rich.console import Group

        self.update_size(
            options.max_width or console.width,
            options.height or console.height,
        )
        yield Group(*AnsiDecoder().decode(self._render()))

    def _render(self) -> str:
        """Get the full chart as a single string."""
        return self.renderer.render(self)

    def draw(self) -> None:
        """Draws the chart by outputting multiples strings in the terminal."""
        print(self._render())  # noqa: T201

    def set_bear_color(self, r: int, g: int, b: int) -> None:
        """Set the color of the bearish candle.
        The default color is  (234, 74, 90).
        """
        self.renderer.bearish_color = r, g, b

    def set_bull_color(self, r: int, g: int, b: int) -> None:
        """Set the color of the bullish candle.
        The default color is  (52, 208, 88).
        """
        self.renderer.bullish_color = r, g, b

    def set_label(self, label: str, value: str) -> None:
        """Set the info bar `label` text with `value`.
        An empty string will disable its display.
        """
        setattr(self.info_bar.labels, label, value)

    def set_highlight(self, price: str, color: str | tuple[int, int, int]) -> None:
        """Set a specific `color` for `price` in the Y-axis.
        `price` must be a string to be able to compare to real values
        and because comparing floats would almost never match.
        Set `color` is an empty string, or None, to reset the color.

        Examples:
            >>> chart.set_highlight(fnum(52,348.63), "red")
            >>> chart.set_highlight(fnum(52,348.63), (255, 0, 0))
            >>> chart.set_highlight(fnum(52,348.63), "91m")
            >>> chart.set_highlight(fnum(52,348.63), "91;47m")

        """
        if color:
            self.highlights[price] = color
        else:
            self.highlights.pop(price, None)

    def set_name(self, name: str) -> None:
        """Set the name of the chart in the info bar."""
        self.info_bar.name = name

    def set_vol_bear_color(self, r: int, g: int, b: int) -> None:
        """Sets the color of the volume when the candle is bearish.
        The default color is  (234, 74, 90).
        """
        self.volume_pane.bearish_color = r, g, b

    def set_vol_bull_color(self, r: int, g: int, b: int) -> None:
        """Sets the color of the volume when the candle is bullish.
        The default color is  (52, 208, 88).
        """
        self.volume_pane.bullish_color = r, g, b

    def set_volume_pane_enabled(self, enabled: bool) -> None:  # noqa: FBT001
        """Hide or show the volume pane."""
        self.volume_pane.enabled = enabled

    def set_volume_pane_height(self, height: int) -> None:
        """Set the volume pane height.
        Default is 1/6 of the terminal height.
        """
        self.volume_pane.height = height

    def set_volume_pane_unicode_fill(self, unicode_fill: str) -> None:
        """Set the character for drawing the volume bars."""
        self.volume_pane.unicode_fill = unicode_fill

    def update_candles(self, candles: Candles, *, reset: bool = False) -> None:
        """Convenient helper to update candles."""
        if reset:
            self.chart_data.reset_candles()
        self.chart_data.add_candles(candles)
        self.chart_data.compute_visible_candles()

    def update_size(self, width: int, height: int) -> None:
        """Adapt chart width, and height. Yes, it is responsive too!"""
        if (width, height) == self.chart_data.terminal_size:
            return

        self.chart_data.set_size(width, height)
        self.chart_data.compute_visible_candles()

        if self.volume_pane.enabled:
            self.set_volume_pane_height(int(self.chart_data.height / 6))
