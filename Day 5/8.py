class Student:
    def __init__(self, name, rollno, mob):
        self.name = name
        self.rollno = rollno
        self.mob = mob

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Mobile No:", self.mob)

stud = Student("Nikhil Fendre", 101, 1234567890)
stud.display()