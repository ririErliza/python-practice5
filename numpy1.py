import numpy as np

'''
NumPy is used to work with arrays. 
The array object in NumPy is called ndarray
'''

print(np.__version__)
#1.25.0




'''            Creating Arrays                  '''
'''---------------------------------------------'''

# array()
arr = np.array([1,2,3,4])
print(arr)
#[1 2 3 4]

# o create an ndarray, we can pass a list, tuple or
#  any array-like object into the array() method,
#  and it will be converted into an ndarray

arr1 = np.array((1,1,3,3)) #this is tuple
print(arr1)
#[1 1 3 3]


# 0-D Array
arr2 = np.array(32)
print(arr2)
# 32

# 1-D Array
arr3 = np.array([6,5,6,5])
print(arr3)
# [6 5 6 5]


#2-D Array
arr4=np.array([[1,2,3], [3,2,1]])
print(arr4)
#[[1 2 3]
# [3 2 1]]

#3-D Array
arr5 = np.array([[[1,2,3], [4,5,6]],[[3,2,1],[4,5,6]]])
print(arr5)

# [[[1 2 3]
#   [4 5 6]]

#  [[3 2 1]
#   [4 5 6]]]

#Check number of dimension
print(arr5.ndim)
# 3


#Higher dimensional array
arr6 =np.array([1,2,3,4], ndmin=5)
print(arr6)
#[[[[[1 2 3 4]]]]]

'''            Array Indexing                   '''
'''---------------------------------------------'''

#access array element

arrA = np.array([4,5,6,7])
print(arrA[0]) 
#4

print(arrA[2] + arrA[3])
#13


#Access 2-D Arrays

arrB = np.array([[1,2,3,4,5], [1,1,1,4,5]])
print("2nd element on first row: ",arrB[0,1])
#2nd element on first row:  2

print('5th element on 2nd row: ', arrB[1, 4])
#5th element on 2nd row:  5


#Access 3-D Arrays
arrC = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])