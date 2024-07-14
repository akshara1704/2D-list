#Part 2
#intializing 2D list

m1 = [[0,1],[0,3],[5,6]] # it is an matrix

m2 = [[0,1,8],[0,3],[5,6,9,9]] # it is not an matrix
#becoz m2 have different no. of columns in each row

#printing m1
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        print(m1[i][j],end=" ")
    print()
