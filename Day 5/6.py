class New:
    a = 10

    def __init__(self):
        self.name = "nikhil"

obj1 = New()
obj2 = New()
obj3 = New()

print(obj1.a)
print(obj2.a)
print(obj3.a)

obj1.a = 50

print(obj1.a)
print(obj2.a)
print(obj3.a)