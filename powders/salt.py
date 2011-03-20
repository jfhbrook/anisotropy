#!/usr/bin/env python

# This tested pure salt.

from testtools import *

#first salt measurement

data = relative_time(hms_to_s(import_raw_data('salt/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t < 180)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 4 < t < 85)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure salt" 1', k_hot, cooling_curve(cold, q_hot)



#second salt measurement

data = relative_time(hms_to_s(import_raw_data('salt/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t < 145)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 200)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure salt" 2', k_hot, cooling_curve(cold, q_hot)


#A third salt measurement

data = relative_time(hms_to_s(import_raw_data('salt/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 37)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '"pure sugar" 2', k_hot, cooling_curve(cold, q_hot)
