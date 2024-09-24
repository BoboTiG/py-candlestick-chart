import pytest

from candlestick_chart.colors import color


@pytest.mark.parametrize(
    ("custom_color", "expected"),
    [
        ("", "𓅂"),
        ("red", "\x1b[91m𓅂\x1b[00m"),
        ((255, 0, 0), "\x1b[38;2;255;0;0m𓅂\x1b[00m"),
        # ANSI color
        ("91m", "\x1b[91m𓅂\x1b[00m"),
        # ANSI color + background
        ("91;47m", "\x1b[91;47m𓅂\x1b[00m"),
    ],
)
def test_color(custom_color: str, expected: str) -> None:
    assert color("𓅂", custom_color) == expected
