ch = ord(input("Enter any character : "))
#ord functiion used to cinvert in ASCII code
if ch>=65 and ch<=91:
    print("Character is uppercase")
elif ch>=97 and ch<=122:
    print("Character is lowercase")
elif ch>=48 and ch<=57:
    print("Character is digit")
else:
    print("Character is special symbol")