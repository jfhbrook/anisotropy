from math import pi
from numpy import arange, \
                  array, \
                  cos, \
                  diag, \
                  dot, \
                  hstack, \
                  linspace, \
                  log, \
                  logspace, \
                  meshgrid, \
                  sin, \
                  sqrt, \
                  zeros
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import csv
from functools import reduce
from progressbar import ProgressBar


####
####Stuff for generating analytical guesses
####

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
    return (4*pi*k_x/q)*array([elliptical(log(time) , k_x/k_y)/elliptical(1, k_x/k_y) for time in t])

def kmeas(k_x, k_y, q, t):
    from numpy import polyfit
    """
    Does a quick linear curve fit 
    """
    #print('Finding k_meas...')
    return (q/4/pi)*polyfit(log(t), Tavg(k_x, k_y, q, t), 1)[0]

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
def proj(matrix, rot):
    #print('Projecting onto twospace...')
    #Using the normalized two-space as
    from numpy import eye, hstack, vstack, newaxis
    from numpy.linalg import eig
    return tuple(eig(reduce( dot, [ vstack((
                                        hstack(( eye(2), array([0, 0])[:, newaxis] )),
                                        array([0, 0, 0]))),
                                    rot,
                                    matrix,
                                    rot.T ]))[0])[0:2]

###
### Importing data
###


with open('./data_fea.csv') as f:
    fea = []
    for row in csv.reader(f):
        fea.append(row)
    fea = map(lambda x: array(x, dtype='float64'), zip(*fea))
    #data.csv = csv.read()

"""
with open('./analytical.csv') as f:
    analytical = []
    for row in csv.reader(f):
        analytical.append(row)
    analytical = map(lambda x: array(x, dtype='float64'), zip(*analytical))
"""

with open('./gridded.csv') as f:
    gridded = []
    for row in csv.reader(f):
        gridded.append(row)
    gridded = array(zip(*gridded), dtype='float64')

headers = ['angle', 'k_z', 'k_meas']

figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')
(xn, yn, zn) = fea

xg = gridded[0, 1::]
yg = gridded[1::, 0]
zg = gridded[1::, 1::]

# Same spacing---fine for now
xa = xg
ya = yg

(xg, yg) = meshgrid(xg, yg)

###
### Generating analytic predictions
###

t = hstack(( logspace(0.1,1.0,15),
             logspace(1.0,3.0,15) ))
q = 0.5 #Like in sims

za = []

for th in ya:
    zrow = []
    for kratio in xa:
        #print(xa)
        #print(kratio)
        kavg = 0.3 #typical value for snow
        kxy = 2*kavg/(1+kavg)
        kz = kratio*kxy
        #print(kxy, kz)
        (k_xp, k_yp) = proj( diag([kxy, kxy, kz]),
                                 rot(pi/180*(90-th), 'y'))
        zrow.append(kmeas(k_xp, k_yp, q, t)/kxy)
    za.append(zrow)
za = array(za, dtype='float64')
(xa, ya) = meshgrid(xa, ya)

###
### PLOTTING
###


axes.scatter(xn, yn, zn, c='k', marker='o')
axes.plot_wireframe(yg, xg, zg, rstride=1,
                              cstride=1).set_color('#AAAAAA')
axes.plot_wireframe(ya, xa, za, rstride=1,
                              cstride=1).set_color('#0088AA')

#axes.set_xlabel(headers[0])
#axes.set_ylabel(headers[1])
#axes.set_zlabel(headers[2])

plt.show()

