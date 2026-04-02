# val1 = int(input("Enter value of val1 : "))
# val2 = int(input("Enter value of val2 : "))
# print("Before swapping val1 =", val1, "and val2 =", val2)
# temp = val1 # temp = 100
# val1 = val2 # val1 = 200
# val2 = temp # val2 = 20
# print("After swapping val1 =", val1, "and val2 =", val2)



# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b : "))
# a = a + b # a = 100 + 200 = 300
# b = a - b # b = 300 - 200 = 100
# a = a - b # a = 300 - 100 = 200
# print(a,b)




# p1 = int(input("Enter the marks of p1 : "))
# p2 = int(input("Enter the marks of p2 : "))
# p3 = int(input("Enter the marks of p3 : "))
# total = p1 + p2 + p3
# percentage = total/3.0
# print("Total marks =", total)
# print("Percentage =", percentage)


# p_amount = int(input("Enter principal amount : "))
# roi = float(input("Enter rate of interest : "))
# time = int(input("Enter duration of loan amount : "))
# si = (p_amount * roi * time)/100
# print("Simple interest =", si)




# height = float(input("enter height of user in feet : "))
# inch = height*12
# cm = inch * 2.54
# print(inch=", inch)")
# print("centimeter=", cm)


# num = 123
# a = num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a*100 + b*10 + c*1
# print("Reverse of 123 is", rev)


# a = 10
# b = 15
# print(a is b) # False
# print(a is not b) # True

# name = "Nikhil"
# print("z"not in name) # True
# print("N" in name) # True
 



# no = int(input("Enter any one number : "))
# if no>0:
#     print("Number is positive")
# if no<0:
#     print("Number is negative")
# if no==0:
#     print("Number is zero")



# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))
# n3 = int(input("Enter third number : "))
# n4 = int(input("Enter fourth number : "))
# n5 = int(input("Enter fifth number : "))
# if n1>n2 and n1>n3 and n1>n4 and n1>n5:
#     print(n1, "is greatest")
# elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
#     print(n2, "is greatest")
# elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
#     print(n3, "is greatest")
# elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
#     print(n4, "is greatest")
# else:
#     print(n5, "is greatest")



# username = input("Enter username : ")
# password = input("Enter password : ")
# if username == password:
#     print("login successful")
# else:
#     print("invalid credential")


#WAP to accept physics, chemistry and maths marks of a student and calculate total and percentage. If percentage is above >=60 then print "Distinction", if percentage is gretter then eqaul to 60 and gender is equal to male so he is eligible for placement else eligible for data entry job.
# phy = int(input("Enter physics marks : "))
# chem = int(input("Enter chemistry marks : "))
# maths = int(input("Enter maths marks : "))
# gender = input("Enter gender : ")
# total = phy + chem + maths
# percentage = total/3.0 
# print("Total marks =", total)
# print("Percentage =", percentage)
# if percentage >= 60:
#     print("Eligible for placement")
# elif percentage >= 60 and gender == "male":
#     print("Eligible for placement")
# else:
#     print("Eligible for data entry job")


#nested if else: #WAP to accept value of A,B,C and find max value
# A = int(input("Enter value of A : "))
# B = int(input("Enter value of B : "))
# C = int(input("Enter value of C : "))
# if A>B:
#     if A>C:
#         print("A is greatest")
#     else:
#         print("C is greatest")
# else:
#     if B>C:
#         print("B is greatest")
#     else:
#         print("C is greatest")




#write days in input and if input is saturday or sunday then print "Holiday" else print "Working day"
# day = input("Enter day : ")
# if day == "saturday" or day == "sunday":
#     print("Holiday")
# else:    print("Working day")