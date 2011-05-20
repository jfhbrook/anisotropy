#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools import *

# Grab the particular dataset we want
data = tab_filter(hms_to_s(import_raw_data('set_b/data.csv')),
                  'sec',
                  lambda t: t > 0)

tab_plot(data, 'sec', y_headers=["needletemp"])

"""
This data ALSO got messed up. Bollocks.
"""
