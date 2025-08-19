def Divexp(a,b):
    if b==0:
        raise ValueError("Deno cant be 0")
    assert a<0, "Nume shd be positive"
    return a/b
a = float(input("Enter a"))
b = float(input("Enter b"))
try:
    print(f"result is {Divexp(a,b)}")
except ValueError as e:
    print(e) 
