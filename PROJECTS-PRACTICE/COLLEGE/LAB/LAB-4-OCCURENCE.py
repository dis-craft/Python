n = int(input("Enter a number"))
print("Digit \t occurence")

for i in range(0,10):
    count = 0
    temp = n
    while(temp>0):
        a = temp%10
        if(a==i):
            count+=1
        temp = temp//10
    if count>0:
        print(i,"\t", count)