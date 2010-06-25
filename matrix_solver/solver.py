#!/usr/bin/env python

from magic_square import magic
from math import cos, pi
from numpy import array, dot, eye
#from numpy import vstack
from scipy.linalg import norm
#from scipy.optimize.minpack import leastsq

def project(x,w):
    """orthogonal projection of x onto w."""
    if len(w.shape) > 1:
        return [(dot(x,v)/dot(v,v))*v for v in w.T]
    else:
        return (dot(x,w)/dot(w,w))*w

def solver(X):
    """Takes a 3x3 matrix of column vectors X and solves for the K matrix."""
    pass
    #return leastsq(lambda K: (1./X).T*K*(1./X) - 1, eye(3)) #very incorrect
    def fxn(X):
        #X being a matrix with column vectors
        # when returns 0, v'Kv=k where v is x/norm(x), 
        # and k is norm(x) (alternately, x'Kx=|x|^(3/2))
        return array([dot(x/norm(x),dot(K,x/norm(x))) for x in X.T])-array([norm(x) for x in X.T])

def unsolver(K,Xdirs):
    """Takes a 3x3 K matrix and a 3x3 matrix of column direction vectors X and returns component.
    Implementation of euler-cauchy action might be faulty. I need to find a pen to check."""

    return array([project((K*Xdirs/norm(Xdirs)).T, x) for x in Xdirs.T]).T

class mag_and_dir:
    """
    Describe a 3-d vector in terms of its length and direction angles.
    """
    def __init__(self,l=1.0,alpha=1.0,beta=0.0,gamma=0.0):
        self.l=l
        self.alpha=alpha
        self.beta=beta
        self.gamma=gamma
    def __len__(self):
        return 2
    def __getitem__(self,key):
        if key==0:
            return self.l
        if key==1:
            return (self.alpha,self.beta,self.gamma)
    def __rmul__(self,a):
        new=self
        new.l=a*self.l
        return new
    def toarray(self):
        return array(map(lambda x: self.l*cos(x), self[1]))
        

if __name__=="__main__":

    #e1=mag_and_dir(1,0,pi/2.,pi/2.)
    #e2=mag_and_dir(1,pi/2.,0,pi/2.)
    #e3=mag_and_dir(1,pi/2.,pi/2.,0)

    print "K:"
    K=magic(3).T+magic(3)
    print K

    print "Components on std. basis:"
    X=unsolver(K,eye(3))
    print X

    #print "Solve for K using ellipse method:"
    #print solver(X)

    #print array([e1.toarray(),e2.toarray(),e3.toarray()])
