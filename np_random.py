import numpy as np
from numpy import random

# number = np.random.randint(100)
number = np.random.randint(100, size =(2,3,4))
print(number)
# [[[ 1 59 26 71]
#   [33 75 67 23]
#   [92 93 86 55]]

#  [[55 27 23 97]
#   [22 52 15 86]
#   [87 78  8 94]]]

number = np.random.randint(90, 100, size =(2,3,4))
print(number)
# [[[94 96 95 95]
#   [99 91 94 93]
#   [92 91 97 99]]

#  [[90 92 98 92]
#   [94 95 92 97]
#   [92 98 99 93]]]

headOrTail = np.random.binomial(10, p=0.5, size=(5,10))
print(headOrTail)
# [[2 6 7 6 5 4 4 8 3 6]
#  [7 8 6 6 4 7 5 2 5 4]
#  [3 6 7 5 5 7 6 5 8 3]
#  [6 6 5 5 9 5 7 4 5 3]
#  [2 6 5 5 9 8 8 5 5 3]]

students = np.random.normal(loc=170, scale=15, size =(5,10))
print(students)

chooseIt = np.random.choice([10,20,30,40,50])
print(chooseIt)

chooseIt = np.random.choice([10,20,30,40,50], size=(3,4))
print(chooseIt)
# [[30 10 20 30]
#  [10 40 40 20]
#  [40 30 50 40]]

''' -------------------------------------------------------------- '''
''' -------------------------------------------------------------- '''
''' ------------------------From W3School------------------------- '''
''' -------------------------------------------------------------- '''
''' -------------------------------------------------------------- '''

#generate random number
x = random.randint(10)
print(x) #9

#Generate Random Float
x = random.rand()
print(x) #0.08409344022158316

#Generate Random Array
x = random.randint(50, size=(5))
print(x)
#[42 38 10 45  5]
# Generate a 1-D array containing 5 random integers from 0 to 100

x = random.randint(100, size=(2, 3))
print(x)
# [35 21 27 29 11]
# [[95 96 42]
#  [58 77 91]]
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

''' Floats '''
# rand() method
x = random.rand(5)
print(x)
#[0.443903   0.74545327 0.87234916 0.35303884 0.86815543]

x = random.rand(3, 3)
print(x)
# [[0.48647312 0.16432578 0.17854357]
#  [0.72939354 0.40701167 0.41303907]
#  [0.99806604 0.78334237 0.30555224]]

''' Generate Random Number From Array '''
#choice()
x = random.choice([3, 5, 7, 9])
print(x)
# 5

x = random.choice([3, 5, 7, 9], size=(3, 4))
print(x)
# [[7 3 3 9]
#  [9 7 5 3]
#  [9 7 5 3]]


'''-------------------------------------------'''
'''             Random Distribution           '''
'''-------------------------------------------'''

# Generate a 1-D array containing 20 values, where
#  each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

rd1 = random.choice([3,5,7,9], p=[0.1,0.1,0.5,0.3], size=(20))
print(rd1)
# [9 7 9 7 7 7 9 7 9 3 5 7 7 7 7 7 3 9 9 7]

#The sum of all probability numbers (p) should be 1.

rd2=random.choice([3,5,7,9], p=[0.1,0.1,0.5,0.3], size=(3,4))
print(rd2)
# [[9 7 9 7]
#  [7 7 3 9]
#  [9 7 7 7]]


'''-------------------------------------------'''
'''              Random Permutation           '''
'''-------------------------------------------'''
#A permutation refers to an arrangement of elements.
#  e.g. [3, 2, 1] is a permutation of [1, 2, 3] and
#  vice-versa.

# Shuffling Arrays
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)
# [4 5 2 3 1]
# The shuffle() method makes changes to the original
# array.

'''Generating Permutation of Arrays'''
arr1= np.array([11,12,13,14])
print(random.permutation(arr1))




'''-------------------------------------------'''
'''                Seaborn Module             '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''             Normal Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''           Binomial Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''            Poisson Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''            Uniform Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''           Logistic Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''         Multinomial Distribution          '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''         Exponential Distribution          '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''          Chi Square Distribution          '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''           Rayleigh Distribution           '''
'''-------------------------------------------'''


'''-------------------------------------------'''
'''            Pareto Distribution            '''
'''-------------------------------------------'''


