class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentId = []
        self.studentName = []
        self.studentMarks = []
        self.studentRollNo = []
        self.studentMobileNo = []

    def addStudent(self):
        self.studentId.append(input("Enter studentId: "))
        self.studentName.append(input("Enter studentName: "))
        self.studentMarks.append(input("Enter studentMarks: "))
        self.studentRollNo.append(input("Enter studentRollNo: "))
        self.studentMobileNo.append(input("Enter studentMobileNo: "))
        print("Student Added Successfully ✅")

    def display(self):
        print("\n--- Student Records ---")
        for i in range(len(self.studentId)):
            print(f"\nStudent {i+1}")
            print("ID:", self.studentId[i])
            print("Name:", self.studentName[i])
            print("Marks:", self.studentMarks[i])
            print("Roll No:", self.studentRollNo[i])
            print("Mobile No:", self.studentMobileNo[i])

    def deleteStudent(self):
        sid = input("Enter studentId to delete: ")
        if sid in self.studentId:
            index = self.studentId.index(sid)
            self.studentId.pop(index)
            self.studentName.pop(index)
            self.studentMarks.pop(index)
            self.studentRollNo.pop(index)
            self.studentMobileNo.pop(index)
            print("Student Deleted ❌")
        else:
            print("Student not found")

    def updateStudent(self):
        sid = input("Enter studentId to update: ")
        if sid in self.studentId:
            index = self.studentId.index(sid)
            self.studentName[index] = input("Enter new Name: ")
            self.studentMarks[index] = input("Enter new Marks: ")
            self.studentRollNo[index] = input("Enter new Roll No: ")
            self.studentMobileNo[index] = input("Enter new Mobile No: ")
            print("Student Updated 🔄")
        else:
            print("Student not found")


# ===== MENU =====
obj = CRUD()

while True:
    print("\n1.Add Student")
    print("2.Display Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        obj.addStudent()
    elif choice == "2":
        obj.display()   
    elif choice == "3":
        obj.updateStudent()
    elif choice == "4":
        obj.deleteStudent()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice ")