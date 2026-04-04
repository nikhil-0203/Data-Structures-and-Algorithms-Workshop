def arithmatic():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

# print(arithmatic())
result = arithmatic()
print("Arithmatic = ", result)