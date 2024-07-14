l=[
    [2,7,8],
    [9,5,1]
]
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if l[i][j] %2 !=0:
            print(l[i][j],end=" ")
