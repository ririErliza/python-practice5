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

# square root
z = np.sqrt(x)
print(z)
# [[1.         1.41421356]
#  [1.73205081 2.        ]]

# dot()
v = np.array([1,2])
w = np.array([2,2])
print(v.dot(w)) # 6
# 1x2 + 2x2 = 6

v = np.array([1,2,1])
w = np.array([2,2,1])
print(v.dot(w)) # 7

#this dot() function will give us scalar value 
# only if we operate same dimension arrays

''' reverse the matrix '''
print(x)
# [[1 2]
#  [3 4]]

print(x.T)
# [[1 3]
#  [2 4]]

print(np.sum(x)) # 10

print(np.sum(x, axis = 0))
# [4 6]

print(np.sum(x, axis = 1))
# [3 7]

print(x-2)
# [[-1  0]
#  [ 1  2]]

print(x+2)
# [[3 4]
#  [5 6]]

print(x*2)
# [[2 4]
#  [6 8]]

print(x/2)
# [[0.5 1. ]
#  [1.5 2. ]]

print(y**2)
# [[25 36]
#  [49 64]]

''' sin cos tan'''
c = np.array(([[45,30],[60,90]]))

sinC = np.sin(c)
print(sinC)
# [[ 0.85090352 -0.98803162]
#  [-0.30481062  0.89399666]]

cosC = np.cos(c)
print(cosC)
# [[ 0.52532199  0.15425145]
#  [-0.95241298 -0.44807362]]

tanC = np.tan(c)
print(tanC)
# [[ 1.61977519 -6.4053312 ]
#  [ 0.32004039 -1.99520041]]

