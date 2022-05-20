from typing import Tuple


def bold(value: str) -> str:
    return f"\033[01m{value}\033[00m"


def green(value: str) -> str:
    return f"\033[92m{value}\033[00m"


def red(value: str) -> str:
    return f"\033[91m{value}\033[00m"


def truecolor(value: str, rgb: Tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{value}\033[00m"


def yellow(value: str) -> str:
    return f"\033[93m{value}\033[00m"
