def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
def bino(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
n = int(input("Enter the value of n"))
k = int(input("Enter the value of k"))
print(factorial(n))
print(bino(n,k))