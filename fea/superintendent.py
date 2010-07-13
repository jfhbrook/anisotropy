#!/usr/bin/env python
"""
superintendent.py
Gives the workers jobs to do
"""

from numpy import linspace
from itertools import cycle, repeat

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
    bash_cmd = "ssh %(host)s %(command)s %(angles)s" % \
               {'host': host, 
                'command': '$SCRATCH/anisotropy/foreman.sh',
                'angles': repr(angles)}
