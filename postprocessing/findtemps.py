#!/usr/bin/env python

from scipy.io import loadmat, savemat
from scipy import log, diff, ones
from numpy import interp
from matplotlib.pylab import plot, show

k_results=loadmat('../data/k_results.mat')['k_results']
log_t = log(k_results[0][0][0])
temp = k_results[0][0][1]

#finding derivatives based on list data
dlog=diff(log_t)
temp_p=diff(temp)/diff(log_t)

dlog2=interp( range(len(dlog)-1)+0.5*ones(len(dlog)-1), #points in between
              range(len(dlog)), #original indices
              dlog**2) #function

temp_pp=(diff(temp,2)/dlog2)

print "sizes of different things:"
print "log_t: " + repr(log_t.shape)
print "temp: " + repr(temp.shape)
print "temp_p: " + repr(temp_p.shape)
print "temp_pp: " + repr(temp_pp.shape)

plot(log_t,temp,'o')
plot(interp(range(len(log_t)-1)+0.5*ones(len(log_t)-1), 
            range(len(log_t)),log_t),
     temp_p,
     'o')
plot(log_t[1:-1],temp_pp,'o')

show()
