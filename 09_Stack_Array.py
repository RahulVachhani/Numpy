
# JOINING ARRAYS USING STACK WHICH IS USED TO JOIN WITH NEW AXIS

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.stack((arr1, arr2), axis=0)  # Stack along new axis (rows)
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]

result = np.stack((arr1, arr2), axis=1)  # Stack along new axis (columns)
print(result)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
