def perfect_num (n):
    sum = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            sum+=i   
    if sum == n:
        return True
    else :
        return False

n = int(input("Enter a number : \n"))

if perfect_num(n):
    print("It's a perfect Number")
else:
    print("It's not a perfect Number")