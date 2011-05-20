from math import pi
from numpy import log, sin, cos, sqrt, array, arange, linspace, dot
from scipy.integrate import quad #Do I want quad?
from ortho_projector import proj as vproj
#from matplotlib import pyplot as plt

def Tavg(r0, k_x, k_y, t):
    """
    given scalar r0, k_x, k_y and 1-d time, this returns T(t). Or rather,
    something slightly different, but proportional.
    """
    def r2(r0, k_x, k_y, theta):
        return r0**2.*(cos(theta)**2. + (k_x/k_y)*sin(theta)**2)
    def f(r0, k_x, k_y, theta, t):
        return (1./k_x) * log(4*k_x*t/r2(r0,k_x, k_y,theta))*sqrt(r2(r0, k_x, k_y, theta))
    def g(r0, k_x, k_y, theta):
        return sqrt(r2(r0, k_x, k_y, theta))

    return array([quad(lambda th: f(r0, k_x, k_y, th, time), 0, 2*pi)[0] / quad(lambda th: g(r0, k_x, k_y, th), 0, 2*pi)[0] for time in t])

#Want to port some of these ideas to proj maybe
def proj(threesp, twosp):
    """
    Project a larger space onto a smaller one. Basically.
    """

    #Alternately, change twospace s.t. it has vectors in other spaces, change
    #3-space to this new orientation, then "lop off" extra dimensions

    #extracts 2-space from three-space, then sums and decreases space dimension
    a = dot(array([1,1,1]),
            dot(pad(twosp, threesp.shape), threesp))[:twosp.shape[1]]
    #Likely returns an array, not a vector--probably good!
    #Needs testing.
    return array([vproj.of(a).onto(twosp[:,n]) for n in twosp.shape[1] ])
    

def pad(matrix, mn):
    """
    pads out matrices to have mxn dimensions
    future: Allow arbitrary placement
    """
    from numpy import hstack, vstack, zeros
    (dh, dw) = tuple(array(mn) - matrix.shape)
    return hstack((
        vstack((matrix,zeros((dh,matrix.shape[1])) )),
        zeros((mn[0],dw))
    ))


if __name__=="__main__":
    #from numpy import logspace
    #t = logspace(-1,3,20)
    #T = Tavg(0.00025, 0.1, 10., t)
    #plolt = plt.plot(log(t), T)
    #plt.show()
