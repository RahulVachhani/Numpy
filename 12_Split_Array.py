
# SPLIT ARRAY INTO 2 OR MORE PARTS

import numpy as np


# np.split:
# Requires equal splitting: The number of sections must evenly divide the array

n1 = np.array([10,20,30,40,50,60,70,80])

n2 = np.split(n1, indices_or_sections=2)
print(type(n2))
print()

for i in n2:
    print(i)
    print(type(i))
    print(f'Dimension : {i.ndim}')




# np.array_split : 
# Allows unequal splitting: If the array size cannot be evenly divided by the number of sections, it will create sub-arrays of unequal sizes.

n1 = np.array([10,20,30,40,50,60,70])

n2 = np.array_split(n1, indices_or_sections=2)
print(type(n2))
print()

for i in n2:
    print(i)



# 2D ARRAY 
n1 = np.array([[10,20,30],[40,50,60]])

n2 = np.array_split(n1, indices_or_sections=2)  # THIS IS ACCESS AS INDIVIDUAL AS IT IS 2D ARRAY 
print(n2)
print()

for i in n2:
    print(i)





