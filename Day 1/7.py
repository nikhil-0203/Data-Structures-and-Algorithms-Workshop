n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
n4 = int(input("Enter fourth number : "))
n5 = int(input("Enter fifth number : "))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print(n1, "is greatest")
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(n2, "is greatest")
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(n3, "is greatest")
elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print(n4, "is greatest")
else:
    print(n5, "is greatest")
