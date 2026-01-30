def GCD(x,y):
    if x < 0 or y < 0:
        return -1
    while(y):
        x, y = y, x%y 
    return x

r = int(input("Enter the value of r : "))
n = int(input("Enter the value of n : "))

if GCD(r,n) == 1 :
    i = 1
    while (r**i % n != 1):
        i += 1
    print("The answer is : ",i)
else :
    print("NOT DEFINED")