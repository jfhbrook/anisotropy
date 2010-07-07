#!/usr/bin/env python

from itertools import cycle
from numpy import linspace

angles=linspace(0,90,15)
hosts=cycle(['hookbill',
             'magpie',
             'mallard',
             'puffin',
             'ruddy',
             'wood'])

domain='arsc.edu'
user='holbrook'

for angle, host in zip(angles,hosts):
    print 'ssh '+'holbrook@'+host+'.arsc.edu comsol matlab -ml -nospash -ml -nodesktop -ml -r "cd scratch/anisotropy/mesh; mesh_generate(\'../data/mesh/\','+str(angle)+'); exit"\n'
 
