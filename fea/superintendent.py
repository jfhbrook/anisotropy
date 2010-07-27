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
angles = list(linspace(0,90,10))

#A subset of hosts I have passwordless ssh to
hosts=['mallard', 'poseidon', 'puffin', 'ruddy', 'wood', 'zeus']

#hosts=['poseidon']

def axemurderer():
    for host in hosts:
        system('ssh %(host)s pkill MATLAB' % {"host": host})



if __name__=="__main__":
    #Mapping? :)
    problem_sets=dict(zip(hosts,([] for i in xrange(6))))
    for (host,a) in izip(cycle(hosts),angles):
        problem_sets[host]+=[a]

    # I haven't done the string subs here yet.
    for host in hosts:
        setup = "ssh %(host)s '. ~/.profile && tar -xzf /archive/u1/uaf/holbrook/fea.tgz -C /scratch/holbrook/'" % \
                 {'host': host}
        foreman = "ssh %(host)s %(command)s %(angles)s &" % \
                   {'host': host, 
                    'command': '/scratch/holbrook/fea/foreman.sh',
                    'angles': sub('[ \t]+', '', repr(list(problem_sets[host])))}
        system(setup)   # It's my understanding that system 
        #print setup
        system(foreman) # is going to be deprecated. TOO BAD
        #print foreman                # this is easy
        #print host
        #print problem_sets[host]
