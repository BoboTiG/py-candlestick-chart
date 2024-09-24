"""
Draw candlesticks charts right into your terminal.

This module is maintained by Mickaël Schoentgen <contact@tiger-222.fr>.

You can always get the latest version of this module at:
    https://github.com/BoboTiG/py-candlestrick-charts
If that URL should fail, try contacting the author.
"""

__version__ = "2.7.1-dev"
__author__ = "Mickaël Schoentgen"
__copyright__ = f"""
Copyright (c) 2022-2024, {__author__}
Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee or royalty is hereby
granted, provided that the above copyright notice appear in all copies
and that both that copyright notice and this permission notice appear
in supporting documentation or portions thereof, including
modifications, that you make.
"""

from .candle import Candle
from .chart import Chart
from .utils import fnum

__all__ = ("Candle", "Chart", "fnum")
