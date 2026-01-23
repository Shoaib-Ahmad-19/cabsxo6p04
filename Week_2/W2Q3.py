# Write a Program to detect whether two numbers are relatively prime or not ?


def GCD(x,y):
    if x < 0 or y < 0:
        return -1
    while(y):
        x, y = y, x%y 
    return x

def is_rel_prime(x,y):
    if GCD(x,y) == 1:
        print("These are Relatively Prime Numbers")
    else :
        print("These are not Relatively Prime Numbers")
    
is_rel_prime(int(input("Enter the First number : \n")), int(input("Enter the Second number : \n")))

    