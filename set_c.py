#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools import *

(fst, data) = Splitters.manual(relative_time(hms_to_s(import_raw_data('set_c/data.csv'))), 'sec', 900)
#tab_plot(fst, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(fst, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_fst = q(hot)


hot = tab_filter(hot, 'sec', lambda t: 10 < t < 500)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

print 'heating,35,', heating_curve(hot, q_fst)

cold = tab_filter(relative_time(cold), 'sec', lambda t: 6 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print 'cooling,35,', cooling_curve(cold, q_fst)
