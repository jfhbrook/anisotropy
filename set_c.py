#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools import *

data = import_raw_data('set_c/data.csv')
fst = relative_time(hms_to_s(tab_filter(data, 'day', lambda d: d == 75)))
data = relative_time(hms_to_s(tab_filter(data, 'day', lambda d: d==76)))
#tab_plot(data, 'sec', y_headers=["needletemp"])

#(fst, data) = Splitters.manual(data, 'sec', 900)
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


(snd, data) = Splitters.manual(data, 'sec', 900)
#tab_plot(snd, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(snd, 'sec', 350)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_snd = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 7 < t < 60)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

print 'heating,85,', heating_curve(hot, q_snd)


cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 10 < t < 75)

print 'cooling,85,', cooling_curve(cold, q_snd)
tab_plot(cold, 'sec', y_headers=["needletemp"])
