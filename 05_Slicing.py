# SLICING IN ARRAY

import numpy as np

# IN THIS SLICE ARE SAME AS LIST
n1 = np.array([10,20,30])
print(n1[0:2])
print(n1[1:])



# IN 2D ARRAY
n2 = np.array([[10,20,30,40]])
print('Dimension : ',n2.ndim)
print(n2[0,1:3])
print(n2[0,:3])




n3 = np.array([[10,20,30,40],[50,60,70,80]])
print('Dimension : ',n3.ndim)

# SLICE IN BOTH 
print(n3[0:2,1:3])

print(n3[0:2,:3].ndim)

