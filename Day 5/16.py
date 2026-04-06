class Father:
    def car_loan(self):
        print("Father:= I am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("Child:= I will be late for breakfast")

obj = Child()