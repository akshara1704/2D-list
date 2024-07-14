m1=[]
row=2
column=2
for i in range(0, row):
    a = []
    for j in range(0, column):
        num = int(input("Enter no="))
        a.append(num)
    m1.append(a)
print(m1)
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        print(m1[i][j],end=" ")
    print()