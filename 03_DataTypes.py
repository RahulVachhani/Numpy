# DATA TYEPS IN NUMPY

import numpy as np

# INT
n1 = np.array([10,20,30])
print(n1.dtype)    # int64


# STRING
n2 = np.array(["Rahul","Jainil","Mohit"])
print(n2.dtype)   # <U6    <-- this means jainil have six character with highest character so U6



n3 = np.array(["Rahul","Jainil","Mohit"],dtype='S5')  # The dtype='S5' specifies that the string length for each element is limited to 5 bytes.
print(n3.dtype)  # |S5


# BOOL
arr = np.array([True, False, True])
print(arr)
print(arr.dtype)



# TYPE CONVERTSION USING  "astype()"
n4 = np.array(['10','20','30','40'])
print(n4)
print(n4.dtype)   # U2

n5  = n4.astype('i')
print(n5)
print(n5.dtype)   # int32
