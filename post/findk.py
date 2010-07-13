from numpy.lib.polynomial import polyder
from scipy.interpolate import lagrange
from numpy import array

def listDerivative(f,x,n,o=5):
    """
    Returns the nth derivative of f with respect to x, 
    where zip(x,f) are datapoints using lagrange
    interpolating polynomials using o points.
    """
    assert(o%2 == 1) #should be odd imo
    derivative=[]
    for i in xrange(len(f)):
        start=i-(o-1)/2
        if start < 0:
            start = 0
        end=start+o
        if end >= len(f):
            end = -1
        spline=lagrange(x[start:end],f[start:end])
        derivative.append(polyder(spline,n)(x[i]))
    return array(derivative)
