"""
Playing with the Heat Equation using sympy
"""
from __future__ import division
from sympy import *

# Mad props
rho = Symbol('rho')
cp = Symbol('Cp')

# conductivity matrix
k_11 = Symbol('k_11')
k_12 = Symbol('k_12')
k_13 = Symbol('k_13') #
k_22 = Symbol('k_22')
k_23 = Symbol('k_23') #
k_33 = Symbol('k_33')

# Symmetrical 3x3 matrix K
K = Matrix([[k_11, k_12, k_13],
            [k_12, k_22, k_23],
            [k_13, k_23, k_33]])

# Coordinates
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

x0 = Symbol('x0')
y0 = Symbol('y0')
z0 = Symbol('z0')


#Scaling factors
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

A = Symbol('A')

#thyme
t = Symbol('t')

#Proposed solution
exppart = exp(-(1/(4*t))*( ((x-x0)/a)**2 + ((y-y0)/b)**2 + ((z-z0)/c)**2 ))
T = A/(t**(3/2)) * exppart

f = Function('f')

delT = Matrix(3,1,[T.diff(x),T.diff(y),T.diff(z)])
f = K * delT

print('lhs:')
lhs = T.diff(t)/cp/rho
lhs = powsimp(collect(lhs,exppart)/exppart)
pprint(lhs)

print('rhs:')
rhs = f[0].diff(x)+f[1].diff(y)+f[2].diff(z)
rhs = powsimp(collect(rhs,exppart)/exppart)
pprint(rhs)

solve(lhs-rhs,[a,b,c,A])
