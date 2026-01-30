# Write a function to display all "n" narcissistic number. 
# for ex: 153 is a 3 narcissist number bcz  153 = 1^3 + 5^3 + 3^3.



def Armstrong_num(n,l):
    temp = n
    sum = 0
    for i in range(l):
        rem = temp%10
        sum+= pow(rem,l)
        temp = int(temp/10)
    if sum == n :
        return True
    else :
        return False


n = int(input("Enter a number : \n"))

for i in range(10**(n-1), 10**n):
    if Armstrong_num(i, n):
        print(i)
