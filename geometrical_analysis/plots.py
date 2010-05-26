#!/usr/bin/env python

def kzkx_planar(rt,rk):
    return (rt**2. + 2.*rt + 1.)/(rt**2. + (rk + (1./rk))*rt + 1.)

def kzkx_honeycomb(rt,rk):
    a1 = 6.*rk**2. - 5.*rk - 1.
    a2 = 6.*rk**3. - 10.*rk**2. + 5.*rk - 1.
    a3 = 2.*rk**3. - 4.*rk**2. + 2.*rk
    a4 = rk**2.
    a5 = 2.*rk**2. - rk
    a6 = rk**2. - 2.*rk
    a7 = 4.*rk**2. + rk
    a8 = a4
    return (2./3.)*(a1*rt**3. + a2*rt**2. - a3*rt -a4)/(a5*rt**3. + a6*rt**2. - a7*rt -a8)

if __name__ == "__main__":
    from matplotlib import pyplot
    from numpy import array, arange, hstack

    rts = hstack( (arange(0,2,0.05),arange(2,15,0.5)) )
    planar_plot = pyplot.plot(rts,kzkx_planar(rts,1))
    pyplot.show()
