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


#Slicing 2-D Arrays
print("----2D Slicing----")

arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2D[1, 1:4])
#From the second element, slice elements from index
#  1 to index 4 (not included)
#[7 8 9]

print(arr2D[0:2, 2])
#From both elements, return index 2
#[3 8]

print(arr2D[0:2, 1:4])
#From both elements, slice index 1 to index 4 (not included),
#  this will return a 2-D array
# [[2 3 4]
#  [7 8 9]]


'''              Data Types                     '''
'''---------------------------------------------'''

#NumPy has some extra data types, and refer to data types
#  with one character
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

print(arrA.dtype) 
#int32

arrS = np.array(["apple","banana","melon"])
print(arrS.dtype)
# <U6

#Creating Arrays With a Defined Data Type
arr7 = np.array([1, 2, 3, 4], dtype='S')

print(arr7)
# [b'1' b'2' b'3' b'4']
print(arr7.dtype)
# |S1

#Create an array with data type 4 bytes integer
arr8 = np.array([1, 2, 3, 4], dtype='i4')

print(arr8)
#[1 2 3 4]
print(arr8.dtype)
#int32

# ValueError: In Python ValueError is raised when the type
#  of passed argument to a function is unexpected/incorrect.
# A non integer string like 'a' can not be converted to integer
#  (will raise an error)



#Converting Data Type on Existing Arrays


# astype()
# this function creates a copy of the array, 
# and allows to specify the data type as a parameter

arr9 = np.array([1.1, 2.1, 3.1])

newarr = arr9.astype('i')

print("new integer array", newarr)
print(newarr.dtype)

#new array [1 2 3]
#int32

newarr = arr.astype(bool)

print("new boolean array",newarr)
print(newarr.dtype)

# new boolean array [ True  True  True  True]
# bool

'''             Copy vs View                    '''
'''---------------------------------------------'''


print(arr8)
# [1 2 3 4]


x = arr8.copy()
arr8[0] = 42

print(arr8)
print(x)


# [42  2  3  4]
# [1 2 3 4]          # The copy SHOULD NOT be affected by the
                     #  changes made to the original array.



y = arr8.view()
arr8[0] = 33

print(arr8)
print(y)

# [33  2  3  4]
# [33  2  3  4]      #The view SHOULD be affected by
                     # the changes made to the original array.



z = arr8.view()
z[0] = 21

print(arr8)
print(z)

# [21  2  3  4]
# [21  2  3  4]      # The original array SHOULD be affected
                     #  by the changes made to the view.


# Check if Array Owns its Data

print(x.base) #None
print(y.base) #[21  2  3  4]

# The copy returns None.
# The view returns the original array.

print("----------------------------------------")


'''                  Shape                      '''
'''---------------------------------------------'''
# The shape of an array is the number of elements
#  in each dimension.


#shape of a 2-D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# (2, 4)
#which means that the array has 2 dimensions,
#where the first dimension has 2 elements and the second has 4.

