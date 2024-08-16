import numpy as np
arr = np.array([[1, 2, 3, 4],
 [5, 2, 4, 2],
 [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

import numpy as np
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)


import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
flarr = arr.flatten()
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


import numpy as np
d = np.full((3, 3), 5, dtype = 'complex')
print ("\nAn array initialized with all 5s."
"Array type is complex:\n", d)

