import math
def mean(data):
    n = len(data)
    mean = sum(data)/n
    return mean
def variance(data):
    n = len(data)
    deviation = [(x-mean(data))**2 for x in data]
    variance = sum(deviation)/n
    return variance
def stddev(data):
    var = variance(data)
    return math.sqrt(var)
listA = []
n = int(input("Enter the number of elements"))
for i in range(0,n):
    ele = int(input(f"Enter element {i}"))
    listA.append(ele)
data = listA
print(mean(data))
print(variance(data))
print(stddev(data))