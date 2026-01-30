def GCD(x,y):
    if x < 0 or y < 0:
        return -1
    while(y):
        x, y = y, x%y 
    return x

def prime_num(n):
    check = True
    for i in range (2, int(n/2)+1):
        if n %i == 0 :
            check = False
            break
    
    return check 

N = int(input("Enter a number :"))

if prime_num(N) == True :
    print("The Result is : ",N-1)
else:
    result = 0
    for i in range (1, N):
        if GCD(i,N) == 1 :
            result += 1
    print("The result is : ",result)