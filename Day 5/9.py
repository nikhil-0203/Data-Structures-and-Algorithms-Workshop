class Student:
    @staticmethod
    def get_personal_details(firstname,lastname):
        print("your personal details are:",firstname,lastname)

    @staticmethod
    def contact_details(mob,rollno):
        print("your contact details are:",mob,rollno)

Student.get_personal_details("Nikhil","Fendre")
Student.contact_details(1234567890,101)