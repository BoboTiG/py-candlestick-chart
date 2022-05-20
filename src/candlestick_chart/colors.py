from functools import cache


def bold(value: str) -> str:
    return f"\033[01m{value}\033[00m"


def green(value: str) -> str:
    return f"\033[92m{value}\033[00m"


def red(value: str) -> str:
    return f"\033[91m{value}\033[00m"


@cache
def truecolor(value: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{value}\033[00m"


def yellow(value: str) -> str:
    return f"\033[93m{value}\033[00m"
