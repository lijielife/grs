# -*- coding: utf-8 -*-
''' All grs module '''
# Copyright (c) 2012, 2013, 2014 Toomore Chiang, http://toomore.net/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__title__ = 'grs'
__version__ = '0.5.6'
__author__ = 'Toomore Chiang'
__license__ = 'MIT'
__copyright__ = 'Copyright (C) 2012, 2013, 2014 Toomore Chiang'


from .best_buy_or_sell import BestFourPoint
try:
    from .fetch_data import Stock
except ImportError:
    pass
from .realtime import RealtimeStock
from .realtime import RealtimeWeight
from .tw_time import Countdown
from .tw_time import TWTime
from .twseno import OTCNo
from .twseno import TWSENo
from .twseopen import TWSEOpen
