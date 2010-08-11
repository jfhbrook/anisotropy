"""
Trying to do something with the not-so-ellipsis
"""

from __future__ import division
from sympy import *

# conductivity matrix
k_11 = Symbol('k__11')
k_12 = Symbol('k__12')
k_13 = Symbol('k__13') #
k_22 = Symbol('k__22')
k_23 = Symbol('k__23') #
k_33 = Symbol('k__33')

# Symmetrical 3x3 matrix K
# K = Matrix([[k_11, k_12, k_13],
#            [k_12, k_22, k_23],
#            [k_13, k_23, k_33]])

K = Matrix([[k_11, 0, 0],
            [0, k_11, 0],
            [0, 0, k_33]])



# Let's parameterize.

theta = Symbol('theta')
phi = Symbol('phi')
phi = 0

#z is now in terms of theta and phi
z_1 = sin(theta)*cos(phi)
z_2 = sin(theta)*sin(phi)
z_3 = cos(theta)

# Some z vector
#z_1 = Symbol('z_1')
#z_2 = Symbol('z_2')
#z_3 = Symbol('z_3')

Z = Matrix(3,1,[z_1,z_2,z_3])

# According to reasoning on paper--comes from dot and cross prod, respectively.
cosz = z_3
sinz = sqrt(z_1**2 + z_2**2)
S = Matrix([[0,  -z_3, z_2],
            [z_3, 0,  -z_1],
            [z_2, z_1,  0 ]])

#rotation matrix
R = Z*Z.T + (eye(3) - Z*Z.T)*cosz + S*sinz

#A-prime, the rotated matrix
Kp = R*K*(R.T)

# Now, supposing we have this rotated matrix,
# let's assume what I did on paper is right

req = cse(Kp[0,0]*Kp[1,1] - Kp[1,2]*Kp[2,1])

#print("req as a function of theta and phi")
printing.print_latex( req )

