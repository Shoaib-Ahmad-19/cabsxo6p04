def Armstrong_num(n,l):
    temp = n
    sum = 0
    for i in range(l):
        rem = temp%10
        sum+= pow(rem,l)
        temp = int(temp/10)
    if sum == n :
        print("It's an Armstrong Number")
    else :
        print("It's not an Armstrong Number")


n = input("Enter a number : \n")
Armstrong_num(int(n), len(n))
