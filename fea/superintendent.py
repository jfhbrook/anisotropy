#!/usr/bin/env python
"""
superintendent.py
Gives the workers jobs to do
"""

from numpy import linspace
from itertools import cycle, izip, repeat
from os import system
from re import sub

#Some parameters most convenient to have in python
angles = linspace(0,90,10)

#A subset of hosts I have passwordless ssh to
hosts=['mallard', 'poseidon', 'puffin', 'ruddy', 'wood', 'zeuss']

#Mapping? :)
problem_sets=dict(zip(hosts,repeat([],6)))
i=0
for (host,a) in izip(cycle(hosts),angles):
    problem_sets[host].append(a)

# I haven't done the string subs here yet.
for host in hosts:
    setup = "ssh %(host)s tar -xzf /archive/u1/uaf/holbrook/fea.tgz -C /scratch/holbrook/" % \
             {'host': host}
    foreman = "ssh %(host)s %(command)s %(angles)s &" % \
               {'host': host, 
                'command': '/scratch/holbrook/fea/foreman.sh',
                'angles': sub('[ \t]+', '', repr(list(angles)))}
    system(setup)   # It's my understanding that system 
    system(foreman) # is going to be deprecated. TOO BAD
    #print foreman                # this is easy
