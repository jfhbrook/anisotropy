#!/usr/bin/env python

from numpy import array,dot

class ortho_projection:
    def of(self,x):
        try:
            return self._proj(x,self._onto)
        except(AttributeError):
            new=self
            new._of=x
            return new
    def onto(self,x):
        try:
            return self._proj(self._of,x)
        except(AttributeError):
            new=self
            new._onto=x
            return new
    def _proj(self,of,onto):
        if len(onto.shape) > 1:
            # Lotsa transposes.
            return sum(array([(dot(of,v)/dot(v,v))*v for v in onto.T]).T)
        else:
            return (dot(of,onto)/dot(onto,onto))*onto

if __name__=="__main__":
    e1=array([1,0,0]).T
    v=array([3,4,5]).T

    print "Projecting "+str(v)+" onto "+str(e1)+":"

    # Look Ma!
    print ortho_projection().of(v).onto(e1)
