# mylist = [['Nikhil','Fendre'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list")
# print(mylist)
# #print(mylist[row][column])
# print(mylist[0][0]) #Nikhil
# print(mylist[0][1]) #Fendre
# print(mylist[1][0]) #85.56
# print(mylist[2][0]) #440022
# print(mylist[2][1]) #yyy

# list2 = [50,25.50,"Nikhil"]
# del list2[2]
# del list2
# print(list2) #NameError: name 'list2' is not defined

#sorting example
# mylist = [50,25.50,77,60.52]
# mylist.sort() #TypeError: '<' not supported between instances of 'str' and 'float'
# print(mylist)


mylist = [50,25.50,77,60.52]
newlist = mylist
print(id(mylist))
print(id(newlist))
mylist[0]= "Nikhil"
print(mylist)
print(newlist)