from scipy.io import loadmat, savemat
from scipy import log, diff, ones
from numpy import interp
from matplotlib.pylab import plot

k_results=loadmat('../data/k_results_feb2010.mat')['k_results']
log_t = log(k_results[0][0][0])
temp = k_results[0][0][1]
temp_p=diff(temp)/diff(log_t)

# one thing too long
# also hard2read
temp_pp=diff(temp,2)/interp(range(len(diff(log_t))) + 0.5*ones(diff(log_t).shape),range(len(diff(log_t))),diff(log_t))**2

plot(log_t,temp)
plot(log_t,temp_p)
plot(log_t,temp_pp)
