WAP to accept physics, chemistry and maths marks of a student and calculate total and percentage. If percentage is above >=60 then print "Distinction", if percentage is gretter then eqaul to 60 and gender is equal to male so he is eligible for placement else eligible for data entry job.
phy = int(input("Enter physics marks : "))
chem = int(input("Enter chemistry marks : "))
maths = int(input("Enter maths marks : "))
gender = input("Enter gender : ")
total = phy + chem + maths
percentage = total/3.0 
print("Total marks =", total)
print("Percentage =", percentage)
if percentage >= 60:
    print("Eligible for placement")
elif percentage >= 60 and gender == "male":
    print("Eligible for placement")
else:
    print("Eligible for data entry job")
