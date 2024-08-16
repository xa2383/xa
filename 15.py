import pandas as pd
import numpy as np
exam_data = {'name': ['a','b','c', 'd', 'e', 'f','g','h','i','j'],
 'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
 'attempts': [1, 3, np.nan, 3, 2, 3, 1, np.nan, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)


import pandas as pd
import numpy as np
exam_data = {'name': ['a','b','c', 'd', 'e', 'f','g','h','i','j'],
 'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
 'attempts': [1, 3, np.nan, 3, 2, 3, 1, np.nan, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)
print(df.iloc[[1, 3, 5, 6], [1, 3]])

import pandas as pd
import numpy as np
exam_data = {'name': ['a','b','c', 'd', 'e', 'f','g','h','i','j'],
 'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
 'attempts': [1, 3, np.nan, 3, 2, 3, 1, np.nan, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("before renaming\n",df)
print("\nafter renaming\n")
df=df.rename(columns={"name":'hi',"score":"gm","attempts":"how","qualify":"are"})
print(df)

import pandas as pd
import numpy as np
exam_data = {'name': ['a','b','c', 'd', 'e', 'f','g','h','i','j'],
 'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
 'attempts': [1, 3, np.nan, 3, 2, 3, 1, np.nan, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)
print("\nafter droping list of rows\n")
df=df.drop(['a','d','c','b'])
print(df)
