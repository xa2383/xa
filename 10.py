import numpy as np
npArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9] , dtype=float)
print('Contents of the Array : ', npArray)
print('Type of the Array : ', npArray.dtype)


import numpy as np
a = np.zeros([3, 4], dtype=int)
print("\nMatrix a : \n", a)

import numpy as np
npArray = np.array( (11,22,33,44,55,66,77,88 ) )
print(npArray)


import numpy as np
# if the shape is not mentioned the output will just be a random integer in the given range
rand_int1 = np.random.randint(5,10)
print("First array", rand_int1)
rand_int2 = np.random.randint(10,90,(4,5)) # random numpy array of shape (4,5)
print("Second array ", rand_int2)


