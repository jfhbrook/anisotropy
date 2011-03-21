#!/usr/bin/env python

# This tested 90 degrees (vertical).

from testtools import *

#first

data = relative_time(hms_to_s(import_raw_data('90/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 2 < t < 190)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 4 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '90 1', k_hot, cooling_curve(cold, q_hot)



#second measurement

data = relative_time(hms_to_s(import_raw_data('90/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 110)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '90 2', k_hot, cooling_curve(cold, q_hot)



#third

"""
data = relative_time(hms_to_s(import_raw_data('90/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: True)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: True)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '90 3', k_hot, cooling_curve(cold, q_hot)

"""
