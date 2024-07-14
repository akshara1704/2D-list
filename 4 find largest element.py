#Program to find the largest element from 2D list or Matrix (for square matrices only)

arr=[[1,2,3],
     [5,9,0],
     [7,8,66]
    ]

max_num=arr[0][0]
row=len(arr)
column=len(arr[0])

for i in range(0,row):
     for j in range(0,column):
          if arr[i][j] > max_num:
               max_num=arr[i][j]

print(f'maximum no from 2D list is {max_num}')

