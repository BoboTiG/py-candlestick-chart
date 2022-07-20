"""
Draw candlesticks charts right into your terminal.

This module is maintained by Mickaël Schoentgen <contact@tiger-222.fr>.

You can always get the latest version of this module at:
    https://github.com/BoboTiG/py-candlestrick-charts
If that URL should fail, try contacting the author.
"""

__version__ = "2.1.0"
__author__ = "Mickaël 'Tiger-222' Schoentgen"
__copyright__ = """
Copyright (c) 2022, Mickaël 'Tiger-222' Schoentgen
Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee or royalty is hereby
granted, provided that the above copyright notice appear in all copies
and that both that copyright notice and this permission notice appear
in supporting documentation or portions thereof, including
modifications, that you make.
"""

from .candle import Candle
from .chart import Chart

__all__ = ("Candle", "Chart")
