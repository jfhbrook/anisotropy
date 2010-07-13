#!/usr/bin/env python
"""
superintendent.py
Gives the workers jobs to do
"""

from numpy import linspace
from itertools import cycle, izip, repeat
from os import system

#Some parameters most convenient to have in python
angles = linspace(0,90,10)
simdir = '$SCRATCH/anisotropy/fea'

#See some other file for the matlab-only options
matlab_opts = '''
'''

#A subset of hosts I have passwordless ssh to
hosts=['hookbill', 'magpie', 'mallard', 'puffin', 'ruddy', 'wood']

#Mapping? :)
problem_sets=dict(zip(hosts,repeat([],6)))
i=0
for (host,a) in izip(cycle(hosts),angles):
    problem_sets[host].append(a)

# I haven't done the string subs here yet.
for host in hosts:
    setup = "ssh %(host)s tar -xzf /archive/u1/uaf/holbrook/fea.tgz -C /scratch/holbrook/" % \
             {'host': host}
    foreman = "ssh %(host)s %(command)s \"%(angles)s\" \n" % \
               {'host': host, 
                'command': '$SCRATCH/fea/foreman.sh',
                'angles': repr(list(angles))}
    system(setup)   # It's my understanding that system 
    system(foreman) # is going to be deprecated. TOO BAD
                    # this is easy
