class Arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("Invalid")

obj = Arithmatic()
obj.add(10,20)
obj.add(10,20,30)
obj.add(10) 