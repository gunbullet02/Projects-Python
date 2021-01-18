import numpy as np
d = np.dtype([('Salary', np.float)])
arr = np.array([(10000.12,),(20000.50,)],dtype=d)
print(arr['Salary'])
