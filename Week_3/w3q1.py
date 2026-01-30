def check2K(n):
    result = False
    for i in range (n):
        if 2**i == n:
            result = True 
            break
        elif 2**i > n :
            break
        
    return result

n = int(input("Enter a number : "))

if check2K(n):
   print("It's in the form 2^k")     
else:
   print("It's not in the form 2^k")     
