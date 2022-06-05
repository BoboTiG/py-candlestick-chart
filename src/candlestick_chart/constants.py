from types import SimpleNamespace

# Info bar labels
# Labels can be customized via `Chart.set_label("label", "value")`
# (setting a label to an empty string will hide it from the chart)
LABELS = SimpleNamespace(
    average="Avg.",
    currency="",
    highest="Highest",
    lowest="Lowest",
    price="Price",
    variation="Var.",
    volume="Cum. Vol.",
)

# Margins, and internal sizes
MARGIN_TOP: int = 3
MARGIN_RIGHT: int = 4
CHAR_PRECISION: int = 6
DEC_PRECISION: int = 5
WIDTH: int = CHAR_PRECISION + MARGIN_RIGHT + 1 + DEC_PRECISION + MARGIN_RIGHT
HEIGHT: int = 2

# Chart characters
UNICODE_BODY: str = "┃"
UNICODE_BOTTOM: str = "╿"
UNICODE_HALF_BODY_BOTTOM: str = "╻"
UNICODE_HALF_BODY_TOP: str = "╹"
UNICODE_FILL: str = "┃"
UNICODE_TOP: str = "╽"
UNICODE_VOID: str = " "
UNICODE_WICK: str = "│"
UNICODE_WICK_LOWER: str = "╵"
UNICODE_WICK_UPPER: str = "╷"
