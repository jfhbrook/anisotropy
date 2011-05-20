#!/usr/bin/env python

# This tested pure sugar.

from testtools import *

#first sugar measurement

data = relative_time(hms_to_s(import_raw_data('sugar/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 8 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 6 < t < 90)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure sugar" 1', k_hot, cooling_curve(cold, q_hot)



#second sugar measurement

data = relative_time(hms_to_s(import_raw_data('sugar/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t < 85)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 6 < t < 75)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure sugar" 2', k_hot, cooling_curve(cold, q_hot)



#third sugar measurement

data = relative_time(hms_to_s(import_raw_data('sugar/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 5 < t < 70)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure sugar" 3', k_hot, cooling_curve(cold, q_hot)
