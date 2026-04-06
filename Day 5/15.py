#method overriding (parent and child relationship must be there)
class Rbi:
    def home_loan(self):
        print("home loan")
    def car_loan(self):
        print("car loan")

class Sbi(Rbi):
    def home_loan(self):
        print("SBI home loan=6.5")
        super().home_loan()
obj = Sbi()
obj.home_loan()
obj.car_loan()