# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])


# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 13
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)


# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])


# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))

# rec = {'Name': 'John', 'Age': 30, 'City': 'New York'}
# r = rec.copy()
# print(id(r))
# print(id(rec))
# print(id(r)== id(rec)) #False

# id1 = id(r)
# del rec 
# rec = {'Name': 'John', 'Age': 30, 'City': 'New York'}
# id2 = id(rec)
# print(id1 == id2) #False
