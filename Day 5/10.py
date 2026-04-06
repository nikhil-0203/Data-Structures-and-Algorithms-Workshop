# multilevel inheritance
class Collage:
    def collage_name(self):
        print("modern collage")
        
class Student(Collage):
    def student_info(self):
        print("Name: Nikhil fendre")
        print("Branch:cse")
        
class Exam(Student):
    def subject(self):
        print("subject1: python")
        print("subject2: java")
        print("subject3: c++")
        
obj=Exam()
obj.collage_name()
obj.student_info()
obj.subject()