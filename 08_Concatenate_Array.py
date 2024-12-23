# JOIN TWO ARRAY USING  "concatenate()"

import numpy as np


n1 = np.array([10,20,30])
n2 = np.array([40,50,60])

print('\nn1 array elements :')
for i in n1:
    print(i)

print('\nn2 array elements :')
for i in n2:
    print(i)


n3 = np.concatenate((n1,n2))
print('After concatenate :',n3)