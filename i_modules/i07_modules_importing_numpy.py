# pip install numpy

import numpy as np

num_range = np.arange(16)

print(num_range)  # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

num2 = num_range.reshape(4, 4)  # 4x4 - 8x2 - 2x8
print(num2)
"""
array
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
 """