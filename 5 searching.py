l1=[
    [76,2,7,8],
    [115,70,5,1],
    [1018,19,57,1],
    [10,1,7,120]
]
for i in range(0,len(l1)):
    for j in range(0,len(l1[i])):
        if l1[i][j]==1018:
            print(l1[i][j],"is found at",i,",",j,"index")
