# for i in range(5,0,-1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)


#WAP to reverse a string using for loop
# name = "Nikhil"
# newname = ""
# for i in name:
#     newname = i + newname
# print(name)
# print(newname)



name = "Nikhil"
newname = ""
n = len(name)
for i in range(n-1,-1,-1):
    newname = newname + name[i]
print(name)
print(newname)