#Nested for loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()


# import time
# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)


import time
n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        time.sleep(0.0000000000000000000001)
        print(chr(64+j),end=" ")
    print()