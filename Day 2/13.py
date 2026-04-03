name = "Nikhil*is*a*good*programmer"
newname = ""
for i in name:
    if i == "*":
        newname = newname + "*" 
newname = newname + name.replace("*","")
print(name)
print(newname)
