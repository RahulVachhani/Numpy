
# SEARCH ELEMENT IN ARRAY 

import numpy as np


n1 = np.array([10,20,30,40,30])

res = np.where(n1 == 30)
print(type(res))
print(res)




# EXAMPLE
import numpy as np

arr = np.array([5, 10, 15, 20, 25])

indices = np.where(arr > 10)
print(indices)
# Output: (array([2, 3, 4]),)

# Access the elements directly
result = arr[indices]
print(result)
# Output: [15 20 25]
