class Student:
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
        self.subjects = []
        self.total = 0
        self.percentage = 0
    def get_marks(self):
        for i in range(3):
            subject_marks = int(input(f"Enter the marks of subjects"))
            self.subjects.append(subject_marks)
            self.total += subject_marks
    def display(self):
        self.percentage = self.total/3
        print("Name: ", self.name)
        print("USN: ", self.usn)
        print("marks: ", self.subjects)
        print("total marks: ", self.total)
        print(f"Percentage : {self.percentage:.2f}%")
name = input("Enter your name")
usn = input("Enter your usn")
stud = Student(name,usn)
stud.get_marks()
stud.display()            