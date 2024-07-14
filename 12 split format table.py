a=input("enter number= ")
result=a.split(" ")
for i in result:
    print("table of",i,"is")
    for j in range(1,11):
        print(int(i),"*",j,"=",int(i)*int(j))
    print()