from math import pi
from numpy import *
from functools import reduce
import csv
import tablib
import re
import matplotlib.pyplot as plt

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

# csv.reader and tablib aren't smart enough to read in numbers as numbers.
# Therefore, I map this over the strings in the rows spat out by csv.reader.
def str2num(string):

    if re.match('^-?\d*\.\d*$', string):
        return float(string)
    elif re.match('^-?\d+$', string):
        return int(string)
    else:
        return string


def import_numerical(filename):

    data = tablib.Dataset()
    for row in csv.reader(open(filename, 'r')):
        data.append( map(str2num, row) )

    data.headers = ( 'angle', 'kz/kxy', 'kmeas/kxy' )
    return data


def tab_filter(data, header, testfxn):
    new_data = [];
    for (i, pt) in enumerate(data[header]):
        if testfxn(pt):
            new_data.append(data[i])
    return tablib.Dataset(*new_data, headers=data.headers)


def unique(col):
    return list(set(col))

def getKmeas(k_xy, k_z, th):
    q = 0.5
    t = hstack(( logspace(0.1,1.0,15),
                 logspace(1.0,3.0,15) ))
    (k_xp, k_yp) = proj( diag([k_xy, k_xy, k_z]),
                         rot(pi/180*(90-th), 'y'))

    #print k_xp, k_yp
    return kmeas(k_xp, k_yp, q, t)/k_xy


if __name__=="__main__":

    fea = import_numerical('./data_fea.csv')

    """
    print "By-Angle Frequencies:"
    for theta in sorted(unique(fea['angle'])):
        print str(theta) + ': ' + str(len([t for t in fea['angle'] if t == theta]))
    """

    angle_0 = tab_filter(fea, 'angle', lambda t: t == 0)
    angle_30 = tab_filter(fea, 'angle', lambda t: t == 30)
    angle_60 = tab_filter(fea, 'angle', lambda t: t == 60)
    angle_90 = tab_filter(fea, 'angle', lambda t: t == 90)

    byAngle = {0: angle_0, 30: angle_30, 60: angle_60, 90: angle_90}


    #zero angle only
    """
    anal_kratios_0 = linspace(0.2, 2.0, 20)
    anal_kmeas_0 = map(lambda k: getKmeas(1, k, 0), list(anal_kratios_0))
    
    plt.plot(angle_0['kz/kxy'], angle_0['kmeas/kxy'], 'o')
    plt.plot([0.2, 2.0], [0.2, 2.0], '--')
    #plt.plot(anal_kratios_0, anal_kmeas_0) Simultaneous with x = y line o__o
    plt.xlabel(r'$k_z/k_{xy}$')
    plt.ylabel(r'$k_{\textrm{meas}}/k_{xy}$')
    plt.show()

    #all, by-angle
    angles = [0, 30, 60, 90]
    anal_kratios = linspace(0.2, 2.0, 20)
    anal_kmeas = [map(lambda k: getKmeas(1, k, a), list(anal_kratios)) for a in angles]

    for (i, a) in enumerate(angles):
        angle_set = byAngle[a]
        (kz,kmeas) = zip(*sorted( zip(angle_set['kz/kxy'], angle_set['kmeas/kxy']),
                                  key=lambda tup: tup[0]))
        #print kz
        plt.plot(kz, kmeas, 'o--', color='k')
        plt.plot(anal_kratios, anal_kmeas[i], 'b')
    plt.xlabel(r'$k_z/k_{xy}$')
    plt.ylabel(r'$k/k_{xy}$')
    plt.show()
    """
