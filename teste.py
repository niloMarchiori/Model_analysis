import numpy as np

a=np.array([1,2,3,5,6])
b=np.array([1,2,3,4,5])*(-1)
mask=a>3
a[mask]=b[mask]
print(a)