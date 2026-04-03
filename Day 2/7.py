#write a program to check if the given string is a palindrome
name = "Nikhil"
print(name)
print(name[::-1])
if name == name[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
