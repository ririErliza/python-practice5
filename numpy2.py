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


''' linspace() '''
x = np.linspace(1.,4., 6)
print(x)
# [1.  1.6 2.2 2.8 3.4 4. ]
# starting from one to 4 but there are 6 elements
#  in the array, numpy will do the calculation


''' full() '''
x = np.full((2,2), 8)
print(x)
# [[8 8]
#  [8 8]]


''' eye() '''
x=np.eye(3)
print(x)
#[[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

''' random.random() '''

x = np.random.random((3,4))
print(x)
# [[0.38135397 0.23462828 0.85515616 0.16874389]
#  [0.05260225 0.39708288 0.16619698 0.81681055]
#  [0.9883331  0.20358459 0.65895373 0.6359358 ]]

#Convert Floats to Integers (Rounded Down)
intX = x.astype(int)
print(intX)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

# Convert Floats to Integers (Rounded to Nearest Integer)
intX = (np.rint(x).astype(int))
print(intX)
# [[0 1 0 1]
#  [0 0 0 0]
#  [1 1 0 1]]

