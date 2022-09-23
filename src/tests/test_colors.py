import pytest

from candlestick_chart.colors import color


@pytest.mark.parametrize(
    "custom_color, expected",
    [
        ("red", "\x1b[91m𓅂\x1b[00m"),
        ((255, 0, 0), "\x1b[38;2;255;0;0m𓅂\x1b[00m"),
        # ANSI color
        ("91m", "\x1b[91m𓅂\x1b[00m"),
        # ANSI color + backgound
        ("91;47m", "\x1b[91;47m𓅂\x1b[00m"),
    ],
)
def test_color(custom_color, expected):
    assert color("𓅂", custom_color) == expected
