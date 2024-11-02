# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [3.1.0] - 2024-11-02

### Added
- Support for Python 3.14.
- Introduce `constants.UNICODE_Y_AXIS`, `constants.UNICODE_Y_AXIS_LEFT`, and `constants.UNICODE_Y_AXIS_RIGHT`, constants to control the Unicode character printed next to prices on the Y-axis (defaults to `│`, `┤`, and `├`, respectively).
- New color: gray (which is an alias to the misspelled "grey").
- New `utils.round_price()` function to either round down, or up, the price on the Y-axis. Previously, it was a private method of the `YAxis` class.

### Changed
- Fixed `CandleSet.min_volume` being always `0.0` (commit [6975d7f]).
- Those functions now also accept a `pathlib.Path` argument, in addition to the original `str`: `utils.parse_candles_from_csv()`, and `utils.parse_candles_from_json()`.
- 100% coverage with tests!
- Updated the `pypa/gh-action-pypi-publish` GitHub action from `master` to `release/v1`.

## [3.0.0] - 2024-09-24

### Added
- Support for Python 3.13.
- CI to automatically publish releases on tag creation.
- Using now the `ruff` module for the code quality.

### Changed
- (breaking change) Enforced usage of proper keyword-arguments.
- Use absolute imports.
- Level up the packaging using `hatchling`.
- Pin all requirements.
- Updated README's code example (fixes [#13]).
- Fixed typos using `codespell` ([#15] by @kianmeng).

### Removed
- Modules `black`, `flake8`, and `isort`, are no more used for the code quality.

## [2.7.0] - 2024-04-23

### Added
- Support for Python 3.12.
- CI to run unit tests.
- Tests for the CLI entry point.

### Changed
- Set the default chart name to a blank string in the CLI (fixes [#9]).
- Use `shutil.get_terminal_size()` instead of `os.get_terminal_size()` to be able to run tests without hitting `OSError: [Errno 25] Inappropriate ioctl for device`.
- Fix Mypy error `PEP 484 prohibits implicit Optional`.

## [2.6.0] - 2023-04-14

### Added
- Allow to use a custom class for the chart rendering via the `Chart(..., renderer_cls=MyClass)` keyword argument (see `examples/custom-renderer-class.py` for inspiration).
- The module is now PEP 561 compatible, and tested with `mypy`.

### Changed
- Fixed off-by-one shift when rendering empty lines on the Y-axis (the issue was visible only when the Y-axis was on the left side) (fixes [#7]).

## [2.5.1] - 2022-10-21

### Changed
- Allow to pass a blank color to `color()`, it will return the text unchanged.
- Refactored price highlights, it should now highlight price that would be hidden by a slightly upper value (like 1.025 being hidden because that exact price is not available, but it is surrounded by 1.02, and 1.03, then it will take the place of 1.02).
- Better-looking Y-axis style (when on the left-side: `PRICE │―` → `PRICE ┤`, and on the right-side: `│― PRICE` → `├ PRICE`).

## [2.5.0] - 2022-10-19

### Added
- Capability to round prices on the Y-axis via `Y_AXIS_ROUND_DIR` (either `down` [default], or `up`), and `Y_AXIS_ROUND_MULTIPLIER` (`0.0` by default, set something like `1 / 0.01` to round price to 2 decimals), constants.

### Changed
- Improve rendering performances by ~60%.

## [2.4.0] - 2022-09-23

### Added
- Capability to highlight values on the Y-axis using `chart.set_highlight()`.
- New colors: blue, cyan, grey, magenta, and white.

## [2.3.0] - 2022-09-23

### Added
- Capability to display graduations on the right side by setting the `constants.Y_AXIS_ON_THE_RIGHT` to `True`.

### Changed
- Fixed a zero division error when no candle volume is set.
- Chart title is now hidden if it is an empty string.

## [2.2.1] - 2022-08-12

### Added
- New `constants.PRECISION`, and `constants.PRECISION_SMALL`, constants to control the number of decimals to keep when formatting numbers with `fnum()` (defaults to `2`, and `4`, respectively).
- New `constants.MIN_DIFF_THRESHOLD`, and `constants.MAX_DIFF_THRESHOLD`, constants to control candle top, and bottom, thickness `fnum()` (defaults to `0.25`, and `0.75`, respectively).

### Changed
- Fixed formatting of `1.0` number within `fnum()`.
- Fixed imports using `isort`.

## [2.2.0] - 2022-08-12

### Added
- `Candle.__eq__()` to allow comparing candles.
- Introduced `constants.Y_AXIS_SPACING` to give control Y-axis spacing between graduations (defaults to `4`, reduce to display more graduations, and set a higher number to display less graduations).

### Changed
- Constant changes are now taken into account in real-time, it allows tweaking the chart appearance after having imported the module.
- Always show the volume pane when it is enabled.

## [2.1.0] - 2022-07-20

### Added
- Nice `Candle` Python representation.

### Changed
- Fixed a zero division error when min, and max, prices are equals inside a same candle (closes [#4]).
- Fixed small numbers display on the Y-axis (closes [#5]).
- Fixed bearish/bullish colors inversion in the volume pane.

## [2.0.0] - 2022-05-22

### Changed
- Fixed values computation in the info bar by using the whole candle set rather than only the visible one (closes [#2]).
- Changed the `Chart.update_candles()` behavior: it will update current candles by default, and now accepts a `reset=True` optional argument to actually erase all previous candles first (closes [#3]).

## [1.0.0] - 2022-05-21

### Added
- First version.


[3.1.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v3.1.0
[3.0.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v3.0.0
[2.7.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.7.0
[2.6.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.6.0
[2.5.1]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.5.1
[2.5.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.5.0
[2.4.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.4.0
[2.3.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.3.0
[2.2.1]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.2.1
[2.2.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.2.0
[2.1.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.1.0
[2.0.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.0.0
[1.0.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v1.0.0

[#2]: https://github.com/BoboTiG/py-candlestick-chart/issues/2
[#3]: https://github.com/BoboTiG/py-candlestick-chart/issues/3
[#4]: https://github.com/BoboTiG/py-candlestick-chart/issues/4
[#5]: https://github.com/BoboTiG/py-candlestick-chart/issues/5
[#7]: https://github.com/BoboTiG/py-candlestick-chart/issues/7
[#9]: https://github.com/BoboTiG/py-candlestick-chart/issues/9
[#13]: https://github.com/BoboTiG/py-candlestick-chart/issues/13
[#15]: https://github.com/BoboTiG/py-candlestick-chart/pull/15

[6975d7f]: https://github.com/BoboTiG/py-candlestick-chart/commit/6975d7fc1952c03af251bb12e758827cbea5b3ad
