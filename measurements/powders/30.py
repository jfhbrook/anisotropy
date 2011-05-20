#!/usr/bin/env python

# This tested 30 degrees, one of the most extreme angles practically testable
# in this apparatus.

from testtools import *

#first

data = relative_time(hms_to_s(import_raw_data('30/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 2 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 2 < t < 120)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '30 1', k_hot, cooling_curve(cold, q_hot)


#2nd

data = relative_time(hms_to_s(import_raw_data('30/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 2.5 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 145)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '30 2', k_hot, cooling_curve(cold, q_hot)


#3rd

data = relative_time(hms_to_s(import_raw_data('30/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 150)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '30 3', k_hot, cooling_curve(cold, q_hot)


#4th

data = relative_time(hms_to_s(import_raw_data('30/4.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '30 4', k_hot, cooling_curve(cold, q_hot)
