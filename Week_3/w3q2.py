def prime_num(n):
    check = True
    for i in range (2, int(n/2)+1):
        if n %i == 0 :
            check = False
            break
    
    return check

def check2K(n):
    result = False
    for i in range (n):
        if 2**i == n:
            result = True 
            break
        elif 2**i > n :
            break
    return result

n = int(input("Enter a Number : "))

if prime_num(n) :
    if prime_num(check2K(n+1)):
        print("Yes, It's a Mersenne Prime number")
    else :
        print("No, It's not a Mersenne Prime number")
else :
    print("No, It's not a Mersenne Prime number")