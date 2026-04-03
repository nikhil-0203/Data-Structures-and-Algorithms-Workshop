# name = [4,2,5,6,8,2]
# for i in name :
#     print(i)

# remove duplicates values of sample input
# name = [1,2,2,3,4,4,5]
# newname = []
# for i in name:
#     if i not in newname:
#         newname.append(i)
# print(name)
# print(newname)

# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)




#zip() inside we can take multiple range function
for i,j in zip(range(1,11),range(11,21)):
    print(i, "\t", j)
