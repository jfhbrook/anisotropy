import json
from math import pi
from numpy import log, sin, cos, sqrt, array, arange, hstack, linspace, dot
from functools import reduce
#from matplotlib import pyplot as plt

def elliptical(fxn, ecc):
    from scipy.integrate import quad #Do I want quad?
    from math import pi
    from numpy import sin, cos, sqrt
    from types import FunctionType, BuiltinFunctionType
    if type(fxn) != FunctionType and type(fxn) != BuiltinFunctionType:
        fxn2 = lambda ecc, th: fxn
    else:
        fxn2 = fxn

    return quad(lambda th: fxn2(ecc,th) *
                               sqrt( cos(th)**2.0 + (ecc*sin(th))**2.0 ),
                0, 2*pi)[0]

def Tavg(k_x, k_y, q, t):
    """
    given scalar r0, k_x, k_y and 1-d time, this returns a curve with the same 
    slope at Tavg(t) for long T. May refactor.
    """
    return (4*pi*k_x/q)*array([elliptical(log(time) , k_y/k_x)/elliptical(1, k_y/k_x) for time in t])

def kmeas(k_x, k_y, q, t):
    from numpy import polyfit
    """
    Does a quick linear curve fit 
    """
    #print('Finding k_meas...')
    return (q/4/pi/k_x)*polyfit(t, log(Tavg(k_x, k_y, q, t)), 1)[0]

#Do I even need this?
def rot(th, axis):
    from numpy.linalg import norm
    from numpy import sin, cos, eye, outer, cross
    #print('Generating matrix...')
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
    #print('Projecting onto twospace...')
    #Using the normalized two-space as
    from numpy import diag
    from numpy.linalg import norm, eig
    twospace = dot(twospace, diag([1.0/norm(twospace.T[i]) for i in xrange(twospace.shape[0])]))
    #kind of a lisp-ish indent pattern, eh? >_<
    #Could probably make this more efficient.
    # BUG IN HERE MOST LIKELY
    return eig(dot(twospace, 
                   diag(dot(array([1,1,1]), 
                            dot(pad(twospace, threespace.shape), 
                                threespace))[0:twospace.shape[0]])))[0]

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
    from numpy import arange, diag, logspace, meshgrid
    from math import pi
    from progressbar import ProgressBar

    angles = arange(90) #Lots angles :D

    ks = arange(0.2, 0.4, 0.05) # Some ks
    [k_xy, k_z] = meshgrid(ks, ks)
    k_xy = k_xy.flatten()
    k_z = k_z.flatten()
    #print(k_xy)
    #print(k_z)

    q = 0.5 #Like in sims
    t = hstack(( logspace(0.1,1.0,15),
                 logspace(1.0,3.0,15) ))

    results = []
    progress = ProgressBar()
    for th in progress(angles):
        #print(rot(pi/180*th, 'z'))
        #print('Angle: '+ str(th))
        for i in xrange(ks.shape[0]):
            #print('k_xy = '+str(k_xy[i])+' and k_z = '+str(k_z[i])+': ')
            (k_xp, k_yp) = proj( diag([k_xy[i], k_xy[i], k_z[i]]),
                                 rot(pi/180*th, 'y')[::2,::2] )
            #print('k_xp = '+str(k_xp))
            #print('k_yp = '+str(k_yp))
            results.append([ th,
                             k_xy[i],
                             k_z[i],
                             k_xp,
                             k_yp,
                             kmeas(k_xp, k_yp, q, t)])
            #print('Done.')
    for row in results:
        print(', '.join(map(str, row)))

