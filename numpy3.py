import numpy as np


''' ARRAY MATH'''

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x+y)
# [[ 6  8]
#  [10 12]]

z = np.add(x,y)
print(z)
# [[ 6  8]
#  [10 12]]

print(x-y)
# [[-4 -4]
#  [-4 -4]]
print(x*y)
# [[ 5 12]
#  [21 32]]
print(x/y)
# [[0.2        0.33333333]
#  [0.42857143 0.5       ]]