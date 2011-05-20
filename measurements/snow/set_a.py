#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools import *

# Grab the particular dataset we want
data = relative_time(
           tab_filter(hms_to_s(import_raw_data('set_a/data.csv')),
                     'sec',
                     lambda t: t > 580))

tab_plot(data, 'sec', y_headers=["needletemp"])

"""
It can be seen that many measurements were lost. This experimental run was a
failure in terms of retrieving useful data.
"""