# ndmin 5d array
arr = np.array([1, 1, 3,5], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
# [[[[[1 2 3 4]]]]]
# shape of array : (1, 1, 1, 1, 4)

'''                Re-Shape                     '''
'''---------------------------------------------'''
#Reshaping means changing the shape of an array.


arrE = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


#Reshape From 1-D to 2-D
newarr = arrE.reshape(3, 4)

print(newarr)

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# The outermost dimension will have 3 arrays, each with 4 elements

#Reshape From 1-D to 3-D
newarr = arrE.reshape(2, 2, 3)
print(newarr)

# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

#The outermost dimension will have 2 arrays that contains 2 arrays,
#  each with 3 elements



# note :
# We can reshape an 8 elements 1D array into 4 elements in
#  2 rows 2D array but we cannot reshape it into a 3 elements
#  3 rows 2D array as that would require 3x3 = 9 elements


#Unknown Dimension
arrG = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr1 = arrG.reshape(2, 2, -1)
print(newarr1)

# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

#Flattening the arrays
arrH = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arrH.reshape(-1)

print(newarr)
#[1 2 3 4 5 6]

'''                Iterating                    '''
'''---------------------------------------------'''
#Iterating means going through elements one by one

for x in arrA:
  print(x)
# 4
# 5
# 6
# 7

#Iterating 2-D Arrays
print("Array 2d", arr2D)
for x in arr2D:
  print(x)

# [1 2 3 4 5]
# [ 6  7  8  9 10]

#To return the actual values, the scalars,
#  we have to iterate the arrays in each dimension

for x in arr2D:
  for y in x:
    print(y)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#Iterating 3-D Arrays
print(arr5)

for x in arr5:
  print(x)

# [[1 2 3]
#  [4 5 6]]
# [[3 2 1]
#  [4 5 6]]

for x in arr5:
  for y in x:
    for z in y:
      print(z)

# 1
# 2
# 3
# 4
# 5
# 6
# 3
# 2
# 1
# 4
# 5
# 6



'''                   Join                      '''
'''---------------------------------------------'''

arrI = np.array([1,2,2])
arrJ = np.array([2,3,3])

joinArr = np.concatenate((arrI,arrJ))

print(joinArr)
#[1 2 2 2 3 3]

#Join two 2-D arrays along rows (axis=1)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
#[[1 2 5 6]
#[3 4 7 8]]

#Stack Functions
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
# [[1 4]
#  [2 5]
#  [3 6]]

#Stacking Along Rows
arrK = np.array([1, 2, 3])

arrL = np.array([4, 5, 6])

arrJoin1 = np.hstack((arrK, arrL))

print(arrJoin1)
#[1 2 3 4 5 6]


#Stacking Along Columns

arrJoin2 = np.vstack((arrK, arrL))

print(arrJoin2)
# [[1 2 3]
#  [4 5 6]]

#Stacking Along Height (depth)
arrJoin3 = np.dstack((arrK, arrL))

print(arrJoin3)

# [[[1 4]
#   [2 5]
#   [3 6]]]

'''                  Split                      '''
'''---------------------------------------------'''
#array_split()

arrN = np.array([1, 2, 3, 4, 5, 6])
splitArr = np.array_split(arrN, 3)

print(splitArr)
#[array([1, 2]), array([3, 4]), array([5, 6])]


#If the array has less elements than required,
#  it will adjust from the end accordingly.
newarr = np.array_split(arrN, 4)

print(newarr)
#[array([1, 2]), array([3, 4]), array([5]), array([6])]


#Access the splitted arrays
newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
# [[1 4]]
# [[2 5]]
# [[3 6]]

#Splitting 2-D Arrays
arrO = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

split2D = np.array_split(arrO, 3)
print(split2D)

# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]


#split 2-D arrays that contains 3 elements
arrP = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newSplitArr = np.array_split(arrP, 3)

print(newSplitArr)
# [array([[1, 2, 3],
#        [4, 5, 6]]), array([[ 7,  8,  9],
#        [10, 11, 12]]), array([[13, 14, 15],
#        [16, 17, 18]])]



'''                  Search                     '''
'''---------------------------------------------'''
#where() method

arrT = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arrT == 4)

print("where? at: ",x)
#where? at:  (array([3, 5, 6], dtype=int64),)
# the value 4 is present at index 3, 5, and 6


a = np.where(arrT%2 == 0)
print("a: ", a)
#a:  (array([1, 3, 5, 6], dtype=int64),)


#searchsorted()

arrU = np.array([6, 7, 8, 9])
b = np.searchsorted(arrU, 7)

print("b:", b)
#b: 1




'''                   Sort                      '''
'''---------------------------------------------'''
#sort()
# that will sort a specified array

arrV = np.array([3, 2, 0, 1])

print(np.sort(arrV))
#[0 1 2 3]

# alphabetically
arrW = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arrW))
#['apple' 'banana' 'cherry']

#Sort a 2-D array
arrX = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arrX))
# [[2 3 4]
#  [0 1 5]]

'''                  Filter                     '''
'''---------------------------------------------'''

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
# [False False  True  True]
# [43 44]


filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
# [False  True False  True]
# [42 44]

'''               Append & Delete               '''
'''---------------------------------------------'''


arrQ = np.array(["jello", 1, True])
print(arrQ) #['jello' '1' 'True']
print(arrQ.ndim) #1
print(arrQ.data) #<memory at 0x0000024766EC5D80>

#append
arrq1= np.append(arrQ[0],99)
print(arrq1) #['jello' '99']

print(arrQ) #['jello' '1' 'True']

arrq2 = np.append(arrQ, 99)
print(arrq2) #['jello' '1' 'True' '99']

arrq2 = np.delete(arrq2,1)
print(arrq2) #['jello' 'True' '99']




