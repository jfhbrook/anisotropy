#!/usr/bin/env python

from matplotlib import pyplot
from numpy import array, linspace, ones

#n=t_t/(t_1+t_2)
def kxk2_planar(n,rk):
    return (rk-1)*n + 1

def kzk2_planar(n,rk):
    return ((1./rk)*n + 1.)**(-1.)

def plot_planar():
    pyplot.figure()
    rts = linspace(0,1,60)
    rks = [100., 50.,10.,4.,2.,1.]
    rks = rks+[1./x for x in reversed(rks)]
    #annotate_text=linspace(-0.05,1.05,len(rks))
    for i, rk in enumerate(rks):
        kxk2 = kxk2_planar(rts,rk)
        pyplot.plot(rts,kxk2,'k')
    pyplot.axis([0,1,0,2])
    pyplot.title('Planar Geometry')
    pyplot.xlabel(r'$n$')
    pyplot.ylabel(r'$ k_x $ / $ k_2 $')

    pyplot.figure()
    for i, rk in enumerate(rks):
        kzk2 = kzk2_planar(rts,rk)
        pyplot.plot(rts,kzk2,'r')
    pyplot.axis([0,1,0,2])
    pyplot.title('Planar Geometry')
    pyplot.xlabel(r'$n$')
    pyplot.ylabel(r'$ k_z $ / $ k_2 $')
    pyplot.show()

if __name__ == "__main__":
    plot_planar()
