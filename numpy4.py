import numpy as np


# we want to create this
'''
[[1 1 1 1 1]
[1 0 0 0 1]
[1 0 9 0 1]
[1 0 0 0 1]
[1 1 1 1 1]]

'''
#start with making everything ones
output = np.ones((5,5))
print(output)

'''
 [[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]

'''

#create zeros matrix
z = np.zeros((3,3))
print(z)

'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

#change the middle value in z
z[1,1] = 9
print(z)
'''
[[0. 0. 0.]
 [0. 9. 0.]
 [0. 0. 0.]]
'''

#insert zeros to output matrix
output[1:4,1:4]=z
print(output)
'''
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
'''



