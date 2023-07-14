import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

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
#[14 11 13 12]


'''-------------------------------------------'''
'''                Seaborn Module             '''
'''-------------------------------------------'''
#Seaborn is a library that uses Matplotlib underneath
# to plot graphs. It will be used to visualize
# random distributions.

#Plotting a Distplot
# sns.distplot([0, 1, 2, 3, 4, 5]) 
# #this distplot function was deprecated

# use either displot (note, no t) or histplot
#sns.histplot([0, 1, 2, 3, 4, 5])
#plt.show()

'''-------------------------------------------'''
'''             Normal Distribution           '''
'''-------------------------------------------'''
#also called the Gaussian Distribution

# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:
    # loc - (Mean) where the peak of the bell exists.
    # scale - (Standard Deviation) how flat the graph distribution
    #  should be.
    # size - The shape of the returned array.


#Generate a random normal distribution of size 2x3
x = random.normal(size=(2, 3))
print(x)
# [[ 0.83680311 -0.35334149  1.37038344]
#  [-0.37580914 -0.01300845 -0.59813139]]

#Generate a random normal distribution of size 2x3
#  with mean at 1 and standard deviation of 2
x = random.normal(loc=3, scale=2, size=(2, 3))
print(x)
# [[3.71697472 2.23212999 2.50407707]
#  [0.5066488  3.52106765 3.69046858]]

# sns.distplot(random.normal(size=1000), hist=False)
# plt.show()

'''-------------------------------------------'''
'''           Binomial Distribution           '''
'''-------------------------------------------'''
# Binomial Distribution is a Discrete Distribution.

# It describes the outcome of binary scenarios, e.g. toss
# of a coin, it will either be head or tails.

# It has three parameters:

    # n - number of trials.
    # p - probability of occurence of each trial (e.g. for toss
    #     of a coin 0.5 each).
    # size - The shape of the returned array.

x = random.binomial(n=10, p=0.5, size=10)

print(x)
#Given 10 trials for coin toss generate 10 data points
# [6 4 4 5 4 4 5 5 3 4]

'''-------------------------------------------'''
'''            Poisson Distribution           '''
'''-------------------------------------------'''
# Poisson Distribution is a Discrete Distribution (it has its own space).
# It estimates how many times an event can happen in a
#  specified time. e.g. If someone eats twice a day what
#  is the probability he will eat thrice?

# It has two parameters:
    # lam - rate or known number of occurrences e.g. 2
    #       for above problem.
    # size - The shape of the returned array.


x = random.poisson(lam=2, size=10)
print(x)


'''-------------------------------------------'''
'''            Uniform Distribution           '''
'''-------------------------------------------'''

# Used to describe probability where every event
#  has equal chances of occuring.
# E.g. Generation of random numbers.

# It has three parameters:

    # a - lower bound - default 0 .0.
    # b - upper bound - default 1.0.
    # size - The shape of the returned array.

x = random.uniform(size=(2, 3))
print(x)

# sns.distplot(random.uniform(size=1000), hist=False)

# plt.show()

'''-------------------------------------------'''
'''           Logistic Distribution           '''
'''-------------------------------------------'''
# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:
    # loc - mean, where the peak is. Default 0.
    # scale - standard deviation, the flatness
    #  of distribution. Default 1.
    # size - The shape of the returned array.

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# sns.distplot(random.logistic(size=1000), hist=False)
# plt.show()
'''-------------------------------------------'''
'''         Multinomial Distribution          '''
'''-------------------------------------------'''
# Multinomial distribution is a generalization of binomial
#  distribution.

# It describes outcomes of multi-nomial scenarios unlike
#  binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

# It has three parameters:
    # n - number of possible outcomes (e.g. 6 for dice roll).
    # pvals - list of probabilties of outcomes
    #       (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
    # size - The shape of the returned array.

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
# [0 1 0 1 2 2]
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


