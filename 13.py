import numpy as np
arr = np.arange(10)
print(arr)
out = np.where(arr%2==1,-1,arr)
print(out)

import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
position=np.where(a == b)
print(position)


import numpy as np
np.random.seed(100)
arr = np.random.randint(1,11,size=(6, 10))
print(arr)
def counts_of_all_values_rowwise(arr2d):
 num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]
 return([[int(b[a==i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array])
counts_of_all_values_rowwise(arr)



