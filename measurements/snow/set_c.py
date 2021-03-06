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


hot = tab_filter(hot, 'sec', lambda t: 4 < t < 40)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

#print 'heating,85,', heating_curve(hot, q_fst)

cold = tab_filter(relative_time(cold), 'sec', lambda t: 6 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

#print 'cooling,85,', cooling_curve(cold, q_fst)


(snd, data) = Splitters.manual(data, 'sec', 900)
#tab_plot(snd, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(snd, 'sec', 350)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_snd = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 7 < t < 60)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 10 < t < 75)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '85', heating_curve(hot, q_snd), cooling_curve(cold, q_snd)

data = relative_time(tab_filter(data, 'sec', lambda t: t > 2000))
(trd, data) = Splitters.manual(data, 'sec', 900)
#tab_plot(trd, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(trd, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_trd = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 8 < t < 58)
#tab_plot(hot, 'sec', y_headers=["needletemp"])


cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 7 < t < 70)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '85', heating_curve(hot, q_trd), cooling_curve(cold, q_trd)

data = relative_time(tab_filter(data, 'sec', lambda t: t > 3000))
(fourth, data) = Splitters.manual(data, 'sec', 910)
#tab_plot(fourth, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(fourth, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_fth = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 12 < t < 58)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 7 < t < 63)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '38', heating_curve(hot, q_fth), cooling_curve(cold, q_fth)

data = relative_time(data)
(fifth, sixth) = Splitters.manual(data, 'sec', 900)
#tab_plot(fifth, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(fourth, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_ffth = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 9 < t < 50)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 13 < t < 70)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '45', heating_curve(hot, q_ffth), cooling_curve(cold, q_ffth)


sixth = relative_time(tab_filter(sixth, 'sec', lambda t: t > 5300))
#tab_plot(sixth, 'sec', y_headers=["needletemp"])

(hot, cold) = Splitters.manual(fourth, 'sec', 360)
#tab_plot(hot, 'sec', y_headers=["volts"])

q_sixth = q(hot)

hot = tab_filter(hot, 'sec', lambda t: 12 < t < 60)
#tab_plot(hot, 'sec', y_headers=["needletemp"])

cold = relative_time(cold)
cold = tab_filter(cold, 'sec', lambda t: 12 < t < 60)
#tab_plot(cold, 'sec', y_headers=["needletemp"])

print '90', heating_curve(hot, q_sixth), cooling_curve(cold, q_sixth)
