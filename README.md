# Python Candlesticks Chart

📈 Draw candlesticks charts right into your terminal with Python!

![Preview](examples/screenshot.png)

This is a portage from the great [cli-candlestick-chart](https://github.com/Julien-R44/cli-candlestick-chart) (developed by @Julien-R44, written in Rust). You are looking at the Python 3.10+ version.

Notes:
1. Not yet released (waiting on issue #1)
2. Not tested on macOS
3. Not tested on Windows (it will likely fail to render colors)

**Table of contents**:
- [Python Candlesticks Chart](#python-candlesticks-chart)
  - [Features](#features)
  - [Intallation](#intallation)
- [Binary Usage](#binary-usage)
- [Examples](#examples)
  - [API](#api)
  - [Binary](#binary)
    - [Read CSV from file](#read-csv-from-file)
    - [Read JSON from file](#read-json-from-file)
    - [Read from stdin](#read-from-stdin)

## Features

- Auto-fit to terminal size
- Practical formatting for big, and tiny, numbers
- Simple, yet customizable, API
- Exact same API as the [Rust version](https://github.com/Julien-R44/cli-candlestick-chart)
- Installation simple, no external dependencies

## Intallation

As simple as:

```bash
$ python -m pip install -U candlestick-chart
```

```python
from candlestick_chart import Candle, Chart

# Add some candles
candles = [
    Candle(133.520004, 133.610001, 126.760002, 129.410004),
    Candle(128.889999, 131.740005, 128.429993, 131.009995),
    Candle(127.720001, 131.050003, 126.379997, 126.599998),
    Candle(128.360001, 131.630005, 127.860001, 130.919998),
    Candle(132.429993, 132.630005, 130.229996, 132.050003),
]

# Create and display the chart
chart = Chart(candles, title="Optional title")

# Set the chart title
chart.set_name("BTC/USDT")

# Set customs colors
chart.set_bear_color(1, 205, 254)
chart.set_bull_color(255, 107, 153)
chart.set_vol_bull_color(1, 205, 254)
chart.set_vol_bear_color(255, 107, 153)

chart.set_volume_pane_height(6)
chart.set_volume_pane_enabled(False)

chart.draw()
```

# Binary Usage

When installing the library, an executable is made available (`candlestick-chart`):

```bash
$ candlestick-chart --help             

options:
  -h, --help            show this help message and exit
  -m {stdin,csv-file,json-file}, --mode {stdin,csv-file,json-file}
                        Select the method for retrieving the candles.
  -f FILE, --file FILE  [MODE:*-file] File to read candles from.
  --chart-name CHART_NAME
                        Sets the chart name.
  --bear-color BEAR_COLOR
                        Sets the descending candles color in hexadecimal.
  --bull-color BULL_COLOR
                        Sets the ascending candles color in hexadecimal.
  --version             show program's version number and exit
```

When requesting the JSON or stdin mode, the library expects a JSON with the following format: 

```json
[
    {
        "open": 28994.009766,
        "high": 29600.626953,
        "low": 28803.585938,
        "close": 29374.152344
    },
    ...
]
```

For all requests, here are supported fields:

```python
"open": float  # mandatory
"close": float  # mandatory
"high": float  # mandatory
"low": float  # mandatory
"volume": float
"timestamp": float
```

# Examples

## API 

- [Basic example with CSV parsing](examples/basic-from-csv-file.py): run with `$ python examples/basic-from-csv-file.py`
- [Basic example with JSON parsing](examples/basic-from-json-file.py): run with `$ python examples/basic-from-json-file.py`
- [Basic example with stdin parsing](examples/basic-from-stdin.sh): run with `$ ./examples/basic-from-stdin.sh`
- [Fetch candles from Binance](examples/fetch-from-binance.py): run with `$ python fetch-from-binance.py`

## Binary 

### Read CSV from file

```bash
$ candlestick-chart \
    --mode=csv-file \
    -f=./examples/BTC-USD.csv \
    --chart-name="My BTC Chart" \
    --bear-color="#b967ff" \
    --bull-color="ff6b99"
```
### Read JSON from file

```bash
$ candlestick-chart \
    --mode=json-file \
    -f=./examples/BTC-chart.json \
    --chart-name="My BTC Chart" \
    --bear-color="#b967ff" \
    --bull-color="ff6b99"
```

### Read from stdin

```bash
echo '[
  {
    "open": 28994.009766,
    "high": 29600.626953,
    "low": 28803.585938,
    "close": 29374.152344
  },
  {
    "open": 29376.455078,
    "high": 33155.117188,
    "low": 29091.181641,
    "close": 32127.267578
  }
]' | candlestick-chart \
    --mode=stdin \
    --chart-name="My BTC Chart" \
    --bear-color="#b967ff" \
    --bull-color="ff6b99"
```
