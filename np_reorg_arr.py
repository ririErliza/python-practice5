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
