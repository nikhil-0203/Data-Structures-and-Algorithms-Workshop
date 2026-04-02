#nested if else: #WAP to accept value of A,B,C and find max value
A = int(input("Enter value of A : "))
B = int(input("Enter value of B : "))
C = int(input("Enter value of C : "))
if A>B:
    if A>C:
        print("A is greatest")
    else:
        print("C is greatest")
else:
    if B>C:
        print("B is greatest")
    else:
        print("C is greatest")
