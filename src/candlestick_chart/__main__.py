import sys
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter

from candlestick_chart import __version__, Chart
from candlestick_chart.utils import (
    hexa_to_rgb,
    parse_candles_from_csv,
    parse_candles_from_stdin,
    parse_candles_from_json,
)


def get_args() -> Namespace:
    parser = ArgumentParser(
        prog="candlestick-chart",
        description="Draw candlesticks charts right into your terminal.",
        epilog=(
            "This module is maintained by Mickaël Schoentgen <contact@tiger-222.fr>."
            "\nYou can always get the latest version of this module at:"
            "\n    https://github.com/BoboTiG/py-candlestrick-charts"
            "\nIf that URL should fail, try contacting the author."
        ),
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-m",
        "--mode",
        help="Select the method for retrieving the candles.",
        choices=["stdin", "csv-file", "json-file"],
        required=True,
    )
    parser.add_argument("-f", "--file", help="[MODE:*-file] File to read candles from.")
    parser.add_argument("--chart-name", help="Sets the chart name.")
    parser.add_argument(
        "--bear-color", help="Sets the descending candles color in hexadecimal."
    )
    parser.add_argument(
        "--bull-color", help="Sets the ascending candles color in hexadecimal."
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser.parse_args(sys.argv[1:])


def main() -> int:
    options = get_args()

    if options.mode == "csv-file":
        candles = parse_candles_from_csv(options.file)
    elif options.mode == "json-file":
        candles = parse_candles_from_json(options.file)
    else:  # stdin
        candles = parse_candles_from_stdin()

    chart = Chart(candles, title=options.chart_name)

    if options.bear_color:
        r, g, b = hexa_to_rgb(options.bear_color)
        chart.set_bear_color(r, g, b)
    if options.bull_color:
        r, g, b = hexa_to_rgb(options.bull_color)
        chart.set_bull_color(r, g, b)

    chart.draw()
    return 0


if __name__ == "__main__":
    sys.exit(main())
