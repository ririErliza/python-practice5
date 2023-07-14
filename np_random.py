import numpy as np

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

