#strings:
first_name = "Srikar"
food = "Healthy"
email = "mrsrikart@gmail.com"

#integers:
age = 19
quantity = 3 

#float: 
price = 10.99

#boolean
is_student = True
for_sale = False
is_online = True



print(f"Hello, {first_name}") #notice automatic line skip?
print("") #currently this is how i think manually it can be done.
print(f"You like {food} food") #{this is called placeholder}
print(f"your email is: {email}")
print(f"Your age is {age}")
print(f"The price is ${price}")
print(f"Are you a student: {is_student}")

if is_student:
    print("Yayy you are a student!")
else:
    print("You are not a student")
    

if for_sale:
    print("it is for sale!")
else:
    print("not for sale!")
    

if (is_online):
    print("you are online!")
else: 
    print("You are offline!")
    
    
    
#Practice variables:

# 1num = 23 not allowed

Name = "Srikar"
USN = "1MJ24EA048"
Sec = "L"
is_workhard = True
print(Sec)

A = 2
B = 2 + A
C = 3 + A
print(C)

First_name = "Srikar"
Last_name = " T"

Full_name = First_name + Last_name
print(Full_name)