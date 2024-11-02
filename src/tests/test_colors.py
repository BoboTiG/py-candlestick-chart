import pytest

from candlestick_chart import colors


@pytest.mark.parametrize(
    ("custom_color", "expected"),
    [
        ("", "𓅂"),
        ("green", "\x1b[92m𓅂\x1b[00m"),
        ((0, 255, 0), "\x1b[38;2;0;255;0m𓅂\x1b[00m"),
        # ANSI color
        ("92m", "\x1b[92m𓅂\x1b[00m"),
        # ANSI color + background
        ("92;47m", "\x1b[92;47m𓅂\x1b[00m"),
    ],
)
def test_color(custom_color: str, expected: str) -> None:
    assert colors.color("𓅂", custom_color) == expected


@pytest.mark.parametrize(
    ("color_name", "expected"),
    [
        ("blue", "\x1b[94mfoo\x1b[00m"),
        ("bold", "\x1b[01mfoo\x1b[00m"),
        ("cyan", "\x1b[96mfoo\x1b[00m"),
        ("gray", "\x1b[90mfoo\x1b[00m"),
        ("grey", "\x1b[90mfoo\x1b[00m"),
        ("magenta", "\x1b[95mfoo\x1b[00m"),
        ("red", "\x1b[91mfoo\x1b[00m"),
        ("white", "\x1b[97mfoo\x1b[00m"),
        ("yellow", "\x1b[93mfoo\x1b[00m"),
    ],
)
def test_colors(color_name: str, expected: str) -> None:
    assert getattr(colors, color_name)("foo") == expected
