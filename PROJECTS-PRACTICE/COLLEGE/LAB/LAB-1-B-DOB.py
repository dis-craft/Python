import datetime
name = input("Enter your name")
yob = int(input("Enter your year of birth"))
current_year = datetime.datetime.now().year
age = current_year - yob
if age>= 60:
    print("senior")
else: 
    print("u good")