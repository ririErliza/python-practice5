import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
# [[1 2 3 4]
#  [5 6 7 8]]
print(before.shape)
# (2, 4)

after = before.reshape((4,2))
print(after)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

after = before.reshape((2,2,2))
print(after)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]


''' Vertical Stack'''

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

verA = np.vstack((v1,v2,v1,v2))
print(verA)
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]]


''' Horizontal Stack'''

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

horA = np.hstack((h1,h2))
print(horA)
# [[1. 1. 1. 1. 0. 0.]
#  [1. 1. 1. 1. 0. 0.]]
