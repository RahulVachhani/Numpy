
# VSTACK IN NUMPY USED FOR  Vertical Stacking

import numpy as np

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]



# 2D ARRAY

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = np.vstack((arr1, arr2))
print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
