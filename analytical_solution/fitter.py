# A port of fitter.m from anisotropy_fea to python/numpy
from numpy import log, pi, polyfit
from numpy import corrcoef as corr

def fitter(t,T,q,rset=0.999):
    #This trick will work for numpy arrays of t and T
    t = t[t>1]
    T = T[t>1];

    print('Finding linear portion...');    
    for i in range(len(t)):
        r2 = corr(log(t)[i::], T[i::])[0,1]**2
        print(r2)
        if r2 > rset**2 :
            print('''linear fitting to %(numpts)2i points from 
                     t= %(tnot)2.2f to t=%(tfinal)2.2f ...''' % 
                 {'numpts': len(t)-i, 'tnot': t[i], 'tfinal': t[-1]} )
            x = polyfit(log(t)[i::],T[i::], 1)[0];
            break
    return (q)/(4*pi*x);

if __name__=="__main__":
    #Just a dumb test.
    from numpy import arange, exp
    from numpy.random import rand
    t = arange(10)
    T = (1 + (rand(len(t))-0.5)*exp(-1000*t))*exp(t)
    print(fitter(t,T,0.5))
