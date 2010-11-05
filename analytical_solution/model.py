from math import pi
from numpy import log, sin, cos, sqrt, array, arange, linspace, dot
from functools import reduce
#from matplotlib import pyplot as plt

def elliptical(fxn, ecc):
    from scipy.integrate import quad #Do I want quad?
    from math import pi
    from numpy import sin, cos, sqrt
    if type(fxn) == int:
        fxn = lambda ecc, th: fxn
    return quad(lambda th: fxn(ecc,th) *
                               sqrt( cos(th)**2.0 + (ecc*sin(th))**2.0 ),
                0, 2*pi)[0]

def Tavg(k_x, k_y, q, t):
    """
    given scalar r0, k_x, k_y and 1-d time, this returns a curve with the same 
    slope at Tavg(t) for long T. May refactor.
    """
    return (4*pi*k_x/q)*array([elliptical(log(t) , k_y/k_x)/elliptical(1, k_y/k_x) for time in t])

def kmeas(Tavg, t, k_x, k_y, q):
    from numpy import polyfit
    """
    Does a quick linear curve fit 
    """
    return (q/4/pi/k_x)*polyfit(t, log(Tavg), 1)[0]

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
    """
    Pads matrix to be mxn by adding zeros to right and bottom
    """
    from numpy import hstack, vstack, zeros
    (dh, dw) = tuple(array(mn) - matrix.shape)
    return hstack((
        vstack((matrix,zeros((dh,matrix.shape[1])) )),
        zeros((mn[0],dw))
    ))

def trim(matrix, mn):
    """
    Trims matrix by dropping right and bottom edges
    Breaks for vectors :S
    """
    return matrix[0:mn[0], 0:mn[1]]

if __name__=="__main__":
    from numpy import diag, arange, meshgrid
    from math import pi
    angles = arange(90) #Lots angles :D
    ks = arange(0.2, 0.05, 0.4)
    [k_xy, k_z] = meshgrid(ks, ks)
    results = []

    #TODO:
    # 1) angles = arange(some bullshit)
    # 2) Rotate xz plane along y by angle degrees
    # 3) Find 2-d problem for x'z' plane
    # 4) Find that k-meas as functions of different k_x and k_y
    # 5) Output those solutions!


    for th in angles:
        #Need some kxy, kz action.
        #Generate angular rotation action
        #Generate k_meas
        #results.push([angle, k_xy, k_z, k_meas])
