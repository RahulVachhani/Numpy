
# ARITHMETIC OPERATION IN ARRAY 

import numpy as np

# ADDITION

n1 = np.array([10,20,30,40])
n2 = np.array([20,30,40,60])

sum = np.sum((n1,n2))
print('Sum is :',sum)



n3 = np.array([10,20,30])
n4 = np.array([40,50,60])

sum = np.sum([n3,n4],axis=1 )
print('sum is :',sum)



# SUBSTRACTION

n5 = np.array([10,20,30])
n6 = np.array([40,50,60])

substract = np.subtract(n5,n6)
print('substract is :',substract)



# MULTIPLICATION

n7 = np.array([10,20,30])
n8 = np.array([20,40,60])

multiply = np.multiply(n7,n8)
print('Multiply is :',multiply)



# DIVISION

n9 = np.array([20,30,40])
n10 = np.array([10,10,10])

divide = np.divide(n9,n10)
print('Division is :',divide)