# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2022-05-22

### Added

### Changed
- Fixed values computation in the info bar by using the whole candle set rather thant only the visible one (closes [#2])
- Changed the `Chart.update_candles()` behavior: it will update current candles by default, and now accepts a `reset=True` optional argument to actually erase all previous candles first (closes [#3])

### Removed


## [1.0.0] - 2022-05-21

### Added
- First version.


[2.0.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v2.0.0
[1.0.0]: https://github.com/BoboTiG/py-candlestick-chart/tree/v1.0.0

[#2]: https://github.com/BoboTiG/py-candlestick-chart/issues/2
[#3]: https://github.com/BoboTiG/py-candlestick-chart/issues/3
