# SHAPE IN NUMPY

import numpy as np


# 0D ARRAY
n1 = np.array(10)
print(n1.ndim)
print(n1.shape)  # () 

 
# 1D ARRAY
n2 = np.array([10,20,30,40])
print(n2.ndim)
print(n2.shape) # (4,) <-- in array have 4 element


# 2D ARRAY
# 2 x 3 matrix
n3 = np.array([[10,20,30],[40,50,60]])
print(n3.ndim)
print(n3.shape) # (2, 3)



# 3D ARRAY
# 2 x 2 x 3 matrix
n4 = np.array([[[10,20,30],[40,50,60]],[[1,2,3],[4,5,6]]])
print(n4.ndim)
print(n4.shape) # (2, 2, 3)