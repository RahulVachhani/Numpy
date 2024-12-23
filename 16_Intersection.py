# INTERSECTION IN ARRAYS

import numpy as np

n1 = np.array([10,40,30,60,20])
n2 = np.array([40,50,70,20,10])

print('Commen element in both array are  :',np.intersect1d(n1,n2))  # output is always sorted
