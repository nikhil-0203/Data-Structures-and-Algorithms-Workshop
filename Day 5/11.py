class SubjectMark:
    math = int(input("Enter paper marks of maths :"))
    DE = int(input("Enter paper marks of DE :"))
    C = int(input("Enter paper marks of C :"))
    english = int(input("Enter paper marks of english :"))

    #===========================parent class -1

class PractMarks:
    cpract = int(input("Enter practical marks of C :"))

    #===========================parent class -2

class Result(SubjectMark,PractMarks):
    def total(self):
        if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=40:
            return "pass"
        else:
            return "Fail"
obj = Result()
obj.total()