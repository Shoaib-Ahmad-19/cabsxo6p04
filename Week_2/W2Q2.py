# Write a function to compute GCD of two integers.

def GCD(x,y):
    if x < 0 or y < 0:
        return -1
    while(y):
        x, y = y, x%y 
    return x

x,y = int(input("Enter the First number : \n")), int(input("Enter the Second number : \n"))
print(f"The GCD of {x} and {y} is {GCD(x,y)}")
    