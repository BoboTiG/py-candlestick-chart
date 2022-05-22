from copy import copy
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .colors import bold, green, red, yellow
from .constants import LABELS, WIDTH
from .utils import fnum

if TYPE_CHECKING:
    from .candle_set import CandleSet


@dataclass(slots=True)
class InfoBar:
    name: str
    labels = copy(LABELS)

    def _render_average(self, candle_set: "CandleSet") -> str:
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

    def _render_highest(self, candle_set: "CandleSet") -> str:
        return (
            f"{self.labels.highest}: {green(fnum(candle_set.max_price))}"
            if self.labels.highest
            else ""
        )

    def _render_lowest(self, candle_set: "CandleSet") -> str:
        return (
            f"{self.labels.lowest}: {red(fnum(candle_set.min_price))}"
            if self.labels.lowest
            else ""
        )

    def _render_price(self, candle_set: "CandleSet") -> str:
        price = f"{self.labels.price}: {bold(green(fnum(candle_set.last_price)))}"
        if self.labels.currency:
            price += f" {self.labels.currency}"
        return price

    def _render_variation(self, candle_set: "CandleSet") -> str:
        if not self.labels.variation:
            return ""

        variation_output = ("↖", green) if candle_set.variation > 0.0 else ("↙", red)
        var = variation_output[1](
            f"{variation_output[0]} {candle_set.variation:>+.2f}%"
        )
        return f"{self.labels.variation}: {var}"

    def _render_volume(self, candle_set: "CandleSet") -> str:
        return (
            f"{self.labels.volume}: {green(fnum(int(candle_set.cumulative_volume)))}"
            if self.labels.volume
            else ""
        )

    def render(self, candle_set: "CandleSet", available_width: int) -> str:
        return "".join(
            (
                "\n",
                "─" * available_width,
                "\n",
                " | ".join(
                    filter(
                        len,
                        (
                            f"{self.name:>{WIDTH + 3}}",
                            self._render_price(candle_set),
                            self._render_highest(candle_set),
                            self._render_lowest(candle_set),
                            self._render_variation(candle_set),
                            self._render_average(candle_set),
                            self._render_volume(candle_set),
                        ),
                    )
                ),
                "\n",
            )
        )
