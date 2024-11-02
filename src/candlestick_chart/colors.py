from functools import cache


def blue(value: str) -> str:
    return f"\033[94m{value}\033[00m"


def bold(value: str) -> str:
    return f"\033[01m{value}\033[00m"


def cyan(value: str) -> str:
    return f"\033[96m{value}\033[00m"


def grey(value: str) -> str:
    return f"\033[90m{value}\033[00m"


gray = grey


def green(value: str) -> str:
    return f"\033[92m{value}\033[00m"


def magenta(value: str) -> str:
    return f"\033[95m{value}\033[00m"


def red(value: str) -> str:
    return f"\033[91m{value}\033[00m"


@cache
def truecolor(value: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{value}\033[00m"


def white(value: str) -> str:
    return f"\033[97m{value}\033[00m"


def yellow(value: str) -> str:
    return f"\033[93m{value}\033[00m"


COLORS = {
    "blue": blue,
    "cyan": cyan,
    "green": green,
    "gray": gray,
    "grey": grey,
    "magenta": magenta,
    "red": red,
    "white": white,
    "yellow": yellow,
}


def color(text: str, value: str | tuple[int, int, int]) -> str:
    if not value:
        return text

    if isinstance(value, tuple):
        return truecolor(text, *value)

    if col_fn := COLORS.get(value):
        return col_fn(text)

    # ANSI color
    # example: "93m" for yellow
    # example: "94;43" for blue on yellow background
    return f"\033[{value}{text}\033[00m"
