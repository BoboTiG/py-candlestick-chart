from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from candlestick_chart import constants
from candlestick_chart.colors import bold, green, red, yellow
from candlestick_chart.utils import fnum

if TYPE_CHECKING:
    from types import SimpleNamespace

    from candlestick_chart.candle_set import CandleSet


def _get_labels() -> SimpleNamespace:
    return copy(constants.LABELS)


@dataclass(slots=True)
class InfoBar:
    name: str
    labels: SimpleNamespace = field(init=False, default_factory=_get_labels)

    def _render_average(self, candle_set: CandleSet) -> str:
        if not self.labels.average:
            return ""

        color = (
            red
            if candle_set.last_price > candle_set.average
            else green
            if candle_set.last_price < candle_set.average
            else yellow
        )
        return f"{self.labels.average}: {color(fnum(candle_set.last_price))}"

    def _render_highest(self, candle_set: CandleSet) -> str:
        return f"{self.labels.highest}: {green(fnum(candle_set.max_price))}" if self.labels.highest else ""

    def _render_lowest(self, candle_set: CandleSet) -> str:
        return f"{self.labels.lowest}: {red(fnum(candle_set.min_price))}" if self.labels.lowest else ""

    def _render_price(self, candle_set: CandleSet) -> str:
        price = f"{self.labels.price}: {bold(green(fnum(candle_set.last_price)))}"
        if self.labels.currency:
            price += f" {self.labels.currency}"
        return price

    def _render_variation(self, candle_set: CandleSet) -> str:
        if not self.labels.variation:
            return ""

        variation_output = ("↖", green) if candle_set.variation > 0.0 else ("↙", red)
        var = variation_output[1](f"{variation_output[0]} {candle_set.variation:>+.2f}%")
        return f"{self.labels.variation}: {var}"

    def _render_volume(self, candle_set: CandleSet) -> str:
        return f"{self.labels.volume}: {green(fnum(int(candle_set.cumulative_volume)))}" if self.labels.volume else ""

    def render(self, candle_set: CandleSet, available_width: int) -> str:
        return "".join(
            (
                "\n",
                "─" * available_width,
                "\n",
                " | ".join(
                    filter(
                        len,
                        (
                            self.name,
                            self._render_price(candle_set),
                            self._render_highest(candle_set),
                            self._render_lowest(candle_set),
                            self._render_variation(candle_set),
                            self._render_average(candle_set),
                            self._render_volume(candle_set),
                        ),
                    ),
                ),
                "\n",
            ),
        )
