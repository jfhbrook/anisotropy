#!/usr/bin/env python

# This tested 60 degrees.

from testtools import *

#first

"""
data = relative_time(hms_to_s(import_raw_data('60/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])


#There was a snafu with the measurement; time started at 14.5 s.
(hot, cold) = Splitters.manual(data, 'sec', 360-14.5)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360-14.5)

cold = tab_filter(cold, 'sec', lambda t: 4 < t < 150)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

#This measurement appears to be garbage.
print '60 1', k_hot, cooling_curve(cold, q_hot)
"""


#second measurement

data = relative_time(hms_to_s(import_raw_data('60/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 1 < t < 30)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3.5 < t)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '60 2', k_hot, cooling_curve(cold, q_hot)



#third

data = relative_time(hms_to_s(import_raw_data('60/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 5 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 135)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '60 3', k_hot, cooling_curve(cold, q_hot)


#fourth

data = relative_time(hms_to_s(import_raw_data('60/4.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 130)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '60 4', k_hot, cooling_curve(cold, q_hot)

