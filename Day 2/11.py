# a = [1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)


# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50
# print(a)

# a = [1,2,3,4,5]
# print(a[3:0:-1])


# mytuple = ("Nikhil", "Rohit", "Satyarth", "Shivam", "Satyarth", "Shivam","Harshad",23,3.15,77,"Rohit")
# print(mytuple)
# print(type(mytuple))



# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1','2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b)

init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))