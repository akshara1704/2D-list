l1=[[1,2],[3,4]]
l2=[[4,5],[6,7]]
l3=[]
for i in range(0,len(l1)):
    a=[]
    for j in range(0,len(l1[i])):
        a.append(l1[i][j]+l2[i][j])
    l3.append(a)
for i in range(0,len(l3)):
    print(l3[i])