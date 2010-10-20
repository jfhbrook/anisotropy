from math import pi
from numpy import log, sin, cos, sqrt, array, arange, linspace
from scipy.integrate import quad as int #Do I want quad?
from matplotlib import pyplot as plt

def Tavg(r0, k_x, k_y, t):
    def r2(r0, k_x, k_y, theta):
        return r0**2.*(cos(theta)**2. + (k_x/k_y)*sin(theta)**2)
    def f(r0, k_x, k_y, theta, t):
        return (1./k_x) * log(4*k_x*t/r2(r0,k_x, k_y,theta))*sqrt(r2(r0, k_x, k_y, theta))
    def g(r0, k_x, k_y, theta):
        return sqrt(r2(r0, k_x, k_y, theta))

    return array([int(lambda th: f(r0, k_x, k_y, th, time), 0, 2*pi)[0] / int(lambda th: g(r0, k_x, k_y, th), 0, 2*pi)[0] for time in t])

if __name__=="__main__":
    from numpy import logspace
    t = logspace(-1,3,20)
    T = Tavg(0.00025, 0.1, 10., t)
    plolt = plt.plot(log(t), T)
    plt.show()
