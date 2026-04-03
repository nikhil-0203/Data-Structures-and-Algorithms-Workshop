# arr = [[1, 2, 3, 4],
#        [4, 5,6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]  
# for i in range(0,4):
#     print(arr[i].pop())  


arr = [1, 2, 3, 4,5,6]
for i in range(1,6):
    arr[i-1]= arr[i]
for i in range(0,6):
        print(arr[i],end=" ")
