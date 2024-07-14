import numpy as np
l1=[[1,2],
    [3,4]]
l2=[[5,6],
    [7,8]]
result=[[0,0],[0,0]]
result=np.dot(l1,l2)
for r in result:
    print(r)