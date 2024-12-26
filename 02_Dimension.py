# N DIMENSION ARRAY IN NUMPY

import numpy as np

# 0D ARRAY
# n1 = np.array(10)
# print(n1)
# print(type(n1))
# print(f'Dimension = {n1.ndim}')


# # 1D ARRAY
# n2 = np.array([10,20,30])
# print(n2)
# print(type(n2))
# print(f'Dimension = {n2.ndim}')


# # 2D ARRAY
# n3 = np.array([[10,20],[30,40]])
# print(n3)
# print(type(n3))
# print(f'Dimension = {n3.ndim}')




# CREATE N DIMENSION ARRAY WITH ZEROS(0)

# 1D ARRAY
n4 = np.zeros([2])
print(n4)
print(type(n4))
print(f'Dimension = {n4.ndim}')

# 2D ARRAY
n5 = np.zeros([2,3])
print(n5)
print(type(n5))
print(f'Dimension = {n5.ndim}')



# INIT ARRAY WITH CUSTOM VALUE
n6 = np.full([2,3],8)   # --> THIS WILL CREATE AN ARRAY OF 2 x 3 WITH VALUE 8
print(n6)


# RANDOM NUMBER OF ARRAY 
n7 = np.random.randint(10,100,(2,3))   # THIS WILL CREATE ARRAY WITH RANDOM VALUE WITH RANGE OF 10 TO 100
print(n7)

# THIS WILL CREATE ARRAY WITH EVENLY SPACED 
n8 = np.linspace(10, 30, 5)
print(n8)


# ARANGE()   --> THIS WILL LIKE GAP 
n9 = np.arange(10,30,6)
print(n9)