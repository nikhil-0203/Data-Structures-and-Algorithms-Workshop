class Principal:
    def role(self):
        print('I am managing all activity of college')
class Dean:
    def role(self):
        print('Dean= I am decision taking person')

class Hod:
    def role(self):
        print('Hod= I have responsibilities of Teachers and students')

class Faculty:
    def role(self):
        print('Faculty= I have to complete Syllabus Successfully')

        # class declaration completee 

def func(obj):
    obj.role()
campus=[Principal(),Dean(),Hod(),Faculty()]
for obj in campus:
    func(obj)