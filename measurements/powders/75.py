#!/usr/bin/env python

# This tested 75 degrees (vertical).

from testtools import *

#first. Forgot to close box.

data = relative_time(hms_to_s(import_raw_data('75/1.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

# mcgaw isn't appropriate for this particular case because I forgot to close
# the door.
cold = relative_time(cold)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 70)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '75 1', k_hot, cooling_curve(cold, q_hot)


#second measurement

data = relative_time(hms_to_s(import_raw_data('75/2.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 3 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 2 < t < 180)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '75 2', k_hot, cooling_curve(cold, q_hot)



#third

data = relative_time(hms_to_s(import_raw_data('75/3.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t < 70)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 125)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '75 3', k_hot, cooling_curve(cold, q_hot)


#fourth

data = relative_time(hms_to_s(import_raw_data('75/4.csv')))
#tab_plot(data, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(data, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_hot = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 4 < t)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

k_hot = heating_curve(hot, q_hot)

cold = mcgaw(relative_time(cold), k_hot, q_hot, 360)

cold = tab_filter(cold, 'sec', lambda t: 3 < t < 160)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '75 4', k_hot, cooling_curve(cold, q_hot)
