import numpy as np

# Question is at matrix.png
a = np.genfromtxt('q2.txt', delimiter= ',')
a = a.astype('int')
print(a)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]
 [26 27 28 29 30]]
'''
#blue
print(a[2:4,0:2])
'''
[[11 12]
 [16 17]]
'''

#try
print(a[0:4, 1:5])
# [[ 2  3  4  5]
#  [ 7  8  9 10]
#  [12 13 14 15]
#  [17 18 19 20]]

#green
print(a[[0,1,2,3],[1,2,3,4]])
#[ 2  8 14 20]

#red
print(a[[0,4,5], 3:])
# [[ 4  5]
#  [24 25]
#  [29 30]]