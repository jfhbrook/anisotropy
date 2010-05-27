#!/usr/bin/env python

from matplotlib import pyplot
from numpy import array, arange, hstack, linspace, ones

def kzkx_planar(rt,rk):
    return (rt**2. + 2.*rt + 1.)/(rt**2. + (rk + (1./rk))*rt + 1.)

def kzkx_honeycomb(rt,rk):
    a1 = 6.*rk**2. - 8.*rk + 2.
    a2 = 6.*rk**3. - 10.*rk**2. + 7.*rk - 1.
    a3 = -2.*rk**3. + 5.*rk**2. - 2.*rk
    a4 = -rk**2.

    b1 = 2.*rk**2. - rk
    b2 = 3.*rk**2. - 3.*rk
    b3 = -2.*rk
    b4 = -rk**2.
    return (a1*rt**3. + a2*rt**2. + a3*rt + a4)/(b1*rt**3. + b2*rt**2. + b3*rt + b4)

def plot_planar():
    pyplot.figure()
    rts = hstack( (arange(0,2,0.05),arange(2,16,0.5)) )
    rks = [100., 50.,10.,4.,2.,1.] #[0.01, 0.05, 0.1, 0.25, 0.5, 1.0]
    annotate_text=linspace(-0.05,1.05,len(rks))
    for i, rk in enumerate(rks):
        kzkx=kzkx_planar(rts,rk)
        pyplot.plot(rts,kzkx,'k')
        pyplot.annotate(str(rk),
                        xy=(15.0,kzkx[-1]),
                        xytext=(16.,annotate_text[i]),
                        arrowprops=dict(width=0.1,headwidth=0,facecolor='black', shrink=0.05) )
    pyplot.axis([0,15,0.0,1.1])
    pyplot.title('Planar Geometry')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')
    pyplot.show()

def plot_honeycomb_low_rk():
    pyplot.figure()
    rt_min=0
    rt_max=0.05
    rts = arange(rt_min,rt_max,0.001)
    rks = [0.05,0.04,0.03,0.02,0.01]
    annotate_text=linspace(0.85,2.0,len(rks))
    for i, rk in enumerate(rks):
        kzkx=kzkx_honeycomb(rts,rk)
        xpts=[rts[j] for j in xrange(len(kzkx)) if kzkx[j]>1]
        ypts=[kzkx[j] for j in xrange(len(kzkx)) if kzkx[j]>1]
        ypts_tail = ypts[-1]
        pyplot.plot(xpts,ypts,'k')
        pyplot.annotate(str(rk),
                        xy=(rt_max,ypts_tail),
                        xytext=(rt_max+0.001,annotate_text[i]),
                        arrowprops=dict(width=0.1,headwidth=0,facecolor='black', shrink=0.05) )
    pyplot.axis([rt_min,rt_max,0.9,2.0])
    pyplot.title('Honeycomb Geometry, decreasing $r_k$')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')

def plot_honeycomb_high_rk():
    pyplot.figure()
    rts = arange(rt_min,rt_max,0.001)
    rks = [5.,10.,20.,30.,100000.]

    for i, rk in enumerate(rks):
        kzkx=kzkx_honeycomb(rts,rk)
        pyplot.plot(rts,kzkx,'k')
    pyplot.axis([rt_min,rt_max,0.9,2.0])
    pyplot.title('Honeycomb Geometry, increasing $r_k$')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')
    pyplot.show()


if __name__ == "__main__":
    plot_planar()
    #plot_honeycomb_low_rk()
    #plot_honeycomb_high_rk()
