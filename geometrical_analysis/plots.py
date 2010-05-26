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
    from numpy import array, arange, hstack, linspace, ones

    rts = hstack( (arange(0,2,0.05),arange(2,16,0.5)) )
    rks = [100., 50.,10.,4.,2.,1.] #[0.01, 0.05, 0.1, 0.25, 0.5, 1.0]
    annotate_text=linspace(-0.05,1.05,len(rks))
    for i, rk in enumerate(rks):
        kzkx=kzkx_planar(rts,rk)
        pyplot.plot(rts,kzkx,'k')
        pyplot.annotate(str(rk),
                        xy=(14.5,kzkx[-1]),
                        xytext=(16.,annotate_text[i]),
                        arrowprops=dict(width=0.1,headwidth=0,facecolor='black', shrink=0.05) )
    pyplot.axis([0,15,0.0,1.1])
    pyplot.title('Planar Geometry')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')
    #pyplot.show()

    pyplot.figure()

    rts = arange(0,0.2,0.001)
    # r_k < 1 situations
    rks = [0.01,0.05, 0.1, 0.3, 0.5,1.0]
    # r_k > 1 situations
    #rks = [1.,2.,3.,5.,7.,10.,20.,30.,100000.]

    for i, rk in enumerate(rks):
        kzkx=kzkx_honeycomb(rts,rk)
        pyplot.plot(rts,kzkx,'k')
    pyplot.axis([0,0.2,0.0,2.0])
    pyplot.title('Honeycomb Geometry')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')

    pyplot.figure()
    rts = arange(0,0.2,0.001)
    # r_k < 1 situations
    #rks = [0.01,0.05, 0.1, 0.3, 0.5,1.0]
    # r_k > 1 situations
    rks = [1.,2.,3.,5.,7.,10.,20.,30.,100000.]

    for i, rk in enumerate(rks):
        kzkx=kzkx_honeycomb(rts,rk)
        pyplot.plot(rts,kzkx,'k')
    pyplot.axis([0,0.2,0.0,2.0])
    pyplot.title('Honeycomb Geometry')
    pyplot.xlabel(r'$r_t$')
    pyplot.ylabel(r'$ k_z $ / $ k_x $')
    pyplot.show()

