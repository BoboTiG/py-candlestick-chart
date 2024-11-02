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
MARGIN_TOP = 3
MARGIN_RIGHT = 4
CHAR_PRECISION = 6
DEC_PRECISION = 5
WIDTH = CHAR_PRECISION + 1 + DEC_PRECISION + MARGIN_RIGHT
HEIGHT = 2
Y_AXIS_SPACING = 4

# Numbers formatting
PRECISION = 2
PRECISION_SMALL = 4

# Chart characters
UNICODE_BODY = "┃"
UNICODE_BOTTOM = "╿"
UNICODE_HALF_BODY_BOTTOM = "╻"
UNICODE_HALF_BODY_TOP = "╹"
UNICODE_FILL = "┃"
UNICODE_TOP = "╽"
UNICODE_VOID = " "
UNICODE_WICK = "│"
UNICODE_WICK_LOWER = "╵"
UNICODE_WICK_UPPER = "╷"
UNICODE_Y_AXIS = "│"
UNICODE_Y_AXIS_LEFT = "┤"
UNICODE_Y_AXIS_RIGHT = "├"
MIN_DIFF_THRESHOLD = 0.25
MAX_DIFF_THRESHOLD = 0.75

# Chart options
Y_AXIS_ON_THE_RIGHT = False
Y_AXIS_ROUND_DIR = "down"  # Or "up"
# Examples:
#   1 / 0.01
#   1 / 0.0025
Y_AXIS_ROUND_MULTIPLIER = 0.0
