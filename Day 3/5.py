#How many type of argument we can pass in function
# 1. Positional argument
# 2. Keyword argument
# 3. Default argument
# 4. Variable length argument


# #positional argument
# def login(username, password):
#     if username == password:
#         print("login successful")
#     else:
#         print("invalid credential")

# username = input("Enter username : ")
# password = input("Enter password : ")
# login(username, password)



# #keyword argument
# def login(username, password):
#     if username == password:
#         print("login successful")
#     else:
#         print("invalid credential")

# login(password="admin", username="admin")



# #default argument
# def cityName(city="Delhi"):
#     print(city)

# cityName("Pune")
# cityName("Mumbai")
# cityName()


# #variable length argument / variable number of argument

# def nameOfCitys(*city):
#     print("City Name's=",city)

# nameOfCitys("Delhi","Pune","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad")

