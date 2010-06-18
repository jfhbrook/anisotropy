#!/usr/bin/env python

from numpy import array

def iter_ij(A):
    """
    returns i,j
    """
    return reduce(lambda x,y: x+y, ([[(i,j) for j in xrange(3)] for i in xrange(3)]))

if __name__=="__main__":
    A=array(range(9)).reshape(3,3)
    print A
    print array([A[i,j] for (i,j) in iter_ij(A)]).reshape(A.shape)
