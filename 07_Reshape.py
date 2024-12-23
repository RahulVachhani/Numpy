# RESHAPE IN NUMPY

# THIS IS USED TO CONVERT 1D ARRAY TO 2D ARRAY OR ND ARRAY TO ND ARRAY

import numpy as np


# 1D ARRAY TO 2D ARRAY

n1 = np.array([10,20,30,40,50,60])
print('Dimension :',n1.ndim)

n2 = n1.reshape(2, 3)
print(n2)
print(n2.ndim)




# 2D ARRAY TO 1D ARRAY

n3  = np.array([[10,20,30],[40,50,60]])
print(n3)
print('Dimension :',n3.ndim)


n4 = n3.reshape(-1)
print(n4)
print('Dimension :',n4.ndim)
