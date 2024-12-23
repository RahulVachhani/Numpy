
# DIFFERENCE BETWEEN TWO ARRAYS

import numpy as np

n1 = np.array([10,20,30,40,50])
n2 = np.array([70,20,60,30,90])


n3 = np.setdiff1d(n1,n2)   # its like (n1 - n2)   <-- remove element from n1 which is also in n2 and return remaining n1 elements
print('Difference :',n3)


n4 = np.setdiff1d(n2,n1)
print('Difference :',n4)

