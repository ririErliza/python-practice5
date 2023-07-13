import numpy as np

''' Statistics '''

arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1)
# [[1 2 3]
#  [4 5 6]]

'''min value'''
minVal = np.min(arr1)
print(minVal)
# 1

minVal = np.min(arr1, axis = 1)
print(minVal)
# [1 4] #---giving the min of 1st and 2nd row

'''max value'''
maxVal = np.max(arr1)
print(maxVal)
#6

maxVal = np.max(arr1,axis = 1)
print(maxVal)
#[3 6]

''' Sum '''
sumAr = np.sum(arr1)
print(sumAr)
# 21

sumAr = np.sum(arr1, axis =0)
print(sumAr)
# [5 7 9]

