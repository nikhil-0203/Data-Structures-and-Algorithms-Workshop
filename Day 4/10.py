
# import csv
# f = open("student.csv", "a",newline = "")
# a = csv.writer(f)
# # a.writerow(["studentID","rollno","name","mobileno"])
# studentid = int(input("enter the studentID:"))
# rollno = int(input("enter the rollno:"))
# name = input("enter the name:")
# mobileno = int(input("enter the mobileno:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")


#["rollno","name","mobileno","p1","p2","p3" (you have accept)]

#"total","percentage"(calculate)
#"result"(pass/fail)
#id user is pass in all subjects then result is pass else fail(passing score = 40)

import csv
f = open("student.csv", "a",newline = "")
a = csv.writer(f)
# a.writerow(["studentID","rollno","name","mobileno"])
studentid = int(input("enter the studentID:"))
rollno = int(input("enter the rollno:"))
name = input("enter the name:")
mobileno = int(input("enter the mobileno:"))
p1 = int(input("enter the marks of p1 : "))
p2 = int(input("enter the marks of p2 : "))
p3 = int(input("enter the marks of p3 : "))
total = p1 + p2 + p3
percentage = total/3.0
print("Total marks =", total)
print("Percentage =", percentage)
result = "pass" if percentage >= 40 else "fail"
a.writerow([studentid,rollno,name,mobileno,p1,p2,p3,total,percentage,result])
print("student record has save")