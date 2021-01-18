import numpy as np
a = np.array([[1,2,30],[10,15,4]]) 
b = np.array([[1,2,3],[12,19,29]])
print("Arrays vertically concatenated\n", np.vstack((a,b)))
print("Arrays horizontally concatenated\n", np.hstack((a,b)))
