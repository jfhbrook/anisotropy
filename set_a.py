#!/usr/bin/env python

# This was a series of tests with Actual Snow.

from testtools.py import *

# Grab the particular dataset we want
data = hms_to_s(import_raw_data('data.csv'))

tab_plot(data, 'sec', y_headers=["needletemp", "volts"])

"""
#Manual split
(hot, cold) = map(relative_time, Splitters.manual(data, 'sec', 725))

#tab_plot(hot, 'sec', y_headers=["needletemp"], fit=linreg(hot))
#tab_plot(cold, 'sec', y_headers=["needletemp"], fit=linreg(cold))

#Choose the "good" part of the hot table.
hot = tab_filter(hot, 'sec', lambda t: t > 4.5)

#tab_plot(hot, 'sec', y_headers=["needletemp"], fit=linreg(hot))

#Find all the parts from the hot part needed to do the cool part
q_hot = q(hot)
k_hot = heating_curve(hot, q_hot)
hot_period = hot['sec'][-1]

#apply the McGaw correction
cold_m = mcgaw(cold, k_hot, q_hot, hot_period)
tab_plot(cold_m, 'sec', y_headers=["needletemp"], fit=linreg(cold_m))
tab_plot(cold, 'sec', y_headers=["needletemp"], fit=linreg(cold))
cold_m = tab_filter(cold_m, 'sec', lambda t: t > 8.0)
cold = tab_filter(cold, 'sec', lambda t: t > 6.0)

k_cold = cooling_curve(cold, q_hot)
k_cold_m = cooling_curve(cold_m, q_hot)
print 'k_hot: ', k_hot
print 'k_cold: ', k_cold
print 'k_cold_m: ', k_cold_m

"""
