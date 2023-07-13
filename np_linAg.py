import numpy as np

#Linear ALgebra

#Matrix multiplication

a = np.ones((2,3))
print(a)
# [[1. 1. 1.]
#  [1. 1. 1.]]

b = np.full((3,2),2)
print(b)
# [[2 2]
#  [2 2]
#  [2 2]]

z = np.matmul(a,b)
print(z)
# [[6. 6.]
#  [6. 6.]]


# Find the determinant
c = np.identity(3)
print(c)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

y = np.linalg.det(c)
print(y)
# 1.0



