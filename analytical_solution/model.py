from math import pi
from numpy import log, sin, cos, sqrt, array, arange, linspace, dot
from functools import reduce
#from stevia import proj
#from matplotlib import pyplot as plt

def elliptical(fxn, ecc):
    from scipy.integrate import quad #Do I want quad?
    from math import pi
    from numpy import sin, cos, sqrt
    return quad(lambda th: fxn(ecc,th) *
                                sqrt( cos(th)**2.0 + (ecc*sin(th))**2.0 )  ,
                0, 2*pi)

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

#Do I even need this?
def rot(th, axis):
    from numpy.linalg import norm
    from numpy import sin, cos, eye, outer, cross
    if axis == "x":
        axis = array([1,0,0])
    elif axis == "y":
        axis = array([0,1,0])
    elif axis == "z":
        axis = array([0,0,1])
    else:
        axis = axis/norm(axis)
    oh = outer(axis, axis)
    return oh + cos(th)*(eye(3) - oh) + sin(th)*cross(axis, eye(3))
    

#Want to port some of these ideas to proj, but I suck at stuff
#Probably don't even actually want to do this, really, but whatevs
def proj(threespace, twospace):
    #Using the normalized two-space as
    from numpy import diag
    from numpy.linalg import norm, eig
    twospace = dot(twospace, diag([1.0/norm(twospace.T[i]) for i in xrange(twospace.shape[0])]))
    print(twospace)
    #kind of a lisp-ish indent pattern, eh? >_<
    #Could probably make this more efficient.
    return eig(dot(twospace, 
                   diag(dot(array([1,1,1]), 
                            dot(pad(twospace, threespace.shape), 
                                threespace))[0:twospace.shape[0]])))

def pad(matrix, mn):
    #Pads matrix to be mxn by adding zeros to right and bottom
    from numpy import hstack, vstack, zeros
    (dh, dw) = tuple(array(mn) - matrix.shape)
    return hstack((
        vstack((matrix,zeros((dh,matrix.shape[1])) )),
        zeros((mn[0],dw))
    ))

def trim(matrix, mn):
    #Trims matrix by dropping right and bottom edges
    #Breaks for vectors :S
    return matrix[0:mn[0], 0:mn[1]]

if __name__=="__main__":
    from numpy import eye, arange
    I = eye(3)
    I[2,2] = 0
    #Generates some matrices with a dimension dropped out
    for theta in pi*arange(90)/180:
        R = rot(theta, 'x')
        print( reduce(dot, [R, I, R.T]) )

