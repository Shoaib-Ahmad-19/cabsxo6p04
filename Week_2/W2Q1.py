# Write a program to detect whether a number is prime or Not.

def prime_num(n):
    check = True
    for i in range (2, int(n/2)+1):
        if n %i == 0 :
            check = False
            break
    
    return check  

if prime_num(n = int(input("Enter a number : \n"))):
    print("It's a Prime number")
else:
    print("It's not a Prime NUmber") 