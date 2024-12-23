
# HSTACK IN NUMPY FOR JOINING OF ARRAYS

# Combines arrays horizontally (along columns).

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.hstack((arr1, arr2))
print(result)  # Output: [1 2 3 4 5 6]



n1 = np.array([[10,20,30],[40,50,60]])
print('Dimension :',n1.ndim)

n2 = np.array([[1,2,3],[4,5,6]])

n3 = np.hstack((n1,n2))
print(n3)