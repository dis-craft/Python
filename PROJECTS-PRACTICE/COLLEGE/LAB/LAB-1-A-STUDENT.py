USN = input("Enter USN")
Name = input("Enter NAME")
print("Enter marks of 3 subjects")
marks = []
for i in range(3):
    m = int(input("Enter the marks: "))
    marks.append(m)
print(marks)
total = sum(marks)
per = int(100*total)/300
print(USN,Name,total,per)