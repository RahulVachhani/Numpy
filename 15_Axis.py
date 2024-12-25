
# USED OF AXIS 
 
# axis = 0  --> vertically   --> row
# axis = 1 --> horizontally  --> column

# axis=0 → Vertically → Row-wise operations affecting columns.
# axis=1 → Horizontally → Column-wise operations affecting rows.

import numpy as np

n1 = np.array([[1,2,3,4],[10,20,30,40],[50,60,70,80]])

print(n1)

print('Minimum value :',n1.min())

print('Minimum value with axis 0 (vertical axes) = ', n1.min(axis=0))  
print('Minimum value with axis 1 (horizontal axes) = ', n1.min(axis=1))
