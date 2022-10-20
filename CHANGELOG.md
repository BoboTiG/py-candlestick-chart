# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 202x-xx-xx

### Added
- 

### Changed
- Allow to pass a blank color to `color()`, it will return the text unchanged
- Refactored price hightlights, it should now highlight price that would be hidden by a slightly upper value (like 1.025 being hidden because that exact price is not available, but it is surrounded by 1.02, and 1.03, then it will take the place of 1.02)
- Better-looking Y-axis style (when on the left-side: `PRICE │―` → `PRICE ┤`, and on the right-side: `│― PRICE` → `├ PRICE`)

### Removed
-

## [2.5.0] - 2022-10-19

### Added
- Capability to round prices on the Y-axis via `Y_AXIS_ROUND_DIR` (either `down` [default], or `up`), and `Y_AXIS_ROUND_MULTIPLIER` (`0.0` by default, set something like `1 / 0.01` to round price to 2 decimals), constants

### Changed
- Improve rendering performances by ~60%

## [2.4.0] - 2022-09-23

### Added
- Capability to highlight values on the Y-axis using `chart.set_highlight()`
- New colors: blue, cyan, grey, magenta, and white

## [2.3.0] - 2022-09-23

### Added
- Capability to display graduations on the right side by setting the `constants.Y_AXIS_ON_THE_RIGHT` to `True`

### Changed
- Fixed a zero division error when no candle volume is set
- Chart title is now hidden if it is an empty string

## [2.2.1] - 2022-08-12

### Added
- `constants.PRECISION`, and `constants.PRECISION_SMALL` to control the number of decimals to keep when formatting numbers with `fnum()` (defaults to `2`, and `4`, respectively)
- `constants.MIN_DIFF_THRESHOLD`, and `constants.MAX_DIFF_THRESHOLD` to control candle top, and bottom, thickness `fnum()` (defaults to `0.25`, and `0.75`, respectively)

### Changed
- Fixed formatting of `1.0` number within `fnum()`
- Fixed imports using `isort`

## [2.2.0] - 2022-08-12

### Added
- `Candle.__eq__()` to allow comparing candles
- Introduced `constants.Y_AXIS_SPACING` to give control Y-axis spacing between graduations (defaults to `4`, reduce to display more graduations, and set a higher number to display less graduations)

### Changed
- Constant changes are now taken into account in real-time, it allowes to tweak the chart appearence after having imported the module
- Always show the volume pane when it is enabled

## [2.1.0] - 2022-07-20

### Added
- Nice `Candle` Python representation

### Changed
- Fixed a zero division error when min, and max, prices are equals inside a same candle (closes [#4])
- Fixed small numbers display on the Y-axis (closes [#5])
- Fixed bearish/bullish colors inversion in the volume pane

## [2.0.0] - 2022-05-22

### Changed
- Fixed values computation in the info bar by using the whole candle set rather thant only the visible one (closes [#2])
- Changed the `Chart.update_candles()` behavior: it will update current candles by default, and now accepts a `reset=True` optional argument to actually erase all previous candles first (closes [#3])

## [1.0.0] - 2022-05-21

### Added
- First version.


[Unreleased]: https://github.com/BoboTiG/py-candlestick-chart/compare/v2.5.0...HEAD
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
