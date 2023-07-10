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
print('3rd element on 2nd array of 1st array: ', arrC[0, 1, 2])
#3rd element on 2nd array of 1st array:  6

#Negative Indexing

arrD = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arrD[1, -1])
#Last element from 2nd dim:  10

'''            Array Slicing                    '''
'''---------------------------------------------'''

# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1


array1 =  np.array([1, 2, 3, 4, 5, 6, 7])

print("elements from index 1 to index 5: ",
       array1[1:5])
#elements from index 1 to index 5:  [2 3 4 5]
#The result includes the start index, but excludes the end index.

print("elements from index index 4 to the end: ",
       array1[4:])
#elements from index index 4 to the end:  [5 6 7]


print("elements from the index 3 from the end to index 1: ",
       array1[-3:-1])
# elements from the index 3 from the end to index 1:  [5 6]


#STEP

print(array1[1:6:2])
#return every other element from index 1 to index 6
#[2 4 6]

print(array1[::2])
#Return every other element from the entire array
#[1 3 5 7]