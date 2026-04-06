# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))
# try:
#     print(n1/n2)
# except:
#     print("Cannot divide by zero")
# print("To be continued")

#-------------------------------------------------------------------------

# try:
#     n1 = int(input("Enter first number : "))
#     n2 = int(input("Enter second number : "))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# expect ValueError:
#     print("Enter only integer value :")

# print("To be continued")


#-------------------------------------------------------------------------

# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter only integer value :", message)
# except:
#     print("this is default part of except vlock")

# print("To be continued")


#-------------------------------------------------------------------------

# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter only integer value :", message)
# finally:
#     print("To be continued")


#-------------------------------------------------------------------------

#nested try expect block
# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as message:
#         print("Cannot divide by zero")
# except ValueError as message:
#     print("Enter only integer value :", message)


#-------------------------------------------------------------------------

# data = input()
# freq = {}

# for d in data:
#     freq[d] = freq.get(d, 0) + 1

# count = sum(1 for v in freq.values() if v > 1)

# print(count if count > 0 else -1)


#-------------------------------------------------------------------------

