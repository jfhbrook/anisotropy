from os import system

#A subset of hosts I have passwordless ssh to
hosts=['mallard', 'poseidon', 'puffin', 'ruddy', 'wood', 'zeus']

#hosts=['poseidon']

for host in hosts:
    system('ssh %(host)s pkill MATLAB' % {"host": host})

