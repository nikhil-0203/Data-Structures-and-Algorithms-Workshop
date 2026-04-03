# name = "racear"
#     #012345
# for i in name:  #i=6:r 
#     print(i)

#WAP to remove duplicates

name = "racear"
newname = ""
for i in name:
    if i not in newname:
        newname = newname + i
print(name)
print(newname)


