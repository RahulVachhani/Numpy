# INDEXING IN ARRAY

import numpy as np

# IN 1D ARRAY
n1 = np.array([10,20,30])
print(n1, "DIMENSION :", n1.ndim)
print(n1[0])



# LAST ELEMENT BY NEGETIVE INDEX
print('Last element :',n1[-1])


# IN 2D ARRAY
n2 = np.array([[10,20,30],[40,50,60]])
print(n2, "DIMENSION :", n2.ndim)
# print(n2[0][0])   
print(n2[0,0])   # Both are same but this is most prefer in numpy
print(n2[0,1])
print(n2[1,0])
print(n2[1,2])


print('Last element :',n2[0,-1])
print('Last element :',n2[1,-1])


# IN 3D ARRAY
n3 = np.array([[[10,20,30],[40,50,60]],[[1,2,3],[4,5,6]]])

print(n3)
print('DIMENSION : ',n3.ndim)
print(n3[0,0,0])
print(n3[0,0,1])
print(n3[0,0,2])

print(n3[0,1,0])
print(n3[0,1,1])
print(n3[0,1,2])

print(n3[1,1,0])
print(n3[1,1,1])
print(n3[1,1,2])


print('Last element :',n3[0,0,-1])
print('Last element :',n3[1,1,-1])