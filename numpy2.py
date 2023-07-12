import numpy as np

x = np.zeros((2,3))
print(x)

# [[0. 0. 0.]
#  [0. 0. 0.]]

x = np.zeros((2,3), dtype=int)
print(x)
# [[0 0 0]
#  [0 0 0]]

x = np.ones((4,5))
print(x)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

x = np.ones((2,4,3))
print(x)
# [[[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]

#  [[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]]


''' RANGE '''

x = np.arange(10)
print(x)
# [0 1 2 3 4 5 6 7 8 9]


x = np.arange(5,10)
print(x)
# [5 6 7 8 9]


x = np.arange(1,11,2) #step of 2
print(x)
# [1 3 5 7 9]


x = np.arange(2,3, 0.1)
print(x)
# [2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9]

