import numpy as np

''' Load Data from File'''

data = np.genfromtxt('data.txt', delimiter= ',')
print(data)
# [[ 1.  2.  3.  1.  1.  5.  6.  7.  8.  9.  0. 11.  4.  5.]
#  [ 0.  1.  0.  3.  2. 12. 14.  5.  6.  7.  2. 13.  4.  1.]  
#  [ 3. 11. 18.  9.  5.  6.  3.  5.  2.  1.  2.  3.  4.  1.]] 

data = data.astype('int')
print(data)
# [[ 1  2  3  1  1  5  6  7  8  9  0 11  4  5]
#  [ 0  1  0  3  2 12 14  5  6  7  2 13  4  1]
#  [ 3 11 18  9  5  6  3  5  2  1  2  3  4  1]]

''' Boolean Masking and Advanced Indexing'''

print( data > 1 )
# [[False  True  True False False  True  True  True  True  True False  True
#    True  True]
#  [False False False  True  True  True  True  True  True  True  True  True
#    True False]
#  [ True  True  True  True  True  True  True  True  True False  True  True
#    True False]]


data1 = data[data > 8]
print(data1)
# [ 9 11 12 14 13 11 18  9]

data2 = np.any(data>11, axis = 0)
print(data2)
# [False False  True False False  True  True False False False False  True
#  False False]

data2 = np.all(data>11, axis = 0)
print(data2)
# [False False False False False False False False False False False False
#  False False]

data2 = np.any(data>3, axis = 1)
print(data2)
# [ True  True  True]

print((data>5) & (data<10))
# [[False False False False False False  True  True  True  True False False
#   False False]
#  [False False False False False False False False  True  True False False
#   False False]
#  [False False False  True False  True False False False False False False
#   False False]]

# WE can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,3,5]])
# [2 4 6]


