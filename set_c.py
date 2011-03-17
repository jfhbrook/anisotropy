#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools import *

(fst, data) = Splitters.manual(relative_time(hms_to_s(import_raw_data('set_c/data.csv'))), 'sec', 630)
#tab_plot(fst, 'sec', y_headers=["needletemp", "reftemp"])

"""
First run appears weird, but the cooling curve may prove useful.
I believe the first measurement may have been 'eaten' by my own stupidity.
"""

(hot, cold) = map(relative_time, Splitters.manual(fst, 'sec', 42))
#tab_plot(cold, 'sec', y_headers=["needletemp"])

cold = tab_filter(cold, 'sec', lambda t: 6 < t < 42)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

#tab_plot(hot, 'sec', y_headers=["volts"])

print "cooling curve, 97 deg.: ", cooling_curve(cold,q(hot))



data = relative_time(data)
#tab_plot(data, 'sec', y_headers=["needletemp"])

(snd, data) = Splitters.manual(relative_time(data), 'sec', 620)
#tab_plot(snd, 'sec', y_headers=["needletemp"])

#tab_plot(data, 'sec', y_headers=["needletemp"])
(trd, data) = Splitters.manual(data, 'sec', 2000)

(hot, cold) = map(relative_time, Splitters.manual(snd, 'sec', 376))
#tab_plot(cold, 'sec', y_headers=["needletemp"])

hot = relative_time(tab_filter(hot, 'volts', lambda v: v > 0.001))
#tab_plot(hot, 'sec', y_headers=["needletemp"])
q_snd = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 20 < t < 90)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

print "heating curve, 50 deg.: ", heating_curve(hot, q_snd)

cold = tab_filter(cold, 'sec', lambda t: 10 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print "cooling curve, 50 deg.: ", cooling_curve(cold,q_snd)

trd = relative_time(tab_filter(trd, 'sec', lambda t: t > 1080))
#tab_plot(trd, 'sec', y_headers=["needletemp"])

(hot, cold) = map(relative_time, Splitters.manual(trd, 'sec', 360))
hot = tab_filter(hot, 'sec', lambda t: t > 6)

#tab_plot(hot, 'sec', y_headers=["volts"])
q_trd = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 0 < t < 80)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

print "heating curve, 35 deg.: ", heating_curve(hot, q_trd)

cold = tab_filter(cold, 'sec', lambda t: 6 < t < 58)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print "cooling curve, 50 deg.: ", cooling_curve(cold,q_trd)
